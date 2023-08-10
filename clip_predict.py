import torch
import clip
from PIL import Image

model, preprocess = clip.load("ViT-B/32", device="cpu")

image = preprocess(Image.open("images/img2.png")).unsqueeze(0)
text = clip.tokenize(["a ball", "a person", "a game"])
with torch.no_grad():
    image_features = model.encode_image(image)
    text_features = model.encode_text(text)
    
    logits_per_image, logits_per_text = model(image, text)
    probs = logits_per_image.softmax(dim=-1).numpy()


print("Label probs:", probs)  # prints: [[0.9927937  0.00421068 0.00299572]]