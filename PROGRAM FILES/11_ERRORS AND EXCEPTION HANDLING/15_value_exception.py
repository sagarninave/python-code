try:
    print(int('a'))
except ValueError:
    print ('Caught ValueError Exception')
else:
    print ('No exception')
