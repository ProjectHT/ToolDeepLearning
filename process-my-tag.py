import glob, os
from PIL import Image

current_dir = os.path.dirname(os.path.abspath(__file__))
#current_dir = '/Volumes/MyData'
store_dir =  '/Users/thongpham/Desktop/KQ/Data'
#store_dir = 'my_data_out'
output_dir = '/Users/thongpham/Desktop/KQ/my_data_training_tag'
param_dir = output_dir + '/Params'
src_dir = output_dir + '/src'

file_train = open('/Users/thongpham/Desktop/KQ/my_data_training_tag/Params/train.list', 'w')
file_class = open('/Users/thongpham/Desktop/KQ/my_data_training_tag/Params/classes.names', 'w')
count = 1
for pathAndFolder in glob.iglob(os.path.join(store_dir, '*')):
    folder, ext = os.path.splitext(os.path.basename(pathAndFolder))
    file_class.write(folder + '\n')
    for pathAndFilename in glob.iglob(os.path.join(pathAndFolder, '*.*')):
        print(pathAndFilename)
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        if(ext == '.png') or (ext == '.PNG') :
                im = Image.open(pathAndFilename)
                rgb_im = im.convert('RGB')
                width = 32
                height = 32
                im_out = rgb_im.resize((width, height), Image.BICUBIC)  
                temp_file = str(count) + '_' + folder + '.png'
                file_train.write('my_data_training_tag/src/' + temp_file + '\n')
                temp_file = src_dir + '/' + temp_file
                im_out.save(temp_file)
        elif (ext == '.jpg') or (ext == '.JPG') :
                im = Image.open(pathAndFilename)
                rgb_im = im.convert('RGB')
                width = 32
                height = 32
                im_out = rgb_im.resize((width, height), Image.BICUBIC)  
                temp_file = str(count) + '_' + folder + '.png'
                file_train.write('my_data_training_tag/src/' + temp_file + '\n')
                temp_file = src_dir + '/' + temp_file
                im_out.save(temp_file)
        else:
                print("Error : %s",pathAndFilename)
        count = count + 1     
print("Finish!!!")
