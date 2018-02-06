# -*- coding: utf-8 -*-
from multiprocessing import Pool
from multiprocessing import Manager
import os
import shutil
def copyFile(filename, oldFolder, newFolder, helpQueue):
    if os.path.exists(oldFolder) and os.path.exists(newFolder):
        pass

def main():
    oldFolderName = input("请输入您要复制的的文件夹位置:")
    newFolderName = oldFolderName + "-复件"
    if os.path.exists(oldFolderName):
        fileNames = os.listdir(oldFolderName)
    else:
        print("您输入的想要复制的文件位置不对，请重新输入:")
        return
    pool = Pool(5)

    helpQueue = Manager().Queue()
    for filename in fileNames:
        pool.apply_async(copyFile, (filename, oldFolderName, newFolderName, helpQueue))

    Alllen = len(fileNames)
    num = 0
    while True:
        helpQueue.get()
        num = num + 1
        copyRate = num / Alllen
        print("copy的进度是:%.2f"%(copyRate,),end="")
if __name__ == '__main__':
    main()
