import pymysql
import datetime
conn = pymysql.connect(
    user='smart-mirror',
    passwd='1234',
    host='localhost',
    db='mirrordb',
    charset='utf8'
)
cursor = conn.cursor()


days = ['mon', 'tue', 'wen', 'thu', 'fri', 'sat', 'sun']
today = datetime.datetime.today().weekday()

sql = 'select name from medicine where userID=1 && '+ days[today]+'=1'
cursor.execute(sql)
result = cursor.fetchall()
print('오늘 먹어야 하는 약은')
i = 0
while(i<len(result)):
    medicine = result[i][0]
    print(medicine) 
    if(medicine == pymysql.NULL):
        break
    i = i+1
   
