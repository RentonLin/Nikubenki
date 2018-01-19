# -*- coding: utf-8 -*-
from rtcommand import rtcommand

adb_path = "/Users/linweichao/dc_car_watcher/adb"

class rt_adb_command:
	@staticmethod
	def input_event(command):
		return rtcommand.run_command(adb_path + " shell " + command)
	
	def input_keyevent(command):
		return rt_adb_command.input_event("input keyevent" + " " + command)
		
	def press_home_button():
		return rt_adb_command.input_keyevent("3")
		
	def tap_point(x, y):
		return rt_adb_command.input_event("input tap" + " " + x + " " + y)
	
	def swipe(x, y, target_x, target_y):
		return rt_adb_command.input_event("input swipe" + " " + x + " " + y + " " + target_x + " " + target_y)
		
	def take_screenshot(filepath):
		return rtcommand.run_command(adb_path + " exec-out screencap -p > " + filepath)

#print(rt_adb_command.tap_point(479, 334))