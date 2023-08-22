import re

str = "hello sagar how are you, + helo i am M good what is your age, i am 23 year old"

###################################### Regular Expressions Functions

#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)
if (x):
  print("YES! We have a match!")
else:
  print("No match")

str1 = "The rain in Spain"
x = re.findall("ai", str1)
print(x)

# x1=re.search("^hello.*sagar$", str)
# print(x1,"\n")
# if (x1):
#     print(str,"\n")
# else:
#     print("not found\n")

# x2=re.findall("hello", str)
# print(x2,"\n")

# x3=re.findall("hellos", str)
# print(x3,"\n")

x3 = re.search('\s', str)
print('white space found at positon: ', x3.start())

x4 = re.split('\s', str)
print("\n",x4, "\n")

print(str.split(' '))

x5 = re.sub("\s", "_", str)
print(x5,"\n")

x6 = re.sub("\s", "_", str, 2)
print(x6,"\n")

###################################### Regular Expressions Metacharacter

x7 = re.findall('[a-m]', str)   # [] set of character
print("Set Character : ",x7,"\n")

x7_1 = re.findall("[asrhyu]", str) #Returns a match where one of the specified characters [asrhyu]
print(x7_1, "\n")

x7_2 = re.findall("[e-h]", str) # retuns the match between [e-h]
print("Between E-H : ",x7_2, "\n")

x7_3 = re.findall("[^hsy ]", str)# Returns a match for any character EXCEPT a, r, and n
print("Word Starts With H, S, Y: ",x7_3, "\n")

x7_4 = re.findall("[23]", str)  # Returns a match where any of the specified digits 2 and 3 are present
print("Digit Find : ", x7_4, "\n")

x7_5 = re.findall("[1-4]", str) # Returns a match for any digit between 0 and 9
print("Digits Between [1-4] : ", x7_5, "\n")

x7_6 = re.findall("[0-2][2-4]", str)  # Returns a match for any two-digit numbers from 00 04
print("Digit Between [0-2][2-4] : ", x7_6, "\n")

x7_7 = re.findall("[a-zA-Z]", str) # Returns a match for any character alphabetically between a and z, lower case OR upper case
print("All Characters in String : ", x7_7, "\n")

x7_8 = re.findall("[+]", str)      # Check if the string has any + characters:
print("String has any character: ", x7_8, "\n")


x8 = re.findall("\d", str)      # \ single sequence 
print(x8,"\n")

x8_1 = re.findall("\Ahello", str) # string Must Be in Begining 
print("First Word From String: " ,x8_1, "\n")

x8_2 = re.findall(r"old\b", str) # string Must Be in Begining or last
print("last Word From String: " ,x8_2, "\n")

x8_3 = re.findall(r"ar\B", str) # string Must Be in middle
print("In Middle of String: " ,x8_3, "\n")

x8_4 = re.findall("\D", str) # doe not contain digits
print("Does Not Contain Digits in String: " ,x8_4, "\n")

x8_5 = re.findall("\s", str) # Returns a match where the string contains a white space characte
print("Contain White Space Character in String: " ,x8_5, "\n")

x8_6 = re.findall("\S", str) # Returns a match where the string does not contains a white space characte
print("Does Not White Space Character in String: " ,x8_6, "\n")

x8_7 = re.findall("\w", str) # Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
print("Contains Digits And Character in String: " ,x8_7, "\n")

x8_8 = re.findall("\W", str) # Return a match at every NON word character 
print("Contains None Word Character in String: " ,x8_8, "\n")

x8_9 = re.findall(r"old\Z", str) # Return End word character 
print("Return End word character in String: " ,x8_9, "\n")

x9 = re.findall("he..o", str)   # . any character
print(x9,"\n")

x10 = re.findall("^hello", str) # ^ starts with
print(x10)
if x10:
    print("yes it is starts with ", x10, "\n")
else:
    print("does not starts with ", x10, "\n")

x11 = re.findall("old$", str)   # $ ends with
print(x11)
if x11:
    print("yes it is starts with ", x11, "\n")
else:
    print("does not starts with ", x11, "\n")

x12 = re.findall("a*", str)     # * zero or more occurence
x13 = re.findall("ax*", str)
print(x12, "\n")
print(x13, "\n")

str1 = "heys sagars"            # + one or more occurence
x14 = re.findall("s+", str1)
print(x14,"\n")

x15 = re.findall("hel{2}", str) # {} exactly specific number of occurence 
print(x15, "\n")

x16 = re.findall("helloo | sagar", str)
print(x16)
