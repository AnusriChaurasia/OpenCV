import cv2 

#reading image in opencv
img= cv2.imread('Photos/b1.jpg')

#function to rescale an image
def resFram(frame, scale=0.10):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[1]*scale)
    dimension = (width,height)

    return cv2.resize(frame, dimension, interpolation=cv2.INTER_AREA)

resizeImg = resFram(img)
cv2.imshow('Baby', resizeImg)
cv2.waitKey(0)

#reading the video
video=cv2.VideoCapture('Videos/v1.3gp')

#reading the video frame by frame
while True:
    sTrue, frame = video.read()
    cv2.imshow('Video1',frame)
    #video is stopped using 'x' from keyboard
    if cv2.waitKey(1) & 0xFF==ord('x'):
        break

video.release()
cv2.destroyAllWindows()
