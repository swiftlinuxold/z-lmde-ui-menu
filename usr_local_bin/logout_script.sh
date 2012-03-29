#!/bin/sh
# From antiX Linux

kill -TERM $(xprop -root _BLACKBOX_PID | awk '{print $3}')
killall icewm-session
killall icewm 
