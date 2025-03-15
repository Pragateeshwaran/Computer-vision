import cv2

image = cv2.imread(r"images\Image.jpg")  

start = (0, 0)
end = (0, 0)
cropping = False

def mouse(event, x, y, flag, others):
    global start, end, cropping, image
    if event == cv2.EVENT_LBUTTONDOWN:
        start = (x, y)
        cropping = True
    if event == cv2.EVENT_MOUSEMOVE:
        if cropping:
            img = image.copy()
            cv2.rectangle(img, start, (x, y), (255, 0, 0), 2)
            cv2.imshow("img", img)
    if event == cv2.EVENT_LBUTTONUP:
        cropping = False
        end = (x, y)
        x1, y1 = start
        x2, y2 = end
        new_img = image[min(y1, y2):max(y1, y2), min(x1, x2):max(x1, x2)]
        cv2.imshow("new_img", new_img)

cv2.imshow("img", image)
cv2.setMouseCallback("img", mouse)
cv2.waitKey(0)
cv2.destroyAllWindows()