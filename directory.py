import os
from datetime import datetime

dirname = datetime.strftime(datetime.now(), '%Y-%m-%d')
print dirname

try:    
    os.makedirs(dirname)
except OSError:
  if os.path.exists(dirname):
      print "directory exist"        
      pass    
  else:        
      # There was an error on creation, so make sure we know about it        
      raise
