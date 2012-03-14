#!/bin/bash
# From antiX Linux
# Modified to remove the sudo

if which persist-config &> /dev/null; then
    sudo persist-config --shutdown --command halt
else
    halt
fi

