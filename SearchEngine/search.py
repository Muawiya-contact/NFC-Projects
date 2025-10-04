# search.py
import os
from stack import Stack
from index import InvertedIndex
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables!")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Folders
DOC_PATH = "./documents"       # local documents folder
GPT_PATH = "./gpt_docs"        # folder to store GPT results
os.makedirs(GPT_PATH, exist_ok=True)

class SearchSim:
    """Hybrid Search Engine: local + GPT fallback with proper undo/redo."""

    def __init__(self, doc_path=DOC_PATH, gpt_path=GPT_PATH):
        self.index = InvertedIndex()
        self.history = Stack()
        self.redo = Stack()
        self.doc_path = doc_path
        self.gpt_path = gpt_path
        self.results = []
        self.gpt_counter = self._init_gpt_counter()
        self._load_docs()

    def _init_gpt_counter(self):
        """Find the last GPT file number to continue numbering."""
        files = [f for f in os.listdir(self.gpt_path) if f.startswith("gpt_") and f.endswith(".txt")]
        numbers = [int(f.split("_")[1].split(".")[0]) for f in files if f.split("_")[1].split(".")[0].isdigit()]
        return max(numbers, default=0) + 1

    def _load_docs(self):
        """Load local text files into index."""
        print("Building index from local documents...")
        try:
            files = [f for f in os.listdir(self.doc_path) if f.endswith(".txt")]
            for f in files:
                doc_name = os.path.splitext(f)[0]
                with open(os.path.join(self.doc_path, f), "r", encoding="utf-8") as file:
                    self.index.add_doc(doc_name, file.read())
            print(f"Index built with {len(files)} documents.")
        except FileNotFoundError:
            print("Documents folder not found! Make sure './documents' exists.")
            exit()

    def run(self):
        """Main loop for user input."""
        while True:
            user_input = input("\nEnter search query, 'back', 'next', 'show', or 'quit': ").strip()
            if not user_input:
                continue
            cmd = user_input.lower()
            if cmd == "quit":
                print("Goodbye!")
                break
            elif cmd == "back":
                self._back()
            elif cmd == "next":
                self._next()
            elif cmd == "show":
                self.history.show()
            else:
                self._search(user_input)

    def _search(self, query):
        self.history.push(query)
        self.redo = Stack()  # clear redo stack
        print(f"\nSearching for: '{query}'")

        # Search local docs first
        self.results = self.index.search(query)

        # If not found locally, ask GPT
        if not self.results:
            print("No matches found locally. Using ChatGPT...")
            filename = f"gpt_{self.gpt_counter}.txt"
            answer = self._ask_chatgpt(query)
            filepath = os.path.join(self.gpt_path, filename)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(answer)
            self.index.add_doc(filename.replace(".txt", ""), answer)
            self.results = [{"doc": filename.replace(".txt", ""), "score": 1}]
            print(f"\n--- GPT Answer ---\n{answer}\n------------------")
            self.gpt_counter += 1

        # Show results
        for i, r in enumerate(self.results, start=1):
            print(f"{i}. {r['doc']}.txt | Score: {r['score']}")
        self._open_doc()

    def _ask_chatgpt(self, query):
        """Query GPT using OpenAI client."""
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": query}],
                temperature=0.7,
                max_tokens=200
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error accessing ChatGPT: {e}"

    def _open_doc(self):
        """Open and display selected document."""
        while True:
            choice = input("\nEnter document number to open, or 'continue': ").strip().lower()
            if choice == "continue":
                break
            try:
                num = int(choice)
                if 1 <= num <= len(self.results):
                    doc = self.results[num - 1]["doc"]
                    path = self.gpt_path if doc.startswith("gpt_") else self.doc_path
                    with open(os.path.join(path, f"{doc}.txt"), "r", encoding="utf-8") as f:
                        print(f"\n--- {doc}.txt ---\n{f.read()}\n------------------")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Enter a valid number or 'continue'.")
            except FileNotFoundError:
                print("File not found.")

    def _back(self):
        """Undo: go back to previous query."""
        if len(self.history.items) <= 1:
            print("No previous search available.")
            return
        current = self.history.pop()
        self.redo.push(current)
        prev_query = self.history.peek()
        print(f"\nBack to: '{prev_query}'")
        self.results = self.index.search(prev_query)
        self._open_doc()

    def _next(self):
        """Redo the last undone query."""
        if self.redo.empty():
            print("Nothing to redo!")
            return
        redo_query = self.redo.pop()
        self.history.push(redo_query)
        print(f"\nRedo: '{redo_query}'")
        self.results = self.index.search(redo_query)
        self._open_doc()
