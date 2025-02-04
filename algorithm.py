import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from PIL import Image



images_adress = "images"
model = RandomForestClassifier()


def model_training(model):
    images = []
    label = []
    for name in os.listdir(images_adress):
        image = Image.open(os.path.join(images_adress, name)).resize((200,200), Image.Resampling.NEAREST)
        images.append(np.array(image))
        if "house" in name:
            label.append(1)
        else:
            label.append(0)


    #Jāpārtaisa par python skaitļu sarakstiem.
    images = np.array(images)
    label = np.array(label)

    images = images/255.0 #
    images = images.reshape(images.shape[0], -1)



    X_train, X_test, y_train, y_test = train_test_split(images, label, test_size=0.2)

    model.fit(X_train, y_train)

    prediction = model.predict(X_test)

    accuracy = accuracy_score(y_test, prediction)

    print(accuracy)
    return model

def house_detector(image, model):
    image = [Image.open(image).resize((200, 200), Image.Resampling.NEAREST)]
    image = np.array(image)
    image = image/255.0
    image = image.reshape(image.shape[0], -1)
    result = model.predict(image)
    if result[0] == 1:
        print(f"Šajā bildē ir māja")
    else:
        print(f"Šajā bildē nav māja")
    return result


model = model_training(model)

house_detector("test2.jpg", model)
