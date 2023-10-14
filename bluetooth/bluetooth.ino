#include "gyro.h"
#include "lights.h"
#include "movement.h"
#include "sensor.h"
#include "temp_reading.h"
#include <Servo.h>
#include <math.h>

int powerOn = 0; // symbolize the power on comand given to the rover

String setting = "";
String comand = "";

void setup() {
  pinMode(PIN_LIGHT, OUTPUT);
  Serial.begin(9600);
  // motor 1
  pinMode(PIN_INPUT_2_MOTOR_1, OUTPUT);
  pinMode(PIN_INPUT_1_MOTOR_1, OUTPUT);

  // motor 2
  pinMode(PIN_INPUT_3_MOTOR_2, OUTPUT);
  pinMode(PIN_INPUT_4_MOTOR_2, OUTPUT);

  // servo
  arm_servos[1].attach(2);
  arm_servos[2].attach(9);
  arm_servos[3].attach(10);
  arm_servos[4].attach(11);
  arm_servos[5].attach(12);

  for (int i = 1; i <= 5; i++) {
    arm_servos[i].write(0);
    stop[i] = 0;
  }

  mpu6050.begin();               // mpu initialized
  mpu6050.calcGyroOffsets(true); // mpu calibrated and ready for measures

  // settings for TPH sensor

  if (!bme.begin()) {
    Serial.println("Could not find a valid BME280 sensor, check wiring!");
    while (1)
      ;
  }
  // settings for magnetic field sensor
  pinMode(PIN_A_MAGNETIC_FIELD, INPUT);
  // setting for temperature reading
  pinMode(LEDpin, OUTPUT);
  Serial.begin(9600);
  reference_temperature = 25 + 273.15; // Temperature  T0 from datasheet,
                                       // conversion from Celsius to kelvin
}

void loop() {
  if (powerOn == 0) {
    AutomaticSettings();
  }
  // light_intensity = analogRead(A0);
  if (Serial.available()) {                             // comand given by input
    int header = (Serial.readStringUntil('-')).toInt(); //

    ReadingTempFunction(); // reading temperature function

    // HEADER-> 0:AT, 8:lights, 1:motors, 2:servo, 3:geiger, 4:gyro, 5:TPH, 6:magnetic
    // field

    switch (header) {

    case 0:

    case 8:                                  // lights
      setting = Serial.readStringUntil('-'); // (Manual / Automatic)
      comand = Serial.readStringUntil('\n'); //(On / Off)
      if (setting == "man") {                // manual control is setted
        comand = Serial.readStringUntil('\n');
        ManualLights(comand);
      }

      else if (setting == "aut") { // automatic control is setted
        AutomaticLights(light_intensity);
      }
      break;

    case 1: // motors
      motor1_vel_max =
          (Serial.readStringUntil('-')).toInt(); // between -255 and 255
      motor2_vel_max =
          (Serial.readStringUntil('\n')).toInt(); // between -255 and 255
      full_speed = 0;
      MotorFunction(PIN_ENABLE_MOTOR_1, PIN_INPUT_1_MOTOR_1,
                    PIN_INPUT_2_MOTOR_1, motor1_vel_max);
      MotorFunction(PIN_ENABLE_MOTOR_2, PIN_INPUT_3_MOTOR_2,
                    PIN_INPUT_4_MOTOR_2, motor2_vel_max);
      break;

    case 2: // servo
      remember == arm_theta;
      String sxstr = Serial.readStringUntil('/');
      Serial.println("x (mm): " + sxstr);
      sx = atof(sxstr.c_str());
      String systr = Serial.readStringUntil('/');
      Serial.println("y (mm): " + systr);
      sy = atof(systr.c_str());
      String szstr = Serial.readStringUntil('/');
      Serial.println("z (mm): " + szstr);
      sz = atof(szstr.c_str());
      String thetaFourstr = Serial.readStringUntil('\n');
      Serial.println("theta4 (mm): " + thetaFourstr);
      theta_four = atof(thetaFourstr.c_str());
      arm_theta[5] = 30;
      for (int i = 1; i <= 5; i++) {
        stop[i] = 0;
      }
      Angles(sx, sy, sz);
      for (int i = 1; i <= 5; i++) {
        ServoFunction(i, arm_theta[i], remember[i]);
      }
      break;

    case 3: // geiger
      // long start;
      int cont = 0;
      GeigerFunction(cont);
      break;
    case 4: // gyro
      String comand = Serial.readStringUntil(
          '-'); // request could be Angles or Acceleration
      if (comand == "get_Angles") {
        GetAngles();
      } else if (comand == "get_acceleration") {
        GetAcceleration();
      }
      break;

    case 5:             // TPH
      PrintValuesTPH(); // print Temperature, Pression, Humidity values
      break;

    case 6: // magnetic field
      MagneticFieldFunction();
      break;

    default:
      Serial.println("write the correct command please");
      break;
    }
  }
}

void AutomaticSettings() { // while none comand is given, automatic control is
                           // setted;
  while (Serial.available() == 0) {
    light_intensity = analogRead(A0);
    AutomaticLights(light_intensity);
  }
  powerOn = 1; // first comand recived; now this "while" won't be repeated
               // again; if automatic control is desired set it by input "aut"
  return;
}