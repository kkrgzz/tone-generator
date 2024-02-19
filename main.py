from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import *
from design import Ui_MainWindow

class main(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.qtMainWindow = Ui_MainWindow()
        self.qtMainWindow.setupUi(self)

        self.frequency = 1000
        self.samplingRate = 44100
        self.volume = 50
        self.selectedWaveformString = "Sine Wave"
        self.samplingRateList = ["44100", "96000", "128000", "176400", "192000"]

        # SET DEFAULT VALUES
        self.qtMainWindow.frequencySlider.setValue(self.frequency)
        self.qtMainWindow.frequencyValueLineEdit.setText(f'{self.frequency}')
        self.qtMainWindow.volumeSlider.setValue(self.volume)
        self.qtMainWindow.frequencyValueLabel.setText(f'{self.frequency} Hz')
        self.qtMainWindow.volumeValueLabel.setText(f'{self.volume} %')
        self.qtMainWindow.samplingRateComboBox.addItems(self.samplingRateList)
        self.qtMainWindow.signalStartLabel.setVisible(False)

        # Restricted the range and input type
        self.onlyInt = QIntValidator()
        self.onlyInt.setRange(0, 20000)
        self.qtMainWindow.frequencyValueLineEdit.setValidator(self.onlyInt)

        # BUTTONS
        self.qtMainWindow.sinePushButton.clicked.connect(self.SineWaveClicked)
        self.qtMainWindow.squarePushButton.clicked.connect(self.SquareWaveClicked)
        self.qtMainWindow.trianglePushButton.clicked.connect(self.TriangularWaveClicked)
        self.qtMainWindow.sawtoothPushButton.clicked.connect(self.SawtoothWaveClicked)
        self.qtMainWindow.startPushButton.clicked.connect(self.StartClicked)
        self.qtMainWindow.stopPushButton.clicked.connect(self.StopClicked)
        
        # UPDATE FUNCTIONS
        self.qtMainWindow.frequencySlider.valueChanged.connect(self.FrequencyUpdate)
        self.qtMainWindow.volumeSlider.valueChanged.connect(self.VolumeUpdate)
        self.qtMainWindow.samplingRateComboBox.currentTextChanged.connect(self.SamplingRateUpdate)
        self.qtMainWindow.frequencyValueLineEdit.textChanged.connect(self.FrequencyTextInputChanged)
    
    def FrequencyUpdate(self, value):
        self.qtMainWindow.frequencyValueLabel.setText(f'{value} Hz')
        self.qtMainWindow.frequencyValueLineEdit.setText(f'{value}')
        self.frequency = value

    def FrequencyTextInputChanged(self, value):
        self.qtMainWindow.frequencyValueLabel.setText(f'{value} Hz')
        if value != '':
            self.qtMainWindow.frequencySlider.setValue(int(value))
            self.frequency = int(value)
        else:
            self.qtMainWindow.frequencySlider.setValue(0)
            self.frequency = 0

    def VolumeUpdate(self, value):
        self.qtMainWindow.volumeValueLabel.setText(f'{value} %')
        self.volume = int(value)

    def SamplingRateUpdate(self, value):
        self.samplingRate = int(value)

    def UpdateSelectedWaveformText(self, value):
        self.selectedWaveformString = value
        self.qtMainWindow.selectedWaveformLabel.setText(value)

    def SineWaveClicked(self): self.UpdateSelectedWaveformText("Sine Wave")
    def SquareWaveClicked(self): self.UpdateSelectedWaveformText("Square Wave")
    def TriangularWaveClicked(self): self.UpdateSelectedWaveformText("Triangular Wave")
    def SawtoothWaveClicked(self): self.UpdateSelectedWaveformText("Sawtooth Wave")

    def StartClicked(self):
        self.qtMainWindow.signalStartLabel.setVisible(True)
        self.qtMainWindow.signalStopLabel.setVisible(False)

    def StopClicked(self):
        self.qtMainWindow.signalStartLabel.setVisible(False)
        self.qtMainWindow.signalStopLabel.setVisible(True)

app = QApplication([])
window = main()
window.show()
app.exec_()