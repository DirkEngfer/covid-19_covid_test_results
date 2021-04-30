#!/usr/bin/env python
# coding: utf-8

import os, numpy as np
import pandas as pd
homedir = os.getenv('HOME')

datapath = os.path.join(homedir, 'Dokumente','python-apps','tensorflow', 'covid-19', 'India_covid-testing')
datafile = 'owid-covid-data.csv'

indatapath = os.path.join(datapath,datafile)


df = pd.read_csv(indatapath, header=0, sep=',',usecols=[2,3,31], names=['location', 'date', 'positive_rate'], dtype={'date': "string", 'positive_rate': np.float64})
df2 = df[   (df.location.isin (['India', 'Germany'])) & ~(df.positive_rate.isin([np.nan]))  ].copy()# copy to avoid settingwithcopyWarning

#print(df2.head())
df2['dt'] = pd.to_datetime(df2.date, format='%Y-%m-%d')
df2.sort_values(by=['location', 'dt'], ascending=[True, True], inplace=True, axis=0)
df_ind = df2[(df2.location == 'India')]
df_ger = df2[(df2.location == 'Germany')]

from matplotlib import pyplot as plt
fig, ax = plt.subplots(figsize=[10,7])
ax.plot(df_ind['dt'], df_ind['positive_rate'], label='India', color='red')
ax.plot(df_ger['dt'], df_ger['positive_rate'], label='Germany', color='blue')

#ax.set_xlim(1960, 2018)
ax.tick_params(labelsize=10)

ax.set_title('COVID-19 testing', fontsize='24')
ax.legend(loc=3, prop={'size': 12})
ax.grid(True)
#t = "xxx"
#ax.text('2020-05', 0.2, t, fontsize=12)

plt.xlabel('Time', fontsize='large')
plt.ylabel('Rate of positive test results', fontsize='large')
plt.figtext(0.01, 0.01, 'Data repository: Hasell, J., Mathieu, E., Beltekian, D. et al. A cross-country database of COVID-19 testing. Sci Data 7, 345 (2020)')
#fig.autofmt_xdate(rotation=30)
plt.savefig('covid19_test_results.png', dpi=None, facecolor='w', edgecolor='w',
        orientation='landscape', format='png')


