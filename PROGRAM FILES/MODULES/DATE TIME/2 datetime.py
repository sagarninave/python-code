from datetime import date
#from datetime import date
def cal_age():
    cdate=date(2018,6,27) # yyyy-mm-dd format
    dob=date(1996,6,8)
    return cdate.year-dob.year
print(cal_age())
