# -*- coding: utf-8 -*-

class rt_dc_strategy(object):
	def __init__(self):
		#coordinate of refresh button, in pixel
		self.refresh_button_x = 0
		self.refresh_button_y = 0
		#coordinate of the point to check if it it a car
		self.check_point_x = 0
		self.check_point_y = 0
		
		#the rgb values of a car image pixel
		self.foundcar_color_r = 255
		self.foundcar_color_g = 255
		self.foundcar_color_b = 255
		self.foundcar_color_r_double = 31
		self.foundcar_color_g_double = 35
		self.foundcar_color_b_double = 23
		
		#the point to tap to return to game
		self.return_to_app_x = 0
		self.return_to_app_y = 0
		
		#the point of the drive button of the second character
		self.second_chara_drive_x = 0
		self.second_chara_drive_y = 0
		self.drive_x = 0
		self.drive_y = 0

class smartphone_dc_strategy(rt_dc_strategy):
	def __init__(self):
		self.refresh_button_x = 0x91
		self.refresh_button_y = 0x29b
		self.check_point_x = 74
		self.check_point_y = 775
		
		self.return_to_app_x = 400
		self.return_to_app_y = 1698
		
		self.second_chara_drive_x = 316
		self.second_chara_drive_y = 1653
		self.drive_x = 527
		self.drive_y = 1653
	