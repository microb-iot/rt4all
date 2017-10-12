This module is responsible for managing the GPIO in Ivy.
   
   
View more info in his [wiki](http://git.whitewallenergy.com/whitewall/ivy_gw/wikis/Modules/RS485)
   
   
# rs485.py   
Handler General Purpose Input/Output (GPIO)    
GPIO 24 Channel pin    
GPIO 23 Transfer and receive pin    
    
Average enable tx/rx is 0.00000369240 seg.  
* __Author__: Javi Ortega <javier.ortega@whitewallenergy.com>   
* __Version__: 0.1   
* __Copyright__: Copyright (C) 2017   
* __License__: MIT (expat) License   

## Classes

###  class `Rs485()`

### Methods:


#### def `__init__()`



#### def `is_rx_enable()`

Return receive status  
  

* **Return:**  GPIO 23 == 0  
* **Type return:**  boolean

#### def `is_tx_enable()`

Return transfer status  
  

* **Return:**  GPIO 23 != 0  
* **Type return:**  boolean

#### def `set_rx_enable()`

Set GPIO 23 to receive (GPIO 23 = 0)  
  

* **Return:**  GPIO Address, 0 to error  
* **Type return:**  integer

#### def `set_tx_enable()`

Set GPIO 23 to transfer (GPIO 23 = 1)  
  

* **Return:**  GPIO Address, 0 to error  
* **Type return:**  integer
