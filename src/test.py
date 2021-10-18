from datetime import datetime
from re import S
from utility import DB


import pandas as pd
import plotly.express as px
df = pd.DataFrame([
    ['Czech Republic', 10228744], ['France', 61083916], ['Germany', 82400996],
    ['Greece', 10706290], ['Italy', 58147733], ['Netherlands', 16570613],
    ['Poland', 38518241], ['Portugal', 10642836], ['Romania', 22276056],
    ['Spain', 40448191], ['Turkey', 71158647], ['United Kingdom', 60776238]],
    columns=['country', 'pop'])
fig = px.pie(df, values='pop', names='country', title='Population')
# fig.show()
fig.save("111111.png")
# def hi():
#     line_id = "U0131826f2d23e1f17a3689d8574fd2cb"
#     abc = DB.run("SELECT Member_LINEid FROM treasure.treasure_member where Member_LINEid = '%s'" %(line_id),'2')
#     if len(abc) == 1:
#         return len(abc)



# print(datetime.today())
# aaa = DB.run('INSERT INTO treasure.treasure_service (Service_LINEid, Service_Location, Service_Problem) VALUES ("%s","%s","%s")' %('U0131826f2d23e1f17a3689d8574fd2cb','台北市中正區','機台門口打不開'))

# print(aaa)

