#import needed packages/functions
from os import listdir
from random import randint
import matplotlib.pyplot as plt
import matplotlib.image as img

#directories to data
#test_dir = "[directory to data]\\test"
train_0_dir = "[directory to data]\\train\\0"
train_1_dir = "[directory to data]\\train\\1"

#get file names in directories
#test_file_list = listdir(test_dir) #unused
train_0_file_list = listdir(train_0_dir)
train_1_file_list = listdir(train_1_dir)

#show 2 random images from the training data 0
print("train 0",end="")    
for i in range(2):
    file = img.imread(train_0_dir+"\\"+train_0_file_list[randint(0,len(train_0_file_list)-1)])
    plt.imshow(file)
    plt.show()

#show 2 random images from the training data 1
print("\ntrain 1",end="")
for i in range(2):
    file = img.imread(train_1_dir+"\\"+train_1_file_list[randint(0,len(train_1_file_list)-1)])
    plt.imshow(file)
    plt.show()
