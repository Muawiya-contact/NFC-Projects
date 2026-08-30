# Mini Search Engine with Stack

A command-line search engine over local text files, built as a 2nd semester
DSA lab project (BS AI, NFC IET Multan). It uses an inverted index (hash map)
for keyword search, two stacks for browser-style undo/redo of queries, and
falls back to OpenAI GPT-3.5-turbo when no local document matches.

## How it works

- On startup, every `.txt` file in `documents/` is indexed into an inverted
  index mapping `word -> {document: frequency}` (lowercased, punctuation
  stripped).
- A query matches documents containing all of its words; results are ranked
  by the summed frequency of the query words.
- Each query is pushed onto a history stack. `back` pops it to return to the
  previous query (undo), `next` redoes an undone one, and `show` prints the
  history stack. A new search clears the redo stack.
- If nothing matches locally, the query is sent to GPT-3.5-turbo. The answer
  is saved as `gpt_docs/gpt_N.txt`, added to the index, and shown as a result.
- After each search you can type a result number to print the file's contents,
  or `continue` to keep searching. `quit` exits.

## Files

- `main.py` - entry point
- `search.py` - search loop, undo/redo, GPT fallback
- `index.py` - inverted index (add, clean, search, rank)
- `stack.py` - list-based stack (push, pop, peek, show)
- `documents/` - sample text files to index
- `gpt_docs/` - saved GPT answers (`gpt_1.txt`, `gpt_2.txt`, ...)

## Running

Requires Python 3.12+ and an OpenAI API key.

```
cd SearchEngine
pip install -r requirements.txt
echo "OPENAI_API_KEY=sk-..." > .env
python main.py
```

The key is required even for local-only searches, since it is loaded at
startup.

## Credits

Course: Data Structures & Algorithms, 2nd Semester, BS Artificial
Intelligence, NFC IET Multan.

Team: Muawiya Amir (team leader), M. Umar.
