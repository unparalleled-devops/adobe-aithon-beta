from predict import predict


objects = predict("images/img2.png")
# question 2: count entities, group like entities and give counts for each
entities_by_name = []
for obj in objects:
    name = obj["name"]
    flag = 0
    for t in entities_by_name:
        if name in t:
            t.append(name)
            flag = 1

    if flag == 0:
        entities_by_name.append([name])

print(entities_by_name)
for e in entities_by_name:
    c = len(e)
    if c > 1:
        print(f"there are {c} {e[0]}s in the image")
    else: 
        print(f"there is 1 {e[0]} in the image")


