import shodan
import sys
import paramiko
import argparse
from colorama import Fore, Back, Style
from colorama import init
init()

parser = argparse.ArgumentParser()
parser.add_argument('-k', '--key', type=str,
                    help='shodan api key')
parser.add_argument('-a', '--address', type=str,
                    help='Specify host')
parser.add_argument('-l', '--login', type=str,
                    help='Specify login')
parser.add_argument('-p', '--password', type=str,
                    help='Specify password')					
results = parser.parse_args()
api = shodan.Shodan(results.key)
host = results.address
login1 = results.login
password1 = results.password
if host is None:
	try:
		results = api.search('raspberry')	
		for result in results['matches']:
			ssh = paramiko.SSHClient()
			ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			try:
				print(result['ip_str'])
				ssh.connect(result['ip_str'], username='pi', password='raspberry')
				ssh.close()
				print (Fore.GREEN + "Connected")
				print(Style.RESET_ALL)
			except:
				print(Fore.RED + "Error when connecting")
				print(Style.RESET_ALL)
	except shodan.APIError as e:
		print ('Error: %s' % e)	
else:
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(host, username=login1, password=password1)
	ssh.close()
	print (Fore.GREEN + "Connected")
	print(Style.RESET_ALL)

