import pickle
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing, cross_validation

carDat=open("carDat.pickle","rb")
gameData=pickle.load(carDat)
trainx=[]
trainy=[]

for feature in gameData:
    trainx.append(feature[0:3])


for feature in gameData:
    trainy.append(feature[-1])   

X_train,X_test,y_train,y_test = cross_validation.train_test_split(trainx,trainy,test_size=0.2)

clf = LogisticRegression(n_jobs = -1)
clf.fit(X_train,y_train)
accuracy = clf.score(X_test,y_test)
for x in X_test:
    print(x,clf.predict(x))

with open('trainedGame.pickle','wb') as f:
    pickle.dump(clf, f)

print(accuracy)



