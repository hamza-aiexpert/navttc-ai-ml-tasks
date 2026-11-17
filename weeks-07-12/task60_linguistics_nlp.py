"""Task 60 - Linguistics / NLP with Python: tokenization, stop words, stemming,
lemmatization, POS tagging, Named Entities.
Uses NLTK when installed (pip install nltk); otherwise falls back to pure Python
so the script always runs."""
import re
from collections import Counter

text = ("Natural Language Processing helps computers understand human language. "
        "Google and Microsoft are building AI tools in Lahore, Pakistan. "
        "NAVTTC trains students to build intelligent applications.")

try:
    import nltk
    for pkg in ["punkt", "punkt_tab", "stopwords", "wordnet",
                "averaged_perceptron_tagger", "averaged_perceptron_tagger_eng",
                "maxent_ne_chunker", "maxent_ne_chunker_tab", "words"]:
        nltk.download(pkg, quiet=True)
    from nltk.tokenize import word_tokenize, sent_tokenize
    from nltk.corpus import stopwords
    from nltk.stem import PorterStemmer, WordNetLemmatizer
    NLTK = True
except Exception:
    NLTK = False
    print("[NLTK unavailable - using simple pure-Python fallback]\n")

if NLTK:
    sentences = sent_tokenize(text)
    tokens = word_tokenize(text)
    stops = set(stopwords.words("english"))
    words = [t for t in tokens if t.isalpha()]
    filtered = [w for w in words if w.lower() not in stops]
    stems = [PorterStemmer().stem(w) for w in filtered]
    lemmas = [WordNetLemmatizer().lemmatize(w.lower()) for w in filtered]
    print("POS tags:", nltk.pos_tag(tokens)[:10])
    print("Named entities:", nltk.ne_chunk(nltk.pos_tag(tokens)))
else:
    sentences = re.split(r"(?<=[.!?])\s+", text)
    tokens = re.findall(r"\w+|[^\w\s]", text)
    stops = {"the", "a", "an", "and", "are", "in", "to", "helps", "is", "of"}
    words = [t for t in tokens if t.isalpha()]
    filtered = [w for w in words if w.lower() not in stops]
    stems = [re.sub(r"(ing|ed|es|s)$", "", w.lower()) for w in filtered]
    lemmas = stems

print("Sentences:", len(sentences))
print("Tokens   :", tokens)
print("No stopwords:", filtered)
print("Stems    :", stems)
print("Lemmas   :", lemmas)
print("Word frequency:", Counter(w.lower() for w in words).most_common(5))
