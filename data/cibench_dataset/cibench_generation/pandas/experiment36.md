---
jupyter:
  title: Data set preprocessing using pandas in Python
  dataset: apple chart Dataset
  difficulty: Easy
  module: pandas
  idx: 36
  num_steps: 5
  step_types:
    - exec
    - vis
    - vis
    - vis
    - vis
  modules:
    - pandas
    - pandas&matplotlib
    - pandas&matplotlib
    - pandas&matplotlib
    - pandas&matplotlib
---

File Path: `data/finance-charts-apple.csv`

Load the dataset from the path into a pandas dataframe called df.

```python
import pandas as pd
url = 'data/finance-charts-apple.csv'
df = pd.read_csv(url)
df.head()
```

Calculate the daily returns of the 'AAPL.Close' column as the percentage change from the previous day. Add this as a new column 'Daily Returns' in the dataframe. Generate a line plot of the 'Daily Returns' column from the dataframe to visualize the daily returns of Apple's stock over time.
```python
import matplotlib.pyplot as plt
df['Daily Returns'] = df['AAPL.Close'].pct_change()
plt.figure(figsize=(10, 6))
df['Daily Returns'].plot()
plt.title('Apple Daily Returns')
plt.xlabel('Date')
plt.ylabel('Returns')
plt.show()
```

Calculate the 50-day and 200-day moving averages of the 'AAPL.Close' column and add these as new columns 'MA50' and 'MA200' in the dataframe. Generate a line plot of the 'AAPL.Close', 'MA50', and 'MA200' columns from the dataframe to visualize the closing price of Apple's stock along with its moving averages over time.
```python
df['MA50'] = df['AAPL.Close'].rolling(50).mean()
df['MA200'] = df['AAPL.Close'].rolling(200).mean()
plt.figure(figsize=(10, 6))
df[['AAPL.Close','MA50','MA200']].plot()
plt.title('Apple Closing Price with Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.show()
```

Calculate the cumulative returns from the 'Daily Returns' column and add it as a new column 'Cumulative Returns' in the dataframe. Generate a line plot of the 'Cumulative Returns' column from the dataframe to visualize the growth of a $1 investment in Apple's stock over time.
```python
df['Cumulative Returns'] = (1 + df['Daily Returns']).cumprod()

plt.figure(figsize=(10, 6))
df['Cumulative Returns'].plot()
plt.title('Apple Cumulative Returns')
plt.xlabel('Date')
plt.ylabel('Growth of $1 investment')
plt.show()
```

Calculate the annualized volatility from the 'Daily Returns' column and add it as a new column 'Volatility' in the dataframe. Generate a line plot of the 'Volatility' column from the dataframe to visualize the volatility of Apple's stock over time.
```python
import numpy as np
df['Volatility'] = df['Daily Returns'].rolling(252).std() * np.sqrt(252)

plt.figure(figsize=(10, 6))
df['Volatility'].plot()
plt.title('Apple Volatility')
plt.xlabel('Date')
plt.ylabel('Volatility')
plt.show()
```
