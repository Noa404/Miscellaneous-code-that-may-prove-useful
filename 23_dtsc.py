# Data from https://datahub.io/machine-learning/creditcard#resource-creditcard

import xgboost as xgb
import pandas as pd
import numpy as np
    def read_data(path:str) -> pd.DataFrame:
        """read in credit card data
        Args:
            path (str): location of credit card data on disk
        Retruns:
            pd.Dataframe: a Dataframe including feature vectors as well as class labels
         """

        df = pd.read_csv(path)
        df['Class'] = df['Class'].str.replace("'",'').astype(int)
            return df

    def train_classifier(data:np.ndarray, labels: np.ndarray, train_test_split: float = 0.8) -> xgb.XGBClassifier:
        """Take credit card data create a classifier to estimate if a transaction is fraudulent

        Args:
            data (mp.ndarray):numpy array of feature vectors lavels (np.ndarray): numpy array of lavels

        Returns:
            xgb.XGBClassifier: a working character"""
        n_rows = len(labels)
        n_training_rows = int(n_rows*n_train_test_split)
        train_data, test_data = data[:,0:n_training_rows], data[:, n_training_rows:]
        train_labels, test_labels = labels[0:n_training_rows], labels[n_training_rows:]




        model = xgb.XGBClassifier()
        model.fit(train_data,train_labels, verbose = True)

        model_labels = model.predict(test_data)
        print('fraction correct', np.sum(model_labels == test_labels)/len(test_labels))
        return model

    if __name__ == '__main__':
        df = read_data('data/creditcard')
        data = df[[f'V{i}'for i in range(1,29)]].values
        labels = df['Class'].values

        model = train
#

    #model = xgb.XGBlassifier()

    if__name__ = 'main':
        read_data('data/creditcard_csv.csv')
