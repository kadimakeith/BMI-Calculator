import tkinter

root = tkinter.Tk()
root.title("BMI Calculator")
root.geometry("250x100")

def calculate_bmi():
    kg = float(entry_kg.get())
    height = float(entry_height.get())
    bmi = round(kg/(height**2),2)
    label_result['text'] = f"BMI:{bmi}"
    if bmi > 26:
        label_result['text'] = f"Overweight:{bmi}"
    elif bmi < 18:
        label_result['text'] = f"Underweight:{bmi}"
    else:
        label_result['text'] = f"Healthy:{bmi}"

# Create GUI
label_kg = tkinter.Label(root, text="Weight(KG)")
label_kg.grid(column=0, row=0)

entry_kg = tkinter.Entry(root)
entry_kg.grid(column=2, row=0)

label_height = tkinter.Label(root, text="Height(M)")
label_height.grid(column=0, row=1)

entry_height = tkinter.Entry(root)
entry_height.grid(column=2, row=1)

button_calculate = tkinter.Button(root, text = "CALCULATE", command = calculate_bmi)
button_calculate.grid(column=0, row=2) 

label_result = tkinter.Label(root, text="BMI")
label_result.grid(column=2, row=2)

root.mainloop()