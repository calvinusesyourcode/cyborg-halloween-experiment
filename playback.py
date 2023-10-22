import pygame
import keyboard
import random

# Initialize pygame
pygame.init()
pygame.mixer.init()

# Array of glitches
glitches = [f"slice_{i}.mp3" for i in range(19)]
hellos = [f"hello{i}.mp3" for i in range(2)]

# Mapping keys to filenamesasdfghjklqwertyuiopzxxxxxxxxcvbbnm
key_to_file = {
    'a': 'anger.mp3',
    'b': 'boring.mp3',
    'c': 'curious.mp3',
    'd': 'DAYUM.mp3',
    'e': 'eh.mp3',
    'f': 'funny.mp3',
    'g': 'good.mp3',
    'h': '', # will play hellos
    'i': 'iam.mp3',
    'j': 'justkidding.mp3',
    'k': 'kool.mp3',
    'l': 'love.mp3',
    'm': 'maybe.mp3',
    'n': 'no.mp3',
    'o': 'optimism.mp3',
    'p': 'poop.mp3',
    'q': 'quiet.mp3',
    'r': 'run.mp3',
    's': 'sad.mp3',
    't': 'true.mp3',
    'u': 'uh.mp3',
    'v': 'very.mp3',
    'w': 'wow.mp3',
    'x': '',  # Special: will play a random glitch
    'y': 'yes.mp3',
    'z': 'zootopia.mp3',
}

# Function to play sound
def play_sound(file):
    pygame.mixer.music.stop()  # Stop any currently playing sound
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

# Callback function for keypress
def on_keypress(e):
    key = e.name
    if key == 'esc':  # Escape key to exit
        keyboard.unhook_all()
        exit()
    if key in key_to_file:
        if key == 'x':  # Special key to play a random glitch
            play_sound(random.choice(glitches))
        elif key == 'h':  # Special key to play a random glitch
            play_sound(random.choice(hellos))
        else:
            play_sound(key_to_file[key])

# Hook keypress event
keyboard.on_press(on_keypress, suppress=True)

# Keep the program running
keyboard.wait()
