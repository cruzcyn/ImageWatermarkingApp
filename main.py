from tkinter import *
from PIL import Image, ImageTk, ImageDraw
from urllib.request import urlopen

# Consider having a global variable for the watermark

def add_watermark():
    img_url = img_route.get()
    user_text = watermark_text.get()

    user_img = Image.open(urlopen(img_url))
    finished_img = ImageDraw.Draw(user_img)
    finished_img.text(xy=(0,0), text=user_text, fill="white")

    display_img = ImageTk.PhotoImage(user_img)

    image_label = Label(image=display_img)
    image_label.image = display_img
    image_label.grid(row=3, column=0, columnspan=2)

# CREATE INTERFACE
window = Tk()
window.title("Image Watermarking")
window.minsize(width=500, height=500)

# Upload img
img_route = Entry(width=30)
img_route.insert(END, string="URL of your image")
img_route.grid(row=0, column=0)

# Upload watermark
watermark_text = Entry(width=30)
watermark_text.insert(END, string="Type what you want your watermark to say.")
watermark_text.grid(row=1, column=0)

# Add watermark to image
convert_img = Button(text="Add your watermark!", command=add_watermark)
convert_img.grid(row=2, column=0, columnspan=2)

window.mainloop()