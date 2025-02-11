import sys
def readname(inPath,index):
    try:
        fin=open(inPath,"r")
    except FileNotFoundError:
        print("Unable to read from file: [Errno 2] No such file or directory:{}".format(inPath))
        return
    lines=fin.readlines();
    lines=[line.strip() for line in lines]
    for i in index:
        print(lines[i])
    fin.close()
inPath=sys.argv[1]
try:
    index=[int(i) for i in sys.argv[2:]]
    readname(inPath,index)
except ValueError:
    print("Invalid line number specified: invalid literal for int() with base 10: 'a'")