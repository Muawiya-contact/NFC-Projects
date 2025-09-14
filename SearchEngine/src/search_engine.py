import webbrowser as web , string as st

class SearchEngine:
    def __init__(self,size):
        self.size = size
        self.table = [[] for _ in range(size)]
        
    # 1 For Hash Table
    def hash_function(self,key):
        return sum(ord(c) for c in key) % self.size
        
    # 2 To add pages
    def add_page(self,key,link):
        key = key.lower()
        index = self.hash_function(key)
        self.table[index].append((key,link))
        print(f"Added: {key} to {link}")

    # 3 Best Match
    def find_best_match(self, query):
        q = query.lower().translate(str.maketrans("", "", st.punctuation))
        words = q.split()
        matches = []

        for w in words:
            index = self.hash_function(w)
            for k, link in self.table[index]:
                if k == w and k not in matches:
                    matches.append(k)

        return matches if matches else None

    # 4 Search for class Use
    def ser(self, k):
        index = self.hash_function(k)
        results = []
        for key, val in self.table[index]:
            if key == k:
                results.append(val)
        return results if results else None


    # 5 Search from obj
    def search(self):
        query = input("Please, Enter any query to search: ")
        best_keywords = self.find_best_match(query)
        if best_keywords:
            options = []
            if len(best_keywords) == 1:
                best_keyword = best_keywords[0]
                index = self.hash_function(best_keyword)
                for k, link in self.table[index]:
                    if k == best_keyword:
                        print(f"Opening the best match for '{query}' : {k} is {link}")
                        return web.open(link)
            else:
                print("Multiple results found:")
                for i, k in enumerate(best_keywords, start=1):
                    links = self.ser(k)
                    if links:
                        for link in links:
                            options.append((k, link))
                # show all options with numbers
                for idx, (k, link) in enumerate(options, start=1):
                    print(f"{idx}. {k} → {link}")
                # ask user
                choice = int(input("Enter the option number to open: ")) - 1
                if 0 <= choice < len(options):
                    chosen_key, chosen_link = options[choice]
                    print(f"Opening: {chosen_key} → {chosen_link}")
                    return web.open(chosen_link)
                else:
                    print("Invalid choice.")
        else:
            print(f"No relevant result is found for: {query}")

            
    # 6 Update page link for a keyword
    def update_page(self, keyword, new_link):
        keyword = keyword.lower()
        index = self.hash_function(keyword)
        for i, (k, link) in enumerate(self.table[index]):
            if k == keyword:
                self.table[index][i] = (k, new_link)
                print(f"Updated: {keyword} → {new_link}")
                return  print(f"Keyword '{keyword}' not found, cannot update.")
       

    # 7 Delete a specific link for a keyword
    def delete_page(self, keyword, link):
        keyword = keyword.lower()
        index = self.hash_function(keyword)
        for (k, l) in self.table[index]:
            if k == keyword and l == link:
                self.table[index].remove((k, l))
                print(f"Deleted: {keyword} is {link}")
                return print(f"Keyword '{keyword}' with link '{link}' not found, cannot delete.")
        

