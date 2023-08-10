import os
from predict import predict
import copy

# first get entities from ideal images
ideal_entities = []
urls = os.listdir("images/question_4_images/ideal")
for url in urls:
    url_ = f"images/question_4_images/ideal/{url}"
    objects = predict(url_)
    for obj in objects:
        name = obj["name"]
        if name not in ideal_entities:
            ideal_entities.append(name)

# then for each other image, find extra or missing ones

# first, get each entity in new image, by name
urls = os.listdir("images/question_4_images/test")
for url in urls:
    given_entities = []
    url_ = f"images/question_4_images/test/{url}"
    objects = predict(url_)
    for obj in objects:
        name = obj["name"]
        if name not in given_entities:
            given_entities.append(name)
    
    
    missing = copy.deepcopy(ideal_entities)
    extra = []
    for name in given_entities:
        if name in missing:
            missing.remove(name)
        else:
            extra.append(name)
    print(f"missing: {missing}")
    print(f"extra: {extra}")