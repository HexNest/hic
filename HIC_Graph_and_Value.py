import tkinter as tk
import tkinter.font as font
import plot as plot
from hic import hic

def calculate_hic():
    hic_val = int(hic() * 1000) / 1000.0
    l1['text'] = "HIC: " + str(hic_val)
    plot.plot_data()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

helv36 = font.Font(family = "Helvetica", size = 36, weight = 'bold')

l1 = tk.Label(root, fg = 'blue', text = 'HIC', font = helv36)
l1.pack(side = tk.BOTTOM)

button = tk.Button(root, text = "Calculate HIC", command = calculate_hic, activebackground = 'orange', relief = tk.RAISED, borderwidth = 5, font = helv36)
button.pack(side = tk.TOP)

root.mainloop()