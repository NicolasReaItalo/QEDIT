from pathlib import Path

from PySide2 import QtWidgets, QtCore

from package.ClipReview import ClipReview


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
        self.debug.clicked.connect(self.current_project.export_report)


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


