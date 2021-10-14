[![license](https://img.shields.io/github/license/takelwerk/takelage-padv?color=blueviolet)](https://github.com/takelwerk/takelage-pad/blob/main/LICENSE)
[![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelpad/latest?label=hub.docker.com&sort=semver&color=blue)](https://hub.docker.com/r/takelwerk/takelpad)
[![deploy project](https://img.shields.io/github/workflow/status/takelwerk/takelage-pad/Build,%20test%20and%20deploy%20project?label=deploy%20project)](https://github.com/takelwerk/takelage-dev/actions/workflows/build_test_deploy_project_on_push.yml)
[![deploy takelbeta](https://img.shields.io/github/workflow/status/takelwerk/takelage-dev/Build,%20test%20and%20deploy%20takelbeta?label=deploy%20takelbeta)](https://github.com/takelwerk/takelage-dev/actions/workflows/build_test_deploy_takelbeta_on_push.yml)
[![deploy takelbuild](https://img.shields.io/github/workflow/status/takelwerk/takelage-dev/Build,%20test%20and%20deploy%20takelbuild?label=deploy%20takelbuild)](https://github.com/takelwerk/takelage-dev/actions/workflows/build_test_deploy_takelbuild_on_push.yml)
[![test project](https://img.shields.io/github/workflow/status/takelwerk/takelage-dev/Build%20and%20test%20project?label=test%20project)](https://github.com/takelwerk/takelage-dev/actions/workflows/build_test_project_nightly.yml)
[![test roles](https://img.shields.io/github/workflow/status/takelwerk/takelage-dev/Test%20roles?label=test%20roles)](https://github.com/takelwerk/takelage-dev/actions/workflows/build_test_roles_nightly.yml)

# takelage-pad

*takelage-pad* is a 
[vagrant box](https://www.vagrantup.com/) 
called 
[takelwerk/takelpad](https://app.vagrantup.com/takelwerk/boxes/takelpad) 
which runs the 
[etherpad-lite](https://github.com/ether/etherpad-lite) 
collaborative editor using the
[virtual box](https://www.virtualbox.org/) 
provider.

The idea of any etherpad is to edit texts together online.
But online does not mean you have to have an uplink to the internet.
You can run this vagrant box on your computer locally.
Others can then connect to your machine locally.
You only need to be in the same local network which allows peer-to-peer 
connections.
This is the case for most default settings of consumer routers
and cell phone hotspots.
This box is for the data cautious who want to store their data
locally rather than in the cloud, i.e. on other people's computers.

## Prerequisites

The prerequisites are fairly low. You need to install 
[vagrant](https://www.vagrantup.com/downloads) from HashiCorp
and
[VirtualBox](https://www.virtualbox.org/wiki/Downloads) from Oracle
in a recent version.

## Getting started

The box is controlled by a Vagrantfile. This is how you get one:

````bash
vagrant init takelwerk/takelpad
````

Now you can start the box 
(and maybe you want to watch the VirtualBox GUI 
while doing so for the first time):

```bash
vagrant up
```

After each start, vagrant will tell you the IP address of the etherpad.
You can then use a browser to connect to the etherpad via this IP address.

When you are finished you can stop the box:

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

As *takelage-pad* is a vagrant box you can easily ssh in to it:

```bash
vagrant ssh
```

This is how you become root:

```bash
vagrant ssh -c 'sudo su -'
```

The script 
[```takelpad```](https://github.com/takelwerk/takelage-pad/blob/master/ansible/roles/takel-etherpad/templates/takelpad.j2.sh)
in the box which is invoked by 
```vagrant provision``` with the parameter ```--summary```
prints the IP of the last network interface.

This is how you can get more information:
```bash
vagrant ssh -c takelpad
``` 

## Technical context

*takel-pad* is based on
[takelwerk/takelbase](https://app.vagrantup.com/takelwerk/boxes/takelbase)
 which is based on
 [Debian](https://www.debian.org/) bullseye.
 
*takel-pad* is made with 
[*takelage-dev*](https://github.com/takelwerk/takelage-dev).
It is the prototype for the vagrant/VirtualBox platform.
