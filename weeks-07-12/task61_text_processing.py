"""Task 61 - Text processing pipeline (cleaning -> tokenizing -> stopwords -> stemming -> n-grams)."""
import re, string
from collections import Counter

raw = """<p>Check https://navttc.gov.pk!! AI & Machine Learning courses in 2026 are GREAT, 
students @NAVTTC love them :) Contact: info@example.com</p>"""

def clean(t):
    t = re.sub(r"<.*?>", " ", t)                 # remove HTML
    t = re.sub(r"https?://\S+|\S+@\S+", " ", t)  # URLs / emails / handles
    t = re.sub(r"@\w+", " ", t)
    t = t.lower()
    t = re.sub(r"\d+", " ", t)                   # numbers
    t = t.translate(str.maketrans("", "", string.punctuation))
    return re.sub(r"\s+", " ", t).strip()

STOP = {"in", "are", "the", "a", "an", "and", "of", "to", "them", "love"}
def stem(w):
    for suf in ("ing", "ed", "es", "s"):
        if w.endswith(suf) and len(w) > len(suf) + 2: return w[:-len(suf)]
    return w

cleaned = clean(raw)
tokens = cleaned.split()
no_stop = [t for t in tokens if t not in STOP]
stems = [stem(t) for t in no_stop]
bigrams = list(zip(tokens, tokens[1:]))
print("Cleaned  :", cleaned); print("Tokens   :", tokens)
print("Stopwords removed:", no_stop); print("Stemmed  :", stems)
print("Bigrams  :", bigrams[:5]); print("Top words:", Counter(no_stop).most_common(3))

# Optional NLTK version
try:
    from nltk.stem import PorterStemmer
    print("NLTK Porter stems:", [PorterStemmer().stem(t) for t in no_stop])
except ImportError:
    print("(Install nltk for the NLTK stemmer: pip install nltk)")
