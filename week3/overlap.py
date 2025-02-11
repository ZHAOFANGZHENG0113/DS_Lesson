import sys

def overlap(inPath, inPath2):
    with open(inPath, "r") as fin, open(inPath2, "r") as fin2:
        lines = fin.readlines()
        lines = [line.strip() for line in lines]  
        lines2 = fin2.readlines()
        lines2 = [line.strip() for line in lines2]  
    setline = set(lines)
    setline2 = set(lines2)

    print(setline.intersection(setline2))

inPath = sys.argv[1]
inPath2 = sys.argv[2]
overlap(inPath, inPath2)
