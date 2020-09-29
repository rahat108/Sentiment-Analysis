# import the library
from appJar import gui
import subprocess

# handle button events
def press(button):
    if button == "Cancel":
        app.stop()
    else:
        key = app.getEntry("Keyword")
        day = app.getEntry("Days")
        comm = "python binder.py "+key+" "+day
        #print(comm)
        subprocess.call(comm)

# create a GUI variable called app
app = gui("Sentiment Analysis", "600x400")
app.setBg("lightblue")
app.setFont(20)

# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Sentiment Analysis")
app.setLabelFg("title", "black")

app.addLabelEntry("Keyword")
app.addLabelEntry("Days")

# link the buttons to the function called press
app.addButtons(["Submit"], press)

#app.setFocus("Username")

# start the GUI
app.go()