---
jupyter:
  title: LightGBM tasks
  dataset: breast cancer dataset
  difficulty: Middle
  module: LightGBM
  idx: 3
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

文件路径： "data/lightgbm_dataset03.csv"

从文件路径加载数据集到pandas DataFrame中。显示列名。

```python
import pandas as pd

path = "data/lightgbm_dataset03.csv"
df = pd.read_csv(path)
print(df.columns)
import re
# add to solve speical json character format error
df = df.rename(columns = lambda x:re.sub('[^A-Za-z0-9_]+', '', x))
```

将数据分为特征和目标"diagnosis"，对y标签和任何其他非数字列进行标签编码，然后将其分为训练和测试集，测试集大小为0.2。

```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

X = df.drop(columns=['diagnosis'], axis=1)
y = df['diagnosis']
y = LabelEncoder().fit_transform(y)
X = pd.get_dummies(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

定义一个LightGBM模型，max_depth=4, n_estimators=120，learning_rate=0.01 and num_leaves=31。使用评估指标'logloss'训练模型。
```python
import lightgbm as lgb

lgbm_model = lgb.LGBMClassifier(max_depth=4, n_estimators=120, learning_rate=0.01, num_leaves=31)
lgbm_model.fit(X_train, y_train, eval_metric='logloss', eval_set=[(X_test, y_test)])
```

预测测试集的目标，并使用测试集评估模型。给出混淆矩阵和相应的准确率、精确率和召回率。最后，只需显示模型在测试集上的准确率(保留两位小数)。
```python
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

y_pred = lgbm_model.predict(X_test)
conf_matrix = confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='macro')
recall = recall_score(y_test, y_pred, average='macro')
round(accuracy, 2)
```

获得每个特征的重要性，打印最重要特征的重要性(保留两位小数)。

```python
# 获取特征重要性
importance = lgbm_model.feature_importances_
feature_names = X_train.columns
feature_importance = pd.DataFrame({'feature_names': feature_names, 'importance': importance})
feature_importance = feature_importance.sort_values(by='importance', ascending=False)
round(feature_importance.iloc[0][1], 2)
```

对max_depth, learning_rate, n_estimators进行模型参数调优，选择每个参数的三个备选值，输出n_estimators的最优值。

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