# -*- coding: utf-8 -*-
from rt_dc_command import rt_dc_command
from rt_adb_command import rt_adb_command
from rtcommand import rtcommand
from rt_slack import rt_slack
import time, datetime, random
from strategy import rt_dc_strategy

class rt_farm:
	
	@staticmethod
	def set_current_strategy(strategy):
		rt_dc_command.set_current_strategy(strategy)
		
	def farm_exp():
		while (True):
			print("try to cast drive_skill")
			print(rt_dc_command.cast_drive_skill())
			print("sleep")
			time.sleep(5)
	
	def refresh_car_list(fake=False):
		#loop
		foundCar = False
		while (not foundCar):
			#make a adb tap event
			print('tap')
			rt_dc_command.tap_refresh_car_button()

			#waiting for refresh completed
			print("waiting for refresh completed")
			time.sleep(5)
			
			#screenshot
			print('taking a screenshot')
			timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y_%m_%d_%H_%M_%S')
			print(timestamp)
			file_name = timestamp + '.png'
			file_path = 'screenshots/' + file_name
			rt_adb_command.take_screenshot(file_path)

			#get a pixel of the image
			#file_path = 'screenshots/test.png'
			print('checking the screenshot')
			foundCar = rt_dc_command.check_screenshot_car(file_path)
			print("existed:" + str(foundCar))
			
			time_interval = 30 + random.randint(10, 20)
			if not fake:
				time_interval = 10
			if (foundCar):
				#upload to slack if this is a car
				print('Car found, upload to slack')
				rt_slack.upload_car()
				
#				time_interval = 180
				
				#stroe picture to cars folder
				rtcommand.run_command('mv ' + file_path + ' cars/' + file_name)
			else:
				print('not found')
				
				if 5 == random.randint(1, 10):
					rtcommand.run_command('mv ' + file_path + ' nocars/' + file_name)
				
				if fake:
				#go to main screen
					rt_dc_command.go_to_home()
					time.sleep(time_interval)		
					#go back
					rt_dc_command.go_back_to_game()			
					time.sleep(5)
				else:
					time.sleep(time_interval)