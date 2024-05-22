# MoleScale

MoleScale is a project that uses an Arduino, a Raspberry Pi, and the HX711 amplifier with a load cell to measure the amount of mols of a substance.

## Usage

* Download the repository
* Download the Arduino [HX711 library](https://www.arduino.cc/reference/en/libraries/hx711/) by Rob Tillaart
* Upload HX_calibration.ino to the Arduino and follow the instructions in the serial monitor
* Modify HX_molscale.ino according to the instructions during calibration and upload
* Connect the Arduino to the Raspberry Pi and run
```bash
python3 table.py
```
* on the Raspberry Pi

## For More Projects

Check out my [digital porfolio!](https://casparchen970.wordpress.com)
