import sys
import random
def randomName(inPath, num):
    lines=[]
    try:
        fin= open(inPath, "r")
    except FileNotFoundError:
        print("FileNotFoundError: [Errno 2] No such file or directory: '{}'".format(inPath))
        return
    for name in fin.readlines():
        name.strip()
        lines.append(name)
    if num>len(lines):
        print("Sample size greater is than number of lines in the file: {} > {}".format(num,len(lines)))
        return
    for i in range(num):
        print(lines[random.randint(0, len(lines)-1)]+"\n")
inPath=sys.argv[1]
num=int(sys.argv[2])
randomName(inPath,num) 