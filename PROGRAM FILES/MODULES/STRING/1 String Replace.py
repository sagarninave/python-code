our_str = 'Hello World'
 
import string
 
new_str = string.replace(our_str, 'World', 'Jackson')
print(new_str)
 
new_str = string.replace(our_str, 'Hello', 'Hello,')
print(new_str)
 
our_str = 'Hello you, you and you!'
new_str = string.replace(our_str, 'you', 'me', 1)
print(new_str)
new_str = string.replace(our_str, 'you', 'me', 2)
print(new_str)
new_str = string.replace(our_str, 'you', 'me', 3)
