---
title: "McKade's Terminal Setup"
date: 2021-05-22T15:55:05-04:00
---

## Environment
Lately I've been rolling with [Guake](http://guake-project.org/) and [Byobu](https://www.byobu.org/). I have not tried *most* terminals, so I will not say that my environment is the best (or even good). It does, however, work well for me right now. I like the clean look and easy terminal multiplexing. I am putting this here mostly for my own reference. If you wish to be a little more like McKade, for some reason, feel free to try my terminal environment out.

## Installation
Install Guake and Byobu. The following is for Ubuntu/Debian environments. If not in one of these environments, I will leave installation as an exercise for the reader.

```
$ sudo apt install guake byobu && byobu-enable
$ which byobu | sudo tee -a /etc/shells
```

## Configuration
##t Guake config:
```
[general]
abbreviate-tab-names=false
compat-delete='delete-sequence'
default-shell='/usr/bin/byobu'
display-n=0
gtk-prefer-dark-theme=false
gtk-theme-name='Yaru-dark'
history-size=3000
infinite-history=false
max-tab-name-length=100
mouse-display=true
open-tab-cwd=true
prompt-on-quit=true
quick-open-command-line='gedit %(file_path)s'
restore-tabs-notify=true
restore-tabs-startup=true
save-tabs-when-changed=true
scroll-keystroke=true
start-at-login=true
use-default-font=true
use-popup=true
use-scrollbar=true
use-trayicon=true
window-halignment=1
window-height=98
window-losefocus=false
window-ontop=false
window-refocus=false
window-tabbar=false
window-width=100

[keybindings/local]
split-tab-vertical='<Primary><Alt>Right'

[style]
cursor-shape=1

[style/background]
transparency=94

[style/font]
allow-bold=true
palette='#343434343434:#D2D251515151:#A5A5C2C26161:#FFFFC6C66D6D:#6C6C9999BBBB:#D1D19797D9D9:#BEBED6D6FFFF:#EEEEEEEEECEC:#535353535353:#F0F00C0C0C0C:#C2C2E0E07575:#E1E1E3E38B8B:#8A8AB7B7D9D9:#EFEFB5B5F7F7:#DCDCF3F3FFFF:#FFFFFFFFFFFF:#FFFFFFFFFFFF:#323232323232'
palette-name='Espresso'
```

Copy the above into a file (e.g., `guake-prefs.txt`) and run `guake --restore-preferences guake-prefs.txt`.

---
### Byobu Config Files:

To update byobu keybindings, replace the following file with the provided content.
/usr/share/byobu/keybindings/f-keys.tmux
```
###############################################################################                                                                                                                                    
#    byobu's tmux f-key keybindings                                                                                                                                                                                
#                                                                                                                                                                                                                  
#    Copyright (C) 2011-2014 Dustin Kirkland <kirkland@byobu.org>                                                                                                                                                  
#                                                                                                                                                                                                                  
#    Authors: Dustin Kirkland <kirkland@byobu.org>                                                                                                                                                                 
#                                                                                                                                                                                                                  
#    This program is free software: you can redistribute it and/or modify                                                                                                                                          
#    it under the terms of the GNU General Public License as published by                                                                                                                                          
#    the Free Software Foundation, version 3 of the License.                                                                                                                                                       
#                                                                                                                                                                                                                  
#    This program is distributed in the hope that it will be useful,                                                                                                                                               
#    but WITHOUT ANY WARRANTY; without even the implied warranty of                                                                                                                                                
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                                                                                                                                                 
#    GNU General Public License for more details.                                                                                                                                                                  
#                                                                                                                                                                                                                  
#    You should have received a copy of the GNU General Public License                                                                                                                                             
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.                                                                                                                                         
###############################################################################                                                                                                                                    
                                                                                                                                                                                                                   
# Add F12 to the prefix list                                                                                                                                                                                       
set -g prefix F12                                                                                                                                                                                                  
                                                                                                                                                                                                                   
# Clear the slate                                                                                                                                                                                                  
source $BYOBU_PREFIX/share/byobu/keybindings/f-keys.tmux.disable                                                                                                                                                   
                                                                                                                                                                                                                   
# Byobu's Keybindings                                                                                                                                                                                              
# Documented in: $BYOBU_PREFIX/share/doc/byobu/help.tmux.txt                                                                                                                                                       
bind-key -n F1 new-window -n config byobu-config                                                                                                                                                                   
bind-key -n S-F1 new-window -n help "sh -c '$BYOBU_PAGER $BYOBU_PREFIX/share/doc/byobu/help.tmux.txt'"                                                                                                             
bind-key -n F2 new-window -c "#{pane_current_path}" \; rename-window "-"
bind-key -n C-V display-panes \; split-window -h -c "#{pane_current_path}"
bind-key -n C-H display-panes \; split-window -v -c "#{pane_current_path}"
bind-key -n C-S-F2 new-session \; rename-window "-"
bind-key -n F3 previous-window
bind-key -n F4 next-window
bind-key -n M-Left previous-window
bind-key -n M-Right next-window
bind-key -n M-Up switch-client -p
bind-key -n M-Down switch-client -n
bind-key -n S-F3 display-panes \; select-pane -t :.- 
bind-key -n S-F4 display-panes \; select-pane -t :.+ 
bind-key -n S-Up display-panes \; select-pane -U
bind-key -n S-Down display-panes \; select-pane -D
bind-key -n S-Left display-panes \; select-pane -L
bind-key -n S-Right display-panes \; select-pane -R
bind-key -n C-F3 display-panes \; swap-pane -s :. -t :.- \; select-pane -t :.-
bind-key -n C-F4 display-panes \; swap-pane -s :. -t :.+ \; select-pane -t :.+
bind-key -n C-S-F3 swap-window -t :-1 -d
bind-key -n C-S-F4 swap-window -t :+1 -d
bind-key -n M-S-Up resize-pane -U
bind-key -n M-S-Down resize-pane -D
bind-key -n M-S-Left resize-pane -L
bind-key -n M-S-Right resize-pane -R
bind-key -n F5 source $BYOBU_PREFIX/share/byobu/profiles/tmuxrc
bind-key -n M-F5 run-shell '$BYOBU_PREFIX/lib/byobu/include/toggle-utf8' \; source $BYOBU_PREFIX/share/byobu/profiles/tmuxrc
bind-key -n S-F5 new-window "$BYOBU_PREFIX/lib/byobu/include/cycle-status" \; source $BYOBU_PREFIX/share/byobu/profiles/tmuxrc
bind-key -n C-F5 send-keys ". $BYOBU_PREFIX/bin/byobu-reconnect-sockets" \; send-keys Enter
bind-key -n C-S-F5 new-window -d "byobu-select-profile -r"
bind-key -n F6 detach
bind-key -n M-F6 run-shell '$BYOBU_PREFIX/lib/byobu/include/tmux-detach-all-but-current-client'
bind-key -n S-F6 run-shell 'exec touch $BYOBU_RUN_DIR/no-logout' \; detach
bind-key -n C-F6 kill-pane
bind-key -n F7 copy-mode
bind-key -n S-F7 capture-pane -S -32768 \; save-buffer "$BYOBU_RUN_DIR/printscreen" \; delete-buffer \; new-window -n "PRINTSCREEN" "$BYOBU_EDITOR $BYOBU_RUN_DIR/printscreen"
bind-key -n M-NPage copy-mode \; send-keys NPage
bind-key -n M-PPage copy-mode \; send-keys PPage
bind-key -n F8 command-prompt -p "(rename-window) " "rename-window '%%'"
bind-key -n C-F8 command-prompt -p "(rename-session) " "rename-session '%%'"
bind-key -n S-F8 next-layout
bind-key -n M-S-F8 new-window "byobu-layout restore; clear; $SHELL"
bind-key -n C-S-F8 command-prompt -p "Save byobu layout as:" "run-shell \"byobu-layout save '%%'\""
bind-key -n F9 new-window -n config byobu-config
bind-key -n S-F9 command-prompt -p "Send command to all panes:" "run-shell \"$BYOBU_PREFIX/lib/byobu/include/tmux-send-command-to-all-panes '%%'\""
bind-key -n C-F9 command-prompt -p "Send command to all windows:" "run-shell \"$BYOBU_PREFIX/lib/byobu/include/tmux-send-command-to-all-windows '%%'\""
bind-key -n M-F9 display-panes \; setw synchronize-panes
bind-key -n M-F11 break-pane
bind-key -n C-F11 join-pane -h -s :. -t :-1
bind-key -n S-F11 resize-pane -Z
bind-key -n S-F12 source $BYOBU_PREFIX/share/byobu/keybindings/f-keys.tmux.disable \; display-message "Byobu F-keys: DISABLED"
bind-key -n C-S-F12 new-window $BYOBU_PREFIX/lib/byobu/include/mondrian
bind-key -n M-F12 source $BYOBU_PREFIX/share/byobu/keybindings/mouse.tmux.enable
bind-key -n M-IC paste-buffer

bind-key -n C-a new-window -n "ctrl-a" "byobu-ctrl-a"
```

Update `~/.byobu/color.tmux`:
```
BYOBU_DARK="\#333333"
BYOBU_LIGHT="\#EEEEEE"
BYOBU_ACCENT="\#75507B"
BYOBU_HIGHLIGHT="\#D197D9"
```

---
### .vimrc
```
set number
set tabstop=4
set softtabstop=4
set wildmenu
set incsearch
set hlsearch
```
