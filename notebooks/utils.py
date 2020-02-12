# drop all columns with less than two different values
import progressbar
from time import sleep
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import cufflinks as cf
# Plotly
import plotly.graph_objs as go
cf.go_offline()
from sklearn.model_selection import cross_val_score, GridSearchCV, RandomizedSearchCV

import time

def dropmissedvalues(df):
    bar = progressbar.ProgressBar(maxval=len(df.columns), \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
    bar.start()
    i=0
    for colname in df.columns:
        if len(df[colname].unique())<2:
            df.drop(colname,axis=1,inplace=True)
            i=i+1
            bar.update(i)
            sleep(0.01)
    bar.finish()
    
    
def split_by(_df,_feature):
    pair=[]
    temp=[]
    temp2=[]
    for index, row in _df.iterrows():
        if(not np.logical_and(row[_feature]>= -43,row[_feature]<=10)):
          temp.append(index)
        elif len(temp)>0:
          temp2.append(temp[0])
          temp2.append(temp[-1])
          pair.append(temp2)
          temp2=[]
          temp=[]
    return pair
    
# split and get features vector
def split_timeSeries(_df,_pair_splits):
  #df_new=pd.DataFrame(columns=_df.loc[_pair_splits[1][0]:_pair_splits[1][1]].mean().index)
  df_new=pd.DataFrame(columns=_df.columns)
  bar = progressbar.ProgressBar(maxval=len(_pair_splits), \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
  bar.start()
  i=0
  for _pair in _pair_splits:
    df_new.loc[i]=_df.loc[_pair[0]:_pair[1]].mean()
    i=i+1
    bar.update(i)
    sleep(0.01)
  bar.finish()
  return df_new
  
# check time series contuinity
def heatmap_tsContinuity(df,month):
  df=df[df.index.month==month]
  list_second_by_day=[]
  list_second_by_day_final=[]
  list_days=pd.DataFrame()
  seconds_by_day=86400
  for day in df.index.day.unique():
    print(day)
    df_temp1=df[df.index.day==day]
    print(df_temp1.index.hour.unique())
    for hours in df_temp1.index.hour.unique():
      df_temp2=df_temp1[df_temp1.index.hour==hours]
      for minutes in df_temp2.index.minute.unique():
        list_second_by_day.append(hours*60*60+minutes*60+df_temp2[df_temp2.index.minute==minutes].index.second.values)
    list_second_by_day = [y for x in list_second_by_day for y in x]
    list_second_by_day_final=np.full(seconds_by_day,np.NaN)
    for i in range(0, len(list_second_by_day)):
      list_second_by_day_final[list_second_by_day[i]]=list_second_by_day[i]
      

    list_days[day]=list_second_by_day_final
    list_second_by_day=[]
    list_second_by_day_final=[]
  return list_days

def plot_learning_curve(estimator, title, X, y, ylim=None, cv=None, n_jobs=1, train_sizes=np.linspace(.1, 1.0, 5)): 
  plt.figure()
  plt.title(title)
  if ylim is not None:
    plt.ylim(*ylim)
  plt.xlabel("Training Samples")
  plt.ylabel("Score")
  train_sizes, train_scores, test_scores = learning_curve( estimator, X, y, cv=cv, n_jobs=n_jobs, train_sizes=train_sizes) 
  train_scores_mean = np.mean(train_scores, axis=1) 
  train_scores_std = np.std(train_scores, axis=1) 
  test_scores_mean = np.mean(test_scores, axis=1) 
  test_scores_std = np.std(test_scores, axis=1) 
  plt.grid()
  plt.fill_between(train_sizes, train_scores_mean - train_scores_std, train_scores_mean + train_scores_std, alpha=0.1, color="r") 
  plt.fill_between(train_sizes, test_scores_mean - test_scores_std, test_scores_mean + test_scores_std, alpha=0.1, color="g") 
  plt.plot(train_sizes, train_scores_mean, 'o-', color="r", label="Training score") 
  plt.plot(train_sizes, test_scores_mean, 'o-', color="g", label="Cross-validation score") 
  plt.legend(loc="best") 
  return plt 
  
  
def search(pipeline, parameters, X_train, y_train, X_test, y_test, optimizer='grid_search', n_iter=None):
    
    start = time.time() 
    #bar = progressbar.ProgressBar(maxval=len(_pair_splits), \
    #widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
    #bar.start()
    if optimizer == 'grid_search':
        grid_obj = GridSearchCV(estimator=pipeline,
                                param_grid=parameters,
                                cv=5,
                                refit=True,
                                return_train_score=False,
                                scoring = 'explained_variance',
                               )
        grid_obj.fit(X_train, y_train,)
    
    elif optimizer == 'random_search':
        grid_obj = RandomizedSearchCV(estimator=pipeline,
                            param_distributions=parameters,
                            cv=5,
                            n_iter=n_iter,
                            refit=True,
                            return_train_score=False,
                            scoring = 'explained_variance',
                            random_state=1)
        grid_obj.fit(X_train, y_train,)
    
    else:
        print('enter search method')
        return

    estimator = grid_obj.best_estimator_
    cvs = cross_val_score(estimator, X_train, y_train, cv=5)
    results = pd.DataFrame(grid_obj.cv_results_)
    
    print("##### Results")
    print("Score best parameters: ", grid_obj.best_score_)
    print("Best parameters: ", grid_obj.best_params_)
    print("Cross-validation Score: ", cvs.mean())
    print("Test Score: ", estimator.score(X_test, y_test))
    print("Time elapsed: ", time.time() - start)
    print("Parameter combinations evaluated: ",results.shape[0])
    
    return results, estimator


