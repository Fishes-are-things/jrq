from gpiozero import LED
import time

K = imput("sleep for: ")

led = LED(23)

while True:

led.toggle()
time.sleep(K)
led.off()
time.sleep(K)
