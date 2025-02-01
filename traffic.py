import cv2
import imutils
cascade_src='C:/Users/Ajith/Downloads/cars.xml'
car_cascade=cv2.CascadeClassifier(cascade_src)
cam=cv2.VideoCapture(0)
while True:
    _,img=cam.read()
    img=imutils.resize(img,width=500)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cars=car_cascade.detectMultiScale(gray,1.1,1)
    for(x,y,w,h)in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("Frame",img)

    b=str(len(cars))
    a=int(b)
    n=a
    print("--------------------")
    if n>=8:
        print("North more traffic, please on the red signal")
    else:
        print("no traffic")
    if cv2.waitKey(33)==27:
        break
cam.release()
cv2.destroyAllWindows()
    
