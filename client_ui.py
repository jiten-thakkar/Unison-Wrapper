from ui_tree import Ui_Tree
from PyQt4 import QtCore,QtGui
from subprocess import Popen
import sys, getopt, os

def ui(path):
  if os.path.exists(path) == False:
    print "Invalid directory path"
    sys.exit(2)
  app = QtGui.QApplication(sys.argv)
  dirModel = QtGui.QFileSystemModel()
  dirModel.setRootPath(path)
  dirModel.setReadOnly(True)    #Set Directory access to read only
  index = dirModel.index(path)

  Tree = QtGui.QWidget()
  ui = Ui_Tree()
  ui.setupUi(Tree)
  ui.treeView.setModel(dirModel)
  ui.treeView.setRootIndex(index)
  ui.treeView.resizeColumnToContents(0)
  ui.treeView.sortByColumn(0, QtCore.Qt.AscendingOrder)
  Tree.show()
  sys.exit(app.exec_())

def parseOptions(argv):
  path = ''
  try:
     opts,args = getopt.getopt(argv, "hd:", ["dir=", "help="])
  except getopt.GetoptError:
     print 'client_ui.py -d <dir>'
     sys.exit(1)
  for opt,arg in opts:
    if opt in ('-h', '--help'):
       print 'client_ui.py -d <dir>'
       sys.exit(1)
    elif opt in ('-d', '--dir'):
       path = arg
  if path == '':
    print 'client_ui.py -d <dir>'
    sys.exit(1)
  return path

if __name__ == "__main__":
   path = parseOptions(sys.argv[1:])
   ui(path)
