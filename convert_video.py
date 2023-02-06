########################################################################
#
# File:     video_converter.py
# Author:   Luke de Munk
# Purpose:  Converts 160x80 videos to .ino files. Upload the .ino file
#           to an ESP32 and connect an ST7735 to the chip. For more info
#           (including wiring) checkout: 
#           https://github.com/LukedeMunk/80x160displayESP32Movie
#
########################################################################
from PIL import Image
import glob
import cv2
import os

PATH = str(os.path.dirname(os.path.realpath(__file__)))                 #For editing files with python
video_path = PATH
num_frames = 0

########################################################################
#
#   @brief  Main program.
#
########################################################################
def main():
    global video_path
    global num_frames

    video_name = input("Videotitle to convert with extension (like example.mp4) NEEDS TO BE 160x80: ")
    video_file = os.path.join(PATH, video_name)
    vidcap = cv2.VideoCapture(video_file)

    while vidcap.read()[0] == False:
        print("Video not found")
        video_name = input("Videotitle to convert with extension (like example.mp4) NEEDS TO BE 160x80: ")
        video_file = os.path.join(PATH, video_name)
        vidcap = cv2.VideoCapture(video_file)

    video_name = os.path.splitext(video_name)[0]
    video_path = os.path.join(PATH, video_name)

    os.makedirs(os.path.join(video_path, "frames"))

    success, image = vidcap.read()
    count = 0

    print("Splitting video into frames")

    while success:
        cv2.imwrite(os.path.join(video_path, "frames", video_name + "_frame%d.jpg") % count, image)          #Save frame as jpg file
        success, image = vidcap.read()
        count += 1

        if count > 40:
            print("Memory limit reached. ESP32 cannot hold more frames")
            break

    num_frames = count

    print("Wrote " + str(count) + " frames")
    print("Converting frames into bitmaps")

    image_to_bitmap(video_name)

########################################################################
#
#   @brief  Reads frames as jpg and writes bitmaps to an .ino file
#
########################################################################
def image_to_bitmap(video_name):
    if os.path.isfile(os.path.join(video_path, video_name + ".ino")):
        if input("File exists and will be overwritten, continue? (y/n) ") != "y":
            print("Process terminated")
            return

    f = open(os.path.join(video_path, video_name + ".ino"), "w+")
    frame_num = 0
    
    print("Writing .ino file")

    f.write("/*\n")
    f.write(" * File:      " + video_name + ".ino\n")
    f.write(" * Author:    Luke de Munk\n")
    f.write(" * \n")
    f.write(" * Generated using convert_video.py.\n")
    f.write(" * Upload to an ESP32 and connect an ST7735 to the chip.\n")
    f.write(" * For more info (including wiring) checkout:\n")
    f.write(" * https://github.com/LukedeMunk/80x160displayESP32Movie\n")
    f.write(" */\n\n")
    f.write("#include <Adafruit_GFX.h>                         //Core graphics library\n")
    f.write("#include <Adafruit_ST7735.h>                      //Hardware-specific library for ST7735\n")
    f.write("#include <SPI.h>\n\n")
    f.write("#define SCLK_PIN        18                        //SPI clock (D18) Don't change\n")
    f.write("#define SDA_PIN         23                        //SPI data (D23) Don't change\n")
    f.write("#define DC_PIN          2                         //Register select (stands for Data Control perhaps!) (0 = command, 1 = display) (D2)\n")
    f.write("#define CS_PIN          5                         //Display enable (Chip select), if not enabled will not talk on SPI bus (D5)\n\n")
    f.write("#define RST_PIN         15                        //Display reset pin (D15)\n")
    f.write("#define BLK_PIN         4                         //Backlight control pin (0 = off, 1 = on) (D4)\n\n")
    f.write("#define SCREEN_WIDTH    160\n")
    f.write("#define SCREEN_HEIGHT   80\n\n")
    f.write("#define NUM_FRAMES      " + str(num_frames) + "\n\n")
    f.write("Adafruit_ST7735 tft = Adafruit_ST7735(CS_PIN, DC_PIN, RST_PIN);\n\n")
    
    for filename in glob.glob(video_path + '\\frames\\*.jpg'):                                              #Assuming jpg
        f.write("static const uint16_t " + video_name + str(frame_num) + "[] = {\n")
        im = Image.open(filename)
        pix = im.load()
        width = im.size[0]
        height = im.size[1]
        i = 0

        f.write("   ")
        for y in range(0, height):
            for x in range(0, width):
                color = ((pix[x,y][0] & 0xF8) << 8) | ((pix[x,y][1] & 0xFC) << 3) | (pix[x,y][2] >> 3)
                r = color & 0b1111100000000000
                g = color & 0b0000011111100000
                b = color & 0b0000000000011111
                r = r >> 11
                b = b << 11
                color = r | g | b
                pad = str.format('0x{:04X}', int(hex(color), 16))
                f.write(pad + ", ")
                i += 1
                if i > 15:
                    i = 0
                    f.write("\n")
                    f.write("    ")                    

        f.write("};\n\n")
        frame_num += 1

    i = 0
    f.write("static const uint16_t* " + video_name + "[] = {\n")
    
    for frame in range(0, frame_num):
        f.write(video_name + str(frame) + ", ")
        i += 1
        if i > 15:
            i = 0
            f.write("\n")
    f.write("};\n\n")

    f.write("/**************************************************************************/\n")
    f.write("/*!\n")
    f.write("  @brief    Setup ESP32.\n")
    f.write("*/\n")
    f.write("/**************************************************************************/\n")
    f.write("void setup(void) {\n")
    f.write("  tft.initR(INITR_MINI160x80);  // Init ST7735S mini display\n\n")
    f.write("  /* SPI speed defaults to SPI_DEFAULT_FREQ defined in the library, you can override it here\n")
    f.write("   * Note that speed allowable depends on chip and quality of wiring, if you go too fast, you\n")
    f.write("   * may end up with a black screen some times, or all the time.\n")
    f.write("   */\n")
    f.write("  //tft.setSPISpeed(40000000);\n\n")
    f.write("  \n")
    f.write("  //tft.setColRowStart(26, 1);\n")
    f.write("  tft.setRotation(3);\n")
    f.write("  tft.invertDisplay(true);\n")
    f.write("}\n\n")
    f.write("/**************************************************************************/\n")
    f.write("/*!\n")
    f.write("  @brief    Mainloop.\n")
    f.write("*/\n")
    f.write("/**************************************************************************/\n")
    f.write("void loop() {\n")
    f.write("   for (uint16_t frame = 0; frame < NUM_FRAMES; frame++) {\n")
    f.write("       tft.drawRGBBitmap(0, 0, " + video_name + "[frame], SCREEN_WIDTH, SCREEN_HEIGHT);\n")
    f.write("   }\n")
    f.write("}\n")

    f.close()

    print("Done")
    print("Now upload the .ino file to the ESP32")

if __name__ == "__main__":
    main()