import sys
import time
import threading
import keyboard

def txtlore(text, delay=0.1):
    def print_text():
        for char in text:
            if keyboard.is_pressed('enter'):
                sys.stdout.write(text[printed_chars:])
                sys.stdout.flush()
                break
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()
    
    printed_chars = 0
    text_thread = threading.Thread(target=print_text)
    text_thread.start()
    text_thread.join()

# Exemplo de uso
txtlore("Este é um exemplo de texto sendo impresso com delay.", delay=0.1)
