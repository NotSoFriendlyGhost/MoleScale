#include "HX711.h"

HX711 scale;

//uint8_t dataPin = 6;
//uint8_t clockPin = 7;
uint8_t dataPin  = 3;//for esp32
uint8_t clockPin = 2;//for esp32

void setup()
{
  Serial.begin(9600);

  scale.begin(dataPin, clockPin);
  scale.set_offset(70007);
  scale.set_scale(453.962493);
}


void loop()
{
  if(Serial.read() == 'T'){
    scale.tare();
  }
  Serial.println(scale.get_units(10));
  delay(250);
}


// -- END OF FILE --


