import json
from linebot import LineBotApi
from linebot.models import TextSendMessage
from datetime import datetime

file = open('info.json','r')
info = json.load(file)

sqedule = [
    ['会計システム : 村上 : 8209','知的財産権 : 山口 : 7105'],
    ['情報リスクマネジメント : 角田 : 5209','ファイナンス概論 : 喜多村 : 8209','データマイニング入門 : 井上 : 8203'],
    ['金融リスク論 : 安藤 : 5209','ビジネスコミュニケーション : 山本 : オンライン'],
    ['製品安全マネジメント : 越山 : 8105','私の研究 : 市川 : 5306','環境保護と法 : 藤本 : オンライン']
]

week = datetime.today().weekday()
hour = datetime.now().hour
 
while True: 
        ## 月曜日
        if week == 0 and hour < 10:
            x = sqedule[week][0]
            break
        if week == 0 and hour < 13:
            x = sqedule[week][1]
            break
        ##水曜日    
        if week == 2 and hour < 10:
            x = sqedule[week-1][0]
            break
        if week == 2 and hour < 13:
            x = sqedule[week-1][1]
            break
        if week == 2 and hour < 15:
            x = sqedule[week-1][2]
            break
        ## 木曜日 
        if week == 3 and hour < 10:
            x = sqedule[week-1][0]
            break
        if week == 3 and hour < 15:
            x = sqedule[week-1][1]
            break
       ## 金曜日
        if week == 4 and hour < 10:
            x = sqedule[week-1][0]
            break
        if week == 4 and hour < 13:
            x = sqedule[week-1][1]
            break
        if week == 4 and hour < 15:
            x = sqedule[week-1][2]
            break
        
        
Access_Token = info['token']
line_bot_api = LineBotApi(Access_Token)


User_Id = info['your_id']
message= TextSendMessage(text=x)
line_bot_api.push_message(User_Id,messages=message)