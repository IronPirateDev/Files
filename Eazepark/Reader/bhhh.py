import cv2

# Initialize global variables
selecting = False
x1, y1, x2, y2 = -1, -1, -1, -1

def draw_rectangle(event, x, y, flags, param):
    global selecting, x1, y1, x2, y2
    
    if event == cv2.EVENT_LBUTTONDOWN:
        selecting = True
        x1, y1 = x, y
    
    elif event == cv2.EVENT_LBUTTONUP:
        selecting = False
        x2, y2 = x, y
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.imshow('Select License Plate', frame)

# Open the camera
cap = cv2.VideoCapture(0)

cv2.namedWindow('Select License Plate')
cv2.setMouseCallback('Select License Plate', draw_rectangle)

while True:
    ret, frame = cap.read()
    
    if selecting:
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
    
    cv2.imshow('Select License Plate', frame)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('s'):
        print(f'Selected Region: x1={x1}, y1={y1}, x2={x2}, y2={y2}')
        
cap.release()
cv2.destroyAllWindows()
