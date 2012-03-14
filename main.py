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
print '================================='
print 'BEGIN THE MAIN MENU CONFIGURATION'

import subprocess

def install_pkg_antix (name1, name2, url):
    # First check for package
    # Credit: http://stackoverflow.com/questions/3387961/check-if-a-package-is-installed
    devnull = open (os.devnull,"w")
    retval = subprocess.call(["dpkg","-s",name1],stdout=devnull,stderr=subprocess.STDOUT)
    devnull.close()
    if retval == 0:
        print (name1 + ' is already installed')
    else:
        print 'DOWNLOADING ' + name1 + ' FROM ' + url
        wget_command = 'wget -nv -nd -nH -r -l1 --no-parent -A '
        deb_file = name1 + '_*' + name2
        wget_command = wget_command + chr(39) + deb_file + chr(39) + ' '
        wget_command = wget_command + url
        print wget_command
        os.system (wget_command)
        os.system ('dpkg -i ' + deb_file)
        os.system ('rm ' + deb_file)
        os.system ('rm robot*')

# Need for exit-antix (logout options): 
# gtkdialog, dbus (already installed), udisks (already installed), xlockmore
# gtangish-2.0a1-icons
install_pkg_antix ('gtkdialog', '_i386.deb', 'http://ftp.us.debian.org/debian/pool/main/g/gtkdialog/')
install_pkg_antix ('xlockmore', '_i386.deb', 'http://ftp.us.debian.org/debian/pool/main/x/xlockmore/')
install_pkg_antix ('gtangish-2.0a1-icons', '.deb', 'http://www.daveserver.info/antiX/main/')
install_pkg_antix ('exit-antix', '.deb', 'http://www.daveserver.info/antiX/main/')
os.system ('chmod u+s /sbin/halt')
os.system ('chmod u+s /sbin/shutdown')

# Configure automatic menu updates
import shutil

def create_dir (dir_to_create):
    if not (os.path.exists(dir_to_create)):
        os.mkdir (dir_to_create)

create_dir ('/usr/share/applications/antix/')
src = dir_develop + '/ui-menu/usr_share_applications_antix/icewm-menu.desktop'
dest = '/usr/share/applications/antix/icewm-menu.desktop'
shutil.copyfile(src, dest)

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
    
src = dir_develop + '/ui-menu/usr_local_bin/reboot.sh'
dest = '/usr/local/bin/reboot.sh'
shutil.copyfile(src, dest)
os.system ('chmod a+rx ' + dest)

src = dir_develop + '/ui-menu/usr_local_bin/shutdown.sh'
dest = '/usr/local/bin/shutdown.sh'
shutil.copyfile(src, dest)
os.system ('chmod a+rx ' + dest)

# menu file
src = dir_develop + '/ui-menu/etc_X11_icewm/menu'
dest = '/etc/X11/icewm/menu'
shutil.copyfile(src, dest)

dest = dir_user + '/.icewm/menu'
shutil.copyfile(src, dest)

print 'FINISHED THE MAIN MENU CONFIGURATION'
print '===================================='
