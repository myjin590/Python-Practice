# to do list app

import tkinter
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title("To do list")
def add_task():
    #get input and store in task
    task = entry_task.get()
    #if task is not empty string
    if task!= "":
        listbox_tasks.insert(tkinter.END, task) #insert task end of task_list
        entry_task.delete(0, tkinter.END) #delete entry_box
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task")
        #show warning

def delete_task():
    try: 
        task_index = listbox_tasks.curselection()[0] #task_index = selected task
        listbox_tasks.delete(task_index) #delete task_index from listbox
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task")
        #show warning

def load_task():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="Cannot find tasks.dat")

def save_task():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open("tasks.dat", "wb"))

def deleteAll_task():
    listbox_tasks.delete(0, tkinter.END) #insert task end of task_list
       
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=3, width=50)
listbox_tasks.pack(side=tkinter.LEFT)

#scrollbar
scrollbar_task = tkinter.Scrollbar(frame_tasks)
scrollbar_task.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_tasks.yview)

entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

button_add_task = tkinter.Button(root, text="Add task", width=48, command=add_task)
button_add_task.pack()

button_delete_task = tkinter.Button(root, text="Delete task", width=48, command=delete_task)
button_delete_task.pack()

button_load_task = tkinter.Button(root, text="Load task", width=48, command=load_task)
button_load_task.pack()

button_save_task = tkinter.Button(root, text="Save task", width=48, command=save_task)
button_save_task.pack()

button_deleteAll_task = tkinter.Button(root, text="Delete all of tasks", width=48, command=deleteAll_task)
button_deleteAll_task.pack()

root.mainloop()
