# takelage-pad

*takelage-pad* is a docker image
called 
[takelwerk/takelpad](https://hub.docker.com/r/takelwerk/takelpad) 
which runs the 
[etherpad-lite](https://github.com/ether/etherpad-lite) 
collaborative editor.

The idea of any etherpad is to edit texts together online.
But online does not mean you have to have an uplink to the internet.

You can use a simple `docker-compose.yml` file to run this pad locally:

```yaml
version: "3.8"

services:
  
  pad:
    image: takelwerk/takelpad:latest
    container_name: takelpad
    hostname: takelpad
    privileged: true
    ports:
      - "80:80"
      - "443:443"
```

Others can then connect to your machine locally if your firewall permits it or if you run it in a bridged virtual machine.
You only need to be in the same local network which allows peer-to-peer
connections.
This is the case for most default settings of consumer routers
and cell phone hotspots.

This box is for the data cautious who want to store their data
locally rather than in the cloud, i.e. on other people's computers.

## Framework Versions

| Project | Artifacts |
|-|-|
| [![takelage-doc](https://img.shields.io/badge/github-takelage--doc-purple)](https://github.com/takelwerk/takelage-doc) | [![License](https://img.shields.io/badge/license-GNU_GPLv3-blue)](https://github.com/takelwerk/takelage-doc/blob/main/LICENSE) |
| [![takelage-var](https://img.shields.io/badge/github-takelage--var-purple)](https://github.com/takelwerk/takelage-var) | [![pypi,org](https://img.shields.io/pypi/v/pytest-takeltest?label=pypi.org&color=blue)](https://pypi.org/project/pytest-takeltest/) |
| [![takelage-cli](https://img.shields.io/badge/github-takelage--cli-purple)](https://github.com/takelwerk/takelage-cli) | [![rubygems.org](https://img.shields.io/gem/v/takeltau?label=rubygems.org&color=blue)](https://rubygems.org/gems/takeltau) |
| [![takelage-img-takelslim](https://img.shields.io/badge/github-takelage--img--takelslim-purple)](https://github.com/takelwerk/takelage-img-takelslim) | [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelslim/latest-amd64?label=hub.docker.com&arch=amd64&color=teal)](https://hub.docker.com/r/takelwerk/takelslim) [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelslim/latest-arm64?label=hub.docker.com&arch=arm64&color=slateblue)](https://hub.docker.com/r/takelwerk/takelslim) | 
| [![takelage-img-takelbase](https://img.shields.io/badge/github-takelage--img--takelbase-purple)](https://github.com/takelwerk/takelage-img-takelbase) | [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelbase/latest-amd64?label=hub.docker.com&arch=amd64&color=teal)](https://hub.docker.com/r/takelwerk/takelbase) [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelbase/latest-arm64?label=hub.docker.com&arch=arm64&color=slateblue)](https://hub.docker.com/r/takelwerk/takelbase) |
| [![takelage-img-takelpodslim](https://img.shields.io/badge/github-takelage--img--takelpodslim-purple)](https://github.com/takelwerk/takelage-img-takelpodslim) | [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelpodslim/latest-amd64?label=hub.docker.com&arch=amd64&color=teal)](https://hub.docker.com/r/takelwerk/takelpodslim) [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelpodslim/latest-arm64?label=hub.docker.com&arch=arm64&color=slateblue)](https://hub.docker.com/r/takelwerk/takelpodslim) | 
| [![takelage-img-takelpodbase](https://img.shields.io/badge/github-takelage--img--takelpodbase-purple)](https://github.com/takelwerk/takelage-img-takelpodbase) | [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelpodbase/latest-amd64?label=hub.docker.com&arch=amd64&color=teal)](https://hub.docker.com/r/takelwerk/takelpodbase) [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelpodbase/latest-arm64?label=hub.docker.com&arch=arm64&color=slateblue)](https://hub.docker.com/r/takelwerk/takelpodbase) | 
| [![takelage-dev](https://img.shields.io/badge/github-takelage--dev-purple)](https://github.com/takelwerk/takelage-dev) | [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelage/latest-amd64?label=hub.docker.com&arch=amd64&sort=semver&color=teal)](https://hub.docker.com/r/takelwerk/takelage) [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelage/latest-arm64?label=hub.docker.com&arch=arm64&sort=semver&color=slateblue)](https://hub.docker.com/r/takelwerk/takelage) |
| [![takelage-pad](https://img.shields.io/badge/github-takelage--pad-purple)](https://github.com/takelwerk/takelage-pad) | [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelpad/latest-amd64?label=hub.docker.com&arch=amd64&sort=semver&color=teal)](https://hub.docker.com/r/takelwerk/takelpad) [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelpad/latest-arm64?label=hub.docker.com&arch=arm64&sort=semver&color=slateblue)](https://hub.docker.com/r/takelwerk/takelpad) |
| [![takelship](https://img.shields.io/badge/github-takelship-purple)](https://github.com/takelwerk/takelship) | [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelship/latest-amd64?label=hub.docker.com&arch=amd64&sort=semver&color=teal)](https://hub.docker.com/r/takelwerk/takelship) [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelship/latest-arm64?label=hub.docker.com&arch=arm64&sort=semver&color=slateblue)](https://hub.docker.com/r/takelwerk/takelship) | |


## Framework Status

| Project | Pipelines |
|-|-|
| [![takelage-var](https://img.shields.io/badge/github-takelage--var-purple)](https://github.com/takelwerk/takelage-var) | [![takeltest](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-var/takeltest.yml?label=takeltest)](https://github.com/takelwerk/takelage-var/actions/workflows/takeltest.yml) [![test_takeltest](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-var/test_takeltest.yml?label=test%20takeltest)](https://github.com/takelwerk/takelage-var/actions/workflows/test_takeltest.yml) |
| [![takelage-cli](https://img.shields.io/badge/github-takelage--cli-purple)](https://github.com/takelwerk/takelage-cli) | [![takeltau](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-cli/takeltau.yml?label=takeltau)](https://github.com/takelwerk/takelage-cli/actions/workflows/takeltau.yml) [![test_takeltau](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-cli/test_takeltau.yml?label=test%20takeltau)](https://github.com/takelwerk/takelage-cli/actions/workflows/test_takeltau.yml) |
| [![takelage-img-takelslim](https://img.shields.io/badge/github-takelage--img--takelslim-purple)](https://github.com/takelwerk/takelage-img-takelslim) | [![takelslim amd64](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-img-takelslim/takelslim_amd64.yml?label=takelslim%20amd64)](https://github.com/takelwerk/takelage-img-takelslim/actions/workflows/takelslim_amd64.yml) |
| [![takelage-img-takelbase](https://img.shields.io/badge/github-takelage--img--takelbase-purple)](https://github.com/takelwerk/takelage-img-takelbase) | [![takelbase amd64](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-img-takelbase/takelbase_amd64.yml?label=takelbase%20amd64)](https://github.com/takelwerk/takelage-img-takelbase/actions/workflows/takelbase_amd64.yml) | 
| [![takelage-img-takelpodslim](https://img.shields.io/badge/github-takelage--img--takelpodslim-purple)](https://github.com/takelwerk/takelage-img-takelpodslim) | [![takelpodslim amd64](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-img-takelpodslim/takelpodslim_amd64.yml?label=takelpodslim%20amd64)](https://github.com/takelwerk/takelage-img-takelpodslim/actions/workflows/takelpodslim_amd64.yml) |
| [![takelage-img-takelpodbase](https://img.shields.io/badge/github-takelage--img--takelpodbase-purple)](https://github.com/takelwerk/takelage-img-takelpodbase) | [![takelpodbase amd64](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-img-takelpodbase/takelpodbase_amd64.yml?label=takelpodbase%20amd64)](https://github.com/takelwerk/takelage-img-takelpodbase/actions/workflows/takelpodbase_amd64.yml) | 
| [![takelage-dev](https://img.shields.io/badge/github-takelage--dev-purple)](https://github.com/takelwerk/takelage-dev) | [![takelage amd64](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-dev/takelage_amd64.yml?label=takelage%20amd64)](https://github.com/takelwerk/takelage-dev/actions/workflows/takelage_amd64.yml) [![test_takelage](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-dev/test_takelage.yml?label=test%20takelage)](https://github.com/takelwerk/takelage-dev/actions/workflows/test_takelage.yml) 
| | [![takelbuild amd64](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-dev/takelbuild_amd64.yml?label=takelbuild%20amd64)](https://github.com/takelwerk/takelage-dev/actions/workflows/takelbuild_amd64.yml) [![test_takelbuild](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-dev/test_takelbuild.yml?label=test%20takelbuild)](https://github.com/takelwerk/takelage-dev/actions/workflows/test_takelbuild.yml) |
| | [![takelbeta amd64](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-dev/takelbeta_amd64.yml?label=takelbeta%20amd64)](https://github.com/takelwerk/takelage-dev/actions/workflows/takelbeta_amd64.yml) [![test_roles](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-dev/test_roles.yml?label=test%20roles)](https://github.com/takelwerk/takelage-dev/actions/workflows/test_roles.yml) |
| [![takelage-pad](https://img.shields.io/badge/github-takelage--pad-purple)](https://github.com/takelwerk/takelage-pad) | [![takelpad docker](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-pad/takelpad_docker.yml?label=takelpad%20docker)](https://github.com/takelwerk/takelage-pad/actions/workflows/takelpad_docker.yml) |
| | [![test takelpad](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-pad/test_takelpad.yml?label=test%20takelpad)](https://github.com/takelwerk/takelage-pad/actions/workflows/test_takelpad.yml) [![test roles](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-pad/test_roles.yml?label=test%20roles)](https://github.com/takelwerk/takelage-pad/actions/workflows/test_roles.yml) |
| [![takelship](https://img.shields.io/badge/github-takelship-purple)](https://github.com/takelwerk/takelship) | [![takelship docker](https://img.shields.io/github/actions/workflow/status/takelwerk/takelship/takelship-amd64.yml?label=takelship%20docker)](https://github.com/takelwerk/takelship/actions/workflows/takelship-amd64.yml) |

## Technical context

*takel-pad* is based on
[takelwerk/takelbase](https://github.com/takelwerk/takelage-img-takelbase)
 which is based on
 [Debian](https:/www.debian.org/).
 
*takel-pad* is made with 
[*takelage-dev*](https://github.com/takelwerk/takelage-dev).
