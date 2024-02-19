import threading
import numpy as np
from scipy import signal
import pyaudio

class SignalGenerator():

    def __init__(self, frequency, sampling_rate, volume, waveform) -> None:
        self.frequency = frequency
        self.sampling_rate = sampling_rate
        self.volume = volume
        self.selected_waveform = waveform
        self.stop_event = threading.Event()  # Event for stopping playback
    
    def _generate_square_wave(self):
        pass

    def _generate_triangular_wave(self):
        pass

    def _generate_sawtooth_wave(self):
        pass

    def _generate_sine_wave(self):
        # Generate a single period of the sine wave
        num_samples = int(self.sampling_rate)
        t = np.linspace(0, 1.0 / self.frequency, num_samples, endpoint=False)
        samples = (np.sin(2 * np.pi * t * self.frequency)).astype(np.float32)
        return samples

    def play_sound_threaded(self):
        p = pyaudio.PyAudio()
        try:
            output_bytes = (self.volume * self._generate_sine_wave()).tobytes()

            stream = p.open(format=pyaudio.paFloat32,
                            channels=1,
                            rate=self.sampling_rate,
                            output=True)
            
            while not self.stop_event.is_set():
                stream.write(output_bytes)

        except Exception as e:
            print(f"Error during playback: {e}")
        finally:
            stream.stop_stream()
            stream.close()
            p.terminate()


    def stop_playback(self):
        # Set the stop_event to signal the playback thread to stop
        self.stop_event.set()
