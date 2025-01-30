import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from PIL import Image

images = []
label = []

images_adress = "images"

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



model = RandomForestClassifier()

model.fit(X_train, y_train)

prediction = model.predict(X_test)

accuracy = accuracy_score(y_test, prediction)

print(accuracy)
