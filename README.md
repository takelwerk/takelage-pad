# takelage-pad

*takelage-pad* is a 
[vagrant box](https://www.vagrantup.com/) 
called 
[takelwerk/takelpad](https://app.vagrantup.com/takelwerk/boxes/takelpad) 
which runs the 
[etherpad-lite](https://github.com/ether/etherpad-lite) 
collaborative editor with the
[virtual box](https://www.virtualbox.org/) 
provider.

The idea of any etherpad is to edit texts together online.
But online does not mean you have to have an uplink to the internet.
You can run this vagrant box on your computer locally.
Others can then connect to your machine locally.
You only need to be in the same local network which allows peer-to-peer 
connection.
This is the case for most default settings of consumer routers
and cell phone hotspots.
This box is for the data cautious who want to store their data
locally rather than in the cloud, i.e. on either people's computers.

## Prerequisites

The prerequisites are fairly low. You need to install 
[vagrant](https://www.vagrantup.com/downloads) from HashiCorp
and
[VirtualBox](https://www.virtualbox.org/wiki/Downloads) from Oracle
in a recent version (vagrant in the Debian buster repos won't work!)

## Getting started

The box is controlled by a Vagrantfile. This is how you get one:

````bash
vagrant init takelwerk/takelpad
````

Now you can start the box 
(and maybe you want to watch the VirtualBox GUI while doing so):

```bash
vagrant up
```

vagrant will tell you the IP address of the etherpad 

Afterwards you can stop the box:

```bash
vagrant halt
```

Or you can destroy it:

```bash
vagrant destroy
```

## Troubleshooting

The IP address of a running takelpad can be printed like so:

```bash
vagrant provision
``` 

The script 
[```takelpad```](https://github.com/takelwerk/takelage-pad/blob/master/ansible/roles/takel-etherpad/templates/takelpad.j2.sh)
in the box which is called by 
```vagrant provision``` prints the IP of the last network interface.

This is how you can see all IP addresses of the box:
```bash
vagrant ssh -c 'ip a'
``` 

As *takelage-pad* is a vagrant box you can easily log in to it
to do further Debugging in the 
[Debian](https://www.debian.org/) buster environment:

```bash
vagrant ssh
```

## Technical context

*takel-pad* is made with 
[*takelage-dev*](https://github.com/geospin-takelage/takelage-dev).
It is the prototype for the vagrant/virtual box platform.
*takel-pad* is based on
[takelwerk/takelbase](https://app.vagrantup.com/takelwerk/boxes/takelbase)  
 