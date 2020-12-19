from pathlib import Path
import os

from PySide2 import QtWidgets, QtCore


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




class ClipReview(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("clipreview")
        self.shot_name = ""



       # Widget creation
        self.lab_circled_show = QtWidgets.QLabel("(X)")
        self.lab_circled_show.setStyleSheet("font-size: 24px; color:gold; font-style: bold")
        self.lab_circled_show.setMaximumWidth(30)
        self.lab_circled_show.setVisible(False)

        self.lab_alert = QtWidgets.QLabel(" ! ")
        self.lab_alert.setStyleSheet("font-size: 24px; color:Red; font-style: bold")
        self.lab_alert.setMaximumWidth(30)
        self.lab_alert.setVisible(False)


        self.lab_shot_name = QtWidgets.QLabel("A234422")
        self.lab_shot_name.setStyleSheet("font-size: 24px; color:cornflowerblue; font-style: bold")
        self.lab_shot_name.setMaximumWidth(120)
        self.lab_shot_name.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)



        self.lab_comment = QtWidgets.QLabel("Commentaire")
        self.lab_comment.setObjectName("scene_label")
        self.le_comment = QtWidgets.QPlainTextEdit()
        self.le_comment.setFixedSize(180,90)


        self.lab_sequence = QtWidgets.QLabel("Sequence")
        self.lab_sequence.setObjectName("scene_label")
        self.lab_sequence.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.le_sequence = QtWidgets.QLineEdit("X")

        self.le_sequence.setAlignment(QtCore.Qt.AlignCenter)
        self.le_sequence.setFixedSize(60,60)


        self.lab_shot = QtWidgets.QLabel("Plan")
        self.lab_shot.setObjectName("scene_label")
        self.le_shot = QtWidgets.QLineEdit("1")
        self.le_shot.setFixedSize(60,60)
        self.le_shot.setObjectName("scene_edit")
        self.le_shot.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)


        self.lab_take = QtWidgets.QLabel("Prise")
        self.lab_take.setObjectName("scene_label")
        self.le_take = QtWidgets.QLineEdit("1")
        self.le_take.setFixedSize(60,60)
        self.le_take.setObjectName("scene_edit")
        self.le_take.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)


        self.circled = QtWidgets.QCheckBox()
        self.circled.setObjectName("circled")
        self.circled.setText("[X] cerclée?")


        self.lab_metadata = QtWidgets.QLabel("AAAAAAA")
        self.lab_metadata.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lab_metadata.setStyleSheet("font-size: 12px; color:slategray;")

        self.line_widget = QtWidgets.QLabel("                                                   ___________________________________________________")
        self.line_widget.setObjectName("line")





    # Layout creation
        self.clip_layout = QtWidgets.QGridLayout(self)
        self.clip_layout.setSpacing(0)

    # Adding widget to layout
        self.clip_layout.addWidget(self.lab_circled_show,0,0)
        self.clip_layout.addWidget(self.lab_alert,1,0)
        self.clip_layout.addWidget(self.lab_shot_name,0,1)
        self.clip_layout.addWidget(self.lab_metadata,1,1,)
        self.clip_layout.addWidget(self.lab_sequence,0,2)
        self.clip_layout.addWidget(self.lab_shot, 0, 3)
        self.clip_layout.addWidget(self.lab_take, 0, 4)
        self.clip_layout.addWidget(self.le_sequence,1,2)
        self.clip_layout.addWidget(self.le_shot,1,3)
        self.clip_layout.addWidget(self.le_take,1,4)
        self.clip_layout.addWidget(self.le_comment,1,5)
        self.clip_layout.addWidget(self.lab_comment,0,5)
        self.clip_layout.addWidget(self.circled,2,4,1,1)
        self.clip_layout.addWidget(self.line_widget,4,1,1,5)




    def set_comment(self):
        self.clip.comment = self.le_comment.toPlainText()
        self.lab_alert.setVisible(False)

    def set_sequence(self):
        self.clip.sequence = self.le_sequence.text()

    def set_shot(self):
        self.clip.shot = self.le_shot.text()

    def set_take(self):
        self.clip.take = self.le_take.text()

    def set_circle(self):
        self.clip.circled = not self.clip.circled

    def circled_actions(self):
        if self.circled.isChecked():
            self.le_take.setStyleSheet("background-color: Moccasin; color: black;")
           # self.lab_shot_name.setStyleSheet("font-size: 24px; color:gold; font-style: bold; border 10px")
            self.lab_circled_show.setVisible(True)
            self.clip.circle_change()
        else:
            self.le_take.setStyleSheet("")
            #self.lab_shot_name.setStyleSheet("font-size: 24px; color:cornflowerblue; font-style: bold")
            self.lab_circled_show.setVisible(False)
            self.clip.circle_change()







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
        self.e2_r3_btn_create_day = QtWidgets.QPushButton('Nouveau jour')
        self.e2_r3_btn_create_day.setMaximumWidth(150)
        ## DEBUG
        self.e2_r3_btn_create_day.clicked.connect(self.add_shooting_day)
        ## DEBUG
        self.e2_r3_lw_days_created = QtWidgets.QListWidget()
        self.e2_r3_lw_days_created.setMaximumWidth(120)
        self.e2_r3_btn_remove_day = QtWidgets.QPushButton("Retirer")
        self.e2_r3_btn_remove_day.setMaximumWidth(150)

        self.r3_layout = QtWidgets.QHBoxLayout()

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
       if self.current_project.create_shooting_day(number=1,shooting_day= 1,month=12,year=2020):
            self.refresh_day_list()

    def refresh_day_list(self):
        for item in self.current_project.shooting_days:
            self.e2_r3_lw_days_created.addItem(f"{item['number']}:{item['day']}/{item['month']}/{item['year']}")



    def edit_report(self):
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
        self.current_project.affichage_clips()
#DEBUG
    def remove_csv(self):
        selected_item = self.e1_r1_lw_imported_csv.selectedItems()
        to_remove_index = []
        i = 0
        print(f"longueur liste:{len(self.current_project.clip_list)}")
        while i < len(self.current_project.clip_list):
            if self.current_project.clip_list[i].csv == selected_item[0].text():
                to_remove_index.append(i)

            i += 1
        print(to_remove_index)
        for index in to_remove_index:
            del self.current_project.clip_list[index]



            # DEBUG
        print("effacement")
        self.current_project.affichage_clips()








class ReportWindow(QtWidgets.QMainWindow):
    def __init__(self,current_project):
        super().__init__()
        self.current_project = current_project
        self.selected_card = ""
        self.current_day_edited = 0

        # menu
        menu = self.menuBar()
        menu.setNativeMenuBar(False)
        file_menu = menu.addMenu("Rapport")

        load_action = QtWidgets.QAction("ouvrir un rapport",self)
        load_action.triggered.connect(self.open_report)

        save_action = QtWidgets.QAction("Sauvegarder le rapport", self)
        save_action.triggered.connect(self.save_report)

        file_menu.addAction(load_action)
        file_menu.addAction(save_action)





        #Window setup
        self.setWindowTitle("La Ruche QCReport")
# LAYOUT  ################## LAYOUT
        #Layouts creation and setup
        self.main_layout = QtWidgets.QGridLayout()
        self.side_layout = QtWidgets.QVBoxLayout()
        self.day_header_layout = QtWidgets.QGridLayout()

        self.day_header_layout.setSpacing(0)


###HEADER############################################
        #DAY HEADER WIDEGTS CREATION and assignment
        self.lab_shooting_day_number_title = QtWidgets.QLabel('Jour')
        self.lab_shooting_day_number = QtWidgets.QLabel(f"{self.current_day_edited} : {self.current_project.get_shooting_date_string_from_number(self.current_day_edited)}")
        self.lab_shooting_day_number.setStyleSheet("font-size: 40px; color:DarkSlateGray; font-style: bold")

        self.lab_clip_number = QtWidgets.QLabel()
        self.lab_clip_number.setStyleSheet("font-size: 20px;")

        self.te_day_comment = QtWidgets.QPlainTextEdit()
        self.te_day_comment.setPlaceholderText("Commentaire de la journée.")
        self.te_day_comment.setMaximumWidth(300)
        self.te_day_comment.setMaximumHeight(80)
        self.te_day_comment.cursorPositionChanged.connect(self.set_day_comment)
#### A REPARER





        self.lw_framerate_list = QtWidgets.QListWidget()
        self.lw_framerate_list.setMaximumSize(100,80)
        self.lw_codec_list = QtWidgets.QListWidget()
        self.lw_codec_list.setMaximumSize(150,80)
        self.lw_cards_list = QtWidgets.QListWidget()
        self.lw_cards_list.setMaximumSize(100,80)

        self.lab_codec = QtWidgets.QLabel("Codec detectés")
        self.lab_codec.setStyleSheet("font-size: 10px;")
        self.lab_framerates = QtWidgets.QLabel("Cadences detectées")
        self.lab_framerates.setStyleSheet("font-size: 10px;")
        self.lab_cards = QtWidgets.QLabel("Cartes")
        self.lab_cards.setStyleSheet("font-size: 10px;")




        self.day_header_layout.addWidget(self.lab_shooting_day_number,0,0,1,1)
        self.day_header_layout.addWidget(self.lab_clip_number,1,0,1,1)
        self.day_header_layout.addWidget(self.te_day_comment,2,0,1,1)

        self.day_header_layout.addWidget(self.lab_framerates,1,2,1,1)
        self.day_header_layout.addWidget(self.lw_framerate_list,2,2,1,1)
        self.day_header_layout.addWidget(self.lab_codec, 1, 3, 1, 1)
        self.day_header_layout.addWidget(self.lw_codec_list,2,3,1,1)
        self.day_header_layout.addWidget(self.lab_cards, 1, 4, 1, 1)
        self.day_header_layout.addWidget(self.lw_cards_list,2,4,1,1)


# HEADER END

### CLIP LIST
        # set scrollable area



        self.lab_scroll = QtWidgets.QLabel("")

        self.clips_layout = QtWidgets.QVBoxLayout(self)
        self.scrollable_area = QtWidgets.QScrollArea(self)
        self.placeholder_widget = QtWidgets.QWidget(self)
        self.placeholder_widget.setLayout(self.clips_layout)
        self.scrollable_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollable_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollable_area.setWidgetResizable(True)
        self.scrollable_area.setWidget(self.placeholder_widget)
        self.scrollable_area.setFrameStyle(QtWidgets.QFrame.StyledPanel | QtWidgets.QFrame.Sunken)



         # Assigning widgets
        #self.side_layout.addWidget(self.lab_side)
        self.clips_layout.addWidget(self.lab_scroll)


        # Side widgets
        #labels
        self.side_lab_title = QtWidgets.QLabel("Titre du film:")
        self.side_lab_director = QtWidgets.QLabel("Mise en scène:")
        self.side_lab_production = QtWidgets.QLabel("Production:")
        self.side_lab_cinematographer = QtWidgets.QLabel("Chef opérateur:")
        self.side_lab_verification_date = QtWidgets.QLabel("Date de vérification:")
        #Line edits
        self.side_le_title = QtWidgets.QLineEdit(self.current_project.film_title)
        self.side_le_director = QtWidgets.QLineEdit(self.current_project.director)
        self.side_le_production = QtWidgets.QLineEdit(self.current_project.production)
        self.side_le_cinematographer = QtWidgets.QLineEdit(self.current_project.cinematographer)
        self.side_le_verification_date = QtWidgets.QDateEdit(QtCore.QDate(self.current_project.qc_date.get("year"),self.current_project.qc_date.get("month"),self.current_project.qc_date.get("day")))
        self.side_le_verification_date.setCalendarPopup(True)

        # Side connectipns
        self.side_le_title.textChanged.connect(self.set_title)
        self.side_le_director.textChanged.connect(self.set_director)
        self.side_le_production.textChanged.connect(self.set_production)
        self.side_le_cinematographer.textChanged.connect(self.set_cinematographer)
        self.side_le_verification_date.userDateChanged.connect(self.set_verification_date)

        # Adding widgets
        self.side_layout.addWidget(self.side_lab_title)
        self.side_layout.addWidget(self.side_le_title)

        self.side_layout.addWidget(self.side_lab_director)
        self.side_layout.addWidget(self.side_le_director)

        self.side_layout.addWidget(self.side_lab_production)
        self.side_layout.addWidget(self.side_le_production)

        self.side_layout.addWidget(self.side_lab_cinematographer)
        self.side_layout.addWidget(self.side_le_cinematographer)

        self.side_layout.addWidget(self.side_lab_verification_date)
        self.side_layout.addWidget(self.side_le_verification_date)


        self.side_layout.addWidget(QtWidgets.QLabel("Jours de tournage"))
        self.day_list = QtWidgets.QListWidget()
        self.day_list.itemSelectionChanged.connect(self.change_day)
        self.side_layout.addWidget(self.day_list)
        self.populate_day_list()


       # self.side_layout.addWidget(QtWidgets.QPushButton("Manage Report"))
       # self.side_layout.addWidget(QtWidgets.QPushButton("Save Report"))
       # self.side_layout.addWidget(QtWidgets.QPushButton("Export Report"))
       ###DEBUG
        self.debug = QtWidgets.QPushButton("Debug")
        self.side_layout.addWidget(self.debug)
        self.debug.clicked.connect(self.set_day_comment)


        # LAYOUTS HIERARCHY

        self.main_layout.addLayout(self.side_layout,0,0,8,2)
        self.main_layout.addLayout(self.day_header_layout,0,2,2,8)
        self.main_layout.addWidget(self.scrollable_area,2,2,6,8)


        self.widget = QtWidgets.QWidget()
        self.widget.setLayout(self.main_layout)
        self.setCentralWidget(self.widget)
        self.resize(1200,800)
        #self.setStyleSheet("background-color: rgb(50,50,50);")


        ######## END OF INIT  ##########


#####





##### Utilities functions

    def codec_list_from_day(self,day_number):
        codec_list = []
        day = self.current_project.get_shooting_day(day_number)
        for clip in self.current_project.clip_list:
            if clip.card in day.get("cards"):
                if clip.codec not in codec_list:
                    codec_list.append(clip.codec)
        return codec_list

    def framerate_list_from_day(self,day_number):
        framerate_list = []
        day = self.current_project.get_shooting_day(day_number)
        for clip in self.current_project.clip_list:
            if clip.card in day.get("cards"):
                if clip.cadence not in framerate_list:
                    framerate_list.append(clip.cadence)
        return framerate_list

    def clip_number_from_day(self,day_number):
        clip_number = 0
        card_list = self.card_list_from_day(day_number = day_number)
        for clip in self.current_project.clip_list:
            if clip.card in card_list:
                clip_number += 1
        return clip_number


    def card_list_from_day(self,day_number):

        day = self.current_project.get_shooting_day(day_number)
        return day.get("cards")

########### DAY HEADER FUNCTIONS
    def refresh_day_header(self):
        self.lab_shooting_day_number.setText(f"J{self.current_day_edited} : {self.current_project.get_shooting_date_string_from_number(self.current_day_edited)}")
        self.lab_clip_number.setText(f"Nombre de clips: {self.clip_number_from_day(self.current_day_edited)}")
        self.refresh_comment_te()
        self.refresh_card_lw()
        self.refresh_codec_lw()
        self.refresh_framerate_lw()


    def set_day_comment(self):
        self.current_project.set_shooting_day_comment(self.current_day_edited,self.te_day_comment.toPlainText())

    def does_nothing(self):
        pass

    def refresh_comment_te(self):
        self.te_day_comment.clear()
        day = self.current_project.get_shooting_day(self.current_day_edited)
        self.te_day_comment.setPlaceholderText(day.get("comment"))


    def refresh_card_lw(self):
        self.lw_cards_list.clear()
        card_list = self.card_list_from_day(self.current_day_edited)
        for card in card_list:
            self.lw_cards_list.addItem(card)

    def refresh_codec_lw(self):
        self.lw_codec_list.clear()
        codec_list = self.codec_list_from_day(self.current_day_edited)
        print(codec_list)
        for codec in codec_list:
            self.lw_codec_list.addItem(codec)

    def refresh_framerate_lw(self):
        self.lw_framerate_list.clear()
        framerate_list = self.framerate_list_from_day(self.current_day_edited)
        for framerate in framerate_list:
            self.lw_framerate_list.addItem(framerate)


######### Clip list functions
    def clear_clip_list(self):
        for i in reversed(range(self.clips_layout.count())):
            self.clips_layout.itemAt(i).widget().setParent(None)


    def populate_clip_list(self):
        day = self.current_project.get_shooting_day(self.current_day_edited)
        print(day.get("cards"))
        for clip in self.current_project.clip_list:
            if clip.card in day.get("cards"):
                wid_clip = ClipReview()
                wid_clip.clip = clip
                wid_clip.clip_name = clip.name
                wid_clip.lab_shot_name.setText(clip.name)
                if clip.comment != "Pas encore vérifié":
                    wid_clip.le_comment.setPlainText(clip.comment)
                else:
                    wid_clip.le_comment.setPlaceholderText(clip.comment)

                wid_clip.le_sequence.setText(str(clip.sequence))
                wid_clip.le_shot.setText(str(clip.shot))
                wid_clip.le_take.setText(str(clip.take))

                wid_clip.le_sequence.textChanged.connect(wid_clip.set_sequence)
                wid_clip.le_shot.textChanged.connect(wid_clip.set_shot)
                wid_clip.le_take.textChanged.connect(wid_clip.set_take)
                wid_clip.le_comment.textChanged.connect(wid_clip.set_comment)
                wid_clip.circled.stateChanged.connect(wid_clip.circled_actions)
                if wid_clip.clip.circled == True:
                    wid_clip.circled.setChecked(True)
                    wid_clip.circled_actions()
                wid_clip.lab_metadata.setText(f"Codec:{clip.codec}\nFramerate:{clip.cadence} im/s\nDuration:{clip.duration[:6]} s\nResolution:{clip.resolution} px\nWhite Balance:{clip.wb} K")
                self.clips_layout.addWidget(wid_clip)

################   SIDE HEADER refresh functions            #################


    def populate_side_header(self):
        self.side_le_title.setText(self.current_project.film_title)
        self.side_le_director.setText(self.current_project.director)
        self.side_le_production.setText(self.current_project.production)
        self.side_le_cinematographer.setText(self.current_project.cinematographer)
        self.side_le_verification_date.setDate(QtCore.QDate(self.current_project.qc_date.get("year"),self.current_project.qc_date.get("month"),self.current_project.qc_date.get("day")))


    def populate_day_list(self):
        for day in self.current_project.shooting_days:
            item = QtWidgets.QListWidgetItem()
            item.day = day
            nb = day.get("number")
            d = day.get("day")
            m = day.get("month")
            y = day.get("year")
            item.setText(f"{nb}-{d}/{m}/{y}")
            self.day_list.addItem(item)
        self.day_list.setCurrentRow(0)


    def set_title(self):
        self.current_project.film_title = self.side_le_title.text()

    def set_director(self):
        self.current_project.director = self.side_le_director.text()

    def set_production(self):
        self.current_project.production = self.side_le_production.text()

    def set_cinematographer(self):
        self.current_project.cinematographer = self.side_le_cinematographer.text()


    def set_verification_date(self):
        self.current_project.qc_date = {"day":self.side_le_verification_date.date().day(),"month":self.side_le_verification_date.date().month(),"year":self.side_le_verification_date.date().year()}

    def change_day(self):
        self.current_day_edited = self.day_list.selectedItems()[0].day.get("number")
        self.clear_clip_list()
        self.populate_clip_list()
        self.refresh_day_header()




############ File operation functions ##########################

    def open_json_path_window(self):
        f = QtWidgets.QFileDialog.getOpenFileUrl(self,"importer fichier",f"{Path.home()}/Desktop","Json files (*.json)")
        return f[0].toLocalFile()

    def save_json_path_window(self):
        f = QtWidgets.QFileDialog.getSaveFileUrl(self,f"{Path.home()}/Desktop")
        return f[0].toLocalFile()

    def open_csv_path_window(self):
        f = QtWidgets.QFileDialog.getOpenFileUrl(self,"importer fichier","/Users/user/Desktop/","CSV files (*.csv)")
        return f[0].toLocalFile()

    def open_report(self):
        self.current_project.load_report(self.open_json_path_window())
        self.clear_clip_list()
        self.populate_day_list()
        self.populate_side_header()


    def save_report(self):
        f = self.save_json_path_window()
        self.current_project.save_report(f)




