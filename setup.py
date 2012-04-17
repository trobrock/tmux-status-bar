import inspect, os

current_dir      = os.path.realpath(os.path.dirname(inspect.getfile(inspect.currentframe())))
real_tmux_config = "%s/tmux.conf" % current_dir
new_tmux_config  = os.path.expanduser("~/.tmux.conf")

print "Symlinking %s to %s" % (real_tmux_config, new_tmux_config)
os.symlink(real_tmux_config, new_tmux_config)

print "Done"
