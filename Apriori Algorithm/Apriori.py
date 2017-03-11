from __future__ import division
from itertools import permutations
from sets import Set


def uniqueItems(transSet):
  
  uniqItems = Set([])
  for trans in transSet:
    
    for items in trans:
      
      uniqItems.add(items)     
  return uniqItems
  
def supportValue(items,tTranSet):
  
  support=0
  for trans in tTranSet:
  
    flag=True
    for item in items:
  
      if item not in trans:
      
        flag=False
        break    
    if flag:
    
      support = support+1
  return support/len(tTranSet)
  
def combSet(uniqItems,cSet,forbSet):
  
  comb = Set([])
  for iSet in cSet:
      
    for items in iSet:
      
      tempSet = Set([])
      for item in items:
        
        tempSet.add(item) 
      for nItem in uniqItems:
    
        tSet = tempSet.copy()
        if nItem in items:
    
          continue
        tSet.add(nItem)
        if tSet in forbSet:
      
          continue  
        comb.add(frozenset(tSet))
  return comb

def Conf(lhs,items,tTranSet):

  return supportValue(items,tTranSet)/supportValue(lhs,tTranSet)
 
def buildSet(uniqItems):
  
  cSet = Set([])
  for items in uniqItems:
  
    cSet.add(frozenset([frozenset([items])]))
  return cSet
    
    
fileName = raw_input('Enter the transaction file name: ')
opFile = raw_input('Enter the output file name: ')
support = input('Enter the minimum support: ')
confidence = input('Enter the minimum confidence: ')
tTranSet = Set([])
utTranSet = Set([])
fSets = Set([])
f = open(opFile, 'w')
sper = support*100
cper = confidence*100
f.write('Support = {}%\nConfidence = {}%'.format(sper,cper))
with open(fileName,'r') as table:
  
  for transaction in table:
     
    if(transaction!=""):
      
      transaction = transaction.rstrip()
      uTempSet = Set([])
      tempSet = Set([])
      items = transaction.split(',')
      for item in items:
      
        uTempSet.add(item)
        tempSet.add(frozenset([item]))
      if len(uTempSet)>0:
       
        tranSet = frozenset(tempSet)
        tTranSet.add(tranSet)
        tranSet = frozenset(uTempSet) 
        utTranSet.add(tranSet)     
uniqItems = uniqueItems(utTranSet)
forbSet = Set([])
iteration = len(uniqItems)-1
cSet = buildSet(uniqItems)
for i in range(1,iteration):

  comb = combSet(uniqItems,cSet,forbSet)
  cSet.clear()
  for items in comb:
  
    if supportValue(items,utTranSet)<support:
      
      forbSet.add(items)
      continue
    cSet.add(frozenset([items]))
    fSets.add(items)    
  uniqItems = uniqueItems(comb)
  if len(uniqItems)==0:
  
    break    
for fItems in fSets:

  tItem = []
  Rules = {}
  for fItem in fItems:
  
    tItem.append(fItem)
  op = list(permutations(tItem))
  for opItem in op:
  
    for i in range(1,len(opItem)):
      
      lhs = opItem[:i]
      rhs = opItem[i:]
      tConf = Conf(lhs,opItem,utTranSet) 
      if tConf>=confidence:
      
        lhsSet = frozenset(lhs)
        rhsSet = frozenset(rhs)
        if(lhsSet in Rules):
        
          if(rhsSet in Rules.get(lhsSet)):
          
            continue
          else:
            
            trhsSet = Rules.get(lhsSet)
            trhsSet.add(rhsSet)
        else:
          
          trhsSet = [rhsSet]
          Rules[lhsSet] = trhsSet
        print '{} -> {}'.format(lhs,rhs)
        f.write('\n{} -> {}'.format(lhs,rhs))
f.close()

    

  
  
  
  
  














