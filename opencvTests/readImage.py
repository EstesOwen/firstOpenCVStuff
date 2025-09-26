import cv2

# read in the image
img = cv2.imread('puppies.jpg')

# get the size of the image(this gives us an array whose components are[width,height,rgb channels])
size = img.shape
print(size)

# resize it to 640x480
resized = cv2.resize(img,(640,480))

# crop the image
# here, we're trimming the sides of the image by saving only from 1/4 the width and height to 3/4 of the dimensions,
cropped = img[int(size[0]/4):int(3*size[0]/4), int(size[1]/4):int(3*size[1]/4)]
#            [start width   :  end width     , start height  :  end height    ]

#cv2.imshow('puppies',img)
#cv2.imshow('puppies',resized)
cv2.imshow('puppies',cropped)
cv2.waitKey(0)
