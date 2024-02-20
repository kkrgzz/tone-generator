from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import *
from design import Ui_MainWindow
from Signal import SignalGenerator


class PlaybackThread(QThread):
    def __init__(self, signal_generator, parent=None):
        super().__init__(parent)
        self.signal_generator = signal_generator

    def run(self):
        self.signal_generator.play_sound_threaded()

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

        self.signal_generator = SignalGenerator(frequency=self.frequency, 
                                                sampling_rate=self.samplingRate, 
                                                volume=self.volume, 
                                                waveform=self.selectedWaveformString)

        self.playback_thread = PlaybackThread(self.signal_generator)
        self.playback_thread.finished.connect(self.handle_playback_finished)

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
        try:
            frequency = float(self.frequency)
            volume = self.volume / 100  # Normalize volume to 0.0-1.0 range
            sampling_rate = self.samplingRate

            self.signal_generator.frequency = frequency
            self.signal_generator.volume = volume
            self.signal_generator.sampling_rate = sampling_rate

            # Connect thread signals and start it
            self.playback_thread.start()  # Start playback in a separate thread

        except ValueError as e:
            print(f"Invalid input: {e}")

        self.qtMainWindow.signalStartLabel.setVisible(True)
        self.qtMainWindow.signalStopLabel.setVisible(False)
        self.qtMainWindow.startPushButton.setEnabled(False)
        self.qtMainWindow.stopPushButton.setEnabled(True)
    
    def handle_playback_finished(self):
        self.qtMainWindow.signalStartLabel.setVisible(False)
        self.qtMainWindow.signalStopLabel.setVisible(True)
        self.qtMainWindow.startPushButton.setEnabled(True)
        self.qtMainWindow.stopPushButton.setEnabled(False)
        self.signal_generator.reset_playback()

    def StopClicked(self): self.signal_generator.stop_playback()

app = QApplication([])
window = main()
window.show()
app.exec_()