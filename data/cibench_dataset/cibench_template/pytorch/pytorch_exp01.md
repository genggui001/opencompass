---
jupyter:
  title: Sentiment Analysis using pytorch
  dataset: Sentiment140 Dataset
  difficulty: Middle
  module: pytorch
  idx: 1
  num_steps: 7
  step_types:
    - exec
    - exec
    - exec
    - exec
    - exec
    - exec
    - exec
  modules:
    - pandas
    - nltk
    - pytorch
    - pytorch & sklearn
    - pytorch
    - pytorch
    - pytorch & sklearn
---
File Path: 'data/pytorch_dataset01.csv'

Load the dataset from the file path into a pandas DataFrame. Display the first 5 rows.
```python
import pandas as pd

tweets_df = pd.read_csv('data/pytorch_dataset01.csv')
tweets_df.head()
```

Preprocess the data and use labelencoder to sentiment. Tokenize the text data and convert to lowercase. Remove the punctuations and stopwords from the text data. Finally build a vocabulary of all the tokens and assign an index to the vocabulary. Display the index of the word "happy".

```python
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
from sklearn.preprocessing import LabelEncoder

nltk.download('punkt')
nltk.download('stopwords')
tweets_df['sentiment'] = LabelEncoder().fit_transform(tweets_df['sentiment'])

def preprocess_and_tokenize(texts):
    vocabulary = Counter()
    processed_texts = []
    stop_words = set(stopwords.words('english'))
    
    for text in texts:
        # 分词
        words = word_tokenize(text.lower())
        
        # 去除停用词和非字母字符
        words = [word for word in words if word.isalpha() and word not in stop_words]
        
        # 更新词汇表
        vocabulary.update(words)
        
        # 添加处理后的文本到列表
        processed_texts.append(words)
    
    return processed_texts, vocabulary

# 应用预处理和分词
processed_texts, vocab = preprocess_and_tokenize(tweets_df['text'])

# 为词汇分配索引
word_to_index = {word: i+2 for i, word in enumerate(vocab)}  # 索引从 2 开始，留出 0 和 1
word_to_index['&lt;pad&gt;'] = 0  # 填充标记
word_to_index['&lt;unk&gt;'] = 1  # 未知词标记

# 展示“happy”的数值标签
word_to_index['happy']
```

Define the maximum length of the sequence to 20, and digitize the text to facilitate subsequent text processing.
Display the numericalized representation of the first text.

```python
# 文本数值化
def numericalize(tokenized_texts, word_to_index, max_length):
    numericalized_texts = []
    for tokens in tokenized_texts:
        numericalized_text = [word_to_index.get(word, word_to_index['&lt;unk&gt;']) for word in tokens]
        # 填充或截断
        numericalized_text = numericalized_text[:max_length] + [word_to_index['&lt;pad&gt;']] * (max_length - len(numericalized_text))
        numericalized_texts.append(numericalized_text)
    return numericalized_texts

max_length = 20  # 定义序列最大长度
numericalized_texts = numericalize(processed_texts, word_to_index, max_length)
# 展示第一条文本的数值化表示
numericalized_texts[0]
```

Split the dataset into training and testing sets using 0.2 as the test size, then define the train_loader and test_loader. Set batch size as 64.

```python
import torch
from torch.utils.data import DataLoader, Dataset
from sklearn.model_selection import train_test_split

class TextDataset(Dataset):
    def __init__(self, texts, labels):
        self.texts = texts
        self.labels = labels

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        return torch.tensor(self.texts[idx], dtype=torch.long), torch.tensor(self.labels[idx], dtype=torch.float)

# 创建数据集
dataset = TextDataset(numericalized_texts, tweets_df['sentiment'])

train_data, test_data = train_test_split(dataset, test_size=0.2, random_state=42)

# 创建 DataLoader
batch_size = 64
train_loader = DataLoader(train_data, shuffle=True, batch_size=batch_size)
test_loader = DataLoader(test_data, shuffle=True, batch_size=batch_size)
```

Define a "SentimentAnalysisLSTM" model for NLP using vocab_size，embedding_dim, hidden_dim, output_dim, n_layers. Put the model to device.

```python
import torch.nn as nn

class SentimentAnalysisLSTM(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim, output_dim, n_layers, drop_prob=0.5):
        super(SentimentAnalysisLSTM, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.lstm = nn.LSTM(embedding_dim, hidden_dim, n_layers, dropout=drop_prob, batch_first=True)
        self.dropout = nn.Dropout(drop_prob)
        self.fc = nn.Linear(hidden_dim, output_dim)
        self.sigmoid = nn.Sigmoid()
        
    def forward(self, x):
        embedded = self.embedding(x)
        lstm_out, hidden = self.lstm(embedded)
        out = self.dropout(lstm_out)
        out = self.fc(out[:, -1])
        return self.sigmoid(out)

vocab_size = len(word_to_index)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = SentimentAnalysisLSTM(vocab_size, embedding_dim=400, hidden_dim=256, output_dim=1, n_layers=2)
model.to(device)
```

Define the BCELoss loss function and the Adam optimizer. Train the model for 5 epochs. Display the loss for the last epoch(Keep to two decimal places).

```python
import torch.optim as optim

criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

epochs = 5
for epoch in range(epochs):
    model.train()
    running_loss = 0.0
    for inputs, labels in train_loader:
        inputs, labels = inputs.to(device), labels.to(device)
        
        optimizer.zero_grad()
        
        outputs = model(inputs)
        loss = criterion(outputs.squeeze(), labels.float())
        loss.backward()
        optimizer.step()
        
        running_loss += loss.item()
    
    if epoch == 4:
        final_loss = round(running_loss/len(train_loader), 2)
        print(final_loss)
```

Evaluate the model performance on the test set. Report the model's accuracy(Keep to two decimal places).

```python
import numpy as np

model.eval()
predictions, truths = [], []
with torch.no_grad():
    for inputs, labels in test_loader:
        inputs, labels = inputs.to(device), labels.to(device)
        
        outputs = model(inputs)
        predictions.append(outputs.squeeze())
        truths.append(labels)
        
predictions = torch.cat(predictions).cpu().numpy()
truths = torch.cat(truths).cpu().numpy()
predictions = np.round(predictions)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(truths, predictions)
round(accuracy, 2)
```