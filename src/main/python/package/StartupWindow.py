from pathlib import Path


from PySide2 import QtWidgets, QtCore


from package.ReportWindow import ReportWindow
from package.ProjectSetup import ProjectSetup


class StartUpWindow(QtWidgets.QWidget):
    def __init__(self,current_project):
        super().__init__()
        self.current_project = current_project
        self.main_layout = QtWidgets.QHBoxLayout()
       # WID CREATION
        self.btn_new_report = QtWidgets.QPushButton("Créer un nouveau rapport")
        self.btn_open_report = QtWidgets.QPushButton("Ouvrir un rapport existant")
        self.lab_choice = QtWidgets.QLabel("OU")
       # WID ADDING
        self.main_layout.addWidget(self.btn_open_report)
        self.main_layout.addWidget(self.lab_choice)
      #WIDGET CONNEXIONS
        self.btn_open_report.clicked.connect(self.open_report)
        self.btn_new_report.clicked.connect(self.test_func)

        self.main_layout.addWidget(self.btn_new_report)
        self.main_layout.setSpacing(20)
        self.setLayout(self.main_layout)
        self.setFixedSize(600,200)


    def open_report(self):
        self.current_project.load_report(self.open_json_path_window())
        self.main_window = ReportWindow(current_project=self.current_project)
        self.main_window.show()
        self.close()

    def open_json_path_window(self):
        f = QtWidgets.QFileDialog.getOpenFileUrl(self,"importer fichier",f"{Path.home()}/Desktop","Json files (*.json)")
        return f[0].toLocalFile()

    def test_func(self):
        self.a = ProjectSetup(current_project= self.current_project)
        self.a.show()
        self.close()

