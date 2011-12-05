#! /usr/bin/env python

# Check for root user login
import os, sys
if not os.geteuid()==0:
    sys.exit("\nOnly root can run this script\n")

# Get your username (not root)
import pwd
uname=pwd.getpwuid(1000)[0]

# The remastering process uses chroot mode.
# Check to see if this script is operating in chroot mode.
# /home/mint directory only exists in chroot mode
is_chroot = os.path.exists('/home/mint')
dir_develop=''
if (is_chroot):
	dir_develop='/usr/local/bin/develop'	
else:
	dir_develop='/home/'+uname+'/develop'

# Everything up to this point is common to all Python scripts called by shared-*.sh
# =================================================================================

# THIS IS THE SCRIPT FOR CONFIGURING THE MAIN MENU

print '================================='
print 'BEGIN THE MAIN MENU CONFIGURATION'

# Remove menu-xdg (not provided in antiX Linux)
os.system('apt-get remove -y menu-xdg')

os.system('apt-get install -y xscreensaver') # Add XScreenSaver

import shutil

print 'FINISHED THE MAIN MENU CONFIGURATION'
print '===================================='
