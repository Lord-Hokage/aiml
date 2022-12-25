import sys
with open ("files/"+sys.argv[1]+".txt") as fil:
    for line in fil.readlines():
        print(line)