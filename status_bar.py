import sys

class TmuxConfig:
  def __init__(self):
    self.config_file = open('config.py')

  def compile(self):
    exec(self.config_file.read())

  def terminal(self, term):
    self.__set("default-terminal \"%s\"" % term)

  def prefix(self, key="C-b"):
    self.__set("prefix %s" % key)

  def status_keys(self, mode="vi"):
    self.__set("status-keys %s" % mode)

  def mode_keys(self, mode="vi"):
    self.__set_window("mode-keys %s" % mode)

  def bind(self, key, command):
    print "bind %s %s" % (key, command)

  def unbind(self, key):
    print "unbind %s" % key

  def __set(self, command):
    print "set -g %s" % command

  def __set_window(self, command):
    print "setw -g %s" % command

if __name__ == "__main__":
  config = TmuxConfig()
  config.compile()
