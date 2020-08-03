import cv2

cap = cv2.VideoCapture(0);

while (True):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)

    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    if cv2.waitKey(1) & 0xff == ord ('s'):
        break

cap.release()
cv2.destroyAllWindows()
