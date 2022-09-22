# 4. Driving with the Keyboard Arrow Keys [5 points]
def drive_with_keyboard(droid: SpheroEduAPI, speed_delta: int = 10, heading_delta: int = 30, dome_delta: int = 20):
    print('Press ESC key to exit...')
    curr_speed = 0
    curr_heading = 0
    while True:
        key = get_key()
        if key == 'esc':
            return
        elif key == 'up':
            droid.set_speed(curr_speed+speed_delta)
        elif key == 'down':
            droid.set_speed(max(0,curr_speed-speed_delta))
        elif key == 'left':
            droid.set_heading(curr_heading-heading_delta)
        elif key == 'right':
            droid.set_heading(curr_heading+heading_delta)


# 5. Sending a Message via Morse Code [5 points]
def encode_in_morse_code(message: str) -> Iterator[str]:
    LETTERS_TO_MC = {
        'A': '.-', 'B': '-...', 'C': '-.-.',
        'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',  '1': '.----',
        '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...',
        '8': '---..', '9': '----.', '0': '-----'
    }
    for char in message.upper():
        yield LETTERS_TO_MC[char]


def blink(droid: SpheroEduAPI, duration: float):
    droid.set_holo_project_led(255)
    time.sleep(duration)
    droid.set_holo_projector_led(0)


def play_message(droid: SpheroEduAPI, message: str, dot_duration: float = 0.1, dash_duration: float = 0.3,
                 time_between_blips: float = 0.1, time_between_letters: float = 0.5):
    for code in encode_in_morse_code(message):
        for char in code:
            if char == '.':
                blink(droid,dot_duration)
            elif char == '-':
                blink(droid,dash_duration)
            time.sleep(time_between_blips)
        time.sleep(time_between_letters)
