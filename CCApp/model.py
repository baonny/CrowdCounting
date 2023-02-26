import cv2, sys
from ultralytics import YOLO
from io import StringIO
from resultgenerator import generatelist, generateResults

model = YOLO("yolov8x.pt")

def run(file):
    if file == 0:
        source = 0 
    else:
        source = str(file)

    fileExt = source.split(".")[-1].lower()

    original_stdout = sys.stdout
    redirected_output = StringIO()
    sys.stdout = redirected_output

    cap = cv2.VideoCapture(source)
    frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    cap.release()

    model.predict(source=source, show=True, classes=0, conf= 0.1)

    rawText = redirected_output.getvalue()
    sys.stdout = original_stdout

    intlist = generatelist(rawText)
    num = generateResults(intlist,frameCount,fileExt)
    return num

if __name__ == '__main__':
    parameter = sys.argv[1]
    run(parameter)
