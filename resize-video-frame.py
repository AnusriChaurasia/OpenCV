import cv2

#function to rescale an video
def resFram(frame, scale=0.50):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimension = (width,height)

    return cv2.resize(frame, dimension, interpolation=cv2.INTER_AREA)

def changeResol(width,height):
    #live video
    capture.set(3,width)
    capture.set(4,height)
    
#reading the video
video=cv2.VideoCapture('Videos/v1.3gp')

#For webcam
video.open(0, cv2.CAP_DSHOW)

#reading the video frame by frame
while True:
    sTrue, frame = video.read()
    frame_res = resFram(frame)

    #read from webcam
    cv2.imshow('Video1',frame)
    
    #display video in resized frame
    cv2.imshow('Video Resized', frame_res)

    #video is stopped using 'd' from keyboard
    if cv2.waitKey(20) & 0xFF==ord('x'):
        break

video.release()
cv2.destroyAllWindows()