from tkinter import Label, Entry, Button, Tk

def calculateGrade():
    raw = int(raw_Mark_text.get())
    maxM = int(max_Mark_text.get())
    result = ""
    percentage = (raw / maxM) * 100

    if percentage > 85:
        result = "A*"
        resultLabel.config(bg='gold')
    elif percentage > 70:
        result = "A"
        resultLabel.config(bg='green')
    elif percentage > 60:
        result = "B"
        resultLabel.config(bg='silver')
    elif percentage > 50:
        result = "C"
        resultLabel.config(bg='silver')
    elif percentage > 40:
        result = "D"
    elif percentage > 30:
        result = "E"
    elif percentage > 20:
        result = "F"
    else:
        result + "U"

    resultLabel.config(text=result)

def clearMarks():
    max_Mark_text.delete('0',END)
    raw_Mark_text.delete('0',END)
    resultLabel.config(text='',bg='linen')

window = Tk()
window.title("Grade Calculator")
# window.geometry('200x300')
window.config(bg='linen')

instruc = Label(window, width=30, height=2, text='Input raw and max score for final grade', bg='linen')
instruc.grid(row=1, column=0, columnspan=2)

raw_label = Label(window, width=10, height=1, text='Raw Score', bg='linen')
raw_label.grid(row=2, column=0)
raw_Mark_text = Entry(window, width=5)
raw_Mark_text.grid(row=2, column=1)

#label and text box for max marks
max_label = Label(window, width=10, height=1, text='Max Mark', bg='linen')
max_label.grid(row=3, column=0)
max_Mark_text = Entry(window, width=5)
max_Mark_text.grid(row=3, column=1)

#buttons
calculate_button = Button(window, text='Calculate', width=15, command=calculateGrade)
calculate_button.grid(row=5, column=0)
clear_Button = Button(window, text='Clear', width=15, command=clearMarks)
clear_Button.grid(row=5, column=1)

finalGrade_label = Label(window, width=10, height=2, text='Overall Grade: ', bg='linen')
finalGrade_label.grid(row=6, column=0)
resultLabel = Label(window, width=15, height=2, text='', bg='linen')
resultLabel.grid(row=6, column=1)

window.mainloop()