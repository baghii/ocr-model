import easyocr
import cv2

import gradio as gr

def ocr_function(img):
    reader = easyocr.Reader(['en'], gpu=False)
    result = reader.readtext(img)
    for detection in result:
        new_left = tuple([int(val) for val in detection[0][0]])
        new_right = tuple([int(val) for val in detection[0][2]])
        text = detection[1]
        font = cv2.FONT_HERSHEY_SIMPLEX
        img = cv2.rectangle(img, new_left, new_right, (0,250,0), 5)
    return img

imagein = gr.inputs.Image()
imageout = gr.outputs.Image()
descriptin = "OCR"

def main():
    gr.Interface(ocr_function, imagein, imageout, description=descriptin).launch()

if __name__ == "__main__":
    main()