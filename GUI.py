import tkinter as tk
import GlobalVars

def on_checkbox_select(event=None):
    value = checkbox_var.get()
    if value == 1:
        slider.config(state='normal')
        output_var.set("Slider is enabled")
    else:
        slider.config(state='disabled')
        output_var.set("Slider is disabled")

def on_slider_change(event=None):
    value = slider.get()
    output_var.set("Slider value: {}".format(value))

root = tk.Tk()
root.geometry("200x800")

checkbox_var = tk.IntVar()
checkbox = tk.Checkbutton(root, text="Enable slider", variable=checkbox_var, command=on_checkbox_select)
checkbox.pack()

slider = tk.Scale(root, from_=0, to=100, orient='horizontal', state='disabled', command=on_slider_change)
slider.pack()

output_var = tk.StringVar()
output_label = tk.Label(root, textvariable=output_var)
output_label.pack()

root.mainloop()