# examples/demo.py
from search_engine import SearchEngine

def run_demo():
    s = SearchEngine(5)
    s.add_page("python", "https://www.python.org")
    s.add_page("ml", "https://en.wikipedia.org/wiki/Machine_learning")
    s.add_page("ai", "https://en.wikipedia.org/wiki/Artificial_intelligence")

    print("\nNow searching for 'ai and python':")
    s.search()

if __name__ == "__main__":
    run_demo()
