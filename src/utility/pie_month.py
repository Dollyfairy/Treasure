
import os
import time


import pandas as pd
import matplotlib.pyplot as plt

# import字型管理套件

from matplotlib.font_manager import FontProperties

# 指定使用字型和大小

myFont = FontProperties(fname='C:/Users/Dolly/AppData/Roaming/Python/Python38/site-packages/matplotlib/mpl-data/fonts/ttf/TaipeiSansTCBeta-Regular.ttf', size=14)


# 設定顏色

color = ['#EDBBBC', '#F8BA91', '#FDDB7E', '#B3D89B', '#A8C3D9', '#808ef9']


quantity = [['玻璃', 3],['塑膠', 3],['紙容器', 2],['鐵鋁', 1],['電池', 1]]


# 設定圓餅圖大小


fig =plt.figure(figsize=(5,5))

# 依據類別數量，分別設定要突出的距離

# separeted = (0, 0, 0, 0, 0, 0)      

df = pd.DataFrame(quantity,
    columns=['country', 'pop'])

# 設定圓餅圖屬性

a,category_text,percent_text = plt.pie(

        df['pop'],
        

        # labels=df['country'],                       # 數值

        colors = color,                   # 指定圓餅圖的顏色
        autopct = "%0.0f%%",              # 四捨五入至小數點後面位數

        # explode = separeted,              # 設定分隔的區塊位置

        pctdistance = 0.65,               # 數值與圓餅圖的圓心距離

        radius = 1.5,                     # 圓餅圖的半徑，預設是1
        
        # center = (-10,0),                 # 圓餅圖的圓心座標
        
        shadow=False)                     # 是否使用陰影



# 把每個分類設成中文字型

for t in category_text:
    t.set_fontproperties(myFont)
    t.set_size(20)

# 把每個數值設成中文字型

for t in percent_text:
    t.set_fontproperties(myFont)
    t.set_size(16)

   

# # 設定legnd的位置

# plt.legend(loc = "center right", prop=myFont)

# 設定圖片標題，以及指定字型設定，x代表與圖案最左側的距離，y代表與圖片的距離

# plt.title("Python 畫圓餅圖(Pie chart)範例", fontproperties=myFont, x=0.5, y=1.03)

# 畫出圓餅圖
plt.savefig("src/static/pie/p1.jpg")
plt.show()


fileTest = ("src/static/pie/p1.jpg")
time.sleep(5)
os.remove(fileTest)