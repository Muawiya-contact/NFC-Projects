# index.py
import string

class InvertedIndex:
    """A simple inverted index: word -> document -> frequency."""

    def __init__(self):
        # Dictionary to store index
        # Example: { "word": {"doc1": 2, "doc2": 1} }
        self.index = {}

    def add_doc(self, doc, text):
        """Add a document to the index."""
        # Convert text to lowercase and remove punctuation
        clean_text = text.lower().translate(str.maketrans('', '', string.punctuation))

        # Split text into words
        words = clean_text.split()

        for word in words:
            if word not in self.index:
                self.index[word] = {}
            # Count how many times a word appears in a document
            self.index[word][doc] = self.index[word].get(doc, 0) + 1

    def _clean_query(self, query):
        """Helper function to clean search queries."""
        query = query.lower().translate(str.maketrans('', '', string.punctuation))
        return query.split()

    def search(self, query):
        """Search for documents that contain all words in the query."""
        q_words = self._clean_query(query)
        if not q_words:
            return []

        # Start with documents containing the first word
        if q_words[0] not in self.index:
            return []
        results = set(self.index[q_words[0]].keys())

        # Keep only docs that contain all other words
        for word in q_words[1:]:
            if word not in self.index:
                return []
            results = results & set(self.index[word].keys())

        # Rank results by score (sum of word frequencies)
        ranked = []
        for doc in results:
            score = sum(self.index[word].get(doc, 0) for word in q_words)
            ranked.append({"doc": doc, "score": score})

        return sorted(ranked, key=lambda x: x["score"], reverse=True)
