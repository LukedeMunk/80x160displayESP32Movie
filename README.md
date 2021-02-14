# 80x160displayESP32Movie
Software to display video's on an Adafruit ST7735 display with an ESP32. Includes ESP32 software and a Python program to convert video's in bitmaps. The video needs to be in bitmap format to be shown.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

The software is written, compiled and uploaded using the Arduino IDE (v1.8.13). You could use the online Arduino IDE or other software, but I recommend using the version you can download on [this page](https://www.arduino.cc/en/software).
You also need Python. The software is tested in v3.9.0, you can download Python [here](https://www.python.org/downloads/).

### Installing

Needed libraries:
* 1
* 2

## Hardware

You need an Adafruit ST7735 display and an ESP32 chip. Other chips or displays (with adjusted code) may work, but I can't guarantee that.

### Pin connections

| ESP32     | Display   |
|-----------|-----------|
| 5V        | VCC       |
| GND       | GND       |
| A5        | SCL       |
| A4        | SDA       |


## Questions or feedback?

You can submit an issue if you have questions or feedback for this repository. If you are interested in more of my projects, checkout my GitHub [profile](https://github.com/LukedeMunk). If you are interested in hiring me, checkout my [website](https://munkservices.com) or [LinkedIn](https://www.linkedin.com/in/luke-de-munk/).

## Authors

* **Luke de Munk** - *Head author* - [LinkedIn](https://www.linkedin.com/in/luke-de-munk/)

<!-- ## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details -->