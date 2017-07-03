#!/usr/bin/env python

import os, sys, matplotlib.pyplot as plt
from matplotlib import rc
# from matplotlib.font_manager import FontProperties
import numpy as np

fname = sys.argv[1]
marker= '-'
if len(sys.argv)>2:
    marker = sys.argv[2]

# print '  Plotting',fname,'using 1st column vs. 2nd and ignoring #s and @s'

# font = FontProperties()
# font.set_family('serif')
plt.rcParams["font.family"] = "serif"
rc('font',**{'family':'serif','serif':['Cambria']})
# rc('text', usetex=True)

fin = open(fname,'r')
ll  = fin.readlines()
fin.close()

x = []
y = []

title  = 'title'
xlabel = 'xaxis'
ylabel = 'yaxis'

for l in ll:
    if l[0] not in ['@','#']:
        s = l.split()
        if len(s)>1:
            x.append(float(s[0]))
            yi = []
            for ys in s[1:]:
                yi.append(float(ys))
            y.append(yi)
    elif l[0]=='@':
        s = l.split()
        if s[1]=='title':
            ind = l.find('"')
            title = l[ind+1:-2]
        elif s[1]=='xaxis':
            ind = l.find('"')
            xlabel = l[ind+1:-2]
        elif s[1]=='yaxis':
            ind = l.find('"')
            ylabel = l[ind+1:-2]

x = np.asarray(x)
y = np.asarray(y)
# print x.shape, y.shape
fig = plt.figure()
plt.grid(b=True, which='major', color='grey', linestyle='--')
plt.plot(x,y,marker)
plt.title(title)
plt.xlabel(xlabel.replace("\\x","").replace("\\f{}","").replace("\\f{12}","").replace("\\f{4}","").replace("\\S-1\\N","$^{-1}$"))
plt.ylabel(ylabel.replace("\\x","").replace("\\f{}","").replace("\\S-1\\N","$^{-1}$").replace("\\S-3\\N","$^{-3}$"))

plt.show()
