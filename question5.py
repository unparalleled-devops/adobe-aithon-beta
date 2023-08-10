import os
from predict import predict
import cv2

# QUICK PREFACE, TO RUN THIS PLEASE DELETE ALL SUBFOLDERS OF
# /images/solution_5_images


def get_entity(img, pos):
        x1 = pos[0]
        y1 = pos[1]
        x2 = pos[2]
        y2 = pos[3]

        new_img = img[y1:y2, x1:x2]
        return new_img

# pipeline for each image : 
# 1. we first find all entities in all images, crop them out save them
# 2. then we take entity no. 1 from image no. 1, then we loop through 
#    each entity in every image, and see if it is same
# 3. if it is, then we add to folder with img url name

images = os.listdir("images/question_5_images")
for url in images:
    img_url = f"images/solution_5_images/{url}"
    os.mkdir(img_url)
    img = cv2.imread(f"images/question_5_images/{url}")

    objects = predict(f"images/question_5_images/{url}")
    for obj in objects:
        name = obj["name"]
        pos = obj["box"]
        os.mkdir(f"images/solution_5_images/{url}/{name}_{pos}")
       

        # now crop entity from image, and save it in above directory
        new_img = get_entity(img, pos)

        cv2.imwrite(f"images/solution_5_images/{url}/{name}_{pos}/entity.png", new_img)
        


# now loop through all images
# find similar for each entity

imgs = os.listdir("images/solution_5_images")
for url in imgs:
    entities = os.listdir(f"images/solution_5_images/{url}")
    for entity in entities:
        name = entity.split('_')[0]
        n = 0

        # now first, entities in this image

        other_entities = os.listdir(f"images/solution_5_images/{url}")
        other_entities.remove(entity)
        flag_to_mkdir_ = 1
        for new_entity in other_entities:
            # these are all the entities in the image, not including 
            # the current one
            new_name = new_entity.split('_')[0]
            if name == new_name:
                # print(url, new_entity)
                if flag_to_mkdir_ == 1:
                    os.mkdir(f"images/solution_5_images/{url}/{entity}/from_{url}")
                    flag_to_mkdir_ = 0;

                c = cv2.imread(f"images/solution_5_images/{url}/{new_entity}/entity.png")
                cv2.imwrite(f"images/solution_5_images/{url}/{entity}/from_{url}/similar_{n}.png", c)
                n += 1

        # now, for each other image
        other_imgs = os.listdir("images/solution_5_images")
        other_imgs.remove(url)
        for other_url in other_imgs:
            other_entities_ = os.listdir(f"images/solution_5_images/{other_url}")
            
            flag_to_mkdir = 1
            for other_entity in other_entities_:
                other_name = other_entity.split('_')[0]
                if name == other_name:
                    if flag_to_mkdir == 1:
                        flag_to_mkdir = 0
                        os.mkdir(f"images/solution_5_images/{url}/{entity}/from_{other_url}")

                    d = cv2.imread(f"images/solution_5_images/{other_url}/{other_entity}/entity.png")
                    cv2.imwrite(f"images/solution_5_images/{url}/{entity}/from_{other_url}/similar_{n}.png", d)
                    n += 1