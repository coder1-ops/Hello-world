import image

img = image.Image("goldygopher.png")
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
img.setDelay(1,15)   # setDelay(0) turns off animation

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col,row)
        
        red=p.getRed()
        green=p.getGreen()
        blue=p.getBlue()
        
        avg = (red+green+blue)/3
        
        new = image.Pixel(avg,avg,avg)
        
        img.setPixel(col,row,new)
        
img.draw(win)
win.exitonclick()
