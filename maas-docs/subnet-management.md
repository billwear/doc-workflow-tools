||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/subnet-management-snap-2-7-cli/3114) ~ [UI](/t/subnet-management-snap-2-7-ui/3115)|[CLI](/t/subnet-management-snap-2-8-cli/3116) ~ [UI](/t/subnet-management-snap-2-8-ui/3117)|[CLI](/t/subnet-management-snap-2-9-cli/3118) ~ [UI](/t/subnet-management-snap-2-9-ui/3119)|[CLI](/t/subnet-management-snap-3-0-cli/4109) ~ [UI](/t/subnet-management-snap-3-0-ui/4110)|
Packages|[CLI](/t/subnet-management-deb-2-7-cli/3120) ~ [UI](/t/subnet-management-deb-2-7-ui/3121)|[CLI](/t/subnet-management-deb-2-8-cli/3122) ~ [UI](/t/subnet-management-deb-2-8-ui/3123)|[CLI](/t/subnet-management-deb-2-9-cli/3124) ~ [UI](/t/subnet-management-deb-2-9-ui/3125)|[CLI](/t/subnet-management-deb-3-0-cli/4111) ~ [UI](/t/subnet-management-deb-3-0-ui/4112)|

The topic of subnet management pertains to whether or not MAAS is in full control of a subnet. When a subnet is managed, MAAS handles all aspects of IP address allocation. This process includes DHCP leases and assigned static addresses. Typically MAAS would have one managed subnet, but any additional subnets can be unmanaged. This arrangement allows for more control over which subnet gets used for DHCP and which ones do not. Additionally, as detailed below, an unmanaged subnet treats reserved IP ranges differently, and in a way that some administrators find more intuitive.

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 
#### Seven questions you may have:

1. [What are managed subnets?](#heading--managed-subnets)
2. [What are unmanaged subnets?](#heading--unmanaged-subnets)
3. [What is IP address tracking?](#heading--ip-address-tracking)
4. [How do I control subnet management](#heading--controlling-subnet-management)
5. [How do I determine a fabric ID to use in other CLI subnet calls?](#heading--determine-fabric-id)
6. [How do I set a default gateway with the CLI?](#heading--default-gateway)
7. [How do i set the DNS server with the CLI?](#heading--set-dns-server)
snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli  -->

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
#### Four questions you may have:

1. [What are managed subnets?](#heading--managed-subnets)
2. [What are unmanaged subnets?](#heading--unmanaged-subnets)
3. [What is IP address tracking?](#heading--ip-address-tracking)
4. [How do I control subnet management](#heading--controlling-subnet-management)
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui  -->

<a href="#heading--managed-subnets"><h2 id="heading--managed-subnets">Managed subnets</h2></a>

When you enable management for a subnet, MAAS will:

1.   Lease addresses for DHCP from a reserved dynamic IP range
2.   Assign static addresses not included in a reserved IP range, typically via 'Auto assign' IP allocation mode for a node.

<!-- deb-2-7-cli
See [Concepts and terms](/t/concepts-and-terms/785#heading--ip-ranges) for an explanation of the two kinds of reserved IP ranges MAAS uses and [Post-commission configuration](/t/commission-machines/2472#heading--post-commission-configuration) for information on IP allocation modes.
 deb-2-7-cli -->

<!-- deb-2-7-ui
See [Concepts and terms](/t/concepts-and-terms/785#heading--ip-ranges) for an explanation of the two kinds of reserved IP ranges MAAS uses and [Post-commission configuration](/t/commission-machines/2473#heading--post-commission-configuration) for information on IP allocation modes.
 deb-2-7-ui -->

<!-- deb-2-8-cli
See [Concepts and terms](/t/concepts-and-terms/785#heading--ip-ranges) for an explanation of the two kinds of reserved IP ranges MAAS uses and [Post-commission configuration](/t/commission-machines/2474#heading--post-commission-configuration) for information on IP allocation modes.
 deb-2-8-cli -->

<!-- deb-2-8-ui
See [Concepts and terms](/t/concepts-and-terms/785#heading--ip-ranges) for an explanation of the two kinds of reserved IP ranges MAAS uses and [Post-commission configuration](/t/commission-machines/2475#heading--post-commission-configuration) for information on IP allocation modes.
 deb-2-8-ui -->

<!-- deb-2-9-cli
See [Concepts and terms](/t/concepts-and-terms/785#heading--ip-ranges) for an explanation of the two kinds of reserved IP ranges MAAS uses and [Post-commission configuration](/t/commission-machines/2476#heading--post-commission-configuration) for information on IP allocation modes.
 deb-2-9-cli -->

<!-- deb-2-9-ui
See [Concepts and terms](/t/concepts-and-terms/785#heading--ip-ranges) for an explanation of the two kinds of reserved IP ranges MAAS uses and [Post-commission configuration](/t/commission-machines/2477#heading--post-commission-configuration) for information on IP allocation modes.
 deb-2-9-ui -->

<!-- deb-3-0-cli
See [Concepts and terms](/t/concepts-and-terms/785#heading--ip-ranges) for an explanation of the two kinds of reserved IP ranges MAAS uses and [Post-commission configuration](/t/commission-machines/3875#heading--post-commission-configuration) for information on IP allocation modes.
 deb-3-0-cli -->

<!-- deb-3-0-ui
See [Concepts and terms](/t/concepts-and-terms/785#heading--ip-ranges) for an explanation of the two kinds of reserved IP ranges MAAS uses and [Post-commission configuration](/t/commission-machines/3876#heading--post-commission-configuration) for information on IP allocation modes.
 deb-3-0-ui -->

<!-- snap-2-7-cli
See [Concepts and terms](/t/concepts-and-terms/785#heading--ip-ranges) for an explanation of the two kinds of reserved IP ranges MAAS uses and [Post-commission configuration](/t/commission-machines/2466#heading--post-commission-configuration) for information on IP allocation modes.
 snap-2-7-cli -->

<!-- snap-2-7-ui
See [Concepts and terms](/t/concepts-and-terms/785#heading--ip-ranges) for an explanation of the two kinds of reserved IP ranges MAAS uses and [Post-commission configuration](/t/commission-machines/2467#heading--post-commission-configuration) for information on IP allocation modes.
 snap-2-7-ui -->

<!-- snap-2-8-cli
See [Concepts and terms](/t/concepts-and-terms/785#heading--ip-ranges) for an explanation of the two kinds of reserved IP ranges MAAS uses and [Post-commission configuration](/t/commission-machines/2468#heading--post-commission-configuration) for information on IP allocation modes.
 snap-2-8-cli -->

<!-- snap-2-8-ui
See [Concepts and terms](/t/concepts-and-terms/785#heading--ip-ranges) for an explanation of the two kinds of reserved IP ranges MAAS uses and [Post-commission configuration](/t/commission-machines/2469#heading--post-commission-configuration) for information on IP allocation modes.
 snap-2-8-ui -->

<!-- snap-2-9-cli
See [Concepts and terms](/t/concepts-and-terms/785#heading--ip-ranges) for an explanation of the two kinds of reserved IP ranges MAAS uses and [Post-commission configuration](/t/commission-machines/2470#heading--post-commission-configuration) for information on IP allocation modes.
 snap-2-9-cli -->

<!-- snap-2-9-ui
See [Concepts and terms](/t/concepts-and-terms/785#heading--ip-ranges) for an explanation of the two kinds of reserved IP ranges MAAS uses and [Post-commission configuration](/t/commission-machines/2471#heading--post-commission-configuration) for information on IP allocation modes.
 snap-2-9-ui -->

<!-- snap-3-0-cli
See [Concepts and terms](/t/concepts-and-terms/785#heading--ip-ranges) for an explanation of the two kinds of reserved IP ranges MAAS uses and [Post-commission configuration](/t/commission-machines/3873#heading--post-commission-configuration) for information on IP allocation modes.
 snap-3-0-cli -->

<!-- snap-3-0-ui
See [Concepts and terms](/t/concepts-and-terms/785#heading--ip-ranges) for an explanation of the two kinds of reserved IP ranges MAAS uses and [Post-commission configuration](/t/commission-machines/3874#heading--post-commission-configuration) for information on IP allocation modes.
 snap-3-0-ui -->

<a href="#heading--unmanaged-subnets"><h2 id="heading--unmanaged-subnets">Unmanaged subnets</h2></a>

When management is disabled for a subnet, the definition of a reserved IP range differs from the managed mode. Here, a reserved IP range tells MAAS to **only allocate addresses from this range** (via 'Auto assign'). Also, DHCP will never lease addresses from an unmanaged subnet.

<a href="#heading--controlling-subnet-management"><h2 id="heading--controlling-subnet-management">Controlling subnet management</h2></a>

By default, MAAS manages subnets in your configuration, but it is easy to change this.

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
To disable (or re-enable) subnet management navigate to the 'Subnets' page and select the subnet. Press the 'Edit' button to allow changes. The 'Managed allocation' field will become a slide switch. Click the label (or the switch icon itself) to toggle between enabled (dark blue) and disabled (grey) and click 'Save summary'.

<a href="https://assets.ubuntu.com/v1/e5d80c8c-installconfig-network-subnet-management__2.6-management-toggle.png" target = "_blank"><img src="https://assets.ubuntu.com/v1/e5d80c8c-installconfig-network-subnet-management__2.6-management-toggle.png"></a>
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui  -->

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 

To enable or disable subnet management:

``` bash
maas $PROFILE subnet update $SUBNET_CIDR managed=false|true
```

For example, to disable:

``` bash
maas $PROFILE subnet update 192.168.1.0/24 managed=false
```

You can use the subnet's ID in place of the CIDR address.
snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli -->

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli
<a href="#heading--determine-fabric-id"><h2 id="heading--determine-fabric-id">Determine fabric ID</h2></a>

To determine a fabric ID based on a subnet address:

```
FABRIC_ID=$(maas $PROFILE subnet read $SUBNET_CIDR \
    | grep fabric | cut -d ' ' -f 10 | cut -d '"' -f 2)
```

This may come in handy when you need a fabric ID for other CLI calls.

<a href="#heading--default-gateway"><h2 id="heading--default-gateway">Set a default gateway</h2></a>

To set the default gateway for a subnet:

```
maas $PROFILE subnet update $SUBNET_CIDR gateway_ip=$MY_GATEWAY
```

<a href="#heading--set-dns-server"><h2 id="heading--set-dns-server">Set a DNS server</h2></a>

To set the DNS server for a subnet:

```
maas $PROFILE subnet update $SUBNET_CIDR dns_servers=$MY_NAMESERVER
```

snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli  -->

<a href="#heading--ip-address-tracking"><h2 id="heading--ip-address-tracking">IP address tracking</h2></a>

MAAS will keep track of all assigned addresses, regardless of whether they come from managed or unmanaged subnets.
