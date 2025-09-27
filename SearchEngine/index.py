# index.py
import string

class InvertedIndex:
    """Inverted Index for storing word → doc → frequency."""

    def __init__(self):
        self.index = {}

    def add_doc(self, doc, text):
        text = text.lower().translate(str.maketrans('', '', string.punctuation))
        words = [w.strip() for w in text.split() if w.strip()]
        for w in words:
            if w not in self.index:
                self.index[w] = {}
            self.index[w][doc] = self.index[w].get(doc, 0) + 1

    def search(self, query):
        q_words = self._clean_query(query)
        if not q_words:
            return []

        if q_words[0] not in self.index:
            return []
        results = set(self.index[q_words[0]].keys())

        for w in q_words[1:]:
            if w not in self.index:
                return []
            results &= set(self.index[w].keys())

        ranked = []
        for doc in results:
            score = sum(self.index[w].get(doc, 0) for w in q_words)
            ranked.append({"doc": doc, "score": score})

        return sorted(ranked, key=lambda x: x["score"], reverse=True)

    def _clean_query(self, query):
        query = query.lower().translate(str.maketrans('', '', string.punctuation))
        return [w.strip() for w in query.split() if w.strip()]
