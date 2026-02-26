# Flash Card Project

This is the starter code for the **Flash Card** project from the "100 Days of Code: The Complete Python Pro Bootcamp" course. The program helps you practice French vocabulary by displaying words on flash cards and allowing you to mark them as "known" or "unknown".

## How It Works

- Uses `tkinter` for the graphical user interface (GUI).
- Reads vocabulary from `data/french_words.csv` or, if available, a progress file `data/words_to_learn.csv`.
- Displays a French word on a card and automatically flips it to show the English translation after 3 seconds.
- Clicking the ✅ button marks a word as learned and removes it from the in‑memory list (it won’t be written to disk immediately).
- Clicking the ❌ button simply moves to the next word without removing it.
- When you close the window, a confirmation dialog asks whether to update your progress; if you agree the current word list is written to `data/words_to_learn.csv` so you can resume later.

## Project Structure

```
flash-card-project-start/
├── data/
│   ├── french_words.csv         # Original list of vocabulary
│   └── words_to_learn.csv       # Created/updated as you learn words
├── images/
│   ├── card_front.png
│   ├── card_back.png
│   ├── right.png
│   └── wrong.png
└── main.py                      # Entry point for the application
```

## Requirements

- Python 3.x
- `pandas` library
- Tkinter (usually included with standard Python installs)

You can install `pandas` using pip:

```bash
pip install pandas
```

## Running the App

1. Clone the repository or navigate to this directory.
2. Make sure the `data` and `images` folders are present.
3. Run the application:

```bash
python main.py
```

A window titled **Flashy** will open and begin showing flash cards.

## Notes

- The app will ask whether to save your progress when you close the window. If you choose yes, the remaining words are written to `data/words_to_learn.csv`.
- To completely reset progress, delete `data/words_to_learn.csv` and restart the app (or answer "No" at the prompt).
- You can edit `data/french_words.csv` to include your own words.
- A messagebox popup is used for the save confirmation; this requires the `tkinter.messagebox` module which is included with standard Python distributions.

## Customization Ideas

- Add additional languages or categories.
- Change the flip timer or add buttons to manually flip the card.
- Enhance the GUI with sounds or animations.

---

This simple tool is a great way to get comfortable with tkinter and basic data handling in Python while building a useful study aid.
