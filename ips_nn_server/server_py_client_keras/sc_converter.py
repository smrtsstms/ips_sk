import numpy as np
import pandas as pd
import sys
from sklearn.preprocessing import StandardScaler
from keras.models import load_model
from sklearn.externals.joblib import load

#import matplotlib.pyplot as plt
#import psycopg2
#from datetime import datetime, date, time
#from sklearn import preprocessing
#lb =preprocessing.LabelBinarizer()

labels_x = np.array([1,2,3,4,5,6,7,8,9,10])
labels_y = np.array([1,2,3,4,5,6,7,8,9,10])
model_name = ""

print("text 1")

#model_name_x = 'IPS_nn_X_ext_9bcns_10c_3hl_240n_b400_e600.h5'
sc_name_x = 'IPS_nn_X_ext.bin'
sc_name_x_sm = 'IPS_nn_X_sm.bin'
 
#model_name_y = 'IPS_nn_Y_ext_9bcns_10c_3hl_240n_b400_e600.h5'
sc_name_y = 'IPS_nn_Y_ext.bin'
sc_name_y_sm = 'IPS_nn_Y_sm.bin'


#model_x = load_model(model_name_x)
sc_x=load(sc_name_x)
sc_x_sm=load(sc_name_x_sm)

#model_y = load_model(model_name_y)
sc_y=load(sc_name_y)
sc_y_sm=load(sc_name_y_sm)

from sklearn.externals.joblib import dump
dump(sc_x, 'IPS_nn_X_ext_p2.bin', compress=True, protocol=2)
dump(sc_y, 'IPS_nn_Y_ext_p2.bin', compress=True, protocol=2)
dump(sc_x_sm, 'IPS_nn_X_sm_p2.bin', compress=True, protocol=2)
dump(sc_y_sm, 'IPS_nn_Y_sm_p2.bin', compress=True, protocol=2)

# if len(result) != 0:
#     for row in result:
#         raw_id.append(row[0])
#         rssi_norm.append(row[1])
#         real_x.append(row[2])
#         real_y.append(row[3])
#         devices.append(row[4])

# df = pd.DataFrame({ 
#                     'databcn1': [data[0]],
#                     'databcn2': [data[1]],
#                     'databcn3': [data[2]],
#                     'databcn4': [data[3]],
#                     'databcn5': [data[4]],
#                     'databcn6': [data[5]],
#                     'databcn7': [data[6]],
#                     'databcn8': [data[7]],
#                     'databcn9': [data[8]] }).astype('float')

# V = df.iloc[:, :].values

# V_online = sc.transform(V)

# predict_x = model_x.predict(V_online)
# predict_y = model_y.predict(V_online)
# #new_y_pred_ones = np.where(predict > 0.4,1,0)

# max_ind_x = np.argmax(predic_x, axis=1);
# prediction_x = labels_x[max_ind_x].tolist()

# order = predict_x.argsort()
# pr_x_1 = labels_x[order[0][-1]];
# pr_x_2 = labels_x[order[0][-2]];

# max_ind_y = np.argmax(predic_y, axis=1);
# prediction_y = labels_y[max_ind_y].tolist()

# order = predict_y.argsort()
# pr_y_1 = labels_y[order[0][-1]];
# pr_y_2 = labels_y[order[0][-2]];


