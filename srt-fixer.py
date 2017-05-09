#Iro Spyrou
#P2014120

import sys
import re
import argparse

rexp = re.compile(r'([0-9][0-9]):([0-5][0-9]):([0-5][0-9],[0-9][0-9][0-9])\s-->\s([0-9][0-9]):([0-5][0-9]):([0-5][0-9],[0-9][0-9][0-9])')

parser = argparse.ArgumentParser()
# add mandatory (positional) arguments
parser.add_argument("fname1",help="input srt file name")
parser.add_argument("offset",type=float,help="subtitle offset in seconds to apply (can be fractional)")

# parse arguments
args = parser.parse_args()
if args.offset < 0:
	args.offset = args.offset * -1
	number = str(args.offset)
	s, ms = number.split('.')
	if len(ms) == 1:
		ms = ms + "0"
	if len(ms) == 2:
		ms = ms + "0"
	s = int(s) * -1
	ms = int(ms) * -1
else:
	number = str(args.offset)
	s, ms = number.split('.')
	if len(ms) == 1:
		ms = ms + "0"
	if len(ms) == 2:	
		ms = ms + "0"
	s = int(s)
	ms = int(ms)

with open(args.fname1,newline='') as ifp:	
	for line in ifp:
	
		m = rexp.search(line)
		if m:
			s_h = int(m.group(1))
			s_m = int(m.group(2)) 
			s_s, s_ms = m.group(3).split(',')
			s_s = int(s_s)
			s_ms = int(s_ms)
			s_s = s_s + s
			s_ms = s_ms + ms
			if s_ms >= 1000:
				a = s_ms // 1000
				s_ms = s_ms - (a * 1000)
				s_s = s_s + a
			if s_ms < 0:
				while s_ms < 0:
					s_ms = 1000 + s_ms
					s_s = s_s - 1
			if s_s >= 60:
				a = s_s // 60
				s_s = s_s - (a * 60)
				s_m = s_m + a
			if s_s < 0:
				while s_s < 0:
					s_s = 60 + s_s
					s_m = s_m - 1
			if s_m >= 60:
				a = s_m // 60
				s_m = s_m - (a * 60)
				s_h = s_h + a
			if s_m < 0:
				while s_m < 0:
					s_m = 60 + s_m
					s_h = s_h - 1
			if s_h > 99 or s_h < 0:
				print("Error")
				sys.exit()

			e_h = int(m.group(4))
			e_m = int(m.group(5)) 
			e_s, e_ms = m.group(6).split(',')
			e_s = int(e_s)
			e_ms = int(e_ms)
			e_s = e_s + s
			e_ms = e_ms + ms
			if e_ms >= 1000:
				a = e_ms // 1000
				e_ms = e_ms - (a * 1000)
				e_s = e_s + a
			if e_ms < 0:
				while e_ms < 0:
					e_ms = 1000 + e_ms
					e_s = e_s - 1
			if e_s >= 60:
				a = e_s // 60
				e_s = e_s - (a * 60)
				e_m = e_m + a
			if e_s < 0:
				while e_s < 0:
					e_s = 60 + e_s
					e_m = e_m - 1
			if e_m >= 60:
				a = e_m // 60
				e_m = e_m - (a * 60)
				e_h = e_h + a
			if e_m < 0:
				while e_m < 0:
					e_m = 60 + e_m
					e_h = e_h - 1
			if e_h > 99 or e_h < 0:
				print("Error")
				sys.exit()

			s_h = str(s_h)
			s_m = str(s_m)
			s_s = str(s_s)
			s_ms = str(s_ms)
			e_h = str(e_h)
			e_m = str(e_m)
			e_s = str(e_s)
			e_ms = str(e_ms)

			if len(s_h) == 1:
				s_h = "0" + s_h
			if len(s_m) == 1:
				s_m = "0" + s_m
			if len(s_s) == 1:
				s_s = "0" + s_s
			if len(s_ms) == 1:
				s_ms = "0" + s_ms
			if len(s_ms) == 2:
				s_ms = "0" + s_ms
			if len(e_h) == 1:
				e_h = "0" + e_h
			if len(e_m) == 1:
				e_m = "0" + e_m
			if len(e_s) == 1:
				e_s = "0" + e_s
			if len(e_ms) == 1:
				e_ms = "0" + e_ms
			if len(e_ms) == 2:
				e_ms = "0" + e_ms

			new_line = s_h + ":" + s_m + ":" + s_s + "," + s_ms + " --> " + e_h + ":" + e_m + ":" + e_s + "," + e_ms + "\n"

			sys.stdout.write(new_line)
		else:
			sys.stdout.write(line)

