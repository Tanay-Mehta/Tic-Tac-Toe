#------------------------------------imports----------------------------
import tkinter as tk
from tkinter import messagebox
import random
COUNT = 0
list_of_buttons = []
for i in range(1, 10):
    list_of_buttons.append(f"b{i}")
screen = tk.Tk()
screen.title("TICK-TACK-TOE")

def single_player():
    b22.grid_forget()
    b11.grid_forget()
    def disable():
        b1["state"] = 'disabled'
        b2["state"] = 'disabled'
        b3["state"] = 'disabled'
        b4["state"] = 'disabled'
        b5["state"] = 'disabled'
        b6["state"] = 'disabled'
        b7["state"] = 'disabled'
        b8["state"] = 'disabled'
        b9["state"] = 'disabled'
    def check_done():
        global COUNT
        if (b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X'):
            b1.config(bg="red")
            b4.config(bg="red")
            b7.config(bg="red")
            messagebox.showinfo(title="Congratulations", message="X wins")
            disable()
            return True
        elif (b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X'):
            b2.config(bg="red")
            b5.config(bg="red")
            b8.config(bg="red")
            messagebox.showinfo(title="Congratulations", message="X wins")
            disable()
            return True
        elif (b3['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X'):
            b3.config(bg="red")
            b6.config(bg="red")
            b9.config(bg="red")
            messagebox.showinfo(title="Congratulations", message="X wins")
            disable()
            return True
        elif (b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X'):
            b1.config(bg="red")
            b2.config(bg="red")
            b3.config(bg="red")
            messagebox.showinfo(title="Congratulations", message="X wins")
            disable()
            return True
        elif (b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X'):
            b4.config(bg="red")
            b5.config(bg="red")
            b6.config(bg="red")
            messagebox.showinfo(title="Congratulations", message="X wins")
            disable()
            return True
        elif (b7['text'] == 'X' and b8['text'] == 'X' and b9['text'] == 'X'):
            b7.config(bg="red")
            b8.config(bg="red")
            b9.config(bg="red")
            messagebox.showinfo(title="Congratulations", message="X wins")
            disable()
            return True
        elif (b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X'):
            b1.config(bg="red")
            b5.config(bg="red")
            b9.config(bg="red")
            messagebox.showinfo(title="Congratulations", message="X wins")
            disable()
            return True
        elif (b7['text'] == 'X' and b5['text'] == 'X' and b3['text'] == 'X'):
            b7.config(bg="red")
            b5.config(bg="red")
            b3.config(bg="red")
            messagebox.showinfo(title="Congratulations", message="X wins")
            disable()
            return True
        elif (b1['text'] == '0' and b4['text'] == '0' and b7['text'] == '0'):
            b1.config(bg="blue")
            b4.config(bg="blue")
            b7.config(bg="blue")
            messagebox.showinfo(title="Congratulations", message="Y wins")
            disable()
            return True
        elif (b2['text'] == '0' and b5['text'] == '0' and b8['text'] == '0'):
            b2.config(bg="blue")
            b5.config(bg="blue")
            b8.config(bg="blue")
            messagebox.showinfo(title="Congratulations", message="Y wins")
            disable()
            return True
        elif (b3['text'] == '0' and b6['text'] == '0' and b9['text'] == '0'):
            b3.config(bg="blue")
            b6.config(bg="blue")
            b9.config(bg="blue")
            messagebox.showinfo(title="Congratulations", message="Y wins")
            disable()
            return True
        elif (b1['text'] == '0' and b2['text'] == '0' and b3['text'] == '0'):
            b1.config(bg="blue")
            b2.config(bg="blue")
            b3.config(bg="blue")
            messagebox.showinfo(title="Congratulations", message="Y wins")
            disable()
            return True
        elif (b4['text'] == '0' and b5['text'] == '0' and b6['text'] == '0'):
            b5.config(bg="blue")
            b4.config(bg="blue")
            b6.config(bg="blue")
            messagebox.showinfo(title="Congratulations", message="Y wins")
            disable()
            return True
        elif (b7['text'] == '0' and b8['text'] == '0' and b9['text'] == '0'):
            b7.config(bg="blue")
            b8.config(bg="blue")
            b9.config(bg="blue")
            messagebox.showinfo(title="Congratulations", message="Y wins")
            disable()
            return True
        elif (b1['text'] == '0' and b5['text'] == '0' and b9['text'] == '0'):
            b1.config(bg="blue")
            b5.config(bg="blue")
            b9.config(bg="blue")
            messagebox.showinfo(title="Congratulations", message="Y wins")
            disable()
            return True
        elif (b7['text'] == '0' and b5['text'] == '0' and b3['text'] == '0'):
            b7.config(bg="blue")
            b5.config(bg="blue")
            b3.config(bg="blue")
            messagebox.showinfo(title="Congratulations", message="Y wins")
            disable()
            return True
        elif (b1['text'] == '0' and b5['text'] == '0' and b9['text'] == '0'):
            b1.config(bg="blue")
            b5.config(bg="blue")
            b9.config(bg="blue")
            messagebox.showinfo(title="Congratulations", message="Y wins")
            disable()
            return True
        elif (b7['text'] == '0' and b5['text'] == '0' and b3['text'] == '0'):
            b7.config(bg="blue")
            b5.config(bg="blue")
            b3.config(bg="blue")
            messagebox.showinfo(title="Congratulations", message="Y wins")
            disable()
            return True
        elif COUNT > 7:
            messagebox.showinfo(title="Good Match!", message="It's a Draw")
            disable()
            return True
        else:
            return False
    def press_random():
        compress = random.choice(list_of_buttons)
        if "b1" == compress:
            b1.config(text="0")
        elif "b2" == compress:
            b2.config(text="0")
        elif "b3" == compress:
            b3.config(text="0")
        elif "b4" == compress:
            b4.config(text="0")
        elif "b5" == compress:
            b5.config(text="0")
        elif "b6" == compress:
            b6.config(text="0")
        elif "b7" == compress:
            b7.config(text="0")
        elif "b8" == compress:
            b8.config(text="0")
        elif "b9" == compress:
            b9.config(text="0")
        list_of_buttons.remove(compress)
        check_done()
    def b1_pr():
        global COUNT
        if (b1['text'] == ''):
            list_of_buttons.remove("b1")
            b1.config(text="X")
            response = check_done()
            if response == False:
                press_random()
            COUNT += 1
        else:
            messagebox.showerror(title="Error!", message="No re-clicking the buttons")
    def b2_pr():
        global COUNT
        if (b2['text'] == ''):
            list_of_buttons.remove("b2")
            b2.config(text="X")
            response = check_done()
            if response == False:
                press_random()
            COUNT += 1
        else:
            messagebox.showerror(title="Error!", message="No re-clicking the buttons")
    def b3_pr():
        global COUNT
        if (b3['text'] == ''):
            list_of_buttons.remove("b3")
            b3.config(text="X")
            response = check_done()
            if response == False:
                press_random()
            COUNT += 1
        else:
            messagebox.showerror(title="Error!", message="No re-clicking the buttons")
    def b4_pr():
        global COUNT
        if (b4['text'] == ''):
            list_of_buttons.remove("b4")
            b4.config(text="X")
            response = check_done()
            if response == False:
                press_random()
            COUNT += 1
        else:
            messagebox.showerror(title="Error!", message="No re-clicking the buttons")
    def b5_pr():
        global COUNT
        if (b5['text'] == ''):
            list_of_buttons.remove("b5")
            b5.config(text="X")
            response = check_done()
            if response == False:
                press_random()
            COUNT += 1
        else:
            messagebox.showerror(title="Error!", message="No re-clicking the buttons")
    def b6_pr():
        global COUNT
        if (b6['text'] == ''):
            list_of_buttons.remove("b6")
            b6.config(text="X")
            response = check_done()
            if response == False:
                press_random()
            COUNT += 1
        else:
            messagebox.showerror(title="Error!", message="No re-clicking the buttons")
    def b7_pr():
        global COUNT
        if (b7['text'] == ''):
            list_of_buttons.remove("b7")
            b7.config(text="X")
            response = check_done()
            if response == False:
                press_random()
            COUNT += 1
        else:
            messagebox.showerror(title="Error!", message="No re-clicking the buttons")
    def b8_pr():
        global COUNT
        if (b8['text'] == ''):
            list_of_buttons.remove("b8")
            b8.config(text="X")
            response = check_done()
            if response == False:
                press_random()
            COUNT += 1
        else:
            messagebox.showerror(title="Error!", message="No re-clicking the buttons")
    def b9_pr():
        global COUNT
        if (b9['text'] == ''):
            list_of_buttons.remove("b9")
            b9.config(text="X")
            response = check_done()
            if response == False:
                press_random()
            COUNT += 1
        else:
            messagebox.showerror(title="Error!", message="No re-clicking the buttons")


    b1 = tk.Button(name="", font=("arial", 20), height=3, width=6, command=b1_pr)
    b2 = tk.Button(name="", font=("arial", 20), height=3, width=6, command=b2_pr)
    b3 = tk.Button(name="", font=("arial", 20), height=3, width=6, command=b3_pr)
    b4 = tk.Button(name="", font=("arial", 20), height=3, width=6, command=b4_pr)
    b5 = tk.Button(name="", font=("arial", 20), height=3, width=6, command=b5_pr)
    b6 = tk.Button(name="", font=("arial", 20), height=3, width=6, command=b6_pr)
    b7 = tk.Button(name="", font=("arial", 20), height=3, width=6, command=b7_pr)
    b8 = tk.Button(name="", font=("arial", 20), height=3, width=6, command=b8_pr)
    b9 = tk.Button(name="", font=("arial", 20), height=3, width=6, command=b9_pr)

    b1.grid(row=1, column=1)
    b2.grid(row=2, column=1)
    b3.grid(row=3, column=1)
    b4.grid(row=1, column=2)
    b5.grid(row=2, column=2)
    b6.grid(row=3, column=2)
    b7.grid(row=1, column=3)
    b8.grid(row=2, column=3)
    b9.grid(row=3, column=3)


def two_players():
    b11.grid_forget()
    b22.grid_forget()
    # ---------------------disable all buttons after the game ends-------------
    def disable():
        b1["state"] = 'disabled'
        b2["state"] = 'disabled'
        b3["state"] = 'disabled'
        b4["state"] = 'disabled'
        b5["state"] = 'disabled'
        b6["state"] = 'disabled'
        b7["state"] = 'disabled'
        b8["state"] = 'disabled'
        b9["state"] = 'disabled'

    # ------------------ check if any of the sequences have been made-----------------
    def check_done():
        global COUNT
        if (b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X'):
            b1.config(bg="red")
            b4.config(bg="red")
            b7.config(bg="red")
            messagebox.showinfo(title="Congratulations", message="X wins")
            disable()
        elif (b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X'):
            b2.config(bg="red")
            b5.config(bg="red")
            b8.config(bg="red")
            messagebox.showinfo(title="Congratulations", message="X wins")
            disable()
        elif (b3['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X'):
            b3.config(bg="red")
            b6.config(bg="red")
            b9.config(bg="red")
            messagebox.showinfo(title="Congratulations", message="X wins")
            disable()
        elif (b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X'):
            b1.config(bg="red")
            b2.config(bg="red")
            b3.config(bg="red")
            messagebox.showinfo(title="Congratulations", message="X wins")
            disable()
        elif (b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X'):
            b4.config(bg="red")
            b5.config(bg="red")
            b6.config(bg="red")
            messagebox.showinfo(title="Congratulations", message="X wins")
            disable()
        elif (b7['text'] == 'X' and b8['text'] == 'X' and b9['text'] == 'X'):
            b7.config(bg="red")
            b8.config(bg="red")
            b9.config(bg="red")
            messagebox.showinfo(title="Congratulations", message="X wins")
            disable()
        elif (b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X'):
            b1.config(bg="red")
            b5.config(bg="red")
            b9.config(bg="red")
            messagebox.showinfo(title="Congratulations", message="X wins")
            disable()
        elif (b7['text'] == 'X' and b5['text'] == 'X' and b3['text'] == 'X'):
            b7.config(bg="red")
            b5.config(bg="red")
            b3.config(bg="red")
            messagebox.showinfo(title="Congratulations", message="X wins")
            disable()
        elif (b1['text'] == '0' and b4['text'] == '0' and b7['text'] == '0'):
            b1.config(bg="blue")
            b4.config(bg="blue")
            b7.config(bg="blue")
            messagebox.showinfo(title="Congratulations", message="Y wins")
            disable()
        elif (b2['text'] == '0' and b5['text'] == '0' and b8['text'] == '0'):
            b2.config(bg="blue")
            b5.config(bg="blue")
            b8.config(bg="blue")
            messagebox.showinfo(title="Congratulations", message="Y wins")
            disable()
        elif (b3['text'] == '0' and b6['text'] == '0' and b9['text'] == '0'):
            b3.config(bg="blue")
            b6.config(bg="blue")
            b9.config(bg="blue")
            messagebox.showinfo(title="Congratulations", message="Y wins")
            disable()
        elif (b1['text'] == '0' and b2['text'] == '0' and b3['text'] == '0'):
            b1.config(bg="blue")
            b2.config(bg="blue")
            b3.config(bg="blue")
            messagebox.showinfo(title="Congratulations", message="Y wins")
            disable()
        elif (b4['text'] == '0' and b5['text'] == '0' and b6['text'] == '0'):
            b5.config(bg="blue")
            b4.config(bg="blue")
            b6.config(bg="blue")
            messagebox.showinfo(title="Congratulations", message="Y wins")
            disable()
        elif (b7['text'] == '0' and b8['text'] == '0' and b9['text'] == '0'):
            b7.config(bg="blue")
            b8.config(bg="blue")
            b9.config(bg="blue")
            messagebox.showinfo(title="Congratulations", message="Y wins")
            disable()
        elif (b1['text'] == '0' and b5['text'] == '0' and b9['text'] == '0'):
            b1.config(bg="blue")
            b5.config(bg="blue")
            b9.config(bg="blue")
            messagebox.showinfo(title="Congratulations", message="Y wins")
            disable()
        elif (b7['text'] == '0' and b5['text'] == '0' and b3['text'] == '0'):
            b7.config(bg="blue")
            b5.config(bg="blue")
            b3.config(bg="blue")
            messagebox.showinfo(title="Congratulations", message="Y wins")
            disable()
        elif (b1['text'] == '0' and b5['text'] == '0' and b9['text'] == '0'):
            b1.config(bg="blue")
            b5.config(bg="blue")
            b9.config(bg="blue")
            messagebox.showinfo(title="Congratulations", message="Y wins")
            disable()
        elif (b7['text'] == '0' and b5['text'] == '0' and b3['text'] == '0'):
            b7.config(bg="blue")
            b5.config(bg="blue")
            b3.config(bg="blue")
            messagebox.showinfo(title="Congratulations", message="Y wins")
            disable()
        elif COUNT > 7:
            messagebox.showinfo(title="Good Match!", message="It's a Draw")

    #----------------------------button functions---------------------------------

    def b1_pr():
        global COUNT
        if (b1['text'] == ''):
            if COUNT % 2 == 0:
                b1.config(text="X")
            else:
                b1.config(text="0")
            check_done()
            COUNT += 1
        else:
            messagebox.showerror(title="Error!", message="No re-clicking the buttons")


    def b2_pr():
        global COUNT
        if (b2['text'] == ''):
            if COUNT % 2 == 0:
                b2.config(text="X")
            else:
                b2.config(text="0")
            check_done()
            COUNT += 1
        else:
            messagebox.showerror(title="Error!", message="No re-clicking the buttons")


    def b3_pr():
        global COUNT
        if (b3['text'] == ''):
            if COUNT % 2 == 0:
                b3.config(text="X")
            else:
                b3.config(text="0")
            check_done()
            COUNT += 1
        else:
            messagebox.showerror(title="Error!", message="No re-clicking the buttons")


    def b4_pr():
        global COUNT
        if (b4['text'] == ''):
            if COUNT % 2 == 0:
                b4.config(text="X")
            else:
                b4.config(text="0")

            check_done()
            COUNT += 1
        else:
            messagebox.showerror(title="Error!", message="No re-clicking the buttons")


    def b5_pr():
        global COUNT
        if (b5['text'] == ''):
            if COUNT % 2 == 0:
                b5.config(text="X")
            else:
                b5.config(text="0")
            check_done()
            COUNT += 1
        else:
            messagebox.showerror(title="Error!", message="No re-clicking the buttons")


    def b6_pr():
        global COUNT
        if (b6['text'] == ''):
            if COUNT % 2 == 0:
                b6.config(text="X")
            else:
                b6.config(text="0")
            check_done()
            COUNT += 1
        else:
            messagebox.showerror(title="Error!", message="No re-clicking the buttons")


    def b7_pr():
        global COUNT
        if (b7['text'] == ''):
            if COUNT % 2 == 0:
                b7.config(text="X")
            else:
                b7.config(text="0")
            check_done()
            COUNT += 1
        else:
            messagebox.showerror(title="Error!", message="No re-clicking the buttons")


    def b8_pr():
        global COUNT
        if (b8['text'] == ''):
            if COUNT % 2 == 0:
                b8.config(text="X")
            else:
                b8.config(text="0")
            check_done()
            COUNT += 1
        else:
            messagebox.showerror(title="Error!", message="No re-clicking the buttons")


    def b9_pr():
        global COUNT
        if (b9['text'] == ''):
            if COUNT % 2 == 0:
                b9.config(text="X")
            else:
                b9.config(text="0")
            check_done()
            COUNT += 1
        else:
            messagebox.showerror(title="Error!", message="No re-clicking the buttons")

    # ------------------------------Button and screen structure------------------------------


    b1 = tk.Button(name="", font=("arial", 20), height=3, width=6, command=b1_pr)
    b2 = tk.Button(name="", font=("arial", 20), height=3, width=6, command=b2_pr)
    b3 = tk.Button(name="", font=("arial", 20), height=3, width=6, command=b3_pr)
    b4 = tk.Button(name="", font=("arial", 20), height=3, width=6, command=b4_pr)
    b5 = tk.Button(name="", font=("arial", 20), height=3, width=6, command=b5_pr)
    b6 = tk.Button(name="", font=("arial", 20), height=3, width=6, command=b6_pr)
    b7 = tk.Button(name="", font=("arial", 20), height=3, width=6, command=b7_pr)
    b8 = tk.Button(name="", font=("arial", 20), height=3, width=6, command=b8_pr)
    b9 = tk.Button(name="", font=("arial", 20), height=3, width=6, command=b9_pr)

    b1.grid(row=1, column=1)
    b2.grid(row=2, column=1)
    b3.grid(row=3, column=1)
    b4.grid(row=1, column=2)
    b5.grid(row=2, column=2)
    b6.grid(row=3, column=2)
    b7.grid(row=1, column=3)
    b8.grid(row=2, column=3)
    b9.grid(row=3, column=3)

b11 = tk.Button(text="Two Players", font=("arial", 10), height=2, width=10, command=two_players)
b22 = tk.Button(text="Single Player", font=("arial", 10), height=2, width=10, command=single_player)
b11.grid(row=1, column=2)
b22.grid(row=2, column=2)
screen.mainloop()
