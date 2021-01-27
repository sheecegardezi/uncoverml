import csv
import statistics 
from pathlib import Path
from pprint import pprint
import pickle
import multiprocessing

import pandas as pd
import numpy as np
import xgboost as xgb

from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.feature_selection import RFECV

from xgboost import XGBRegressor
from matplotlib import pyplot as plt


def get_score_without_feature(X, y, features_to_drop):    
    scoring='r2'
    scoring='neg_root_mean_squared_error'
    model = XGBRegressor(objective='reg:squarederror',tree_method='gpu_hist', gpu_id=0, n_jobs=-1)
    kf = KFold(n_splits=3,shuffle=True, random_state=3)
    cv_scores = cross_val_score(model, X.drop(features_to_drop,axis=1).values, y.values, cv=kf,scoring=scoring, n_jobs=-1)
    mean_score = np.mean(cv_scores)
    return mean_score



def find_least_important_feature(X, y):
        
    intermediate_results = {}
    for featureindex,feature_name in enumerate(X.columns):
        score_without_feature = get_score_without_feature(X, y, feature_name)
        intermediate_results[feature_name] = score_without_feature
        print("Getting score for: ",feature_name,score_without_feature)
           
    # calculate the results        
    lowest_feature = None
    lowest_score = -9999
    for feature_name in intermediate_results.keys():
        score_without_feature = intermediate_results[feature_name]
        if score_without_feature >= lowest_score:
            lowest_score = score_without_feature
            lowest_feature = feature_name
        del score_without_feature
    
    
    results = {}
    results["lowest_score"] = lowest_score
    results["lowest_feature"] = lowest_feature
    results["intermediate_results"] = intermediate_results
    return results

def feature_ranking_elimination(X,y, min_features_required=2):
    
    results = {}
    current_total_feature = X.shape[1]

    count = 1
    print("Using neg_root_mean_squared_error as scoring ")
    print("Staring experiment for: ",X.shape[1]," features")
    results[current_total_feature] = find_least_important_feature(X,y)
    print("Results of ",str(count)," iteration:",results[current_total_feature]["lowest_score"],results[current_total_feature]["lowest_feature"])

    current_X = X.drop(results[current_total_feature]["lowest_feature"],axis=1)   
    current_total_feature = current_X.shape[1]

    count = 2
    while(current_total_feature>min_features_required):
        print("Staring experiment for: ",current_total_feature)
        results[current_total_feature] = find_least_important_feature(current_X,y)
        print("Results of ",str(count)," iteration:",results[current_total_feature]["lowest_score"] )
        current_X = current_X.drop(results[current_total_feature]["lowest_feature"],axis=1)
        current_total_feature = current_X.shape[1]
        count = count + 1
    
    
    return results
    