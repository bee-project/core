#!/usr/bin/env python
#
#	Bee Anti Forensics Tool   
#
#
# License :
#			Copyright (C) <2013>  <0x0ptim0us (Fardin Allahverdinazhand)>
#
#			This program is free software: you can redistribute it and/or modify
#			it under the terms of the GNU General Public License as published by
#			the Free Software Foundation, either version 3 of the License, or
#			any later version.
#
#			This program is distributed in the hope that it will be useful,
#			but WITHOUT ANY WARRANTY; without even the implied warranty of
#			MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#			GNU General Public License for more details.
#
#			You should have received a copy of the GNU General Public License
#			along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
# Descriptin :
# 	Script For inject Standard Header And Footer In Your Shell Scripts and Other Files, Finally Create Fake File ...
#	
# About Auther :
#	Writen By : Fardin Allahverdinazhand (0x0ptim0us)
#	Email : 0x0ptim0us@gmail.com
#	Web : Http://Turk-BH.ir 
#	Location : Iran - Azarbayjan (Turkish)
#	Date : 2013/4/17
#	Version : 0.1.1 Beta

import optparse
from time import sleep
extensions_list = '''
  bee.py [options]

This Scipt Help You To inject Diffrent Headers And Footers Into Your Files ...
Writen By : Fardin Allahverdinazhand (0x0ptim0us)
Email : 0x0ptim0us@Gmail.com

List Of Supported Extensions :
  Images:
	gif , bmp , jpg , png , tif , art
  Multimedia:
	avi , mov , mpg , ra , wav
  Documents & Others:
	doc , pst , ost , dbx , idx , mbx , mail , zip , java

'''
parse = optparse.OptionParser(usage=extensions_list)
parse.add_option('-t', '--type', help="Type of extension")
parse.add_option('-i', '--input', help="Name of input file")
parse.add_option('-o', '--output', help="Name of output file")
opt, args =parse.parse_args()
class Injector:
	def main(self):
		try:
			if opt.type and opt.input and opt.output:
				if opt.type =="jpg":
					header = "\xFF\xD8\xFF\xE0\x00\x10"
					footer = "\xFF\xD9"
				elif opt.type =="gif":
					header = "\x47\x49\x46\x38\x37\x61"
					footer = "\x00\x3B"
				elif opt.type =="png":
					header = "\x50\x4E\x47?"
					footer = "\xFF\xFC\xFD\xFE"
				elif opt.type =="bmp":
					header = "BM??\x00\x00\x00"
					footer = ""
				elif opt.type =="tif":
					header = "\x49\x49\x2A\x00"
					footer = ""
				elif opt.type =="avi":
					header = "RIFF????AVI"
					footer = ""
				elif opt.type =="mov":
					header = "????????\x6D\x6F\x6F\x76"
					footer = ""
				elif opt.type =="mpg":
					header = "\x00\x00\x01\xBA"
					footer = "\x00\x00\x01\xB9"
				elif opt.type =="doc":
					header = "\xD0\xCF\x11\xE0\xA1\xB1"
					footer = ""
				elif opt.type =="pst":
					header = "\x21\x42\x4E\xA5\x6F\xB5\xA6"
					footer = ""
				elif opt.type =="ost":
					header = "\x21\x42\x44\x4E"
					footer = ""
				elif opt.type =="dbx":
					header = "\xCF\xAD\x12\xFE\xC5\xFD\x74\x6F"
					footer = ""
				elif opt.type =="idx":
					header = "\x4A\x4D\x46\x39"
					footer = ""
				elif opt.type =="mbx":
					header = "\x4A\x4D\x46\x36"
					footer = ""
				elif opt.type =="mail":
					header = "\x41\x4F\x4C\x56\x4D"
					footer = ""
				elif opt.type =="wav":
					header = "RIFF????WAVE"
					footer = ""
				elif opt.type =="ra":
					header = "\x2E\x72\x61\xFD"
					footer = ""
				elif opt.type =="zip":
					header = "PK\x03\x04"
					footer = "\x3C\xAC"
				elif opt.type =="java":
					header = "\xCA\xFE\xBA\xBE"
					footer = ""
				else:
					print "[!]Error : Format Not Supported."
					exit(1)
			else:
				print "[!]Error : Invalid Option!"
				print "[?]Info : Use '--help' or '-h' Switchs For Help."
				exit(1)
			print "[*]Input File : %s"%opt.input
			print "[*]Type Of Extension : %s"%opt.type
			print "[*]Output File : %s"%opt.output
			print "\n[*]Please Wait .....",
			O1 = open(opt.output, "wb")
			O1.write(header)
			O1.close()
			O2 = open(opt.input, "rb").read()
			for line in O2:
				O3 = open(opt.output, "ab")
				O3.write(line)
				O3.close()
			O4 = open(opt.output, "ab")
			O4.write(footer)
			O4.close()
			print " [OK]"
			sleep(1)
			print "[*]Done. [%s] File Has Been Created." % (opt.output)
		except(KeyboardInterrupt):
			print "[!]Ctrl + C Detected ! Exit."


sti = Injector()
if __name__ == "__main__":
	sti.main()

# TBH Security Center
# Copyright <TBH 2013>
# Enjoy.