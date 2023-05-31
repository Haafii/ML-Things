import sys
if (len(sys.argv) < 2):
    print("Enter a file name in the command line")
    sys.exit()
try:
    f = open(sys.argv[1], 'r')
    linesList = f.readlines()
    print("The following are the first 10 lines of the file: ")
    for textLine in (linesList[:10]):
        print(textLine, end='')
    print("The following are the last 10 lines of the file: ")
    for textLine in (linesList[-10:]):
        print(textLine, end='')
    f.close()
except FileNotFoundError:
  print("File not found")
