#Import necessary libraries
from tkinter import*
from tkinter.filedialog import askopenfilename, asksaveasfilename
#Setup root window
window=Tk()
window.title("Codingal's Text Editor")
window.geomtry("600x500")
window.rowconfigure(0, minsize=800, height=1)
window.columnconfigure(1, minsize=800, height=1)
#Function to open a file
def open_file():
    """Open a file for editing"""
    filepath = askopenfilename(
    filetypes=[("Text files", "*.txt") ("All files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, END)
    #If a file is open then display the contents of the file
    with open(filepath, "r") as input_file:
        #Read contents of the input file
        text = input_file.read()
        #Insert contents of the file in the editor box
        txt_edit.insert(END, text)
        input_file.close()
        window.title(f"Codingal's text editor - {filepath}")
#Function to save a file
def save_file():
    #Save the current file as a new file
    filepath = asksaveasfilename(
    filetypes=[("Text files", "*.txt") ("All files", "*.*")]
    )
    if not filepath:
        return
    with open(filepath, "r") as output_file:
        #Read the edited content and update in the output file
        text = txt_edit.get(1.0, END)
        output_file.write(text)
        window.title(f"Codingal's text editor - {filepath}")

#Add widgets in the application
txt_edit = Text(window) 
fr_button = Frame(window, relief=RAISED, bd=2)
btn_open = Button(fr_button, text="Open", command= open_file)
btn_save = Button(fr_button, text="Save As...", command= save_file)     
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)    
btn_save.grid(row=0, column=0, sticky="ew", padx=5)

fr_button.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=0, sticky="nsew")

#Start the GUI event loop
window.mainloop()