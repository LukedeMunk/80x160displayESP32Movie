# 80x160 Display ESP32 Movie

Software to display videos on an Adafruit ST7735 display with an ESP32. Includes ESP32 software and a Python program to convert (160x80) videos into .ino files. The software is tested on the following boards:

* ESP32 DEVKIT V1

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

The software is written, compiled and uploaded using the Arduino IDE (v1.8.13). You could use the online Arduino IDE or other software, but I recommend using the version you can download on [this page](https://www.arduino.cc/en/software). In order to use the Arduino IDE as tool for uploading to the ESP, there are several steps to follow. Please visit the following tutorials:

* https://randomnerdtutorials.com/installing-the-esp32-board-in-arduino-ide-windows-instructions/

You also need Python. The software is tested in v3.10.0, you can download Python [here](https://www.python.org/downloads/).

### Installing

Needed libraries:

* [OpenCV](https://pypi.org/project/opencv-python/)

## Convert video into .ino file

Copy the video in the same folder as the `convert_video.py` file. Run `convert_video.py` and follow the steps. Make sure the video you convert is 160x80! After the conversion is done, upload on the ESP32.

## Hardware

You need an Adafruit ST7735 display and an ESP32 chip. In the `documentation` folder you can find a circuit diagram.

## Questions or feedback?

You can submit an issue if you have questions or feedback for this repository. If you are interested in more of my projects, checkout my GitHub [profile](https://github.com/LukedeMunk). If you are interested in hiring me, checkout my [LinkedIn](https://www.linkedin.com/in/luke-de-munk/).

## Authors

* **Luke de Munk** - *Head author* - [LinkedIn](https://www.linkedin.com/in/luke-de-munk/)