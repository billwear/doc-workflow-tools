||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/supported-versions-snap-2-7-cli/4347) ~ [UI](/t/supported-versions-snap-2-7-ui/4346)|[CLI](/t/supported-versions-snap-2-8-cli/4349) ~ [UI](/t/supported-versions-snap-2-8-ui/4348)|[CLI](/t/supported-versions-snap-2-9-cli/4351) ~ [UI](/t/supported-versions-snap-2-9-ui/4350)|[CLI](/t/supported-versions-snap-3-0-cli/4113) ~ [UI](/t/supported-versions-snap-3-0-ui/4114)|
Packages|[CLI](/t/supported-versions-deb-2-7-cli/4353) ~ [UI](/t/supported-versions-deb-2-7-ui/4352)|[CLI](/t/supported-versions-deb-2-8-cli/4355) ~ [UI](/t/supported-versions-deb-2-8-ui/4354)|[CLI](/t/supported-versions-deb-2-9-cli/4357) ~ [UI](/t/supported-versions-deb-2-9-ui/4356)|[CLI](/t/supported-versions-deb-3-0-cli/4115) ~ [UI](/t/supported-versions-deb-3-0-ui/4116)|
This document explains what versions of MAAS are supported, and how they are supported.

## Support matrix

The following table summarises the support provided for various MAAS versions.  Explanations of the terms used in the table are provided below.

| Version | Support Level | Professional Support | On Ubuntu base |
|:-------:|:-------------:|:--------------------:|:----------------:|
| 2.9     | COMMUNITY     |  Available           | Ubuntu 20.04 LTS |
| 2.8     | COMMUNITY     |  Available           | Ubuntu 18.04 LTS |
| 2.7     | SUSTAINING    |  Available           | Ubuntu 18.04 LTS |
| 2.6     | SUSTAINING    |  Available           | Ubuntu 18.04 LTS |
| 2.5     | SUSTAINING    |  Available           | Ubuntu 18.04 LTS |
| < 2.5   | SUSTAINING    |  Not available       | Ubuntu 16.04 LTS |

### Support levels

The following support levels are defined for MAAS.  They cover MAAS major versions as indicated in the table above:

 - SUSTAINING = Fixes, back-ports, and security fixes, via Professional Support only from the Sustaining Engineering Group.

 - COMMUNITY = Community support, via discourse, with no guaranteed timeline. MAAS core team will review requests and accept bugs for versions that fall into this category, with the understanding that they're handled on a best-effort basis. Essentially this is the support available for those who do not engage professional support.  This level also covers anything covered by the SECURITY and FAILURE levels.

Note that Professional Support is more widely available, and can be customised with respect to versions and length of support contract, on a case-by-case basis within limits.  Discuss these needs with your sales representative. 


### Support coverage

1. MAAS releases are community-supported by the MAAS core team for a period of one year following the offical release of the major version.  Support for point releases ends when the corresponding major version goes out of support.

2. The majority of bug fixes and support issues are fixed with point releases of the covered major version.

3. Not all versions of MAAS are supported on all Ubuntu releases, depending upon how the version is delivered.

4. Snap versions should function on any Ubuntu version that supports snap.  Support on non-Ubuntu is not guaranteed for any release.

5. Each Debian package is supported on a specific version(s) of the Ubuntu OS.  For example, currently, the MAAS 2.9 Debian package is only supported on Ubuntu 20.04 LTS (Focal), while MAAS 2.8 is only supported on Ubuntu 18.04 LTS (Bionic).

			
## Upgrade guide

The following table links to upgrade instructions, indexed by the target release, e.g., the "2.8" row gives instructions on how to upgrade from 2.7 to 2.8.

| Target release | Installed  release | Snap upgrade | Package upgrade |
|:--------------:|:------------------:|:-------------|:----------------|
| 2.9 | 2.8 | [Snap 2.8 to Snap 2.9](https://maas.io/docs/snap/2.9/ui/installation#heading--upgrade-maas-snap) | [Deb 2.8 to Deb 2.9](https://maas.io/docs/deb/2.9/ui/installation#heading--upgrade-via-packages) |
| 2.8 | 2.7 | [Snap 2.7 to Snap 2.8](https://maas.io/docs/snap/2.8/cli/installation#heading--upgrade-maas-snap)| [Deb 2.7 to Deb 2.8](https://maas.io/docs/deb/2.9/ui/installation#heading--upgrade-via-packages)|
| 2.7 | 2.6 | [Snap 2.6 to Snap 2.7](https://maas.io/docs/2.7/release-notes#heading--upgrade-2-6-to-2-7-snap) | [Deb 2.6 to Deb 2.7](#heading--deb-2-6-to-deb-2-7) |
| 2.6 | 2.5 | N/A | [Deb 2.5 to Deb 2.6](#heading--deb-2-5-to-deb-2-6) |

<h3 id="heading--deb-2-6-to-deb-2-7">Upgrading packages from MAAS 2.6 to MAAS 2.7</h3>

MAAS 2.6 and MAAS 2.7 both run on Ubuntu 18.04 LTS (Bionic), so the upgrade is trivial:

```
sudo add-apt-repository -u ppa:maas/2.7
sudo apt upgrade maas
```

<h3 id="heading--deb-2-5-to-deb-2-6">Upgrading packages from MAAS 2.5 to MAAS 2.6</h3>

MAAS 2.5 and MAAS 2.6 both run on Ubuntu 18.04 LTS (Bionic), so the upgrade should be trivial:

```
sudo add-apt-repository -u ppa:maas/2.6
sudo apt upgrade maas
```
