import glob, os
from PIL import Image

# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
store_dir = current_dir + '/data_training'
image_dir = current_dir + '/Images'
label_dir = current_dir + '/Labels'
param_dir = store_dir + '/Params'
src_dir = store_dir + '/src'
print(current_dir)

# Directory where the data will reside, relative to 'darknet.exe'
#path_data = './Images/'

# Percentage of images to be used for the test set
percentage_test = 0.0001

# Create and/or truncate train.txt and test.txt
file_train = open('data_training/Params/train.txt', 'w')
file_test = open('data_training/Params/test.txt', 'w')
os.system('cp ' + current_dir + '/classes.txt ' + param_dir + '/classes.names')

#im = Image.open("image_path")
#im.convert('RGB').save("image_name.jpg","JPEG")

# Populate train.txt and test.txt
counter = 1
index_test = round(100 / percentage_test)
type_file = 'jpg'
for pathAndFilename in glob.iglob(os.path.join(image_dir, '*.' + type_file)):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))

    if counter == index_test:
        counter = 1
        im = Image.open(pathAndFilename)
        #im.convert('RGB').save(src_dir + '/' + title + '.jpg',"JPEG")
        os.system('cp ' + pathAndFilename + ' ' + src_dir + '/' + title + ext)
        os.system('cp ' + label_dir + '/' + title + '.txt ' + src_dir + '/' + title + '.txt')
        file_test.write( 'data_training/src/' + title + '.jpg' + "\n")
    else:
        im = Image.open(pathAndFilename)
        #im.convert('RGB').save(src_dir + '/' + title + '.jpg',"JPEG")
        os.system('cp ' + pathAndFilename + ' '  + src_dir + '/' + title + ext)
        os.system('cp ' + label_dir + '/' + title + '.txt ' + src_dir + '/' + title + '.txt')
        file_train.write('data_training/src/' + title + '.jpg' + "\n")
        counter = counter + 1
