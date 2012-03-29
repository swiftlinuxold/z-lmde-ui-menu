#!/usr/bin/env python
import pygtk
pygtk.require('2.0')
import gtk
import os

class App:
    def __init__(self):
        self.window = gtk.Window(type=gtk.WINDOW_TOPLEVEL)
        self.window.set_title("Exit OS")
        
        self.hbox = gtk.HBox()
            
        self.button_lock = gtk.Button(label='Lock')
        self.button_logout = gtk.Button(label='Log Out')

        self.hbox.pack_start(self.button_lock)
        self.hbox.pack_start(self.button_logout)

        self.button_lock.connect('clicked', self.lock)
        self.button_logout.connect('clicked', self.logout)

        self.window.connect('destroy', self.quit)
        self.window.add(self.hbox)

        self.window.show_all()

        gtk.main()

    def lock (self, widget, callback_data=None):
        os.system ('xlock')
     
    def logout(self, widget, callback_data=None):
        os.system ('sh logout_script.sh')

     

    def quit(self, widget, callback_data=None):
        gtk.main_quit() 

if __name__ == "__main__":
    app = App()
