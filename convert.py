import os
import subprocess

def convert_m4a_to_mp3():
    files = [f for f in os.listdir(os.getcwd()) if f.endswith('.m4a') and not f.startswith('Recording')]

    for file in files:
        mp3_file = file.replace('.m4a', '.mp3')
        command = [
            'ffmpeg',
            '-i', file,
            '-codec:a', 'libmp3lame',
            '-qscale:a', '2',  # Quality, 0 is best, 9 is worst. You can change it accordingly.
            mp3_file
        ]
        subprocess.run(command)
        print(f"Converted {file} to {mp3_file}")

if __name__ == "__main__":
    convert_m4a_to_mp3()
