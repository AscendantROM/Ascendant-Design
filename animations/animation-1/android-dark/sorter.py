import os, sys

files = os.listdir(sys.argv[1])


for i in range(len(files)):
    if len(str(len(files))) == 2:
        filename = "000" + "0" * (len(str(len(files))) - len(str(i))) + str(i)
    else:
        filename = "00" + "0" * (len(str(len(files))) - len(str(i))) + str(i)

    os.rename(f"{sys.argv[1]}/{files[i]}", f"{sys.argv[1]}/{filename}.png")