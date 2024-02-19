# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(451, 535)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(451, 535))
        MainWindow.setMaximumSize(QtCore.QSize(451, 535))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ButtonIcons/wave-square.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 10, 431, 472))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.sineWaveImg = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.sineWaveImg.setMaximumSize(QtCore.QSize(100, 100))
        self.sineWaveImg.setText("")
        self.sineWaveImg.setPixmap(QtGui.QPixmap(":/ButtonIcons/wave-sine.png"))
        self.sineWaveImg.setScaledContents(True)
        self.sineWaveImg.setAlignment(QtCore.Qt.AlignCenter)
        self.sineWaveImg.setObjectName("sineWaveImg")
        self.verticalLayout_5.addWidget(self.sineWaveImg)
        self.sinePushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.sinePushButton.setEnabled(True)
        self.sinePushButton.setMaximumSize(QtCore.QSize(100, 24))
        self.sinePushButton.setObjectName("sinePushButton")
        self.verticalLayout_5.addWidget(self.sinePushButton)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.squareWaveImg = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.squareWaveImg.setMaximumSize(QtCore.QSize(100, 100))
        self.squareWaveImg.setText("")
        self.squareWaveImg.setPixmap(QtGui.QPixmap(":/ButtonIcons/wave-square.png"))
        self.squareWaveImg.setScaledContents(True)
        self.squareWaveImg.setAlignment(QtCore.Qt.AlignCenter)
        self.squareWaveImg.setObjectName("squareWaveImg")
        self.verticalLayout_7.addWidget(self.squareWaveImg)
        self.squarePushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.squarePushButton.setEnabled(True)
        self.squarePushButton.setMaximumSize(QtCore.QSize(100, 24))
        self.squarePushButton.setObjectName("squarePushButton")
        self.verticalLayout_7.addWidget(self.squarePushButton)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.triangleWaveImg = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.triangleWaveImg.setMaximumSize(QtCore.QSize(100, 100))
        self.triangleWaveImg.setText("")
        self.triangleWaveImg.setPixmap(QtGui.QPixmap(":/ButtonIcons/wave-triangular.png"))
        self.triangleWaveImg.setScaledContents(True)
        self.triangleWaveImg.setAlignment(QtCore.Qt.AlignCenter)
        self.triangleWaveImg.setObjectName("triangleWaveImg")
        self.verticalLayout_9.addWidget(self.triangleWaveImg)
        self.trianglePushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.trianglePushButton.setEnabled(True)
        self.trianglePushButton.setMaximumSize(QtCore.QSize(100, 24))
        self.trianglePushButton.setObjectName("trianglePushButton")
        self.verticalLayout_9.addWidget(self.trianglePushButton)
        self.horizontalLayout.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.sawtoothWaveImg = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.sawtoothWaveImg.setMaximumSize(QtCore.QSize(100, 100))
        self.sawtoothWaveImg.setText("")
        self.sawtoothWaveImg.setPixmap(QtGui.QPixmap(":/ButtonIcons/wave-sawtooth.png"))
        self.sawtoothWaveImg.setScaledContents(True)
        self.sawtoothWaveImg.setAlignment(QtCore.Qt.AlignCenter)
        self.sawtoothWaveImg.setObjectName("sawtoothWaveImg")
        self.verticalLayout_10.addWidget(self.sawtoothWaveImg)
        self.sawtoothPushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.sawtoothPushButton.setEnabled(True)
        self.sawtoothPushButton.setMaximumSize(QtCore.QSize(100, 24))
        self.sawtoothPushButton.setObjectName("sawtoothPushButton")
        self.verticalLayout_10.addWidget(self.sawtoothPushButton)
        self.horizontalLayout.addLayout(self.verticalLayout_10)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_3.setMinimumSize(QtCore.QSize(128, 16))
        self.label_3.setMaximumSize(QtCore.QSize(128, 16))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.selectedWaveformLabel = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.selectedWaveformLabel.setMinimumSize(QtCore.QSize(128, 16))
        self.selectedWaveformLabel.setMaximumSize(QtCore.QSize(128, 16))
        self.selectedWaveformLabel.setStyleSheet("color:rgb(0, 170, 127)\n"
"")
        self.selectedWaveformLabel.setObjectName("selectedWaveformLabel")
        self.horizontalLayout_3.addWidget(self.selectedWaveformLabel)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.line_3 = QtWidgets.QFrame(self.verticalLayoutWidget_4)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_4.addWidget(self.line_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.samplingRateLabel = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.samplingRateLabel.sizePolicy().hasHeightForWidth())
        self.samplingRateLabel.setSizePolicy(sizePolicy)
        self.samplingRateLabel.setObjectName("samplingRateLabel")
        self.horizontalLayout_6.addWidget(self.samplingRateLabel)
        self.samplingRateComboBox = QtWidgets.QComboBox(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.samplingRateComboBox.sizePolicy().hasHeightForWidth())
        self.samplingRateComboBox.setSizePolicy(sizePolicy)
        self.samplingRateComboBox.setFrame(True)
        self.samplingRateComboBox.setObjectName("samplingRateComboBox")
        self.horizontalLayout_6.addWidget(self.samplingRateComboBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget_4)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_11.addWidget(self.line)
        self.frequencyLabel = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frequencyLabel.sizePolicy().hasHeightForWidth())
        self.frequencyLabel.setSizePolicy(sizePolicy)
        self.frequencyLabel.setMaximumSize(QtCore.QSize(16777215, 24))
        self.frequencyLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.frequencyLabel.setObjectName("frequencyLabel")
        self.verticalLayout_11.addWidget(self.frequencyLabel)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_11.addWidget(self.label_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frequencyValueLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.frequencyValueLineEdit.setMinimumSize(QtCore.QSize(128, 36))
        self.frequencyValueLineEdit.setMaximumSize(QtCore.QSize(1234124, 36))
        self.frequencyValueLineEdit.setStyleSheet("padding:10px")
        self.frequencyValueLineEdit.setInputMask("")
        self.frequencyValueLineEdit.setMaxLength(5)
        self.frequencyValueLineEdit.setObjectName("frequencyValueLineEdit")
        self.horizontalLayout_2.addWidget(self.frequencyValueLineEdit)
        self.verticalLayout_11.addLayout(self.horizontalLayout_2)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label.setObjectName("label")
        self.verticalLayout_11.addWidget(self.label)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frequencyValueLabel = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frequencyValueLabel.sizePolicy().hasHeightForWidth())
        self.frequencyValueLabel.setSizePolicy(sizePolicy)
        self.frequencyValueLabel.setMinimumSize(QtCore.QSize(75, 0))
        self.frequencyValueLabel.setMaximumSize(QtCore.QSize(100, 24))
        self.frequencyValueLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.frequencyValueLabel.setObjectName("frequencyValueLabel")
        self.horizontalLayout_7.addWidget(self.frequencyValueLabel)
        self.frequencySlider = QtWidgets.QSlider(self.verticalLayoutWidget_4)
        self.frequencySlider.setMaximum(20000)
        self.frequencySlider.setOrientation(QtCore.Qt.Horizontal)
        self.frequencySlider.setObjectName("frequencySlider")
        self.horizontalLayout_7.addWidget(self.frequencySlider)
        self.verticalLayout_11.addLayout(self.horizontalLayout_7)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget_4)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_11.addWidget(self.line_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_11)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.volumeLabel = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.volumeLabel.sizePolicy().hasHeightForWidth())
        self.volumeLabel.setSizePolicy(sizePolicy)
        self.volumeLabel.setMaximumSize(QtCore.QSize(16777215, 24))
        self.volumeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.volumeLabel.setObjectName("volumeLabel")
        self.verticalLayout_12.addWidget(self.volumeLabel)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.volumeValueLabel = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.volumeValueLabel.sizePolicy().hasHeightForWidth())
        self.volumeValueLabel.setSizePolicy(sizePolicy)
        self.volumeValueLabel.setMinimumSize(QtCore.QSize(75, 0))
        self.volumeValueLabel.setMaximumSize(QtCore.QSize(100, 24))
        self.volumeValueLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.volumeValueLabel.setObjectName("volumeValueLabel")
        self.horizontalLayout_8.addWidget(self.volumeValueLabel)
        self.volumeSlider = QtWidgets.QSlider(self.verticalLayoutWidget_4)
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setObjectName("volumeSlider")
        self.horizontalLayout_8.addWidget(self.volumeSlider)
        self.verticalLayout_12.addLayout(self.horizontalLayout_8)
        self.line_4 = QtWidgets.QFrame(self.verticalLayoutWidget_4)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_12.addWidget(self.line_4)
        self.verticalLayout_4.addLayout(self.verticalLayout_12)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.startPushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.startPushButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startPushButton.sizePolicy().hasHeightForWidth())
        self.startPushButton.setSizePolicy(sizePolicy)
        self.startPushButton.setMinimumSize(QtCore.QSize(0, 36))
        self.startPushButton.setMaximumSize(QtCore.QSize(1123412, 16777215))
        self.startPushButton.setObjectName("startPushButton")
        self.horizontalLayout_9.addWidget(self.startPushButton)
        self.stopPushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.stopPushButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopPushButton.sizePolicy().hasHeightForWidth())
        self.stopPushButton.setSizePolicy(sizePolicy)
        self.stopPushButton.setMinimumSize(QtCore.QSize(0, 36))
        self.stopPushButton.setMaximumSize(QtCore.QSize(12342134, 16777215))
        self.stopPushButton.setObjectName("stopPushButton")
        self.horizontalLayout_9.addWidget(self.stopPushButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.signalStartLabel = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.signalStartLabel.setStyleSheet("color:rgb(0, 170, 127)")
        self.signalStartLabel.setObjectName("signalStartLabel")
        self.horizontalLayout_4.addWidget(self.signalStartLabel)
        self.signalStopLabel = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.signalStopLabel.setStyleSheet("color:rgb(255, 0, 0)")
        self.signalStopLabel.setObjectName("signalStopLabel")
        self.horizontalLayout_4.addWidget(self.signalStopLabel)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 451, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tone Generator"))
        self.sinePushButton.setText(_translate("MainWindow", "Sine"))
        self.squarePushButton.setText(_translate("MainWindow", "Square"))
        self.trianglePushButton.setText(_translate("MainWindow", "Triangle"))
        self.sawtoothPushButton.setText(_translate("MainWindow", "Sawtooth"))
        self.label_3.setText(_translate("MainWindow", "Selected Waveform:"))
        self.selectedWaveformLabel.setText(_translate("MainWindow", "Sine Wave"))
        self.samplingRateLabel.setText(_translate("MainWindow", "Sampling Rate"))
        self.frequencyLabel.setText(_translate("MainWindow", "Frequency"))
        self.label_2.setText(_translate("MainWindow", "Enter a frequency value:"))
        self.frequencyValueLineEdit.setPlaceholderText(_translate("MainWindow", "Frequency value"))
        self.label.setText(_translate("MainWindow", "Select a frequency value with slider:"))
        self.frequencyValueLabel.setText(_translate("MainWindow", "20"))
        self.volumeLabel.setText(_translate("MainWindow", "Volume"))
        self.volumeValueLabel.setText(_translate("MainWindow", "0"))
        self.startPushButton.setText(_translate("MainWindow", "Start"))
        self.stopPushButton.setText(_translate("MainWindow", "Stop"))
        self.label_4.setText(_translate("MainWindow", "Signal State:"))
        self.signalStartLabel.setText(_translate("MainWindow", "Signal is being generated"))
        self.signalStopLabel.setText(_translate("MainWindow", "No signal is generated"))
import Resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
