> **Index**
* hello_world
   * [raw](#rawpy) [(source)](http://git.whitewallenergy.com/whitewall/ivy_gw/blob/master/modules/modbus/examples/hello_world/raw.py)
   * [write](#writepy) [(source)](http://git.whitewallenergy.com/whitewall/ivy_gw/blob/master/modules/modbus/examples/hello_world/write.py)
* mx2
   * [loop_test](#loop_testpy) [(source)](http://git.whitewallenergy.com/whitewall/ivy_gw/blob/master/modules/modbus/examples/mx2/loop_test.py)
   * [read_coil](#read_coilpy) [(source)](http://git.whitewallenergy.com/whitewall/ivy_gw/blob/master/modules/modbus/examples/mx2/read_coil.py)
   * [read_register](#read_registerpy) [(source)](http://git.whitewallenergy.com/whitewall/ivy_gw/blob/master/modules/modbus/examples/mx2/read_register.py)
   * [write_coil](#write_coilpy) [(source)](http://git.whitewallenergy.com/whitewall/ivy_gw/blob/master/modules/modbus/examples/mx2/write_coil.py)
   * [write_coils](#write_coilspy) [(source)](http://git.whitewallenergy.com/whitewall/ivy_gw/blob/master/modules/modbus/examples/mx2/write_coils.py)
   * [write_read_registers](#write_read_registerspy) [(source)](http://git.whitewallenergy.com/whitewall/ivy_gw/blob/master/modules/modbus/examples/mx2/write_read_registers.py)
   * [write_register](#write_registerpy) [(source)](http://git.whitewallenergy.com/whitewall/ivy_gw/blob/master/modules/modbus/examples/mx2/write_register.py)
   * [write_registers](#write_registerspy) [(source)](http://git.whitewallenergy.com/whitewall/ivy_gw/blob/master/modules/modbus/examples/mx2/write_registers.py)
* relay
   * [off_r1](#off_r1py) [(source)](http://git.whitewallenergy.com/whitewall/ivy_gw/blob/master/modules/modbus/examples/relay/off_r1.py)
   * [on_r2__off_r6](#on_r2__off_r6py) [(source)](http://git.whitewallenergy.com/whitewall/ivy_gw/blob/master/modules/modbus/examples/relay/on_r2__off_r6.py)
   * [on_r5](#on_r5py) [(source)](http://git.whitewallenergy.com/whitewall/ivy_gw/blob/master/modules/modbus/examples/relay/on_r5.py)
* sensor
   * [read_name_configuration](#read_name_configurationpy) [(source)](http://git.whitewallenergy.com/whitewall/ivy_gw/blob/master/modules/modbus/examples/sensor/read_name_configuration.py)
   * [read_registers](#read_registerspy) [(source)](http://git.whitewallenergy.com/whitewall/ivy_gw/blob/master/modules/modbus/examples/sensor/read_registers.py)
   * [write_registers](#write_registerspy) [(source)](http://git.whitewallenergy.com/whitewall/ivy_gw/blob/master/modules/modbus/examples/sensor/write_registers.py)
* tools
   * [usb_port_sniffer](#usb_port_snifferpy) [(source)](http://git.whitewallenergy.com/whitewall/ivy_gw/blob/master/modules/modbus/examples/tools/usb_port_sniffer.py)
   
   
   
# hello_world
# raw.py   
Example sending the "Hello World" message using the raw function    
of the Modbus module. To verify it's operation, you must connect    
the PC and Ivy to the same rs485 network and run it on the PC    
../tools/snifferPort.py before launching this script.  
   
# write.py   
Example that sends the message "Hello World" using Modbus module,    
but without using the raw function. To verify it's operation,    
you must connect the PC and Ivy to the same rs485 network and    
run it on the PC ../tools/snifferPort.py before launching this script.    
    
Devices : Ivy and PC  
* __Author__: Juan Carlos Chaves <juan.chaves@whitewallenergy.com>   
* __Version__: 0.1   
* __Copyright__: Copyright (C) 2017   
* __License__: MIT (expat) License   
   
# mx2
# loop_test.py   
Example Loop test to check communication.    
    
Device: Variable Frequency Drives    
Model: MX2-series    
See documentation (https://assets.omron.eu/downloads/manual/en/i570_mx2_users_manual_en.pdf)  
* __Author__: Juan Carlos Chaves <juan.chaves@whitewallenergy.com>   
* __Version__: 0.1   
* __Copyright__: Copyright (C) 2017   
* __License__: MIT (expat) License   
   
# read_coil.py   
Example read coil.    
    
Device: Variable Frequency Drives    
Model: MX2-series    
See documentation (https://assets.omron.eu/downloads/manual/en/i570_mx2_users_manual_en.pdf)  
* __Author__: Juan Carlos Chaves <juan.chaves@whitewallenergy.com>   
* __Version__: 0.1   
* __Copyright__: Copyright (C) 2017   
* __License__: MIT (expat) License   
   
# read_register.py   
Example read registers.    
    
Device: Variable Frequency Drives    
Model: MX2-series    
See documentation (https://assets.omron.eu/downloads/manual/en/i570_mx2_users_manual_en.pdf)  
* __Author__: Juan Carlos Chaves <juan.chaves@whitewallenergy.com>   
* __Version__: 0.1   
* __Copyright__: Copyright (C) 2017   
* __License__: MIT (expat) License   
   
# write_coil.py   
Example write coil.    
    
    
Device: Variable Frequency Drives    
Model: MX2-series    
See documentation (https://assets.omron.eu/downloads/manual/en/i570_mx2_users_manual_en.pdf)  
* __Author__: Juan Carlos Chaves <juan.chaves@whitewallenergy.com>   
* __Version__: 0.1   
* __Copyright__: Copyright (C) 2017   
* __License__: MIT (expat) License   
   
# write_coils.py   
Example write consecutive coils.    
    
Device: Variable Frequency Drives    
Model: MX2-series    
See documentation (https://assets.omron.eu/downloads/manual/en/i570_mx2_users_manual_en.pdf)  
* __Author__: Juan Carlos Chaves <juan.chaves@whitewallenergy.com>   
* __Version__: 0.1   
* __Copyright__: Copyright (C) 2017   
* __License__: MIT (expat) License   
   
# write_read_registers.py   
Example write and read register    
    
Device: Variable Frequency Drives    
Model: MX2-series    
See documentation (https://assets.omron.eu/downloads/manual/en/i570_mx2_users_manual_en.pdf)  
* __Author__: Juan Carlos Chaves <juan.chaves@whitewallenergy.com>   
* __Version__: 0.1   
* __Copyright__: Copyright (C) 2017   
* __License__: MIT (expat) License   
   
# write_register.py   
Example write register.    
    
Device: Variable Frequency Drives    
Model: MX2-series    
See documentation (https://assets.omron.eu/downloads/manual/en/i570_mx2_users_manual_en.pdf)  
* __Author__: Juan Carlos Chaves <juan.chaves@whitewallenergy.com>   
* __Version__: 0.1   
* __Copyright__: Copyright (C) 2017   
* __License__: MIT (expat) License   
   
# write_registers.py   
Example write consecutive registers    
    
Device: Variable Frequency Drives    
Model: MX2-series    
See documentation (https://assets.omron.eu/downloads/manual/en/i570_mx2_users_manual_en.pdf)  
* __Author__: Juan Carlos Chaves <juan.chaves@whitewallenergy.com>   
* __Version__: 0.1   
* __Copyright__: Copyright (C) 2017   
* __License__: MIT (expat) License   
   
# relay
# off_r1.py   
Example Turn off relay 1    
    
Device: Relay board KMtronick  
* __Author__: Juan Carlos Chaves <juan.chaves@whitewallenergy.com>   
* __Version__: 0.1   
* __Copyright__: Copyright (C) 2017   
* __License__: MIT (expat) License   
   
# on_r2__off_r6.py   
Example Turn on relay 2 and turn off relay 6    
    
Device: Relay board KMtronick  
* __Author__: Juan Carlos Chaves <juan.chaves@whitewallenergy.com>   
* __Version__: 0.1   
* __Copyright__: Copyright (C) 2017   
* __License__: MIT (expat) License   
   
# on_r5.py   
Example Turn on relay 5    
    
Device: Relay board KMtronick  
* __Author__: Juan Carlos Chaves <juan.chaves@whitewallenergy.com>   
* __Version__: 0.1   
* __Copyright__: Copyright (C) 2017   
* __License__: MIT (expat) License   
   
# sensor
# read_name_configuration.py   
Example to read the transducer's name and configuration    
    
Device:    
Digital transducer    
Model: CE-AD11B-32ES5    
See documentation (http://www.ce-transducer.com/down/CE-A-catalog.pdf)    
    
TX    
Addres of slave:                01h    
Function code:                  03h    
Addres of the first register:   0020h    
Quanty of registers:            0003h    
CRC:                            0401h    
    
RX    
Addres of slave:                01h    
Function code:                  03h    
Byte count:                     06h    
Address of slave:               01h    
Baudrate code:                  06h         (9600)    
Name:                           44313133h   (D113)    
CRC:                            b81eh  
* __Author__: Javi Ortega <javier.ortega@whitewallenergy.com>   
* __Version__: 0.1   
* __Copyright__: Copyright (C) 2017   
* __License__: MIT (expat) License   

## Functions

###  def `get_baudrate_value(baudrate_code)`

Translate baurate code to baudrate value  
  
* **Parameter *baudrate_code*:** Baudrate code from rx  

* **Type *baudrate_code*:** int  
  

* **Return:** Baudrate value  
* **Type return:** int, None
   
# read_registers.py   
Example to read the transducer's name and configuration    
address (0-256)    
baudrate (3-7) | values (3-->1200), (4-->2400), (5-->4800), (6-->9600), (7-->19200).    
    
Device:    
Digital transducer    
Model: CE-AD11B-32ES5    
See documentation (http://www.ce-transducer.com/down/CE-A-catalog.pdf)  
* __Author__: Juan Carlos Chaves <juan.chaves@whitewallenergy.com>   
* __Version__: 0.1   
* __Copyright__: Copyright (C) 2017   
* __License__: MIT (expat) License   
   
# write_registers.py   
Example to write the transducer's name and configuration    
address (0-256)    
baudrate (3-7) | values (3-->1200), (4-->2400), (5-->4800), (6-->9600), (7-->19200).    
    
Device:    
Digital transducer    
Model: CE-AD11B-32ES5    
See documentation (http://www.ce-transducer.com/down/CE-A-catalog.pdf)  
* __Author__: Juan Carlos Chaves <juan.chaves@whitewallenergy.com>   
* __Version__: 0.1   
* __Copyright__: Copyright (C) 2017   
* __License__: MIT (expat) License   
   
# tools
# usb_port_sniffer.py   
USB port sniffer  
* __Author__: Javi Ortega <javier.ortega@whitewallenergy.com>   
* __Version__: 0.1   
* __Copyright__: Copyright (C) 2017   
* __License__: MIT (expat) License   
   
   
   
   
