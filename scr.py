import numpy as np
import cv2

cap = cv2.VideoCapture(0)

(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
#cap.set(5, 60)

fourcc = cv2.VideoWriter_fourcc('I','4','2','0')
#fourcc = cv2.VideoWriter_fourcc(*'MPEG')
if int(major_ver)  < 3 :
    fps = cap.get(cv2.cv.CV_CAP_PROP_FPS)
    print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
else :
    fps = cap.get(cv2.CAP_PROP_FPS)
    print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))

out = cv2.VideoWriter('out.mp4',fourcc, fps, (640,360))

count = 0;

while(cap.isOpened()):
    #cap.set(5, 60)
    ret, frame = cap.read()

    k = cv2.waitKey(1) & 0xFF

    #if (count > 128):
	#    break;
    if k == 27:
        break

    if ret==True:
        #frame = cv2.flip(frame,0)
        cv2.imshow('frame',frame)
        out.write(frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    else:
        break

    count+=1;        

cap.release()
out.release()
cv2.destroyAllWindows()

