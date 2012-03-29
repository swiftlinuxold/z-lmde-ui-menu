#!/usr/bin/env python
import pygtk
pygtk.require('2.0')
import gtk
import time
import os

class App:
    def __init__(self):
        self.window = gtk.Window(type=gtk.WINDOW_TOPLEVEL)
        self.hbox = gtk.HBox()
        
        self.button_lock = gtk.Button(label='Lock')
        self.button_logout = gtk.Button(label='Log Out')
        self.button_reboot = gtk.Button(label='Reboot')
        self.button_poweroff = gtk.Button(label='Power Off')
        
        self.hbox.pack_start(self.button_lock)
        self.hbox.pack_start(self.button_logout)
        self.hbox.pack_start(self.button_reboot)
        self.hbox.pack_start(self.button_poweroff)
        
        self.button_lock.connect('clicked', self.button_lock)
        self.button_logout.connect('clicked', self.button_logout)
        self.button_reboot.connect('clicked', self.button_reboot)
        self.button_poweroff.connect('clicked', self.button_poweroff)
        
        self.window.connect('destroy', self.quit)
        
        self.window.add(self.hbox)
        self.window.show_all()
        gtk.main()

    def button_lock (self, widget, callback_data=None):
        os.system ('xlock')
        gtk.main_quit()
        
    def button_logout (self, widget, callback_data=None):
        os.system ('killall icewm-session')
        
    def button_reboot (self, widget, callback_data=None):
        os.system ('sh /usr/local/bin/reboot.sh')
        
    def button_poweroff (self, widget, callback_data=None):
        os.system ('sh /usr/local/bin/shutdown.sh')
        
    def quit(self, widget, callback_data=None):
        gtk.main_quit()

if __name__ == "__main__":
    app = App()

