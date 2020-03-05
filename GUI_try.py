from tkinter import *

class Application(Frame):
    def __init__(self, master):
        """ Initialize the frame. """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create button, text, and entry widgets. """
        # create instruction label
        self.inst_lbl = Label(self, text = "Select location")
        self.inst_lbl.grid(row = 0, column = 0, sticky = W)

        # create instruction label
        Label(self,
              text="Select one:"
              ).grid(row=1, column=0, sticky=W)

        # create variable for single, favorite type of movie
        self.location = StringVar()
        self.location.set(None)

        """
        # create buttons in the frame
        bttn1 = Button(root, text="Settings")
        entry1 = Entry(root)

        bttn1
        """

        # create location radio buttons
        Radiobutton(self,
                    text="Location1",
                    variable=self.location,
                    value="loc1",
                    command=self.update_text
                    ).grid(row=2, column=0, sticky=W)

        Radiobutton(self,
                    text="Location2",
                    variable=self.location,
                    value="loc2",
                    command=self.update_text
                    ).grid(row=3, column=0, sticky=W)

        Radiobutton(self,
                    text="Location 3",
                    variable=self.location,
                    value="loc3",
                    command=self.set_location
                    ).grid(row=4, column=0, sticky=W)

        # create text widget to display message
        self.results = Text(self, width = 35, height = 5, wrap = WORD)
        self.results.grid(row = 3, column = 0, columnspan = 2, sticky = W)



    def set_location(self):
        """ Update text area and display user's favorite movie type. """
        message = "Displaying current conditions for "
        message += self.location.get()

        self.results.delete(0.0, END)
        self.results.insert(0.0, message)

"""
        def reveal(self):
            
            contents = self.pw_ent.get()
            if contents == "secret":
                message = "Here's the secret to living to 100: live to 99 " \
                          "and then be VERY careful."
            else:
                message = "That's not the correct password, so I can't share " \
                          "the secret with you."
            self.secret_txt.delete(0.0, END)
            self.secret_txt.insert(0.0, message)"""

# main
# create root window
root = Tk()
root.title("Tide is High")
root.geometry("600x400")

# create a frame int the window to hold other widgets
app = Frame(root)
app.grid()

root.mainloop()