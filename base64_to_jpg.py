import base64
def turn(txt,name):
    txt = txt.split(',')[-1]
    imgdata = base64.b64decode(txt)
    file = open(name, 'wb')
    file.write(imgdata)
    file.close()

if __name__ == '__main__':
    with open("1.txt", "r") as f:
        txt=f.read()

    turn(txt)