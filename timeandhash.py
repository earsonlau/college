# import os
#
# filePath = '.'
# filenames = os.listdir(filePath)
# timestamp = []
# for name in filenames:
#     if name[1] == 'json'
#         timestamp.append(name[0])
# print(filenames)
# # if os.path.splitext(file_path)[1] == '.json':
import os
import hashlib
#h=hashlib.md5(open(filename,'rb').read()).hexdigest()
def getFileName(path):
    ''' 获取指定目录下的所有指定后缀的文件名 '''
    timestamp=[]
    filepaths=[]
    f_list = os.listdir(path)
    print(f_list)
    for i in f_list:
        # os.path.splitext():分离文件名与扩展名
        if os.path.splitext(i)[1] == '.jpeg':
            print(i)
            timestamp.append(os.path.splitext(i)[0])
            # filepaths.append(os.path.splitext(i))
    #把list以txt格式输出到指定路径
    fileObject = open('TimeStamp+Address.txt', 'w')
    for time in timestamp:
        fileObject.write(time)
        fileObject.write('\n')
    fileObject.write('----------')
    fileObject.write('\n')
    for filenames in f_list:
         # fileObject.write(path)
         truepath = path+filenames
         print(truepath)
         md5=hashlib.md5(open(truepath, 'rb').read()).hexdigest()
         fileObject.write(md5)
         fileObject.write('\n')
    fileObject.close()

if __name__ == '__main__':

    #path = '/home/liurishen/JsonAndPhotos/few/1/'
    try:
        dirpath = sys.argv[1]
    except IndexError as e:
        sys.exit('need one dirctory')
    if os.path.isfile(dirpath):
        sys.exit('Please input a directory')

    getFileName(path)
