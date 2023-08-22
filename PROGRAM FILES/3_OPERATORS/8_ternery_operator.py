x = 5
y = 6
  # conditional statements let you use "a if C else b"
st = "x is less than y" if (x < y) else "x is greater than or equal to y"
print (st)
  
  # Python does not have support for higher-order conditionals
  # like "switch-case" in other languages
  
a, b = 10, 20
  
print ("Both a and b are equal" if a == b else "a is greater than b"
        if a > b else "b is greater than a") 
