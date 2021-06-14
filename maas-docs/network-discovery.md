||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/network-discovery-snap-2-7-cli/2922) ~ [UI](/t/network-discovery-snap-2-7-ui/2923)|[CLI](/t/network-discovery-snap-2-8-cli/2924) ~ [UI](/t/network-discovery-snap-2-8-ui/2925)|[CLI](/t/network-discovery-snap-2-9-cli/2926) ~ [UI](/t/network-discovery-snap-2-9-ui/2927)|[CLI](/t/network-discovery-snap-3-0-cli/4041) ~ [UI](/t/network-discovery-snap-3-0-ui/4042)|
Packages|[CLI](/t/network-discovery-deb-2-7-cli/2928) ~ [UI](/t/network-discovery-deb-2-7-ui/2929)|[CLI](/t/network-discovery-deb-2-8-cli/2930) ~ [UI](/t/network-discovery-deb-2-8-ui/2931)|[CLI](/t/network-discovery-deb-2-9-cli/2932) ~ [UI](/t/network-discovery-deb-2-9-ui/2933)|[CLI](/t/network-discovery-deb-3-0-cli/4043) ~ [UI](/t/network-discovery-deb-3-0-ui/4044)|

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 
MAAS constantly listens to the network and reports any discovered devices. Devices are identified when the rack controller observes them communicating on an attached IPv4 subnet. Discovered devices that do not correspond to machines and devices already known to MAAS are shown on the dashboard. If a device advertises a hostname using `mDNS` (such as with `avahi` or `Bonjour`), MAAS will also present the discovered hostname when listing devices..

An unknown discovered device can be added to MAAS as a device or as a network interface belonging to a machine or device. Clicking the down arrow to the right of a new device allows values such as 'Type', 'Domain', 'IP Assignment' and 'Parent' to be changed prior to the device being added. Selecting a Parent device is optional.

To enable network discovery, enter the following at the command line:

```
maas admin maas set-config name=network_discovery value="enabled"
```

Network discovery can be disabled or re-enabled at any time with this CLI command.
snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli  snap-3-0-cli deb-3-0-cli -->

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
MAAS constantly listens to the network and reports any discovered devices. Devices are identified when the rack controller observes them communicating on an attached IPv4 subnet. Discovered devices that do not correspond to machines and devices already known to MAAS are shown on the dashboard. If a device advertises a hostname using `mDNS` (such as with `avahi` or `Bonjour`), MAAS will also present the discovered hostname in the Dashboard.

Using the Dashboard, an unknown discovered device can be added to MAAS as a device or as a network interface belonging to a machine or device. Clicking the down arrow to the right of a new device allows values such as 'Type', 'Domain', 'IP Assignment' and 'Parent' to be changed prior to the device being added. Selecting a Parent device is optional.

Network discovery can be disabled or re-enabled using the switch on the Network discovery dashboard.

<a href="https://assets.ubuntu.com/v1/1782e4aa-installconfig-networking__2.4_discovery.png" target = "_blank"><img src="https://assets.ubuntu.com/v1/1782e4aa-installconfig-networking__2.4_discovery.png"></a>

snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui -->
