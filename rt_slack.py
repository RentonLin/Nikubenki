# -*- coding: utf-8 -*-
import requests
import json
	
class rt_slack(object):
	@staticmethod
	def upload_text(text, icon_emoji=":ghost:"):
		headers = {'Content-Type': 'application/json'}
		params = {"icon_emoji": icon_emoji,
			"text": text,
			"username": "car_watcher_daze"}
		payload = json.dumps(params)
		print('payload is ' + payload)
		
		response = requests.post('https://hooks.slack.com/services/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', data=payload, headers=headers)
		print(response, response.status_code, response.text)
		
	def upload_car():
		rt_slack.upload_text("出车啦~快来上啊(Ahe脸)")
	
	def upload_net_error():
		rt_slack.upload_text("网络出错啦(Ahe脸)，修一下～")
		