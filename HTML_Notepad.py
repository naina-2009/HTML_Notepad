from tkinter import*
from PIL import ImageTk, Image
from tkinter import filedialog
import os
import webbrowser

root = Tk()
root.title("HTML Notepad")
root.minsize(650,650)
root.maxsize(650,650)

open_img1 = Image.open("open.png")
open_img2 = open_img1.resize((40,40))
open_img = ImageTk.PhotoImage(open_img2)

exit_img1 = Image.open("exit.jpg")
exit_img2 = exit_img1.resize((40,40))
exit_img = ImageTk.PhotoImage(exit_img2)

save_img1 = Image.open("save.png")
save_img2 = save_img1.resize((40,40))
save_img = ImageTk.PhotoImage(save_img2)

run_img1 = Image.open("run.jpg")
run_img2 = run_img1.resize((40,40))
run_img = ImageTk.PhotoImage(run_img2)

label_file_name = Label(root, text = "File : ")
label_file_name.place(relx = 0.55, rely = 0.03, anchor = CENTER)

input_file_name = Entry(root)
input_file_name.place(relx = 0.70, rely = 0.03, anchor = CENTER)

my_text = Text(root, height = 30, width = 60)
my_text.place(relx= 0.5, rely = 0.55, anchor =CENTER)

name = ""
def openFile():
    global name
    my_text.delete(1.0, END)
    input_file_name.delete(0, END)
    html_file = filedialog.askopenfilename(title = "Open HTML files", filetypes = (("HTML files", "*.html"),))
    print(html_file)
    name = os.path.basename(html_file)
    formatted_name = name.split(".")[0]
    input_file_name.insert(END, formatted_name)
    root.title(formatted_name)
    html_file = open(name, 'r')
    paragraph = html_file.read()
    my_text.insert(END, paragraph)
    html_file.close()
    
def save():
    input_name = input_file_name.get()
    file = open(input_name+".html", 'r+')
    data = my_text.get(1.0, END)
    file.write(data)
    input_file_name.delete(0, END)
    my_text.delete(1.0, END)
    messagebox.showinfo("Update", "File has been successfully updated and saved!")

def run_html_file():
    global name
    webbrowser.open(name)
    
def close():
    root.destroy()

open_btn = Button(root, image = open_img, command = openFile)
open_btn.place(relx = 0.05, rely = 0.05, anchor = CENTER)

save_btn = Button(root, image = save_img, command = save)
save_btn.place(relx = 0.13, rely = 0.05, anchor = CENTER)

run_btn = Button(root, image = run_img, command = run_html_file)
run_btn.place(relx = 0.21, rely = 0.05, anchor = CENTER)

close_btn = Button(root, image = exit_img, command = close)
close_btn.place(relx = 0.29, rely = 0.05, anchor = CENTER)

root.mainloop()