import pyaudio
import wave
import subprocess

# Function to capture system audio
def capture_system_audio(output_filename, duration, device):
    # Record system audio using the "ffmpeg" command
    command = [
        "ffmpeg",
        "-f", "dshow",
        "-i", "audio="+device,
        "-t", str(duration),
        output_filename,
    ]

    subprocess.run(command, shell=True)

def show_capture_systems():
    command = [
        "ffmpeg",
        "-list_devices", "true",
        "-f", "dshow",
        "-i", "dummy"
    ]

    subprocess.run(command, shell=True)


if __name__ == "__main__":
    audio_filename = input("Name of the Audio file add(.wav): ")
    open(audio_filename, "w")
    duration = int(input("Enter duration of recording in seconds: "))
    show_capture_systems()
    device = input("Enter a device name: ")

    capture_system_audio(audio_filename, duration, device)