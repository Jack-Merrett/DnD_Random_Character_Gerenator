# 🐉 Dungeons & Dragons Character Generator

This is a Python-based random character generator for **Dungeons & Dragons 5e**. It generates a new character with:

- 🎭 Race  
- 🛡️ Class  
- ⚖️ Alignment  
- 📊 Ability Scores (STR, DEX, CON, INT, WIS, CHA)

Great for quick one-shots, NPC creation, or when inspiration is running low!

---

## 📦 Features

- Uses Python's built-in `random` module  
- Classic D&D-style ability score generation (4d6 drop lowest)  
- Outputs character info in a clean, vertical YAML-style format  
- Easy to read, easy to expand  

---

## 🚀 How to Run

1. Clone this repository or download the script:

    ```bash
    git clone https://github.com/your-username/dnd-character-generator.git
    cd dnd-character-generator
    ```

2. Run the script:

    ```bash
    python character_generator.py
    ```

3. Sample output:

    ```
    🧙 Race: Half-Elf  
    ⚔️ Class: Ranger  
    ⚖️ Alignment: Lawful Neutral  

    📊 Ability Scores:
    STR: 14  DEX: 15  CON: 13  INT: 12  WIS: 10  CHA: 11  
    ```

---

## 🧠 How It Works

- **Race**, **Class**, and **Alignment** are chosen randomly from preset lists.  
- **Ability Scores** are calculated using the classic "4d6 drop lowest" method.  
- All output is printed in a vertical, human-readable format.

---

## 🧰 Tech Stack

- Python 3.6 or higher  
- No external libraries required  

---

## 🛠️ Customize It

Want to add homebrew races, classes, or house rules? Just edit the lists in the script:

```python
races = ["Elf", "Dwarf", "Dragonborn", "Half-Elf", "Human", "Tiefling"]
classes = ["Fighter", "Wizard", "Rogue", "Cleric", "Paladin", "Ranger"]
alignments = ["Lawful Good", "Neutral", "Chaotic Evil", ...]
```

---

## 📜 License
This project is licensed under the MIT License.

---

## ✨ Credits
Created by Jack Merrett.
Inspired by dice, dragons, and the need for speed (in character creation).

