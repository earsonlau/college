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
import sys
import json
#h=hashlib.md5(open(filename,'rb').read()).hexdigest()
def getFileName(path):
    ''' 获取指定目录下的所有指定后缀的文件名 '''
    timestamps=[]
    filepaths=[]
    jpegpaths=[]
    # md5s=[]
    f_list = os.listdir(path)
    print(f_list)
    #获取所有图片的名字和路径
    for i in f_list:
        # os.path.splitext():分离文件名与扩展名
        if os.path.splitext(i)[1] == '.json':
            # print(i)
            timestamps.append(os.path.splitext(i)[0])
            truejpegpath=path+i
            jpegpaths.append(truejpegpath)
    #把list以txt格式输出到指定路径
    txtname='TimeStamp+Hash.txt'
    fileObject = open(txtname, 'w')
    #把图片名称也就是时间戳写进txt
    for time in timestamps:
        fileObject.write(time)
        fileObject.write('\n')
    fileObject.write('----------')
    fileObject.write('\n')


    #获取所有文件的路径并作MD5编码
    # for filenames in f_list:
    #      # fileObject.write(path)
    #      truepath = path+filenames
    #      filepaths.append(truepath)
    #      # print(truepath)
    #      md5=hashlib.md5(open(truepath, 'rb').read()).hexdigest()
    #      md5s.append(md5)
    #
    #
    #      fileObject.write(md5)
    #      fileObject.write('\n')
    # fileObject.close()
    #
    #

    ##接下来写几个字典
    # 1 key为时间戳 value为路径
    if(len(timestamps) == len(jpegpaths)):
        time_path_dict  = dict(zip(timestamps,jpegpaths))
    # 2 key为md5 value为路径
    if(len(md5s) == len(filepaths)):
        md5_path_dict = dict(zip(md5s,filepaths))
    print(len(md5s))
    print(len(filepaths))
    #
    # jsObj = json.dumps(time_path_dict)
    # fileObject = open('time_path_dict.json', 'w')
    # fileObject.write(jsObj)
    # fileObject.close()
    #
    # jsObj = json.dumps(md5_path_dict)
    # fileObject = open('md5_path_dict.json', 'w')
    # fileObject.write(jsObj)
    # fileObject.close()






if __name__ == '__main__':

    #path = '/home/liurishen/JsonAndPhotos/few/1/'
    try:
        dirpath = sys.argv[1]
    except IndexError as e:
        sys.exit('need one dirctory')
    if os.path.isfile(dirpath):
        sys.exit('Please input a directory')

    getFileName(dirpath)
