#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
import os

class NetworkWizard:

    def __init__(self):
        
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL) # Create a new window
        self.window.set_title("Exit OS") # Set the window title
        self.window.set_border_width(20)# Sets the border width of the window.
        self.window.connect("delete_event", self.delete_event) # Click on the X -> close window
        
        # Create vertical box
        self.vbox = gtk.VBox ()
        
        # EACH OPTION GETS ITS OWN HORIZONTAL BOX (wizard_option)
        
        # OPTION 1: Lock Screen
        self.box_image = '/usr/share/icons/gTangish-2.0a1/32x32/actions/system-lock-screen.png'
        self.box_label = 'Lock Screen'
        self.box = self.wizard_option (self.box_image, self.box_label, self.lock_screen)
        self.vbox.add (self.box)
        
        # Option 2: Log Out
        self.box_image = '/usr/share/icons/gTangish-2.0a1/32x32/apps/gnome-session-logout.png'
        self.box_label = 'Log Out'
        self.box = self.wizard_option (self.box_image, self.box_label, self.logout)
        self.vbox.add (self.box)
        
        # Option 3: Reboot
        self.box_image = '/usr/share/icons/gTangish-2.0a1/32x32/apps/gnome-session-reboot.png'
        self.box_label = 'Reboot Computer'
        self.box = self.wizard_option (self.box_image, self.box_label, self.reboot)
        self.vbox.add (self.box)
        
        # Option 4: Power Off
        self.box_image = '/usr/share/icons/gTangish-2.0a1/32x32/apps/gnome-session-halt.png'
        self.box_label = 'Power Off Computer'
        self.box = self.wizard_option (self.box_image, self.box_label, self.poweroff)
        self.vbox.add (self.box)
        
        # Show everything
        #self.table.show()
        self.window.add (self.vbox)
        self.window.show ()
        self.window.show_all ()
        
        
        
    # This callback quits the program
    def delete_event (self, widget, event, data=None):
        gtk.main_quit()
        return False
        
    def lock_screen (self, widget, callback_data=None):
        os.system ('xlock')
        
    def logout (self, widget, callback_data=None):
        os.system ('sh /usr/local/bin/logout_script.sh')
        
    def reboot (self, widget, callback_data=None):
        os.system ('sh /usr/local/bin/reboot.sh')
    
    def poweroff (self, widget, callback_data=None):
        os.system ('sh /usr/local/bin/shutdown.sh')
    
    def wizard_option (self, filename_image, string_label, fctn_action):
        # Horizontal box
        self.hbox = gtk.HBox ()
        
        # Button icon
        self.image = gtk.Image ()
        self.image.set_from_file (filename_image)
        self.image.show ()
        
        # Button
        self.button = gtk.Button()
        self.button.set_size_request(64, 64)
        self.button.connect('clicked', fctn_action)
        self.button.add(self.image) # Add image to button
        self.button.show()
        self.hbox.pack_start(self.button, False, False, 0)
        
        # Label
        self.label = gtk.Label (' ' + string_label)
        self.label.set_alignment (0, .5)
        self.label.show ()
        
        self.hbox.pack_start(self.label, False, False, 0)
        self.hbox.show ()
        
        return self.hbox
    
def main():
    gtk.main()
    return 0       

if __name__ == "__main__":
    NetworkWizard()
    main()
