# search.py
import os
from stack import Stack
from index import InvertedIndex

class SearchSim:
    """Search engine simulation using Inverted Index + Stack (for history)."""

    def __init__(self, path="./"):
        self.index = InvertedIndex()
        self.history = Stack()
        self.path = path
        self.results = []
        self._load()

    def _load(self):
        print("Building index...")
        try:
            files = [f for f in os.listdir(self.path) if f.endswith(".txt")]
            if not files:
                print("No .txt files in documents/")
            for f in files:
                doc = os.path.splitext(f)[0]
                with open(os.path.join(self.path, f), "r", encoding="utf-8") as file:
                    self.index.add_doc(doc, file.read())
            print(f"Index built with {len(files)} docs.")
        except FileNotFoundError:
            print("documents/ folder not found.")
            exit()

    def run(self):
        while True:
            user_input = input("\nEnter search query, 'back', 'show', or 'quit': ").strip()
            if user_input.lower() == "quit":
                break
            elif user_input.lower() == "back":
                self._back()
            elif user_input.lower() == "show":
                self.history.show()
            else:
                self._search(user_input)

    def _search(self, q):
        self.history.push(q)
        print(f"\nSearching: '{q}'")
        self.results = self.index.search(q)

        if not self.results:
            print("No matches.")
            return

        print(f"Found {len(self.results)} docs:")
        for i, r in enumerate(self.results, 1):
            print(f"{i}. {r['doc']}.txt | Score: {r['score']}")

        self._open_doc()

    def _open_doc(self):
        while True:
            sel = input("\nEnter doc number to open, or 'next': ").strip().lower()
            if sel == "next":
                break
            try:
                i = int(sel)
                if 1 <= i <= len(self.results):
                    doc = self.results[i - 1]["doc"]
                    with open(os.path.join(self.path, f"{doc}.txt"), "r", encoding="utf-8") as f:
                        print(f"\n--- {doc}.txt ---\n{f.read()}\n------------------")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Enter a number or 'next'.")
            except FileNotFoundError:
                print("File not found.")

    def _back(self):
        if len(self.history.items) <= 1:
            print("No previous search.")
            return
        self.history.pop()
        prev = self.history.peek()
        print(f"\nBack to: '{prev}'")
        self.results = self.index.search(prev)
        if not self.results:
            print("No matches.")
        else:
            for i, r in enumerate(self.results, 1):
                print(f"{i}. {r['doc']}.txt | Score: {r['score']}")
            self._open_doc()
