#!/usr/bin/env python

import sys, json, requests
import argparse
from getpass import getpass

### We need to prompt the user for authentication details to avoid hard coding creds
### Here we will define the arguments --username and --password.
parser = argparse.ArgumentParser(description='Add Username and Password')
parser.add_argument('-u', '--username', nargs=1, dest='username', required=True, help='Username for Connecting to Satellite')
parser.add_argument('-p', '--password', action='store_true', dest='password', required=True, help='Field for calling a Password prompt')
parser.add_argument('-H', '--host', nargs=1, dest='host', required=False, help='Specify a URL to connect to. Such as https://satellite.example.com')
args=parser.parse_args()

if args.password:
    PASSWORD = getpass()
if args.username:
    USERNAME = args.username[0]
if args.host:
    URL = args.host[0]
else:
    URL = "https://foreman.bne-home.net"

if 'https://' not in URL:
    URL = "https://%s" % args.host[0]

## Connect to Satellite server
DEBUG = 0
SAT_API = "%s/katello/api/v2/" % URL
KATELLO_API = "%s/katello/api/" % URL
POST_HEADERS = {'content-type': 'application/json'}

SSL_VERIFY = False

ORG_NAME = "bne-home"
ENVIRONMENTS = ["Development", "Testing", "Production"]

def get_hosts(hostCall):
    print("Making API Call")
    socks = ''
    ident = ''
    f = open('/tmp/hosts.csv', 'w')
    f.write("ID,Hostname,CPUs, OS \n")
    r = requests.get(URL + "/api/hosts" , auth=(USERNAME, PASSWORD), verify=SSL_VERIFY)
    r = r.json()
    for item in r['results']:
        name = item['certname']
        ident = item['id']
        ident = str(ident)
        operatingSystem = item['operatingsystem_name']
        ## FIX ME ##
        if 'RedHat' or 'RHEL' in operatingSystem:
            try:
                    req = requests.get(URL + "/api/hosts/" + str(ident), auth=(USERNAME, PASSWORD), verify=SSL_VERIFY)
                    req = req.json()
                    socks = req['facts']['cpu::cpu_socket(s)']
                    f.write(str(ident) + "," + name + "," + str(socks) + "," + operatingSystem + '\n')
            except KeyError or TypeError as e:
                    if DEBUG:
                        print(e)
                    else:
                        continue
        else:
            socks = '0'
            f.write(str(ident) + "," + name + "," + str(socks) + "," + operatingSystem + '\n')
            continue
    f.close()
    return (open("/tmp/hosts.csv", "r"))


def main():
    """
    Main routine that creates or re-uses an organization and
    life cycle environments. If life cycle environments already
    exist, exit out.
    """

    # Check if our organization already exists
    #org = get_hosts(SAT_API + "organizations/" + ORG_NAME)

    # If our organization is not found, create it

    # Now, let's get a list of hosts

    for line in get_hosts(SAT_API):
        print(line)

if __name__ == "__main__":
    main()
