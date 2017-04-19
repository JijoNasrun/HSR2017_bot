from gpiozero import Buzzer
from time import sleep

buzzer = Buzzer(14)

while True:
	buzzer.on()
	sleep(0.1)
	buzzer.off()
	sleep(0.5)
