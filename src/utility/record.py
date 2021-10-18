from linebot.models import *
from utility import DB
from datetime import datetime
import json
import pandas as pd
import matplotlib.pyplot as plt

# import字型管理套件

from matplotlib.font_manager import FontProperties


# 執行 MySQL 查詢指令


def record_todayr(line_id):
    print('12434343434')
    today_record = DB.run(("select a.Record_Recycling_time,c.Location_Name,d.Type_Name,b.Sub_Get_points,b.Sub_Picture from treasure_recycling_record as a join treasure_sub_record as b on a.Record_Recycling_number=b.Sub_Recycling_number join treasure_type as d on b.Sub_Type_number = d.Type_Number join treasure_erection_location as c on a.Record_Location_number=c.Location_Number where a.Record_LINEid='%s' and date(a.Record_Recycling_time)=curdate()" % (line_id)), '1')
    # sum_point = DB.run(("select a.Record_LINEid,sum(b.Sub_Get_points) from treasure_recycling_record as a join treasure_sub_record as b on a.Record_Recycling_number=b.Sub_Recycling_number where a.Record_LINEid='%s' group by a.Record_LINEid and date(a.Record_Recycling_time)= curdate()" % (line_id)), '1')

    print(today_record)
    

    div = []

    for i in range(len(today_record)):
        # d_time = datetime.strftime(today_record[i][0], '%Y-%m-%d %H:%M')
        div.append({"type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "本日紀錄",
                                        "weight": "bold",
                                        "color": "#1DB446",
                                        "size": "16px"
                                    },
                                    {
                                        "type": "text",
                                        "text": "1",
                                        "weight": "bold",
                                        "size": "22px",
                                        "flex": 0
                                    },
                                    {
                                        "type": "separator",
                                        "margin": "5px"
                                    }
                                ],
                                "height": "75px",
                                "paddingTop": "15px"
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "icon",
                                                        "url": "https://i.imgur.com/W5OteZZ.png",
                                                        "size": "20px",
                                                        "offsetTop": "1px"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "weight": "bold",
                                                        "size": "20px",
                                                        "margin": "md",
                                                        "text": today_record[i][1],
                                                        "flex": 0
                                                    }
                                                ],
                                                "spacing": "none",
                                                "margin": "xs"
                                            },
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "icon",
                                                        "url": "https://i.imgur.com/Im2m2S1.png",
                                                        "size": "20px",
                                                        "offsetTop": "3px"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "weight": "bold",
                                                        "size": "20px",
                                                        "margin": "md",
                                                        "text": today_record[i][2],
                                                        "flex": 0
                                                    }
                                                ],
                                                "margin": "xs"
                                            },
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "icon",
                                                        "url": "https://i.imgur.com/IHx8NYC.png",
                                                        "size": "20px",
                                                        "offsetTop": "3px",
                                                        "offsetStart": "1px"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "weight": "bold",
                                                        "size": "20px",
                                                        "margin": "md",
                                                        "text": str(today_record[i][3]),
                                                        "flex": 0
                                                    }
                                                ],
                                                "margin": "xs"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "image",
                                        "url": "https://i.imgur.com/06wOhyx.png",
                                        "size": "lg",
                                        "action": {
                                            "type": "uri",
                                            "label": "action",
                                            "uri": today_record[i][4]
                                        }
                                    }
                                ],
                                "alignItems": "center"
                            }
                        ],
                        "paddingTop": "1%",
                        "height": "200px"
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "　累積點數  30p 　＞",
                                        "size": "20px",
                                        "align": "center",
                                        "weight": "bold"
                                    }
                                ],
                                "borderWidth": "bold",
                                "height": "50px",
                                "cornerRadius": "lg",
                                "backgroundColor": "#c3e1c3",
                                "justifyContent": "center",
                                "width": "90%"
                            }
                        ],
                        "justifyContent": "center",
                        "alignItems": "center",
                        "paddingBottom": "lg"
                }
            }
        )
        

    with open('src/json/record.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        data['contents'] = div

    with open('src/json/record.json', 'w', encoding='utf-8') as file:
        json.dump(data, file)

    search_record = json.load(
        open('src/json/record.json', 'r', encoding='utf-8'))

    return search_record

#//判斷txt是什麼紀錄
def record(txt,line_id):
    if txt == '本日紀錄':
        return record_today()
    elif  txt == '本周紀錄':
        return record_week()
    elif  txt == '本月紀錄':
        return record_month(line_id)
    elif  txt == '累積紀錄':
        return record_add()

def record_today():

    
    record_today = json.load(open('src/json/record_today.json', 'r', encoding='utf-8'))
    imagemap_today = ImagemapSendMessage(
        base_url='https://i.imgur.com/Z96l63C.png',
        alt_text='this is an imagemap',
        base_size=BaseSize(height=110, width=1040),
        actions=[
            MessageImagemapAction(
                text='本日紀錄',
                area=ImagemapArea(
                    x=4, y=8, width=175, height=92
                )
            ),
            MessageImagemapAction(
                text='本周紀錄',
                area=ImagemapArea(
                    x=205, y=8, width=154, height=92
                )
            ),
            MessageImagemapAction(
                text='本月紀錄',
                area=ImagemapArea(
                    x=402, y=8, width=160, height=96
                )
            ),
            MessageImagemapAction(
                text='累積紀錄',
                area=ImagemapArea(
                    x=598, y=8, width=147, height=96
                )
            )
        ]
    )
    return[FlexSendMessage('record_today', record_today),imagemap_today]

def record_week():
    record_today = json.load(open('src/json/record_week.json', 'r', encoding='utf-8'))
    imagemap_today = ImagemapSendMessage(
        base_url='https://i.imgur.com/PmTz1kD.png',
        alt_text='this is an imagemap',
        base_size=BaseSize(height=110, width=1040),
        actions=[
            MessageImagemapAction(
                text='本日紀錄',
                area=ImagemapArea(
                    x=4, y=8, width=175, height=92
                )
            ),
            MessageImagemapAction(
                text='本周紀錄',
                area=ImagemapArea(
                    x=205, y=8, width=154, height=92
                )
            ),
            MessageImagemapAction(
                text='本月紀錄',
                area=ImagemapArea(
                    x=402, y=8, width=160, height=96
                )
            ),
            MessageImagemapAction(
                text='累積紀錄',
                area=ImagemapArea(
                    x=598, y=8, width=147, height=96
                )
            )
        ]
    )
    return[FlexSendMessage('record_today', record_today),imagemap_today]

def record_month(line_id):
    pie_month(line_id)

    record_today = json.load(open('src/json/record_month.json', 'r', encoding='utf-8'))
    imagemap_today = ImagemapSendMessage(
        base_url='https://i.imgur.com/jHrl9VA.png',
        alt_text='this is an imagemap',
        base_size=BaseSize(height=110, width=1040),
        actions=[
            MessageImagemapAction(
                text='本日紀錄',
                area=ImagemapArea(
                    x=4, y=8, width=175, height=92
                )
            ),
            MessageImagemapAction(
                text='本周紀錄',
                area=ImagemapArea(
                    x=205, y=8, width=154, height=92
                )
            ),
            MessageImagemapAction(
                text='本月紀錄',
                area=ImagemapArea(
                    x=402, y=8, width=160, height=96
                )
            ),
            MessageImagemapAction(
                text='累積紀錄',
                area=ImagemapArea(
                    x=598, y=8, width=147, height=96
                )
            )
        ]
    )
    return[FlexSendMessage('record_today', record_today),imagemap_today]


def record_add():
    record_today = json.load(open('src/json/record_add.json', 'r', encoding='utf-8'))
    imagemap_today = ImagemapSendMessage(
        base_url='https://i.imgur.com/g0WeLP1.png',
        alt_text='this is an imagemap',
        base_size=BaseSize(height=110, width=1040),
        actions=[
            MessageImagemapAction(
                text='本日紀錄',
                area=ImagemapArea(
                    x=4, y=8, width=175, height=92
                )
            ),
            MessageImagemapAction(
                text='本周紀錄',
                area=ImagemapArea(
                    x=205, y=8, width=154, height=92
                )
            ),
            MessageImagemapAction(
                text='本月紀錄',
                area=ImagemapArea(
                    x=402, y=8, width=160, height=96
                )
            ),
            MessageImagemapAction(
                text='累積紀錄',
                area=ImagemapArea(
                    x=598, y=8, width=147, height=96
                )
            )
        ]
    )
    return[FlexSendMessage('record_today', record_today),imagemap_today]


def pie_month(line_id):
    quantity = DB.run(('select d.Type_Name ,count(d.Type_Name) from treasure.treasure_recycling_record as a join treasure.treasure_sub_record as b on a.Record_Recycling_number=b.Sub_Recycling_number join treasure.treasure_erection_location as c on a.Record_Location_number=c.Location_Number join treasure.treasure_type as d on b.Sub_Type_number = d.Type_Number where a.Record_LINEid="%s" and month(a.Record_Recycling_time)=month(now()) group by d.Type_Name' %(line_id)),'1')

    # 指定使用字型和大小
    myFont = FontProperties(fname='C:/Users/Dolly/AppData/Roaming/Python/Python38/site-packages/matplotlib/mpl-data/fonts/ttf/TaipeiSansTCBeta-Regular.ttf', size=14)

    # 設定顏色

    color = ['#EDBBBC', '#F8BA91', '#FDDB7E', '#B3D89B', '#A8C3D9', '#808ef9']

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

    # 畫出圓餅圖
    plt.savefig("src/static/pie/p1.jpg")
    # plt.show()