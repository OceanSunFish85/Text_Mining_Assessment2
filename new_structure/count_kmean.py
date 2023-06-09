import os
import numpy as np
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import silhouette_score, adjusted_rand_score

# the data should include in pos_data_strategy folder
data_folder = r'D:\textmining lab demo\Assessment2\Assignment2BlogData\pos_data_strategy\sub_dir_obj\male'

# read data
documents = []
for file in os.listdir(data_folder):
    if file.endswith('.txt'):
        file_path = os.path.join(data_folder, file)
        with open(file_path, 'r', encoding='utf-8') as f:
            document = f.read()
            documents.append(document)

# create count vectorizer
vectorizer = CountVectorizer()
features = vectorizer.fit_transform(documents)
feature_names = vectorizer.get_feature_names_out()

# k class number
num_clusters = 2

# create k-means model
kmeans = KMeans(n_clusters=num_clusters, random_state=42)

# apply clustering
kmeans.fit(features)

# get label
labels = kmeans.labels_

# calculate sample frequency
cluster_word_counts = np.zeros((num_clusters, len(feature_names)))
for i, label in enumerate(labels):
    document_words = documents[i].split()
    for word in document_words:
        word_indices = np.where(feature_names == word)[0]
        if len(word_indices) > 0:
            word_index = word_indices[0]
            cluster_word_counts[label][word_index] += 1

# calculate top topic
top_keywords_per_cluster = []
for cluster in range(num_clusters):
    cluster_word_freqs = cluster_word_counts[cluster]
    top_keyword_indices = cluster_word_freqs.argsort()[-2:][::-1]
    top_keywords = [feature_names[index] for index in top_keyword_indices]
    top_keywords_per_cluster.append(top_keywords)

# print result
for cluster, keywords in enumerate(top_keywords_per_cluster):
    print("Cluster:", cluster)
    print("Top Keywords:", ', '.join(keywords))
    print("-----------------------------")

# assume true label
true_labels = [0, 0, 1, 1, 1]

# calculate silhouette score
silhouette_avg = silhouette_score(features, labels)
print("Average Silhouette Score:", silhouette_avg)
