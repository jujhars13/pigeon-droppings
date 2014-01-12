Pigeon Droppings
======================================
Utility that gets the DNS names of your Amazon Web services EC2 instances based on the name you supply.

Often found myself having to go through the rigmarole of the using the EC2 webconsole to find the DNS name of servers to administer them.  Now I don't have to leave my beloved console.
**aws-describe-instances** from the [AWS command line tools](http://aws.amazon.com/cli/) does the same, but the syntax is difficult and the output is very messy and inconsistent which makes it's hard to find what you want (even with bash-fu).  This util just gives you your DNS name and the instance name.

Usage
-----
`pg.exe -q api.mycoolapp.com`

Requirements
------------
You'll need your AWS IAM credentials (key and secret).
Set them in your environment using the standard AWS command line tools environment variables (AWS_SECRET_KEY and AWS_SECRET_KEY) or pass them in using params
Currently built for Windows 8, will setup a build process for MacOS and RPM Linux.
- Python >= 2.7

TODO
----
- TODO build with py2exe
- TODO build script
- TODO build on macos
- TODO build on linux
- TODO add github screenshot

License
-------
MIT licensed.

Why Pigeon Droppings?
--------------------
My [CTO](http://uk.linkedin.com/in/doylie) suggested it as a name for a software project, so I took him up on it.
