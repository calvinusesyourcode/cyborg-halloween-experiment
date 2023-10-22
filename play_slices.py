import os
import pygame

def play_slices():
    pygame.init()
    pygame.mixer.init()

    # List all files in CWD that start with "slice" and end with ".mp3"
    files = [f for f in os.listdir(os.getcwd()) if f.startswith('slice') and f.endswith('.mp3')]
    
    # Sort the files to play them in order
    files.sort()

    for filename in files:
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        print(f"Finished playing {filename}")

if __name__ == "__main__":
    play_slices()
