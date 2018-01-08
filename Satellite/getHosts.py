#!/usr/bin/env python

import sys, json, requests
import argparse
from getpass import getpass

### We need to prompt the user for authentication details to avoid hard coding creds
### Here we will define the arguments --username and --password.
parser = argparse.ArgumentParser(description='Query the Foreman API to get the necessary information for monthly reporting')
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

## Connect to Satellite server

SAT_API = "%s/katello/api/v2/" % URL
KATELLO_API = "%s/katello/api/" % URL
POST_HEADERS = {'content-type': 'application/json'}

SSL_VERIFY = False

ORG_NAME = "bne-home.net"
ENVIRONMENTS = ["Development", "Testing", "Production"]

def get_hosts(hosts):
    print("Making API Call")
    f = open('/tmp/hosts', 'w')
    r = requests.get(URL + "/api/hosts", auth=(USERNAME, PASSWORD), verify=SSL_VERIFY)
    r = r.json()
    for item in r['results']:
        host = item['certname']
        ident = str(item['id'])
        print(ident + host)
        req = requests.get(URL + "/api/hosts/" + host, auth=(USERNAME, PASSWORD), verify=SSL_VERIFY)
        req = req.json()
        cpus = req['facts']['processorcount']
        f.write(ident + ',' + host + ',' + cpus + '\n')
        print(req['facts']['processorcount'])
        #for system in req['results'][host]["cpu::cpu_socket(s)"]:
         #   print(system)
            #sockets = system['physicalprocessorcount']
            #print(sockets)



def main():
    """
    Main routine that creates or re-uses an organization and
    life cycle environments. If life cycle environments already
    exist, exit out.
    """

    # Check if our organization already exists
    org = get_hosts(SAT_API + "organizations/" + ORG_NAME)

    # If our organization is not found, create it

    # Now, let's get a list of hosts
    host_list = get_hosts(SAT_API + "/hosts")

    #hosts = json.dump(host_list["results"["certname"]])
    print(host_list)


if __name__ == "__main__":
    main()
