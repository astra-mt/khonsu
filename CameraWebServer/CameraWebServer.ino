#include "esp_camera.h"  // Camera
#include <WiFi.h>        // for Wi-Fi
#include "Arduino.h"     // for general functionalities
#include <SD.h>          // SD card
#include "FS.h"          //File System
#include "soc/soc.h"
#include "soc/rtc_cntl_reg.h"
#include "soc/rtc_io.h"
#include "EEPROM.h"  // Flash memory
#include "time.h"      // Time functions


//HOW IMAGE IS DECIDED TO BE TAKEN
#define USE_INCREMENTAL_FILE_NUMBERING  // Uses flash memory to store file (pictures)
//#define USE_TIMESTAMP // Through wi-fi current time saved on every picture taken

//only one have to be commented in order to work properly
/*#define TIME_MODE // Photo taken with constant delay*/
#define TRIGGER_MODE  //Photo capture triggered by GPIO pin rising/falling


//CONSTANTS
const byte ledPin = GPIO_NUM_33;      //ledPin CAMERA ON OR OFF
const byte flashPin = GPIO_NUM_4;     //FLASH FOR LOW LIGHT
const byte triggerPin = GPIO_NUM_13;  //Triggercamera Pin
const byte flashPower = 1;

#ifdef TIMED_MODE
  const int timeLapseInterval = 30; //seconds between successive shots in TIMELAPSE MODE
#endif

const int startupDelayMillis = 3000;  // Little delay after initializing to be sure it is done correctly in milliseconds



//GLOBALS
int pictureNumber = 0; //Keep track of number of photoes taken
String path; //Full paht of filename of the last photo saved


// ===================
// Select camera model
// ===================
//#define CAMERA_MODEL_WROVER_KIT // Has PSRAM
//#define CAMERA_MODEL_ESP_EYE // Has PSRAM
//#define CAMERA_MODEL_ESP32S3_EYE // Has PSRAM
//#define CAMERA_MODEL_M5STACK_PSRAM // Has PSRAM
//#define CAMERA_MODEL_M5STACK_V2_PSRAM // M5Camera version B Has PSRAM
//#define CAMERA_MODEL_M5STACK_WIDE // Has PSRAM
//#define CAMERA_MODEL_M5STACK_ESP32CAM // No PSRAM
//#define CAMERA_MODEL_M5STACK_UNITCAM // No PSRAM
#define CAMERA_MODEL_AI_THINKER  // Has PSRAM
//#define CAMERA_MODEL_TTGO_T_JOURNAL // No PSRAM
// ** Espressif Internal Boards **
//#define CAMERA_MODEL_ESP32_CAM_BOARD
//#define CAMERA_MODEL_ESP32S2_CAM_BOARD
//#define CAMERA_MODEL_ESP32S3_CAM_LCD

#include "camera_pins.h"

// ===========================
// Enter your WiFi credentials
// ===========================

// Casa Marco
// const char* ssid = "Wind3 HUB-2BB528";
// const char* password = "21hgqxxaygwl6vh7";

// Casa Enf
const char* ssid = "Wind3 HUB-58B2D9";
const char* password = "Gambascawifi";

void startCameraServer();
void setupLedFlash(int pin);

void sleep() {
  pinMode(triggerPin, INPUT_PULLDOWN);
  gpio_hold_en(GPIO_NUM_4);   //remember the status of flashPin, so it doesn't turn accidentaly on while sleeping
    digitalWrite(ledPin, HIGH);  //turn off the led (it is active low led)
  delay(1000);

#ifdef TRIGGER_MODE
  esp_sleep_enable_ext0_wakeup(GPIO_NUM_13, 1); //turn on camera when signal is high on 13 (use 0 if you want to turn on when the signal is low)
  //esp_sleep_enable_ext() _wakeup(GPIO_NUM_13, 0);
#endif

#ifdef TIME_MODE
    esp_sleep_enable_timer_wakeup(timeLapseInterval * 100000000)
    */
  //da usare se si vuole il controlo con il timer
  Serial.println("Camera is sleeping now");
  esp_deep_sleep_start();  //function that starts the deep sleep of the esp 32 module
#endif
}


void setup() {
  //control that module is working
  pinMode(ledPin, OUTPUT);
    digitalWrite(ledPin, LOW);  //turn on the led (it is active low led)
    
    
    //WRITE_PERI_REG(REC_CNTL_BROW_OUT_REG, 0);


    Serial.begin(115200);
  Serial.setDebugOutput(true);
  Serial.println();

  camera_config_t config;
  config.ledc_channel = LEDC_CHANNEL_0;
  config.ledc_timer = LEDC_TIMER_0;
  config.pin_d0 = Y2_GPIO_NUM;
  config.pin_d1 = Y3_GPIO_NUM;
  config.pin_d2 = Y4_GPIO_NUM;
  config.pin_d3 = Y5_GPIO_NUM;
  config.pin_d4 = Y6_GPIO_NUM;
  config.pin_d5 = Y7_GPIO_NUM;
  config.pin_d6 = Y8_GPIO_NUM;
  config.pin_d7 = Y9_GPIO_NUM;
  config.pin_xclk = XCLK_GPIO_NUM;
  config.pin_pclk = PCLK_GPIO_NUM;
  config.pin_vsync = VSYNC_GPIO_NUM;
  config.pin_href = HREF_GPIO_NUM;
  config.pin_sscb_sda = SIOD_GPIO_NUM;
  config.pin_sscb_scl = SIOC_GPIO_NUM;
  config.pin_pwdn = PWDN_GPIO_NUM;
  config.pin_reset = RESET_GPIO_NUM;
  config.xclk_freq_hz = 20000000;
  config.frame_size = FRAMESIZE_UXGA;
  config.pixel_format = PIXFORMAT_JPEG;  // for streaming
  //config.pixel_format = PIXFORMAT_RGB565; // for face detection/recognition
  config.grab_mode = CAMERA_GRAB_WHEN_EMPTY;
  config.fb_location = CAMERA_FB_IN_PSRAM;
  config.jpeg_quality = 12;
  config.fb_count = 1;

  // if PSRAM IC present, init with UXGA resolution and higher JPEG quality
  //                      for larger pre-allocated frame buffer.
  if (config.pixel_format == PIXFORMAT_JPEG) {
    if (psramFound()) {
      config.jpeg_quality = 10;
      config.fb_count = 2;
      config.grab_mode = CAMERA_GRAB_LATEST;
    } else {
      // Limit the frame size when PSRAM is not available
      config.frame_size = FRAMESIZE_UXGA;  //see all frame size possible on documentation
      config.fb_location = CAMERA_FB_IN_DRAM;
    }
  } else {
    // Best option for face detection/recognition
    config.frame_size = FRAMESIZE_240X240;
#if CONFIG_IDF_TARGET_ESP32S3
    config.fb_count = 2;
#endif
  }
  //Flash setting
  ledcSetup(7, 5000, 8);
  ledcAttachPin(4, 7);
  ledcWrite(7, flashPower);

#if defined(CAMERA_MODEL_ESP_EYE)
  pinMode(13, INPUT_PULLUP);
  pinMode(14, INPUT_PULLUP);
#endif

  // camera init
  esp_err_t err = esp_camera_init(&config);
  if (err != ESP_OK) {
    Serial.printf("Camera init failed with error 0x%x", err);
    Serial.println("Camera is going to sleep to avoid errors");
    sleep();
  }
  // for all the possible settings see video min 48:50
  sensor_t* s = esp_camera_sensor_get();
  // initial sensors are flipped vertically and colors are a bit saturated
  if (s->id.PID == OV3660_PID) {
    s->set_vflip(s, 1);        // flip it back
    s->set_brightness(s, 1);   // up the brightness just a bit
    s->set_saturation(s, -2);  // lower the saturation
  }
  // drop down frame size for higher initial frame rate
  if (config.pixel_format == PIXFORMAT_JPEG) {
    s->set_framesize(s, FRAMESIZE_QVGA);
  }

#if defined(CAMERA_MODEL_M5STACK_WIDE) || defined(CAMERA_MODEL_M5STACK_ESP32CAM)
  s->set_vflip(s, 1);
  s->set_hmirror(s, 1);
#endif

#if defined(CAMERA_MODEL_ESP32S3_EYE)
  s->set_vflip(s, 1);
#endif

// Setup LED FLash if LED pin is defined in camera_pins.h
#if defined(LED_GPIO_NUM)
  setupLedFlash(LED_GPIO_NUM);
#endif

  WiFi.begin(ssid, password);
  WiFi.setSleep(false);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");

  startCameraServer();

  Serial.print("Camera Ready! Use 'http://");
  Serial.print(WiFi.localIP());
  Serial.println("' to connect");
}

void loop() {
  // Do nothing. Everything is done in another task by the web server
  delay(10000);
}
