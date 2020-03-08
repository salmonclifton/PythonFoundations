#!/usr/bin/env python
from pprint import pprint  # For pretty printing
import noaa_coops as nc
from tkinter import *
import pandas as pd

class Application(Frame):
    def __init__(self, master):
        """ Initialize the frame. """
        super(Application, self).__init__(master)
        self.results_txt = Text(self, wrap = WORD)
        self.settings_txt = Text(self, wrap = WORD)
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

        # create variable for a single tidal observation station
        self.location = StringVar()
        self.location.set(None)

        # create location radio buttons
        Radiobutton(self,
                    text="Location1",
                    variable=self.location,
                    value="Seattle",
                    command=self.set_location
                    ).grid(row=2, column=0, sticky=W)

        Radiobutton(self,
                    text="Location2",
                    variable=self.location,
                    value="loc2",
                    command=self.set_location
                    ).grid(row=3, column=0, sticky=W)

        Radiobutton(self,
                    text="Location 3",
                    variable=self.location,
                    value="loc3",
                    command=self.set_location
                    ).grid(row=4, column=0, sticky=W)

        # create text widget to display message
        self.results_txt.grid(row=5, column=0, columnspan=3, sticky=N+E+S+W)


    def set_location(self):
        station = self.location.get()
        if station == "Seattle":
            seattle = nc.Station(9447130)
            pprint(seattle.lat_lon['lat'])
            pprint(seattle.lat_lon['lon'])
            water_level = seattle.get_data(
                begin_date="20200307 16:18",
                end_date="20200307 16:18",
                product="predictions",
                datum="MLLW",
                units="english",
                time_zone="lst_ldt")

        #Update text area and display user's favorite movie type.
        message = "Displaying current conditions for "
        message += self.location.get()

        print(type(water_level))
        print(water_level)
        """if level < 7:
            print("Start walking!")"""

        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, message)



# main
# create root window
root = Tk()
root.title("Tide is High")
root.geometry("600x400")



#pprint(current)

# create a frame int the window to hold other widgets
app = Application(root)
#app.grid()

root.mainloop()