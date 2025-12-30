from ultralytics import YOLO
import cv2

model = YOLO("bestv8.pt")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise RuntimeError("Kamera açılamadı. Doğru indexi dene (0,1,2) veya izinleri kontrol et.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Kare okunamadı, çıkılıyor.")
        break

    
    results = model.predict(frame, conf=0.5, imgsz=640, verbose=False)


    annotated = results[0].plot()

    cv2.imshow("YOLOv8 Camera", annotated)

   
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
