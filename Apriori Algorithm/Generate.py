from itertools import permutations
import csv
import random
from sets import Set

uniqItems = ['Milk','Cheese','Fruits','Beer','Water','Snacks','Soda','Butter','Vegetables','choclate']
f = open('transaction5.csv','w')
cw = csv.writer(f)
for i in range(1,20):

  ran = random.randint(3,7)
  i = 0
  itemSet = Set([])
  while i<ran:
    
    ran1 = random.randint(0,9)
    if uniqItems[ran1] in itemSet:
      
      continue
    itemSet.add(uniqItems[ran1])
    i=i+1
  cw.writerow(list(itemSet))
f.close()
