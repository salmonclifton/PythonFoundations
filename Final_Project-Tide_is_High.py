#!/usr/bin/env python

"""
This application retrieves NOAA tidal data to report the current tidal height for a selected location via a gui.

Criteria included:
Contains at least one if/else statement
Creates a class to contain the related functions
Displays a graphical user interface

The application takes advantage of the noaa_coops module that is available on GitHub.
noaa_coops is a Python wrapper for the NOAA CO-OPS Tides & Currents Data and Metadata APIs.
https://github.com/GClunies/noaa_coops/blob/master/README.md

All data and metadata is handled using a Station class with methods and attributes for
retrieving metadata, observed data, and predicted data.

This application can be launched from a terminal window using the following command: python Final_Project-Tide_is_High.py
Your environment must have the following modules installed: noaa_coops and tkinter.
"""

import noaa_coops as nc
from tkinter import *
import datetime

# create a class to contain all of the functions
class Application(Frame):
    # init function to initialize the frame
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.location_txt = Text(self, height=5, width=50, wrap = WORD)
        self.level_txt = Text(self, wrap = WORD)
        self.location_txt.grid(row=6, column=0, sticky=W)

    # function that creates widgets for the gui
    def create_widgets(self):
        """ Create button, text, and entry widgets. """
        # create instruction label for radio buttons
        Label(self,
              text="Location:"
              ).grid(row=1, column=0, sticky=W)

        # create variable for a single tidal observation station
        self.location = StringVar()
        self.location.set(None)

        # create location radio buttons based on the locations list
        locations = ["Seattle", "Bremerton", "Tacoma"]
        row = 2
        column = 0
        for location in locations:
                    Radiobutton(self,
                                text = location,
                                variable = self.location,
                                value = location
                                ).grid(row = row, column = column, sticky = W)
                    row += 1

        # create a submit button which calls the set_location function
        Button(self,
               text = "Click for current conditions",
               command = self.set_location
               ).grid(row = 5, column = 0, sticky = W)



    # function that gets the location value from the gui, gets the current water level from
    # the server and outputs the go/no go message
    def set_location(self):
        location = self.location.get()
        if location == "Seattle":
            station = nc.Station(9447130)
            #pprint(seattle.lat_lon['lat'])
            #pprint(seattle.lat_lon['lon'])

        elif location == "Bremerton":
            station = nc.Station(9445958)

        elif location == "Tacoma":
            station = nc.Station(9446484)

        # gets current water level from the server for the selected location
        currentDT = datetime.datetime.now()
        current_time = currentDT.strftime("%Y%m%d %H:%M")
        time_txt = str(currentDT.strftime("%a, %b %d, %Y %H:%M"))
        water_level = station.get_data(
            begin_date=current_time,
            end_date=current_time,
            product="predictions",
            datum="MLLW",
            units="english",
            time_zone="lst_ldt")

        # format the returned water level value so that it can be used in the output message
        # as well as a value in the if statement
        level_text = str(format(water_level.iloc[0]['predicted_wl'], ".1f"))
        water_level = float(water_level.iloc[0]['predicted_wl'])

        # Update text area and display location, water level and and go/no go statement.
        message = "{}\nDisplaying current conditions for {}.".format(time_txt, self.location.get())
        #message += self.location.get()
        message += "\nWater level = {} feet".format(level_text)

        if water_level < 6.5:
            message += "\nThe beach is yours!"
        elif water_level < 7.0:
            message += "\nGo if you dare but wear boots and have an exit strategy!"
        else:
            message += "\nNo go, man. The tide is high."
        self.location_txt.delete(0.0, END)
        self.location_txt.insert(0.0, message)

##### main #####
# create root window
root = Tk()
root.title("Tide is High")
root.geometry("400x220")
# create a frame in the window to hold the widgets
app = Application(root)
# kick off the windows event loop
root.mainloop()