# import os
# def fil(pat):
#     for dirpath,dirnames,filenames in os.walk(pat):
#         for file in filenames:
#             print(file)
#         for dirname in dirnames:
#             fil(dirname)
#
# if __name__=='__main__':
#     pat=r'C:\Users\Administrator\Desktop\北京站\材料'
#     fil(pat)

# # 找出单个目录中的(最大)文件(大小)
# import os
# def getsize(path):
#     files = []
#     dirlist= os.listdir(path) #返回文件和文件夹的名字列表
#     for cont in dirlist:
#         dirname=os.path.join(path,cont) #拼接路径里的内容
#         if os.path.isfile(dirname):  #判断是否是文件
#             listsize=os.path.getsize(dirname) #是文件就获取大小
#             dic={'dirname':dirname,'listsize':listsize}
#             #files.append(dic['listsize'])
#
#     #print(files)
#         #return dirname,listsize
# if __name__ == '__main__':
#     pat=r'C:\Users\Administrator\Desktop\北京站\材料'
#     getsize(pat)
#     #最后加个排序取出最大值


#找出目录树中的(最大)文件(大小)：
# import os
# def get_Tree_max(path):
#     files = []
#     cont = os.listdir(path)  # 获取目录内容
#     for dirpath in cont:
#         dirname=os.path.join(path,dirpath) #拼接目录路径
#         if os.path.isfile(dirname): #判断是否为文件
#             #print(dirname)
#             # print(os.path.getsize(dirname))
#             size=os.path.getsize(dirname) #获取文件大小
#             alli={'dirname': dirname, 'size': size}
#             files.append(alli['size'])
#             #files.append(alli)
#         else:
#             p=os.path.join(path,dirpath)
#             get_Tree_max(p)
#     print(files)
# if __name__ == '__main__':
#     pat=r'C:\Users\Administrator\Desktop\北京站\材料'
#     get_Tree_max(pat)

import os
path=r'C:\Users\Administrator\Desktop\北京站\材料'
#

#os.path.abspath() 将相对路径转化为绝对路径(前面加当前路径，当前路径为：E:/git-test/)
#path=r'Desktop\北京站\材料'
#print(os.path.abspath(r'Desktop\北京站\材料'))
#结果：E:\git-test\Desktop\北京站\材料
#
#os.path.dirname() 获取完整路径当中的目录部分(不包括当前（最后一个）目录）
#print(os.path.dirname(r'C:\Users\Administrator\Desktop\北京站\材料'))
#结果：C:\Users\Administrator\Desktop\北京站
#
#os.path.basename()获取完整路径当中的主体部分
#print(os.path.basename(r'C:\Users\Administrator\Desktop\北京站\材料'))
#结果：材料

#os.path.split() 将一个完整的路径切割成目录部分和主体部分，返回元组
#print(os.path.split(r'C:\Users\Administrator\Desktop\北京站\材料'))
#结果：('C:\\Users\\Administrator\\Desktop\\北京站', '材料')

#os.path.join() 将2个路径合并成一个
#print(os.path.join(r'C:\Users\Administrator\Desktop\北京站\材料', "test"))
#结果：C:\Users\Administrator\Desktop\北京站\材料\test

# getsize() 获取文件的大小 os.path.getsize(path)
# isfile() 检测是否是文件 os.path.isfile(path)
# isdir() 检测是否是文件夹 os.path.isdir(path)
