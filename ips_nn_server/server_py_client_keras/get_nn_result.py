from __future__ import print_function
from concurrent import futures

import numpy as np
import pandas as pd
import sys
from sklearn.preprocessing import StandardScaler
from keras.models import load_model
from joblib import load

import logging
import grpc
import ips_nn_py_pb2
import ips_nn_py_pb2_grpc

labels_x = np.array([1,2,3,4,5,6,7,8,9,10])
labels_y = np.array([1,2,3,4,5,6,7,8,9,10])
model_name = ""

print("text 1")

model_name_x = 'IPS_nn_X_ext_9bcns_10c_3hl_240n_b400_e600.h5'
sc_name_x = 'IPS_nn_X_ext_9bcns_10c_3hl_240n_b400_e600.bin'
 
model_name_y = 'IPS_nn_Y_ext_9bcns_10c_3hl_240n_b400_e600.h5'
sc_name_y = 'IPS_nn_Y_ext_9bcns_10c_3hl_240n_b400_e600.bin'


model_x = load_model(model_name_x)
sc_x=load(sc_name_x)

model_y = load_model(model_name_y)
sc_y=load(sc_name_y)

result = 1
raw_id = []
rssi_norm = []
real_x = []
real_y = []
devices = []

channel = grpc.insecure_channel('server_nn2db:50052')
stub = ips_nn_py_pb2_grpc.PutterStub(channel)

class Exchanger(ips_nn_py_pb2_grpc.ExchangerServicer):

    def putData2nn(self, request, context):
        rs = [request.rssi[0],request.rssi[1], request.rssi[2], request.rssi[3], request.rssi[4], request.rssi[5], request.rssi[6], request.rssi[7], request.rssi[8]]
        device = request.devserial
        mac_addr = request.addr
        prediction = predict(rs)
        
        response = stub.putData2DB(ips_nn_py_pb2.nn2db(p_frst_x=str(prediction['pr_x_1']), p_frst_y=str(prediction['pr_y_1']), p_scnd_x=str(prediction['pr_x_2']), p_scnd_y=str(prediction['pr_y_2']), devserial=device, addr=mac_addr, rssi=rs))
        print("response ", response)
        return ips_nn_py_pb2.response2client(message='OK')

def predict(rssi):
    #print("prediction: ")
    
    df = pd.DataFrame({'databcn1':rssi[0],'databcn2': rssi[1],'databcn3': rssi[2],'databcn4': rssi[3],'databcn5': rssi[4],'databcn6': rssi[5],'databcn7':rssi[6],'databcn8': rssi[7],'databcn9': rssi[8] }, index=[0])
    V = df.iloc[:, :].values
    V_online_x = sc_x.transform(V)
    V_online_y = sc_y.transform(V)
    predict_x = model_x.predict(V_online_x)
    predict_y = model_y.predict(V_online_y)
    
    max_ind_x = np.argmax(predict_x, axis=1)
    prediction_x = labels_x[max_ind_x].tolist()
    order = predict_x.argsort()
    pr_x_1 = labels_x[order[0][-1]]
    pr_x_2 = labels_x[order[0][-2]]
    
    max_ind_y = np.argmax(predict_y, axis=1);
    prediction_y = labels_y[max_ind_y].tolist()
    order = predict_y.argsort()
    pr_y_1 = labels_y[order[0][-1]];
    pr_y_2 = labels_y[order[0][-2]];
    
    print("prx: ", pr_x_1 )
    print("pry: ", pr_y_1)
    result = {"pr_x_1":pr_x_1, "pr_y_1":pr_y_1, "pr_x_2":pr_x_2, "pr_y_2":pr_y_2}
    
    return(result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ips_nn_py_pb2_grpc.add_ExchangerServicer_to_server(Exchanger(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('python server started')
    
    rs=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    prediction = predict(rs)
    server.wait_for_termination()

if __name__ == '__main__':
    
    logging.basicConfig()
    serve()


# if len(result) != 0:
#     for row in result:
#         raw_id.append(row[0])
#         rssi_norm.append(row[1])
#         real_x.append(row[2])
#         real_y.append(row[3])
#         devices.append(row[4])


