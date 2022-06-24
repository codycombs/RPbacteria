import numpy as np
from scipy import integrate

def calc_base_i(_i):
    
    return (_i[0]+_i[-1])/2.

def calc_dt(t0,t1):
    
    return t1-t0

def calc_di(_base,_i,_t):
    
    I1 = integrate.simpson(_i,_t)
    
    return np.abs(_base)-np.abs(I1/(_t[-1]-_t[0]))

def calc_dioi(_di,_base):
    
    return _di/(np.abs(_base)-np.abs(_di))

def calc_vel(_dt,_L = 12.*10**-6):
    
    return (_L)/(_dt/1000.)


def find_start(ic,thresh):
    
    start,end = 0,0
    active = False
    ic = np.abs(ic)

    for j in range(len(ic)):
        
        if (ic[j]>thresh) & (not active):
            
            continue
            
        elif (ic[j]<thresh) & (not active):
            
            start = j
            active = True
            
        elif (ic[j] > thresh) & active & (j>start+50):
            
            end = j
            
            return start,end  

    return 0,len(ic)-1

def calc_thresh(ic,sigma=5):

	ic = np.abs(ic)
	
	b_avg = np.mean(np.concatenate([ic[10:20],ic[-21:-10]]))
	b_std = np.std(np.concatenate([ic[10:20],ic[-21:-10]]))
	   
	thresh = b_avg-sigma*b_std

	return thresh

def calc_dioi_pred(d,D,L=12):

    #calculate event amplitude from pore and particle size (in um)
    #Assumes pore is 12um
    s = (1-0.8*((d/D)**3))**(-1)

    di = ((d**3)/(D**2*(L+0.8*D)))*s

    return di
