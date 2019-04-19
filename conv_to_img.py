import sys
import os
from math import log
import numpy as np
import scipy as sp
from PIL import Image

def saveimg(array,name):
    print name
    print array.shape
    if array.shape[1]!=16:
        assert(False)
    b=int((array.shape[0]*16)**(0.5))
    b=2**(int(log(b)/log(2))+1)
    a=int(array.shape[0]*16/b)
    print a,b,array.shape
    array=array[:a*b/16,:]

    array=np.reshape(array,(a,b))
    #print array.shape
    #array = np.uint8(array)
    #print array
    #array.resize((128,128))
     
    im = Image.fromarray(np.uint8(array))
    im.save('image_bytes2_size_asal/'+name[:-6]+'.jpg', "JPEG")
    
files=os.listdir('test')
c=0
for cc,x in enumerate(files):
    if '.bytes' != x[-6:]: #skip .asm file
        continue
    print cc
    
    f=open('test/'+x)
    array=[]
    c+=1
    for line in f:
        xx=line.split()
        if len(xx)!=17:
            continue
        #if xx[1]=='??':
        #    break
        array.append([int(i,16) if i!='??' else 0 for i in xx[1:] ])
    saveimg(np.array(array),x)
    del array
    f.close()
    
print c

