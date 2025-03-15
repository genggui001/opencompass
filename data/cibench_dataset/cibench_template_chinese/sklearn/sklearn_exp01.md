---
jupyter:
  title: Sklearn分类任务
  dataset: 鸢尾花数据集
  difficulty: 中级
  module: Sklearn
  idx: 1
  num_steps: 7
  step_types:
    - exec
    - exec
    - vis
    - exec
    - vis
    - num
    - vis
  modules:
    - pandas
    - sklearn
    - sklearn & matplotlib
    - sklearn
    - sklearn & matplotlib
    - sklearn
    - sklearn & matplotlib
---

文件路径: `data/sklearn_dataset01.csv`

### 从文件路径加载数据集,保存为 pandas DataFrame，并显示列名。
```python
import pandas as pd
df = pd.read_csv("data/sklearn_dataset01.csv")
df.columns
```

### 将数据拆分为特征x和目标y两部分,其中 "Species"列作为目标，其余列作为特征，对 y 标签和其他非数值列进行标签编码，然后划分为训练集和测试集，测试集大小为数据集的1/5。
```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

X = df.drop(columns=['Species'], axis=1)
y = df['Species']
y = LabelEncoder().fit_transform(y)
X = pd.get_dummies(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

### 首先使用 "PCA" 对特征数据进行降维，然后在三维空间中显示不同类别的数据。
```python
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

Dimensionality_Reduction = "PCA"
Plot_Title = "PCA of Iris Dataset"

pca = PCA(n_components=3)
X_pca = pca.fit_transform(X_train)
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X_pca[:, 0], X_pca[:, 1], X_pca[:, 2], c=LabelEncoder().fit_transform(y_train))
ax.set_title(Plot_Title)
plt.show()
```

### 建立 MLP 分类模型，使用优化器 "Adam" 和激活函数 "relu"。然后进行 200 轮模型训练。
```python
from sklearn.neural_network import MLPClassifier

Model_Name = "MLPClassifier"
Optimizer = "adam"
Activation_Function = "relu"

model = MLPClassifier(hidden_layer_sizes=(100,), max_iter=200, activation=Activation_Function, solver=Optimizer, random_state=42)
model.fit(X_train, y_train)
```

### 绘制以 epoch 为横轴、损失为纵轴的损失曲线。
```python
train_accuracy = model.score(X_train, y_train)
test_accuracy = model.score(X_test, y_test)

plt.figure(figsize=(10,6))
plt.plot(model.loss_curve_)
plt.title("Loss Curve")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.show()
```

### 对测试集进行预测，给出混淆矩阵，并计算每个类别的预测准确度、精确度、召回率和 F1 分数。最后，显示模型在测试集上的准确度（保留两位小数）。
```python
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

y_pred = model.predict(X_test)
y_true = y_test

confusion = confusion_matrix(y_true, y_pred)
accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred, average=None)
recall = recall_score(y_true, y_pred, average=None)
f1 = f1_score(y_true, y_pred, average=None)

round(accuracy, 2)
```

### 用 3D 图形可视化pca降维后的预测数据。
```python
predictions = model.predict(X_test)
X_pca_test = pca.transform(X_test)

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X_pca_test[:, 0], X_pca_test[:, 1], X_pca_test[:, 2], c=LabelEncoder().fit_transform(predictions))
ax.set_title(Plot_Title)
plt.show()
```