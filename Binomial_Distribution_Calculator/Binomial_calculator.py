import tkinter as tk  # Import the tkinter library for creating the GUI (Graphical User Interface)
from tkinter import messagebox
from scipy.stats import binom  # Import the binom module from scipy.stats for calculating binomial distribution

def calculate_binomial():
    """Function to calculate the Binomial Probability based on user input."""
    try:
        # Get the value of n, p, and k from the input fields and convert them to the right type
        n = int(entry_n.get())  # Number of trials (n)
        p = float(entry_p.get())  # Probability of Success in a single trial (p)
        k = int(entry_k.get())  # Number of Success (k)


        # Calculate the Binomial Probability mass Function (pmf) using scipy's binom.pmf
        binom_prob = binom.pmf(k, n, p)

        # Update the result label to show the calculated binomial probability
        result_label.config(text=f"Binomial Probability: {binom_prob:.4f}")

        # Disable the calculate button after the first calculation
        calculate_button.config(state=tk.DISABLED)

    except ValueError:
        # If there is an error in input conversion, show an error message
        result_label.config(text="Please enter valid inputs.")
        messagebox.showerror("Input Error", "Please enter valid inputs. Make sure n is non-negative, p is between 0 and 1, and k is between 0 and n.")

def clear_and_enable():
    """Clear the entry fields and enable the calculate button for a new calculation."""
    entry_n.delete(0, tk.END)  # Clear the number of trials entry
    entry_p.delete(0, tk.END)  # Clear the probability of success entry
    entry_k.delete(0, tk.END)  # Clear the number of successes entry

    # Re-enable the calculate button
    calculate_button.config(state=tk.NORMAL)

# Create the main application window
root = tk.Tk()  # Initialize the tkinter window
root.title("Binomial Distribution Calculator")  # Set the title of the window

# Create and place the label and entry for the number of trials (n)
label_n = tk.Label(root, text="Number of trials (n): ")
label_n.grid(row=0, column=0, padx=10, pady=10)  # Position the label with padding
entry_n = tk.Entry(root)  # Create an entry widget for the user to input the number of trials
entry_n.grid(row=0, column=1, padx=10, pady=10)  # Position the entry widget with padding

# Create and place the label and entry for the probability of success (p)
label_p = tk.Label(root, text="Probability of Success (p): ")
label_p.grid(row=1, column=0, padx=10, pady=10)  # Position the label with padding
entry_p = tk.Entry(root)  # Create an entry widget for the user to input the probability of success
entry_p.grid(row=1, column=1, padx=10, pady=10)  # Position the entry widget with padding

# Create and place the label and entry for the number of successes (k)
label_k = tk.Label(root, text="Number of successes (k): ")
label_k.grid(row=2, column=0, padx=10, pady=10)  # Position the label with padding
entry_k = tk.Entry(root)  # Create an entry widget for the user to input the number of successes
entry_k.grid(row=2, column=1, padx=10, pady=10)  # Position the entry widget with padding

# Create a button to trigger the calculation when clicked
calculate_button = tk.Button(root, text="Calculate Binomial", command=calculate_binomial)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)  # Position the button with padding

# Create and place the result label
result_label = tk.Label(root, text="")  # Create a label to display the result
result_label.grid(row=4, column=0, columnspan=2, pady=10)  # Position the result label with padding

# Create a button to clear the fields and re-enable the calculate button
clear_button = tk.Button(root, text="Perform Another Calculation", command=clear_and_enable)
clear_button.grid(row=5, column=0, columnspan=2, pady=10)  # Position the clear button with padding

# Run the application's event loop
root.mainloop()  # Keep window open and responsive to user interaction
