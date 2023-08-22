from skimage import data
coffeecup=data.coffee()
import matplotlib.pyplot as plt
#plt.imshow(coffeecup)
print(type(coffeecup))
print(coffeecup.shape)
coffeecup[120:150,270:300]=[255,255,255]
plt.imshow(coffeecup)



