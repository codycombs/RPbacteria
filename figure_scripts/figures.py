import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def event_plots(df):

	fig, (ax1,ax2,ax3) = plt.subplots(1,3,figsize=(11,3))
	i = 35
	df_staph = df[(df.particle=='staph')&(df.date=='12-17-21')].reset_index()
	event = df_staph.iloc[i]
	t = event.t*1000
	i = event.i_clean[::-1]

	ax1.plot(t-t[0],i)

	ax1.set_ylabel('Current (nA)',size=16)

	ax1.tick_params(axis='both', which='major', labelsize=12)
	ax1.set_xlabel('Time (ms)', size = 16)

	i = 90
	df_ecoli = df[(df.particle=='ecoli')&(df.run=='0')]
	event = df_ecoli.iloc[i]
	t = event.t*1000
	i = event.i_clean[::-1]


	ax2.plot(t-t[0],i)

	ax2.set_ylabel('Current (nA)',size=16)

	ax2.tick_params(axis='both', which='major', labelsize=12)
	ax2.set_xlabel('Time (ms)', size = 16)

	df_ecoli2 = df[(df.particle=='ecoli2')&(df.run=='0')]
	i = 35
	event = df_ecoli2.iloc[i]
	t = event.t*1000
	i = event.i_clean[::-1]


	ax3.plot(t-t[0],i)

	ax3.set_ylabel('Current (nA)',size=16)

	ax3.tick_params(axis='both', which='major', labelsize=12)
	ax3.set_xlabel('Time (ms)', size = 16)
	plt.tight_layout()

	plt.savefig('D:/bacteria_data/plots/events/event_comparison',dpi=300)

def staph_event_plots(df):

	df_staph = df[(df.particle=='staph')&(df.date=='12-17-21')].reset_index()
	i = 35
	event = df_staph.iloc[i]
	t = event.t*1000
	i = event.i_clean[::-1]

	fig, (ax1,ax2) = plt.subplots(2, 1,figsize=(5,6))

	ax1.plot(t-t[0],i)

	ax1.set_ylabel('Current (nA)',size=16)

	ax1.tick_params(axis='both', which='major', labelsize=12)


	i = 48
	event = df_staph.iloc[i]
	t = event.t*1000
	i = event.i_clean [::-1]

	ax2.plot(t-t[0],i)
	ax2.set_xlabel('Time (ms)', size = 16)

	ax2.set_ylabel('Current (nA)',size=16)
	ax2.tick_params(axis='both', which='major', labelsize=12)

	plt.tight_layout()
	plt.savefig('D:/bacteria_data/plots/events/staph_event',dpi=300)

def ecoli_event_plots(df):

	i = 127
	event = df_ecoli.iloc[i]
	t = event.t*1000
	i = event.i_clean[::-1]

	fig, (ax1,ax2) = plt.subplots(2, 1,figsize=(5,6))

	ax1.plot(t-t[0],i)

	ax1.set_ylabel('Current (nA)',size=16)

	ax1.tick_params(axis='both', which='major', labelsize=12)


	i = 90
	event = df_ecoli.iloc[i]
	t = event.t*1000
	i = event.i_clean [::-1]

	ax2.plot(t-t[0],i)
	ax2.set_xlabel('Time (ms)', size = 16)

	ax2.set_ylabel('Current (nA)',size=16)
	ax2.tick_params(axis='both', which='major', labelsize=12)

	plt.tight_layout()
	plt.savefig('D:/bacteria_data/plots/events/ecoli_event',dpi=300)

def ecoli2_event_plots(df):

	df_ecoli2 = df[(df.particle=='ecoli2')&(df.run=='0')]
	i = 25
	event = df_ecoli2.iloc[i]
	t = event.t*1000
	i = event.i_clean[::-1]

	fig, (ax1,ax2) = plt.subplots(2, 1,figsize=(5,6))

	ax1.plot(t-t[0],i)

	ax1.set_ylabel('Current (nA)',size=16)

	ax1.tick_params(axis='both', which='major', labelsize=12)


	i = 35
	event = df_ecoli2.iloc[i]
	t = event.t*1000
	i = event.i_clean [::-1]

	ax2.plot(t-t[0],i)
	ax2.set_xlabel('Time (ms)', size = 16)

	ax2.set_ylabel('Current (nA)',size=16)
	ax2.tick_params(axis='both', which='major', labelsize=12)

	plt.tight_layout()
	plt.savefig('D:/bacteria_data/plots/events/ecoli2_event',dpi=300)

def control_event_plots(df):

	df_control = df[(df.particle=='control')]

	i = 127
	event = df_control.iloc[i]
	t = event.t*1000
	i = event.i_clean

	fig, (ax1,ax2) = plt.subplots(2, 1,figsize=(5,6))

	ax1.plot(t-t[0],i)

	ax1.set_ylabel('Current (nA)',size=16)

	ax1.tick_params(axis='both', which='major', labelsize=12)


	i = 91
	event = df_control.iloc[i]
	t = event.t*1000
	i = event.i_clean

	ax2.plot(t-t[0],i)
	ax2.set_xlabel('Time (ms)', size = 16)

	ax2.set_ylabel('Current (nA)',size=16)
	ax2.tick_params(axis='both', which='major', labelsize=12)

	plt.tight_layout()
	plt.savefig('D:/bacteria_data/plots/events/control_event',dpi=300)


def scatter_full(df):

	temp_df = df[(df.pore=='pet2363')&(df.particle=='control')]

	plt.scatter(temp_df.dt*1000,temp_df.di_i)

	temp_df = df[(df.pore=='pet2363')&(df.particle=='ecoli')&(df.run=='0')]

	plt.scatter(temp_df.dt*1000,temp_df.di_i)

	temp_df = df[(df.pore=='pet2363')&(df.particle=='ecoli2')]

	plt.scatter(temp_df.dt*1000,temp_df.di_i)

	temp_df = df[(df.pore=='pet2363')&(df.particle=='staph')&(df.date=='12-17-21')]

	plt.scatter(temp_df.dt*1000,temp_df.di_i)

	plt.legend(['400nm_poly','E. Coli.','Elongated E. Coli','Staph.'])
	plt.xlabel('Event Time (ms)',size=16)
	plt.ylabel('$\Delta$I/I',size=16)
	plt.xticks(size=14)
	plt.yticks(size=14)
	#plt.title('Pore radius = 2363 nm')
	plt.tight_layout()
	plt.savefig('D://bacteria_data//plots/scatter/scatter_2363_poly_ecoli12_staph.png',dpi=300)

def scatter_zoom(df):

	temp_df = df[(df.pore=='pet2363')&(df.particle=='control')]

	plt.scatter(temp_df.dt*1000,temp_df.di_i)

	temp_df = df[(df.pore=='pet2363')&(df.particle=='ecoli')&(df.run=='0')]

	plt.scatter(temp_df.dt*1000,temp_df.di_i)

	#temp_df = df[(df.pore=='pet2363')&(df.particle=='ecoli2')]

	#plt.scatter(temp_df.dt,temp_df.di_i)

	temp_df = df[(df.pore=='pet2363')&(df.particle=='staph')&(df.date=='12-17-21')]

	plt.scatter(temp_df.dt*1000,temp_df.di_i,color='#d62728')

	plt.legend(['400nm_poly','E. Coli.','Staph.'])
	plt.xlabel('Event Time (ms)',size=16)
	plt.ylabel('$\Delta$I/I',size=16)
	plt.xticks(size=14)
	plt.yticks(size=14)
	#plt.title('Pore radius = 2363 nm')
	plt.tight_layout()
	plt.savefig('D://bacteria_data//plots/scatter/scatter_2363_poly_ecoli_staph.png',dpi=300)


def bar_full(df,feat='di_i'):

	temp_df = df[(df.particle=='control')]
	poly_mean = temp_df[feat].mean()
	poly_std = temp_df[feat].std()

	temp_df = df[(df.run=='0')&(df.particle=='ecoli')]
	ecoli_mean = temp_df[feat].mean()
	ecoli_std = temp_df[feat].std()

	temp_df = df[(df.particle=='ecoli2')]
	ecoli2_mean = temp_df[feat].mean()
	ecoli2_std = temp_df[feat].std()

	temp_df = df[(df.particle=='staph')]
	staph_mean = temp_df[feat].mean()
	staph_std = temp_df[feat].std()

	x = np.arange(4)

	plt.bar(x,[poly_mean,ecoli_mean,ecoli2_mean,staph_mean],yerr=[poly_std,ecoli_std,ecoli2_std,staph_std],capsize=10)

	plt.xticks(x,('Polystyrene','E. Coli.','E. Coli. 2','Staph'),size=14,rotation=0)
	plt.tick_params(axis='both', which='major', labelsize=14)

	plt.ylabel('$\Delta$I/I',size=16)

	plt.title('Pore Radius = 2.36 $\mu m$')

	plt.tight_layout()
	plt.savefig('D://bacteria_data/plots/bar/di/bar_2363_di_full.png',dpi=300)

def di_comparison(df):

	dfm = pd.read_pickle('D://bacteria_data//microscope_images//df//dfm')

	fig, (ax1, ax2,ax3) = plt.subplots(1, 3,figsize=(12,6))

	sns.kdeplot(x=df[(df.run=='0')&(df.particle=='ecoli')].di_i,fill=True,label='Measured',ax=ax1)
	sns.kdeplot(x=dfm[dfm.particle=='ecoli'].di_i,fill=True,label = 'Predicted',ax=ax1)
	ax1.set_xlabel('')
	ax1.legend()

	sns.kdeplot(x=df[(df.particle=='ecoli2')].di_i,fill=True,label='Measured',ax=ax2)
	sns.kdeplot(x=dfm[dfm.particle=='ecoli2'].di_i,fill=True,label = 'Predicted',ax=ax2)

	ax2.legend()

	sns.kdeplot(x=df[(df.particle=='staph')&(df.date=='12-17-21')].di_i,fill=True,label='Measured',ax=ax3)
	sns.kdeplot(x=dfm[dfm.particle=='staph'].di_i,fill=True,label = 'Predicted',ax=ax3)

	ax3.legend()

	ax1.set_xlabel(r'$\frac{\Delta I}{I_p}$',size=18)
	ax2.set_xlabel(r'$\frac{\Delta I}{I_p}$',size=18)
	ax3.set_xlabel(r'$\frac{\Delta I}{I_p}$',size=18)

	ax1.yaxis.label.set_size(16)
	ax2.set_ylabel(r'',size=16)
	ax3.set_ylabel(r'',size=16)

	ax1.tick_params(axis='both', which='major', labelsize=12)
	ax2.tick_params(axis='both', which='major', labelsize=12)
	ax3.tick_params(axis='both', which='major', labelsize=12)

	plt.tight_layout()
	plt.savefig('D://bacteria_data//plots//kde//kde_comp.png',dpi=300)

