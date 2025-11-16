import torch
from PIL import Image
from transformers import CLIPModel, AutoProcessor

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = AutoProcessor.from_pretrained("openai/clip-vit-base-patch32")

def normalize(v):
    return (v / v.norm(dim=-1, keepdim=True)).squeeze().tolist()

def get_text_embedding(text: str):
    inputs = processor(text=[text], return_tensors="pt")
    with torch.no_grad():
        emb = model.get_text_features(**inputs)
    return normalize(emb)

def get_image_embedding(file):
    image = Image.open(file).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")
    with torch.no_grad():
        emb = model.get_image_features(**inputs)
    return normalize(emb)
