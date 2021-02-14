from PIL import Image
import os
import glob

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
file = "testbitmap"
f = open(os.path.join(__location__, file + ".h"), "w+")
frame_num = 0
for filename in glob.glob(__location__ + '/img/*.jpg'): #assuming jpg
    f.write("static const uint16_t " + file + str(frame_num) + "[] = {\n")

    
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
            color = r  g | b
            pad = str.format('0x{:04X}', int(hex(color), 16))
            f.write(pad + ", ")                 # Get the RGBA Value of the a pixel of an image
            i += 1
            if i > 15:
                i = 0
                f.write("\n")
    f.write("}; \n")
    
    frame_num += 1
for frame in range(0, frame_num):
    f.write("tft.drawRGBBitmap(0, 0, " + file + str(frame) + ", SCREEN_WIDTH, SCREEN_HEIGHT);\n")
print("Done")
f.close()


#pix[x,y] = value                # Set the RGBA Value of the image (tuple)