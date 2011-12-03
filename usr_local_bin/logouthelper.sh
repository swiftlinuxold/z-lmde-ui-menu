# File Name: logouthelper.sh
# Purpose: clean logout from fluxbox and/or icewm
# Authors: OU812 for antiX
# Latest Change: 28 October 2010
############################################################

#!/bin/sh

kill -TERM $(xprop -root _BLACKBOX_PID | awk '{print $3}')
killall icewm-session
killall icewm 