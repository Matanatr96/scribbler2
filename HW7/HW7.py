#############################################################################################
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Homework 5//////////////////////////////////////////////#
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Anush Mattapalli///////////////////////////////////////////#
#\\We worked on the homework assignment alone, using only this semester's course materials//#
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\amattapalli3@gatech.edu////////////////////////////////////////#
#\\\\\\\\\\\\\\\\\\\\\\cgbrandys22@gatech.edu - Colin Brandys///////////////////////////////#
#############################################################################################
from Myro import *

# Wibbly Wobbly
def screenShake():
    a = [10,20,30,40,50,60,70,80,90,100,110,120]
    gif = []
    pic = makePicture("Happy.jpg")
    pic2 = makePicture("White.jpg")

    for i in range(0,12):
        shift = a[i]
        pic2 = makePicture("White.jpg")
        for x in range(0,getWidth(pic)):
            for y in range(0,getHeight(pic)):
                pix = getPixel(pic,x,y)
                r = getRed(pix)
                g = getGreen(pix)
                b = getBlue(pix)
                #get the pixels from the original picture
                if (i % 2) == 0:
                    pix = getPixel(pic2,x, shift + y)

                else:
                    pix = getPixel(pic2,x + shift, y)

                setRed(pix,r)
                setGreen(pix,g)
                setBlue(pix,b)
                # if not in that range, shift them over 30 pixels and copy the pixel over.

        show(pic2)
        gif.append(pic2)
        #wait(1)# slow down so i can see


    savePicture(gif,"Shake.gif")
    a = fade(gif)
    savePicture(a,"Shaking Fade.gif")

# Moving Fade!!!!! == EXTRA AWESOME
def fade(picList):
    pics = len(picList)
    for i in range(0,pics):
        p = picList[i]
        pic2 = copyPicture(p)
        for x in range(0,getWidth(pic2)):
            for y in range(0,getHeight(pic2)):
                pix = getPixel(pic2,x,y)
                r = getRed(pix)
                g = getGreen(pix)
                b = getBlue(pix)
                per = 255 / pics
                setRed(pix,r - per * (i+1))
                setGreen(pix,g - per * (i+1))
                setBlue(pix,b - per * (i+1))
        show(pic2)
        picList.append(pic2)
    return picList

def seeingRed():
    picture = makePicture("Anchorman.PNG")
    show(picture)
    for pixel in getPixels(picture):
        setRed(pixel, 255)

def overLay():
    pic = makePicture("flying cat.PNG")
    show(pic)
    for x in range(100, 120):
        for y in range(80,200):
            pix= getPixel(pic,x,y)
            setRed(pix, 255)
            setBlue(pix,0)
            setGreen(pix,0)
    for x in range(160, 180):
        for y in range(80,200):
            pix= getPixel(pic,x,y)
            setRed(pix, 255)
            setBlue(pix,0)
            setGreen(pix,0)
    for x in range(80, 200):
        for y in range(100,120):
            pix= getPixel(pic,x,y)
            setRed(pix, 255)
            setBlue(pix,0)
            setGreen(pix,0)
    for x in range(80, 200):
         for y in range(160,180):
            pix= getPixel(pic,x,y)
            setRed(pix, 255)
            setBlue(pix,0)
            setGreen(pix,0)
    show(pic)



def lensFlare():
    pic = makePicture("kitten 2.PNG")
    show(pic)
    for x in range(500, 550):
        for y in range(500,550):
            pix= getPixel(pic,x,y)
            setRed(pix, 220)
            setBlue(pix,220)
            setGreen(pix,220)
    for x in range(502, 548):
        for y in range(502,548):
            pix= getPixel(pic,x,y)
            setRed(pix, 230)
            setBlue(pix,230)
            setGreen(pix,230)
    for x in range(504, 546):
        for y in range(504,546):
            pix= getPixel(pic,x,y)
            setRed(pix, 240)
            setBlue(pix,240)
            setGreen(pix,240)
    for x in range(506, 544):
        for y in range(506,544):
            pix= getPixel(pic,x,y)
            setRed(pix, 245)
            setBlue(pix,245)
            setGreen(pix,248)
    for x in range(508, 542):
        for y in range(508,542):
            pix= getPixel(pic,x,y)
            setRed(pix, 250)
            setBlue(pix,250)
            setGreen(pix,250)
    for x in range(510, 540):
        for y in range(510,540):
            pix= getPixel(pic,x,y)
            setRed(pix, 252)
            setBlue(pix,252)
            setGreen(pix,252)
    for x in range(520, 530):
        for y in range(520,530):
            pix= getPixel(pic,x,y)
            setRed(pix, 255)
            setBlue(pix,255)
            setGreen(pix,255)


def negativeColors():
# So this is our make your own function.It makes a
# negative colors picture. If you'd like to change
# the picture simply change "kitten 3.PNG" to some
# other picture. Otherwise it'll simply change a
# cute picture of a kitten in a tea cup into a
# terrifying negative version that looks almost like
# a demon of some kind. Regardless, it can make
# anything scarier (except a solid color photo which
# will just be a different color). The function itself
# was probably twice as difficult as seeing red to
# write, and has some great use and cool applications
# thus I think 25 points would be a fair point value.
    from Myro import *
    scaryPhoto = makePicture("kitten 3.PNG")
    show(scaryPhoto)
    for pix in getPixels(scaryPhoto):
        r = getRed(pix)
        g = getGreen(pix)
        b = getBlue(pix)
        R=255-int(r)
        B=255-int(b)
        G=255-int(g)
        setRed(pix,R)
        setBlue(pix,B)
        setGreen(pix,G)

# Calling screenshake will make a screenshake gif
# and then make a fading version of that
# and to top it all off, saves them too
#screenShake()


