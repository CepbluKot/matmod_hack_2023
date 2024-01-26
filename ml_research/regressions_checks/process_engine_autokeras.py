#!/usr/bin/env python
# coding: utf-8


import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 


import pandas as pd 


x_df = pd.read_csv('/home/oleg/Documents/matmod_challeng/splitted_data/CF34-8E5_0.0_CRUISE')
y_df = pd.read_csv('/home/oleg/Documents/matmod_challeng/y.csv')


y_params = y_df.columns[3:]
merged_df = pd.merge(x_df, y_df, on=["engine_id", "flight_datetime", "flight_phase"])

merged_df = merged_df.dropna(axis=1, how='all')

mergd = []
for val in y_params:
    if val in merged_df:
        mergd.append(val)


for predicted_param in mergd:
    merged_df = pd.merge(x_df, y_df, on=["engine_id", "flight_datetime", "flight_phase"])

    params_to_delete = y_params.drop(predicted_param)
    merged_df = merged_df.drop(params_to_delete, axis=1)


    merged_df = merged_df.dropna(how='all', axis=1)

    to_rm = ['Unnamed: 0', 'engine_id', 'aircraft_id', 'flight_phase', 'engine_position', 'n1_modifier', 'number_blades', 'engine_family', 'engine_type', 'manufacturer', 'aircraft_family', 'aircraft_grp', 'ac_manufacturer', 'aircraft_type', ]

    merged_df = merged_df.drop(to_rm, axis=1)


    merged_df = merged_df.loc[:,merged_df.apply(pd.Series.nunique) != 1]

    # splitting data :\


    columns_w_train_data = merged_df.columns.drop([predicted_param, "flight_datetime"])

    x = merged_df[columns_w_train_data]
    y = merged_df[predicted_param]

    x = x.fillna(0)
    y = y.fillna(0)



    import numpy as np
    import tensorflow as tf
    import autokeras as ak
    from sklearn.model_selection import train_test_split


    x_train, x_test, y_train, y_test  = train_test_split(x, y, test_size = 0.20, shuffle = True)



    # Initialize the structured data regressor.
    reg = ak.StructuredDataRegressor(
        overwrite=True, max_trials=1
    )
    reg.fit(x = x_train, y = y_train, epochs = 5, validation_data=(x_test,y_test))

    test_mae, _ = reg.evaluate(x_test, y_test, verbose=0)
    print('error for ' + predicted_param + ' ' + str(test_mae) )

    # print(predicted_param, res)
