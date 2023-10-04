from gpiozero import LED
import time

led = LED(23)

led.on()
time.sleep(5)
led.off()
