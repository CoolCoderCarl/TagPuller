import tkinter
import get_info_db


def click_download():
    """
    Click to download from Internet
    :return:
    """
    # pass
    download = 'Result from Internet {}'.format(input_text.get())
    lbl_status.configure(text=download)


def click_from_db():
    """
    Click to get from database
    :return:
    """
    # pass
    lbl_status.configure(text="Get from database")
    lbl_tags_counter_value.configure(text=get_info_db.test_show_data())


# Window initialization and properties
window = tkinter.Tk()
window.title('HTML tags gatherer')
window.geometry('500x500')
window.minsize(width=350, height=350)


# Frames
frame_input = tkinter.Frame(window, width=500, height=250, bg='blue')
frame_tags = tkinter.Frame(window, width=250, height=250, bg='yellow')
frame_status = tkinter.Frame(window, width=250, height=250, bg='red')

frame_input.place(relx=0, rely=0, relwidth=1, relheight=0.5)
frame_tags.place(relx=0, rely=0.5, relwidth=0.5, relheight=0.5)
frame_status.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.5)

# frame_input.grid(row=0, column=0, columnspan=2, sticky="we")
# frame_tags.grid(row=1, column=0, sticky="wens")
# frame_status.grid(row=1, column=1, sticky="wens")

# Labels
lbl_tags_counter = tkinter.Label(frame_tags, text="Tags count")
lbl_tags_counter_value = tkinter.Label(frame_tags, text="Count of tags")
lbl_tags_title = tkinter.Label(frame_tags, text="Tags")
lbl_tags_title_value = tkinter.Label(frame_tags, text="Test query")

lbl_status = tkinter.Label(frame_status, text="Status")
# lbl = tkinter.Label()
# lbl = tkinter.Label()
# lbl = tkinter.Label()

lbl_tags_counter.grid(row=0, column=0, sticky="w", padx=10, pady=10)
lbl_tags_counter_value.grid(row=0, column=1, sticky="e", padx=10, pady=10)
lbl_tags_title.grid(row=1, column=0, sticky="w", padx=10, pady=10)
lbl_tags_title_value.grid(row=1, column=1, sticky="e", padx=10, pady=10)

lbl_status.grid(row=0, column=0, padx=10, pady=10)


# Input
l_tmp_frame_input = tkinter.Label(frame_input, text="frame_input")
input_text = tkinter.Entry(frame_input, width=40)
input_text.focus()
input_text.grid(column=1, row=0)

# Buttons
btn_download = tkinter.Button(frame_input, text='Download', command=click_download)
btn_download.grid(column=0, row=350)

btn_frm_db = tkinter.Button(frame_input, text='From database', command=click_from_db)
btn_frm_db.grid(column=10, row=350)


# Start window
window.mainloop()
