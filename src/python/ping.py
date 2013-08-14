import re
import time

class Ping:
	def __init__(self, ping):
		match = re.search('time=(\d+) ', ping)
		self.time = int(match.group(1))

	def sleep(self):
		if self.time >= 1000:
			return

		time.sleep(1 - (self.time/1000.0))
