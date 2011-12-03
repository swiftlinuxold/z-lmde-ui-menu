
# Filename:      shutdown.sh
# Purpose:       shutdown from exit menu
# Authors:       anticapitalista for antiX
# Latest change: 05 December 2010
# Thanks to secipolla
################################################################################

#!/bin/sh

dbus-send --system --print-reply --dest="org.freedesktop.Hal" /org/freedesktop/Hal/devices/computer org.freedesktop.Hal.Device.SystemPowerManagement.Shutdown