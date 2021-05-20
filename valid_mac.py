import re
def valid_mac(filename):
	with open(filename, 'r') as f:
		f.readline()
		for line in f:
			server, mac,last_modified = line.strip().split()
			pattern = r'^([0-9A-F]{2}:){5}[0-9A-F]{2}$'
			if re.match(pattern, mac):
				print(server,mac)


valid_mac('servers_mac.txt')