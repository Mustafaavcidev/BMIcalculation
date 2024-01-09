from tkinter import *
def calculation_bmi():
    try:
        weight = int(weight_user_entry.get())
        height = int(height_user_entry.get())

        result_label.config(text="")

        body_index = weight / ((height / 100) ** 2)
        if (weight == "" or height == "") or (weight <= 0 or height <= 0):
            result_label.config(text="Please enter valid numeric values weıght and heıght...")
        else:
            if  body_index <= 0:
                result_label.config(text="Please check values weight and height...")
            elif (body_index) > 0 and (body_index < 18.5):
                result_label.config(text="your bmı value: {}, status : underweıght ".format(round(body_index,2)))
            elif (body_index) >= 18.5 and (body_index < 25):
                result_label.config(text="your bmı value: {}, status : normal ".format(round(body_index,2)))
            elif (body_index) >=25 and (body_index < 30):
                result_label.config(text="your bmı value: {}, status : overweıght ".format(round(body_index,2)))
            elif (body_index) >=30 and (body_index < 35):
                result_label.config(text="your bmı value: {}, status : obese ".format(round(body_index,2)))
            elif (body_index) >=35:
                result_label.config(text="your bmı value: {}, status : extremly obese ".format(round(body_index, 2)))
    except:
        result_label.config(text="Please check values")

window = Tk()
window.title("calculator BMI")
window.minsize(width=250,height=250)
window.config(padx=40,pady=40)

weight_label = Label(text="Please, your enter weight")
weight_label.pack()

weight_user_entry = Entry()
weight_user_entry.focus()
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
