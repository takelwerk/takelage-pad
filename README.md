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

There exists a docker image
[takelwerk/takelpad](https://hub.docker.com/repository/docker/takelwerk/takelpad)
and a parallels vm, too.

## Framework Versions

| Project                                                                                                                                                             | Artifacts                                                                                                                                                                                                                                                                                                                                                                 |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [![takelage-doc](https://img.shields.io/badge/github-takelage--doc-purple)](https://github.com/takelwerk/takelage-doc)                                            | [![License](https://img.shields.io/badge/license-GNU_GPLv3-blue)](https://github.com/takelwerk/takelage-doc/blob/main/LICENSE)                                                                                                                                                                                                                                            |
| [![takelage-img-takelslim](https://img.shields.io/badge/github-takelage--img--takelslim-purple)](https://github.com/takelwerk/takelage-img-takelslim)             | [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelslim/latest?label=hub.docker.com&arch=amd64&color=teal)](https://hub.docker.com/r/takelwerk/takelslim) [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelslim/latest?label=hub.docker.com&arch=arm64&color=slateblue)](https://hub.docker.com/r/takelwerk/takelslim)                  | 
| [![takelage-img-takelbase](https://img.shields.io/badge/github-takelage--img--takelbase-purple)](https://github.com/takelwerk/takelage-img-takelbase)             | [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelbase/latest?label=hub.docker.com&arch=amd64&color=teal)](https://hub.docker.com/r/takelwerk/takelbase) [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelbase/latest?label=hub.docker.com&arch=arm64&color=slateblue)](https://hub.docker.com/r/takelwerk/takelbase)                    | 
| [![takelage-img-takelruby](https://img.shields.io/badge/github-takelage--img--takelruby-purple)](https://github.com/takelwerk/takelage-img-takelruby)             | [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelruby/latest?label=hub.docker.com&arch=amd64&color=teal)](https://hub.docker.com/r/takelwerk/takelruby) [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelruby/latest?label=hub.docker.com&arch=arm64&color=slateblue)](https://hub.docker.com/r/takelwerk/takelruby)                    | 
| [![takelage-vagrant-takelbase](https://img.shields.io/badge/github-takelage--vagrant--takelbase-purple)](https://github.com/takelwerk/takelage-vagrant-takelbase) | [![vagrantup.com](https://img.shields.io/badge/vagrantup.com-debian--bullseye-blue)](https://app.vagrantup.com/takelwerk/boxes/takelbase)                                                                                                                                                                                                                                 | 
| [![takelage-var](https://img.shields.io/badge/github-takelage--var-purple)](https://github.com/takelwerk/takelage-var)                                            | [![pypi,org](https://img.shields.io/pypi/v/pytest-takeltest?label=pypi.org&color=blue)](https://pypi.org/project/pytest-takeltest/)                                                                                                                                                                                                                                       |
| [![takelage-cli](https://img.shields.io/badge/github-takelage--cli-purple)](https://github.com/takelwerk/takelage-cli)                                            | [![rubygems.org](https://img.shields.io/gem/v/takeltau?label=rubygems.org&color=blue)](https://rubygems.org/gems/takeltau)                                                                                                                                                                                                                                                |
| [![takelage-dev](https://img.shields.io/badge/github-takelage--dev-purple)](https://github.com/takelwerk/takelage-dev)                                            | [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelage/latest?label=hub.docker.com&arch=amd64&sort=semver&color=teal)](https://hub.docker.com/r/takelwerk/takelage) [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelage/latest?label=hub.docker.com&arch=arm64&sort=semver&color=slateblue)](https://hub.docker.com/r/takelwerk/takelage) |
| [![takelage-pad](https://img.shields.io/badge/github-takelage--pad-purple)](https://github.com/takelwerk/takelage-pad)                                            | [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelpad/latest?label=hub.docker.com&sort=semver&color=blue)](https://hub.docker.com/r/takelwerk/takelpad)                                                                                                                                                                                                   |

## Framework Status

| Project                                                                                                                                                 | Pipelines                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [![takelage-img-takelslim](https://img.shields.io/badge/github-takelage--img--takelslim-purple)](https://github.com/takelwerk/takelage-img-takelslim) | [![takelslim amd64](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-img-takelslim/takelslim_amd64.yml?label=takelslim%20amd64)](https://github.com/takelwerk/takelage-img-takelslim/actions/workflows/takelslim_amd64.yml) [![takelslim arm64](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-img-takelslim/takelslim_arm64.yml?label=takelslim%20arm64)](https://github.com/takelwerk/takelage-img-takelslim/actions/workflows/takelslim_arm64.yml) |
| [![takelage-img-takelbase](https://img.shields.io/badge/github-takelage--img--takelbase-purple)](https://github.com/takelwerk/takelage-img-takelbase) | [![takelbase amd64](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-img-takelbase/takelbase_amd64.yml?label=takelbase%20amd64)](https://github.com/takelwerk/takelage-img-takelbase/actions/workflows/takelbase_amd64.yml) [![takelbase arm64](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-img-takelbase/takelbase_arm64.yml?label=takelbase%20arm64)](https://github.com/takelwerk/takelage-img-takelbase/actions/workflows/takelbase_arm64.yml) |
| [![takelage-img-takelruby](https://img.shields.io/badge/github-takelage--img--takelruby-purple)](https://github.com/takelwerk/takelage-img-takelruby) | [![takelruby amd64](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-img-takelruby/takelruby_amd64.yml?label=takelruby%20amd64)](https://github.com/takelwerk/takelage-img-takelruby/actions/workflows/takelruby_amd64.yml)                                                                                                                                                                                                                                                  |
| [![takelage-vagrant-takelbase](https://img.shields.io/badge/github-takelage--vagrant--takelbase-purple)](https://github.com/takelwerk/takelage-vagrant-takelbase) | [![takelbase vagrant virtualbox](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-vagrant-takelbase/takelbase-vagrant-virtualbox.yml?label=takelbase%20vagrant%20virtualbox)](https://github.com/takelwerk/takelage-vagrant-takelbase/actions/workflows/takelbase-vagrant-virtualbox.yml)                                                                                                                                                                                    |
| [![takelage-var](https://img.shields.io/badge/github-takelage--var-purple)](https://github.com/takelwerk/takelage-var) | [![takeltest](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-var/takeltest.yml?label=takeltest)](https://github.com/takelwerk/takelage-var/actions/workflows/takeltest.yml) [![test_takeltest](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-var/test_takeltest.yml?label=test%20takeltest)](https://github.com/takelwerk/takelage-var/actions/workflows/test_takeltest.yml)                                                                    |
| [![takelage-cli](https://img.shields.io/badge/github-takelage--cli-purple)](https://github.com/takelwerk/takelage-cli) | [![takeltau](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-cli/takeltau.yml?label=takeltau)](https://github.com/takelwerk/takelage-cli/actions/workflows/takeltau.yml) [![test_takeltau](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-cli/test_takeltau.yml?label=test%20takeltau)](https://github.com/takelwerk/takelage-cli/actions/workflows/test_takeltau.yml)                                                                            |
| [![takelage-dev](https://img.shields.io/badge/github-takelage--dev-purple)](https://github.com/takelwerk/takelage-dev) | [![takelage amd64](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-dev/takelage_amd64.yml?label=takelage%20amd64)](https://github.com/takelwerk/takelage-dev/actions/workflows/takelage_amd64.yml) [![test_takelage](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-dev/test_takelage.yml?label=test%20takelage)](https://github.com/takelwerk/takelage-dev/actions/workflows/test_takelage.yml)                                                  
| | [![takelbuild amd64](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-dev/takelbuild_amd64.yml?label=takelbuild%20amd64)](https://github.com/takelwerk/takelage-dev/actions/workflows/takelbuild_amd64.yml) [![test_takelbuild](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-dev/test_takelbuild.yml?label=test%20takelbuild)](https://github.com/takelwerk/takelage-dev/actions/workflows/test_takelbuild.yml) |
| | [![takelbeta amd64](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-dev/takelbeta_amd64.yml?label=takelbeta%20amd64)](https://github.com/takelwerk/takelage-dev/actions/workflows/takelbeta_amd64.yml) [![test_roles](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-dev/test_roles.yml?label=test%20roles)](https://github.com/takelwerk/takelage-dev/actions/workflows/test_roles.yml) |
| [![takelage-pad](https://img.shields.io/badge/github-takelage--pad-purple)](https://github.com/takelwerk/takelage-pad) | [![takelpad docker](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-pad/takelpad_docker.yml?label=takelpad%20docker)](https://github.com/takelwerk/takelage-pad/actions/workflows/takelpad_docker.yml) [![takelpad virtualbox](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-pad/takelpad_virtualbox.yml?label=takelpad%20virtualbox)](https://github.com/takelwerk/takelage-pad/actions/workflows/takelpad_virtualbox.yml)                      |
| | [![test takelpad](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-pad/test_takelpad.yml?label=test%20takelpad)](https://github.com/takelwerk/takelage-pad/actions/workflows/test_takelpad.yml) [![test roles](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-pad/test_roles.yml?label=test%20roles)](https://github.com/takelwerk/takelage-pad/actions/workflows/test_roles.yml) |

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

## Update

From time to time you should update the box:
```bash
vagrant box update --box=takelwerk/takelpad
```

Keep in mind that you have to destroy your old box and create a new one 
for the update to take effect:
```bash
vagrant destroy
vagrant up
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
 [Debian](https:/www.debian.org/) bullseye.
 
*takel-pad* is made with 
[*takelage-dev*](https://github.com/takelwerk/takelage-dev).
It is the prototype for the vagrant/VirtualBox platform.
