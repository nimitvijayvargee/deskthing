from adafruit_st7735r import ST7735R
import displayio
import busio
import board
from fourwire import FourWire
import terminalio
from adafruit_display_text import label
import jpegio
import wifi
import socketpool
import adafruit_requests
import ssl
from io import BytesIO
WIFI_SSID = <SSID>
WIFI_PASSWORD = <PASS>
wifi.radio.connect(WIFI_SSID, WIFI_PASSWORD)
pool = socketpool.SocketPool(wifi.radio)
ssl_context = ssl.create_default_context()
requests = adafruit_requests.Session(pool, ssl_context)
def scale_bitmap(src_bitmap, new_width, new_height):
    src_width = src_bitmap.width
    src_height = src_bitmap.height
    dst_bitmap = displayio.Bitmap(new_width, new_height, 65535)
    for y in range(new_height):
        for x in range(new_width):
            src_x = int(x * src_width / new_width)
            src_y = int(y * src_height / new_height)
            color = src_bitmap[src_x, src_y]
            dst_bitmap[x, y] = color
    return dst_bitmap
displayio.release_displays()
display_bus = FourWire(
    busio.SPI(clock=board.GP18, MOSI=board.GP19),
    command=board.GP22,
    chip_select=board.GP21,
    reset=board.GP20
)
display = ST7735R(display_bus, width=160, height=128, rotation=90)
splash = displayio.Group()
display.root_group = splash
text_group.append(text_area)
splash.append(text_group)
print("MAC addr:", [hex(i) for i in wifi.radio.mac_address])
print(f"IP address is {wifi.radio.ipv4_address}")
url = "https://i.scdn.co/image/ab67616d00001e02de3c04b5fc750b68899b20a9"
response = requests.get(url)
image_bytes = BytesIO(response.content)
response.close()
decoder = jpegio.JpegDecoder()
width, height = decoder.open(image_bytes)
big_bitmap = displayio.Bitmap(width, height, 65535)
decoder.decode(big_bitmap)
scaled_bitmap = scale_bitmap(big_bitmap, 128, 128)
sprite = displayio.TileGrid(scaled_bitmap, pixel_shader=displayio.ColorConverter())
group = displayio.Group()
group.append(sprite)
display.root_group = group
