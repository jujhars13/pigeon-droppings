#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''pigeon droppings the Ansible version

Get the Running EC2 instances in your AWS beginning with <query> outputs in ansible friendly json
Usage:
  pd [options] --list
  pd [options] --host <hostname>
  pd (-h | --help)

Examples:
  pd --list

Options:
  --list                      return all instances
  --host <hostname>           return all info about a host
  -h --help                   Show this screen.
  -v                          Verbose output
  --version                   Show version.
  --id=<AWS ACCESS_KEY_ID>    Your AWS account access id
  --key=<AWS ACCESS_KEY_KEY>  Your AWS account access key
  --region=<AWS REGION_NAME>  Your AWS account region [default: eu-west-1]
'''

import docopt
import ec2
import os
import json
import pprint
import sys

""" Outputs a list of all our machines
use --list
"""

def getList():
    instances = ec2.instances.filter(state='running')

    applications = {}
    for instance in instances:
        if (hasattr(instance, 'tags')):
            if ('application_name' in instance.tags):
                application_name = instance.tags['application_name']
                if not application_name in applications:
                    applications[application_name] = []
                applications[instance.tags['application_name']].append(instance.dns_name)

    print json.dumps(applications)
    sys.exit(0)


""" Outputs meta for a particular instance
"""


def hostInfo(dns_name):
    output = dns_name
    machine = ec2.instances.filter(state='running', public_dns_name=dns_name)
    if (not machine):
        print "cant find machine with dns of dns_name"
    else:
        instance = machine.pop()
        #pprint.pprint(instance.__dict__)
        output = {}
        output['id'] = instance.id
        output['dns_name'] = instance.dns_name
        output['ip_address'] = instance.ip_address
        output['private_dns_name'] = instance.private_dns_name
        output['image_id'] = instance.image_id
        output['kernel'] = instance.kernel
        output['tags']=instance.tags
        output['spot_instance_request_id'] = instance.spot_instance_request_id
        output['persistent'] = instance.persistent
        output['key_name'] = instance.key_name
        output['launch_time'] = instance.launch_time
    print json.dumps(output)
    sys.exit(0)


def main():
    '''Main entry point for the pd CLI.'''
    args = docopt.docopt(__doc__, help=True, version=None, options_first=False)

    #get AWS details from os environment if not passed in, if still not set then prompt user
    if (args['--id'] is None):
        aws_id = os.environ['AWS_ACCESS_KEY'] if os.environ.has_key('AWS_ACCESS_KEY') else None
    else:
        aws_id = args['--id']

    if (args['--key'] is None):
        aws_secret = os.environ['AWS_SECRET_KEY'] if os.environ.has_key('AWS_SECRET_KEY') else None
    else:
        aws_secret = args['--key']

    if (args['--region'] is None):
        aws_region = 'eu-west-1'
    else:
        aws_region = args['--region']

    #if key or secret is not found
    if (aws_id is None or aws_secret is None):
        print "You need to provide your AWS ID and Secret Key via --id and --key OR via your environment using AWS_ACCESS_KEY and AWS_SECRET_KEY"
        quit()
    else:
        # set the aws ec2 credentials
        ec2.credentials.ACCESS_KEY_ID = aws_id
        ec2.credentials.SECRET_ACCESS_KEY = aws_secret
        ec2.credentials.REGION_NAME = aws_region

    if (args['--list']):
        getList()
    elif (args['--host']):
        hostInfo(args['--host'])
    else:
        print "You must specify either --list or --host"


if __name__ == '__main__':
    main()

