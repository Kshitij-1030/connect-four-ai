# Connect Four AI 

An AI-powered Connect Four project that combines a **Minimax agent with alpha-beta pruning**, **gameplay simulation** vs. random agents, an **interactive GUI**, and **data-driven strategy analysis** using Python, pandas, and matplotlib.

---

##  Features

- Rule-Based AI (Minimax with Alpha-Beta Pruning)
- GUI to play Connect Four against the AI (Tkinter)
- 1000-game simulation: AI vs Random player
- Visual and statistical analysis using Jupyter Notebook
- Attempted machine learning agent (discontinued due to poor accuracy)

---

##  Project Structure

```
├── connect_four_gui.py              # GUI using Tkinter
├── game.py                          # Game board logic
├── rule_based.py                    # Minimax agent logic
├── random_vs_ai.py                  # Game simulator
├── random_vs_ai.csv                 # Output of 1000 simulated games
├── connect_four_analysis_and_modelling.ipynb  # Analysis & ML notebook
└── README.md                        # You are here
```

---

## How to Run

### 1. Play the game (human vs AI)
```bash
python connect_four_gui.py
```

### 2. Run game simulations
```bash
python random_vs_ai.py
```

### 3. View insights
Open the notebook:
```
connect_four_analysis_and_modelling.ipynb
```

---

## Sample from Simulation Data (`random_vs_ai.csv`)

| Game | Move_Num | Player | Move | Winner | Board_State     |
|------|----------|--------|------|--------|------------------|
| 1    | 1        | 1      | 3    | -1     | [0, 0, ..., 0]   |
| 1    | 2        | -1     | 2    | -1     | [0, 0, ..., 1]   |

---

## Credits

- Minimax + Alpha Beta pruning logic was **inspired by** [zakuraevs/connect4-ai](https://github.com/zakuraevs/connect4-ai).
- Built as the final project for *COMP 255: Artificial Intelligence & Machine Learning* at Wheaton College (Spring 2025).

---

## 📜 License

MIT License. Free to use, modify, and distribute with credit.
