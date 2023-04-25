import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askokcancel
from PIL import Image

# title frame on opening
isTitle = True

root = tk.Tk()
root.title('Bird Track')
root.geometry('600x450')

# containers
titleFrame = tk.Frame(root, bg='light blue', width=580, height=40, pady=3)
dispFrame = tk.Frame(root, bg='light blue', width=580, height=360, padx=3, pady=3)
navFrame = tk.Frame(root, bg='light yellow', width=580, height=40, pady=3, padx=6)

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

titleFrame.grid(row=0, sticky='ew')
dispFrame.grid(row=1, sticky='nsew')
navFrame.grid(row=2, sticky='ew')

titleFrame.grid_rowconfigure(0, weight=1)
titleFrame.grid_columnconfigure(1, weight=1)

title = tk.Label(titleFrame, text='Bird Track', font='TkHeadingFont', bg='light blue')
title.grid(row=0, column=1)
quit = tk.Button(titleFrame, text='Quit', anchor='e',
                 command=lambda: tk.messagebox.askquestion('Quit?', 'Are you sure you want to quit?'))
quit.grid(row=0, column=2, sticky='e')

dispFrame.grid_rowconfigure(0, weight=1)
dispFrame.grid_columnconfigure(1, weight=1)

welcomeText = tk.Label(dispFrame, text='Choose a task below.', font='TkHeadingFont', bg='light blue')
welcomeText.grid(row=0, column=1)


def createMenuFrame():
    isTitle = False
    dirFrame = tk.Frame(dispFrame, bg='light green', width=150, height=360, padx=3, pady=3)
    dirFrame.grid(row=0, column=0, sticky='nsew')
    dirFrame.grid_rowconfigure(0, weight=1)
    dirFrame.grid_columnconfigure(1, weight=1)
    return dirFrame


def createContentFrame():
    ioFrame = tk.Frame(dispFrame, bg='light blue', width=430, height=360, padx=3, pady=3)
    ioFrame.grid(row=0, column=1, sticky='nsew')
    ioFrame.grid_rowconfigure(0, weight=1)
    ioFrame.grid_columnconfigure(1, weight=1)
    return ioFrame


def clearFrame():
    for child in dispFrame.winfo_children():
        child.destroy()


def displayGallery():
    clearFrame()
    menuFrame = createMenuFrame()
    galInstLabel = tk.Label(menuFrame, text='Choose a date to see\nphotos from that day', font='TkSmallCaptionFont',
                            bg='light green')
    galInstLabel.grid(row=0, column=0)
    tempDates = ['01/22/2022', '02/04/2022', '03/25/2023']
    dateList = tk.Listbox(menuFrame, height=16)
    for i, date in enumerate(tempDates):
        dateList.insert(i, date)
    dateList.grid(row=1, column=0)
    # temp data, implement file i/o later
    addDateButton = tk.Button(menuFrame, text='Add Date',
                              command=lambda: dateList.insert(dateList.size() + 1, 'NEW DATE placeholder'))
    addDateButton.grid(row=2, column=0)
    delDateButton = tk.Button(menuFrame, text='Delete Date', command=lambda: confirmDelete(dateList, menuFrame))
    delDateButton.grid(row=3, column=0)

    ioFrame = createContentFrame()
    i1 = tk.Label(ioFrame, text = 'bird1.jpg', padx=3, pady=3)
    i1.grid(row=0, column=0)
    i2 = tk.Label(ioFrame, text = 'bird2.jpg', padx=3, pady=3)
    i2.grid(row=0, column=1)
    i3 = tk.Label(ioFrame, text = 'bird3.jpg', padx=3, pady=3)
    i3.grid(row=0, column=2)


def displayLog():
    clearFrame()
    menuFrame = createMenuFrame()
    logInstLabel = tk.Label(menuFrame, text='Choose a date to see or add\nbirds to your log', font='TkSmallCaptionFont',
                            bg='light green')
    logInstLabel.grid(row=0, column=0)
    tempDates = ['01/22/2022', '02/04/2022', '03/25/2023']
    dateList = tk.Listbox(menuFrame, height=16)
    for i, date in enumerate(tempDates):
        dateList.insert(i, date)
    dateList.grid(row=1, column=0)
    # temp data, implement file i/o later
    addDateButton = tk.Button(menuFrame, text='Add Date',
                              command=lambda: dateList.insert(dateList.size() + 1, 'NEW DATE placeholder'))
    addDateButton.grid(row=2, column=0)
    delDateButton = tk.Button(menuFrame, text='Delete Date', command=lambda: confirmDelete(dateList, menuFrame))
    delDateButton.grid(row=3, column=0)

    ioFrame = createContentFrame()
    tempBirdList = ['Choose bird', 'Tufted Titmouse', 'Eastern Bluebird', 'Pileated Woodpecker', 'Add new']
    birdMenuList = tk.StringVar()
    addBirdButton = tk.Button(ioFrame, text='Add bird', command=lambda: addBirdLog(ioFrame, tempBirdList))
    addBirdButton.grid(row=10, column=0)


def addBirdLog(ioFrame, birdList):
    chooseBird = ttk.Combobox(ioFrame, textvariable=birdList)
    chooseBird['values'] = (birdList)
    chooseBird.grid(row=0, column=0)
    birdQuant = tk.Spinbox(ioFrame, from_=0, to=20)
    birdQuant.grid(row=0, column=1)
    chooseBird.current(0)
    saveButton = tk.Button(ioFrame, text='Save', command=lambda: tk.messagebox.showinfo('Saved', 'Bird Saved'))
    saveButton.grid(row=10, column=1)


# separate this function, reuse menu for other sections
def displayNotes(notesButton):
    clearFrame()
    # for dates menu
    menuFrame = createMenuFrame()
    notesInstLabel = tk.Label(menuFrame, text='Choose a date to see\n or add notes', font='TkSmallCaptionFont',
                              bg='light green')
    notesInstLabel.grid(row=0, column=0)
    tempDates = ['01/22/2022', '02/04/2022', '03/25/2023']
    dateList = tk.Listbox(menuFrame, height=16)
    for i, date in enumerate(tempDates):
        dateList.insert(i, date)
    dateList.grid(row=1, column=0)
    # temp data, implement file i/o later
    addDateButton = tk.Button(menuFrame, text='Add Date',
                              command=lambda: dateList.insert(dateList.size() + 1, 'NEW DATE placeholder'))
    addDateButton.grid(row=2, column=0)
    delDateButton = tk.Button(menuFrame, text='Delete Date', command=lambda: confirmDelete(dateList, menuFrame))
    delDateButton.grid(row=3, column=0)

    # for text entry
    ioFrame = createContentFrame()
    notesText = tk.Text(ioFrame, wrap = tk.WORD, padx = 3, pady = 3 )
    notesText.grid(row=0, column=0, columnspan=2)
    notesText.insert('1.0', 'Enter your notes for the day...')
    saveButton = tk.Button(ioFrame, text='Save', command=lambda: tk.messagebox.showinfo('Saved', 'Note saved.'))
    saveButton.grid(row=1, column=1)
    discardButton = tk.Button(ioFrame, text='Discard', command=lambda: confirmDelete(notesText, ioFrame))
    discardButton.grid(row=1, column=0)


def saveNote():
    pass


def confirmDelete(widget, ioFrame):
    conf = tk.messagebox.askokcancel(
        title='Confirm Discard',
        message='Are you sure you want to discard this note?')
    if conf:
        # add conditionals for different widgets
        # widget.delete('1.0', 'end')
        deletedMessage = tk.messagebox.showwarning('Delete Confirmed', 'Deleted')


navFrame.grid_rowconfigure(0, weight=1)
navFrame.grid_columnconfigure(1, weight=1)

galButton = ttk.Button(navFrame, text='Gallery', command=displayGallery)
galButton.grid(row=0, column=0)
galLabel = tk.Label(navFrame, text='See your photos, arranged by date', font='TkSmallCaptionFont', bg='light yellow')
galLabel.grid(row=1, column=0)

logButton = ttk.Button(navFrame, text='Logbook', command=displayLog)
logButton.grid(row=0, column=1)
logLabel = tk.Label(navFrame, text='Track your sightings by date', font='TkSmallCaptionFont', bg='light yellow')
logLabel.grid(row=1, column=1)

notesButton = ttk.Button(navFrame, text='Notes', command=lambda: displayNotes(notesButton))
notesButton.grid(row=0, column=2)
notesLabel = tk.Label(navFrame, text='Save your notes by date', font='TkSmallCaptionFont', bg='light yellow')
notesLabel.grid(row=1, column=2)

root.mainloop()