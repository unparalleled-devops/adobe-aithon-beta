from predict import predict


objects = predict("images/img2.png", show=True)
for obj in objects:
    name = obj["name"]
    box = obj["box"]
    print(f"entity : location --> {name} : {box}")

