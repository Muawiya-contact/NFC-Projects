# main.py
from search_engine import SearchEngine

s = SearchEngine(10)

# Adding AI-related pages
s.add_page("ai", "https://en.wikipedia.org/wiki/Artificial_intelligence")
s.add_page("ai", "https://www.ibm.com/cloud/learn/what-is-artificial-intelligence")
s.add_page("ai", "https://www.sciencedaily.com/news/computers_math/artificial_intelligence/")

# Machine Learning
s.add_page("ml", "https://en.wikipedia.org/wiki/Machine_learning")
s.add_page("ml", "https://www.geeksforgeeks.org/machine-learning/")
s.add_page("ml", "https://www.coursera.org/learn/machine-learning")

# Python
s.add_page("python", "https://www.python.org")
s.add_page("python", "https://docs.python.org/3/tutorial/")
s.add_page("python", "https://realpython.com/")

# Data Science
s.add_page("datascience", "https://en.wikipedia.org/wiki/Data_science")
s.add_page("datascience", "https://www.datacamp.com/")
s.add_page("datascience", "https://towardsdatascience.com/")

# NFC IET Multan & AI Department
s.add_page("nfc", "https://www.nfciet.edu.pk/")
s.add_page("nfc", "https://en.wikipedia.org/wiki/NFC_Institute_of_Engineering_and_Technology")
s.add_page("ai_department", "https://www.nfciet.edu.pk/bs-artificial-intelligence/")
s.add_page("ai_department", "https://www.nfciet.edu.pk/computer-science-department/")  

# Run search
s.search()
