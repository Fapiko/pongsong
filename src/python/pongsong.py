import subprocess
import time
from ping import Ping

delay = 1000

while True:
	ping = Ping(subprocess.check_output(['ping', 'fapiko.com', '-c 1']))
	print ping.time
	ping.sleep()