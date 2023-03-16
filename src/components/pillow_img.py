import sys
from PIL import Image, ImageDraw

class PillowImg:
    def draw_bounding_box(image_path):
        with Image.open(image_path) as im:

            draw = ImageDraw.Draw(im)
            draw.line((0, 0) + im.size, fill=128)
            draw.line((0, im.size[1], im.size[0], 0), fill=128)

            # write to stdout


            im.save(sys.stdout, "PNG")


    def draw_bounding_box_2(image_path):
            
            

    
    
        # importing image object from PIL
        import math
        from PIL import Image, ImageDraw
        
        w, h = 220, 190
        shape = [(40, 40), (w - 10, h - 10)]
        
        # creating new Image object
        # img = Image.new("RGB", (w, h))
        with Image.open(image_path) as im:
            # create rectangle image
            img1 = ImageDraw.Draw(im)  
            img1.rectangle(shape, outline ="red")
            im.show()