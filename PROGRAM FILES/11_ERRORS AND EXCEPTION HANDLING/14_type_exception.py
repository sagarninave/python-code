try:
    a=int(5)
    b=str
    c=a+b
except TypeError:
    print ('Caught TypeError Exception')
else:
    print ('No exception')
