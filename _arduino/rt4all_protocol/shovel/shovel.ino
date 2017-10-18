/* 

 By Juan Carlos Chaves Puertas lobolanja@gmail.coim

 

 The functions implemented are functions 3, 10 and 20.

 read var, preset var and actions

 of the Modbus RTU Protocol, to be used over the Arduino serial connection.

 

 This implementation is similar with the Modbus specifications.

 

 

 These library of functions are designed to enable a program send and

 receive data from a device that communicates using a similar implementation of Modbus protocol.

 

RT4ALLSlave implements an unsigned int return value on a call to modbus_update().

 This value is the total error count since the slave started. It's useful for fault finding.



*/
#include <DHT11.h>
#include <Servo.h>

#define BUFFER_SIZE 128

enum 
{     
  // just add or remove registers and your good to go...
  // The first register starts at address 0
  LED_STATE, // 0000h
  temperature,// 0001h
  humidity,//0002h
  pos_servo,//0003h
  vel_servo,//0004h
  vel_motors,//0005h
  GO,//0006h
  BACK,//0007h
  LEFT,//0008h
  RIGHT,//0009h
  CAM_L,//000Ah
  CAM_R,//000Bh
  SCOOP,
 
  TOTAL_ERRORS,
  // leave this one
  TOTAL_REGS_SIZE 
  // total number of registers for function 3 and 16 share the same register array
};

int engine_l_f = 5;
int engine_l_b = 6;
int engine_r_f = 10;
int engine_r_b = 11;
int pin_dht=4;
DHT11 dht11(pin_dht);
unsigned int holdingRegs[TOTAL_REGS_SIZE];
Servo servoMotor;


// frame[] is used to recieve and transmit packages. 

// The maximum serial ring buffer size is 128

unsigned char frame[BUFFER_SIZE];

unsigned int holdingRegsSize; // size of the register array 

unsigned char broadcastFlag;

unsigned char slaveID;

unsigned char function;

unsigned char TxEnablePin;

unsigned int errorCount;

unsigned int T1_5; // inter character time out

unsigned int T3_5; // frame delay


int led = 13;
// the setup routine runs once when you press reset:
void setup() {                
  // initialize the digital pin as an output.
   
   modbus_configure(9600, 1, TOTAL_REGS_SIZE, 0);
   holdingRegs[LED_STATE]=1;
   holdingRegs[temperature]=7;
   holdingRegs[vel_motors]=100;
   holdingRegs[pos_servo]=100;
   holdingRegs[vel_servo]=5;
   servoMotor.attach(9);
  pinMode(led, OUTPUT);
  pinMode(3,OUTPUT); 
  pinMode(engine_l_f,OUTPUT);  
  pinMode(engine_l_b,OUTPUT);  
  pinMode(engine_r_f,OUTPUT);  
  pinMode(engine_r_b,OUTPUT); 
  servoMotor.write(holdingRegs[pos_servo]);
  
}
void go(int vel){
    holdingRegs[pos_servo]+=2;
}

void left(int vel){
    digitalWrite(engine_l_b,1);  
    digitalWrite(engine_r_b,0);
    digitalWrite(engine_l_f,0);  
    digitalWrite(engine_r_f,1);
}

void back(int vel){
    holdingRegs[pos_servo]-=2;
}

void right(int vel){
    digitalWrite(engine_l_b,0);  
    digitalWrite(engine_r_b,1);
    digitalWrite(engine_l_f,1);  
    digitalWrite(engine_r_f,0);
}
void idle(){
    digitalWrite(engine_l_b,0);  
    digitalWrite(engine_r_b,0);
    digitalWrite(engine_l_f,0);  
    digitalWrite(engine_r_f,0);
}



// the loop routine runs over and over again forever:
void loop() {
    //Serial.print("funcionando");
  for(int i=0;i<10000;i++){
    slave_update(holdingRegs);
     if(holdingRegs[GO])    go(holdingRegs[vel_motors]);
     else if(!holdingRegs[GO]){
       idle();
       if(holdingRegs[BACK]) back(vel_motors);
       else if(!holdingRegs[BACK]){
          idle();
          if(holdingRegs[LEFT]) left(vel_motors);
          else if(!holdingRegs[LEFT]){
            idle(); 
            if(holdingRegs[RIGHT]) right(vel_motors);
            else if (!holdingRegs[RIGHT])idle();
          }
       }
     }
  }     
}

unsigned int slave_update(unsigned int *holdingRegs)
{

  unsigned char buffer = 0;

  unsigned char overflow = 0;

  

  while (Serial.available())

  {
    

    // The maximum number of bytes is limited to the serial buffer size of 128 bytes

    // If more bytes is received than the BUFFER_SIZE the overflow flag will be set and the 

    // serial buffer will be red untill all the data is cleared from the receive buffer.

    if (overflow) 

      Serial.read();

    else

    {

      if (buffer == BUFFER_SIZE) overflow = 1;

        

      frame[buffer] = Serial.read();

      buffer++;

    }

    delayMicroseconds(T1_5); // inter character time out

  }

  

  // If an overflow occurred increment the errorCount

  // variable and return to the main sketch without 

  // responding to the request i.e. force a timeout

  if (overflow)

    return errorCount++;

  

  // The minimum request packet is 8 bytes for function 3 & 16

  if (buffer > 5) 

  {
    unsigned char id = frame[0];

    

    broadcastFlag = 0;

    

    if (id == 0)

      broadcastFlag = 1;

    

    if (id == slaveID || broadcastFlag) // if the recieved ID matches the slaveID or broadcasting id (0), continue

    {


        function = frame[1];

        unsigned int startingAddress = ((frame[2] << 8) | frame[3]); // combine the starting address bytes

        unsigned int no_of_registers = ((frame[4] << 8) | frame[5]); // combine the number of register bytes  

        unsigned int maxData = startingAddress + no_of_registers;

        unsigned char index;

        unsigned char address;


        if (!broadcastFlag && (function == 3))

        {

          if (startingAddress < holdingRegsSize) // check exception 2 ILLEGAL DATA ADDRESS

          {

            if (maxData <= holdingRegsSize) // check exception 3 ILLEGAL DATA VALUE

            {

              unsigned char noOfBytes = no_of_registers * 2;

              unsigned char responseFrameSize = 3 + noOfBytes; // ID, function, noOfBytes, (dataLo + dataHi) * number of registers, crcLo, crcHi

              frame[0] = slaveID;

              frame[1] = function;

              frame[2] = noOfBytes;

              address = 3; // PDU starts at the 4th byte

              unsigned int temp;

              

              for (index = startingAddress; index < maxData; index++)

              {

                temp = holdingRegs[index];

                frame[address] = temp >> 8; // split the register into 2 bytes

                address++;

                frame[address] = temp & 0xFF;

                address++;

              } 

            

              sendPacket(responseFrameSize);

            }

            else  

              exceptionResponse(3); // exception 3 ILLEGAL DATA VALUE

          }

          else

            exceptionResponse(2); // exception 2 ILLEGAL DATA ADDRESS

        }

        else if (function == 6)

        {

          if (startingAddress < holdingRegsSize) // check exception 2 ILLEGAL DATA ADDRESS

          {

              unsigned int startingAddress = ((frame[2] << 8) | frame[3]);

              unsigned int regStatus = ((frame[4] << 8) | frame[5]);

              unsigned char responseFrameSize = 6;

              

              holdingRegs[startingAddress] = regStatus;

              sendPacket(responseFrameSize);

          }

          else

            exceptionResponse(2); // exception 2 ILLEGAL DATA ADDRESS

          }

        
    } // incorrect id

  }

  else if (buffer > 0 && buffer < 8)

    errorCount++; // corrupted packet

    

  return errorCount;

}       



void exceptionResponse(unsigned char exception)

{

  errorCount++; // each call to exceptionResponse() will increment the errorCount

  if (!broadcastFlag) // don't respond if its a broadcast message

  {

    frame[0] = slaveID;

    frame[1] = (function | 0x80); // set the MSB bit high, informs the master of an exception

    frame[2] = exception;

    sendPacket(3); // exception response is always 3 bytes ID, function + 0x80, exception code, 2 bytes crc

  }

}



void modbus_configure(long baud, unsigned char _slaveID, unsigned int _holdingRegsSize, unsigned char _lowLatency)

{

  slaveID = _slaveID;

  Serial.begin(baud);

  

  // Modbus states that a baud rate higher than 19200 must use a fixed 750 us 

  // for inter character time out and 1.75 ms for a frame delay.

  // For baud rates below 19200 the timeing is more critical and has to be calculated.

  // E.g. 9600 baud in a 10 bit packet is 960 characters per second

  // In milliseconds this will be 960characters per 1000ms. So for 1 character

  // 1000ms/960characters is 1.04167ms per character and finaly modbus states an

  // intercharacter must be 1.5T or 1.5 times longer than a normal character and thus

  // 1.5T = 1.04167ms * 1.5 = 1.5625ms. A frame delay is 3.5T.

  // Added experimental low latency delays. This makes the implementation

  // non-standard but practically it works with all major modbus master implementations.

  

  if (baud == 1000000 && _lowLatency)

  {

      T1_5 = 1; 

      T3_5 = 10;

  }

  else if (baud >= 115200 && _lowLatency){

      T1_5 = 75; 

      T3_5 = 175; 

  }

  else if (baud > 19200)

  {

    T1_5 = 750; 

    T3_5 = 1750;

  }

  else 

  {

    T1_5 = 15000000/baud; // 1T * 1.5 = T1.5

    T3_5 = 35000000/baud; // 1T * 3.5 = T3.5

  }

  

  holdingRegsSize = _holdingRegsSize;

  errorCount = 0; // initialize errorCount

}   



unsigned int calculateCRC(byte bufferSize) 

{

  unsigned int temp, temp2, flag;

  temp = 0xFFFF;

  for (unsigned char i = 0; i < bufferSize; i++)

  {

    temp = temp ^ frame[i];

    for (unsigned char j = 1; j <= 8; j++)

    {

      flag = temp & 0x0001;

      temp >>= 1;

      if (flag)

        temp ^= 0xA001;

    }

  }

  // Reverse byte order. 

  temp2 = temp >> 8;

  temp = (temp << 8) | temp2;

  temp &= 0xFFFF;

  return temp; // the returned value is already swopped - crcLo byte is first & crcHi byte is last

}



void sendPacket(unsigned char bufferSize)

{

  if (TxEnablePin > 1)

    digitalWrite(TxEnablePin, HIGH);

    

  for (unsigned char i = 0; i < bufferSize; i++)

    Serial.write(frame[i]);

    

  Serial.flush();

  

  // allow a frame delay to indicate end of transmission

  delayMicroseconds(T3_5); 

  

  if (TxEnablePin > 1)

    digitalWrite(TxEnablePin, LOW);

}

