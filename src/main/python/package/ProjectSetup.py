from pathlib import Path
import os

from PySide2 import QtWidgets, QtCore

from package.ReportWindow import ReportWindow

class ProjectSetup(QtWidgets.QMainWindow):
    def __init__(self,current_project):
        super().__init__()
### WINDOW SETUP
        self.current_project = current_project
        self.main_layout =  QtWidgets.QVBoxLayout()
        self.setWindowTitle("Project Setup")
### ETAPE 1: row 0 et 1
        self.e1_r0_lab_instruction = QtWidgets.QLabel("1_ Importez un ou plusieurs fichier Silverstack (.csv)")

        self.e1_r1_btn_csv_import = QtWidgets.QPushButton("Importer")
        self.e1_r1_btn_csv_import.setMaximumWidth(150)
        self.e1_r1_btn_csv_import.clicked.connect(self.import_csv)

        self.e1_r1_lw_imported_csv = QtWidgets.QListWidget()
        self.e1_r1_lw_imported_csv.setMaximumWidth(120)

        self.e1_r1_btn_remove_csv = QtWidgets.QPushButton("Retirer")
        self.e1_r1_btn_remove_csv.setMaximumWidth(150)
        self.e1_r1_btn_remove_csv.clicked.connect(self.remove_csv)

        self.r1_layout = QtWidgets.QHBoxLayout()
        self.r1_layout.addWidget(self.e1_r1_btn_csv_import)
        self.r1_layout.addWidget(self.e1_r1_lw_imported_csv)
        self.r1_layout.addWidget(self.e1_r1_btn_remove_csv)

        self.main_layout.addWidget(self.e1_r0_lab_instruction)
        self.main_layout.addLayout(self.r1_layout,stretch=20)

        self.main_layout.addWidget(QtWidgets.QLabel("                                                       _____________________________________________________________"))

### ETAPE 2: row 2 et 3
        self.e2_r2_lab_instruction = QtWidgets.QLabel("2_ Créer une ou plusieurs journées de tournage")

        self.e2_r3_cal_date_creation_calendar = QtWidgets.QDateEdit()
        self.e2_r3_cal_date_creation_calendar.setCalendarPopup(True)
        self.e2_r3_btn_create_day = QtWidgets.QPushButton('Nouveau jour')
        self.e2_r3_btn_create_day.setMaximumWidth(150)

        self.e2_r3_day_number_selector = QtWidgets.QSpinBox()
        self.e2_r3_day_number_selector.setMaximumWidth(55)
        self.e2_r3_day_number_selector.setMinimum(0)
        self.e2_r3_day_number_selector.setMaximum(999)


        self.e2_r3_btn_create_day.clicked.connect(self.add_shooting_day)

        self.e2_r3_lw_days_created = QtWidgets.QListWidget()
        self.e2_r3_lw_days_created.setMaximumWidth(120)
        self.e2_r3_btn_remove_day = QtWidgets.QPushButton("Retirer")
        self.e2_r3_btn_remove_day.setMaximumWidth(150)

        self.r3_layout = QtWidgets.QHBoxLayout()

        self.r3_layout.addWidget(self.e2_r3_cal_date_creation_calendar)
        self.r3_layout.addWidget(self.e2_r3_day_number_selector )
        self.r3_layout.addWidget(self.e2_r3_btn_create_day)
        self.r3_layout.addWidget(self.e2_r3_lw_days_created)
        self.r3_layout.addWidget(self.e2_r3_btn_remove_day)

        self.main_layout.addWidget(self.e2_r2_lab_instruction)
        self.main_layout.addLayout(self.r3_layout, stretch=0)
        self.main_layout.addWidget(QtWidgets.QLabel("                                                       _____________________________________________________________"))
### ETAPE 3 rows 5, 6 et 7
        self.e3_r5_lab_instruction = QtWidgets.QLabel("3_ Repartir les cartes detectées entre les jours de tournage")

        self.e3_r6_lw_day_selection = QtWidgets.QListWidget()
        self.e3_r6_lw_day_selection.setMaximumSize(120,60)

        self.e3_r6_lw_cards_from_day = QtWidgets.QListWidget()
        self.e3_r6_lw_cards_from_day.setMaximumSize(120,300)

        self.e3_r6_btn_add =QtWidgets.QPushButton("-->")
        self.e3_r6_btn_add.setMaximumWidth(150)
        self.e3_r6_btn_remove =QtWidgets.QPushButton("<--")
        self.e3_r6_btn_remove.setMaximumWidth(150)

        self.e3_r6_lw_available_cards = QtWidgets.QListWidget()
        self.e3_r6_lw_available_cards.setMaximumSize(120,300)

        self.e3_layout = QtWidgets.QGridLayout()
        self.e3_layout.addWidget(self.e3_r6_lw_cards_from_day,1,0,2,1)
        self.e3_layout.addWidget(self.e3_r6_btn_add,1,1,1,1)
        self.e3_layout.addWidget(self.e3_r6_btn_remove,2,1,1,1)
        self.e3_layout.addWidget(self.e3_r6_lw_day_selection,0,2,1,1)
        self.e3_layout.addWidget(self.e3_r6_lw_available_cards,1,2,2,1)

        self.main_layout.addWidget(self.e3_r5_lab_instruction)
        self.main_layout.addLayout(self.e3_layout)
        self.main_layout.addWidget(QtWidgets.QLabel(
            "                                                       _____________________________________________________________"))


# Edit button
        self.edit_btn =  QtWidgets.QPushButton("Editer le rapport")
        self.edit_btn.clicked.connect(self.edit_report)

        self.main_layout.addWidget(self.edit_btn)








### Window setup
        self.widget = QtWidgets.QWidget()
        self.widget.setLayout(self.main_layout)
        self.setCentralWidget(self.widget)
        self.resize(800, 600)

### FUNCTIONS
    def add_shooting_day(self):
       # On récupère la date du calendrier
       day = self.e2_r3_cal_date_creation_calendar.date().day()
       month = self.e2_r3_cal_date_creation_calendar.date().month()
       year = self.e2_r3_cal_date_creation_calendar.date().year()
      # On récupère le numéro du jour de tournage
       number = self.e2_r3_day_number_selector.value()



       if self.current_project.create_shooting_day(number= number,day= day,month= month,year=year):
            self.refresh_day_list()

    def refresh_day_list(self):
        self.e2_r3_lw_days_created.clear()
        for item in self.current_project.shooting_days:
            self.e2_r3_lw_days_created.addItem(f"{item['number']}:{item['day']}/{item['month']}/{item['year']}")



    def edit_report(self):
        if not self.current_project.shooting_days:
            return
       #DEBUG
        day = self.current_project.shooting_days[0]

        for card in self.current_project.all_card_list:
            day.get("cards").append(card)
       #DEBUG

        self.w = ReportWindow(current_project=self.current_project)
        self.w.show()
        self.close()


    def open_csv_path_window(self):
        f = QtWidgets.QFileDialog.getOpenFileUrl(self,"importer fichier","/Users/user/Desktop/","CSV files (*.csv)")
        return f[0].toLocalFile()

    def import_csv(self):
        path = self.open_csv_path_window()
        self.current_project.csv_importer(path)
        self.e1_r1_lw_imported_csv.addItem(os.path.basename(path))
        self.e1_r1_lw_imported_csv.setCurrentRow(0)
#DEBUG
       # self.current_project.affichage_clips()
#DEBUG
    def remove_csv(self):
        selected_item = self.e1_r1_lw_imported_csv.selectedItems()
        if not selected_item:
            return
        csv_to_remove = selected_item[0].text()
        i = len(self.current_project.clip_list) - 1
        while i >= 0:
            if self.current_project.clip_list[i].csv == csv_to_remove:
                del self.current_project.clip_list[i]
            i -= 1
        self.e1_r1_lw_imported_csv.takeItem(self.e1_r1_lw_imported_csv.row(selected_item[0]))

