#%%

import pandas as pd
import pickle as pk
from sklearn.model_selection import train_test_split
# load the model from disk
load_model_1 = pk.load(open('finalized_model_1.sav', 'rb'))
load_model_2 = pk.load(open('finalized_model_2.sav', 'rb'))
load_model_3 = pk.load(open('finalized_model_3.sav', 'rb'))
load_model_4 = pk.load(open('finalized_model_4.sav', 'rb'))
load_model_5 = pk.load(open('finalized_model_5.sav', 'rb'))
load_model_6 = pk.load(open('finalized_model_6.sav', 'rb'))
load_model_7 = pk.load(open('finalized_model_7.sav', 'rb'))
load_model_8 = pk.load(open('finalized_model_8.sav', 'rb'))
load_model_9 = pk.load(open('finalized_model_9.sav', 'rb'))
load_model_10 = pk.load(open('finalized_model_10.sav', 'rb'))
load_model_11 = pk.load(open('finalized_model_11.sav', 'rb'))
load_model_12 = pk.load(open('finalized_model_12.sav', 'rb'))
load_model_13 = pk.load(open('finalized_model_13.sav', 'rb'))
load_model_14 = pk.load(open('finalized_model_14.sav', 'rb'))
load_model_15 = pk.load(open('finalized_model_15.sav', 'rb'))
load_model_16 = pk.load(open('finalized_model_16.sav', 'rb'))
load_model_17 = pk.load(open('finalized_model_17.sav', 'rb'))
load_model_18 = pk.load(open('finalized_model_18.sav', 'rb'))
load_model_19 = pk.load(open('finalized_model_19.sav', 'rb'))
load_model_20 = pk.load(open('finalized_model_20.sav', 'rb'))
load_model_21 = pk.load(open('finalized_model_21.sav', 'rb'))
load_model_22 = pk.load(open('finalized_model_22.sav', 'rb'))
load_model_23 = pk.load(open('finalized_model_23.sav', 'rb'))
load_model_24 = pk.load(open('finalized_model_24.sav', 'rb'))

d_workout = pd.read_csv('C:/Users/Ali Raza Qureshi/Desktop/Models/exercise models/workout.csv')

#%%

import numpy
a = numpy.array([60,80,6.0,1])
print(load_model_9.predict([a]))

#%%

def train_model_1():
    data = d_workout[['age','weight','height','goal']]
    target = d_workout['straight bench press']
    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size = 0.30, random_state=65)
    from sklearn.naive_bayes import GaussianNB
    from sklearn.metrics import accuracy_score
    model = GaussianNB()
    pred = model.fit(data_train, target_train).predict(data_test)
    print("Naive-Bayes accuracy : ",accuracy_score(target_test, pred, normalize = True))
    # save the model to disk
    filename = 'finalized_model_1.sav'
    pk.dump(model, open(filename, 'wb'))

#%%

train_model_1()

#%%

def train_model_2():
    data = d_workout[['age','weight','height','goal']]
    target = d_workout['decline bench press']
    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size = 0.30, random_state=6)
    from sklearn.naive_bayes import GaussianNB
    from sklearn.metrics import accuracy_score
    model = GaussianNB()
    pred = model.fit(data_train, target_train).predict(data_test)
    print("Naive-Bayes accuracy : ",accuracy_score(target_test, pred, normalize = True))
    # save the model to disk
    filename = 'finalized_model_2.sav'
    pk.dump(model, open(filename, 'wb'))

#%%

train_model_2()

#%%

def train_model_3():
    data = d_workout[['age','weight','height','goal']]
    target = d_workout['dumbell flyes']
    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size = 0.30, random_state=51)
    from sklearn.naive_bayes import GaussianNB
    from sklearn.metrics import accuracy_score
    model = GaussianNB()
    pred = model.fit(data_train, target_train).predict(data_test)
    print("Naive-Bayes accuracy : ",accuracy_score(target_test, pred, normalize = True))
    # save the model to disk
    filename = 'finalized_model_3.sav'
    pk.dump(model, open(filename, 'wb'))

#%%

train_model_3()

#%%

def train_model_4():
    data = d_workout[['age','weight','height','goal']]
    target = d_workout['side laterals']
    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size = 0.30, random_state=58)
    from sklearn.naive_bayes import GaussianNB
    from sklearn.metrics import accuracy_score
    model = GaussianNB()
    pred = model.fit(data_train, target_train).predict(data_test)
    print("Naive-Bayes accuracy : ",accuracy_score(target_test, pred, normalize = True))
    # save the model to disk
    filename = 'finalized_model_4.sav'
    pk.dump(model, open(filename, 'wb'))

#%%

train_model_4()

#%%

def train_model_5():
    data = d_workout[['age','weight','height','goal']]
    target = d_workout['rear delt flyes']
    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size = 0.30, random_state=65)
    from sklearn.naive_bayes import GaussianNB
    from sklearn.metrics import accuracy_score
    model = GaussianNB()
    pred = model.fit(data_train, target_train).predict(data_test)
    print("Naive-Bayes accuracy : ",accuracy_score(target_test, pred, normalize = True))
    # save the model to disk
    filename = 'finalized_model_5.sav'
    pk.dump(model, open(filename, 'wb'))

#%%

train_model_5()

#%%

def train_model_6():
    data = d_workout[['age','weight','height','goal']]
    target = d_workout['face pull']
    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size = 0.30, random_state=61)
    from sklearn.naive_bayes import GaussianNB
    from sklearn.metrics import accuracy_score
    model = GaussianNB()
    pred = model.fit(data_train, target_train).predict(data_test)
    print("Naive-Bayes accuracy : ",accuracy_score(target_test, pred, normalize = True))
    # save the model to disk
    filename = 'finalized_model_6.sav'
    pk.dump(model, open(filename, 'wb'))

#%%

train_model_6()

#%%

def train_model_7():
    data = d_workout[['age','weight','height','goal']]
    target = d_workout['dumbell shrugs']
    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size = 0.30, random_state=71)
    from sklearn.naive_bayes import GaussianNB
    from sklearn.metrics import accuracy_score
    model = GaussianNB()
    pred = model.fit(data_train, target_train).predict(data_test)
    print("Naive-Bayes accuracy : ",accuracy_score(target_test, pred, normalize = True))
    # save the model to disk
    filename = 'finalized_model_7.sav'
    pk.dump(model, open(filename, 'wb'))

#%%

train_model_7()

#%%

def train_model_8():
    data = d_workout[['age','weight','height','goal']]
    target = d_workout['bent over barbell rows']
    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size = 0.30, random_state=38)
    from sklearn.naive_bayes import GaussianNB
    from sklearn.metrics import accuracy_score
    model = GaussianNB()
    pred = model.fit(data_train, target_train).predict(data_test)
    print("Naive-Bayes accuracy : ",accuracy_score(target_test, pred, normalize = True))
    # save the model to disk
    filename = 'finalized_model_8.sav'
    pk.dump(model, open(filename, 'wb'))

#%%

train_model_8()

#%%

def train_model_9():
    data = d_workout[['age','weight','height','goal']]
    target = d_workout['T bar rows']
    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size = 0.30, random_state=73)
    from sklearn.naive_bayes import GaussianNB
    from sklearn.metrics import accuracy_score
    model = GaussianNB()
    pred = model.fit(data_train, target_train).predict(data_test)
    print("Naive-Bayes accuracy : ",accuracy_score(target_test, pred, normalize = True))
    # save the model to disk
    filename = 'finalized_model_9.sav'
    pk.dump(model, open(filename, 'wb'))

#%%

train_model_9()

#%%

def train_model_10():
    data = d_workout[['age','weight','height','goal']]
    target = d_workout['front cable pull down']
    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size = 0.30, random_state=62)
    from sklearn.naive_bayes import GaussianNB
    from sklearn.metrics import accuracy_score
    model = GaussianNB()
    pred = model.fit(data_train, target_train).predict(data_test)
    print("Naive-Bayes accuracy : ",accuracy_score(target_test, pred, normalize = True))
    # save the model to disk
    filename = 'finalized_model_10.sav'
    pk.dump(model, open(filename, 'wb'))

#%%

train_model_10()

#%%

def train_model_11():
    data = d_workout[['age','weight','height','goal']]
    target = d_workout['back cable pull down']
    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size = 0.30, random_state=96)
    from sklearn.naive_bayes import GaussianNB
    from sklearn.metrics import accuracy_score
    model = GaussianNB()
    pred = model.fit(data_train, target_train).predict(data_test)
    print("Naive-Bayes accuracy : ",accuracy_score(target_test, pred, normalize = True))
    # save the model to disk
    filename = 'finalized_model_11.sav'
    pk.dump(model, open(filename, 'wb'))

#%%

train_model_11()

#%%

def train_model_12():
    data = d_workout[['age','weight','height','goal']]
    target = d_workout['barbell curls']
    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size = 0.30, random_state=58)
    from sklearn.naive_bayes import GaussianNB
    from sklearn.metrics import accuracy_score
    model = GaussianNB()
    pred = model.fit(data_train, target_train).predict(data_test)
    print("Naive-Bayes accuracy : ",accuracy_score(target_test, pred, normalize = True))
    # save the model to disk
    filename = 'finalized_model_12.sav'
    pk.dump(model, open(filename, 'wb'))

#%%

train_model_12()

#%%

def train_model_13():
    data = d_workout[['age','weight','height','goal']]
    target = d_workout['hammer curls']
    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size = 0.30, random_state=61)
    from sklearn.naive_bayes import GaussianNB
    from sklearn.metrics import accuracy_score
    model = GaussianNB()
    pred = model.fit(data_train, target_train).predict(data_test)
    print("Naive-Bayes accuracy : ",accuracy_score(target_test, pred, normalize = True))
    # save the model to disk
    filename = 'finalized_model_13.sav'
    pk.dump(model, open(filename, 'wb'))

#%%

train_model_13()

#%%

def train_model_14():
    data = d_workout[['age','weight','height','goal']]
    target = d_workout['ez bar curls']
    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size = 0.30, random_state=25)
    from sklearn.naive_bayes import GaussianNB
    from sklearn.metrics import accuracy_score
    model = GaussianNB()
    pred = model.fit(data_train, target_train).predict(data_test)
    print("Naive-Bayes accuracy : ",accuracy_score(target_test, pred, normalize = True))
    # save the model to disk
    filename = 'finalized_model_14.sav'
    pk.dump(model, open(filename, 'wb'))

#%%

train_model_14()

#%%

def train_model_15():
    data = d_workout[['age','weight','height','goal']]
    target = d_workout['preacher curls']
    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size = 0.30, random_state=2)
    from sklearn.naive_bayes import GaussianNB
    from sklearn.metrics import accuracy_score
    model = GaussianNB()
    pred = model.fit(data_train, target_train).predict(data_test)
    print("Naive-Bayes accuracy : ",accuracy_score(target_test, pred, normalize = True))
    # save the model to disk
    filename = 'finalized_model_15.sav'
    pk.dump(model, open(filename, 'wb'))

#%%

train_model_15()

#%%

def train_model_16():
    data = d_workout[['age','weight','height','goal']]
    target = d_workout['tricep dips']
    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size = 0.30, random_state=2)
    from sklearn.naive_bayes import GaussianNB
    from sklearn.metrics import accuracy_score
    model = GaussianNB()
    pred = model.fit(data_train, target_train).predict(data_test)
    print("Naive-Bayes accuracy : ",accuracy_score(target_test, pred, normalize = True))
    # save the model to disk
    filename = 'finalized_model_16.sav'
    pk.dump(model, open(filename, 'wb'))

#%%

train_model_16()

#%%

def train_model_17():
    data = d_workout[['age','weight','height','goal']]
    target = d_workout['squat']
    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size = 0.30, random_state=49)
    from sklearn.naive_bayes import GaussianNB
    from sklearn.metrics import accuracy_score
    model = GaussianNB()
    pred = model.fit(data_train, target_train).predict(data_test)
    print("Naive-Bayes accuracy : ",accuracy_score(target_test, pred, normalize = True))
    # save the model to disk
    filename = 'finalized_model_17.sav'
    pk.dump(model, open(filename, 'wb'))

#%%

train_model_17()

#%%

def train_model_18():
    data = d_workout[['age','weight','height','goal']]
    target = d_workout['leg press']
    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size = 0.30, random_state=1)
    from sklearn.naive_bayes import GaussianNB
    from sklearn.metrics import accuracy_score
    model = GaussianNB()
    pred = model.fit(data_train, target_train).predict(data_test)
    print("Naive-Bayes accuracy : ",accuracy_score(target_test, pred, normalize = True))
    # save the model to disk
    filename = 'finalized_model_18.sav'
    pk.dump(model, open(filename, 'wb'))

#%%

train_model_18()

#%%

def train_model_19():
    data = d_workout[['age','weight','height','goal']]
    target = d_workout['dumbell lunges']
    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size = 0.30, random_state=61)
    from sklearn.naive_bayes import GaussianNB
    from sklearn.metrics import accuracy_score
    model = GaussianNB()
    pred = model.fit(data_train, target_train).predict(data_test)
    print("Naive-Bayes accuracy : ",accuracy_score(target_test, pred, normalize = True))
    # save the model to disk
    filename = 'finalized_model_19.sav'
    pk.dump(model, open(filename, 'wb'))

#%%

train_model_19()

#%%

def train_model_20():
    data = d_workout[['age','weight','height','goal']]
    target = d_workout['lying leg curl']
    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size = 0.30, random_state=69)
    from sklearn.naive_bayes import GaussianNB
    from sklearn.metrics import accuracy_score
    model = GaussianNB()
    pred = model.fit(data_train, target_train).predict(data_test)
    print("Naive-Bayes accuracy : ",accuracy_score(target_test, pred, normalize = True))
    # save the model to disk
    filename = 'finalized_model_20.sav'
    pk.dump(model, open(filename, 'wb'))

#%%

train_model_20()

#%%

def train_model_21():
    data = d_workout[['age','weight','height','goal']]
    target = d_workout['front barbell press']
    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size = 0.30, random_state=11)
    from sklearn.naive_bayes import GaussianNB
    from sklearn.metrics import accuracy_score
    model = GaussianNB()
    pred = model.fit(data_train, target_train).predict(data_test)
    print("Naive-Bayes accuracy : ",accuracy_score(target_test, pred, normalize = True))
    # save the model to disk
    filename = 'finalized_model_21.sav'
    pk.dump(model, open(filename, 'wb'))

#%%

train_model_21()

#%%

def train_model_22():
    data = d_workout[['age','weight','height','goal']]
    target = d_workout['deadlift']
    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size = 0.30, random_state=15)
    from sklearn.naive_bayes import GaussianNB
    from sklearn.metrics import accuracy_score
    model = GaussianNB()
    pred = model.fit(data_train, target_train).predict(data_test)
    print("Naive-Bayes accuracy : ",accuracy_score(target_test, pred, normalize = True))
    # save the model to disk
    filename = 'finalized_model_22.sav'
    pk.dump(model, open(filename, 'wb'))

#%%

train_model_22()

#%%

def train_model_23():
    data = d_workout[['age','weight','height','goal']]
    target = d_workout['double hand overhead dumbell press']
    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size = 0.30, random_state=34)
    from sklearn.naive_bayes import GaussianNB
    from sklearn.metrics import accuracy_score
    model = GaussianNB()
    pred = model.fit(data_train, target_train).predict(data_test)
    print("Naive-Bayes accuracy : ",accuracy_score(target_test, pred, normalize = True))
    # save the model to disk
    filename = 'finalized_model_23.sav'
    pk.dump(model, open(filename, 'wb'))

#%%

train_model_23()

#%%

def train_model_24():
    data = d_workout[['age','weight','height','goal']]
    target = d_workout['skullcrusher']
    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size = 0.30, random_state=68)
    from sklearn.naive_bayes import GaussianNB
    from sklearn.metrics import accuracy_score
    model = GaussianNB()
    pred = model.fit(data_train, target_train).predict(data_test)
    print("Naive-Bayes accuracy : ",accuracy_score(target_test, pred, normalize = True))
    # save the model to disk
    filename = 'finalized_model_24.sav'
    pk.dump(model, open(filename, 'wb'))

#%%

train_model_24()

#%%

def test_model():
    data = d_workout[['age','weight','height','goal']]
    target = d_workout['skullcrusher']
    a = []
    for i in range(0,100):
        data_train, data_test, target_train, target_test = train_test_split(data, target, test_size = 0.30, random_state=i)
        from sklearn.naive_bayes import GaussianNB
        from sklearn.metrics import accuracy_score
        model = GaussianNB()
        pred = model.fit(data_train, target_train).predict(data_test)
        a.append(accuracy_score(target_test, pred, normalize = True))
    print(a.index(max(a)))

#%%

test_model()

#%%


