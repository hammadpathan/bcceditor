import sys 
import hashlib
import os
from os import system
import codecs
import requests
from requests import Session
import random
import time
import os.path
import json
from termcolor import colored
import colorama
import ctypes
import re
import binascii

#SET TITLE FOR WINDOW
ctypes.windll.kernel32.SetConsoleTitleW("Editor EN")

#CREATE PATH FOR SAVEFILE
dir_path = os.path.dirname(os.path.realpath(sys.argv[0]))
file = "SAVE_DATA(transfer)"
exefile = "EditorEN.exe"
finalpath = os.path.join(dir_path,file) 
exepath = os.path.join(dir_path,exefile)

#CREATE BACKUP
backupsave = 'BackupSave(use_backupmanager_to_restore)'
backuppath = os.path.join(dir_path,backupsave)

#URL TO RECIEVE AND DELETE SAVEFILE
urlrequest = "https://nyanko-save.ponosgames.com/v1/transfers/tcode/reception"
urldelete = "https://nyanko-backups.ponosgames.com/?action=delete&accountId=transfer&pin=confirmation&country=en"

session = Session()
session.verify = os.path.join(dir_path,"charlescert.pem")

def welcomescreen():
	colorama.init()
	universaleditor = (colored("Editor EN", 'magenta', attrs=['bold']))
	names = colored("Lethal / 1plus1equalswindow_", 'cyan', attrs=['bold'])
	names2 = colored("JulietCat", 'yellow', attrs=['bold'])
	names3 = colored("csehydrogen", 'blue', attrs=['bold'])
	names4 = colored("beeven", 'green', attrs=['bold'])
	nott = colored("not", 'red', attrs=['bold'])
	rootjailbreak = colored("root/jailbreak", 'green', attrs=['bold'])
	free = colored("free", 'green', attrs=['bold'])
	print('\033[1mWelcome to ' + universaleditor + ' \033[1mmade by:\n'+ names + ' \033[1mand ' + names2 + '\033[1m; inspired by ' + names3 + ' \033[1mand ' + names4 + '\n\033[1mThis editor does ' + nott + ' \033[1mrequire a '+ rootjailbreak + '.\n\033[1mIt only requires your Transfer Code and Confirmation code.\n\n\nIf you paid for this Editor, you were ripped off. This Editor is available for ' + free + '\033[1m.\n\nGet your codes ready and press enter...\n')
	input()

def checkhash():
	global exechecksum
	with open(exepath, 'rb') as e:
		readdatboi = e.read()
		exechecksum = hashlib.md5(readdatboi).hexdigest()
		e.close()
	
def checkserver():
#CHECK WEBSITE FOR EDITOR VERSION AND CHECK FOR UPDATES/MAINTANENCE
	colorama.init()
	global catfood
	maintenance = colored("The Editor is under maintenance!!!", 'red', attrs=['bold'])
	tryagainlater = colored("Please try again later!", 'red', attrs=['bold'])
	pleaseupdate = colored("Your Editor is OUTDATED! Please UPDATE!", 'red', attrs=['bold'])
	salturl = 'http://1plus1equalswindow.pythonanywhere.com/'
	r = requests.get(salturl)
	response = (json.loads(r.text))
	check = (response['newcheckEN2020'])
	originalmd5 = (response['originalmd5ver3'])
	catfood = (response['catfoodlimit'])
	#compare hash of exe to original
	#if exechecksum == originalmd5:
	#	pass
	#else:
	#	print(colored("WARNING: THE HASH OF THIS EXE DOES NOT MATCH THE ORIGINAL!\nTHIS EXE HAS BEEN ALTERED PLEASE DELETE THIS AND DOWNLOAD THE OFFICIAL ONE!", 'red', attrs=['bold']))
	#	input()
	#	sys.exit(0)
	#confirm to allow exe to run
	if check == "0":
		pass
	#check for maintenance
	elif check == "1":
		print("\n"+(maintenance)+"\n"+(tryagainlater))
		input()
		sys.exit(0)
	#check any updates
	elif check == "2":
		print("\n"+(pleaseupdate))
		input()
		sys.exit(0)

	print (colored("PLEASE USE THE BACKUPMANAGER TO BACKUP YOUR SAVES BEFORE USING THIS EDITOR!!\n", 'red', attrs=['bold']))


def getsave():
	try:
		print('\033[1m\nPlease type only your transfer code:')
		transfercode = input()
		print('\033[1m\nPlease type only your confirmation code:')
		confirmationcode = input()

		noncenum = random.randint(0, 1 << 6)
		noncehash = hashlib.md5(str(noncenum).encode()).hexdigest()

		getsaveurlpost = urlrequest.replace("tcode", transfercode)
		
		receivedata = {
		
		"clientInfo": {
			"client": {
				"countryCode": "en",
				"version": "100400"
			},
			"device": {
				"model": "iPhone12,1"
			},
			"os": {
				"type": "ios",
				"version": "14.400000"
			}
		},
		"nonce": noncehash,
		"pin": str(confirmationcode)
		}
		
		headers = { 
		'content-type':'application/json'
		}
		receivedsave = requests.post(getsaveurlpost, json=receivedata ,headers=headers, verify=False)
		
		validity = (receivedsave.status_code)
		
		if validity == 200:
			with open(finalpath, 'wb') as c:
				c.write(receivedsave.content)
				c.close()
		while validity != 200:
			system('cls')
			colorama.init()
			print (colored("These transfer codes aren't valid!! Please try again.\n", 'red', attrs=['bold']))
			print('\033[1m\nPlease type only your transfer code:')
			transfercode = input()
			print('\033[1m\nPlease type only your confirmation code:')
			confirmationcode = input()

			noncenum = random.randint(0, 1 << 6)
			noncehash = hashlib.md5(str(noncenum).encode()).hexdigest()

			getsaveurlpost = urlrequest.replace("tcode", transfercode)
		
			receivedata = {
		
			"clientInfo": {
				"client": {
					"countryCode": "en",
					"version": "100400"
				},
				"device": {
					"model": "iPhone12,1"
				},
				"os": {
					"type": "ios",
					"version": "14.400000"
				}
			},
			"nonce": noncehash,
			"pin": str(confirmationcode)
			}
		
			headers = { 
			'content-type':'application/json'
			}
			receivedsave = requests.post(getsaveurlpost, json=receivedata ,headers=headers, verify=False)
		
			validity = (receivedsave.status_code)
		
			if validity == 200:
				with open(finalpath, 'wb') as c:
					c.write(receivedsave.content)
					c.close()

	except IOError:
		print (colored("\nYou are missing the cacert.pem file in this directory!\n\nPlease extract all files from the ZIP into the folder!\n", 'red', attrs=['bold']))
		time.sleep(10)
		exit()


def removesave():
	os.remove(finalpath)
	input("\nPress enter to exit")
	sys.exit(0)

def mainmenu():	
	raw_data = f.read()
	choice = "0"

	while choice != "3":
		colorama.init()
		print(colored("\nWhat would you like to do with your save? Type a number:", 'cyan', attrs=['bold']))
		print('\033[1m\n1 = Edit amount of CF\n2 = Edit amount of XP\n3 = Finish, and Get your Transfer Codes!\n')
		choice = input()
		if choice == "1":
			try:
				print("\033[1m\nHow much CF do you want? MAX: " + catfood)
				catfoodamntdec = input()
				val = int(catfoodamntdec)
				catfoodamnthex = hex(val)[2:]
				p = bytes.fromhex("00")
				
				while val > int(catfood):
					system('cls')
					colorama.init()
					print (colored("You cannot put more than " + catfood + " CF! Enter " + catfood + " or lower!" , 'red', attrs=['bold']))
					print("\033[1m\nHow much CF do you want? MAX: " + catfood)
					catfoodamntdec = input()
					val = int(catfoodamntdec)
					catfoodamnthex = hex(val)[2:]
					p = bytes.fromhex("00")
					num = len(catfoodamnthex)
					if (num)==1:
						one = bytes.fromhex("0" + (catfoodamnthex))
						f.seek(7)
						f.write (one)
						f.seek(8)
						f.write (p)
						f.seek(9)
						f.write (p)
					if (num)==2:
						two = bytes.fromhex(catfoodamnthex)
						f.seek(7)
						f.write (two)
						f.seek(8)
						f.write (p)
						f.seek(9)
						f.write (p)
					if (num)==3:
						three = bytes.fromhex("0" + ((catfoodamnthex)[:1]))
						three2 = bytes.fromhex((catfoodamnthex)[1:])
						f.seek(7)
						f.write (three2)
						f.seek(8)
						f.write (three)
						f.seek(9)
						f.write (p)
					if (num)==4:
						four = bytes.fromhex((catfoodamnthex)[-4:-2:])
						four2 = bytes.fromhex((catfoodamnthex)[-2::1])
						f.seek(7)
						f.write (four2) 
						f.seek(8)
						f.write (four)
						f.seek(9)
						f.write (p)
			
				while val < (int(catfood) + 1):
					num = len(catfoodamnthex)
					if (num)==1:
						one = bytes.fromhex("0" + (catfoodamnthex))
						f.seek(7)
						f.write (one)
						f.seek(8)
						f.write (p)
						f.seek(9)
						f.write (p)
					if (num)==2:
						two = bytes.fromhex(catfoodamnthex)
						f.seek(7)
						f.write (two)
						f.seek(8)
						f.write (p)
						f.seek(9)
						f.write (p)
					if (num)==3:
						three = bytes.fromhex("0" + ((catfoodamnthex)[:1]))
						three2 = bytes.fromhex((catfoodamnthex)[1:])
						f.seek(7)
						f.write (three2)
						f.seek(8)
						f.write (three)
						f.seek(9)
						f.write (p)
					if (num)==4:
						four = bytes.fromhex((catfoodamnthex)[-4:-2:])
						four2 = bytes.fromhex((catfoodamnthex)[-2::1])
						f.seek(7)
						f.write (four2) 
						f.seek(8)
						f.write (four)
						f.seek(9)
						f.write (p)
					break
				
				for i in range(101):
					time.sleep(0.01)
					sys.stdout.write("\r%d%%" % i)
					sys.stdout.flush()
				print('\n')
				colorama.init()
				print (colored("Done", 'green', attrs=['bold']))
			#except NameError:
				#colorama.init()
				#print (colored("\nGoing back to the main menu because you didn't type a  nameerror PROPER NUMBER", 'red', attrs=['bold']))
			except ValueError:
				colorama.init()
				print (colored("\nGoing back to the main menu because you didn't type a  valueerror PROPER NUMBER", 'red', attrs=['bold']))
			except TypeError:
				colorama.init()
				print (colored("\nGoing back to the main menu because you didn't type a   typererror PROPER NUMBER", 'red', attrs=['bold']))
		elif choice == "2":
			try:
				print("\033[1m\nHow much XP do you want? MAX: 99999999")
				xpdec = input()
				val2 = int(xpdec)
				xphex = hex(val2)[2:]
				p = bytes.fromhex("00")
			
				while val2 > 99999999:
					system('cls')
					colorama.init()
					print (colored("You cannot add more than 99999999 XP! Enter 99999999 or lower!", 'red', attrs=['bold']))
					print('\033[1m\nHow much XP do you want? MAX: 99999999')
					xpdec = input()
					val2 = int(xpdec)
					xphex = hex(val2)[2:]
					p = bytes.fromhex("00")
				
					numb = len(xphex)
					if (numb)==1:
						onex = bytes.fromhex("0" + (xphex))
						f.seek(76)
						f.write (onex)
						f.seek(77)
						f.write (p)
						f.seek(78)
						f.write (p)
						f.seek(79)
						f.write (p)
					if (numb)==2:
						twox = bytes.fromhex(xphex)
						f.seek(76)
						f.write (twox)
						f.seek(77)
						f.write (p)
						f.seek(78)
						f.write (p)
						f.seek(79)
						f.write (p)
					if (numb)==3:
						threex = bytes.fromhex("0" + ((xphex)[:1]))
						threex2 = bytes.fromhex((xphex)[1:])
						f.seek(76)
						f.write (threex2)
						f.seek(77)
						f.write (threex)
						f.seek(78)
						f.write (p)
						f.seek(79)
						f.write (p)
					if (numb)==4:
						fourx = bytes.fromhex((xphex)[-4:-2:])
						fourx2 = bytes.fromhex((xphex)[-2::1])
						f.seek(76)
						f.write (fourx2)
						f.seek(77)
						f.write (fourx)
						f.seek(78)
						f.write (p)
						f.seek(79)
						f.write (p)
					if (numb)==5:
						fivex = bytes.fromhex("0" + ((xphex)[:1]))
						fivex2 = bytes.fromhex((xphex)[1:3])
						fivex3 = bytes.fromhex((xphex)[3:])
						f.seek(76)
						f.write (fivex3)
						f.seek(77)
						f.write (fivex2)
						f.seek(78)
						f.write (fivex)
						f.seek(79)
						f.write (p)
					if (numb)==6:
						sixx = bytes.fromhex((xphex)[4:])
						six2 = bytes.fromhex((xphex)[2:4])
						six3 = bytes.fromhex((xphex)[:2])
						f.seek(76)
						f.write (sixx)
						f.seek(77)
						f.write (six2)
						f.seek(78)
						f.write (six3)
						f.seek(79)
						f.write (p)
					if (numb)==7:
						sevenx = bytes.fromhex((xphex)[5:])
						sevenx2 = bytes.fromhex((xphex)[3:5])
						sevenx3 = bytes.fromhex((xphex)[1:3])
						sevenx4 = bytes.fromhex("0" + ((xphex)[:1]))
						f.seek(76)
						f.write (sevenx)
						f.seek(77)
						f.write (sevenx2)
						f.seek(78)
						f.write (sevenx3)
						f.seek(79)
						f.write (sevenx4)
			
				while val2 < 100000000:
					numb = len(xphex)
					if (numb)==1:
						onex = bytes.fromhex("0" + (xphex))
						f.seek(76)
						f.write (onex)
						f.seek(77)
						f.write (p)
						f.seek(78)
						f.write (p)
						f.seek(79)
						f.write (p)
					if (numb)==2:
						twox = bytes.fromhex(xphex)
						f.seek(76)
						f.write (twox)
						f.seek(77)
						f.write (p)
						f.seek(78)
						f.write (p)
						f.seek(79)
						f.write (p)
					if (numb)==3:
						threex = bytes.fromhex("0" + ((xphex)[:1]))
						threex2 = bytes.fromhex((xphex)[1:])
						f.seek(76)
						f.write (threex2)
						f.seek(77)
						f.write (threex)
						f.seek(78)
						f.write (p)
						f.seek(79)
						f.write (p)
					if (numb)==4:
						fourx = bytes.fromhex((xphex)[-4:-2:])
						fourx2 = bytes.fromhex((xphex)[-2::1])
						f.seek(76)
						f.write (fourx2)
						f.seek(77)
						f.write (fourx)
						f.seek(78)
						f.write (p)
						f.seek(79)
						f.write (p)
					if (numb)==5:
						fivex = bytes.fromhex("0" + ((xphex)[:1]))
						fivex2 = bytes.fromhex((xphex)[1:3])
						fivex3 = bytes.fromhex((xphex)[3:])
						f.seek(76)
						f.write (fivex3)
						f.seek(77)
						f.write (fivex2)
						f.seek(78)
						f.write (fivex)
						f.seek(79)
						f.write (p)
					if (numb)==6:
						sixx = bytes.fromhex((xphex)[4:])
						six2 = bytes.fromhex((xphex)[2:4])
						six3 = bytes.fromhex((xphex)[:2])
						f.seek(76)
						f.write (sixx)
						f.seek(77)
						f.write (six2)
						f.seek(78)
						f.write (six3)
						f.seek(79)
						f.write (p)
					if (numb)==7:
						sevenx = bytes.fromhex((xphex)[5:])
						sevenx2 = bytes.fromhex((xphex)[3:5])
						sevenx3 = bytes.fromhex((xphex)[1:3])
						sevenx4 = bytes.fromhex("0" + ((xphex)[:1]))
						f.seek(76)
						f.write (sevenx)
						f.seek(77)
						f.write (sevenx2)
						f.seek(78)
						f.write (sevenx3)
						f.seek(79)
						f.write (sevenx4)
					break
				
				for i in range(101):
					time.sleep(0.01)
					sys.stdout.write("\r%d%%" % i)
					sys.stdout.flush()
				print('\n')
				
				colorama.init()
				print (colored("Done", 'green', attrs=['bold']))
			except NameError:
				colorama.init()
				print (colored("\nGoing back to the main menu because you didn't type a  PROPER NUMBER", 'red', attrs=['bold']))
			except ValueError:
				colorama.init()
				print (colored("\nGoing back to the main menu because you didn't type a  PROPER NUMBER", 'red', attrs=['bold']))
			except TypeError:
				colorama.init()
				print (colored("\nGoing back to the main menu because you didn't type a  PROPER NUMBER", 'red', attrs=['bold']))
		elif choice == "3":
			return
		else:
			system('cls')
			colorama.init()
			print (colored("Please enter a number from the list!", 'red', attrs=['bold']))

def patchdata():
	with open(finalpath, 'r+b') as z:
		raw_data = z.read()
		data, checksum = raw_data[:-32], raw_data[-32:]
		newchecksum = hashlib.md5(b'battlecatsen' + data).hexdigest()

		print ('\033[1m\nStarting patcher...')
		if newchecksum != checksum.decode():
			colorama.init()
			print (colored('SAVE_DATA not patched, patching now...', 'red', attrs=['bold']))
			z.seek(-32, os.SEEK_END)
			z.write(binascii.hexlify(bytes.fromhex(newchecksum)))
			colorama.init()
			print (colored('SAVE_DATA patched successfully.', 'green', attrs=['bold']))
		else:
			colorama.init()
			print (colored('\nSAVE_DATA already patched.', 'green', attrs=['bold']))
	input('\nPress Enter to get your transfercodes')
		
def senddata():
	data = open(finalpath, 'rb').read()
	urlpost = 'https://nyanko.ponosgames.com/?action=store&country=en'
	r_num = random.randint(0, 1 << 32)
	ct = int(time.time()*1000)
	bdry = '__-----------------------{}{}'.format(r_num, ct)
	msg = '--' + bdry
	msg += ('\r\nContent-Disposition: attachment; name="saveData";'
			'filename="data.sav"\r\nContent-Type: application/octet'
			'-stream\r\n\r\n')
	msg += data.decode('ISO-8859-1') + '\r\n'
	msg += '--' + bdry + '--'
	headers = {
		'Connection': 'Keep-Alive',
		'Charset': 'UTF-8',
		'Content-Type': 'multipart/form-data;boundary={}'.format(bdry),
		}

	r = requests.post(urlpost, data=msg, headers=headers, verify=False)
	if (r.status_code) == 200:
		response = (json.loads(r.text))
		colorama.init()
		print (colored('\nTransfer Code: ','blue', attrs=['bold']) + colored((response['accountId']), 'cyan', attrs=['bold']))
		colorama.init()
		print (colored('Confirmation Code: ', 'blue', attrs=['bold']) + colored((response['pin']), 'cyan', attrs=['bold']))
		print('\nThose are your codes, put them back in the game.\n')

	if (r.status_code) != 200:
		colorama.init()
		print (colored('\nSomething went wrong!!!! Your save was messed up!!Please close this app and try again! Your save is still in your game, make another transfer.\n', 'red', attrs=['bold']))
		

welcomescreen()
#checkhash()
checkserver()
getsave()
with open(finalpath, 'r+b') as f:
	mainmenu()
	f.close()
patchdata()
senddata()
input("Press ENTER to exit")