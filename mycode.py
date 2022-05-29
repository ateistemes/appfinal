try:
    import random
    import sys
    from tkinter import filedialog
    from PIL import Image, ImageDraw, ImageTk
except:
    print("WARNING: PIL modules not found; you must install the Python Imaging Library", file=sys.stderr)

###
def pickfile():
    res = filedialog.askopenfilename() # filetypes = [('image file', '*.jpg'), ('image file', '*.jpeg')])
    if res is None:
        print("Error: no file selected, returning an empty string")
        return ""
    else:
        return res
