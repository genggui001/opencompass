---
jupyter:
  title: Implement natural language processing with nltk
  dataset: AI texts
  difficulty: Middle
  module: nltk
  idx: 2
  num_steps: 7
  step_types:
    - exec
    - num
    - text
    - text
    - vis
    - num
    - num
  modules:
    - nltk
    - nltk
    - nltk
    - nltk
    - matplotlib
    - nltk
    - nltk
---

文本内容："Artificial intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think and act like humans. The term can also be applied to any machine that exhibits traits associated with a human mind such as learning and problem-solving. The ideal characteristic of artificial intelligence is its ability to rationalize and take actions that have the best chance of achieving a specific goal."

加载文本并将所有单词转换为小写。基于word tokenizer对文本进行分词。

```python
from nltk.tokenize import word_tokenize
ai_text = "Artificial intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think and act like humans. The term can also be applied to any machine that exhibits traits associated with a human mind such as learning and problem-solving. The ideal characteristic of artificial intelligence is its ability to rationalize and take actions that have the best chance of achieving a specific goal."
lowercase_text = ai_text.lower()
tokens = word_tokenize(lowercase_text)
```

从文本中删除英文停用词。从token列表中删除标点符号。最后报告tokens的数量。

```python
import nltk
from nltk.corpus import stopwords
import string
nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words("english"))
tokens = [word for word in tokens if word not in stop_words]
tokens = [word for word in tokens if word not in string.punctuation]
len(tokens)
```

为这些tokens实现词干提取。显示stemmed_tokens中的前五个tokens。

```python
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(word) for word in tokens]
print(stemmed_tokens[:5])
```

计算stemmed tokens的频率分布。显示频率最高的token和其频率。

```python
from nltk.probability import FreqDist

freq_dist = FreqDist(stemmed_tokens)
common_tokens = freq_dist.most_common(10)
common_tokens[0]
```

使用figsize=(12, 6)的折形图可视化前十个频率最高tokens的累计频率分布。

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
freq_dist.plot(10, cumulative=True)
plt.show()
```

为第二步结束后得到的tokens实现词性标注。显示名词、动词和形容词数量的总和。

```python
from nltk.tag import pos_tag
from collections import Counter

pos_tags = pos_tag(tokens)
# Counting part-of-speech tags
pos_counts = Counter(tag for word, tag in pos_tags)

# Extracting counts for nouns, verbs, adjectives, and adverbs
noun_count = sum(val for key, val in pos_counts.items() if key.startswith('N'))
verb_count = sum(val for key, val in pos_counts.items() if key.startswith('V'))
adjective_count = sum(val for key, val in pos_counts.items() if key.startswith('J'))

noun_count + verb_count + adjective_count
```

基于上一步的结果。计算每个组的标准化后的频率（名词、动词、形容词和副词）。打印数值最高的频率(保留两位小数)。

```python

adverb_count = sum(val for key, val in pos_counts.items() if key.startswith('R'))

normalized_nouns = round(noun_count / len(pos_tags), 2)
normalized_verbs = round(verb_count / len(pos_tags), 2)
normalized_adjectives = round(adjective_count / len(pos_tags), 2)
normalized_adverbs = round(adverb_count / len(pos_tags), 2)

# Calculate total number of tokens
max([normalized_nouns, normalized_verbs, normalized_adjectives, normalized_adverbs])
```