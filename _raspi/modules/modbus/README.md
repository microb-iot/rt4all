This module is responsible for communication using the Modbus protocol.
   
   
View more info in his [wiki](http://git.whitewallenergy.com/whitewall/ivy_gw/wikis/Modules/Modbus)
   
   
# modbus.py   
Modbus module  
* __Author__: Javi Ortega <javier.ortega@whitewallenergy.com>   
* __Version__: 0.1   
* __Copyright__: Copyright (C) 2017   
* __License__: MIT (expat) License   

## Classes

###  class `Modbus()`

### Methods:


#### def `__init__(port=/dev/ttyUSB0, baudrate=9600, bytesize=8, parity=N, stopbits=1, timeout=None, delay=0, protocol=RTU)`

* **Parameter *port*:** Port  
* **Parameter *baudrate*:** Baud rate  
* **Parameter *bytesize*:** Number of data bits  
* **Parameter *parity*:** Enable parity checking  
* **Parameter *stopbits*:** Number of stop bits  
* **Parameter *timeout*:** Set a read timeout value  
* **Parameter *delay*:** Set a read delay value  
* **Parameter *protocol*:** Communication protocol  
  

* **Type *port*:** string  
* **Type *baudrate*:** integer  
* **Type *bytesize*:** integer  
* **Type *parity*:** char  
* **Type *stopbits*:** integer  
* **Type *timeout*:** float  
* **Type *delay*:** float  
* **Type *protocol*:** string

#### def `get_baudrate()`


* **Return:**  Baud rate pySerial  
* **Type return:**  integer, None

#### def `get_bytesize()`


* **Return:**  Number of data bits pySerial  
* **Type return:**  integer, None

#### def `get_crc(tx, is_big_endian=True)`

Used RTU MODE  
  
* **Parameter *tx*:** Bytes to transfer  
* **Parameter *is_big_endian*:** Set big o little endian  
  

* **Type *tx*:** bytes  
* **Type *is_big_endian*:** bool  
  

* **Return:**  Two bytes (crc16)  
* **Type return:**  Buffer of bytes

#### def `get_delay()`


* **Return:**  Delay  
* **Type return:**  float, None

#### def `get_lrc(tx)`

Used ASCII MODE  
http://www.simplymodbus.ca/ASCII.htm  
  
* **Parameter *tx*:** Bytes to transfer  
  

* **Type *tx*:** bytes  
  

* **Return:**  One bytes  
* **Type return:**  Buffer of bytes

#### def `get_parity()`


* **Return:**  Parity pySerial  
* **Type return:**  char, None

#### def `get_port()`


* **Return:**  Port pySerial  
* **Type return:**  string, None

#### def `get_protocol()`


* **Return:**  Protocol  
* **Type return:**  string

#### def `get_serial()`


* **Return:**  Serial  
* **Type return:**  pySerial

#### def `get_stopbits()`


* **Return:**  Number of stop bits pySerial  
* **Type return:**  integer, None

#### def `get_supported_baudrate()`


* **Return:**  All supported baudrate  
* **Type return:**  Array (integer)

#### def `get_supported_bytesize()`


* **Return:**  All supported bytesize  
* **Type return:**  Array (integer)

#### def `get_supported_parity()`


* **Return:**  All supported parity  
* **Type return:**  Array (integer)

#### def `get_supported_protocol()`


* **Return:**  All supported Protocol  
* **Type return:**  Array (string)

#### def `get_supported_stopbits()`


* **Return:**  All supported stopbits  
* **Type return:**  Array (integer)

#### def `get_time_silent(baud=None)`

* **Parameter *baud*:** Baud rate to transfer. If baud is None, get_baudrate()  

* **Type *baud*:** integer, None  
  

* **Return:**  Call `self.get_time_transfer(3.5)`  
* **Type return:**  float

#### def `get_time_transfer(tx_bytes=0, baud=None)`

* **Parameter *tx_bytes*:** Number of byte to transfer  
* **Parameter *baud*:** Baud rate to transfer. If baud is None, get_baudrate()  
  

* **Type *tx_bytes*:** float  
* **Type *baud*:** integer, None  
  

* **Return:**  Seconds to transfer, -1 if baud not supported  
* **Type return:**  float

#### def `get_timeout()`


* **Return:**  Timeout  
* **Type return:**  float, None

#### def `is_rx_enable()`


* **Return:**  Call `rs485.is_rx_enable()`  
* **Type return:**  boolean

#### def `is_tx_enable()`


* **Return:**  Call `rs485.is_tx_enable()`  
* **Type return:**  boolean

#### def `raw(tx, byte_read=255)`

* **Parameter *tx*:** Buffer to transfer  
* **Parameter *byte_read*:** Number of bytes to read  
  

* **Type *tx*:** Bytes  
* **Type *byte_read*:** integer  
  

* **Return:**  Response  
* **Type return:**  Buffer of bytes, None

#### def `read(num_bytes=255)`

* **Parameter *num_byte*:** Number of bytes to read  

* **Type *num_byte*:** integer  
  

* **Return:**  Buffer of bytes readed  
* **Type return:**  Buffer of bytes, None

#### def `rtu_to_ascii(tx, colon=False, lrc=False, carriage_return=False, line_feed=False)`

Turn from tx_rtu to tx_ascii  
tx_rtu = '...'  
tx_ascii = '0103...'  
  
* **Parameter *tx*:** Buffer of bytes  
* **Parameter *colon*:** Add colon (5) to the beginning  
* **Parameter *lrc*:** Add lrc  
* **Parameter *carriage_return*:** Add carriage (  
) return at the end  
* **Parameter *line_feed*:** Add line feed (  
) at the end  
  

* **Type *tx*:** Buffer of bytes  
* **Type *colon*:** bool  
* **Type *lrc*:** bool  
* **Type *carriage_return*:** bool  
* **Type *line_feed*:** bool  
  

* **Return:**  Buffer of bytes readed  
* **Type return:**  Buffer of bytes, None

#### def `serial_close()`

Close pySerial

#### def `set_baudrate(baudrate=9600)`

If pySerial already existed modify baudrate else create a new pyserial with default values and new baudrate  
  
* **Parameter *baudrate*:** Baud rate  

* **Type *baudrate*:** integer  
  

* **Return:**  Serial  
* **Type return:**  pySerial

#### def `set_bytesize(bytesize=8)`

If pySerial already existed modify bytesize else create a new pyserial with default values and new bytesize  
  
* **Parameter *bytesize*:** Number of data bits  

* **Type *bytesize*:** integer  
  

* **Return:**  Serial  
* **Type return:**  pySerial

#### def `set_delay(delay=0)`

If pySerial already existed modify delay else create a new pyserial with default values and new delay  
  
* **Parameter *delay*:** Set a read delay value  

* **Type *delay*:** float  
  

* **Return:**  Serial  
* **Type return:**  pySerial

#### def `set_parity(parity=N)`

If pySerial already existed modify parity else create a new pyserial with default values and new parity  
  
* **Parameter *parity*:** Enable parity checking  

* **Type *parity*:** char  
  

* **Return:**  Serial  
* **Type return:**  pySerial

#### def `set_port(port=/dev/ttyUSB0)`

If pySerial already existed modify port else create a new pyserial with default values and new port  
  
* **Parameter *port*:** Port  

* **Type *port*:** string  
  

* **Return:**  Serial  
* **Type return:**  pySerial

#### def `set_protocol(protocol=RTU)`

Update communication protocol  
  
* **Parameter *protocol*:** New protocol  

* **Type *delay*:** string  
  

* **Return:**  Current protocol  
* **Type return:**  string

#### def `set_rx_enable()`

Call `rs485.set_rx_enable()`  
  

* **Return:**  GPIO Address, 0/None to error  
* **Type return:**  integer, None

#### def `set_serial(port=None, baudrate=None, bytesize=None, parity=None, stopbits=None, timeout=None, delay=None)`

Create a new pySerial.  
Default timeout is get_time_transfer(255, baudrate)  
pySerial.timeout = (timeout + delay)  
  
* **Parameter *port*:** Port  
* **Parameter *baudrate*:** Baud rate  
* **Parameter *bytesize*:** Number of data bits  
* **Parameter *parity*:** Enable parity checking  
* **Parameter *stopbits*:** Number of stop bits  
* **Parameter *timeout*:** Set a read timeout value  
* **Parameter *delay*:** Set a read delay value  
  

* **Type *port*:** string  
* **Type *baudrate*:** integer  
* **Type *bytesize*:** integer  
* **Type *parity*:** char  
* **Type *stopbits*:** integer  
* **Type *timeout*:** float  
* **Type *delay*:** float  
  

* **Return:**  Serial  
* **Type return:**  pySerial, None

#### def `set_stopbits(stopbits=1)`

If pySerial already existed modify stopbits else create a new pyserial with default values and new stopbits  
  
* **Parameter *stopbits*:** Number of stop bits  

* **Type *stopbits*:** integer  
  

* **Return:**  Serial  
* **Type return:**  pySerial

#### def `set_timeout(timeout=None)`

If pySerial already existed modify timeout else create a new pyserial with default values and new timeout  
  
* **Parameter *timeout*:** Set a read timeout value  

* **Type *timeout*:** float  
  

* **Return:**  Serial  
* **Type return:**  pySerial

#### def `set_tx_enable()`

Call `rs485.set_tx_enable()`  
  

* **Return:**  GPIO Address, 0/None to error  
* **Type return:**  integer, None

#### def `sleep_tx(num_bytes)`

Call `time.sleep(get_time_transfer(num_byte))`  
  
* **Parameter *num_byte*:** Number of bytes to write  

* **Type *num_byte*:** integer

#### def `write(tx)`

* **Parameter *tx*:** Buffer to transfer  

* **Type *tx*:** Buffer of bytes  
  

* **Return:**  Number of byte written  
* **Type return:**  int, None
