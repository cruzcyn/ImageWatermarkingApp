from tkinter import *
from PIL import Image, ImageTk, ImageDraw, ImageFont
from urllib.request import urlopen

img_font = ImageFont.load_default(size=50)

def add_watermark():
    img_url = img_route.get()
    user_text = watermark_text.get()

    with Image.open(urlopen(img_url)) as user_img:
        user_img.resize((500, 500))
        finished_img = ImageDraw.Draw(user_img)
        finished_img.text(xy=(0,0), text=user_text, fill="white", font=img_font)
        display_img = ImageTk.PhotoImage(user_img)

    image_label = Label(image=display_img)
    image_label.image = display_img
    image_label.grid(row=3, column=0, columnspan=2)

# CREATE INTERFACE
window = Tk()
window.title("Image Watermarking")
window.minsize(width=500, height=200)
window.config(padx=30, pady=30)

# Upload img
img_route_label = Label(text="Paste the URL of your image:")
img_route_label.grid(row=0, column=0)

img_route = Entry(width=50)
img_route.grid(row=0, column=1)

# Upload watermark
watermark_label = Label(text="Enter the text of your watermark:")
watermark_label.grid(row=1, column=0)

watermark_text = Entry(width=50)
watermark_text.grid(row=1, column=1)

# Add watermark to image
convert_img = Button(text="Add your watermark!", command=add_watermark)
convert_img.grid(row=2, column=0, columnspan=2)

window.mainloop()