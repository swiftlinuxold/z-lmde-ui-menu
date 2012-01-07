#!/bin/sh

# This is a modified version of the script /usr/local/bin/exitantix.sh from antiX Linux.

export Logout='

<window title="Log Out" window-position="1">

<vbox>
  <frame>
  <hbox>
	<vbox>
	  <hbox>
		<button>
		<input file>"/usr/share/icons/gTangish-2.0a1/32x32/actions/gnome-lockscreen.png"</input>
		<action>xscreensaver-command -lock</action>
                <action>EXIT:close</action>
		</button>
		<text use-markup="true" width-chars="15"><label>"Lock Screen"</label></text>
      </hbox>
	  <hbox>
		<button>
		<input file>"/usr/share/icons/gTangish-2.0a1/32x32/apps/gnome-session-reboot.png"</input>
		<action>reboot.sh</action>
		</button>
		<text use-markup="true" width-chars="15"><label>"Reboot"</label></text>
	  </hbox>
	</vbox>

	<vbox>
	  <hbox>
		<button>
		<input file>"/usr/share/icons/gTangish-2.0a1/32x32/apps/gnome-session-logout.png"</input>
		<action>logouthelper.sh</action>
		</button>
		<text use-markup="true" width-chars="15"><label>"Log Out"</label></text>
      </hbox>
	  <hbox>
		<button>
		<input file>"/usr/share/icons/gTangish-2.0a1/32x32/apps/gnome-session-halt.png"</input>
		<action>shutdown.sh</action>
		</button>
		<text use-markup="true" width-chars="15"><label>"Shutdown"</label></text>
	  </hbox>
	</vbox>
  </hbox>
  </frame>
		
  <hbox>
	<button>
	  <label>"Close"</label>
	  <input file>"/usr/share/icons/gTangish-2.0a1/16x16/actions/dialog-cancel.png"</input>
	  <action>EXIT:close</action>
	</button>
  </hbox>
</vbox>
  
</window>
'

gtkdialog -c --program=Logout
unset Logout
