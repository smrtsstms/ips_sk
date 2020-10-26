import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys
import psycopg2
from datetime import datetime, date, time

from sklearn import preprocessing
lb =preprocessing.LabelBinarizer()

if __name__ == "__main__":
	if len (sys.argv) > 1:
		n = sys.argv[1]
		bs = int(sys.argv[2])
		ep = int(sys.argv[3])
		crd = sys.argv[4]

	else:
		rd = 0;
		print("You setup not all required arguments")
		print("You shoud put name, batch, epochs, coordinate (x or y) of NN")

try:
    con = psycopg2.connect("host='127.0.0.1' dbname='ipsskolkovo' user='ipsrw' password='neuralnet'")   
    cur = con.cursor()
    print(con)
except psycopg2.DatabaseError:
    if con:
        con.rollback()
    # print 'Error %s' % e    
    # sys.exit(1)
if(crd == 'x'):
	dataset = pd.read_csv('dataset_x_ext.csv', sep = ';')
	start_training = True
elif(crd == 'y'):
	dataset = pd.read_csv('dataset_y_ext.csv', sep = ';')
	start_training = True
	print("Y is set")
else:
	start_training = False

if(start_training):
	# Importing the dataset
	dataset_wona = dataset
	X = dataset_wona.iloc[:, 1:10].values/110
	y_c = dataset_wona.iloc[:, 0].values
	l = lb.fit_transform(y_c)

	ctime = datetime.now(tz=None)
	train_name = n
	labels = lb.classes_.tolist()
	binarized_labels = lb.transform(labels).tolist()



	cur.execute("INSERT INTO labels (ctime, train_name, labels, binarized_labels) VALUES (%s, %s, %s, %s)", (ctime, train_name, labels, binarized_labels))
	con.commit()

	# Splitting the dataset into the Training set and Test set
	from sklearn.model_selection import train_test_split
	X_train, X_test, y_train, y_test = train_test_split(X, l, test_size = 0.1, random_state = 0)

	#print(l[0])

	# Feature Scaling
	from sklearn.preprocessing import StandardScaler
	from sklearn.preprocessing import Normalizer

	sc = StandardScaler()
	X_train = sc.fit_transform(X_train)
	X_test = sc.transform(X_test)



	# Importing the Keras libraries and packages
	import keras
	from keras.models import Sequential
	from keras.layers import Dense
	from keras.layers import Dropout
	from keras import initializers

	# Initialising the ANN
	classifier = Sequential()
	classifier.add(Dense(units = 240, kernel_initializer = 'uniform', activation = 'relu', input_dim = 9))
	classifier.add(Dense(units = 240, kernel_initializer = 'uniform', activation = 'relu'))
	#classifier.add(Dense(units = 92, kernel_initializer = 'uniform', activation = 'relu'))
	# classifier.add(Dense(units = 40, kernel_initializer = 'uniform', activation = 'relu'))
	# classifier.add(Dense(units = 40, kernel_initializer = 'uniform', activation = 'relu'))
	classifier.add(Dense(units = 240, kernel_initializer = 'uniform', activation = 'relu'))
	classifier.add(Dense(units = 10, kernel_initializer = 'uniform', activation = 'softmax'))

	# Compiling the ANN
	classifier.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

	print("ANN compiled")
	print("Start fitting ANN")

	nn_file_name = n + ".h5"
	sc_file_name = n + ".bin"

	# Fitting the ANN to the Training set
	classifier.fit(X_train, y_train, batch_size = bs, epochs = ep)

	classifier.save(nn_file_name)
	from sklearn.externals.joblib import dump
	dump(sc, sc_file_name, compress=True)

	print("ANN trained")

	# Predicting the Test set results
	y_pred = classifier.predict(X_test)

	y_train_inverse = lb.inverse_transform(y_train)

	y_test_inverse = lb.inverse_transform(y_test)
	y_pred_ones = np.where(y_pred > 0.45,1,0)
	y_pred_invesrse = lb.inverse_transform(y_pred_ones)
	label_list = lb.classes_

	from sklearn.metrics import multilabel_confusion_matrix
	cm = multilabel_confusion_matrix(y_test_inverse, y_pred_invesrse)

	print(cm)

else:
	print("You shoud put name, batch, epochs, coordinate of NN")


con.close()
