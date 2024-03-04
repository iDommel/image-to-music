from PIL import Image
import numpy as np
from sklearn.cluster import KMeans

image = Image.open("Flag_of_Sudan.png")
x, y = image.size

if image.mode != 'RGB':
    image = image.convert('RGB')

pixels = list(image.getdata())
pixels_list = [pixels[i * x:(i + 1) * x] for i in range(y)]
image_array = np.array(image)
pixels = image_array.reshape(-1, 3)
nombre_clusters = 3

kmeans = KMeans(n_clusters=nombre_clusters)
kmeans.fit(pixels)
labels = kmeans.labels_

for i in range(y):
    for j in range(x):
        pixel_index = i * x + j
        pixels_list[i][j] = labels[pixel_index]

for ligne in pixels_list:
    print(ligne)

primary_color = kmeans.cluster_centers_.astype(int)

print("colors principales en format hexadécimal:")
for color in primary_color:
    print('#{:02x}{:02x}{:02x}'.format(*color))