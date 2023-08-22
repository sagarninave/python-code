x = 5
y = 6

st = "x is less than y" if (x < y) else "x is greater than or equal to y"
print (st)
  
  # Python does not have support for higher-order conditionals
  # like "switch-case" in other languages
  
a, b = 10, 20
  
print ("Both a and b are equal" if a == b else "a is greater than b"
        if a > b else "b is greater than a") 

a,b,c=10,40,30

if a>b and a>c:
    print(a, "a is greater")
else:
    if b>a and b>c:
        print(b, "b is grater")
    else:
        print(c, "c is greater")
print("a is greater" if a>b and a>c else "b is grater" if b>a and b>c else "c is greater")
