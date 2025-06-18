import numpy as np

def calculate(lst):
  if(len(lst) != 9):
    raise ValueError('List must contain nine numbers.')
  else:
    a=np.reshape(lst,(3,3))
    cal = {'mean' : [(np.mean(a,axis=0)).tolist(),(np.mean(a,axis=1)).tolist(),(np.mean(a)).tolist()] }
    cal ['variance'] = [(np.var(a,axis=0)).tolist(),(np.var(a,axis=1)).tolist(),(np.var(a)).tolist()] 
    cal ['standard deviation'] = [(np.std(a,axis=0)).tolist(),(np.std(a,axis=1)).tolist(),(np.std(a)).tolist()] 
    cal ['max'] = [(np.max(a,axis=0)).tolist(),(np.max(a,axis=1)).tolist(),(np.max(a)).tolist()] 
    cal ['min'] = [(np.min(a,axis=0)).tolist(),(np.min(a,axis=1)).tolist(),(np.min(a)).tolist()] 
    cal ['sum'] = [(np.sum(a,axis=0)).tolist(),(np.sum(a,axis=1)).tolist(),(np.sum(a)).tolist()] 
    return cal

