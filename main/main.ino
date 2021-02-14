#include <Adafruit_GFX.h>    // Core graphics library
#include <Adafruit_ST7735.h> // Hardware-specific library for ST7735
#include <SPI.h>

#include "testbitmap.h"

#define SCLK_PIN  18        //SPI clock (D18) Don't change
#define SDA_PIN   23        //SPI data (D23) Don't change
#define DC_PIN    2         //Register select (stands for Data Control perhaps!) (0 = command, 1 = display) (D2)
#define CS_PIN    5         //Display enable (Chip select), if not enabled will not talk on SPI bus (D5)

#define RST_PIN   15        //Display reset pin (D15)
#define BLK_PIN   4         //Backlight control pin (0 = off, 1 = on) (D4)

#define SCREEN_WIDTH  160
#define SCREEN_HEIGHT 80

Adafruit_ST7735 tft = Adafruit_ST7735(CS_PIN, DC_PIN, RST_PIN);

void setup(void) {
  tft.initR(INITR_MINI160x80);  // Init ST7735S mini display
  
  // SPI speed defaults to SPI_DEFAULT_FREQ defined in the library, you can override it here
  // Note that speed allowable depends on chip and quality of wiring, if you go too fast, you
  // may end up with a black screen some times, or all the time.
  //tft.setSPISpeed(40000000);
  
  tft.setColRowStart(26, 1);
  tft.setRotation(3);
  tft.invertDisplay(true);

}

void loop() {
  tft.drawRGBBitmap(0, 0, testbitmap0, SCREEN_WIDTH, SCREEN_HEIGHT);
  tft.drawRGBBitmap(0, 0, testbitmap1, SCREEN_WIDTH, SCREEN_HEIGHT);
  tft.drawRGBBitmap(0, 0, testbitmap2, SCREEN_WIDTH, SCREEN_HEIGHT);
  tft.drawRGBBitmap(0, 0, testbitmap3, SCREEN_WIDTH, SCREEN_HEIGHT);
  tft.drawRGBBitmap(0, 0, testbitmap4, SCREEN_WIDTH, SCREEN_HEIGHT);
  tft.drawRGBBitmap(0, 0, testbitmap5, SCREEN_WIDTH, SCREEN_HEIGHT);
  tft.drawRGBBitmap(0, 0, testbitmap6, SCREEN_WIDTH, SCREEN_HEIGHT);
  tft.drawRGBBitmap(0, 0, testbitmap7, SCREEN_WIDTH, SCREEN_HEIGHT);
  tft.drawRGBBitmap(0, 0, testbitmap8, SCREEN_WIDTH, SCREEN_HEIGHT);
  tft.drawRGBBitmap(0, 0, testbitmap9, SCREEN_WIDTH, SCREEN_HEIGHT);
  tft.drawRGBBitmap(0, 0, testbitmap10, SCREEN_WIDTH, SCREEN_HEIGHT);
  tft.drawRGBBitmap(0, 0, testbitmap11, SCREEN_WIDTH, SCREEN_HEIGHT);
  tft.drawRGBBitmap(0, 0, testbitmap12, SCREEN_WIDTH, SCREEN_HEIGHT);
  tft.drawRGBBitmap(0, 0, testbitmap13, SCREEN_WIDTH, SCREEN_HEIGHT);
  tft.drawRGBBitmap(0, 0, testbitmap14, SCREEN_WIDTH, SCREEN_HEIGHT);
  tft.drawRGBBitmap(0, 0, testbitmap15, SCREEN_WIDTH, SCREEN_HEIGHT);
  tft.drawRGBBitmap(0, 0, testbitmap16, SCREEN_WIDTH, SCREEN_HEIGHT);
  tft.drawRGBBitmap(0, 0, testbitmap17, SCREEN_WIDTH, SCREEN_HEIGHT);
  tft.drawRGBBitmap(0, 0, testbitmap18, SCREEN_WIDTH, SCREEN_HEIGHT);
  tft.drawRGBBitmap(0, 0, testbitmap19, SCREEN_WIDTH, SCREEN_HEIGHT);
  tft.drawRGBBitmap(0, 0, testbitmap20, SCREEN_WIDTH, SCREEN_HEIGHT);
  tft.drawRGBBitmap(0, 0, testbitmap21, SCREEN_WIDTH, SCREEN_HEIGHT);
  tft.drawRGBBitmap(0, 0, testbitmap22, SCREEN_WIDTH, SCREEN_HEIGHT);
  tft.drawRGBBitmap(0, 0, testbitmap23, SCREEN_WIDTH, SCREEN_HEIGHT);
  tft.drawRGBBitmap(0, 0, testbitmap24, SCREEN_WIDTH, SCREEN_HEIGHT);
  tft.drawRGBBitmap(0, 0, testbitmap25, SCREEN_WIDTH, SCREEN_HEIGHT);
  tft.drawRGBBitmap(0, 0, testbitmap26, SCREEN_WIDTH, SCREEN_HEIGHT);
  tft.drawRGBBitmap(0, 0, testbitmap27, SCREEN_WIDTH, SCREEN_HEIGHT);
  tft.drawRGBBitmap(0, 0, testbitmap28, SCREEN_WIDTH, SCREEN_HEIGHT);
  tft.drawRGBBitmap(0, 0, testbitmap29, SCREEN_WIDTH, SCREEN_HEIGHT);
  tft.drawRGBBitmap(0, 0, testbitmap30, SCREEN_WIDTH, SCREEN_HEIGHT);
  tft.drawRGBBitmap(0, 0, testbitmap31, SCREEN_WIDTH, SCREEN_HEIGHT);
}
