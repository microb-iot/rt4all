#! /usr/bin/env python
"""

# MX2 MANUALS
* https://industrial.omron.es/es/products/mx2#downloads

TO-DO

* Hay bobinas/registros que no se pueden modificar mienstras esta RUN. Que pasa cuando se modifica una de estas durante RUN?


"""

__author__ = 'Juan Carlos Chaves'
__copyright__ = 'Copyright (C) 2017'
__license__ = 'MIT (expat) License'
__version__ = '0.1'
__maintainer__ = 'Juan Carlos Chaves'
__email__ = 'juan.chaves@whitewallenergy.com'

import struct
from frame import Frame
import mx2
import doctest


import sys
import os

#PATH_MODBUS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + '/ivy_gw/modules/modbus'
PATH_MODBUS = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/ivy_gw/modules/modbus'
sys.path.insert(0, PATH_MODBUS)

import modbus




class Inverter:
    """"""
    def __init__(self, modbus, slave_address=mx2.DEFAULT_SLAVE_ADDRESS, big_endian=mx2.DEFAULT_BIG_ENDIAND):
        self.modbus = modbus
        self.frame = Frame(self.modbus, slave_address, big_endian)

        self.three_phase = mx2.DEFAULT_IS_THREE_PHASE
        self.height_impulse = mx2.DEFAULT_HEIGHT_IMPULSE # meters
        self.water_density = mx2.DEFAULT_DENSITY    # kg/m^3
        self.max_power = mx2.DEFAULT_MAX_POWER        # Watts
        self.flow_at_maximum_power = mx2.DEFAULT_FLOW_AT_MAXIMUM_POWER   # m^3/h

    """ CLASS METHODS """

    def is_run(self):
        """
        returns true if the run command is enabled
        :returns: Status of run.
        :rtype: Bool/None.
        """
        response = self.frame.raw_read_coils(start_address=mx2.COIL_RUN, num_coil=1)
        if response is not None:
            return response[0]

    def is_irdy(self):
        """

        Get if the inverter is operational or not.

        :returns: Status operational of te inverter.
        :rtype: Bool/None.
        """
        response = self.frame.raw_read_coils(start_address=mx2.COIL_IRDY, num_coil=1)
        if response and len(response) > 0:
            return response[0]

    def is_tank_full(self):
        """
        :returns: true if the tank is full, else return false.
        :rtype: Boolean/None.
        """

        is_full = self.read_smart_entries()
        if is_full is not None:
            return is_full[1]

    def read_smart_entries(self):
        """
        Returns a vector of booleans, which contains the state of the intelligent
        inputs, from 1 to 7. In the vector 0 to 6, with 1 in the 0 position of
        the vector and 7 in the position 6.

        :returns: Status of smart inputs.
        :rtype: Boolean Array/None.
        """
        return self.frame.raw_read_coils(start_address=mx2.COIL_RUN_ENTRY, num_coil=7)


    def get_output_current(self):
        """
        Returns the current that is using the pump. [0-65.530]. 0.01 amp resolution.
        If the current is greater than 0, it indicates that the engine is running

        :returns: current that is using the motor in amperes
        :rtype: float/None
        """
        # It is multiplied by 0.01, to obtain the value in amps, since the value returned by the modbus query
        # indicates how many times there are 0.01 amps.
        response = self.frame.raw_read_registers(start_address=mx2.D002, num_register=1, is_double=False)
        if response is not None:
            return response[0]*0.01


    def get_time_run_pump(self):
        """
        Returns the time that the run command is active [hours].

        :returns: time in hours that the run command is active.
        :rtype: interger/None
        """
        response = self.frame.raw_read_registers(start_address=mx2.D016, num_register=1, is_double=True)
        if response and len(response) > 0:
            return response[0]

    def get_time_run_inverter(self):
        """
        Returns the time the inverter has been in use [hours].

        :returns: time in hours that the pump has been in use.
        :rtype: interger/None
        """
        response = self.frame.raw_read_registers(start_address=mx2.D017, num_register=1, is_double=True)
        if response and len(response) > 0:
            return response[0]

    def get_pump_flow(self):
        """
        Returns the flow rate of the pump.
        If the current is 0 then the power and the flow rate is also 0

        :returns: flow rate of the pump in m^3/h.
        :rtype: float/None
        """
        power = self.get_pump_power()
        if power is not None:
            return (power*self.flow_at_maximum_power)/float(self.max_power)

    def get_pump_power(self):
        """
        Returns the instant power consumption of the pump in watts.
        If the current is 0 then the instant power consumption is also 0

        :returns: instant power consumption of the pump in watts.
        :rtype: float/None
        """
        current = self.get_output_current()
        if current is not None:
            if self.three_phase:
                return 400*current
            else:
                return 220*current

    def get_performance(self):
        """
        Returns the instant performance of the pump [%].

        N = pump performance in %.
        Q = Water flow in m^3/h
        H = height of impulse in meters.
        D = water density 1000 kg/m^3 .
        P = power of the pump in watts.

        N = ((Q*H*D)/(367*P))

        :returns: instant performance of the pump [%].
        :rtype: float/None
        """
        pump_flow = self.get_pump_flow()
        if pump_flow is not None:
            return (pump_flow*self.height_impulse*self.water_density)/float(367*self.max_power)
    def get_hertz(self):
        """
        Returns the Output hertz of the inverter

        :returns: Output herts of the inverter
        :rtype: interger/None
        """
        hertz = self.frame.raw_read_registers(start_address=mx2.D001, num_register=1, is_double=True)[0]
        if hertz is not None:
            return herts[0]
    def get_pump_rpm(self):
        """
        Returns the number of revolutions per minute to which the pump rotor rotates

        :returns: RPM of the pump.
        :rtype: interger/None
        """

        hz = get_hertz()
        if hz is not None:
            n_poles = self.get_num_poles()
            if n_poles is not None:
                return (hz*60)/n_poles

    def get_num_poles(self):
        """
        Returns the number of poles that have the pump.

        :returns: number of pump poles.
        :rtype: Integer/None [0, 38] For the query modbus it is required as data (n_poles*2), since 0 = 0, 1 = 2, 2 = 4, ..., 19 = 38
        """
        n_poles = self.frame.raw_read_registers(start_address=mx2.P049, num_register=1, is_double=False)
        if n_poles is not None:
            return n_poles[0]*2

    def set_num_poles(self, n_poles=mx2.DEFAULT_N_POLES):
        """
        Modifies the value of the number of poles of the pump and returns the same value if it has been modified correctly.

        :param n_poles: Number of poles to set.

        :type n_poles: Integer [0, 38] For the query modbus it is passed as data n_poles / 2, since 0 = 0, 1 = 2, 2 = 4, ..., 19 = 38

        :returns: True if set correctly else return flase
        :rtype: integer/None
        """
        request = self.frame.raw_write_registers(start_address=mx2.P049, num_register=1, values = [(n_poles/2)], is_double=False)

        if request is not None:
            return True
        else:
            return False

    def get_input_voltage(self):
        """
        Returns the input voltage of the inverter. [0-10000]. 0.1 Volts resolution.

        :returns: input voltage of the inverter in Volts with 0.1 Volt of resolution
        :rtype: float/None
        """

        voltage = self.frame.raw_read_registers(start_address=mx2.D102,num_register=1,is_double=False)
        if voltage is not None:
            return voltage[0]*0.1

    def get_input_power(self):
        """
        Returns the input power of the inverter. [0-1000]. 0.1 KW resolution.

        :returns: input power of the inverter in Watts with 100 Watts of resolution.
        :rtype: float/None
        """

        power = self.frame.raw_read_registers(start_address=mx2.D014,num_register= 1, is_double=False)
        if power is not None:
            return power[0]*1000

    def get_input_current(self):
        """
        Returns the input current of the inverter.
            As the input power in kilowatts, we passed it to Watts.

        :returns: input current of the inverter in Amps
        :rtype: float/None
        """

        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # Posible error al intentar dividir entre None (self.get_input_voltage())
        # siempre devuelve double ??? Creo que es float
        # Al dividir, mejor devolver float: return a/float(b)
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        input_voltage=self.get_input_voltage()
        if input_voltage is not None and input_voltage > 1:
            return ((self.get_input_power()*1000.0)/input_voltage)

    def get_reference_voltage(self):
        """
        return the reference voltage in volts.

        :returns: reference Voltage in volts.
        :rtype: float/None
        """
        voltage = self.frame.raw_read_registers(start_address=mx2.P102, num_register=1, is_double=False)
        if voltage is not None:
            return voltage[0]/10.0

    def set_reference_voltage(self,voltage=mx2.DEFAULT_REFERENCE_VOLTAGE):
        """
        Modifies the value of reference voltage

        If the DC bus voltage falls below this level, the
        inverter for operation. The march will be resumed when the
        DC bus voltage is above the level and has
        after the time set in P100 (get_security time()).

        :param voltage: voltage to set in Volts.

        :type voltage: interger

        :returns: True if all is correctly
        :rtype: boolean/None
        """


        voltage = voltage*10

        request = self.frame.raw_write_registers(start_address=mx2.P102,num_register=1, values=[voltage], )
        if request==1: # uno porque escribimos 1 registro y es lo que nos va a devolver ras_write_registers(), el numero de registros modificados
            return True
        else:
            return False

    def get_security_time(self):
        """
        Returns the security time.

        Run delay time to avoid continuous starts in moments with
        low irradiance. (Scale: 200 = 2000ms)

        :returns: security time in milliseconds.
        :rtype: float/None
        """


        time = self.frame.raw_read_registers(start_address=mx2.P100, num_register=1, is_double=False)
        if time is not None:
            return 100*(float(time[0]))

    def set_security_time(self,time=mx2.DEFAULT_SECURITY_TIME):
        """
        Modifies the safe start time of the pump, which allows checking that the voltage is constant and not a peak.

        :param time: time to set in milliseconds.

        :type time: interger

        :returns: True if set register correctly
        :rtype: boolean
        """


        time = time/10
        # Con nuevo metodo
        request =  self.frame.raw_write_registers(start_address=mx2.P100, value=[time])
        if request == 1:
            return True
        else:
            return False

    def get_max_voltage(self):
        """
        Returns parameter A020 which is the max voltage in 0.01 Volts of resolution.

        :returns: max voltage in 0.01 Volts of resolution.
        :rtype: float/None
        TO-DO saber que significa realmente esto.
        """


        voltage = self.frame.raw_read_registers(start_address=mx2.A020,num_register=1,is_double=True)
        if voltage is not None:
            return voltage[0]/float(10)

    def set_max_voltage(self, voltage=mx2.DEFAULT_MAX_VOLTAGE):
        """
        Change parameter A020 which is the max voltage in 0.01 Volts of resolution.

        :param voltage: Max voltage in volts.

        :type voltage: interger

        :returns: True if all is correctly
        :rtype: boolean

        TO-DO se modifica, aunque parece que el escalado no es correcto y las definiciones son ambiguas... to-doing.py 5.3
        """
        request = self.frame.raw_write_registers(start_address=mx2.A020, num_register=1, values=[voltage*10], is_double = True, unsigned= False)

        if request i==num_register:
            return True
        else:
            return False


    def get_min_frequency(self):
        """
        Return parameter A062 which is the lower frequency reference limit in 0.01 Hz

        :returns: Lower frequency reference limit (in Hz).
        :rtype: float/None
        """
        frequency = self.frame.raw_read_registers(start_address=mx2.A062,num_register=1,is_double=True)
        if frequency is not None:
            return frequency[0]/float(100)

    def set_min_frequency(self, frequency=mx2.DEFAULT_MIN_FREQUENCY):
        """
        Change parameter A062 which is the lower frequency reference limit in 0.01 Hz

        :param frequency: Lower frequency reference limit (in Hz).

        :type frequency: double

        :returns: True if all is correctly
        :rtype: boolean
        """
        request = self.frame.raw_write_registers(start_address=mx2.A062, values=[(frequency*100)], is_double = True)

        if request == 1:
            return True
        else:
            return False

    def get_max_frequency(self):
        """
        Return parameter A061 which is the max frequency reference limit in 0.01 Hz

        :returns: Max frequency reference limit (in Hz).
        :rtype: float
        """

        frequency = self.frame.raw_read_registers(start_address=mx2.A061,num_register=1,is_double=True)
        if frequency is not None:
            return frequency[0]/100.0


    def set_max_frequency(self, frequency=mx2.DEFAULT_MAX_FREQUENCY):
        """
        Change parameter A061 which is the max frequency reference limit (in Hz).

        :param frequency: Max frequency reference limit (in Hz).

        :type frequency: double

        :returns: True if all is correctly
        :rtype: boolean

        TO-DO por alguna razon la peticion modbus devuelve el codigo de excepcion 01h (otros registros los modifico de la misma manera)
        """

        # Con nuevo metodo
        request = self.frame.raw_write_registers(start_address=mx2.A061, num_register=1, values=[frequency*100], is_double=True)
        #print request
        if request == 1:
            return True
        else :
            return False

    def set_source_run(self, value=mx2.DEFAULT_SOURCE_RUN):
        """
        Change parameter A002 which is the source of the command.

        :param value:
            1 = Control terminal
            2 = RUN key of the keyboard or digital operator
            3 = Red Modbus
            4 = option
        :type value: integer

        :returns: True if all is correctly
        :rtype: boolean
        """

        result = self.frame.raw_write_registers(start_address=mx2.A002, num_register=1, values=[value] , is_double=False)

        if result ==1:
            return True
        else:
            return False

    def get_acceleration_time(self):
        """
        Recommended value 30.0 seconds, this value must be pre-set at first sight,
        the value will be read to Parameter F002.

        :returns: Acceleration time in seconds
        :rtype: float
        """
        time = self.frame.raw_read_multiple_registers(start_address=mx2.F002, num_register=1, is_double=True)
        if time is not None:
            return time[0]/float(100)


    def set_acceleration_time(self, time=30.0):
        """
        Recommended value 30.0 seconds, this value must be pre-set at first sight,
        the value will be send to Parameter F002.

        :param time: Acceleration time in seconds
        :type time: float

        :returns: True if all is correctly
        :rtype: boolean
        """
        result = self.frame.raw_write_single_register(start_address=mx2.F002, value=time)
        if result ==1:
            return True
        else:
            return False


    def getAutoreset(self):
        """"""
        if self.connection:
            tx = self.slave + FN_DIAGNOSTIC + '\x00\x00\xAB\xCD'
            tx += modbus.get_crc(tx, self.big_endian)

            self.connection = tx == modbus.raw(tx)

            return self.connection




if __name__ == '__main__':


    i = Inverter(modbus.Modbus())
    doctest.testmod()
    # print i.is_run()
    # print i.is_irdy()
    # print i.is_tank_full()
    # print i.read_smart_entries()
    # Funciona,TO-DO pero hay que probar con algo conectado. print i.get_output_current()
    # print i.get_time_run_pump()
    #print i.get_num_poles()
    #print i.set_num_poles(n_poles=6)
    # print i.get_pump_flow()
    # funciona print i.get_pump_power()
    # funciona print i.get_performance()
    # funciona print i.get_pump_rpm()
    #print i.get_max_frequency()
    #print i.set_max_frequency(27.78)
    #print i.get_vias()
    #print i.set_with_eeprom(10)
    #print i.get_num_poles()
    #print i.set_max_frequency()
    # funciona print i.get_security_time()
    # funciona print i.get_input_voltage()
    # funciona print i.set_max_frequency(28.45)
    # funciona print i.get_min_frequency()
    # TO-DO print i.set_max_voltage()
    # TO-DO print i.get_max_voltage()
    # Funciona print i.set_source_run()
    #print i.set_acceleration_time()
    #print i.get_acceleration_time()
"""
    i.frame.parseReadCoilResponse()

    UV_detection = 'P101'

    if UV_detection == 0:
        print 'MODE: micro cuts'
        print 'Delay time to FW 1', 'P100'

        B001 Seleccion de reintento
            00 (fallo), 01 (inicio en 0 Hz),
            02 (arranque en busqueda de frecuencia),
            03 (fallo tras parada por deceleracion en busqueda de frecuencia),
            04 (reinicio en busqueda de frecuencia)

        B002 Tiempo permitido de interrupcion momentanea de la alimentacion
            De 3 a 250
            0,1 [seg]



    elif UV_detection == 1:
        print 'MODE: UV detection'
        print 'Delay time to FW 1', 'P100'

    ###################
    #### AUTORESET ####
    ###################
    autoreset = 'P105'

    if autoreset == 0:
        print 'Autoreset P105: Never'
    elif autoreset == 1:
        print 'Autoreset P105: Always'
    elif autoreset == 2:
        print 'Autoreset P105: Yes, P106'
"""
