from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def extract_keywords(text, top_n=15):
    vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2))
    tfidf_matrix = vectorizer.fit_transform([text])
    scores = zip(
        vectorizer.get_feature_names_out(),
        np.asarray(tfidf_matrix.sum(axis=0)).ravel()
    )
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    return [word for word, score in sorted_scores[:top_n]]