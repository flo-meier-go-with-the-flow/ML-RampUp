import pandas as pd
import sklearn.preprocessing
from titanic_dataset.load_data import fetch_titanic_data, load_titanic_data

bool_has_parent = False
bool_has_child = False
bool_is_married = False
bool_is_child_of_big_family = False
bool_remove_SibSp = False
bool_remove_Parch = False


def preprocessing(train_data, embarked_onehot=True, pclass_onehot=True, bool_has_parent=True, bool_has_child=True,\
                  bool_is_married=True,bool_is_child_of_big_family=True, bool_remove_SibSp=True, bool_remove_Parch=True):
    # drop data columns
    train_data.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1, inplace=True)
    # important: try one hot for Embarked

    # encode female: 1, male: 0
    train_data['Sex'] = (train_data['Sex'] == 'female').astype(int)

    # fill Age NaN with mean
    median = train_data['Age'].mean()
    train_data["Age"].fillna(median, inplace=True)

    #fill Fare=0 values with average Fare of that Pclass
    train_data[(train_data['Fare'] == 0) & (train_data['Pclass'] == 1)]['Fare'].replace({0.0: train_data[train_data['Pclass']==1]['Fare'].mean()}, inplace=True)
    print(train_data[(train_data['Fare']==0) & (train_data['Pclass']==1)]['Fare'])
    print(train_data[train_data['Pclass']==1]['Fare'].mean())
        #=train_data[train_data['Fare']==0]['Fare'].mean()
    if embarked_onehot:
        titanic_cat = train_data[["Embarked"]]
        max_cat = 3
        cat_encoder = sklearn.preprocessing.OneHotEncoder(max_categories=max_cat)
        titanic_cat_1hot = cat_encoder.fit_transform(titanic_cat).toarray()
        # print(titanic_cat_1hot.shape)
        # print(cat_encoder.categories_)
        embarked_onehot_df = pd.DataFrame(titanic_cat_1hot, columns=['C', 'Q', 'S'])
        # print(embarked_onehot_df.head())
        train_data = pd.concat([train_data, embarked_onehot_df], axis=1)
    if pclass_onehot:
        titanic_cat = train_data[["Pclass"]]
        cat_encoder = sklearn.preprocessing.OneHotEncoder()
        titanic_cat_1hot = cat_encoder.fit_transform(titanic_cat).toarray()
        # print(titanic_cat_1hot.shape)
        # print(cat_encoder.categories_)
        pclass_onehot_df = pd.DataFrame(titanic_cat_1hot, columns=['pclass 1', 'pclass 2', 'pclass 3'])
        # print(pclass_onehot_df.head())
        train_data = pd.concat([train_data, pclass_onehot_df], axis=1)
        train_data.drop(['Pclass'], axis=1, inplace=True)
    train_data.drop(['Embarked'], axis=1, inplace=True)

    if bool_has_parent:
        train_data['has_parent']=((train_data['Parch']>=1) & (train_data['Age']<18)).replace({True: 1, False: 0})
    #print(train_data[14 < train_data['Age'] < 19][['Age', 'SibSp', 'Parch']])

    if bool_has_child:
        train_data['has_child']=((train_data['Parch']>=1) & (train_data['Age']>=18)).replace({True: 1, False: 0})

    #variable that is True if age>=18 is married or has siblings on board
    if bool_is_married:
        train_data['is_married']=((train_data['SibSp']>=1) & (train_data['Age']>=18)).replace({True: 1, False: 0})

    #variable that is True if age <18 and has siblings
    if bool_is_child_of_big_family:
        train_data['child_of_big_familiy']=((train_data['SibSp']>=1) & (train_data['Age']<18)).replace({True: 1, False: 0})

    if bool_remove_SibSp:
        train_data.drop(['SibSp'],inplace=True,axis=1)
    if bool_remove_Parch:
        train_data.drop(['Parch'],inplace=True,axis=1)



    X_train = train_data.drop(['Survived'], axis=1)
    y_train = train_data['Survived'].to_numpy()
    return X_train, y_train


if __name__ == '__main__':
    fetch_titanic_data()
    train_data = load_titanic_data("train.csv")
    test_data = load_titanic_data("test.csv")

    # preprocessing parameters
    embarked_onehot = True
    pclass_onehot = True
    train_data, y_train = preprocessing(train_data, embarked_onehot=embarked_onehot, pclass_onehot=pclass_onehot)
    print(train_data.head())
    #print(train_data[(train_data['Parch']==0) & (train_data['SibSp']>1)][['Age','SibSp','Parch']])
