---
jupyter:
  title: Implement natural language processing with nltk
  dataset: Shakespeare
  difficulty: Middle
  module: nltk
  idx: 8
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

Text Content: "Romeo and Juliet is a tragedy written by William Shakespeare. It is among the most popular plays ever written in the English language. The play revolves around two young star-crossed lovers whose deaths ultimately reconcile their feuding families."

Load the text and convert all words to lowercase. Tokenize the text based on word tokenizer.

```python
from nltk.tokenize import word_tokenize
ai_text = "Romeo and Juliet is a tragedy written by William Shakespeare. It is among the most popular plays ever written in the English language. The play revolves around two young star-crossed lovers whose deaths ultimately reconcile their feuding families."
lowercase_text = ai_text.lower()
tokens = word_tokenize(lowercase_text)
```

Remove stop words from the text using "english". Remove punctuation from the list of tokens. Finally report the number of tokens.

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

Implement stemming for theses tokens. Display the first five tokens in the stemmed_tokens.

```python
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(word) for word in tokens]
print(stemmed_tokens[:5])
```

Calculate frequency distribution of stemmed tokens. Print the token with the most frequency. 
```python
from nltk.probability import FreqDist

freq_dist = FreqDist(stemmed_tokens)
common_tokens = freq_dist.most_common(10)
common_tokens[0]
```

Visualize the cumulative frequency distribution with first ten most frequent tokens using a line chart with figsize=(12, 6).
```python
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
freq_dist.plot(10, cumulative=True)
plt.show()
```

Implement part-of-speech tagging for the tokens after the second step. Only display the sum of number of nouns, verbs and adjectives.

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

Based on previous pos tagging. Calculate the group(nouns, verbs, adjectives and adverbs) normalized frequency in tokens. Only display the highest frequency(Keep to two decimal places).


```python
adverb_count = sum(val for key, val in pos_counts.items() if key.startswith('R'))

normalized_nouns = round(noun_count / len(pos_tags), 2)
normalized_verbs = round(verb_count / len(pos_tags), 2)
normalized_adjectives = round(adjective_count / len(pos_tags), 2)
normalized_adverbs = round(adverb_count / len(pos_tags), 2)

# Calculate total number of tokens
max([normalized_nouns, normalized_verbs, normalized_adjectives, normalized_adverbs])
```