#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import json
import datetime
import time
import random
import os

def get_current_human_time():
	value = datetime.datetime.fromtimestamp(time.time())
	return value.astimezone(datetime.timezone.utc).strftime('UTC %Y-%m-%d %H:%M:%S')




def run_cmd(cmdAndArgsList):
	#print(cmdAndArgsList)
	retryCount = 10
	out = b''
	err = b''
	for i in range(retryCount):
		p = subprocess.Popen(cmdAndArgsList, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		out, err = p.communicate()
		if err == b'':
			return out.decode('utf-8')
		elif "kex_exchange_identification" in err.decode('utf-8'): # Just try again in this case.
			continue
		else:
			# Assume this is an ssh connection error.
			print(f"[{get_current_human_time()}] stderr: \"{err.decode('utf-8')}\" from cmd {cmdAndArgsList}") # This could go to stderr or stdio.
			return out.decode('utf-8')
		#pass
		#raise IOError(f"Non-empty error: {err.decode('utf-8')}")
	print(f"[{get_current_human_time()}] Max retries ({retryCount}) reached. stderr: \"{err.decode('utf-8')}\" from cmd {cmdAndArgsList}") # This could go to stderr or stdio.
	return out.decode('utf-8')
		

def run_cmd_at_node(nodeConfig, cmd):
	# change to "-oStrictHostKeyChecking=accept-new" for increased security on newer systems. "-oStrictHostKeyChecking=no",
	dirname = os.path.dirname(os.path.realpath(__file__))
	return run_cmd(["ssh", f"-i{dirname}/../keys/vultr/{nodeConfig['key']}", "-oStrictHostKeyChecking=accept-new", f"{nodeConfig['user']}@{nodeConfig['ip']}", cmd])
