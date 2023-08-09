from predict import predict
import os
import warnings
warnings.filterwarnings("ignore")


entities = []
img_urls = os.listdir("images/question_3_images")
for img_url in img_urls:
    print(img_url)
    objects = predict(f"images/question_3_images/{img_url}")
    for obj in objects:
        name = obj["name"]
        obj["url"] = img_url
        flag = 0
        for entity_list in entities:
            entity = entity_list[0]
            if name == entity:
                flag = 1
                entity_list.append(obj)
        if flag == 0:
            entities.append([name, obj])

# print(entities, len(entities), len(entities[0]))
# entities is a list containing an invidual list for each entity
# and each list having ["name of entity", entity_object, entity_object]    

# now we can easily sort the urls
url_dict = {}
for entity in entities:
    urls = []
    for obj in entity[1:]:
        urls.append(obj["url"])
    url_dict[entity[0]] = urls

print(url_dict)     