self.terminal("screen-256color")

# Bind Control key to match Screen
self.prefix("C-a")

# Use vi key bindings
self.status_keys("vi")
self.mode_keys("vi")

# Control+C-a to go to previous window
self.bind("C-a", "last-window")

# Status bar options
#set -g status-fg          green
#set -g status-bg          black
#set -g status-left-length 25
#set -g status-left        "[ #S (#(uptime | awk -F'load averages:' '{ print $2 }' | awk '{ print $2 }')) ] ["
#set -g status-right       ' ] [ #(/Users/trobrock/Scripts/power.sh) #[fg=blue]%Y-%m-%d #[fg=default]%H:%M ]'

# Window title Options
#set-window-option -g window-status-fg white
#set-window-option -g window-status-bg black
#set-window-option -g window-status-attr dim

# active window title colors
#set -g window-status-format         '#I:#W#F'
#set -g window-status-current-format '#[bg=colour245,fg=black]#I:#W '

#set-window-option -g mode-fg white
#set-window-option -g mode-bg red
#set-window-option -g mode-attr bright

# Remap split window keys
self.unbind("%") # Remove default binding since we’re replacing
self.bind("|", "split-window -h")
self.bind("-", "split-window -v")

# Resize to the smallest client actively viewing a window
#setw -g aggressive-resize on
self.aggressive_resize(True)

# Don't wait so long for commands
#set -s escape-time 0
