from datetime import datetime

now = datetime.now()
format = "%d-%m-%Y %H:%M:%S"
time1 = now.strftime(format)
print(time1)