Pigeon Droppings
======================================

![](https://github.com/jujhars13/pigeon-droppings/blob/master/pigeon.jpg?raw=true)

Utility that gets the DNS names of your Amazon Web services EC2 instances based on the name you supply.

Often found myself having to go through the rigmarole of the using the EC2 webconsole to find the DNS name of servers to administer them.  Now I don't have to leave my beloved [console](http://gnometerminator.blogspot.co.uk/p/introduction.html).
**aws-describe-instances** from the [AWS command line tools](http://aws.amazon.com/cli/) does the same, but the syntax is difficult and the output is very messy and inconsistent which makes it's hard to find what you want (even with bash-fu).  This util just gives you your DNS name and the instance name.

Usage
-----
`pd.exe -q api.mycoolapp.com`

Requirements
------------
You'll need your AWS IAM credentials (key and secret).
Set them in your environment using the standard AWS command line tools environment variables (AWS_SECRET_KEY and AWS_SECRET_KEY) or pass them in using params
Originally built for Windows 8, works on OS X and DEB Linux.
- Python >= 2.7

TODO
----
- TODO build script
- TODO better testing

## Ansible
Just added an [Ansible](http://www.ansible.com/home) output compatible format version `pd-ansible.py`

`pd-ansible` --host <hostname>` will output something like below.  You can use these as vars in your Ansible playbooks

```javascript
    {
      "kernel": "aki-52a34525",
      "private_dns_name": "ip-11-41-123-119.eu-west-1.compute.internal",
      "tags": {
        "application_name": "futo-ppi"
      },
      "dns_name": "ec2-11-41-123-119.eu-west-1.compute.amazonaws.com",
      "launch_time": "2014-03-02T11:25:10.000Z",
      "persistent": false,
      "image_id": "ami-2226b825",
      "key_name": "Futon",
      "spot_instance_request_id": null,
      "ip_address": "11.31.29.523",
      "id": "i-abf7c7fd"
    }
```

## Deps
[https://github.com/mattrobenolt/ec2](https://github.com/mattrobenolt/ec2) nice sugar on top of [boto](https://github.com/boto/boto)

[https://github.com/docopt/docopt](https://github.com/docopt/docopt)

[https://github.com/kennethreitz/clint](https://github.com/kennethreitz/clint)

License
-------
MIT licensed.

Why Pigeon Droppings?
--------------------
My [CTO](http://uk.linkedin.com/in/doylie) suggested it as a name for a software project, so I took him up on it.

It's known as "Kabooter Tatee" ਕਬੂਤਰ ਤਤੀ in the [Punjabi](http://en.wikipedia.org/wiki/Punjabi_language) language, which just tickles me silly.