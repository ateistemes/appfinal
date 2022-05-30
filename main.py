import tkinter as tk
from tkinter import ttk
import mycode
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw


global file
global reset
class windows(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Adding a title to the window
        self.wm_title("Test Application")

        # creating a frame and assigning it to container
        container = tk.Frame(self, height=700, width=600)
        # specifying the region where the frame is packed in root
        container.pack(side="top", fill="both", expand=True)

        # configuring the location of the container using grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # We will now create a dictionary of frames
        self.frames = {}
        # we'll create the frames themselves later but let's add the components to the dictionary.
        for F in (WelcomePage, MainPage):
            frame = F(container, self)

            # the windows class acts as the root window for the frames.
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Using a method to switch frames
        self.show_frame(WelcomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        # raises the current frame to the top
        frame.tkraise()
class WelcomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Main Page")
        label.pack(padx=10, pady=10)

        self.welcome_image = Image.open("175-1750430_sagiri-loli-eromangasensei-welcome-cartoon-hd-png-download.png")
        self.welcome_image = ImageTk.PhotoImage(self.welcome_image)
        self.lbl = tk.Label(self, image = self.welcome_image).pack()
        self.logo_image = Image.open("logoalatoo.png")
        self.logo_image = ImageTk.PhotoImage(self.logo_image)
        self.logo = tk.Label(self,image=self.logo_image).pack(side='bottom')
        # We use the switch_window_button in order to call the show_frame() method as a lambda function
        switch_window_button = tk.Button(
            self,
            text="++++++start++++++",
            command=lambda: controller.show_frame(MainPage),
        )
        switch_window_button.pack(side="bottom", fill=tk.X)


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        self.im = Image.open('c334963f3b5977997bd2ef4ebf325ab8.jpg')
        self.im = ImageTk.PhotoImage(self.im)
        self.lbl = tk.Label(self,image=self.im).pack()
        self.btn = tk.Button(self, command= lambda: self.ask(), text="choose your file").pack(fill=tk.X)
        # We use the switch_window_button in order to call the show_frame() method as a lambda function
        switch_window_button = tk.Button(
            self,
            text="back",
            command=lambda: controller.show_frame(WelcomePage),
        )
        switch_window_button.pack(side="bottom", fill=tk.X)
    def ask(self):
        global file
        file = tk.filedialog.askopenfilename()
        global reset
        img = Image.open(file)
        image = img.copy()
        img = ImageTk.PhotoImage(img)
        reset = Image.open(file)
        reset = ImageTk.PhotoImage(reset)
        mainWindow = tk.Toplevel(self, width=img.width(),height=img.height())
        label = tk.Label(mainWindow, image=img).pack(side='left')
        ###buttons
        sepia = tk.Button(mainWindow, text="sepia",command=mycode.sepia(image)).pack(anchor='nw')
        grey = tk.Button(mainWindow, text="greyshade",command=mycode.grey(image)).pack(anchor='nw')
        blackwhite = tk.Button(mainWindow, text="black and white",command=mycode.blacwhite(image)).pack(anchor='nw')
        negative = tk.Button(mainWindow, text="negative", command=mycode.negative(image)).pack(anchor='nw')


        mainWindow.mainloop()






if __name__ == "__main__":
    application = windows()
    application.mainloop()

