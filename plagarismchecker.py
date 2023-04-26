import string
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')

def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))
    
    # Tokenize text into words
    words = nltk.word_tokenize(text)
    
    # Remove stop words
    stop_words = set(nltk.corpus.stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    
    # Join words into a string
    text = " ".join(words)
    
    return text

def check_plagiarism(text1, text2):
    # Preprocess text
    text1 = preprocess_text(text1)
    text2 = preprocess_text(text2)
    
    # Create vectorizer
    vectorizer = TfidfVectorizer()
    
    # Fit and transform vectorizer on the two texts
    tfidf1 = vectorizer.fit_transform([text1])
    tfidf2 = vectorizer.transform([text2])
    
    # Calculate cosine similarity between the two texts
    similarity = cosine_similarity(tfidf1, tfidf2)[0][0]
    
    return similarity

# Example usage
text1 = "The quick brown fox jumps over the lazy dog."
text2 = "A quick brown dog jumps over the lazy fox."
similarity = check_plagiarism(text1, text2)
print(f"Similarity: {similarity:.2f}")
