import time

import board
import digitalio
import adafruit_character_lcd.character_lcd as character_lcd

lcd_rs = digitalio.DigitalInOut(board.D7)
lcd_en = digitalio.DigitalInOut(board.D8)
lcd_d7 = digitalio.DigitalInOut(board.D18)
lcd_d6 = digitalio.DigitalInOut(board.D23)
lcd_d5 = digitalio.DigitalInOut(board.D24)
lcd_d4 = digitalio.DigitalInOut(board.D25)
lcd_backlight = digitalio.DigitalInOut(board.D13)

lcd_columns = 16
lcd_rows = 2

lcd = character_lcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

def print(text):
    lcd.message = text

def printout(text):
    
    split_text = text.split(":")
    message = split_text[0]
    message += ":\n"
    message += split_text[1]

    lcd.message = message
    time.sleep(5)
    lcd.clear()

def clear():
    lcd.clear()
    lcd.backlight = False