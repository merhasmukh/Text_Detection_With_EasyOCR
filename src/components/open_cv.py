import cv2

class OpenCV:
    def __init__(self):
        pass
    def draw_bounding_box(image_path,pixels):
        try:
            
            # cv2.rectangle(image_path, start_point, end_point, color=(0,255,0), thickness=2)
            x=pixels[0][0][0]
            y=pixels[0][0][1]
            w=pixels[0][1][0]
            h=pixels[0][2][1]

            img=cv2.imread(image_path)
            print(x,y,h,w)
            cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,255),2)
            print("write image")
            cv2.imwrite('result.jpg',img)
            print("sucessfull")
            cv2.imshow("Show",img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            cv2.imwrite('result.jpg',img)

        except:
            pass