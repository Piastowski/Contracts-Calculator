📊 Contracts Calculator
A simple and intuitive desktop app built with Python and Tkinter to help futures traders calculate the optimal number of contracts based on their risk tolerance, stop-loss size (in ticks), and instrument selection.
🛠 Features
•	Supports multiple instruments with defined tick values:
o	EUR (M6E) – micro – 1.25 USD/tick
o	GBP (M6B) – micro – 0.625 USD/tick
o	AUD (M6A) – micro – 0.5 USD/tick
o	CAD (6C) – full – 10 USD/tick ⚠️
•	Highlights higher risk when full contracts are selected
•	Real-time calculation of contract quantity based on:
o	Risk in USD
o	Tick value (auto-filled from selected instrument)
o	Stop-loss size in ticks
•	Simple, clean, and responsive GUI
•	Error handling for invalid inputs

🧮 Formula Used
contracts = floor(risk / (tick_value * stop_loss_in_ticks))

🚀 Getting Started
1.	Make sure you have Python 3 installed.
2.	Clone the repo or download the script.
3.	Install tkinter (if not already available).
4.	Run the script:
python contracts_calculator.py
Optionally, add your own Contract-Calculator-Icon.ico for a custom window icon.

📦 Dependencies
•	Python 3
•	Tkinter (standard with most Python installations)
•	math (built-in)

⚠️ Disclaimer
This tool is for educational and personal use only. Always double-check your calculations before placing real trades.
