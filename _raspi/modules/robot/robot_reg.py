# REGISTERS
A002 = '\x12\x01'       # 1202  Fuente comando RUN
A020 = '\x12\x15'       # 1216  Tension maxima (Juan)/Frecuencia de multivelocidad 0
A061 = '\x12\x4E'       # 124F  Limite frecuencia superior
A062 = '\x12\x50'       # 1251  Limite frecuencia inferior

D001 = '\x10\x00'       # 1001  Frecuencia de salida
D002 = '\x10\x02'       # 1003h R   SIMPLE  Output current monitoring   0.01 [A]
D003 = '\x10\x03'       # 1004  Direccion de rotacion
D004 = '\x10\x04'       # 1005  Realimentacion de PID
D005 = '\x10\x06'       # 1007  Estado de terminal de entrada inteligente 1-7
D006 = '\x10\x07'       # 1008  Estado de terminal de salida inteligente 11-12, rele
D013 = '\x10\x10'       # 1011  Voltaje de salida al motor
D014 = '\x10\x11'       # 1011  Potencia de entrada al inversor
D016 = '\x10\x14'       # 1015 R   DOUBLE  Total time in RUN mode      1 [h]
D017 = '\x10\x16'       # 1017  Tiempo conectado
D102 = '\x10\x25'       # 1026  Tension del bus de c.c. interno del variador

P037 = '\x16\x24'       # 1625  Valor de bias de par
P049 = '\x16\x32'       # 1633  Configuracion de la polaridad de los polos del motor //NO editable en MODO_RUN error '"'
P057 = '\x16\x3A'       # 163B  Grado de desviacion de la frecuencia del tren de pulsos
P060 = '\x16\x3D'       # 163E  Comando de posicion de multivelocidad 0
P100 = '\x16\x65'       # 1666  Tiempo para disparo rearranque. Tiempo de seguridad para vericar que la tension en el bus c.c. es constante y no ha sido un pico de tension
P101 = '\x16\x66'       # 1667  (Des)Habilita la deteccion del nivel de baja tension
P102 = '\x16\x67'       # 1668  Voltage de entrada para disparo rearranque (tension de referencia)
P060 = '\x16\x3D'       # 163E Comando de posicio   n de multivelocidad 0
# COILS
COIL_SET_RUN = '\x00\x00'
COIL_RUN = '\x00\x12'   # 0013h  R    1: ON, 0: OFF
COIL_IRDY = '\x00\x44'  # 0045h  R    1: Prepardo, 0: No preparado
COIL_RUN_ENTRY = '\x00\x06' # 0007h R/W 1: ON, 0:OFF ademas es la primera bobina de las entradas inteligentes.
COIL_SE1 = '\x00\x06'
COIL_TANK = '\x00\x07'  # 0008h R/W   1: ON, 0: OFF

# DEFAULT VALUES
DEFAULT_SLAVE_ADDRESS = 1
DEFAULT_BIG_ENDIAND = True

DEFAULT_IS_THREE_PHASE = False
DEFAULT_HEIGHT_IMPULSE = 0              # meters
DEFAULT_DENSITY = 1000                  # kg/m^3
DEFAULT_MAX_POWER = 1000                # Watts
DEFAULT_FLOW_AT_MAXIMUM_POWER = 1000    # m^3/h

DEFAULT_N_POLES = 0
DEFAULT_REFERENCE_VOLTAGE = 270
DEFAULT_SECURITY_TIME = 2000            # ms
DEFAULT_MAX_VOLTAGE = 250               # V
DEFAULT_MIN_FREQUENCY = 20
DEFAULT_MAX_FREQUENCY = 49
DEFAULT_SOURCE_RUN = 3


# OLD
# ------------
STX = '\x01'

FN_READ = '\x03'        # Lectura registro de retencion
FN_WRITE = '\x06'       # Escritura registro de retencion
FN_WRITE_CONSECUTIVE = '\x10'
FN_COIL_READ = '\x01'   # Lectura de bobina
FN_COIL_WRITE = '\x05'  # Escritura en bobina
FN_LAZO = '\x08'

VDF_A = '\x00\x02'      # 0003  Estado del variador A

A001 = '\x12\x00'       # 1201  Fuente de frecuencia

A003 = ''               # Frecuencia maxima
A041 = '\x12\x3B'       # Seleccion de refuerzo par

B001 = '\x13\x00'       # 1301
B002 = '\x13\x01'       # 1302
B082 = '\x13\x54'       # 1355  Frecuencia de inicio
B084 = '\x13\x56'       # 1357  Modo de inicializacion (parametros o historial de disparo)
B085 = '\x13\x57'       # 1358  Seleccion de datos iniciales
B094 = '\x13\x60'       # 1361  Configuracion de datos objetivo de inicializacion
B180 = '\x13\xB6'       # 13B7  Activacion de inicializacion

C002 = ''
C106 = '\x14\x6D'       # 146E  Ajuste de ganancia de AM
C109 = '\x14\x70'       # 1471  Ajuste de bias de AM
C021 = '\x14\x14'       # 1415  Funcion de salida [11]
C022 = '\x14\x15'       # 1416  Funcion de salida [12]
C026 = '\x14\x19'       # 141A  Funcion de rele de alarma
C028 = '\x14\x1B'       # 141C
C031 = '\x14\x1E'       # 141F  Estado activo de salida [11] 0 NO 1 NC
C032 = '\x14\x1F'       # 1420  Estado activo de salida [11] 0 NO 1 NC
C036 = '\x14\x23'       # 1424  Estado activo de rele 0 NO 1 NC
C071 = '\x14\x4A'       # 144B  velocidad comunicaciones
C072 = '\x14\x4B'       # 144C  Direccion modbus
C074 = '\x14\x4D'       # 144E  Paridad de comunicaciones
C075 = '\x14\x4E'       # 144F  Bit parada de comunicaciones
C078 = '\x14\x51'       # 1452  Tiempo espera de comunicaciones


D062 = '\x10\x58'       # Monitorizacion de la fuente de frecuencia
D081 = '\x00\x11'       # 0012  Monitor 1
REG_D081 = '\x00\x12'   #       Monitor 1
D090 = '\x00\x4D'       # 004E  Monitorizacion de errores de programacion (advertencia)


F002 = '\x11\x02'       # 1103  Tiempo aceleracion
F003 = '\x11\x04'       # 1105  Tiempo deceleracion




H004 = '\x15\x03'       # 1504  Seleccion del numero de polos del motor

#############################
########## BOBINAS ##########
#############################

b_operational = '\x00\x0E' # 000F Bobina de operacion

REG_DOUBLE = [A061, A062, D001, D004, D016, D017, F002, F003]

#################################################
# Elementos para configuracion y monitorizacion #
#################################################
############## Funciones de salida ##############
RUN = 0                 # Funcionamiento
FA1 = 1                 # Velocidad constante alcanzada
FA2 = 2                 # Frecuencia establecida superada
OL = 3                  # Senal anticipada de sobrecarga
OD = 4                  # Desviacion de salida para control PID
AL = 5                  # Senal de alarma
FA3 = 6                 # Frecuencia establecida alcanzada (1)
OTQ = 7                 # Par excesivo
UV = 9                  # Infratension
TRQ = 10                # Par limitado
RNT = 11                # Tiempo de operacion transcurrido
ONT = 12                # Tiempo de conexion transcurrido
THM = 13                # Senal de alarma termica
BRK = 19                # Liberacion del freno
BER = 20                # Error de frenado
ZS = 21                 # Senal de deteccion de 0 Hz
DSE = 22                # Desvio maximo de velocidad
POK = 23                # Posicionado finalizado
FA4 = 24                # Frecuencia establecida superada (2)
FA5 = 25                # Frecuencia establecida alcanzada 2
OL2 = 26                # Senal anticipada de sobrecarga (2)
"""
31 (FBV: comparacion de realimentacion de PID
32 (NDc: desconexion de linea de comunicaciones
33 (LOG1: resultado de operacion logica 1
34 (LOG2: resultado de operacion logica 2)
35 (LOG3: resultado de operacion logica 3)
39 (WAC: advertencia de vida util del condensador)
40 (WAF: ventilador de refrigeracion
41 (FR: senal de On directo/inverso),
42 (OHF: advertencia de sobrecalentamiento del disipador termico),
43 (LOC: nivel de indicacion de corriente baja),
44 (M01: salida de proposito general 1
45 (M02: salida de proposito general 2
46 (M03: salida de proposito general 3)
50 (IRDY: variador preparado)
51 (FWR: rotacion directa
52 (RVR: rotacion inversa
53 (MJA: fallo grave
54 (WCO: comparador de intervalo O
55 (WCO: comparador de intervalo OI
58(FREF),
59(REF),
60(SETM),
62(EDM),
63(OPO: opcion)
"""
