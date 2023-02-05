import cv2
import os


# Get the dimensions of the image
#height, width = image.shape[:2]

# Set the desired dimensions
new_height = 720
new_width = 1280

folderPath='slides'
myList=os.listdir(folderPath)

# Resize the image

for img in myList:
    image = cv2.imread(f'{folderPath}/{img}')
    resized_image = cv2.resize(image, (new_width, new_height))
    #resized_image=cv2.flip(resized_image,1)
    cv2.imwrite(f'{img}', resized_image)
