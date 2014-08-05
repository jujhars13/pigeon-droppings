#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''pigeon droppings

Get the Running EC2 instances in your AWS beginning with <query>

Usage:
  pd [options] -q <query>
  pd (-h | --help)

Examples:
  pd -q api

Options:
  -q <query>                  search by instance name, eg web-server...
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
from clint.textui import colored
#import pprint

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

    # the api query
    query = args['-q']
    instances = ec2.instances.filter(state='running', name__icontains=query)

    print "Checking for '" + query + "' amongst your EC2 instances..."

    #foreach and print using (clint)colours
    if (len(instances)) > 0:
        print "Found " + str(len(instances)) + " running instances:"
        for instance in instances:
            print (getattr(colored, 'cyan')(instance.public_dns_name)) + "\t",
            print " " + (getattr(colored, 'magenta')(instance.tags['Name'] if instance.tags['Name'] else '*blank*')).ljust(40)
        if (args['-v']):
            print (getattr(colored, 'green')(instance.instance_type)),
            print (getattr(colored, 'blue')(instance.placement))
    else:
        print "Didn't find any running instances beginning with " + query

    # if __name__ == '__main__':
    #     main()

main()
