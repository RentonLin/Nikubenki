from rt_dc_command import rt_dc_command
import time


while (True):
	print("try to cast drive_skill")
	rt_dc_command.cast_drive_skill()
	print("sleep")
	time.sleep(5)