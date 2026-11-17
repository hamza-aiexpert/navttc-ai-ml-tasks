"""Task 62 - Text analysis: Bag-of-Words, TF-IDF, document similarity and a sentiment classifier."""
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

docs = ["Machine learning is fun and powerful",
        "Deep learning is a part of machine learning",
        "I love eating fresh mangoes in summer",
        "Mangoes and apples are tasty fruits"]

bow = CountVectorizer(stop_words="english"); B = bow.fit_transform(docs)
print("Bag of Words:\n", pd.DataFrame(B.toarray(), columns=bow.get_feature_names_out()), "\n")

tfidf = TfidfVectorizer(stop_words="english"); T = tfidf.fit_transform(docs)
print("Document similarity (cosine, TF-IDF):\n",
      pd.DataFrame(cosine_similarity(T).round(2), index=range(4), columns=range(4)), "\n")

# Tiny sentiment classifier
data = [(t,1) for t in ['great course very useful', 'excellent teacher and clear lectures', 'I loved the practical labs', 'really helpful and well organised', 'amazing content easy to follow', 'fantastic experience I learned a lot', 'the labs were excellent and useful', 'clear and helpful teacher', 'great practical content and good support', 'I enjoyed the course and learned a lot', 'very well organised and easy lectures', 'excellent support and great labs', 'useful content and amazing teacher', 'good explanation and clear examples', 'I loved the great practical projects', 'helpful lectures and fantastic labs', 'easy to follow and well explained', 'the teacher was great and the content useful']] + [(t,0) for t in ['boring and confusing lectures', 'waste of time', 'terrible internet and poor support', 'very bad explanation', 'disappointing and too slow', 'I hated the confusing assignments', 'the lectures were boring and slow', 'poor content and bad teacher', 'terrible labs and confusing examples', 'I did not learn anything it was a waste', 'bad support and slow internet', 'confusing and badly organised course', 'boring content and poor explanation', 'the labs were terrible and confusing', 'disappointing teacher and bad lectures', 'slow lectures and poor organisation', 'I hated the boring and slow classes', 'useless course and terrible support']]
X, y = zip(*data)
from sklearn.model_selection import cross_val_score
clf = make_pipeline(TfidfVectorizer(), LogisticRegression())
scores = cross_val_score(clf, X, y, cv=6)   # dataset is tiny, so use cross-validation
print("Sentiment 6-fold CV accuracy:", scores.round(2), "mean =", round(scores.mean(), 2))
clf.fit(X, y)
for s in ["the labs were excellent", "boring and terrible class"]:
    print(f"'{s}' ->", "positive" if clf.predict([s])[0] else "negative")
