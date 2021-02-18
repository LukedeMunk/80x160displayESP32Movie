from PIL import Image
import glob
import cv2
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def main():
    makeDirectories()

    file = input("Videotitle: ")
    f = os.path.join(__location__, file + ".mp4")
    vidcap = cv2.VideoCapture(f)

    while vidcap.read()[0] == False:
        print("Video not found!")
        file = input("Videotitle: ")
        f = os.path.join(__location__, file + ".mp4")
        vidcap = cv2.VideoCapture(f)

    success, image = vidcap.read()
    count = 0

    while success:
        cv2.imwrite(os.path.join(__location__ + "/frames/", file + "_frame%d.jpg") % count, image)          #Save frame as JPEG file
        success, image = vidcap.read()
        #print("Read a new frame: ", success)
        count += 1
    
    print("Read " + str(count) + " frames")
    imageToBitmap()

def makeDirectories():
    if not os.path.exists(os.path.join(__location__, "frames")):
        os.makedirs(os.path.join(__location__, "frames"))
    
    if os.path.exists(os.path.join(__location__, "bitmap")):
        os.makedirs(os.path.join(__location__, "bitmaps"))

def imageToBitmap():
    bitmapName = input("Bitmap name: ")
    if os.path.isfile(os.path.join(__location__ + "/bitmaps/", bitmapName + ".h")):
        if input("File exists and will be overwritten, continue? (y/n) ") != "y":
            print("Process terminated")
            return

    f = open(os.path.join(__location__ + "/bitmaps/", bitmapName + ".h"), "w+")
    frame_num = 0
    for filename in glob.glob(__location__ + '/frames/*.jpg'):                                              #Assuming jpg
        f.write("static const uint16_t " + bitmapName + str(frame_num) + "[] = {\n")

        im = Image.open(filename)
        pix = im.load()
        width = im.size[0]
        height = im.size[1]
        i = 0

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
                f.write(pad + ", ")                 # Get the RGBA Value of the a pixel of an image
                i += 1
                if i > 15:
                    i = 0
                    f.write("\n")

        f.write("}; \n\n")
        
        frame_num += 1

    i = 0
    f.write("static const uint16_t " + bitmapName + "[] = {\n")
    
    for frame in range(0, frame_num):
        f.write(bitmapName + str(frame) + ", ")
        i += 1
        if i > 15:
            i = 0
            f.write("\n")
    f.write("};\n\n")

    f.write("for (uint16_t frame = 0; frame > NUM_FRAMES; frame++) {")
    f.write("\ttft.drawRGBBitmap(0, 0, " + bitmapName + "[frame], SCREEN_WIDTH, SCREEN_HEIGHT)\n")
    f.write("}")
    f.close()

    print("Done")

if __name__ == "__main__":
    main()