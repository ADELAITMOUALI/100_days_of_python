import tkinter as tk


#setup screen 
window = tk.Tk()
window.minsize(width=250,height=150)
window.title("Miles to Km")
window.config(padx=20, pady=20)
#fonction calcul
def miles_to_km():
    try:
        result = round((float(user_input.get()) / 0.6214), 4)
        result_label["text"] = str(result)
    except ValueError:
        result_label["text"] = "Invalid input"
#user input 
user_input = tk.Entry(width=10)

user_input.grid(column=1,row=0)
#labele miles
miles_label = tk.Label(text="Miles")
miles_label.grid(column=2,row=0)
#label equal to
equal_label = tk.Label(text="is equal to")
equal_label.grid(column=0,row=1)
#result  label
result_label = tk.Label(text="0")
result_label.grid(column=1,row=1)
#km label 
km_label = tk.Label(text="Km")
km_label.grid(column=2,row=1)
#button calculate 
calc = tk.Button(text="Calculate", command=miles_to_km)
calc.grid(column=1,row=2)

window.mainloop()