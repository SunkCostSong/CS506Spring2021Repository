# -*- coding: utf-8 -*-
"""data_processing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18Enl37WUrzT7PFp0nMSPfwtgmpxcn2t8
"""

from google.colab import drive
drive.mount('/content/drive')

"""# CS506 - Team 1 Project """

import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt # we can also use seaborn for prettier graphs or bokeh for interactive graphs 
import statistics as stat

"""# Data preprocessing"""

DATASET_PATH = 'Blake_RPD_Dataset_NonTwin.xlsx'
df = pd.read_excel(DATASET_PATH, "data") # data is the sheet name
df

# gender: male = 0. female = 1
# location: remote = 0. in classrom = 1
# cooperation = 0. defection = 1

# tfti = Decision made in ith round when facing Tit for Tat Partner.
# TFT partner cooperates on the 1st round and then repeats the child's decision in following rounds

# coopi = Decision made in ith round when facing cooperative Partner.
# Coop partner cooperates on all rounds BUT defects on rounds 3 & 7

# defi = Decision made in ith round when facing the defective partner.
# Def partner defects on all rounds BUT cooperates on rounds 3 & 7.

# Here, I generate list of column names for easy access:

tft = ['tft' + str(i) for i in range(1,11)]
tft_rt = ['tft_rt' + str(i) for i in range(1,11)]
coop = ['coop' + str(i) for i in range(1,11)]
coop_rt = ['coop_rt' + str(i) for i in range(1,11)]
defs = ['def' + str(i) for i in range(1,11)]
def_rt = ['def_rt' + str(i) for i in range(1,11)]

features = [tft, tft_rt, coop, coop_rt, defs, def_rt]

# Now you can simply call the data frame + feature name. Try it!
df[tft]

#Dropping rows with NaN values:

dropped_len = df.shape[0] - df.dropna().shape[0] 
data = df.dropna() #Now, we have a clean data frame. 

print('Number of datapoints dropped:', dropped_len)

# Calculating averages - feel free to manipulate 
# these dataframes however way you see fit
df['tft_avg'] = df[tft].mean(axis=1)
df['tft_rt_avg'] = df[tft_rt].mean(axis=1)
df['coop_avg'] = df[coop].mean(axis=1)
df['coop_rt_avg'] = df[coop_rt].mean(axis=1)
df['def_avg'] = df[defs].mean(axis=1)
df['def_rt_avg'] = df[def_rt].mean(axis=1)

avgs = ['tft_avg','tft_rt_avg','coop_avg','coop_rt_avg','def_avg','def_rt_avg']
df[avgs]

# a row of column means
col_means = df.mean()
col_means

# Whether children are naturally cooperative/defiant as their parents reported
def scatter_plt(x,y,xlabel,ylabel,title):
  plt.scatter(x,y)
  plt.xlabel(xlabel)
  plt.ylabel(ylabel)
  plt.title(title)
  plt.show()
  plt.close()

proactive_aggr = list(df['P-Proactive_aggr'])
reactive_aggr = list(df['P-Reactive_aggr'])
tft_avg = list(df['tft_avg'])
coop_avg = list(df['coop_avg'])
def_avg = list(df['def_avg'])
scatter_plt(proactive_aggr,tft_avg,'reported aggr','avg decision','Average Decision vs Proactive Aggr Score When Playing Against TFT Partner')
scatter_plt(proactive_aggr,coop_avg,'reported aggr','avg decision','Average Decision vs Proactive Aggr Score When Playing Against Coop Partner')
scatter_plt(proactive_aggr,def_avg,'reported aggr','avg decision','Average Decision vs Proactive Aggr Score When Playing Against Def Partner')
scatter_plt(reactive_aggr,tft_avg,'reported aggr','avg decision','Average Decision vs Reactive Aggr Score When Playing Against TFT Partner')
scatter_plt(reactive_aggr,coop_avg,'reported aggr','avg decision','Average Decision vs Reactive Aggr Score When Playing Against Coop Partner')
scatter_plt(reactive_aggr,def_avg,'reported aggr','avg decision','Average Decision vs Reactive Aggr Score When Playing Against Def Partner')

def Aggr_DecAvg_Plot(reported_aggr,dec_avg,title):
  l = [(0,0)] * 20
  for child in range(len(reported_aggr)):
    if reported_aggr[child] != reported_aggr[child]:
      continue
    i = int(reported_aggr[child])
    sum_dec,count = l[i]
    sum_dec += dec_avg[child]
    count += 1
    l[i] = (sum_dec,count)
  aggr_dec_avg = []
  for i in range(len(l)):
    sum_dec,count = l[i]
    if count == 0:
      break;
    aggr_dec_avg.append(sum_dec/count)
  aggr_scores = range(len(aggr_dec_avg))
  plt.plot(aggr_scores,aggr_dec_avg)
  plt.xlabel('Aggr Score')
  plt.ylabel('Avg Decision')
  plt.title(title)
  plt.show()
  plt.close

Aggr_DecAvg_Plot(proactive_aggr,tft_avg,'Reported Proactive Aggr Score vs Average Decision of All Children against TFT Partner')
Aggr_DecAvg_Plot(proactive_aggr,coop_avg,'Reported Proactive Aggr Score vs Average Decision of All Children against Coop Partner')
Aggr_DecAvg_Plot(proactive_aggr,def_avg,'Reported Proactive Aggr Score vs Average Decision of All Children against Def Partner')
Aggr_DecAvg_Plot(reactive_aggr,tft_avg,'Reported Reactive Aggr Score vs Average Decision of All Children against TFT Partner')
Aggr_DecAvg_Plot(reactive_aggr,coop_avg,'Reported Reactive Aggr Score vs Average Decision of All Children against Coop Partner')
Aggr_DecAvg_Plot(reactive_aggr,def_avg,'Reported Reactive Aggr Score vs Average Decision of All Children against Def Partner')

# Change in children after deviation
plt.figure(num=None,figsize=(7, 5))
plt.xlabel('Trial Number', fontsize=14)
plt.ylabel('Average Response', fontsize=14)
y = [df['coop' + str(x)].mean() for x in range(3,6)]
plt.plot([3,4,5],y,color='blue',linewidth=2,label="Cooperative")
y = [df['coop' + str(x)].mean() for x in range(7,10)]
plt.plot([7,8,9],y,color='blue',linewidth=2)
y = [df['def' + str(x)].mean() for x in range(3,6)]
plt.plot([3,4,5],y,color='red',linewidth=2,label="Defiant")
y = [df['def' + str(x)].mean() for x in range(7,10)]
plt.plot([7,8,9],y,color='red',linewidth=2)
plt.legend()
plt.title('Average Responses After Deviation in Opponent')
plt.show()

# Change in children with more reactive aggression after deviation
plt.figure(num=None,figsize=(7, 5))
plt.xlabel('Trial Number', fontsize=14)
plt.ylabel('Average Response', fontsize=14)
y = []
helper = []
helper_mean = 0
for i in df['P-Reactive_aggr'].iteritems():
  if i[1] >= 3:
    helper.append(i[0])
for x in range(3,6):
  values = df['coop' + str(x)].values
  for i in helper:
    helper_mean += values[i]
  y.append(helper_mean/len(helper))
  helper_mean = 0
plt.plot([3,4,5],y,color='blue',linewidth=2,label="Cooperative")
y = []
for x in range(7,10):
  values = df['coop' + str(x)].values
  for i in helper:
    helper_mean += values[i]
  y.append(helper_mean/len(helper))
  helper_mean = 0
plt.plot([7,8,9],y,color='blue',linewidth=2)
y = []
for x in range(3,6):
  values = df['def' + str(x)].values
  for i in helper:
    helper_mean += values[i]
  y.append(helper_mean/len(helper))
  helper_mean = 0
plt.plot([3,4,5],y,color='red',linewidth=2,label="Defiant")
y = []
for x in range(7,10):
  values = df['def' + str(x)].values
  for i in helper:
    helper_mean += values[i]
  y.append(helper_mean/len(helper))
  helper_mean = 0
plt.plot([7,8,9],y,color='red',linewidth=2)
plt.legend()
plt.title('Average Responses for Children with More Reactive Aggression After Deviation in Opponent')
plt.show()

# Change in children with more proactive aggression after deviation
plt.figure(num=None,figsize=(7, 5))
plt.xlabel('Trial Number', fontsize=14)
plt.ylabel('Average Response', fontsize=14)
y = []
helper = []
helper_mean = 0
for i in df['P-Proactive_aggr'].iteritems():
  if i[1] >= 1:
    helper.append(i[0])
for x in range(3,6):
  values = df['coop' + str(x)].values
  for i in helper:
    helper_mean += values[i]
  y.append(helper_mean/len(helper))
  helper_mean = 0
plt.plot([3,4,5],y,color='blue',linewidth=2,label="Cooperative")
y = []
for x in range(7,10):
  values = df['coop' + str(x)].values
  for i in helper:
    helper_mean += values[i]
  y.append(helper_mean/len(helper))
  helper_mean = 0
plt.plot([7,8,9],y,color='blue',linewidth=2)
y = []
for x in range(3,6):
  values = df['def' + str(x)].values
  for i in helper:
    helper_mean += values[i]
  y.append(helper_mean/len(helper))
  helper_mean = 0
plt.plot([3,4,5],y,color='red',linewidth=2,label="Defiant")
y = []
for x in range(7,10):
  values = df['def' + str(x)].values
  for i in helper:
    helper_mean += values[i]
  y.append(helper_mean/len(helper))
  helper_mean = 0
plt.plot([7,8,9],y,color='red',linewidth=2)
plt.legend()
plt.title('Average Responses for Children with More Proactive Aggression After Deviation in Opponent')
plt.show()

# Change in children with more total aggression after deviation
plt.figure(num=None,figsize=(7, 5))
plt.xlabel('Trial Number', fontsize=14)
plt.ylabel('Average Response', fontsize=14)
y = []
helper = []
helper_mean = 0
for i in df['P-Aggression_Total'].iteritems():
  if i[1] >= 4:
    helper.append(i[0])
for x in range(3,6):
  values = df['coop' + str(x)].values
  for i in helper:
    helper_mean += values[i]
  y.append(helper_mean/len(helper))
  helper_mean = 0
plt.plot([3,4,5],y,color='blue',linewidth=2,label="Cooperative")
y = []
for x in range(7,10):
  values = df['coop' + str(x)].values
  for i in helper:
    helper_mean += values[i]
  y.append(helper_mean/len(helper))
  helper_mean = 0
plt.plot([7,8,9],y,color='blue',linewidth=2)
y = []
for x in range(3,6):
  values = df['def' + str(x)].values
  for i in helper:
    helper_mean += values[i]
  y.append(helper_mean/len(helper))
  helper_mean = 0
plt.plot([3,4,5],y,color='red',linewidth=2,label="Defiant")
y = []
for x in range(7,10):
  values = df['def' + str(x)].values
  for i in helper:
    helper_mean += values[i]
  y.append(helper_mean/len(helper))
  helper_mean = 0
plt.plot([7,8,9],y,color='red',linewidth=2)
plt.legend()
plt.title('Average Responses for Children with More Total Aggression After Deviation in Opponent')
plt.show()

#Takes processed dataframe and isolates reaction times and game choices for a single participant at a specific index point.
def isolate_participant(df, patient_index): 
  patient_df=df.iloc[patient_index]
  return patient_df[tft], patient_df[tft_rt]
[actions, reaction_times]=isolate_participant(df, 0)

#Determines state based on differences in reaction times from a starting point. The eval point is used to determine the participant's state after a given round. 
def determine_state(reaction_times, actions, eval_point):
    defect_times=[]
    defect_rounds=[]
    cooperate_times=[]
    cooperate_rounds=[]
    #At the moment, there is no consideration for a "balanced state" where reaction times for cooperation and defection are roughly equal. 
    #Discussion about what constitutes distinctively different reaction times to come.
    for i, (action, time) in enumerate(zip(actions, reaction_times)):
      if i >= eval_point:
        if action == 1:
          defect_times.append(time)
          defect_rounds.append(i)
        if action ==0:
          cooperate_times.append(time)
          cooperate_rounds.append(i)
    assert len(cooperate_rounds)>0, "Data must contain at least one cooperative round"
    assert len(defect_rounds)>0, "Data must contain at least one uncooperative round" 
    print('Cooperative reaction times: ', cooperate_times)
    print('Defection reaction times: ', defect_times)
    plt.scatter(defect_rounds, defect_times, c = 'red', label='defection')
    plt.scatter(cooperate_rounds, cooperate_times, c = 'blue', label='cooperation')
    plt.title("Reaction Times for Each Round")
    plt.xlabel('Round Number')
    plt.ylabel('Reaction Time (seconds)')
    plt.legend()
    plt.show()
    if stat.mean(defect_times) > stat.mean(cooperate_times):
      return 'cooperative'
    if stat.mean(cooperate_times) > stat.mean(defect_times):
      return 'uncooperative'
    else:
      return 'Could not determine state'

print(determine_state(reaction_times, actions, 0))

"""
A preliminary determination of a participant’s state was constructed using the difference in reaction times between cooperation and defection choices in subsequent rounds. 
In addition to raw cooperation and defection data, this model will be useful in investigating the long-term change in a participant’s preference over many rounds. 
The preliminary model assesses relative reaction times after a round specified by the user. In the future, this function will take into account the overall trends in reaction time. 
Additionally, the model does not account for roughly equal cooperative and uncooperative reaction times. 
What constitutes roughly equal reaction times will need to be discussed with Peter. There seems to be significant differences between cooperative and uncooperative reaction times for many participants. 
A formal drift diffusion model will eventually be required for a rigorous analysis of the primary research questions covered in this project. 

"""