import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cv2.namedWindow("Test")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Test", frame)

    # Window closed?
    if cv2.getWindowProperty("Test", cv2.WND_PROP_VISIBLE) < 1:
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()