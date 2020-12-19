
from PySide2 import QtWidgets, QtCore


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


