> **Index**
* communication
   * [DonJose_slave](#DonJose_slavepy) [(source)](http://git.whitewallenergy.com/whitewall/ivy_gw/blob/master/modules/rs485/examples/communication/DonJose_slave.py)
   * [DonPepito_master](#DonPepito_masterpy) [(source)](http://git.whitewallenergy.com/whitewall/ivy_gw/blob/master/modules/rs485/examples/communication/DonPepito_master.py)
* hello_world
   * [screen](#screenpy) [(source)](http://git.whitewallenergy.com/whitewall/ivy_gw/blob/master/modules/rs485/examples/hello_world/screen.py)
   * [serial_master](#serial_masterpy) [(source)](http://git.whitewallenergy.com/whitewall/ivy_gw/blob/master/modules/rs485/examples/hello_world/serial_master.py)
   * [serial_slave](#serial_slavepy) [(source)](http://git.whitewallenergy.com/whitewall/ivy_gw/blob/master/modules/rs485/examples/hello_world/serial_slave.py)
   
   
   
# communication
# DonJose_slave.py   
Example in which it runs a script that sends a greeting    
from Ivy to the PC, then Ivy receives a greeting from the PC.    
To finish Ivy says goodbye to the PC and the PC says    
goodbye to Ivy, after the above the script ends.    
Is necessary to run DonPepito.py first and then Run DonJose.py    
Device: Ivy  
* __Author__: Juan Carlos Chaves <juan.chaves@whitewallenergy.com>   
* __Version__: 0.1   
* __Copyright__: Copyright (C) 2017   
* __License__: MIT (expat) License   
   
# DonPepito_master.py   
The PC is until it receives a greeting from the Ivy. Then answer with    
another greeting to Ivy. To finish Ivy says goodbye to the PC and    
the PC says goodbye to Ivy, after the above the script ends.    
You need to run DonPepito.py first and then Run DonJose.py    
    
Device: PC  
* __Author__: Juan Carlos Chaves <juan.chaves@whitewallenergy.com>   
* __Version__: 0.1   
* __Copyright__: Copyright (C) 2017   
* __License__: MIT (expat) License   
   
# hello_world
# screen.py   
Example in which the message "hello world" is sent from Ivy to a PC that is listening to receive the message    
whit "screen /dev/ttyUSB0"    
    
Devices: Ivy and PC  
* __Author__: Juan Carlos Chaves <juan.chaves@whitewallenergy.com>   
* __Version__: 0.1   
* __Copyright__: Copyright (C) 2017   
* __License__: MIT (expat) License   
   
# serial_master.py   
Example in which the master sends the message "hello world" to a slave,    
for the example to work correctly, it is necessary to launch the    
hello_world_serial_slave.py script first in the slave and then launch this script    
    
    
Device: Ivy  
* __Author__: Juan Carlos Chaves <juan.chaves@whitewallenergy.com>   
* __Version__: 0.1   
* __Copyright__: Copyright (C) 2017   
* __License__: MIT (expat) License   
   
# serial_slave.py   
Example in which the slave waits to receive a message,    
once it receives it, displays it on the screen and ends.    
    
    
Device: PC  
* __Author__: Juan Carlos Chaves <juan.chaves@whitewallenergy.com>   
* __Version__: 0.1   
* __Copyright__: Copyright (C) 2017   
* __License__: MIT (expat) License   
   
   
   
   
