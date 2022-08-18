from tkinter import *
import tkinter
# from tkinter import ttk
# from tkinter import messagebox
from image_detection import *
from PIL import Image, ImageTk
from tkinter.font import Font
from tkinter.ttk import Combobox

from string import ascii_uppercase
from os.path import exists
import shutil
# class Animal_Gui(tkinter.Frame):


#     Animal_Lots =   ('ant', 'beaver', 'cricket', 'duck', 'fish',
#                      'horse', 'mosquito', 'otter', 'pig', 'sloth', 'crab', 
#                      'dodo', 'dog', 'elephant', 'flamingo', 'hedgehog', 
#                      'peacock', 'rat', 'shrimp', 'spider', 'swan', 'badger', 
#                      'blowfish', 'camel', 'giraffe', 'kangaroo', 'ox', 
#                      'rabbit', 'sheep', 'snail', 'turtle', 'whale', 'bison', 
#                      'deer', 'dolphin', 'hippo', 'monkey', 'penguin', 'rooster', 
#                      'skunk', 'squirrel', 'worm', 'cow', 'crocodile', 'parrot', 
#                      'rhino', 'scorpion', 'seal', 'shark', 'turkey', 'cat', 
#                      'boar',  'dragon', 'fly', 'gorilla', 'leopard', 'mammoth', 
#                      'snake', 'tiger', 'zombie-cricket', 'bus', 'zombie-fly', 
#                      'dirty-rat', 'chick', 'ram', 'bee')

#     def __init__(self):
#         ...
#         self._LotCombo['values'] = Animal_Gui.Animal_Lots
#         ...

#     ...
#     def findInBox(self, event):
#         keypress = event.char.upper()

#         if keypress in ascii_uppercase:
#             for index, lot_name in enumerate(Animal_Gui.PARKING_LOTS):
#                 if lot_name[0] >= keypress:
#                     self._LotCombo.current(index)
#                     break

def capture_animals_tkinter(label):
    animals = find_the_animals()
    label.config(text = animals)
    # messagebox.showinfo(animals)

def add_image(files, file):
    image = Image.open(files)
    photo = ImageTk.PhotoImage(image)
    Button(root, text=file, image=photo, compound=BOTTOM).pack(side= RIGHT)

def show(label2):
    label2.config(text = clicked.get())

def change_animals_in_tool_res(references, list_of_names, shu):
    global button_list
    # print(len(button_list))
    # i need a corrective mechanism: 
    # the buttons are
    animal_list = []
    for i in button_list:
        # print(i['text'].split("_")[0])
        animal_list.append(i['text'].split("_")[0])
    # print(animal_list)
    image_path = r'C:\Users\jivit\Documents\Python_Scripts\RL\image classification\tool_res'
    delete_files_from_directory(image_path)
    references2 = []
    list_of_names2 = []
    for i in range(len(references)):
        references2.append(references[shuffle[i]])
    for i in range(len(list_of_names)):
        list_of_names2.append(list_of_names[shuffle[i]])
    write_to_tool_res(references, animal_list, list_of_names)

# def setImageAs():
def check_and_save_images():
    # isExist = {}
    image_path = r'C:\Users\jivit\Documents\Python_Scripts\RL\image classification\tool_res'
    animal_list = get_images_path(image_path)
    # animal_dir_list = os.path.join(image_path, )
    for i in animal_list:
        text = i.split("_")
        animal = text[0]
        position = text[1].split(".")[0]
        image_path = "C:\\Users\\jivit\\Documents\\Python_Scripts\\RL\\image classification\\SAP_res\\"+str(animal)+"\\"+str(animal)+"_"+str(position)+".jpg"
        # dir = os.listdir(image_path)
        isExist = os.path.exists(image_path)
        if not isExist:
            src_path = "C:\\Users\\jivit\\Documents\\Python_Scripts\\RL\\image classification\\tool_res\\"+str(animal)+"_"+str(position)+".jpg"
            shutil.copyfile(src_path, image_path)

def get_images_path(image_path):
    # image_path = r'C:\Users\jivit\Documents\Python_Scripts\RL\image classification\tool_res'
    dir = os.listdir(image_path)
    return dir
def delete_files_from_directory(path):
    dir = get_images_path(path)
    # dir = os.path.join(path, dir1)
    for j in dir:
        i = os.path.join(path, j)
        # print(i)
        if os.path.isfile(i):
            os.remove(i)
    # for file_name in os.listdir(path):
    # # construct full file path
    #     file = path + file_name
    #     if os.path.isfile(file):
    #         print('Deleting file:', file)
    #         os.remove(file)

def write_to_tool_res(references,list_of_animals1, list_of_names):
    for i in range(5):
        # print(type(references[i]))
        print("being printed: ", list_of_animals1[i], list_of_names[i])
        _ = references[i].save("C:\\Users\\jivit\\Documents\\Python_Scripts\\RL\\image classification\\tool_res\\" +str(list_of_animals1[i])+"_"+str(list_of_names[i]) +".jpg")

def spit_number(i):
    j = i
    return j


def openWindow(j):
    # print(1)
    button_id = j
    global button_list
    def Update(data):
        # print(2)
        listbox.delete(0, 'end')

        # print(data)
        # put new data
        for item in data:
            listbox.insert('end', item)
    
    def selected_item(event):
        # print("somwthitn")
        # print(event.widget.winfo_parent())
        # print(button_id)
        for i in listbox.curselection():
            value = button_list[button_id]['text']
            position = value.split("_")[1].split(".")[0]
            button_list[button_id]['text'] = listbox.get(i)+"_"+str(position)+".jpg"
    
    # def just_print(event):
        # print("jell")

    def Scankey(event):
        # print(3)
        val = event.widget.get()
        # print("hello")
        print(val)
        

        if val == '':
            data = list
        else:
            data = []
            for item in list:
                if val.lower() in item.lower():
                    data.append(item)				

        
        Update(data)
    
    list = ('ant', 'beaver', 'cricket', 'duck', 'fish',
                     'horse', 'mosquito', 'otter', 'pig', 'sloth', 'crab', 
                     'dodo', 'dog', 'elephant', 'flamingo', 'hedgehog', 
                     'peacock', 'rat', 'shrimp', 'spider', 'swan', 'badger', 
                     'blowfish', 'camel', 'giraffe', 'kangaroo', 'ox', 
                     'rabbit', 'sheep', 'snail', 'turtle', 'whale', 'bison', 
                     'deer', 'dolphin', 'hippo', 'monkey','nothing', 'penguin', 'rooster', 
                     'skunk', 'squirrel', 'worm', 'cow', 'crocodile', 'parrot', 
                     'rhino', 'scorpion', 'seal', 'shark', 'turkey', 'cat', 
                     'boar',  'dragon', 'fly', 'gorilla', 'leopard', 'mammoth', 
                     'snake', 'tiger', 'zombie-cricket', 'bus', 'zombie-fly', 
                     'dirty-rat', 'chick', 'ram', 'bee')
    
    ws = Toplevel(root)
    ws.attributes('-topmost',True)
    ws.grab_set()
    ws.focus()
    entry = Entry(ws)
    entry.pack()
    entry.bind('<KeyRelease>', Scankey)
    entry.bind('<Enter>', selected_item)

    listbox = Listbox(ws)
    listbox.pack()
    Update(list)

    ws.mainloop()

root = Tk()

root.title("DCT")

clicked = StringVar()

# options =           ['ant', 'beaver', 'cricket', 'duck', 'fish',
#                      'horse', 'mosquito', 'otter', 'pig', 'crab', 
#                      'dodo', 'dog', 'elephant', 'flamingo', 'hedgehog', 
#                      'peacock', 'rat', 'shrimp', 'spider', 'swan', 'badger', 
#                      'blowfish', 'camel', 'giraffe', 'kangaroo', 'ox', 
#                      'rabbit', 'sheep', 'snail', 'turtle', 'whale', 'bison', 
#                      'deer', 'dolphin', 'hippo', 'monkey', 'penguin', 'rooster', 
#                      'skunk', 'squirrel', 'worm', 'cow', 'crocodile', 'parrot', 
#                      'rhino', 'scorpion', 'seal', 'shark', 'turkey', 'cat', 
#                      'boar',  'dragon', 'fly', 'gorilla', 'leopard', 'mammoth', 
#                      'snake', 'tiger', 'bus', 'ram']

# clicked.set( "Monday" )

# drop = OptionMenu( root , clicked , *options )
# drop.pack()

# root.geometry('350x200')

root.attributes('-topmost',True)
frame = Frame(root)
frame.pack(side=BOTTOM)
frame2 = Frame(root)
frame2.pack(side=BOTTOM)
# val = find_the_animals()
photo_list = []
button_list = []
animal_dir_list = []
list_of_names = ('first', 'second', 'third', 'fourth', 'fiveth', 'sixth', 'seventh')
references = ()
shuffle = []
def refresh_screen():
    image_path = r'C:\Users\jivit\Documents\Python_Scripts\RL\image classification\tool_res'
    delete_files_from_directory(image_path)
    global list_of_names
    global references
    val, references = find_the_animals()
    print(list_of_names)
    # print("Length of references: "+str(len(references)))
    write_to_tool_res(references, val, list_of_names)
    for widgets in frame.winfo_children():
        widgets.destroy()
    dir = get_images_path(image_path)
    global animal_dir_list
    animal_dir_list = dir
    global photo_list
    photo_list = []
    # check_and_save_images(dir)
    for file in dir:
        # print(file)
        files = os.path.join(image_path, file)
        # print(files)
        # label = Label(root, image = photo)
        # label.image = photo
        # Button(root, text=file, image=photo, compound=BOTTOM).pack(side= RIGHT)
        image = Image.open(files)
        photo = ImageTk.PhotoImage(image)
        photo_list.append((photo,file))
    
    global button_list 
    button_list = []
    # label_list = {}
    # numbers = [i for i in range(len(photo_list))]
    # print(len(photo_list))
    # for j in range(len(photo_list)):
    #     photo = photo_list[j][0]
    #     file = photo_list[j][1]
    # # for photo,file in photo_list:
    #     # label_list[str(file)] = Label( root , text = " " ).pack()
    #     # print('hello')
    #     button_list.append(Button(frame, text=str(j)+":"+file, image=photo, compound=BOTTOM,command=lambda: openWindow(numbers[j])))
        # add_image(files, file)
    # photo = photo_list[j][0]
    # file = photo_list[j][1]
    # button_list.append(Button(frame, text=str(j)+":"+file, image=photo, compound=BOTTOM,command=lambda: openWindow(numbers[j])))
    photo = photo_list[0][0]
    file = photo_list[0][1]
    print(file)
    button_list.append(Button(frame, text=file, image=photo, compound=BOTTOM,command=lambda: openWindow(0)))
    # button_list[-1].pack(side= LEFT)
    photo = photo_list[1][0]
    file = photo_list[1][1]
    button_list.append(Button(frame, text=file, image=photo, compound=BOTTOM,command=lambda: openWindow(1)))
    # button_list[-1].pack(side= LEFT)
    photo = photo_list[2][0]
    file = photo_list[2][1]
    button_list.append(Button(frame, text=file, image=photo, compound=BOTTOM,command=lambda: openWindow(2)))
    # button_list[-1].pack(side= LEFT)
    photo = photo_list[3][0]
    file = photo_list[3][1]
    button_list.append(Button(frame, text=file, image=photo, compound=BOTTOM,command=lambda: openWindow(3)))
    # button_list[-1].pack(side= LEFT)
    photo = photo_list[4][0]
    file = photo_list[4][1]
    button_list.append(Button(frame, text=file, image=photo, compound=BOTTOM,command=lambda: openWindow(4)))
    # button_list[-1].pack(side= LEFT)
    global shuffle
    shuffle = []
    for i in list_of_names:
        for j in range(len(button_list)):
            # print(j['text'].split("_")[1])
            # print(i.split("_")[1])
            if button_list[j]['text'].split("_")[1].split(".")[0] == i:
                button_list[j].pack(side=LEFT)
                shuffle.append(j)
        # i.pack(side= LEFT)
        # how does it get shuffled?
        # 

Button(root, text='Capture', compound=BOTTOM, command=refresh_screen).pack(side= TOP)
Button(root, text="Commit", compound=BOTTOM, command=check_and_save_images).pack(side=BOTTOM)
# Button(root, text="Add", compound=BOTTOM, command=lambda: change_animals_in_tool_res(references, list_of_names, shuffle)).pack(side=BOTTOM)

# label.grid(row=1)

# separator = ttk.Separator(root, orient='horizontal')
# separator.pack(fill='x')
# label.pack()
# Label(root, text= "Animals").pack(pady=15)

# btn = Button(root, text = 'Click me !',
#                 command = capture_animals_tkinter).pack(pady=15)
# btn.pack(side = 'top')   

# label = Label(root, text = "")
# label.pack()
# button = Button(root, text= "Click!", command= lambda: capture_animals_tkinter(label))

# button.pack()



root.mainloop()