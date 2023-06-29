"""
@author:Tommy
"""
import os
import pandas as pd
import zipfile

def getFilesName(path):
    s = []
    if not os.path.exists(path):
        print("该路径不存在，找不到该文件")
        return
    if os.path.isdir(path):
        files = os.listdir(path)
        files.sort()
        for file in files:  # 遍历文件夹
            s.append(file)
    elif os.path.isfile(path):
        print('该路径是一个文件，不是一个文件夹，请重新输入')
        return

    fileNames = {'fileName': s,'filePath':[str(path)+"/"+str(i) for i in s]}
    exportFile = pd.DataFrame(fileNames)
    # exportFile.to_csv("lala.csv",index=False)
    # print("lalal")
    return exportFile

def unZipFiles(fileName,startPath,endPath):
    fileName=fileName.replace(".zip","").replace(".tar","")
    f = zipfile.ZipFile(startPath, 'r')  # 压缩文件位置

    if len(f.namelist()) ==1: #替换名字
        finalPathName=f.extract(f.namelist()[0], endPath)
        portion = os.path.splitext(finalPathName)
        print(portion)
        os.rename(finalPathName, str(endPath)+"/"+fileName+portion[1])

    elif len(f.namelist())==0:
        print("{} 该压缩包无文件，已跳过解压".format(fileName))

    else:
        for file in f.namelist():
            theName=f.extract(file, endPath)  # 解压位置
            portion = os.path.splitext(theName)
            os.rename(theName, str(endPath) + "/" + fileName+"_"+str(portion[0]).split("/")[-1]+ portion[1])

    f.close()


def unZipAll(dir,desPath):
    for index,item in dir.iterrows():
       if (".zip" or ".tar") in item['fileName']:
            unZipFiles(item['fileName'],item['filePath'],desPath)

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    zipFiles="zipFiles" # 这个路径是压缩包的文件路径
    unZipFilesDir="unZipFiles"# 这个是指定的解压路径

    if not os.path.exists(unZipFilesDir):
        os.makedirs(unZipFilesDir)

    filesName=getFilesName(zipFiles)
    unZipAll(filesName,unZipFilesDir)

