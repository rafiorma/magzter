import requests
import time
import img2pdf
import glob
import re
import os

numbers = re.compile(r'(\d+)')


def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts


def images(link):
    url = link
    for x in range(1, 40):
        url_working = url + str(x) + ".jpg"
        #    print url_working
        #    urllib.request.urlretrieve(url_working)
        requests.codes(url_working)
        r = requests.get(url_working, stream=True)
        if(r.status_code==200):
            with open(str(x) + '.jpg', 'wb') as fd:
                for chunk in r.iter_content(chunk_size=512):
                    fd.write(chunk)
        else:
            break


# 'https://maghtml.magzter.com/data/7965/1519128696/267039eX3RCxVy/jpg/.jpg'(Sample link)
def imgtopdf(output):
    my_list=[]
    for infile in sorted(glob.glob('G:\magazins\onandamela\*jpg'), key=numericalSort):
        my_list.append(infile)
    with open(output, "wb") as f:
        print(my_list)
        f.write(img2pdf.convert(my_list))

def delete():
    for infile in sorted(glob.glob('G:\magazins\onandamela\*jpg'), key=numericalSort):
        os.remove(infile)


images('https://maghtml.magzter.com/data/7965/1519128696/267039eX3RCxVy/jpg/')
time.sleep(2)
print("waiting")
imgtopdf('G:\magazins\Anandamela.pdf')
delete()
