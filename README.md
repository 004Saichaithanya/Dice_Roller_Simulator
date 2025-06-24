# 🎲 Suspense Dice Roller 🎲

A fun Python terminal application that simulates the roll of a standard six-sided die, complete with a suspenseful animated countdown using dice face emojis before revealing the result!

---

## 📌 Approach

The program waits for the user to press **Enter** to roll the dice. It then creates a rolling animation by displaying random dice face emojis in quick succession to mimic the feel of a real dice roll. Finally, it generates a random number between 1 and 6 and displays the corresponding dice emoji along with a fun emoji for a lively experience. The user can choose to roll again or exit.

---

## 📦 Libraries Used

| Library  | Purpose                                                           |
| :------- | :---------------------------------------------------------------- |
| `random` | To generate random numbers and select random emojis for animation |
| `time`   | To add delays between animation frames for suspense               |

*Both libraries are built-in Python standard libraries — no external installation required.*

---

## 🎮 How to Run

1. **Clone or Download** the project to your local system.
2. Open a terminal in the project directory.
3. Run the following command:

   ```bash
   python dice_roller.py
   ```
4. Follow the prompts in the terminal — press **Enter** to roll, and **y/n** to roll again or quit.

---

## ✨ Sample Output

![image](https://github.com/user-attachments/assets/9fd0c476-6459-4c56-8854-8794218578d9)


---

## 📌 Features

* Random dice number generation.
* Rolling animation using dice face emojis ⚀⚁⚂⚃⚄⚅.
* Fun emojis on result for a cheerful experience 🎲🎉.
* Option to continue rolling or exit.

---

## 💡 Future Ideas

* Add sound effects during the roll.
* Create a simple GUI using Tkinter.
