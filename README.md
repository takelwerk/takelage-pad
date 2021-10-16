[![license](https://img.shields.io/github/license/takelwerk/takelage-pad?color=blueviolet)](https://github.com/takelwerk/takelage-pad/blob/main/LICENSE)
[![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelpad/latest?label=hub.docker.com&sort=semver&color=blue)](https://hub.docker.com/r/takelwerk/takelpad)
[![deploy docker image](https://img.shields.io/github/workflow/status/takelwerk/takelage-pad/Build,%20test%20and%20deploy%20project?label=deploy%20docker%20image)](https://github.com/takelwerk/takelage-pad/actions/workflows/build_test_deploy_project_on_push.yml)
[![deploy vagrant vbox](https://img.shields.io/github/workflow/status/takelwerk/takelage-pad/Build%20and%20deploy%20project%20vbox%20to%20vagrantup?label=deploy%20vagrant%20vbox)](https://github.com/takelwerk/takelage-pad/actions/workflows/build_deploy_project_vbox_on_push.yml)
[![test project](https://img.shields.io/github/workflow/status/takelwerk/takelage-pad/Build%20and%20test%20project?label=test%20project)](https://github.com/takelwerk/takelage-pad/actions/workflows/build_test_project_nightly.yml)
[![test roles](https://img.shields.io/github/workflow/status/takelwerk/takelage-pad/Build%20and%20test%20roles?label=test%20roles)](https://github.com/takelwerk/takelage-pad/actions/workflows/build_test_roles_nightly.yml)

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

There is also a docker image
[takelwerk/takelpad](https://hub.docker.com/repository/docker/takelwerk/takelpad).

## Framework Versions

| App | Artifact |
| --- | -------- |
| *[takelage-doc](https://github.com/takelwerk/takelage-doc)* | [![License](https://img.shields.io/github/license/takelwerk/takelage-doc?color=blueviolet)](https://github.com/takelwerk/takelage-doc/blob/main/LICENSE) |
| *[takelage-dev](https://github.com/takelwerk/takelage-dev)* | [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelage/latest?label=hub.docker.com&sort=semver&color=blue)](https://hub.docker.com/r/takelwerk/takelage) |
| *[takelage-pad](https://github.com/takelwerk/takelage-pad)* | [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelpad/latest?label=hub.docker.com&sort=semver&color=blue)](https://hub.docker.com/r/takelwerk/takelpad) |
| *[takelage-cli](https://github.com/takelwerk/takelage-cli)* | [![rubygems.org](https://img.shields.io/gem/v/takeltau?label=rubygems.org&color=blue)](https://rubygems.org/gems/takeltau) |
| *[takelage-var](https://github.com/takelwerk/takelage-var)* | [![pypi,org](https://img.shields.io/pypi/v/pytest-takeltest?label=pypi.org&color=blue)](https://pypi.org/project/pytest-takeltest/) |
| *[takelage-img-takelslim](https://github.com/takelwerk/takelage-img-takelslim)* | [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelslim/latest?label=hub.docker.com&color=blue)](https://hub.docker.com/r/takelwerk/takelslim) | 
| *[takelage-img-takelbase](https://github.com/takelwerk/takelage-img-takelbase)* | [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelbase/latest?label=hub.docker.com&color=blue)](https://hub.docker.com/r/takelwerk/takelbase) | 
| *[takelage-img-takelruby](https://github.com/takelwerk/takelage-img-takelruby)* | [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelruby/latest?label=hub.docker.com&color=blue)](https://hub.docker.com/r/takelwerk/takelruby) | 
| *[takelage-vbox-takelbase](https://github.com/takelwerk/takelage-vbox-takelbase)* | [![vagrantup.com](https://img.shields.io/badge/vagrantup.com-debian--bullseye-blue)](https://app.vagrantup.com/takelwerk/boxes/takelbase) | 

## Framework Status

| App | Deploy project | Test project | Test roles | Deploy vbox |
| --- | -------------- | ------------ | ---------- | ----------- |
| *[takelage-dev](https://github.com/takelwerk/takelage-dev)* | [![deploy project](https://img.shields.io/github/workflow/status/takelwerk/takelage-dev/Build,%20test%20and%20deploy%20project?label=deploy%20project)](https://github.com/takelwerk/takelage-dev/actions/workflows/build_test_deploy_project_on_push.yml) | [![test project](https://img.shields.io/github/workflow/status/takelwerk/takelage-dev/Build%20and%20test%20project?label=test%20project)](https://github.com/takelwerk/takelage-dev/actions/workflows/build_test_project_nightly.yml) | [![test roles](https://img.shields.io/github/workflow/status/takelwerk/takelage-dev/Test%20roles?label=test%20roles)](https://github.com/takelwerk/takelage-dev/actions/workflows/build_test_roles_nightly.yml) |
| *[takelage-pad](https://github.com/takelwerk/takelage-pad)* | [![deploy project](https://img.shields.io/github/workflow/status/takelwerk/takelage-pad/Build,%20test%20and%20deploy%20project%20to%20dockerhub?label=deploy%20project)](https://github.com/takelwerk/takelage-pad/actions/workflows/build_test_deploy_project_on_push.yml) | [![test project](https://img.shields.io/github/workflow/status/takelwerk/takelage-pad/Build%20and%20test%20project?label=test%20project)](https://github.com/takelwerk/takelage-pad/actions/workflows/build_test_project_nightly.yml) | [![test roles](https://img.shields.io/github/workflow/status/takelwerk/takelage-pad/Build%20and%20test%20roles?label=test%20roles)](https://github.com/takelwerk/takelage-pad/actions/workflows/build_test_roles_nightly.yml) | [![deploy vbox](https://img.shields.io/github/workflow/status/takelwerk/takelage-pad/Build%20and%20deploy%20project%20vbox%20to%20vagrantup?label=deploy%20vbox)](https://github.com/takelwerk/takelage-pad/actions/workflows/build_deploy_project_vbox_on_push.yml) |
| *[takelage-cli](https://github.com/takelwerk/takelage-cli)* | [![deploy project](https://img.shields.io/github/workflow/status/takelwerk/takelage-cli/Build,%20test%20and%20deploy%20project?label=deploy%20project)](https://github.com/takelwerk/takelage-cli/actions/workflows/build_test_deploy_project_on_push.yml) | [![test project](https://img.shields.io/github/workflow/status/takelwerk/takelage-cli/Test%20project?label=test%20project)](https://github.com/takelwerk/takelage-cli/actions/workflows/test_project_nightly.yml) |
| *[takelage-var](https://github.com/takelwerk/takelage-var)* | [![deploy project](https://img.shields.io/github/workflow/status/takelwerk/takelage-var/Build,%20test%20and%20deploy%20project?label=deploy%20project)](https://github.com/takelwerk/takelage-var/actions/workflows/build_test_deploy_project_on_push.yml) | [![test project](https://img.shields.io/github/workflow/status/takelwerk/takelage-var/Build%20and%20test%20project?label=test%20project)](https://github.com/takelwerk/takelage-var/actions/workflows/build_test_project_nightly.yml) |
| *[takelage-img-takelslim](https://github.com/takelwerk/takelage-img-takelslim)* | [![deploy project](https://img.shields.io/github/workflow/status/takelwerk/takelage-img-takelslim/Build%20and%20deploy%20takelslim?label=deploy%20project)](https://github.com/takelwerk/takelage-img-takelslim/actions/workflows/build_deploy_takelslim_nightly.yml) |
| *[takelage-img-takelbase](https://github.com/takelwerk/takelage-img-takelbase)* | [![deploy project](https://img.shields.io/github/workflow/status/takelwerk/takelage-img-takelbase/Build%20and%20deploy%20takelbase?label=deploy%20project)](https://github.com/takelwerk/takelage-img-takelbase/actions/workflows/build_deploy_takelbase_nightly.yml) |
| *[takelage-img-takelruby](https://github.com/takelwerk/takelage-img-takelruby)* | [![deploy project](https://img.shields.io/github/workflow/status/takelwerk/takelage-img-takelruby/Build%20and%20deploy%20takelruby%20latest?label=deploy%20project)](https://github.com/takelwerk/takelage-img-takelruby/actions/workflows/build_deploy_takelruby_nightly.yml) |
| *[takelage-vbox-takelbase](https://github.com/takelwerk/takelage-vbox-takelbase)* | [![deploy project](https://img.shields.io/github/workflow/status/takelwerk/takelage-vbox-takelbase/Build%20and%20deploy%20project?label=deploy%20project)](https://github.com/takelwerk/takelage-vbox-takelbase/actions/workflows/build_and_deploy_project_nightly.yml) | | | [![deploy vbox](https://img.shields.io/github/workflow/status/takelwerk/takelage-vbox-takelbase/Build%20and%20deploy%20project?label=deploy%20vbox)](https://github.com/takelwerk/takelage-vbox-takelbase/actions/workflows/build_and_deploy_project_nightly.yml) |

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
[takelwerk/takelbase](https://github.com/takelwerk/takelage-vbox-takelbase)
 which is based on
 [Debian](https://www.debian.org/) bullseye.
 
*takel-pad* is made with 
[*takelage-dev*](https://github.com/takelwerk/takelage-dev).
It is the prototype for the vagrant/VirtualBox platform.
