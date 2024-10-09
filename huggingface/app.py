import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

import gradio as gr
import torch
from ultralytics import YOLO
from PIL import Image, ImageDraw, ImageFont

# Define the class names and bounding box colors
class_names = ['black_scurf', 'blackleg', 'healthy', 'pink_rot']
class_colors = {
    0: "red",       # black_scurf
    1: "blue",      # blackleg
    2: "green",     # healthy
    3: "orange"     # pink_rot
}

def yoloV8_func(image_path, image_size, conf_threshold, iou_threshold):
    """This function performs YOLOv8 object detection on the given image.

    Args:
        image_path (str): Input image filepath to detect objects on.
        image_size (int): Desired image size for the model.
        conf_threshold (float): Confidence threshold for object detection.
        iou_threshold (float): Intersection over Union threshold for object detection.
    """
    # Load the YOLOv8 model from the 'best.pt' checkpoint
    model_path = "best.pt"
    model = YOLO(model_path)

    # Open the image from the filepath
    image = Image.open(image_path)

    # Perform object detection on the input image using the YOLOv8 model
    results = model.predict(image,
                            conf=conf_threshold,
                            iou=iou_threshold,
                            imgsz=image_size)

    # Get bounding boxes and class names for detected objects
    draw = ImageDraw.Draw(image)
    
    # Optional: Define a font for the class name (PIL can load custom fonts if available)
    try:
        font = ImageFont.truetype("arial.ttf", 15)
    except IOError:
        font = ImageFont.load_default()

    for result in results[0].boxes:
        box = result.xyxy[0]  # Get the bounding box
        cls = int(result.cls[0].item())  # Get the class index
        conf = result.conf[0].item()  # Get the confidence score

        # Get color for the class
        color = class_colors.get(cls, "white")  # Default to white if class not found

        # Draw the bounding box
        draw.rectangle([box[0], box[1], box[2], box[3]], outline=color, width=3)

        # Draw the class label and confidence score
        label = f"{class_names[cls]}: {conf:.2f}"
        # Use textbbox to calculate text dimensions
        text_bbox = draw.textbbox((0, 0), label, font=font)
        text_location = (box[0], box[1] - (text_bbox[3] - text_bbox[1]))
        
        # Draw the background rectangle for the label
        draw.rectangle([text_location, (box[0] + (text_bbox[2] - text_bbox[0]), box[1])], fill="black")
        draw.text(text_location, label, fill="white", font=font)

    # Return the modified image with bounding boxes
    return image

# Define inputs and outputs for the Gradio app
inputs = [
    gr.Image(type="filepath", label="Input Image"),  # Image upload input
    gr.Slider(minimum=320, maximum=1280, value=640, step=32, label="Image Size"),
    gr.Slider(minimum=0.0, maximum=1.0, value=0.25, step=0.05, label="Confidence Threshold"),
    gr.Slider(minimum=0.0, maximum=1.0, value=0.45, step=0.05, label="IOU Threshold"),
]

outputs = gr.Image(type="pil", label="Output Image")  # Output as PIL image

# Set up the Gradio interface
title = "Deteksi Penyakit Kentang dengan YOLOv8"

yolo_app = gr.Interface(
    fn=yoloV8_func,
    inputs=inputs,
    outputs=outputs,
    title=title,
    cache_examples=True,
)

# Enable the queuing system if needed
yolo_app.queue()

# Launch the Gradio app
yolo_app.launch(debug=True)
