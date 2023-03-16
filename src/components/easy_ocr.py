import easyocr

class EasyOCR:
    def __init__(self):
        pass
    def extract_all_text(image_path):
        try:
            reader = easyocr.Reader(['en'])

            result = reader.readtext(image_path,detail = 0, paragraph=True)
            print(result)
            return result
        except:
            pass


    def get_text_region_pixel(image_path):
        try:
            reader = easyocr.Reader(['en'])

            result=reader.readtext(image_path, paragraph=True)
            pixels=result[3]
            print(result[3])
            return pixels
        except:
            pass