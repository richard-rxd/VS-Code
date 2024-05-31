from ultralytics import YOLO

model = YOLO('Football Project/Models/best.pt')

result = model.predict('Football Project/Football Analysis/Input/08fd33_4.mp4', save=True)
print(result[0])
print("===================================")
for box in result[0].boxes:
    print(box)