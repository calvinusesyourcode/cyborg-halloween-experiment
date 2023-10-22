import subprocess
import os

def split_by_silence(input_file, silence_threshold=-40.0, silence_length=500):
    # Use ffmpeg to detect silences in the audio
    command = [
        'ffmpeg',
        '-i', input_file,
        '-af', f'silencedetect=noise={silence_threshold}dB:d={silence_length / 1000}',
        '-f', 'null',
        '-y', '/dev/null'
    ]

    # Get silencedetect output
    result = subprocess.run(command, stderr=subprocess.PIPE, text=True)
    output = result.stderr

    # Parse silencedetect output to get silence intervals
    slices = []
    start = None
    last_end = 0.0  # Keep track of the last ending time of silence

    for line in output.split('\n'):
        if "silence_start" in line:
            start = float(line.split(":")[1].strip())
            if start - last_end > 0:
                slices.append((last_end, start))
        if "silence_end" in line:
            end = float(line.split(":")[1].split("|")[0].strip())
            last_end = end

    # Create audio slices based on NON-silence intervals
    for i, (start, end) in enumerate(slices):
        output_file = f'slice_{i}.mp3'
        command = [
            'ffmpeg',
            '-ss', str(start),
            '-to', str(end),
            '-i', input_file,
            '-acodec', 'copy',
            '-y', output_file
        ]
        subprocess.run(command)

if __name__ == "__main__":
    split_by_silence('glitch.mp3', silence_threshold=-40.0, silence_length=500)
