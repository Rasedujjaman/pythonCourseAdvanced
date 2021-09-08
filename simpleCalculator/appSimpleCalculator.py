# Inspired from the model CITIZEN (SLD-322BK)


import tkinter as tk


LIGHT_GRAY = '#F5F5F5'
LABEL_COLOR = '#25265E'
SMALL_FONT_STYLE =("Arial", 16)
LARGE_FONT_STYLE =("Arial", 40, "bold")
DIGITS_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)
WHITE = '#FFFFFF'
OFF_WHITE = '#F8FAFF'
LIGHT_BLUE ='#CCEDFF'



class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("Simple calculator")
        
        # the label 
        self.total_expression =   "0"
        self.current_expression = "0"
        
        
        
        # Display and buttons frame
        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_buttons_frame()
        
        # the label
        self.tatal_label, self.label = self.create_display_labels()
    
        # the digits
        self.digits = {
            7:(1,1), 8:(1,2), 9:(1,3),
            4:(2,1), 5:(2,2), 6:(2,3),
            1:(3,1), 2:(3,2), 3:(3,3),
            0:(4, 2), '.':(4,1)
            }
        
        # Operation button
        self.operations = {"/":"\u00F7", "*":"\u00D7", "-": "-", "+":"+"}

        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_clear_button()
        self.create_equals_button()
    
    
        #  Stretch the button to fill the button_frame
        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)
            
    
    
    def create_clear_button(self):
            button = tk.Button(self.buttons_frame, text="C", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                               borderwidth=0)
            button.grid(row = 0, column = 1, columnspan = 3, sticky = tk.NSEW)
      
    
    
    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0)
        button.grid(row = 4, column = 3, columnspan = 2, sticky = tk.NSEW)
    
    
    def create_digit_buttons(self):
        for digit, gird_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg = WHITE, fg=LABEL_COLOR,font=DIGITS_FONT_STYLE,
                               borderwidth=0)
            button.grid(row=gird_value[0], column=gird_value[1], sticky=tk.NSEW)
        
    
    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                               borderwidth=0)
            button.grid(row = i, column = 4, sticky = tk.NSEW)
            i = i+1
    
    
    def create_display_labels(self):
        
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg =LIGHT_GRAY,fg=LABEL_COLOR, padx=24, font = SMALL_FONT_STYLE)
        total_label.pack(expand = True, fill = "both")
        
        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg =LIGHT_GRAY,fg=LABEL_COLOR, padx=24, font = LARGE_FONT_STYLE)
        label.pack(expand = True, fill = "both")
        
        return total_label, label
        
        
        
        
        
    
    def run(self):
        self.window.mainloop()
        

    def create_display_frame(self):
        frame = tk.Frame(self.window, height = 221, bg=LIGHT_GRAY)
        frame.pack(expand = True, fill= "both")
        return frame

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand = True, fill= "both")
        return frame









if __name__ == "__main__":
    calc = Calculator()
    calc.run()
    








#create a root window
# root = Tk()
# #set geometry
# #root.geometry("250x400+300+300")
# #disable the resize option for better UI
# root.resizable(0,0)
# #Give the tiltle to the calculator window
# root.title("Simple Calculator")
# 
# # Text display
# disp = Entry(root, width = 45, borderwidth=10)
# disp.grid(row = 0, column = 0, columnspan=4, padx=10, pady=10)
# 
# 
# # Creating the buttons
# button_onC = Button(root, text="ON/C",font = ("Verdana",14), relief =GROOVE,command=lambda:button_onC())
# button_CE = Button(root, text="CE",font = ("Verdana",14), relief =GROOVE,command=lambda:button_CE())
# button_Percent = Button(root, text="%",font = ("Verdana",14), relief =GROOVE,command=lambda:button_percent())
# button_Sqrt = Button(root, text="sq", font = ("Verdana",14), relief =GROOVE,command=lambda:button_sqrt())
# 
# button_MRC = Button(root, text="MRC", font = ("Verdana",14), relief =GROOVE,command=lambda:button_mrc())
# button_Mminus = Button(root, text="M-", font = ("Verdana",14), relief =GROOVE,command=lambda:button_mminus())
# button_Mplus = Button(root, text="M+", font = ("Verdana",14), relief =GROOVE,command=lambda:button_mplus())
# button_Div = Button(root, text="/", font = ("Verdana",14), relief =GROOVE,command=lambda:button_div())
# 
# button_7 = Button(root, text="7", font = ("Verdana",14), relief =GROOVE,command=lambda:button_click())
# button_8 = Button(root, text="8", font = ("Verdana",14), relief =GROOVE,command=lambda:button_click())
# button_9 = Button(root, text="9", font = ("Verdana",14), relief =GROOVE,command=lambda:button_click())
# button_Mul = Button(root, text="*", font = ("Verdana",14), relief =GROOVE,command=lambda:button_op())
# 
# button_4 = Button(root, text="4", font = ("Verdana",14), relief =GROOVE,command=lambda:button_click())
# button_5 = Button(root, text="5", font = ("Verdana",14), relief =GROOVE,command=lambda:button_click())
# button_6 = Button(root, text="6",  font = ("Verdana",14), relief =GROOVE,command=lambda:button_click())
# button_Minus = Button(root, text="-", font = ("Verdana",14), relief =GROOVE,command=lambda:button_op())
# 
# 
# 
# button_1 = Button(root, text="1", font = ("Verdana",14), relief =GROOVE,command=lambda:button_click())
# button_2 = Button(root, text="2", font = ("Verdana",14), relief =GROOVE,command=lambda:button_click())
# button_3 = Button(root, text="3", font = ("Verdana",14), relief =GROOVE,command=lambda:button_click())
# 
# 
# button_0 = Button(root, text="0", font = ("Verdana",14), relief =GROOVE,command=lambda:button_click())
# button_Point = Button(root, text=".", font = ("Verdana",14), relief =GROOVE,command=lambda:button_click())
# button_Equal = Button(root, text="=", font = ("Verdana",14), relief =GROOVE,command=lambda:button_eq())
# 
# 
# button_Plus = Button(root, text="+", font = ("Verdana",14), relief =GROOVE,command=lambda:button_eq())
# 
# # Placing the button on the main window
# button_onC.grid(row = 2, column = 0)
# button_CE.grid(row = 2, column = 1)
# button_Percent.grid(row = 2, column = 2)
# button_Sqrt.grid(row = 2, column = 3)
# 
# button_MRC.grid(row = 3, column = 0)
# button_Mminus.grid(row = 3, column = 1)
# button_Mplus.grid(row = 3, column = 2)
# button_Div.grid(row = 3, column = 3)
# 
# button_7.grid(row = 4, column = 0)
# button_8.grid(row = 4, column = 1)
# button_9.grid(row = 4, column = 2)
# button_Mul.grid(row = 4, column = 3)
# 
# 
# button_4.grid(row = 5, column = 0)
# button_5.grid(row = 5, column = 1)
# button_6.grid(row = 5, column = 2)
# button_Minus.grid(row = 5, column = 3)
# 
# button_1.grid(row = 6, column = 0)
# button_2.grid(row = 6, column = 1)
# button_3.grid(row = 6, column = 2)
# 
# button_0.grid(row = 7, column = 0)
# button_Point.grid(row = 7, column = 1)
# button_Equal.grid(row = 7, column = 2)
# 
# button_Plus.grid(row = 6, column = 3, rowspan=2)


# root.mainloop()