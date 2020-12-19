import sys

from PySide2.QtWidgets import QMainWindow
from fbs_runtime.application_context.PySide2 import ApplicationContext

from  package.api2 import Clip, Rapport
from package.StartupWindow import StartUpWindow


#import qtmodern.styles
#import qtmodern.windows

if __name__ == '__main__':
    current_project = Rapport()
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    first_window = StartUpWindow(current_project = current_project)
   # qtmodern.styles.dark(appctxt.app)
    first_window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)



