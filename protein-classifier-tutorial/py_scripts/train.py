import sklearn
from sklearn.svm import SVC
from sklearn.utils import shuffle
import sklearn.model_selection as model_selection
import pandas as pd

tar = pd.read_pickle('/Users/desho/Desktop/protein-classifier-tutorial/training_sets/tardigrade_set.pkl')
# tar.to_csv("test.csv")
pop = pd.read_pickle('/Users/desho/Desktop/protein-classifier-tutorial/training_sets/poplar_set.pkl')

membrane_proteins = pd.concat([tar, pop], axis=0)

X = membrane_proteins.drop(['target', 'flexibility'], axis='columns')
y = membrane_proteins.target

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)

# model = SVC()
model = SVC(gamma=100, kernel='linear')
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
