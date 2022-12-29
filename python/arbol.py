# Se importa la librería scikit-learn y la librería numpy
import pandas as pd
#training = pd.read_csv("titanic-train.csv")
training = pd.read_csv("sample_data/autismo.csv")
# training.info()
# training.head(5)

training["Class/ASD"] = training["Class/ASD"].apply(lambda toLabel: 0 if toLabel == 'NO' else 1)

#almacena los valores de la columna "Survived" en una variable llamada "y_target".
y_target = training["Class/ASD"].values

columns = ["A1_Score","A2_Score","A3_Score","A4_Score","A5_Score","A6_Score","A7_Score","A8_Score","A9_Score","A10_Score"]
x_input = training[list(columns)].values
# print(x_input)

from sklearn import tree

#create mirabol as a decision tree classifier object
mirabol = tree.DecisionTreeClassifier(criterion="entropy")

#train the model using the fit() method of the decision tree object. 
#Supply the method with the input variable X_input and the target variable y_target
mirabol = mirabol.fit(x_input, y_target)
mirabol.score(x_input,y_target)

import six
#from sklearn.externals.six import StringIO
with open("titanic.dot", 'w') as f:
  f = tree.export_graphviz(mirabol, out_file=f, feature_names=columns)

# !dot -Tpng ./titanic.dot -o ./titanic.png

from IPython.display import Image
#display the decison tree graphic
Image("titanic.png")

import numpy as np
y_target_predecido = mirabol.predict(x_input)
acc = np.sum(y_target==y_target_predecido)/float(len(y_target_predecido))
# print(acc)

print(mirabol.predict(x_input))