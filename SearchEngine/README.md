# 🔍 Mini Search Engine

A simple **Search Engine project** built as part of my **2nd Semester DSA Lab Project (BS AI, NFC IET Multan)**.  
It demonstrates core **Data Structures and Algorithms concepts** such as **hash tables, string processing, searching, and modular coding**.

---

## 📌 Features
- ✅ Store and retrieve web pages using **Hash Tables**  
- ✅ Search queries with **best keyword matching**  
- ✅ Support for **multiple results** with user choice  
- ✅ Update and delete existing page links  
- ✅ Organized into **modular files** (`search_engine.py`, `main.py`)  
- ✅ Example usage in the `examples/` folder  

---

## 🗂️ Project Structure
```txt
NFC-Search-Engine/
│
├── search_engine.py # Core SearchEngine class implementation
├── main.py # Main program (semester project runner)
│
├── examples/ # Example usage (optional demos)
│ └── demo.py
│
└── README.md # Project documentation
```

---

## ⚡ How It Works
1. Pages are added with a **keyword → link** mapping.  
2. A **hash function** stores them in a fixed-size hash table.  
3. The user can search with any query:  
   - If one best match → the page opens directly.  
   - If multiple matches → a numbered menu appears for choice.  
4. Extra features:
   - `update_page(keyword, new_link)` → update existing link.  
   - `delete_page(keyword, link)` → delete specific page link.  

---

## ▶️ Usage

### Run the main program:
```bash
python main.py
```
## Example Search
```python
Please, Enter any query to search:  nfc and ai
Multiple results found:
1. ai → https://en.wikipedia.org/wiki/Artificial_intelligence
2. nfc → https://www.nfciet.edu.pk/
3. ai_department → https://www.nfciet.edu.pk/bs-artificial-intelligence/
```

## 🏫 Academic Info
- 📖 **Course**: Data Structures & Algorithms (DSA)  
- 🎓 **Semester**: 2nd Semester, BS Artificial Intelligence  
- 🏛️ **University**: NFC IET Multan  
- 👨‍💻 **Student**: Muawiya  

---
## 👥 Team Members
- 👨‍💻 **Muawiya** (Team Leader)  
- 👨‍💻 M. Umar  
- 👨‍💻 Hassan Khan  

---
## 🚀 Future Improvements
- Add **ranking system** for results (frequency & relevance).  
- Build a **GUI or Web-based interface**.  
- Support **export/import** of stored links.  

---
