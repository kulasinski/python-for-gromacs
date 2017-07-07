#!/usr/bin/env python

import os, sys, matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np

marker= '-'

plt.rcParams["font.family"] = "serif"
rc('font',**{'family':'serif','serif':['Cambria']})

import os,sys, numpy as np
from matplotlib import pyplot as plt

fname = sys.argv[1]
if fname[-3:] != "xvg":
    print "The provided file is not in .xvg format."
    sys.exit(0)

with open(fname, 'r') as fid:
  ll = fid.readlines()

try:
  inputc = sys.argv[2].split(',')
except:
  inputc = ['1:2']

indices = []
for c in inputc:
    s = c.split(':')
    indices.append([int(s[0])-1,int(s[1])-1])

try:
  marker = sys.argv[3]
except:
  marker = '-'

M = len(ll[-1].split())
labels = [""]*M
labels[0] = "Time (ps)"
print "Found",M,"columns:"
print '  ',"[1] Time"
ALL = []
i=1
for l in ll:
  if l.startswith("@ s"):
      label = ' '.join(l.split()[3:])[1:-1]
      print '  ','[%d]'%(i+1),label
      labels[i] = label
      i += 1
  if l[0] in ['#','@']:
    continue
  s = l.split()
  ALL.append([float(x) for x in s])

ALL = np.asarray(ALL)
print '  ',"Data array dimensions:",ALL.shape[0],'x',ALL.shape[1]

for ind in indices:
    plt.plot(ALL[:,ind[0]],ALL[:,ind[1]],marker,label=labels[ind[1]])
plt.legend()
plt.grid(b=True, which='major', color='grey', linestyle='--')
plt.xlabel(labels[indices[0][0]])
plt.ylabel(', '.join( labels[ind[1]] for ind in indices ))
plt.title('Content of \'%s\'' % fname)
plt.show()
