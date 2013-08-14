import subprocess
import time
from ping import Ping

hostname = 'minecraft.fapiko.com'

while True:
	try:
		ping = Ping(subprocess.check_output(['ping', hostname, '-c 1', '-w 5']))
		print "%s %s %s" % (time.strftime('%a, %d %b %Y %H:%M:%S +0000', time.gmtime()), hostname, ping.time)
		ping.sleep()
	except subprocess.CalledProcessError:
		print "%s %s %s" % (time.strftime('%a, %d %b %Y %H:%M:%S +0000', time.gmtime()), hostname, "Timeout")
