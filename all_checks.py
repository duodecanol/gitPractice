#!/usr/bin/env python3

import os
import shutil
import sys
import socket

def check_reboot():
	"""returns True if the computer has a pending reboot."""
	return os.path.exists("/run/reboot-required")

def check_disk_full(disk, min_absolute, min_percent):
	"""Returns True if there isn't enough disk space, False otherwise."""
	du = shutil.disk_usage(disk)
	# Calculate the percentage of free space
	percent_free = 100 * du.free / du.total
	# Calculate how many free gigabytes
	gigabytes_free = du.free / 2**30
	if percent_free < min_percent or gigabytes_free < min_absolute:
		return True
	return False

def check_root_full():
	"""Returns True if the root partition is full, False otherwise"""
	return check_disk_full(disk="/", min_absolute=2, min_percent=10)

def check_no_network():
	"""Returns True if it fails to resolve Google's URL, False otherwise"""
	try:
		socket.gethostbyname("www.google.com")
		return False
	except:
		return True

def main():
	checks = [
		(check_reboot, "Pending Reboot."),
		(check_root_full, "Root partition full"),

		(check_no_network, "No working network.")
		]

	everython_ok=True
	for check, msg in checks:
		if check():
			print(msg)
			everython_ok=False
	
	if not everython_ok:
		sys.exit(1)
		
	print("Everython OK.")
	sys.exit(0)

main()