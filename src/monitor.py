import time
import board
import digitalio
import adafruit_dht
import adafruit_character_lcd.character_lcd as characterlcd

# ----- DHT11 -----
dht = adafruit_dht.DHT11(
    board.D17,
    use_pulseio=False
)

# ----- LCD pins -----
lcd_rs = digitalio.DigitalInOut(board.D5)
lcd_en = digitalio.DigitalInOut(board.D6)
lcd_d4 = digitalio.DigitalInOut(board.D13)
lcd_d5 = digitalio.DigitalInOut(board.D19)
lcd_d6 = digitalio.DigitalInOut(board.D26)
lcd_d7 = digitalio.DigitalInOut(board.D21)

lcd = characterlcd.Character_LCD_Mono(
    lcd_rs,
    lcd_en,
    lcd_d4,
    lcd_d5,
    lcd_d6,
    lcd_d7,
    16,
    2
)

lcd.clear()

while True:
    try:
        temperature = dht.temperature
        humidity = dht.humidity

        lcd.message = (
            f"Temp: {temperature:.1f} C\n"
            f"Humidity: {humidity}%"
        )

        print(f"Temperature: {temperature:.1f} C")
        print(f"Humidity: {humidity}%")

    except RuntimeError as e:
        print("DHT read failed:", e)

    time.sleep(2)