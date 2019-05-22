#Certificate

from PIL import Image, ImageDraw, ImageFont
 

 
image = Image.open('White.jpg')
 
# initialise the drawing context with
# the image object as background
 
draw = ImageDraw.Draw(image)

font = ImageFont.truetype('comicbd.ttf', size=55)
 
# starting position of the message
 
(x, y) = (130, 0)
message = "CERTIFICATE"
color = 'rgb(153, 50, 204)' # black color
 
# draw the message on the background
 
draw.text((x, y), message, fill=color, font=font)
str1 = input()
draw.text((120,200), """This is to certify that """ + str1 + 
          """ has 
   completed training in ML & AI
 at Forsk Summer Boot Camp 2019.""", 'rgb(128,0,128)', ImageFont.truetype('Georgia.ttf', size=40))

image.save( 'certi.pdf', "PDF", resolution=100)
#image.save('text_forsk.jpg')

#(x, y) = (150, 150)
#name = 'Vinay'
#color = 'rgb(255, 255, 255)' # white color
#draw.text((x, y), name, fill=color, font=font)
# 
#draw.text(())
 


img = Image.open("Forsk_logo_bw.png")
w,h = img.size
img=img.resize((w/50, h/2))
img.save('Forsk_logo_bw.png')






image.paste(img, (0,0))

photo = Image.open(input_image_path)
 
    # make the image editable
    drawing = ImageDraw.Draw(photo)
 
    black = (3, 8, 12)
    font = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 40)
    drawing.text(pos, text, fill=black, font=font)
    photo.show()
    photo.save(output_image_path)
 
 