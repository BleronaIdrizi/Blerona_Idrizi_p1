import datetime
# 10.04.2020 11:00:00 PM

x=datetime.datetime.now()

print(x.strftime("%d.%m.%Y")+ " " +x.strftime('%X')+" "+ x.strftime('%p'))
