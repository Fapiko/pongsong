import subprocess
import time
from ping import Ping

delay = 1000

while True:
	ping = Ping(subprocess.check_output(['ping', 'minecraft.fapiko.com', '-c 1']))
	print "%s %s" % (time.strftime('%a, %d %b %Y %H:%M:%S +0000', time.gmtime()), ping.time)
	# print ping.time
	ping.sleep()