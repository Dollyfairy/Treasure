import qrcode,random
from linebot.models import *
# ? 不能只import DB
from utility import DB
import zxing
import time



# # //取得mcode 製作QRcode
def mcodeQR():
    mcode = DB.run('SELECT Location_Machinecode FROM treasure_erection_location','1')
    for i in range(len(mcode)):
        randomQR=random.randint(1,5)
        randomborder=random.randint(4,11)
        if randomQR==1:
            qr = qrcode.QRCode(version = 3, error_correction = qrcode.constants.ERROR_CORRECT_L, box_size = 10,border = randomborder)
        elif randomQR==2:
            qr = qrcode.QRCode(version = 3, error_correction = qrcode.constants.ERROR_CORRECT_M, box_size = 10,border = randomborder)
        elif randomQR==3:
            qr = qrcode.QRCode(version = 3, error_correction = qrcode.constants.ERROR_CORRECT_Q, box_size = 10,border = randomborder)
        else:
            qr = qrcode.QRCode(version = 3, error_correction = qrcode.constants.ERROR_CORRECT_H, box_size = 10,border = randomborder)

        qr.add_data(mcode[i][0]) 
        qr.make(fit = True)
        img = qr.make_image()
        img.save(f'src/img/QR{i+1}.jpg')

    return 0

# //開啟相機
def open_camera():
    emoji=[
            {
                "index": 0,
                "productId": "5ac21e6c040ab15980c9b444",
                "emojiId": "082"
            },
            {
                "index": 8,
                "productId": "5ac22e85040ab15980c9b44f",
                "emojiId": "045"
            },
            {
                "index": 18,
                "productId": "5ac2264e040ab15980c9b44b",
                "emojiId": "222"
            },
            {
                "index": 35,
                "productId": "5ac2280f031a6752fb806d65",
                "emojiId": "001"
            },
            {
                "index": 36,
                "productId": "5ac22775040ab15980c9b44c",
                "emojiId": "244"
            }
            
        ]
    camera = TextSendMessage(
        text='$點擊開啟相機\n$拍攝QRcode\n$等待閘門打開\n就可以開始回收啦~$$',
        emojis=emoji,
        quick_reply=QuickReply
        (
            items=[
                QuickReplyButton(
                    action=CameraAction(
                        label="開啟相機",
                        text="text"
                    )
                )
            ]
        )
    )

    return camera

# login_info()

# //解讀 userQR
def decodeQR(line_id,message_content):
    with open('src/img/1.jpg', 'wb') as fd:
        for chunk in message_content.iter_content():
            fd.write(chunk)
    print('照片1')

    reader = zxing.BarCodeReader()
    barcode = reader.decode('src/img/1.jpg')
    print('照片2')
    return line_id,barcode.parsed

# //透過Line_id檢查是否有此user
def check_user_db(line_id):
    check = DB.run("SELECT Member_LINEid FROM treasure.treasure_member where Member_LINEid = '%s'" %(line_id),'2')
    if len(check) == 1:
        return True



# ? 驗證user 新增總紀錄 開門
def add_record(line_id,mcode,recycling_time):

    # //有此user的話，add總紀錄
    if check_user_db(line_id):
        recycling_number = DB.run("SELECT max(Record_Recycling_number)+1 FROM treasure.treasure_recycling_record",'1')[0][0]
        location_number = DB.run(("SELECT Location_Number  FROM treasure.treasure_erection_location where Location_Machinecode ='%s'") %(mcode),'1')[0][0]
        print(recycling_number,location_number)

        DB.run('INSERT INTO treasure_recycling_record (Record_Recycling_number , Record_LINEid , Record_Location_number , Record_Recycling_time)' 'VALUES (%d,"%s",%d,"%s")' %(recycling_number,line_id,location_number,recycling_time))
    else:
        return 'hhhhhhh'

        #!開門
        #! return TextSendMsg() 告訴user可以回收，讓他選擇回收完畢or取消回收