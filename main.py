def decsize(imagetocompress,resize="no"):
    from PIL import Image
    import math
    image = Image.open("orginals/"+imagetocompress)
    dim = image.size
    width,height=image.size

    #print(f"file size: {dim}")
    image.save("processed/" + imagetocompress, optimize=True, quality=2)


    if resize =="yes":
     foo = Image.open("processed/"+imagetocompress)
     x, y = foo.size
     x2, y2 = math.floor(x - width/2), math.floor(y - height/2)
     foo = foo.resize((x2, y2), Image.ANTIALIAS)
     foo.save("processed/"+ imagetocompress)
    else:
        pass

if __name__ == '__main__':
    import os
    print(os.listdir('orginals'))
    directory = os.listdir('orginals')
    jsonfile=open('datas/data.json')
    data = json.load(jsonfile)

    for x in directory:
        y=data[x]
        print("compressing : "+x)
        if y =="no":
            print("resize : no")
        else:
            print("resize : yes")
        decsize(x,"yes")
