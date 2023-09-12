import cv2 as cv
from pathlib import Path

imgPath = "./input/cccdc_front_1.jpg"
title_window = "Pixel Mark"

coor = list()

index = 0

def mouse_callback(event, x, y, flags, params):
    if event == cv.EVENT_LBUTTONDOWN:
        global index
        cv.drawMarker(img, (x,y), (0,0,255), cv.MARKER_CROSS, 5)
        cv.putText(img, str(index), (x,y-5), cv.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,255))
        index+=1
        coor.append((x, y))
        print ((x, y))
        outputFile.write("{} {}\n".format(x,y))
        cv.imshow(title_window, img)

if __name__ == "__main__":
    inputPath = Path(imgPath)
    outputTxt = Path("output/"+inputPath.stem+".txt")
    outputImg = Path("output/"+inputPath.stem+".jpg")
    
    img = cv.imread(str(inputPath),cv.IMREAD_COLOR)
    
    outputFile = open(str(outputTxt), "w")
    
    cv.namedWindow(title_window, cv.WINDOW_AUTOSIZE)

    cv.setMouseCallback(title_window, mouse_callback)
    
    cv.imshow(title_window, img)
    cv.waitKey(0)
    cv.imwrite(str(outputImg), img)
    outputFile.close()
    cv.destroyAllWindows()
    
    cv.waitKey()
        
    cv.destroyAllWindows()
