from PIL import Image
import os
import time
import random

path = input("Enter The Path OF Folder\n")
# path = r"D:\TestPDF"
ListDir = os.listdir(path)

ImageDirList = []
ImageVarList = []
ImageConvertList = []
ImageList = []

for i in range(len(ListDir)):
    try:
        if "pdf" in ListDir[i]:
            ListDir.pop(i)
    except:
        print("There Exist a PDF")

for i in range(len(ListDir)):
    ImageDirList.append(f"{path}\{ListDir[i]}")

for i in range(len(ListDir)):
    ImageVarList.append(Image.open(ImageDirList[i]))
    ImageConvertList.append(ImageVarList[i].convert('RGB'))

for i in range(len(ListDir)-1):
    ImageList.append(ImageConvertList[i+1])

print(ListDir)
print("Getting Files.......\n")
time.sleep(0.2)
print("Scanning File......\n")
time.sleep(0.2)
print("Converting......\n")
time.sleep(0.2)

ran = random.randint(1,1000000)
ImageConvertList[0].save(path+"\\alpha"+str(ran)+".pdf",save_all=True, append_images=ImageList)
print(f"PDF is Saved As Alpha{ran}.pdf\n")
time.sleep(1)

# image1 = Image.open(r'F:\Subhash Dorlikarji\Rasitol Invoices\1.jpeg')
# image2 = Image.open(r'F:\Subhash Dorlikarji\Rasitol Invoices\2.jpeg')
# image3 = Image.open(r'F:\Subhash Dorlikarji\Rasitol Invoices\3.jpeg')
# image4 = Image.open(r'F:\Subhash Dorlikarji\Rasitol Invoices\4.jpeg')
#
# im1 = image1.convert('RGB')
# im2 = image2.convert('RGB')
# im3 = image3.convert('RGB')
# im4 = image4.convert('RGB')
#
# imagelist = [im2,im3,im4]
#
# im1.save(r'D:\TestPDF\1.pdf',save_all=True, append_images=imagelist)
