#!/usr/bin/env python

import os,sys, numpy as np
from matplotlib import pyplot as plt

fname = sys.argv[1]
if fname[-3:] != "xvg":
    print "The provided file is not in .xvg format."
    sys.exit(0)

with open(fname, 'r') as fid:
  ll = fid.readlines()

try:
  column = int(sys.argv[2])
except:
  column = 1

try:
  nbins = int(sys.argv[3])
except:
  nbins = 100

M = len(ll[-1].split())
labels = [""]*M
labels[0] = "Time (ps)"
print "Found",M,"columns:"
print '  ',"Time"
ALL = []
i=1
for l in ll:
  if l.startswith("@ s"):
      label = ' '.join(l.split()[3:])[1:-1]
      print '  ',label
      labels[i] = label
      i += 1
  if l[0] in ['#','@']:
    continue
  s = l.split()
  ALL.append([float(x) for x in s])

ALL = np.asarray(ALL)
print "Data length:",ALL.shape[0]

x = ALL[:,0]
y = ALL[:,column]

values,bins = np.histogram(y,nbins)
bins = (bins[:-1]+bins[1:])/2

with open("histogram.csv",'w') as fout:
    fout.write(labels[column]+",Counts\n")
    for i in range(nbins):
        fout.write("%f,%f\n" % (bins[i],values[i]))



plt.plot(bins,values)
plt.title("Histogram")
plt.xlabel(labels[column])
plt.ylabel("Counts")
plt.show()
