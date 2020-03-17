from PIL import Image

img = Image.open("sp.png")
img=img.convert("RGBA")
datas=img.getdata()

newData = []
cutOff = 50

for item in datas :
    if item[0] >= cutOff and item[1] >= cutOff and item[2] >= cutOff :
        newData.append((255,255,255,0))
        # RGB의 각 요소가 모두 cutOff 이상이면 transparent하게 바꿈
    else :
        newData.append(item)
        # 나머지 요소는 변경하지 않음

img.putdata(newData)
img.save("sp_t.png", "PNG")