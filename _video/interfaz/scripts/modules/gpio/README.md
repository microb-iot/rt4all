This module allow handle GPIO: set direction (in/out) and value (0/1), get address and value.
   
   
View more info in his [wiki](http://git.whitewallenergy.com/whitewall/ivy_gw/wikis/Modules/GPIO)
   
   
# gpio.py   
Handler General Purpose Input/Output (GPIO)  
* __Author__: XXX <info@whitewallenergy.com>   
* __Copyright__: Copyright (C) 2016   

## Classes

###  class `Gpio()`

### Methods:


#### def `__init__()`



#### def `clear(gpio)`

Set gpio value 0  
  
* **Parameter *gpio*:** Number of gpio  

* **Type *gpio*:** integer

#### def `get_dir(gpio)`

Return gpio address  
  
* **Parameter *gpio*:** Number of gpio  

* **Type *gpio*:** integer  
  

* **Return:**  Direction  
* **Type return:**  integer

#### def `input(gpio)`

Enable pin and set value in  
  
* **Parameter *gpio*:** Number of gpio  

* **Type *gpio*:** integer

#### def `output(gpio)`

Enable pin and set value out  
  
* **Parameter *gpio*:** Number of gpio  

* **Type *gpio*:** integer

#### def `read(gpio)`

* **Parameter *gpio*:** Number of gpio  

* **Type *gpio*:** integer  
  

* **Return:**  Get gpio value  
* **Type return:**  integer

#### def `set(gpio)`

Set gpio value 1  
  
* **Parameter *gpio*:** Number of gpio  

* **Type *gpio*:** integer

#### def `setup()`

Setup address map  
  

* **Return:**  Status setup: -1 Open failed '/dev/mem', -2 Map failed, 0 Map success  
* **Type return:**  integer
