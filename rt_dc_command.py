# -*- coding: utf-8 -*-
from rt_adb_command import rt_adb_command
import time
import random
from PIL import Image
from strategy import rt_dc_strategy, smartphone_dc_strategy

class rt_dc_command(object):
	current_strategy = smartphone_dc_strategy()
		
	@staticmethod
	def set_current_strategy(strategy):
		rt_dc_command.current_strategy = strategy
		
	def go_to_home():
		rt_adb_command.press_home_button()
	
	def tap(x, y):
		rt_adb_command.tap_point(str(x), str(y))
		
	def swipe(x, y, target_x, target_y):
		rt_adb_command.swipe(str(x), str(y), str(target_x), str(target_y))
	
	#now it only cast sill of No.1
	def cast_drive_skill():
		rt_dc_command.tap(rt_dc_command.current_strategy.second_chara_drive_x + random.randint(1, 5), rt_dc_command.current_strategy.second_chara_drive_y + random.randint(1, 5))
		time.sleep(0.45)
		rt_dc_command.tap(rt_dc_command.current_strategy.drive_x + random.randint(1, 5), rt_dc_command.current_strategy.drive_y + random.randint(1, 5))
		
	def tap_pause_button():
		rt_dc_command.tap(479, 334)
		time.sleep(0.4)
		rt_dc_command.tap(100, 334)
	
	def tap_refresh_car_button():
		x = rt_dc_command.current_strategy.refresh_button_x +  random.randint(0, 6) - 3 
		y = rt_dc_command.current_strategy.refresh_button_y + random.randint(0, 6) - 3
		print(rt_dc_command.tap(x, y))
	
	def check_screenshot_car(filepath):
		image = Image.open(filepath, 'r')
		pix = image.load()

		point_x = rt_dc_command.current_strategy.check_point_x
		point_y = rt_dc_command.current_strategy.check_point_y
		pixel = pix[point_x, point_y]
		print(pix[point_x, point_y])
		r = pixel[0]
		g = pixel[1]
		b = pixel[2]
		#color = hex(r * 16 * 16 * 16 * 16 + g * 16 * 16 + b)
		#print(r, g, b)
		#print(color)

		#todo now net error is not taken into consideration
		#check if any car exists
		foundCar = ((r == 255 and g == 255 and b == 255) | (r == 31 and g == 35 and b == 23))
		neterror = (r == 12 and g == 12 and b == 12)
		return (foundCar, neterror)
	
	def go_back_to_game():
		rt_dc_command.tap(rt_dc_command.current_strategy.return_to_app_x, rt_dc_command.current_strategy.return_to_app_y)
		