#!/bin/sh
# Filename:      auto-icewm-menu.sh
# Purpose:       automate icewm menu in conjunction with icewm-xdg-menu
# Authors:       anticapitalista for antiX
# Latest change: 26 December 2010
#
################################################################################

icewm-xdg-menu --terminal 'roxterm -e %s' --default-entry-icon --default-entry-icon /usr/share/icons/gTangish-2.0a1/32x32/apps/preferences-desktop-theme.png --with-theme-paths --theme gTangish-2.0a1 --entire-menu > ~/.icewm/application  
