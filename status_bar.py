import sys

class TmuxConfig:
  def __init__(self):
    self.config_file = open('config.py')

  def compile(self):
    exec(self.config_file.read())

  def terminal(self, term):
    print "set -g default-terminal \"%s\"" % term

  def prefix(self, key="C-b"):
    print "set -g prefix %s" % key

if __name__ == "__main__":
  config = TmuxConfig()
  config.compile()
