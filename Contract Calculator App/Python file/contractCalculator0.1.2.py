import tkinter as tk
from tkinter import ttk
import math

tick_values = {
    "EUR (M6E) – micro – 1.25 USD/tick": 1.25,
    "GBP (M6B) – micro – 0.625 USD/tick": 0.625,
    "AUD (M6A) – micro – 0.5 USD/tick": 0.5,
    "CAD (6C) – full – 10 USD/tick ⚠️": 10.0
}

def contractsCalculator(risk, tick_value, tick_to_sl):
    if tick_value == 0 or tick_to_sl == 0:
        return 0
    return math.floor(risk / (tick_value * tick_to_sl))

def on_instrument_change(event):
    instrument = combo_instrument.get()
    tick_value = tick_values.get(instrument, 0)
    label_tick_value.config(text=f"Tick value: {tick_value} USD")
    if "full" in instrument:
        label_warning.config(text="⚠️ Note: This is a full contract – more risk!")
    else:
        label_warning.config(text="")

def calculate():
    try:
        risk = float(entry_risk.get())
        ticks = int(entry_ticks.get())
        instrument = combo_instrument.get()
        tick_value = tick_values.get(instrument, 0)
        contracts = contractsCalculator(risk, tick_value, ticks)
        label_result.config(text=f'Number of contracts: {contracts}')
    except ValueError:
        label_result.config(text="Error: Please provide valid data.")

# GUI setup
root = tk.Tk()
root.title("Contracts Calculator")
root.geometry("400x350")
root.resizable(False, False)

frame = tk.Frame(root)
frame.pack(expand=True)

tk.Label(frame, text="Risk amount (USD):").pack(pady=(10, 0))
entry_risk = tk.Entry(frame, width=25, justify='center')
entry_risk.pack()

tk.Label(frame, text="Instrument:").pack(pady=(10, 0))
combo_instrument = ttk.Combobox(frame, values=list(tick_values.keys()), width=40, justify='center')
combo_instrument.pack()
combo_instrument.current(0)
combo_instrument.bind("<<ComboboxSelected>>", on_instrument_change)

label_tick_value = tk.Label(frame, text="Tick value: 1.25")
label_tick_value.pack(pady=(5, 0))

label_warning = tk.Label(frame, text="", fg="orange")
label_warning.pack(pady=(0, 10))

tk.Label(frame, text="Ticks to SL:").pack()
entry_ticks = tk.Entry(frame, width=25, justify='center')
entry_ticks.pack()

btn_calc = tk.Button(frame, text="Calculate", command=calculate, width=20)
btn_calc.pack(pady=15)

label_result = tk.Label(frame, text="Number of contracts: ", font=('Arial', 12, 'bold'))
label_result.pack()

root.mainloop()
