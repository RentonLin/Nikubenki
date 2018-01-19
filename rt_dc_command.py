# -*- coding: utf-8 -*-
from rt_adb_command import rt_adb_command
import time
import random

class rt_dc_command(object):
	@staticmethod
	def go_to_home():
		rt_adb_command.press_home_button()
	
	def tap(x, y):
		rt_adb_command.tap_point(str(x), str(y))
		
	def swipe(x, y, target_x, target_y):
		rt_adb_command.swipe(str(x), str(y), str(target_x), str(target_y))
	
	#now it only cast sill of No.1
	def cast_drive_skill():
		rt_dc_command.tap(316 + random.randint(1, 5), 1653 + random.randint(1, 5))
		time.sleep(0.45)
		rt_dc_command.tap(527 + random.randint(1, 5), 1653 + random.randint(1, 5))
		
	def tap_pause_button():
		rt_dc_command.tap(479, 334)
		time.sleep(0.4)
		rt_dc_command.tap(100, 334)
		
#rt_dc_command.cast_drive_skill()
#rt_dc_command.tap_pause_button()