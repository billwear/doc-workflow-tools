||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/networking-snap-2-7-cli/2946) ~ [UI](/t/networking-snap-2-7-ui/2947)|[CLI](/t/networking-snap-2-8-cli/2948) ~ [UI](/t/networking-snap-2-8-ui/2949)|[CLI](/t/networking-snap-2-9-cli/2950) ~ [UI](/t/networking-snap-2-9-ui/2951)|[CLI](/t/networking-snap-3-0-cli/4045) ~ [UI](/t/networking-snap-3-0-ui/4046)|
Packages|[CLI](/t/networking-deb-2-7-cli/2952) ~ [UI](/t/networking-deb-2-7-ui/2953)|[CLI](/t/networking-deb-2-8-cli/2954) ~ [UI](/t/networking-deb-2-8-ui/2955)|[CLI](/t/networking-deb-2-9-cli/2956) ~ [UI](/t/networking-deb-2-9-ui/2957)|[CLI](/t/networking-deb-3-0-cli/4047) ~ [UI](/t/networking-deb-3-0-ui/4048)|

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli
You can use the CLI to manage the networking elements of MAAS, including subnets, fabrics, VLANs, and spaces.  This page shows how to access and edit these elements. See [Concepts and terms](/t/concepts-and-terms/785) for the definitions of networking objects, along with a basic networking tutorial (if needed).

#### Nine questions you may have:

1. [How do I list available subnets?](#heading--cli-list-available-subnets)
2. [How do I manage subnets?](#heading--cli-managing-subnets)
3. [How do I manage static routes?](#heading--static-routes)
4. [How do I manage reserved ranges?](#heading--reserved-ranges)
5. [How do I set up a bridge?](#heading--setting-up-a-bridge)
6. [How do I set up a bridge with the MAAS CLI/API?](#heading--maas-bridge-cli)
7. [How do I set up a bridge with netplan?](#heading--maas-bridge-netplan)

<a href="#heading--cli-list-available-subnets"><h2 id="heading--cli-list-available-subnets">List available subnets</h2></a>

To view the list of available subnets, enter the following command:

```
maas admin subnets read | \
jq -r '(["FABRIC", "VLAN", "DHCP", "SUBNET"]
| (., map(length*"-"))),
(.[] | [.vlan.fabric, .vlan.name, .vlan.dhcp_on, .cidr])
| @tsv' \
| column -t
```

which produces output something like this:

```
FABRIC        VLAN      DHCP       SUBNET
------        ----      ---------  ------
Patient-Care  untagged  true       192.168.123.0/24
fabric-0      untagged  false      0.0.0.0/0
fabric-0      untagged  false      10.0.0.0/24
fabric-1      untagged  false      10.70.132.0/24
fabric-1      untagged  false      fd42:8b52:7114:9ef8::/64
fabric-3      untagged  true       192.168.43.0/24
fabric-3      untagged  true       2600:100d:b125:d5e9::/64
fabric-3      untagged  true       2600:100d:b120:3933::/64
fabric-3      untagged  true       2600:100d:b109:dee0::/64
fabric-3      untagged  true       2600:100d:b104:94c0::/64
```
snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli-->

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui deb-3-0-ui snap-3-0-ui
You can use the Web UI to manage the networking elements of MAAS, including subnets, fabrics, VLANs, and spaces.  This page shows how to access and edit these elements. See [Concepts and terms](/t/concepts-and-terms/785) for the definitions of networking objects, along with a basic networking tutorial (if needed).

#### Ten questions you may have:

1. [How do I access the main networking view?](#heading--ui-main-view)
2. [How do I view the subnet window?](#heading--ui-subnet-window)
3. [How do I view a subnet summary?](#heading--ui-subnet-summary)
4. [How do I view utilisation?](#heading--ui-utilisation)
5. [How do I manage static routes?](#heading--static-routes)
6. [How do I manage reserved ranges?](#heading--reserved-ranges)
7. [How do I view used addresses?](#heading--ui-used-addresses)
8. [How do I set up a bridge?](#heading--setting-up-a-bridge)
9. [How do I set up a bridge with the web UI?](#heading--maas-bridge-web-ui)
10. [How do I set up a bridge with netplan?](#heading--maas-bridge-netplan)

<a href="#heading--ui-main-view"><h2 id="heading--ui-main-view">Main networking view</h2></a>

To access the main networking view visit the 'Subnets' page:

<a href="https://assets.ubuntu.com/v1/657bb332-installconfig-networking__2.4_subnets.png" target = "_blank"><img src="https://assets.ubuntu.com/v1/657bb332-installconfig-networking__2.4_subnets.png"></a>

Due to the nature of this example, we re-use elements like fabrics, VLANs, subnets, and spaces.  MAAS can automatically detect these elements -- here there are two fabrics, one VLAN, five subnets, and two spaces -- but if MAAS doesn't find them, they can be added manually using the 'Add' button.

This main view can also be filtered either by fabrics or by spaces through the use of the 'Group by' drop-down.
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui deb-3-0-ui snap-3-0-ui -->

<!-- deb-2-7-cli
Fabrics, VLANs, and spaces do not require much configuration beyond names and descriptions. You can change the MTU for a VLAN, as well as [enable DHCP](/t/managing-dhcp/2904#heading--enabling-dhcp) (see 'Take action' button).  None of these options requires detailed instruction. A subnet, on the other hand, provides a number of configuration options relevant to the day-to-day operation of MAAS.
 deb-2-7-cli -->

<!-- deb-2-7-ui
Fabrics, VLANs, and spaces do not require much configuration beyond names and descriptions. You can change the MTU for a VLAN, as well as [enable DHCP](/t/managing-dhcp/2905#heading--enabling-dhcp) (see 'Take action' button).  None of these options requires detailed instruction. A subnet, on the other hand, provides a number of configuration options relevant to the day-to-day operation of MAAS.
 deb-2-7-ui -->

<!-- deb-2-8-cli
Fabrics, VLANs, and spaces do not require much configuration beyond names and descriptions. You can change the MTU for a VLAN, as well as [enable DHCP](/t/managing-dhcp/2906#heading--enabling-dhcp) (see 'Take action' button).  None of these options requires detailed instruction. A subnet, on the other hand, provides a number of configuration options relevant to the day-to-day operation of MAAS.
 deb-2-8-cli -->

<!-- deb-2-8-ui
Fabrics, VLANs, and spaces do not require much configuration beyond names and descriptions. You can change the MTU for a VLAN, as well as [enable DHCP](/t/managing-dhcp/2907#heading--enabling-dhcp) (see 'Take action' button).  None of these options requires detailed instruction. A subnet, on the other hand, provides a number of configuration options relevant to the day-to-day operation of MAAS.
 deb-2-8-ui -->

<!-- deb-2-9-cli
Fabrics, VLANs, and spaces do not require much configuration beyond names and descriptions. You can change the MTU for a VLAN, as well as [enable DHCP](/t/managing-dhcp/2908#heading--enabling-dhcp) (see 'Take action' button).  None of these options requires detailed instruction. A subnet, on the other hand, provides a number of configuration options relevant to the day-to-day operation of MAAS.
 deb-2-9-cli -->

<!-- deb-2-9-ui
Fabrics, VLANs, and spaces do not require much configuration beyond names and descriptions. You can change the MTU for a VLAN, as well as [enable DHCP](/t/managing-dhcp/2909#heading--enabling-dhcp) (see 'Take action' button).  None of these options requires detailed instruction. A subnet, on the other hand, provides a number of configuration options relevant to the day-to-day operation of MAAS.
 deb-2-9-ui -->

<!-- deb-3-0-cli
Fabrics, VLANs, and spaces do not require much configuration beyond names and descriptions. You can change the MTU for a VLAN, as well as [enable DHCP](/t/managing-dhcp/4035#heading--enabling-dhcp) (see 'Take action' button).  None of these options requires detailed instruction. A subnet, on the other hand, provides a number of configuration options relevant to the day-to-day operation of MAAS.
 deb-3-0-cli -->

<!-- deb-3-0-ui
Fabrics, VLANs, and spaces do not require much configuration beyond names and descriptions. You can change the MTU for a VLAN, as well as [enable DHCP](/t/managing-dhcp/4036#heading--enabling-dhcp) (see 'Take action' button).  None of these options requires detailed instruction. A subnet, on the other hand, provides a number of configuration options relevant to the day-to-day operation of MAAS.
 deb-3-0-ui -->

<!-- snap-2-7-cli
Fabrics, VLANs, and spaces do not require much configuration beyond names and descriptions. You can change the MTU for a VLAN, as well as [enable DHCP](/t/managing-dhcp/2898#heading--enabling-dhcp) (see 'Take action' button).  None of these options requires detailed instruction. A subnet, on the other hand, provides a number of configuration options relevant to the day-to-day operation of MAAS.
 snap-2-7-cli -->

<!-- snap-2-7-ui
Fabrics, VLANs, and spaces do not require much configuration beyond names and descriptions. You can change the MTU for a VLAN, as well as [enable DHCP](/t/managing-dhcp/2899#heading--enabling-dhcp) (see 'Take action' button).  None of these options requires detailed instruction. A subnet, on the other hand, provides a number of configuration options relevant to the day-to-day operation of MAAS.
 snap-2-7-ui -->

<!-- snap-2-8-cli
Fabrics, VLANs, and spaces do not require much configuration beyond names and descriptions. You can change the MTU for a VLAN, as well as [enable DHCP](/t/managing-dhcp/2900#heading--enabling-dhcp) (see 'Take action' button).  None of these options requires detailed instruction. A subnet, on the other hand, provides a number of configuration options relevant to the day-to-day operation of MAAS.
 snap-2-8-cli -->

<!-- snap-2-8-ui
Fabrics, VLANs, and spaces do not require much configuration beyond names and descriptions. You can change the MTU for a VLAN, as well as [enable DHCP](/t/managing-dhcp/2901#heading--enabling-dhcp) (see 'Take action' button).  None of these options requires detailed instruction. A subnet, on the other hand, provides a number of configuration options relevant to the day-to-day operation of MAAS.
 snap-2-8-ui -->

<!-- snap-2-9-cli
Fabrics, VLANs, and spaces do not require much configuration beyond names and descriptions. You can change the MTU for a VLAN, as well as [enable DHCP](/t/managing-dhcp/2902#heading--enabling-dhcp) (see 'Take action' button).  None of these options requires detailed instruction. A subnet, on the other hand, provides a number of configuration options relevant to the day-to-day operation of MAAS.
 snap-2-9-cli -->

<!-- snap-2-9-ui
Fabrics, VLANs, and spaces do not require much configuration beyond names and descriptions. You can change the MTU for a VLAN, as well as [enable DHCP](/t/managing-dhcp/2903#heading--enabling-dhcp) (see 'Take action' button).  None of these options requires detailed instruction. A subnet, on the other hand, provides a number of configuration options relevant to the day-to-day operation of MAAS.
 snap-2-9-ui -->

<!-- snap-3-0-cli
Fabrics, VLANs, and spaces do not require much configuration beyond names and descriptions. You can change the MTU for a VLAN, as well as [enable DHCP](/t/managing-dhcp/4033#heading--enabling-dhcp) (see 'Take action' button).  None of these options requires detailed instruction. A subnet, on the other hand, provides a number of configuration options relevant to the day-to-day operation of MAAS.
 snap-3-0-cli -->

<!-- snap-3-0-ui
Fabrics, VLANs, and spaces do not require much configuration beyond names and descriptions. You can change the MTU for a VLAN, as well as [enable DHCP](/t/managing-dhcp/4034#heading--enabling-dhcp) (see 'Take action' button).  None of these options requires detailed instruction. A subnet, on the other hand, provides a number of configuration options relevant to the day-to-day operation of MAAS.
 snap-3-0-ui -->

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli deb-3-0-cli snap-3-0-cli
<a href="#heading--cli-managing-subnets"><h2 id="heading--cli-managing-subnets">Managing subnets</h3></a>

You can view the details of an individual subnet with the command:

```
maas $PROFILE subnet read $SUBNET_ID \
| jq -r '(["NAME","CIDR","GATEWAY","DNS","DISCOVERY","FABRIC","VLAN"]
| (., map(length*"-"))), ([.name,.cidr,.gateway_ip // "-", .allow_dns,.active_discovery,.vlan.name,.vlan.fabric]) | @tsv' | column -t
```

This command retrieves output similar to this:

```
NAME              CIDR              GATEWAY  DNS   DISCOVERY  FABRIC    VLAN
----              ----              -------  ---   ---------  ------    ----
192.168.123.0/24  192.168.123.0/24  -        true  false      untagged  default
```

If you don't know the subnet ID, you can look it up like this:

```
maas $PROFILE subnets read \
| jq -r '(["NAME", "SUBNET_ID"]
| (., map(length*"-"))), (.[] | [.name, .id]) | @tsv' \
| column -t | grep $SUBNET_NAME
```

For example, if you're using the "admin" profile, and your subnet name contains "192.168.123," you could find the subnet ID with this command:

```
maas admin subnets read \
| jq -r '(["NAME", "SUBNET_ID"]
| (., map(length*"-"))), (.[] | [.name, .id]) | @tsv' \
| column -t | grep 192.168.123
```

Subnets support the following configurable values:
snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli -->

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
<a href="#heading--ui-subnet-window"><h2 id="heading--ui-subnet-window">Subnet window</h3></a>

Clicking a subnet (here `192.168.100.0/24`) will display its detail screen, which presents several vertical sections.  Let's take them one by one.

<a href="#heading--ui-subnet-summary"><h3 id="heading--ui-subnet-summary">Subnet summary</h3></a>

The **Subnet summary** section is the largest and most complex of the subnet configuration screens:

<a href="https://assets.ubuntu.com/v1/17617b35-installconfig-networking__2.4_subnets-summary.png" target = "_blank"><img src="https://assets.ubuntu.com/v1/17617b35-installconfig-networking__2.4_subnets-summary.png"></a>

This screen presents the following configurable options:
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui -->

* **Name**: Subnet names can be any valid text string, although usually, and by default, they are named with the CIDR of the subnet itself.

* **CIDR**: This is the address parameter for the subnet.  In keeping with standard CIDR notation, the number of bits of the prefix are indicated after the slash.

* **Gateway IP**: This is the address of the default gateway for your subnet, which is the IP address that transfers packets to other subnets or networks. Typically, this is simply the first IP address in a block of addresses (the `.1` address).

* **DNS**: This is the address of a DNS (domain name server, or simply "nameserver") for your subnet.  It's optional, but can be configured if desired.

* **Description**: This field represents freeform text that you can enter to describe your subnet, as needed to keep important notes attached to the definition of the subnet.

<!-- deb-2-7-cli
* **Managed allocation** refers to the ability of MAAS to completely manage a subnet. See [Subnet management](/t/subnet-management/3120).
 deb-2-7-cli -->

<!-- deb-2-7-ui
* **Managed allocation** refers to the ability of MAAS to completely manage a subnet. See [Subnet management](/t/subnet-management/3121).
 deb-2-7-ui -->

<!-- deb-2-8-cli
* **Managed allocation** refers to the ability of MAAS to completely manage a subnet. See [Subnet management](/t/subnet-management/3122).
 deb-2-8-cli -->

<!-- deb-2-8-ui
* **Managed allocation** refers to the ability of MAAS to completely manage a subnet. See [Subnet management](/t/subnet-management/3123).
 deb-2-8-ui -->

<!-- deb-2-9-cli
* **Managed allocation** refers to the ability of MAAS to completely manage a subnet. See [Subnet management](/t/subnet-management/3124).
 deb-2-9-cli -->

<!-- deb-2-9-ui
* **Managed allocation** refers to the ability of MAAS to completely manage a subnet. See [Subnet management](/t/subnet-management/3125).
 deb-2-9-ui -->

<!-- deb-3-0-cli
* **Managed allocation** refers to the ability of MAAS to completely manage a subnet. See [Subnet management](/t/subnet-management/4111).
 deb-3-0-cli -->

<!-- deb-3-0-ui
* **Managed allocation** refers to the ability of MAAS to completely manage a subnet. See [Subnet management](/t/subnet-management/4112).
 deb-3-0-ui -->

<!-- snap-2-7-cli
* **Managed allocation** refers to the ability of MAAS to completely manage a subnet. See [Subnet management](/t/subnet-management/3114).
 snap-2-7-cli -->

<!-- snap-2-7-ui
* **Managed allocation** refers to the ability of MAAS to completely manage a subnet. See [Subnet management](/t/subnet-management/3115).
 snap-2-7-ui -->

<!-- snap-2-8-cli
* **Managed allocation** refers to the ability of MAAS to completely manage a subnet. See [Subnet management](/t/subnet-management/3116).
 snap-2-8-cli -->

<!-- snap-2-8-ui
* **Managed allocation** refers to the ability of MAAS to completely manage a subnet. See [Subnet management](/t/subnet-management/3117).
 snap-2-8-ui -->

<!-- snap-2-9-cli
* **Managed allocation** refers to the ability of MAAS to completely manage a subnet. See [Subnet management](/t/subnet-management/3118).
 snap-2-9-cli -->

<!-- snap-2-9-ui
* **Managed allocation** refers to the ability of MAAS to completely manage a subnet. See [Subnet management](/t/subnet-management/3119).
 snap-2-9-ui -->

<!-- snap-3-0-cli
* **Managed allocation** refers to the ability of MAAS to completely manage a subnet. See [Subnet management](/t/subnet-management/4109).
 snap-3-0-cli -->

<!-- snap-3-0-ui
* **Managed allocation** refers to the ability of MAAS to completely manage a subnet. See [Subnet management](/t/subnet-management/4110).
 snap-3-0-ui -->

* **Active mapping** instructs MAAS to scan the subnet every 3 hours to discover hosts that have not been discovered passively.

* **Proxy access** instructs MAAS to allow clients from this subnet to access the MAAS proxy.

* **Allow DNS resolution** allows subnet clients to use MAAS for DNS resolution.

* **Fabric**: This field allows you to set the subnet's fabric.

* **VLAN**: This field allows you to set the subnet's VLAN.

* **Space** is presented for clarity, though spaces are managed at the VLAN level.

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui
<a href="#heading--ui-utilisation"><h3 id="heading--ui-utilisation">Utilisation</h3></a>

This section of the subnet page presents metrics regarding address usage by this subnet.

<a href="https://assets.ubuntu.com/v1/3d3e4b61-installconfig-networking__2.4_subnets-utilisation.png" target = "_blank"><img src="https://assets.ubuntu.com/v1/3d3e4b61-installconfig-networking__2.4_subnets-utilisation.png"></a>

'Subnet addresses' shows the total number of addresses associated with the subnet, here 254. 'Availability' shows how many of those addresses are unused, and therefore "available", here 189, which corresponds to a percentage of roughly 74% of the total. Finally, 'Used' shows the percentage that is used, here roughly 26%.
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui --> 

<a href="#heading--static-routes"><h2 id="heading--static-routes">Static Routes</h2></a>

This section can be used to define a static route between two subnets. A route is defined on a per-subnet basis to use a particular gateway, using a configured destination and metric.

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli
To create a static route, use the following command:

```
maas admin static-routes create source=$SOURCE_SUBNET destination=$DEST_SUBNET \
gateway_ip=$GATEWAY_IP
```
snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli -->

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui
To create a static route, click the 'Add static route' button to reveal the edit pane. Enter a Gateway IP address, select a destination subnet from the 'Destination' drop-down list, and edit the routing metric value if needed. Clicking 'Add' will activate the route. Routes can be edited and removed using the icons to the right of each entry.

<a href="https://assets.ubuntu.com/v1/49f5e240-installconfig-networking__2.4_subnets-routes.png" target = "_blank"><img src="https://assets.ubuntu.com/v1/49f5e240-installconfig-networking__2.4_subnets-routes.png"></a>
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui -->

<a href="#heading--reserved-ranges"><h2 id="heading--reserved-ranges">Reserved ranges</h2></a>

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui deb-3-0-ui snap-3-0-ui
The reserved ranges section of the subnet screen looks like this:

<a href="https://assets.ubuntu.com/v1/5f9f50f9-installconfig-networking__2.4_subnets-reserved.png" target = "_blank"><img src="https://assets.ubuntu.com/v1/5f9f50f9-installconfig-networking__2.4_subnets-reserved.png"></a>
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui deb-3-0-ui snap-3-0-ui -->

<!-- deb-2-7-cli
This subject is treated separately in [IP ranges](/t/ip-ranges/2760).
 deb-2-7-cli -->

<!-- deb-2-7-ui
This subject is treated separately in [IP ranges](/t/ip-ranges/2761).
 deb-2-7-ui -->

<!-- deb-2-8-cli
This subject is treated separately in [IP ranges](/t/ip-ranges/2762).
 deb-2-8-cli -->

<!-- deb-2-8-ui
This subject is treated separately in [IP ranges](/t/ip-ranges/2763).
 deb-2-8-ui -->

<!-- deb-2-9-cli
This subject is treated separately in [IP ranges](/t/ip-ranges/2764).
 deb-2-9-cli -->

<!-- deb-2-9-ui
This subject is treated separately in [IP ranges](/t/ip-ranges/2765).
 deb-2-9-ui -->

<!-- deb-3-0-cli
This subject is treated separately in [IP ranges](/t/ip-ranges/3967).
 deb-3-0-cli -->

<!-- deb-3-0-ui
This subject is treated separately in [IP ranges](/t/ip-ranges/3968).
 deb-3-0-ui -->

<!-- snap-2-7-cli
This subject is treated separately in [IP ranges](/t/ip-ranges/2754).
 snap-2-7-cli -->

<!-- snap-2-7-ui
This subject is treated separately in [IP ranges](/t/ip-ranges/2755).
 snap-2-7-ui -->

<!-- snap-2-8-cli
This subject is treated separately in [IP ranges](/t/ip-ranges/2756).
 snap-2-8-cli -->

<!-- snap-2-8-ui
This subject is treated separately in [IP ranges](/t/ip-ranges/2757).
 snap-2-8-ui -->

<!-- snap-2-9-cli
This subject is treated separately in [IP ranges](/t/ip-ranges/2758).
 snap-2-9-cli -->

<!-- snap-2-9-ui
This subject is treated separately in [IP ranges](/t/ip-ranges/2759).
 snap-2-9-ui -->

<!-- snap-3-0-cli
This subject is treated separately in [IP ranges](/t/ip-ranges/3965).
 snap-3-0-cli -->

<!-- snap-3-0-ui
This subject is treated separately in [IP ranges](/t/ip-ranges/3966).
 snap-3-0-ui -->

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui
<a href="#heading--ui-used-addresses"><h2 id="heading--ui-used-addresses">Used</h2></a>

This section displays hosts (including controllers) associated with the used addresses along with related bits of host information.

<a href="https://assets.ubuntu.com/v1/b9e69b0b-installconfig-networking__2.4_subnets-used.png" target = "_blank"><img src="https://assets.ubuntu.com/v1/b9e69b0b-installconfig-networking__2.4_subnets-used.png"></a>
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui -->

<a href="#heading--setting-up-a-bridge"><h2 id="heading--setting-up-a-bridge">Setting up a bridge</h2></a>

At various times in your MAAS network, you may need to set up a bridge to connect between your machines and MAAS.  This section explains several ways of accomplishing this.

[note]
It's essential to enforce usage of IP addresses to avoid domain name conflicts, should different controllers resolve the same domain name with different IP addresses. You should also avoid using 127.0.0.1 when running multiple controllers, as it would confuse MAAS.
[/note]

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui
<a href="#heading--maas-bridge-web-ui"><h2 id="heading--maas-bridge-web-ui">Set up a bridge with MAAS UI</h2></a>

You can use the MAAS UI to configure a bridge. Select the machine you want to bridge and switch to the "Network" tab. Select the network where you want to create the bridge and click "Create bridge:"

<a href="https://discourse.maas.io/uploads/default/original/1X/29624d737106c5bad777aee9d2c8cad9c3de7151.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/29624d737106c5bad777aee9d2c8cad9c3de7151.jpeg"></a> 

Configure the bridge on a subnet MAAS controls.  You may use any IP mode for the bridge:

<a href="https://discourse.maas.io/uploads/default/original/1X/dd8567ff1cd76606c5ce1751e606fcfab2bc7ce2.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/dd8567ff1cd76606c5ce1751e606fcfab2bc7ce2.jpeg"></a> 

When you're done, it should look something like this:

<a href="https://discourse.maas.io/uploads/default/original/1X/e392d638f0acecb9d54c81bbca4ee17cbcd05445.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/e392d638f0acecb9d54c81bbca4ee17cbcd05445.jpeg"></a> 

Then you can deploy using the bridge.

snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui -->

<!-- snap-2-9-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui
**NOTE** that you can create an "OpenVswitch" bridge if desired, and MAAS will create the netplan model for you.
 snap-2-9-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui --> 

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli
<a href="#heading--maas-bridge-cli"><h2 id="heading--maas-bridge-cli">Use the MAAS API to configure a bridge</h2></a>

You can use the MAAS CLI/API to configure a bridge, with the following procedure:

1. Select the interface you wish to configure the bridge on. This example uses the boot interface, since the boot interface must be connected to a MAAS controlled network -- but any interface is allowed:

        INTERFACE_ID=$(maas $PROFILE machine read $SYSTEM_ID | jq .boot_interface.id)

2. Create the bridge:

         BRIDGE_ID=$(maas $PROFILE interfaces create-bridge $SYSTEM_ID name=br0 parent=$INTERFACE_ID | jq .id)

3. Select the subnet where you want the bridge (this should be a MAAS controlled subnet):

        SUBNET_ID=$(maas $PROFILE subnets read | jq -r '.[] | select(.cidr == "10.0.0.0/24" and .managed == true).id')

4. Connect the bridge to the subnet:

          maas $PROFILE interface link-subnet $SYSTEM_ID $BRIDGE_ID subnet=$SUBNET_ID mode="STATIC" ip_address="10.0.0.101"

snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli -->

<a href="#heading--maas-bridge-netplan"><h2 id="heading--maas-bridge-netplan">Use netplan to configure a bridge</h2></a>

You can also use netplan to configure a bridge:

Open your netplan configuration file.  This should be in `/etc/netplan`.  It could be called `50-cloud-init.yaml`, `netplan.yaml`, or something else.  Modify the file to add a bridge, using the example below to guide you:

```
network:
    bridges:
        br0:
            addresses:
            - 10.0.0.101/24
            gateway4: 10.0.0.1
            interfaces:
            - enp1s0
            macaddress: 52:54:00:39:9d:f9
            mtu: 1500
            nameservers:
                addresses:
                - 10.0.0.2
                search:
                - maas
            parameters:
                forward-delay: 15
                stp: false
    ethernets:
        enp1s0:
            match:
                macaddress: 52:54:00:39:9d:f9
            mtu: 1500
            set-name: enp1s0
        enp2s0:
            match:
                macaddress: 52:54:00:df:87:ac
            mtu: 1500
            set-name: enp2s0
        enp3s0:
            match:
                macaddress: 52:54:00:a7:ac:46
            mtu: 1500
            set-name: enp3s0
    version: 2
```

Apply the new configuration with `netplan apply`.
