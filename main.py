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
	dir_user = '/home/mint'
else:
	dir_develop='/home/' + uname + '/develop'
	dir_user = '/home/' + uname

# Everything up to this point is common to all Python scripts called by shared-*.sh
# =================================================================================

# THIS IS THE SCRIPT FOR CONFIGURING THE MAIN MENU
# Special thanks to antiX Linux for the exit menu and automatic menu updating

def message (string):
    os.system ('echo ' + string)

message ('=================================')
message ('BEGIN THE MAIN MENU CONFIGURATION')

import subprocess

# Add xlockmore and icons
message ('INSTALLING xlockmore')
os.system ('dpkg -i ' + dir_develop + '/ui-menu/deb/xlockmore*.deb')
message ('INSTALLING gtangish-2.0a1-icons')
os.system ('dpkg -i ' + dir_develop + '/ui-menu/deb/gtangish*.deb')

# Allow the user to reboot or shut down
os.system ('chmod u+s /sbin/shutdown')

# Add the exit-os.py menu
import shutil
src = dir_develop + '/ui-menu/usr_local_bin/exit-os.py'
dest = '/usr/local/bin/exit-os.py'
shutil.copyfile(src, dest)
os.system ('chmod a+rwx ' + dest)

# Add the logout script menu
src = dir_develop + '/ui-menu/usr_local_bin/logout_script.sh'
dest = '/usr/local/bin/logout_script.sh'
shutil.copyfile(src, dest)
os.system ('chmod a+rwx ' + dest)

# Add the reboot script menu
src = dir_develop + '/ui-menu/usr_local_bin/reboot.sh'
dest = '/usr/local/bin/reboot.sh'
shutil.copyfile(src, dest)
os.system ('chmod a+rx ' + dest)

# Add the shutdown script menu
src = dir_develop + '/ui-menu/usr_local_bin/shutdown.sh'
dest = '/usr/local/bin/shutdown.sh'
shutil.copyfile(src, dest)
os.system ('chmod a+rx ' + dest)


# Configure automatic menu updates

def create_dir (dir_to_create):
    if not (os.path.exists(dir_to_create)):
        os.mkdir (dir_to_create)

create_dir ('/usr/share/applications/antix/')
src = dir_develop + '/ui-menu/usr_share_applications_antix/icewm-menu.desktop'
dest = '/usr/share/applications/antix/icewm-menu.desktop'
shutil.copyfile(src, dest)

os.system ('ln -s /etc/xdg/menus/lxde-applications.menu /etc/xdg/menus/applications.menu')

src = dir_develop + '/ui-menu/usr_local_bin/auto-icewm-menu.sh'
dest = '/usr/local/bin/auto-icewm-menu.sh'
shutil.copyfile(src, dest)
os.system ('chmod a+rwx ' + dest)
if (is_chroot):
    os.system ('chown -R mint:users ' + dest)
else:
    os.system ('chown -R ' + uname + ':users ' + dest)

src = dir_develop + '/ui-menu/usr_local_bin/icewm-xdg-menu'
dest = '/usr/local/bin/icewm-xdg-menu'
shutil.copyfile(src, dest)
os.system ('chmod a+rwx ' + dest)
if (is_chroot):
    os.system ('chown -R mint:users ' + dest)
else:
    os.system ('chown -R ' + uname + ':users ' + dest)
    
# menu file
src = dir_develop + '/ui-menu/etc_X11_icewm/menu'
dest = '/etc/X11/icewm/menu'
shutil.copyfile(src, dest)

dest = dir_user + '/.icewm/menu'
shutil.copyfile(src, dest)

print 'FINISHED THE MAIN MENU CONFIGURATION'
print '===================================='
