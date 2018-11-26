import os
def fil(pat):
    for dirpath,dirnames,filenames in os.walk(pat):
        for file in filenames:
            print(file)
        for dirname in dirnames:
            fil(dirname)


if __name__=='__main__':
    pat=r'C:\Users\Administrator\Desktop\北京站\材料'
    fil(pat)

