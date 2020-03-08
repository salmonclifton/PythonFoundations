#!/usr/bin/env python
from pprint import pprint  # For pretty printing
import noaa_coops as nc
from tkinter import *
import pandas as pd

class Application(Frame):
    def __init__(self, master):
        """ Initialize the frame. """
        super(Application, self).__init__(master)
        self.location_txt = Text(self, wrap = WORD)
        self.level_txt = Text(self, wrap = WORD)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create button, text, and entry widgets. """
        # create instruction label for radio buttons
        Label(self,
              text="Location:"
              ).grid(row=1, column=0, sticky=W)

        # create variable for a single tidal observation station
        self.location = StringVar()
        self.location.set(None)

        # create body part radio buttons
        locations = ["Seattle", "Bremerton", "Anacortes"]
        row = 2
        column = 0
        for location in locations:
                    Radiobutton(self,
                                text = location,
                                variable = self.location,
                                value = location
                                ).grid(row = row, column = column, sticky = W)
                    row += 1

        # create a submit button
        Button(self,
               text = "Click for current conditions",
               command = self.set_location
               ).grid(row = 5, column = 0, sticky = W)

        self.location_txt = Text(self, height = 5, width = 50,  wrap = WORD)
        self.location_txt.grid(row = 6, column = 0, sticky = W)


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

        level_text = str(water_level.iloc[0]['predicted_wl'])
        water_level = float(water_level.iloc[0]['predicted_wl'])
        #Update text area and display user's favorite movie type.
        message = "Displaying current conditions for "
        message += self.location.get()
        message += ".\nWater level = "
        message += level_text

        if water_level < 6.5:
            message += "\nThe beach is yours!"
        elif water_level < 7.0:
            message += "\nGo if you dare but wear boots and hav an exit strategy!"
        else:
            message += "\nNo go, man. The tide is high."
        self.location_txt.delete(0.0, END)
        self.location_txt.insert(0.0, message)

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