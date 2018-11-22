
import datetime


date_format = "%Y-%m-%d %H:%M:%S"
date_format = "%Y-%m-%d"

date_1 = '2018-07-02 09:00:00'

date_2 = '2018-07-02 12:00:00'

dt_1 = datetime.datetime.strptime(date_1, date_format)

dt_2 = datetime.datetime.strptime(date_2, date_format)

dt_2 - dt_1


now = datetime.datetime.now()