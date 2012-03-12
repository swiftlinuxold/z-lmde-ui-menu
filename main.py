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
install_pkg_antix ('gtkdialog_', '_i386.deb', 'http://ftp.us.debian.org/debian/pool/main/g/gtkdialog/')
install_pkg_antix ('xlockmore_', '_i386.deb', 'http://ftp.us.debian.org/debian/pool/main/x/xlockmore/')
install_pkg_antix ('exit-antix_', '.deb', 'http://www.daveserver.info/antiX/main/')

	
# wget_command = 'wget -nd -nH -r -l1 --no-parent -A '
# wget_command = wget_command + chr(39) + 'gtkdialog*i386.deb' + chr(39)
# wget_command = wget_command + ' http://ftp.us.debian.org/debian/pool/main/g/gtkdialog/'
# os.system(wget_command)
# wget -nd -nH -r -l1 --no-parent -A 'gtkdialog*i386.deb' http://ftp.us.debian.org/debian/pool/main/g/gtkdialog/
# wget -nd -r -l1 --no-parent -A 'gtkdialog*i386.deb' http://ftp.us.debian.org/debian/pool/main/g/gtkdialog/

# os.system('wget http://ftp.us.debian.org/debian/pool/main/g/gtkdialog/gtkdialog_0.7.20-4_i386.deb')
# os.system('dpkg -i gtkdialog_0.7.20-4_i386.deb')
# os.system('rm gtkdialog_0.7.20-4_i386.deb')

# Allow non-root users to shutdown, reboot, etc.
# os.system('sudo chmod u+s /sbin/poweroff')
# os.system('sudo chmod u+s /sbin/reboot')

# import shutil

# dir1 = dir_develop+'/ui-menu/usr_local_bin'
# dir2 = '/usr/local/bin'
# Copy the logout files to /usr/local/bin
# src = dir1 + '/exitswift.sh'
# dest = dir2 + '/exitswift.sh'
# shutil.copyfile(src, dest)
# os.system ('chmod a+rx ' + dest)

# src = dir1 + '/logouthelper.sh'
# dest = dir2 + '/logouthelper.sh'
# shutil.copyfile(src, dest)
# os.system ('chmod a+rx ' + dest)

# src = dir1 + '/reboot.sh'
# dest = dir2 + '/reboot.sh'
# shutil.copyfile(src, dest)
# os.system ('chmod a+rx ' + dest)

# src = dir1 + '/shutdown.sh'
# dest = dir2 + '/shutdown.sh'
# shutil.copyfile(src, dest)
# os.system ('chmod a+rx ' + dest)


print 'FINISHED THE MAIN MENU CONFIGURATION'
print '===================================='
