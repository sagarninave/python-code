from datetime import date
        
def cal_age(dat):
        
        now=date.today()
        td=now.day
        tm=now.month
        ty=now.year
        if dat.day>td:
           td+=30
           tm-=1
        dd=td-dat.day
        if dat.month>tm:
            tm+=12
            ty-=1
        mm=tm-dat.month
        yy=ty-dat.year
        
        return[yy, mm, dd]
        
