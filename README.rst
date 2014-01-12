Pigeon Droppings
======================================
Utility that gets the DNS names of your aws instances based on the name you supply.
Often found myself having to go through the rigmarole of the using the EC2 webconsole to find the DNS name of servers to administer them.  Now I don't have to leave my CLI.

**aws-describe-instances** from the AWS command line tools does the same, but the syntax is difficult and the output is very messy and it's hard to find what you want.  This util just gives you your DNS name and the instance name.

## Usage
`pg -q api.mycoolapp.com`


Requirements
------------
You'll need your AWS IAM credentials (KEY and SECRET).
Set them in your environment using the standard AWS command line tools environment variables (AWS_SECRET_KEY and AWS_SECRET_KEY) or pass them in using params
Currently built for Windows 8, will setup a build process for MacOS and RPM Linux.
- Python >= 2.7

License
-------

MIT licensed. See the bundled `LICENSE <https://github.com/jujhars13/sabd/blob/master/LICENSE>`_ file for more details.

### Why Pigeon Droppings
My [CTO](http://uk.linkedin.com/in/doylie) suggested it as a name for a software project, so I took him up on it.
