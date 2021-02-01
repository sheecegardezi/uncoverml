import numpy as np
from sklearn.model_selection import KFold, cross_val_score
from xgboost import XGBRegressor



def get_scoring_funtion_polarity(scoring):
    polarity = {
        "explained_variance": True,
        "max_error": False,
        "neg_mean_absolute_error": False,
        "neg_mean_squared_error": False,
        "neg_root_mean_squared_error": False,
        "neg_mean_squared_log_error": False,
        "neg_median_absolute_error": False,
        "r2": True,
        "neg_mean_poisson_deviance": False,
        "neg_mean_gamma_deviance": False,
        "neg_mean_absolute_percentage_error": False
    }

    return polarity[scoring]

def get_score_without_feature(X, y, features_to_drop, scoring, model,n_splits=3):

    kf = KFold(n_splits=n_splits, shuffle=True, random_state=3)
    cv_scores = cross_val_score(model, X.drop(features_to_drop, axis=1).values, y.values, cv=kf, scoring=scoring, n_jobs=-1)
    mean_score = np.mean(cv_scores)
    return mean_score


def find_least_important_feature(X, y, scoring, model, n_splits):
    is_polarity_positive = get_scoring_funtion_polarity(scoring)
    intermediate_results = {}
    for featureindex, feature_name in enumerate(X.columns):
        score_without_feature = get_score_without_feature(X, y, feature_name, scoring, model, n_splits)
        intermediate_results[feature_name] = score_without_feature
        print("Getting score for: ", feature_name, score_without_feature)

    # calculate the results        
    if is_polarity_positive:
        lowest_feature = None
        lowest_score = -99999
        for feature_name in intermediate_results.keys():
            score_without_feature = intermediate_results[feature_name]
            if score_without_feature >= lowest_score:
                lowest_score = score_without_feature
                lowest_feature = feature_name
            del score_without_feature
    else:
        lowest_feature = None
        lowest_score = 99999
        for feature_name in intermediate_results.keys():
            score_without_feature = intermediate_results[feature_name]
            if score_without_feature <= lowest_score:
                lowest_score = score_without_feature
                lowest_feature = feature_name
            del score_without_feature

    results = {}
    results["lowest_score"] = lowest_score
    results["lowest_feature"] = lowest_feature
    results["intermediate_results"] = intermediate_results
    del intermediate_results
    del lowest_feature
    del lowest_score
    return results


# scoring = 'r2'
# scoring = 'neg_root_mean_squared_error'

def feature_ranking_elimination(X, y, min_features_required, scoring, model, n_splits):
    results = {}
    current_total_feature = X.shape[1]

    count = 1
    results[current_total_feature] = find_least_important_feature(X, y, scoring, model, n_splits)

    current_X = X.drop(results[current_total_feature]["lowest_feature"], axis=1)
    current_total_feature = current_X.shape[1]

    count = count + 1
    while (current_total_feature > min_features_required):
        print("Staring experiment for: ", current_total_feature)
        results[current_total_feature] = find_least_important_feature(current_X, y, scoring, model, n_splits)
        print("Results of ", str(count), " iteration:", results[current_total_feature]["lowest_score"])
        current_X = current_X.drop(results[current_total_feature]["lowest_feature"], axis=1)
        current_total_feature = current_X.shape[1]
        count = count + 1

    return results
