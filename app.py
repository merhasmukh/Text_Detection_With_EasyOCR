from src.components.easy_ocr import EasyOCR
from src.components.open_cv import OpenCV
from src.components.pillow_img import PillowImg



image_path="./data/page0.jpg"
# EasyOCR.extract_all_text(image_path=image_path)
pixel=EasyOCR.get_text_region_pixel(image_path=image_path)
OpenCV.draw_bounding_box(image_path=image_path,pixels=pixel)
# PillowImg.draw_bounding_box_2(image_path=image_path)
