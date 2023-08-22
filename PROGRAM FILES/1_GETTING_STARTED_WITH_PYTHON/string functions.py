message = "Hello World"
print(message.find("World"))
# it finds starting point of word, and world is tart on index 6


message1 = "Hello World"
print(message1.find("there"))
#it does not find anything so that it return -1

message2 = "Hello World"
message2.replace("Hello", "Hey")
print(message2)

# it does not place string like this because replace function return new string
# see changes in below lines

new_message = message2.replace("Hello", "Hey")
print(new_message)


indexing = ["hey", "sagar", "sanket", "rajas", "rmesh"]
print("index : ", indexing.index("sagar"))

print("sagar" in indexing) # it return true
print("sagar ninave" in indexing) # it return False


join_1 = "".join(indexing)
print("Join 1 : ", join_1)

join_2 = " ".join(indexing)
print("Join 2 : ", join_2)

join_3 = ", ".join(indexing)
print("Join 3 : ", join_3)

join_4 = " - ".join(indexing)
print("Join 4 : ", join_4)

split_1 = join_2.split(" ")
print("split 1 : ", split_1)