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

        # Define the duration of each chunk in seconds
        self.chunk_duration = 0.5  # Adjust this value as I needed

        self.stop_event = threading.Event()  # Event for stopping playback
    
    def _set_samples(self):
            match self.selected_waveform:
                case "Sine Wave":
                    samples = self._generate_sine_wave(self.chunk_duration)

                case "Square Wave":
                    samples = self._generate_square_wave(self.chunk_duration)

                case "Triangular Wave":
                    pass

                case "Sawtooth Wave":
                    pass

                case _:
                    self.selected_waveform = "Sine Wave"
                    samples = self._generate_sine_wave(self.chunk_duration)

            return samples
        

    def _generate_sine_wave(self, duration):
        num_samples = int(self.sampling_rate * duration)
        t = np.linspace(0, duration, num_samples, endpoint=False)
        samples = (np.sin(2 * np.pi * t * self.frequency)).astype(np.float32)
        return samples

    def _generate_square_wave(self, duration):
        num_samples = int(self.sampling_rate * duration)
        t = np.linspace(0, duration, num_samples, endpoint=False)
        samples = (signal.square(2 * np.pi * t * self.frequency)).astype(np.float32)
        return samples

    def _generate_triangular_wave(self):
        pass

    def _generate_sawtooth_wave(self):
        pass

    def play_sound_threaded(self):
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paFloat32,
                        channels=1,
                        rate=self.sampling_rate,
                        output=True)
        
        try:
            while not self.stop_event.is_set():
                output_bytes = (self.volume * self._set_samples()).tobytes()
                stream.write(output_bytes)

        except Exception as e:
            print(f"Error during playback: {e}")
        finally:
            stream.stop_stream()
            stream.close()
            p.terminate()


    def stop_playback(self):
        self.stop_event.set()

    def reset_playback(self):
        # Create a new threading.Event for the next playback
        self.stop_event = threading.Event()
        
