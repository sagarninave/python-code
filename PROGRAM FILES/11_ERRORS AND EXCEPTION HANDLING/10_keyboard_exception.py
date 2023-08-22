try:
    print ('Press Return or Ctrl+C:')
    ignore = input()
    print(ignore)
except KeyboardInterrupt:
    print ('Caught KeyboardInterrupt')
else:
    print ('No exception')
