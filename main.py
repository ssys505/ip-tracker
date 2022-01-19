import requests
import socket
def track(ip):
	response = requests.get(f'http://ip-api.com/json/{ip}')
	dic = response.json()
	print("")
	print("country: "+dic['country'])
	print("regionName: "+dic['regionName'])
	print("city: "+dic['city'])
	print("Pincode: "+dic['zip'])
	print("lat: "+str(dic['lat']))
	print("lon: "+str(dic['lon']))
	print("timezone: "+dic['timezone'])
	print("isp: "+dic['isp'])
	print("Ip: "+str(dic['query']))

def main():
	meun = '''
	Enter 1 for Track your IP..
	Enter 2 for Track Victim IP..
	Enter 3 for know about US..
	'''
	print(meun)
	command = input('>> ')
	if(int(command) == 1):
		ip = requests.get("https://api.ipify.org/").text
		track(ip)
	elif(int(command) == 2):
		print("")
		ip = str(input("Enter Ip >> "))
		track(ip)
	elif(int(command) == 3):
		print('''
	We have created this project only for legends.. 
	Don't use it for Illigal work..
	Project Owner : github(ssys505)
	Project Owner : insta(katssys505)
			''')
	else:
		print("Enter correct command..")
		main()
main()