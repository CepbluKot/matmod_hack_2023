#!/usr/bin/env python
# coding: utf-8



import pandas as pd 
import numpy as np
from lightgbm import LGBMRegressor
from sklearn.metrics import r2_score


benchmark_results = pd.DataFrame()


def benchmark_1(the_model):
    print('process', str(the_model), '\n')

    x_df = pd.read_csv('/home/oleg/Documents/matmod_challeng/X.csv')
    y_df = pd.read_csv('/home/oleg/Documents/matmod_challeng/y.csv')


    y_params = y_df.columns[3:]
    merged_df = pd.merge(x_df, y_df, on=["engine_id", "flight_datetime", "flight_phase"])

    merged_df = merged_df.dropna(axis=1, how='all')


    params_to_predict = []
    for val in y_params:
        if val in merged_df:
            params_to_predict.append(val)


    # create row object

    row_data = {}

    for predicted_param in params_to_predict:
        merged_df = pd.merge(x_df, y_df, on=["engine_id", "flight_datetime", "flight_phase"])


        params_to_delete = y_params.drop(predicted_param)
        merged_df = merged_df.drop(params_to_delete, axis=1)


        merged_df = merged_df.dropna(how='all', axis=1)


        to_rm = [ 'engine_id', 'aircraft_id', 'flight_phase', 'engine_position', 'number_blades', 'engine_family', 'engine_type', 'manufacturer', 'aircraft_family', 'aircraft_grp', 'ac_manufacturer', 'aircraft_type', ]

        merged_df = merged_df.drop(to_rm, axis=1)

        merged_df = merged_df.loc[:,merged_df.apply(pd.Series.nunique) != 1]


        # splitting data :\

        if predicted_param in merged_df.columns:
            columns_w_train_data = merged_df.columns.drop([predicted_param, "flight_datetime"])

                
            x = merged_df[columns_w_train_data]
            y = merged_df[predicted_param]

            x = x.fillna(0)
            y = y.fillna(0)


            # edit branchark


            for col in params_to_predict:
                if col not in benchmark_results.columns:
                    benchmark_results[col] = np.nan



            # time 2 test
            
            from sklearn.model_selection import train_test_split


            x_train, x_test, y_train, y_test  = train_test_split(x, y, test_size = 0.20, shuffle = True)


            model = the_model()


            model.fit(x_train, y_train)


            # res = model.score(x_test, y_test)


            res = r2_score(y_test, model.predict(x_test))
        
            # add 2 benchmark data

            row_data[predicted_param] = res


    benchmark_results.loc[str(the_model)]=row_data



def benchmark_2(the_model):
    print('process', the_model, '\n')

    x_df = pd.read_csv('/home/oleg/Documents/matmod_challeng/X.csv')
    y_df = pd.read_csv('/home/oleg/Documents/matmod_challeng/y.csv')


    y_params = y_df.columns[3:]
    merged_df = pd.merge(x_df, y_df, on=["engine_id", "flight_datetime", "flight_phase"])

    merged_df = merged_df.dropna(axis=1, how='all')

    params_to_predict = []

    for val in y_params:
        if val in merged_df:
            params_to_predict.append(val)


    # edit branchark


    for col in params_to_predict:
        if col not in benchmark_results.columns:
            benchmark_results[col] = np.nan


    row_data = {}


    for predicted_param in params_to_predict:
        merged_df = pd.merge(x_df, y_df, on=["engine_id", "flight_datetime", "flight_phase"])


        params_to_delete = y_params.drop(predicted_param)

        merged_df = merged_df.drop(params_to_delete, axis=1)


        merged_df = merged_df.dropna(how='all', axis=1)

        to_rm = [ 'engine_id', 'aircraft_id', 'flight_phase', 'engine_position', 'n1_modifier', 'number_blades', 'engine_family', 'engine_type', 'manufacturer', 'aircraft_family', 'aircraft_grp', 'ac_manufacturer', 'aircraft_type', ]

        merged_df = merged_df.drop(to_rm, axis=1)

        if 'Unnamed: 0' in merged_df.columns:
            merged_df = merged_df.drop(['Unnamed: 0'], axis=1)
        

        merged_df = merged_df.loc[:,merged_df.apply(pd.Series.nunique) != 1]


        # splitting data :\

        if predicted_param in merged_df.columns:
            columns_w_train_data = merged_df.columns.drop([predicted_param, "flight_datetime"])

            x = merged_df[columns_w_train_data]
            y = merged_df[predicted_param]

            x = x.fillna(0)
            y = y.fillna(0)



            # scaling

            from sklearn.preprocessing import StandardScaler

            scaler = StandardScaler()
            x = scaler.fit_transform(x)


            # time 2 test

            from sklearn.model_selection import train_test_split


            x_train, x_test, y_train, y_test  = train_test_split(x, y, test_size = 0.20, shuffle = True)


            modl = the_model()


            modl.fit(x_train, y_train)
            res = modl.score(x_test, y_test)

            row_data[predicted_param] = res


    benchmark_results.loc[str(the_model)]=row_data



def benchmark_3(the_model):
    print('process', the_model, '\n')

    x_df = pd.read_csv('/home/oleg/Documents/matmod_challeng/X.csv')
    y_df = pd.read_csv('/home/oleg/Documents/matmod_challeng/y.csv')


    y_params = y_df.columns[3:]
    merged_df = pd.merge(x_df, y_df, on=["engine_id", "flight_datetime", "flight_phase"])

    merged_df = merged_df.dropna(axis=1, how='all')

    params_to_predict = []

    for val in y_params:
        if val in merged_df:
            params_to_predict.append(val)


    # edit branchark


    for col in params_to_predict:
        if col not in benchmark_results.columns:
            benchmark_results[col] = np.nan


    row_data = {}

    for predicted_param in params_to_predict:
        merged_df = pd.merge(x_df, y_df, on=["engine_id", "flight_datetime", "flight_phase"])

        params_to_delete = y_params.drop(predicted_param)
        merged_df = merged_df.drop(params_to_delete, axis=1)


        merged_df = merged_df.dropna(how='all', axis=1)

        to_rm = [ 'engine_id', 'aircraft_id', 'flight_phase', 'engine_position', 'n1_modifier', 'number_blades', 'engine_family', 'engine_type', 'manufacturer', 'aircraft_family', 'aircraft_grp', 'ac_manufacturer', 'aircraft_type', ]

        merged_df = merged_df.drop(to_rm, axis=1)

        if 'Unnamed: 0' in merged_df.columns:
            merged_df = merged_df.drop(['Unnamed: 0'], axis=1)
        

        merged_df = merged_df.loc[:,merged_df.apply(pd.Series.nunique) != 1]


        # splitting data :\


        columns_w_train_data = merged_df.columns.drop([predicted_param, "flight_datetime"])

        x = merged_df[columns_w_train_data]
        y = merged_df[predicted_param]

        x = x.fillna(0)
        y = y.fillna(0)



        # scaling

        from sklearn.preprocessing import StandardScaler

        scaler = StandardScaler()
        x = scaler.fit_transform(x)


        # time 2 test

        from sklearn.model_selection import train_test_split


        x_train, x_test, y_train, y_test  = train_test_split(x, y, test_size = 0.20, shuffle = True)


        modl = the_model()
        
        res = modl.score(x_test, y_test)

        row_data[predicted_param] = res

    benchmark_results.loc[str(the_model)]=row_data



from sklearn.linear_model import BayesianRidge, Lars, LassoLars, BayesianRidge
from sklearn.linear_model import   Ridge
from sklearn.linear_model import Lasso, LinearRegression, Ridge, ElasticNet
from sklearn.linear_model import SGDRegressor, TweedieRegressor, HuberRegressor, RANSACRegressor, TheilSenRegressor

from sklearn.ensemble import GradientBoostingRegressor, AdaBoostRegressor
from sklearn.ensemble import BaggingRegressor, ExtraTreesRegressor, RandomForestRegressor
from sklearn.ensemble import StackingRegressor, VotingRegressor


modls_1 = [LinearRegression, SGDRegressor, GradientBoostingRegressor ]

for model_to_check in modls_1:
    benchmark_1(model_to_check)


modls_2 = [Ridge,  BayesianRidge, Lars, LassoLars, Lasso, ElasticNet, TweedieRegressor,  
          HuberRegressor, TheilSenRegressor,
          
          AdaBoostRegressor, BaggingRegressor,  ExtraTreesRegressor, RandomForestRegressor, LGBMRegressor]


for model_to_check in modls_2:
    benchmark_2(model_to_check)



benchmark_results.to_csv('benchmark_2.csv')


print('done')
