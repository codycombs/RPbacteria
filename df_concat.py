import pandas as pd
import numpy as np



# pore = ['pet409']*2 + ['pet484']*2 + ['pet2363']*11 + ['pet2250']*3
# run = ['0','0']+['0','0']+['0','0','1','0','0','2','3','4','5','3'] +['0']*2+['1']+['1']
# date = ['10-28-21']*2+['10-28-21']*2+['11-16-21'] + ['11-30-21']*2 + ['11-18-21'] + ['12-17-21']*5 + ['1-19-22']+['1-25-22']*3+['12-7-21']
# particle = ['control','ecoli']*2+['control','ecoli','ecoli','ecoli2'] + ['staph']*6 + ['ecoli']*2 + ['ecoli2'] + ['control']

csv = pd.read_csv('E://bacteria_data//pores//pore_list.csv')

assert(len(csv.pore)==len(csv.run)==len(csv.date)==len(csv.particle))

df_list = []

def merge_dataframes():

	for i,row in csv.iterrows():

		pore = str(row.pore)
		particle = str(row.particle)
		date = str(row.date)
		run = str(row.run)

		base = 'E://bacteria_data/pores/'+pore + '/' + particle +'/' + date + '/' + run 
		df = pd.read_pickle(base+'/df/df_processed3.pkl')

		df_list.append(df)

	df2 = pd.concat(df_list,ignore_index=True)

	print(len(df2))
	df2.to_pickle('E://bacteria_data/dataframes/full_df3.pkl')

if __name__ == '__main__':
	merge_dataframes()