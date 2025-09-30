# search.py
import os
from stack import Stack
from index import InvertedIndex

# Path to the folder that has all text files
PATH = "./documents" # First we go to base dir

class SearchSim:
    """A simple search engine simulation."""

    def __init__(self, path=PATH):
        self.index = InvertedIndex()   # for word search
        self.history = Stack()         # to store search history
        self.path = path               # folder path
        self.results = []              # last search results
        self._load()                   # load documents into index

    def _load(self):
        """Load all text files and build the index."""
        print("Loading index...")
        try:
            files = [f for f in os.listdir(self.path) if f.endswith(".txt")]
            if not files:
                print("No .txt files found in documents folder.")
            for f in files:
                doc = os.path.splitext(f)[0]  # filename without .txt
                with open(os.path.join(self.path, f), "r", encoding="utf-8") as file:
                    self.index.add_doc(doc, file.read())
            print(f"Index built with {len(files)} documents.")
        except FileNotFoundError:
            print("Documents folder not found!")
            exit()

    def run(self):
        """Main loop for user interaction."""
        while True:
            user_input = input("\nEnter search query, 'back', 'show', or 'quit': ").strip().lower()

            if user_input == "quit":
                print("Goodbye!")
                break
            elif user_input == "back":
                self._back()
            elif user_input == "show":
                self.history.show()
            elif user_input:   # if user typed something
                self._search(user_input)

    def _search(self, query):
        """Handle search queries."""
        self.history.push(query)
        print(f"\nSearching for: '{query}'")

        self.results = self.index.search(query)
        if not self.results:
            print("No matches found.")
            return

        print(f"Found {len(self.results)} document(s):")
        for i, r in enumerate(self.results, start=1):
            print(f"{i}. {r['doc']}.txt | Score: {r['score']}")

        self._open_doc()

    def _open_doc(self):
        """Open and show the contents of a selected document."""
        while True:
            choice = input("\nEnter document number to open, or 'next': ").strip().lower()
            if choice == "next":
                break
            try:
                num = int(choice)
                if 1 <= num <= len(self.results):
                    doc = self.results[num - 1]["doc"]
                    with open(os.path.join(self.path, f"{doc}.txt"), "r", encoding="utf-8") as f:
                        print(f"\n--- {doc}.txt ---\n{f.read()}\n------------------")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a valid number or 'next'.")
            except FileNotFoundError:
                print("File not found.")

    def _back(self):
        """Go back to the previous search query."""
        if len(self.history.items) <= 1:
            print("No previous search available.")
            return

        self.history.pop()   # remove current search
        prev_query = self.history.peek()  # last one left
        print(f"\nBack to: '{prev_query}'")

        self.results = self.index.search(prev_query)
        if not self.results:
            print("No matches found.")
        else:
            for i, r in enumerate(self.results, start=1):
                print(f"{i}. {r['doc']}.txt | Score: {r['score']}")
            self._open_doc()
