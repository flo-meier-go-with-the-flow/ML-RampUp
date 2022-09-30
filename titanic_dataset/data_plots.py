import matplotlib.pyplot as plt
from titanic_dataset.load_data import fetch_titanic_data, load_titanic_data
from preprocessing import preprocessing
import math

fetch_titanic_data()
train_data = load_titanic_data("train.csv")
test_data = load_titanic_data("test.csv")

# preprocessing parameters
embarked_onehot = False
pclass_onehot = False
train_data, y_train = preprocessing(train_data, embarked_onehot=embarked_onehot, pclass_onehot=pclass_onehot)


print(train_data.head())
train_data.hist(bins=50, figsize=(20,15))
#save_fig("attribute_histogram_plots")
#plt.show()


print(train_data[train_data['Fare']<=0])
#print(train_data['Fare'].apply(lambda x: math.log(x)))