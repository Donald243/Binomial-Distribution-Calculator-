import tkinter as tk
from tkinter import messagebox
from math import comb
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def calculate_binomial():
    try:
        # Get inputs
        n = int(entry_n.get())
        p = float(entry_p.get())
        k = int(entry_k.get())

        # Validate inputs
        if n < 0 or k < 0 or k > n or not (0 <= p <= 1):
            raise ValueError("Invalid inputs. Ensure: n >= 0, 0 <= k <= n, and 0 <= p <= 1.")

        # Calculate binomial probability
        probability = comb(n, k) * (p ** k) * ((1 - p) ** (n - k))
        label_result.config(text=f"P(X = {k}) = {probability:.5f}")

        # Plot the binomial distribution
        x_values = list(range(n + 1))
        y_values = [comb(n, x) * (p ** x) * ((1 - p) ** (n - x)) for x in x_values]
        ax.clear()
        ax.bar(x_values, y_values, color='blue', alpha=0.7)
        ax.set_title("Binomial Distribution")
        ax.set_xlabel("Number of Successes (k)")
        ax.set_ylabel("Probability")
        canvas.draw()
    
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("Binomial Distribution Calculator")

# Input fields
frame_inputs = tk.Frame(root)
frame_inputs.pack(pady=10)

label_n = tk.Label(frame_inputs, text="Number of Trials (n):")
label_n.grid(row=0, column=0, padx=5, pady=5)
entry_n = tk.Entry(frame_inputs)
entry_n.grid(row=0, column=1, padx=5, pady=5)

label_p = tk.Label(frame_inputs, text="Probability of Success (p):")
label_p.grid(row=1, column=0, padx=5, pady=5)
entry_p = tk.Entry(frame_inputs)
entry_p.grid(row=1, column=1, padx=5, pady=5)

label_k = tk.Label(frame_inputs, text="Number of Successes (k):")
label_k.grid(row=2, column=0, padx=5, pady=5)
entry_k = tk.Entry(frame_inputs)
entry_k.grid(row=2, column=1, padx=5, pady=5)

# Calculate button
btn_calculate = tk.Button(root, text="Calculate", command=calculate_binomial)
btn_calculate.pack(pady=10)

# Result display
label_result = tk.Label(root, text="P(X = k) = ", font=("Arial", 14))
label_result.pack(pady=10)

# Graph display
frame_graph = tk.Frame(root)
frame_graph.pack(pady=10)
fig, ax = plt.subplots(figsize=(5, 4))
canvas = FigureCanvasTkAgg(fig, master=frame_graph)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack()

# Run the application
root.mainloop()