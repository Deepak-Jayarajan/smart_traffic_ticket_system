from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import os

reader = SimpleMFRC522()

print("Hold a tag near the reader")

try:
    id, text = reader.read()
    print(id)
    print(text)
    os.system("python3 send_sms.py")

finally:
    GPIO.cleanup()
