#!/usr/bin/env python
# coding: utf-8

import os, numpy as np
import pandas as pd
from matplotlib import pyplot as plt
homedir = os.getenv('HOME')

datapath = os.path.join(homedir, 'Dokumente','python-apps','tensorflow', 'covid-19', 'covid-test-clinicaldata')

df1 = pd.read_csv(datapath+'/09-22_carbonhealth_and_braidhealth.csv', header=0, sep=',')
df1 = df1[  (df1.covid19_test_results == 'Positive')  ]
df2 = pd.read_csv(datapath+'/10-20_carbonhealth_and_braidhealth.csv', header=0, sep=',')
df2 = df2[  (df2.covid19_test_results == 'Positive')  ]
df3 = pd.read_csv(datapath+'/09-29_carbonhealth_and_braidhealth.csv', header=0, sep=',')
df3 = df3[  (df3.covid19_test_results == 'Positive')  ]
df4 = pd.read_csv(datapath+'/10-06_carbonhealth_and_braidhealth.csv', header=0, sep=',')
df4 = df4[  (df4.covid19_test_results == 'Positive')  ]
df5 = pd.read_csv(datapath+'/10-13_carbonhealth_and_braidhealth.csv', header=0, sep=',')
df5 = df5[  (df5.covid19_test_results == 'Positive')  ]

df1 = pd.concat([df1, df2, df3, df4, df5], ignore_index=True)

df1['maxval'] = df1[['headache', 'cough', 'loss_of_smell', 'loss_of_taste', 'runny_nose'\
,'muscle_sore', 'sore_throat', 'sob', 'diarrhea', 'fatigue']].max(axis=1)
labelsD = {"No symptoms":False, "Has symptoms":True}
df1 = df1[['headache', 'cough', 'loss_of_smell', 'loss_of_taste', 'runny_nose'\
,'muscle_sore', 'sore_throat', 'sob', 'diarrhea', 'fatigue', 'maxval']]
n = len(df1.index)

plt.figure(figsize=(10,5))
ax1 = plt.subplot(111, aspect='equal')
ax1.set_title("Subjects with positive covid-19 test result by symptom status\nN={}".format(n), fontsize='18')
df1.maxval.value_counts().plot(kind='pie', ax=ax1, autopct='%1.0f%%', 
 startangle=90, shadow=False,  legend = False, ylabel='', labels=labelsD, fontsize=14)
plt.figtext(0.1, 0.1, 'Data repository: https://covidclinicaldata.org/, by Carbon Health and Braid Health 2020')
plt.savefig('covid19_testing.png', dpi=None, facecolor='w', edgecolor='w',
        orientation='landscape', format='png')


