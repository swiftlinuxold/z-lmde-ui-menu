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

# gtkdialog is needed to run exitantix.sh, the script that provides the logout options.
# MUST download and install gtkdialog, which is not in any of the repositories in sources.list.
# Therefore, wget is needed to install it directly.
os.system('wget http://ftp.us.debian.org/debian/pool/main/g/gtkdialog/gtkdialog_0.7.20-4_i386.deb')
os.system('dpkg -i gtkdialog_0.7.20-4_i386.deb')
os.system('rm gtkdialog_0.7.20-4_i386.deb')

import shutil

dir1 = dir_develop+'/ui-menu/usr_local_bin'
dir2 = '/usr/local/bin'
# Copy the logout files to /usr/local/bin
src = dir1 + '/exitantix.sh'
dest = dir2 + '/exitantix.sh'
shutil.copyfile(src, dest)
os.system ('chmod a+rx ' + dest)

src = dir1 + '/logouthelper.sh'
dest = dir2 + '/logouthelper.sh'
shutil.copyfile(src, dest)
os.system ('chmod a+rx ' + dest)

src = dir1 + '/reboot.sh'
dest = dir2 + '/reboot.sh'
shutil.copyfile(src, dest)
os.system ('chmod a+rx ' + dest)

src = dir1 + '/shutdown.sh'
dest = dir2 + '/shutdown.sh'
shutil.copyfile(src, dest)
os.system ('chmod a+rx ' + dest)


print 'FINISHED THE MAIN MENU CONFIGURATION'
print '===================================='
