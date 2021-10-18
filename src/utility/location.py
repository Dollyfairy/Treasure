from math import sin, cos, sqrt, atan2, radians
import json
# ? 為啥可以只import DB
from utility import DB


# //算出[3個]近距離
def location(user_lat, user_lng):
    datas = DB.run("SELECT * FROM treasure.treasure_erection_location", "1")
    outData = []

    for i in range(len(datas)):
        no, station, address, mcode, lat, lng, url = datas[i]

        lat = float(lat)
        lng = float(lng)
        user_lat = float(user_lat)
        user_lng = float(user_lng)

        # 計算捷運站至北商的距離(公里)
        R = 6373.0
        lat1 = radians(lat)
        lng1 = radians(lng)
        lat2 = radians(user_lat)
        lng2 = radians(user_lng)

        dlon = lng2 - lng1
        dlat = lat2 - lat1
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = round(R * c, 2)

        # 將每行資料加入清單中
        outData.append((station, distance, address, lat, lng, url))
    s = sorted(outData, key=lambda x: x[1])

    div = []

    for i in range(3):
        div.append({
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": s[i][0],
                        "weight": "bold",
                        "size": "lg",
                        "margin": "none",
                        "wrap": True
                    },
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
                                        "url": "https://i.imgur.com/fUP8pRm.png"
                                    },
                                    {
                                        "type": "text",
                                        "text": s[i][2],
                                        "weight": "bold",
                                        "margin": "md",
                                        "wrap": True
                                    }
                                ],
                                "action": {
                                    "type": "uri",
                                    "label": "action",
                                    "uri": s[i][5]
                                }
                            }
                        ]
                    }
                ]
            })
    

    with open('src\json\location.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        data["body"]['contents'] = div

    with open('src\json\location.json', 'w', encoding='utf-8') as file:
        json.dump(data, file)

    search_location = json.load(open('src\json\location.json','r',encoding='utf-8'))
    
    return search_location



