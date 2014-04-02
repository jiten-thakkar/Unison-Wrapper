import subprocess as sub
import socket, getopt, sys, time, os

def is_connected(hostname, port):
  try:
    host = socket.gethostbyname(hostname)
    s = socket.create_connection((host, port))
    return True
  except:
    pass
  return False

def sync(path, hostname, port):
  try:
    while True:
      if is_connected(hostname, port):
         sub.call(["/usr/bin/unison", "-ui", "text", "-batch", path, "socket://"+hostname+":"+port])
      time.sleep(1)
  except KeyboardInterrupt:
    sys.exit(0)

def parseOptions(argv):
  path = ''
  hostname = ''
  port = ''
  try:
     opts,args = getopt.getopt(argv, "h:d:p:", ["dir=", "host=", "port="])
  except getopt.GetoptError:
     print 'client_sync.py -d <dir> -h <host> -p <port>'
     sys.exit(1)
  for opt,arg in opts:
    if opt in ('-h', '--host'):
       hostname = arg   
    elif opt in ('-d', '--dir'):
       path = arg
    elif opt in ('-p', '--port'):
       port = arg
    else:
       print 'client_sync.py -d <dir> -h <host> -p <port>'

  if path == '' or hostname == '' or port == '':
    print 'client_sync.py -d <dir> -h <host> -p <port>'
    sys.exit(1)
  return path, hostname, port


if __name__ == "__main__":
  path, hostname, port = parseOptions(sys.argv[1:])
  if os.path.exists(path) == False:
    print "Invalid directory path"
    sys.exit(2)
  sync(path, hostname, port)
