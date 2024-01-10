from tkinter import *
def calculation_bmi():
    try:
        name = str(name_user_entry.get())
        weight = int(weight_user_entry.get())
        height = int(height_user_entry.get())

        result_label.config(text="")

        body_index = weight / ((height / 100) ** 2)

        if name == "" or not name.isalpha():
            result_label.config(text="Please enter a valid name ")
        elif (weight == "" or height == "") or (weight <= 0 or height <= 0):
            result_label.config(text="Please enter valid numeric values weıght and heıght...")
        else:
            if body_index <= 0:
                result_label.config(text=f"{name}, Please check values weight and height...")
            elif (body_index) > 0 and (body_index < 18.5):
                result_label.config(text="{}'s bmı value: {}, status : underweıght ".format(name,round(body_index,2)))
            elif (body_index) >= 18.5 and (body_index < 25):
                result_label.config(text="{}'s bmı value: {}, status : normal ".format(name,round(body_index,2)))
            elif (body_index) >=25 and (body_index < 30):
                result_label.config(text="{}'s bmı value: {}, status : overweıght ".format(name,round(body_index,2)))
            elif (body_index) >=30 and (body_index < 35):
                result_label.config(text="{}'s bmı value: {}, status : obese ".format(name,round(body_index,2)))
            elif (body_index) >=35:
                result_label.config(text="{}'s bmı value: {}, status : extremly obese ".format(name,round(body_index, 2)))
    except:
        result_label.config(text="Please check values")

window = Tk()
window.title("calculator BMI")
window.minsize(width=250,height=250)
window.config(padx=40,pady=40)

name_label = Label(text="Please, your enter name")
name_label.pack()

name_user_entry = Entry()
name_user_entry.focus()
name_user_entry.pack()

weight_label = Label(text="Please, your enter weight")
weight_label.pack()

weight_user_entry = Entry()
weight_user_entry.pack()

height_label = Label(text="Please, your enter height")
height_label.pack()

height_user_entry = Entry()
height_user_entry.pack()

calculator_button = Button(text="calculator",command=calculation_bmi)
calculator_button.pack()

result_label = Label()
result_label.pack()

window.mainloop()
