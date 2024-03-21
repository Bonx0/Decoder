
from PIL import Image



txt = open("result.txt", mode="r", encoding = "UTF-8")

line1 = txt.readline().strip().split(" ")

img = Image.new(mode="RGB", size=(int(line1[0]), int(line1[1])), color="white")
pixels = img.load()

y=0
counter = 0
temp = ""
c=0
fresult = ""
fresultlist = []
for line in txt:
    x=0
    for letter in line.strip():
        if counter < 5:
            counter += 1
            temp += letter
        else:
            temp += letter
            for l in temp:
                c += 1
                fresult += l
                if c >= 2:
                    fresultlist.append(int(fresult, 16))           
                    c = 0
                    fresult = ""
            
            tupresult = tuple(fresultlist)
            pixels[x,y] = tupresult
            fresultlist = []
            temp = ''
            x+=1
            counter = 0
        
    
    y +=1    
    
img.show()

txt.close()