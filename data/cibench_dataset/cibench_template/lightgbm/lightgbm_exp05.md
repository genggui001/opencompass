---
jupyter:
  title: LightGBM tasks
  dataset: heart dataset
  difficulty: Middle
  module: LightGBM
  idx: 5
  num_steps: 6
  step_types:
    - exec
    - exec
    - exec
    - num
    - num
    - num
  modules:
    - pandas
    - sklearn
    - LightGBM
    - LightGBM & sklearn
    - LightGBM 
    - sklearn
---

File Path: "data/lightgbm_dataset05.csv"

Load the dataset from the file path into a pandas DataFrame. Display the column names.

```python
import pandas as pd

path = "data/lightgbm_dataset05.csv"
df = pd.read_csv(path)
print(df.columns)
```

Split the data into features and target "output", conduct label encoder towards y label and any other non-numeric columns, then into training and testing sets with test size being 0.2.
```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

X = df.drop(columns=['output'], axis=1)
y = df['output']
y = LabelEncoder().fit_transform(y)
X = pd.get_dummies(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

Define a LightGBM model  with max_depth=4, n_estimators=120，learning_rate=0.01 and num_leaves=31. Train the model with Evaluation Metric='logloss'.
```python
import lightgbm as lgb

lgbm_model = lgb.LGBMClassifier(max_depth=4, n_estimators=120, learning_rate=0.01, num_leaves=31)
lgbm_model.fit(X_train, y_train, eval_metric='logloss', eval_set=[(X_test, y_test)])
```

Predict the target for the test set and Evaluate the model using the test set. Give the confusion matrix and corresponding accuracy, precision, and recall. Remember you only need to display the accuracy of the model on the test set(Keep to two decimal places).
```python
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

y_pred = lgbm_model.predict(X_test)
conf_matrix = confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='macro')
recall = recall_score(y_test, y_pred, average='macro')
round(accuracy, 2)
```

Get the feature importance of each feature，print the importance of the most important feature(Keep to two decimal places).

```python
# 获取特征重要性
importance = lgbm_model.feature_importances_
feature_names = X_train.columns
feature_importance = pd.DataFrame({'feature_names': feature_names, 'importance': importance})
feature_importance = feature_importance.sort_values(by='importance', ascending=False)
round(feature_importance.iloc[0][1], 2)
```

Conduct model parameter tuning for max_depth, learning_rate, n_estimators, select three alternative values of each parameter and output the optimal value of n_estimators.

```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    'max_depth': [3, 4, 5],
    'learning_rate': [0.01, 0.05, 0.1],
    'n_estimators': [50, 100, 150],
}
grid_search = GridSearchCV(estimator=lgbm_model, param_grid=param_grid, scoring='accuracy', cv=3, verbose=1)
grid_search.fit(X_train, y_train)
grid_search.best_params_["n_estimators"]
```