#!/usr/bin/env python

import os,sys

delimiter = ','

fname = sys.argv[1]
if fname[-3:] != "xvg":
    print "The provided file is not in .xvg format."
    sys.exit(0)

with open(fname, 'r') as fid:
  ll = fid.readlines()

try:
  rem = int(sys.argv[2])
except:
  rem = 1

fout = open(fname[:-3]+'csv','w')

it = 0
M = len(ll[-1].split())
labels = [""]*M
labels[0] = "Time (ps)"
print "Found",M,"columns:"
print '  ',"Time"

i=1
for l in ll:
  if l.startswith("@ s"):
      label = ' '.join(l.split()[3:])[1:-1]
      print '  ',label
      labels[i] = label
      i += 1
      if i == M:
          fout.write(delimiter.join(labels)+'\n')
  if l[0] in ['#','@']:
    continue
  elif it%rem == 0:
    s = l.split()
    fout.write(delimiter.join(s)+'\n')
  it += 1
fout.close()
