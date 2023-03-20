/*
 * https://www.adrirobot.it/Modulo_hc-05/modulo_hc-05.htm
https://www.lombardoandrea.com/arduino-hc-05-base/
https://www.instructables.com/id/How-to-Configure-HC-05-Bluetooth-Module-As-Master-/
The required AT commands to set the configuration as SLAVE
    AT+RMAAD (To clear any paired devices)
    AT+ROLE=0 (To set it as slave)
    AT+ADDR (To get the address of this HC-05, remember to jot the address down as it will be used during master configuration)
    AT+UART=38400,0,0 (To fix the baud rate at 38400)
    
*/

/*
  For this sketch use pins TX0 and RX0 of arduino mega
*/
#include <SoftwareSerial.h>

#define __BAUD 38400

void setup(){
  Serial.begin(__BAUD);
  delay(1000);
  Serial.println("ready...");
}

void loop() {  
  //if data coming from BT module print them...
  if (Serial.available() > 0) {
    Serial.println(Serial.read());
  }
}