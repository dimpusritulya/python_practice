import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title("Decimal to Any Base Converter")
window.geometry('1240x1240')
window.configure(bg='#333333')
            
            
frame=tkinter.Frame(bg='#333333')


label=tkinter.Label(frame,text='Converting base of a number',bg='#333333',fg='#FFFFFF',font=('Roboto','22'))

label1 = tkinter.Label(frame, text="Initial base",bg='#333333',fg='#FFFFFF',font=('Roboto','16'))
comb1 = ttk.Combobox(frame, values=['decimal'],font=('Roboto','16'))
label3=tkinter.Label(frame,text='Enter number',bg='#333333',fg='#FFFFFF',font=('Roboto','16'))
label3_entry=tkinter.Entry(frame,font=('Roboto','16'))

label2 = tkinter.Label(frame, text="Base converting into",bg='#333333',fg='#FFFFFF',font=('Roboto','16'))
comb2 = ttk.Combobox(frame, values=['decimal','binary','octal','hexal'],font=('Roboto','16'))
label4=tkinter.Label(frame,text='Converted number : ',bg='#333333',fg='#FFFFFF',font=('Roboto','18'))



def convert():
    if comb1.get()=='decimal' and comb2.get()=='binary':
        ans = str(bin(int(label3_entry.get())))
        tkinter.Label(frame, text=ans[2:],font=('Roboto','16'),bg='#333333',fg='#FFFFFF').grid(row=5, column=1)
    elif comb1.get()=='decimal' and comb2.get()=='octal':
        ans = str(oct(int(label3_entry.get())))
        tkinter.Label(frame, text=ans[2:],font=('Roboto','16'),bg='#333333',fg='#FFFFFF').grid(row=5, column=1)
    elif comb1.get()=='decimal' and comb2.get()=='hexal': 
        ans = str(hex(int(label3_entry.get())))
        tkinter.Label(frame, text=ans[2:],font=('Roboto','16'),bg='#333333',fg='#FFFFFF').grid(row=5, column=1)
    else:
        tkinter.Label(frame, text='Not Convertable',font=('Roboto','16'),bg='#333333',fg='#FFFFFF').grid(row=5, column=1)
          


convert_button=tkinter.Button(frame,text='CONVERT',font=('Roboto','18'),command=convert)

label.grid(row=0,column=0,columnspan=2,sticky='news',pady=20)
label1.grid(row=1,column=0,pady=10)
comb1.grid(row=2,column=0,padx=15)
label3.grid(row=3,column=0,pady=10)
label3_entry.grid(row=4,column=0)
label2.grid(row=1,column=1)
comb2.grid(row=2,column=1)
label4.grid(row=5,column=0,columnspan=2,pady=10)
convert_button.grid(row=3,column=1,rowspan=2)

frame.pack()

window.mainloop()