import cv2
import numpy as np
import os

import requests

'''
INFO SECTION
- if you want to monitor raw parameters of ESP32CAM, open the browser and go to http://192.168.x.x/status
- command can be sent through an HTTP get composed in the following way http://192.168.x.x/control?var=VARIABLE_NAME&val=VALUE (check varname and value in status)
'''

print(cv2.__file__)
# ESP32 URL
URL = "http://192.168.1.18"
AWB = True

# Se crasha dopo 2 tentativi tranquillo è normale!!!!!!!!!!!!!!!!!! :) Al terzo va bene

# Face recognition and opencv setup
cap = cv2.VideoCapture(URL + ":81/stream")
print('MAKE SURE TO RUN THIS CODE FROM Astra/khonsu/cam')
path = os.path.join(os.getcwd(), 'haarcascade_frontalface_alt.xml')
print(path)
face_classifier = cv2.CascadeClassifier(rf'{path}')

def set_resolution(url: str, index: int=1, verbose: bool=False):
    try:
        if verbose:
            resolutions = "10: UXGA(1600x1200)\n9: SXGA(1280x1024)\n8: XGA(1024x768)\n7: SVGA(800x600)\n6: VGA(640x480)\n5: CIF(400x296)\n4: QVGA(320x240)\n3: HQVGA(240x176)\n0: QQVGA(160x120)"
            print("available resolutions\n{}".format(resolutions))

        if index in [10, 9, 8, 7, 6, 5, 4, 3, 0]:
            requests.get(url + "/control?var=framesize&val={}".format(index))
        else:
            print("Wrong index")
    except:
        print("SET_RESOLUTION: something went wrong")

def set_quality(url: str, value: int=1, verbose: bool=False):
    try:
        if value >= 10 and value <=63:
            requests.get(url + "/control?var=quality&val={}".format(value))
    except:
        print("SET_QUALITY: something went wrong")

def set_awb(url: str, awb: int=1):
    try:
        awb = not awb
        requests.get(url + "/control?var=awb&val={}".format(1 if awb else 0))
    except:
        print("SET_QUALITY: something went wrong")
    return awb

def set_torch(url: str, value: int=1, verbose: bool=False):
    try:
        if value >= 0 and value <=255:
            requests.get(url + "/control?var=led_intensity&val={}".format(value))
        else:
            print('You inserted a wrong value')
    except:
        print("SET_QUALITY: something went wrong")

def set_effect(url: str, index: int=1, verbose: bool=False):
    try:
        if verbose:
                special_effects = "0: No Special Effects \n1: Negative \n2: Grey Scale \n3: Red Filter \n4: Green Filter \n5: Blue Filter\n6: Seppia Filter"
                print("Available Effects\n{}".format(special_effects))
        if index in [0, 1, 2, 3, 4, 5, 6]:
            requests.get(url + "/control?var=special_effect&val={}".format(index))
        else:
            print("Wrong index")
    except:
        print("SET_RESOLUTION: something went wrong")


if __name__ == '__main__':
    set_resolution(URL, index=8)

    while True:
        if cap.isOpened():
            ret, frame = cap.read()

            if ret:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                gray = cv2.equalizeHist(gray)

                faces = face_classifier.detectMultiScale(gray)
                for (x, y, w, h) in faces:
                    center = (x + w//2, y + h//2)
                    frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 4)

            cv2.imshow("frame", frame)

            key = cv2.waitKey(1)

            if key == ord('r'):
                idx = int(input("Select resolution index: "))
                set_resolution(URL, index=idx, verbose=True)

            elif key == ord('q'):
                val = int(input("Set quality (10 - 63): "))
                set_quality(URL, value=val)

            elif key == ord('a'):
                AWB = set_awb(URL, AWB)
            
            elif key == ord('e'):
                effect_indx = int(input("Select effect index: "))
                verbose = True
                set_effect(URL, index=effect_indx, verbose=True)


            elif key == ord('t'):
                val = int(input("Set torch intensity (0-255): "))
                set_torch(URL, value=val)

            elif key == ord('p'):
                break

    cv2.destroyAllWindows()
    cap.release()
