import pickle

from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

from config import MODELPATH


iris = load_iris()
X = iris.data
y = iris.target


def train(X, y):
    """just a simple training job"""
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    clf = DecisionTreeClassifier()
    model = clf.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(accuracy)

    pickle.dump(model, open(MODELPATH, 'wb'))


if __name__ == "__main__":
    train(X, y)