#!/usr/bin/env python
import pygtk
pygtk.require('2.0')
import gtk
import os

class App:
    def __init__(self):
		# Create window
        self.window = gtk.Window(type=gtk.WINDOW_TOPLEVEL)
        self.window.set_title("Exit OS")
        
        # Create horizontal boxes
        self.hbox = gtk.HBox()
            
        # Create buttons
        self.button_lock = gtk.Button(label='Lock')
        self.button_logout = gtk.Button(label='Log Out')
        self.button_reboot = gtk.Button(label='Reboot')
        self.button_poweroff = gtk.Button(label='Power Off')

        # Pack buttons into horizontal box
        self.hbox.pack_start (self.button_lock)
        self.hbox.pack_start (self.button_logout)
        self.hbox.pack_start (self.button_reboot)
        self.hbox.pack_start (self.button_poweroff)

        # Responses from clicking on buttons
        self.button_lock.connect('clicked', self.lock)
        self.button_logout.connect('clicked', self.logout)
        self.button_reboot.connect('clicked', self.reboot)
        self.button_poweroff.connect('clicked', self.poweroff)

        # Close window if you click on the X in the upper right corner
        self.window.connect('destroy', self.quit)
        
        # Add horizontal box to window
        self.window.add(self.hbox)

        # Show window
        self.window.show_all()

        gtk.main()

    def lock (self, widget, callback_data=None):
        os.system ('xlock')
     
    def logout (self, widget, callback_data=None):
        os.system ('sh /usr/local/bin/logout_script.sh')

    def reboot (self, widget, callback_data=None):
        os.system ('sh /usr/local/bin/reboot.sh')
        
    def poweroff (self, widget, callback_data=None):
        os.system ('sh /usr/local/bin/shutdown.sh')

    def quit(self, widget, callback_data=None):
        gtk.main_quit() 

if __name__ == "__main__":
    app = App()
