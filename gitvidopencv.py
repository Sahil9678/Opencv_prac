import cv2          # Import open cv
video_file_path = "F:\\dynamic warm up.mp4"

cap = cv2.VideoCapture(video_file_path)

ret, frame = cap.read()
print 'Read data:', ret    # True
while ret:
    ret, frame = cap.read()
    # Converts color image to grayscale
    # grayscaled_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if ret == True:
        cv2.imshow('Video Title', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        print 'No frame!'  # Video
        break

cap.release()
cv2.destroyAllWindows()