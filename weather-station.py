
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

R = [255, 0, 0]
O = [255, 165, 0]
Y = [255, 255, 0]
G = [0, 128, 0]
B = [0, 0, 255]
I = [75, 0, 130]
V = [139, 0, 255]
N = [0, 0, 0]

rainbow = [
  R, R, R, R, R, R, R, R,
  O, O, O, O, O, O, O, O,
  Y, Y, Y, Y, Y, Y, Y, Y,
  G, G, G, G, G, G, G, G,
  B, B, B, B, B, B, B, B,
  I, I, I, I, I, I, I, I,
  V, V, V, V, V, V, V, V,
  N, N, N, N, N, N, N, N
  ]

while True:
  temp = int(sense.get_temperature())
  if temp > 19 and temp < 26:
    sense.set_pixels(rainbow)
    sleep(1)
    sense.clear()
    sleep(1)
  else:
    sense.show_message(str(temp), text_colour=[255, 0, 0])
    sleep(1)