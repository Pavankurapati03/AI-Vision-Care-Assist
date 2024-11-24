import torch
from torchvision import transforms
from torchvision.models.detection import fasterrcnn_resnet50_fpn
import google.generativeai as genai
from PIL import ImageDraw
from io import BytesIO

# Initialize the generative AI model
def configure_generative_ai(api_key):
    genai.configure(api_key=api_key)

# Load object detection model
def load_object_detection_model():
    model = fasterrcnn_resnet50_fpn(pretrained=True)
    model.eval()
    return model

# COCO class labels (object categories for detection)
COCO_CLASSES = [
    "_background_", "person", "bicycle", "car", "motorcycle", "airplane", "bus", "train", "truck", "boat",
    "traffic light", "fire hydrant", "N/A", "stop sign", "parking meter", "bench", "bird", "cat", "dog",
    "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "N/A", "backpack", "umbrella", "N/A",
    "N/A", "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
    "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "N/A", "wine glass", "cup", "fork",
    "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza",
    "donut", "cake", "chair", "couch", "potted plant", "bed", "N/A", "dining table", "N/A", "N/A", "toilet",
    "N/A", "tv", "laptop", "mouse", "remote", "keyboard", "cell phone", "microwave", "oven", "toaster", "sink",
    "refrigerator", "N/A", "book", "clock", "vase", "scissors", "teddy bear", "hair drier", "toothbrush"
]

# Detect objects in the image
def detect_objects(image, object_detection_model, threshold=0.5):
    transform = transforms.Compose([transforms.ToTensor()])
    img_tensor = transform(image)
    predictions = object_detection_model([img_tensor])[0]

    filtered_boxes = [
        (box, label, score)
        for box, label, score in zip(predictions['boxes'], predictions['labels'], predictions['scores'])
        if score > threshold
    ]
    return filtered_boxes

# Draw bounding boxes on the image
def draw_boxes(image, predictions):
    draw = ImageDraw.Draw(image)
    for box, label, score in predictions:
        x1, y1, x2, y2 = box.tolist()
        class_name = COCO_CLASSES[label.item()]
        draw.rectangle([x1, y1, x2, y2], outline="yellow", width=3)
        draw.text((x1, y1), f"{class_name} ({score:.2f})", fill="black")
    return image

# Generate scene description using Generative AI
def generate_scene_description(input_prompt, image_data):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content([input_prompt, image_data[0]])
        return response.text
    except Exception as e:
        return f"⚠ Error generating scene description: {str(e)}"
    

# In models.py
import google.generativeai as genai

def generate_task_assistance(input_prompt, image_data):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content([input_prompt, image_data[0]])
        return response.text
    except Exception as e:
        return f"⚠ Error generating task assistance: {str(e)}"

