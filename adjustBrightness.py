#!/usr/bin/python

#I wrote this script to use with xfce on my fn keys to turn brightness up and down.
#I tried a bunch of different methods for getting the keys working on this machine,
#and none of them worked. Rather than bang my head against it I decided it would be
#faster to just make a script.
#
#Ymmv this script requires sticky bit, or you can open up your /sys/.../brightness
#file for others to use. Using this script may mean sacrificing some security
#on your system due to either changing brightness file perms or executing it as
#suid.
#
#In order for this to work on your system you will need to find your
#brightness file in sys. Edit the variables below.

####Do not edit.####
import argparse,sys#
####################

#Edit to fit your system.
location = "/sys/class/backlight/intel_backlight/brightness"

#This is what the max brightness of your monitor is, mine is 6k
#change to fit your system.
maxBrightness = 6000

#This is the amount it will go down or up per usage.
#It will never go above max.
brightnessIncrement = 500






#End of user settings.
#############################################################
def fullDim():
	f=open( location, 'r+' )
	f.write( str(0) )
	print "Brightness at: 0"
	f.close()

def fullBright():
	f=open( location, 'r+' )
	f.write( str(maxBrightness) )
	f.close()

def up():
	f=open( location, 'r+' )
	bstring = f.read()
	bnumber = int(bstring)

	if bnumber < maxBrightness:
		bnumber = bnumber + brightnessIncrement
		bstring = str(bnumber)
		print "Brightness at: ", bnumber
		f.write( bstring )
		f.close()
	else:
		print "Reached maximum adjustment allowed in script."		
		f.close()

def down():
	f=open( location, 'r+' )
	bstring = f.read()
	bnumber = int(bstring)

	if bnumber > brightnessIncrement:
		bnumber = bnumber - brightnessIncrement
		bstring = str(bnumber)
		print "Brightness at: ", bnumber		
		f.write( bstring )
		f.close()
	else:
		print "Reached maximum adjustment allowed in script."		
		f.close()

class CustomParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)


parser = CustomParser( description = 'Adjust screen brightness settings.' )

parser.add_argument('--up', help='This will turn up display brightness.', 
action='store_true', default=False )

parser.add_argument('--down', help='This will turn down display brightness.', 
action='store_true', default=False )

parser.add_argument( '--black', help='This will drop screen brightness to 0.',
action='store_true', default = False )

parser.add_argument( '--full', help='This will set the screen to max brightness.',
action='store_true', default = False)

args = parser.parse_args()
if args.black == True:
	fullDim()

if args.full == True:
	fullBright()

if args.up == True:
	up()

if args.down == True:
	down()


