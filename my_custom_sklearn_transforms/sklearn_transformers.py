from sklearn.base import BaseEstimator, TransformerMixin

class RemoveColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        data = X.copy()

        return data.drop(labels=self.columns, axis='columns')
