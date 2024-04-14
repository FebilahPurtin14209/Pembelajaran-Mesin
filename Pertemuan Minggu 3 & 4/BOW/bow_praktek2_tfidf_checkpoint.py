# -*- coding: utf-8 -*-
"""BOW-Praktek2-tfidf-checkpoint.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mnpue9mzC7J_vJ7OS0LVMu6J_l3dK6pD

Praktek TF-IDF
=============================

**Modul untuk Pembelajaran Analitika Media Sosial**

**Author:** *Dr. Eng. Farrikh Alzami, M.Kom*, *Abu Salam, M.Kom*

Program Studi Sistem Informasi S1

***Universitas Dian Nuswantoro 2021***
"""

import pandas as pd
import numpy as np

dataset = pd.read_csv('clean_dataset_stem.csv',sep=';')

dataset_feature = dataset['ProcessedText'].astype(str)

dataset.shape

dataset_label = dataset['Sentimen']

"""# cek distribusi label"""

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

# Visualizing the target variable
plt.figure(figsize=(12,8))
sns.distplot(dataset_label, label=f'target, skew: {dataset_label.skew():.2f}')
plt.legend(loc='best')
plt.show()

dataset_label.value_counts()

"""# TF-IDF"""

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(dataset_feature)

print(X)

print(X.shape)

print(vectorizer.get_feature_names_out())