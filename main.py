from tkinter import *

# Consider having a global variable for the watermark

# Button functions:
def upload_img():
    pass


def upload_watermark():
    pass


def add_watermark():
    pass

# CREATE INTERFACE
window = Tk()
window.title("Image Watermarking")
window.minsize(width=500, height=500)

# Upload img
img_route = Entry(width=30)
img_route.grid(row=0, column=0)

img_upload_btn = Button(text="Upload Image", command=upload_img)
img_upload_btn.grid(row=0, column=1)

# Upload watermark
watermark_route = Entry(width=30)
watermark_route.grid(row=1, column=0)

watermark_upload_btn = Button(text="Upload Watermark", command=upload_watermark)
watermark_upload_btn.grid(row=1, column=1)

# Add watermark to image
convert_img = Button(text="Add your watermark!", command=add_watermark)
convert_img.grid(row=2, column=0, columnspan=2)

window.mainloop()