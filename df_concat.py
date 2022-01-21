import pandas as pd
import numpy as np



pore = ['pet2363']*9
run = ['0','0','1','0','0','2','3','4','5']
particle = ['control','ecoli','ecoli','ecoli2'] + ['staph']*5

df_list = []

def merge_dataframes():

	for i in range(len(pore)):

		base = 'D://bacteria_data/pores/'+pore[i] + '/' + particle[i] +'/' + run[i] 
		df = pd.read_pickle(base+'/df/df_processed.pkl')

		df_list.append(df)

	df2 = pd.concat(df_list,ignore_index=True)

	df2.to_pickle('D://bacteria_data/dataframes/full_df.pkl')

if __name__ == '__main__':
	merge_dataframes()