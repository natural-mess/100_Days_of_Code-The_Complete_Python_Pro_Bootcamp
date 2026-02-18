from tkinter import *

def mile_to_km():
    """Convert mile to km"""
    km_result.config(text=f"{round(float(mile_input.get())*1.60934,2)}")

# Window
window = Tk()
window.title("Mile to Km Converter")
# window.minsize(width=250, height=150)
window.config(padx=20, pady=20)

# Label
convert_info = Label(text="is equal to")
convert_info.grid(column=0, row=1)

mile = Label(text="Miles")
mile.grid(column=2, row=0)

km = Label(text="Km")
km.grid(column=2, row=1)

km_result = Label(text="0")
km_result.grid(column=1, row=1)

# Entry
mile_input = Entry(width=10)
mile_input.grid(column=1, row=0)

# Button
calculate_btn = Button(text="Calculate", command=mile_to_km)
calculate_btn.grid(column=1, row=2)

window.mainloop()