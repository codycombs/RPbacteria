import numpy as np
import pandas as pd
import pyabf
import matplotlib.pyplot as plt
from scipy import integrate 
import os
from rp_calcs import *


# pore = ['pet409']*2 + ['pet484']*2 + ['pet2363']*11 + ['pet2250']*3
# run = ['0','0']+['0','0']+['0','0','1','0','0','2','3','4','5','3'] +['0']*2+['1']+['1']
# date = ['10-28-21']*2+['10-28-21']*2+['11-16-21'] + ['11-30-21']*2 + ['11-18-21'] + ['12-17-21']*5 + ['1-19-22']+['1-25-22']*3+['12-7-21']
# particle = ['control','ecoli']*2+['control','ecoli','ecoli','ecoli2'] + ['staph']*6 + ['ecoli']*2 + ['ecoli2'] + ['control']
csv = pd.read_csv('E://bacteria_data//pores//pore_list.csv')

assert(len(csv.pore)==len(csv.run)==len(csv.date)==len(csv.particle))

def calc(overwrite=False):

	for i,row in csv.iterrows():

		pore = str(row.pore)
		particle = str(row.particle)
		date = str(row.date)
		run = str(row.run)
		
		base_path = 'E://bacteria_data/pores/'+pore + '/' + particle +'/' + date + '/' + run

		
		if overwrite or not os.path.isfile(base_path+'/df/df_processed3.pkl') :

			abf_path = base_path +'/raw/' + os.listdir(base_path+'/raw/')[0]

			print('Processing file: ' + abf_path)

			abf = pyabf.ABF(abf_path)
			abf.setSweep(0)
			ic = abf.sweepY
			v = abf.sweepC
			t = abf.sweepX

			events = pd.read_excel(base_path+'/events/events.xlsx').iloc[:,:2]

			columns = events.columns
			
			events = events.rename({columns[0]:'t0',columns[1]:'t1'},axis=1)

			events = events.dropna()

			events.t0 = np.around(events.t0/1000.,decimals=4)

			events.t1 = np.around(events.t1/1000.,decimals=4)

			print('Num of events: ' + str(len(events)))


			args = []
			i_events = []
			i_events2 = []
			velocity = []
			velocity2 = []
			t_events = []
			t_events2 = []
			baseline = []
			baseline2 = []
			delta_t = []
			delta_t2 = []
			delta_i = []
			delta_i2 = []
			delta_i_i = []
			delta_i_i2 = []
			i_clean = []
			i_clean2 = []

			for j,row in events.iterrows():
			    
			    arg = np.where((t>=row.t0)&(t<=row.t1))[0]
			    time = t[arg]
			    i_raw = ic[arg]
			    
			    ib = calc_base_i(i_raw)
			    dt = calc_dt(row.t0,row.t1)
			    
			    di = calc_di(ib,i_raw,time)
			    dioi = calc_dioi(di,ib)
			    vel = calc_vel(dt)

			    thresh = calc_thresh(i_raw,sigma=5)
			    t0,t1 = find_start(i_raw-ib,thresh)

			    time2 = time[t0:t1]
			    i_raw2 = i_raw[t0:t1]
			    
			    ib2 = calc_base_i(i_raw2)
			    dt2 = calc_dt(time2[0],time2[-1])
			    
			    di2 = calc_di(ib2,i_raw2,time2)
			    dioi2 = calc_dioi(di2,ib2)
			    vel2 = calc_vel(dt2)
			    

			    baseline.append(ib)
			    delta_t.append(dt)
			    delta_i.append(di)
			    delta_i_i.append(dioi)
			    velocity.append(vel)
			    
			    args.append(arg)
			    i_events.append(i_raw)
			    t_events.append(time)
			    i_clean.append(np.abs(i_raw)-np.abs(ib))

			    baseline2.append(ib2)
			    delta_t2.append(dt2)
			    delta_i2.append(di2)
			    delta_i_i2.append(dioi2)
			    velocity2.append(vel2)
			    
			    
			    i_events2.append(i_raw2)
			    t_events2.append(time2)
			    i_clean2.append(np.abs(i_raw2)-np.abs(ib2))




			events['baseline'] = baseline
			events['dt'] = delta_t
			events['di'] = delta_i
			events['di_i'] = delta_i_i
			events['vel'] = velocity

			events['baseline2'] = baseline2
			events['dt2'] = delta_t2
			events['di2'] = delta_i2
			events['di_i2'] = delta_i_i2
			events['vel2'] = velocity2

			events['args'] = args
			events['i'] = i_events
			events['i_clean'] = i_clean
			events['t'] = t_events

			events['i2'] = i_events2
			events['i_clean2'] = i_clean2
			events['t2'] = t_events2

			events['voltage'] = np.median(v)
			events['particle'] = particle
			events['pore'] = pore
			events['run'] = run
			events['date'] = date

			print('Saving...')
			events.to_pickle(base_path+'/df/df_processed3.pkl')
			events.to_csv(base_path+'/csv/calcs3.csv')



		else:
			print('Calculations already exist for ' + base_path)
			continue


if __name__ == '__main__':
	calc()