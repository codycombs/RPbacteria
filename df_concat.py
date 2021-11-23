import pandas as pd
import numpy as np



pore = ['pet409']*2+['pet484']*2+['pet2363']*2
particle = ['control','ecoli']*2+['control','ecoli2']

df_list = []

def merge_dataframes():

	for i in range(len(pore)):

		an_base = 'D://bacteria_data/analysis/'+pore[i] + '/' + particle[i] +'/'
		df = pd.read_pickle(an_base+'/dataframe/df_processed.pkl')

		df_list.append(df)

	df2 = pd.concat(df_list,ignore_index=True)

	df2.to_pickle('D://bacteria_data/analysis/full_df.pkl')

if __name__ == '__main__':
	merge_dataframes()