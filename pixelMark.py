import cv2 as cv
import numpy as np
from pathlib import Path

imgPath = "Data/ocr-obb-label/192_crop_corners.jpg"
output = "Data/ocr-obb-label/corners/"
title_window = "Pixel Mark"

coors = []

index = 0


def mouse_callback(event, x, y, flags, params):
    if event == cv.EVENT_LBUTTONDOWN:
        global index
        cv.drawMarker(img, (x,y), (0,0,255), cv.MARKER_CROSS, 5)
        cv.putText(img, str(index), (x,y-5), cv.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,255))
        index+=1
        coors.append((x, y))
        print ((x, y))
        outputFile.write("{} {}\n".format(x,y))
        cv.imshow(title_window, img)


if __name__ == "__main__":
    inputPath = Path(imgPath)
    outputTxt = Path(output+inputPath.stem+".txt")
    
    print(outputTxt)
    
    img = cv.imread(str(inputPath),cv.IMREAD_COLOR)
    
    outputFile = open(str(outputTxt), "w")
    
    cv.namedWindow(title_window, cv.WINDOW_AUTOSIZE)

    cv.setMouseCallback(title_window, mouse_callback)
    
    cv.imshow(title_window, img)
    
    cv.waitKey()
    cv.destroyAllWindows()
    
    # for i in range(0, 10):
    #     x1, y1 = coors[i]
    #     x2, y2 = coors[i + 10]
    #     tan = (y2-y1)/(x2-x1)
    #     angle = np.rad2deg(np.arctan(tan))
    #     print(angle)
    #     outputFile.write("{}\n".format(angle))
    
    # cv.imwrite(str(outputImg), img)
    outputFile.close()