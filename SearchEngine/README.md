# 🔍 Mini Search Engine with Stack 

A **Mini Search Engine project** developed as part of my **2nd Semester DSA Lab Project (BS AI, NFC IET Multan)**.  
It demonstrates **core Data Structures and Algorithms (DSA)** concepts such as:  
- **Stack** (for search history navigation)  
- **Inverted Index / Hash Map** (for efficient keyword-based searching)  
- **String processing & searching algorithms**  
- **GPT Integration** → fallback when no local documents match  

---

## ✨ Features
- ✅ **Keyword-based Search** → finds documents containing query terms  
- ✅ **Ranked Results** → based on frequency of query terms  
- ✅ **Search History (UNDO)** → supports `back` command just like a browser  
- ✅ **Search History (REDO)** → supports `next` command just like a browser  
- ✅ **Document Viewer** → open `.txt` files directly from search results  
- ✅ **Automatic Crawler** → indexes all `.txt` files in the `documents/` folder  
- ✅ **GPT Fallback** → uses OpenAI GPT-3.5-Turbo when no local results found, saves responses in `gpt_docs/gpt.txt`  
- ✅ **Clean modular structure** for GitHub  

---

## 🗂️ Project Structure
```txt
Mini-Search-Engine/
│
├── stack.py          # Stack implementation (push, pop, peek, empty)
├── index.py          # Inverted Index implementation
├── search.py         # Search Engine logic + GPT integration
├── main.py           # Entry point for running the project
│
├── documents/        # Folder containing sample text files
│   ├── doc1.txt
│   ├── doc2.txt
│   └── ...
│
├── gpt_docs/         # Folder storing GPT responses
│   └── gpt.txt
│
├── .env              # Stores OPENAI_API_KEY
├── requirements.txt  # Required Python packages
└── README.md         # Project documentation
```
### ⚡ How It Works

+ The program scans the `documents/` folder and builds an inverted index.

+ When the user searches, queries are cleaned (lowercased, punctuation removed, split into words).

+ Matching documents are ranked by query word frequency.

+ The query is pushed onto the Stack (history).

+ If the user types `back`, the last query is popped and the previous one is shown again.

+ If no local document matches, the engine calls GPT, saves the result in `gpt_docs/gpt.txt`, indexes it, and shows it.

+ Users can open a result to see the full content of the file.

## ▶️ Usage

1. Go to base Dir:
```batch
cd SearchEngine
```
2. Run 
```batch
python main.py
```

***Example Session:***
```py
Loading index...
Index built with 5 documents.

Enter search query, 'back','next', 'show', or 'quit': ai
[Stack] Pushed: ai

Searching for: 'ai'
Found 1 document(s):
1. doc5.txt | Score: 2

Enter document number to open, or 'continue': continue

Enter search query, 'back','next', 'show', or 'quit': cs
[Stack] Pushed: cs

Searching for: 'cs'
No matches found in local documents. Using ChatGPT...
--- GPT Answer ---
CS is the study of computers and computational systems...
------------------
1. gpt.txt | Score: 1

Enter document number to open, or 'continue': 1
--- gpt.txt ---
CS is the study of computers and computational systems...
------------------

Enter search query, 'back','next', 'show', or 'quit': back
[Stack] Popped: cs
[Stack] Pushed: cs

Back to: 'ai'
1. doc5.txt | Score: 2

Enter search query, 'back','next', 'show', or 'quit': next
Redo: 'cs'
1. gpt.txt | Score: 1

Enter document number to open, or 'continue': continue
Enter search query, 'back','next', 'show', or 'quit': quit
Goodbye!
```

## 🏫 Academic Info

📖 Course: Data Structures & Algorithms (DSA)

🎓 Semester: 2nd Semester, BS Artificial Intelligence

🏛️ University: NFC IET Multan

👨‍💻 Student: Muawiya Amir

---
## 👥 Team Members

👨‍💻 Muawiya (Team Leader)

👨‍💻 M. Umar

---

## 🚀 Future Improvements

> Add synonym & fuzzy matching for queries

> Implement OR / NOT search operators

> Enhance ranking with TF-IDF instead of simple    counts

> Build a GUI or Web-based interface

> Maintain multiple GPT files (gpt_1.txt, gpt_2.txt, ...) to fully integrate undo/redo