
import cv2
import pyautogui
from typing import TypeAlias

GriddyVariable:TypeAlias = int
XYranges:TypeAlias = tuple[list,list]

def tunicate(source:int)->int:

    check = source
    variable = str(round(source,-2))
    lenOfVariable = len(variable)
    firstIntOfVariable = variable[0]
    rangeFromLastTo3ndFromFirst = variable[-lenOfVariable+2:lenOfVariable]
    result = int(firstIntOfVariable+"0"+rangeFromLastTo3ndFromFirst)
    if result <= check: return result
def gridifyDimentions(hight:int,width:int)->tuple[int:int]:
    return (tunicate(hight),tunicate(width))
def DimentionedRanges(hight:GriddyVariable,width:GriddyVariable)->XYranges:
    return (list(range(0,hight,int(hight/10))),list(range(0,width,int(width/10))))

screenW,screenH = pyautogui.size()
screenW,screenH = gridifyDimentions(screenW,screenH)
RANGExD,RANGEyD = DimentionedRanges(screenW,screenH)
widthD,hightD = pyautogui.size()
#-

image = cv2.imread("whiteCloth.jpeg")
image = cv2.resize(image, (widthD,hightD), interpolation = cv2.WINDOW_FULLSCREEN)#width and hight is new order not hight width
###
for everyx,everyy in zip(RANGExD,RANGEyD):
    print(everyx,everyy)
    image = cv2.putText(image, str((everyx,everyy)),
                        (everyx,everyy), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=.54,color=(0,0,0),thickness=2)
    image = cv2.circle(image, (everyx,everyy),3,color=(255,28,202),thickness=2)#b,g,r
    
###
cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
cv2.imshow("window",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
exit()

'''
while True:
    cv2.imshow("Press q to close!", image)
    cv2.resizeWindow(winname="Press q to close!", width=widthD,height=hightD)
    if cv2.waitKey(0) & 0xFF == ord('q'):
            break
cv2.destroyAllWindows()
exit()
'''
'''
while True:
    Mx, My = pyautogui.position()
    r,g,b = pyautogui.pixel(Mx,My)
    print(f"At ({Mx},{My}) : The Color is ({r},{g},{b}).")
'''
