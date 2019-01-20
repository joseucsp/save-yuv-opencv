import numpy as np
import cv2

#cap = cv2.VideoCapture("output.mp4")
cap = cv2.VideoCapture(0)
"""
(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
cap.set(5, 60)

fourcc = cv2.VideoWriter_fourcc('I','4','2','0')
"""
def printFPS(cap):
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
    if int(major_ver)  < 3 :
        fps = cap.get(cv2.cv.CV_CAP_PROP_FPS)
        print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
    else :
        fps = cap.get(cv2.CAP_PROP_FPS)
        print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))

#out = cv2.VideoWriter('output.avi',fourcc, fps, (640,480))
count = 0
cnt   = 1
while(cap.isOpened()):
    ret, frame = cap.read()
    k = cv2.waitKey(1) & 0xFF
    #printFPS(cap)
    if ret==True:
        #frame = cv2.flip(frame,0)
        cv2.imshow('frame',frame)
        count += 1
        #out.write(frame)
        if  k == 27:
            break
    else:
        break

    if k == ord('c'):
        cv2.imwrite('tmp'+str(cnt)+'.png', frame)
        cnt += 1

        
cap.release()
#out.release()
cv2.destroyAllWindows()

print("frames : ", count)
