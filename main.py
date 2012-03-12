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

print '================================='
print 'BEGIN THE MAIN MENU CONFIGURATION'

def install_pkg_antix (name1, name2, url):
    print 'DOWNLOADING ' + name1 + ' FROM ' + url
    wget_command = 'wget -nv -nd -nH -r -l1 --no-parent -A '
    deb_file = name1 + '*' + name2
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
install_pkg_antix ('gtkdialog_', '_i386.deb', 'http://ftp.us.debian.org/debian/pool/main/g/gtkdialog/')
install_pkg_antix ('xlockmore_', '_i386.deb', 'http://ftp.us.debian.org/debian/pool/main/x/xlockmore/')
install_pkg_antix ('exit-antix_', '.deb', 'http://www.daveserver.info/antiX/main/')
install_pkg_antix ('gtangish-2.0a1-icons_', '.deb', 'http://www.daveserver.info/antiX/main/')

print 'FINISHED THE MAIN MENU CONFIGURATION'
print '===================================='
