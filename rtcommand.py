# -*- coding: utf-8 -*-

import subprocess

class rtcommand(object):
	@staticmethod
	def run_command(command):
		procId = subprocess.Popen(command, shell=True, stdin = subprocess.PIPE, stderr=subprocess.PIPE)
		stdout, stderror = procId.communicate()
		return (stdout, stderror)
		
#test
#rtcommand.run_command("ls")