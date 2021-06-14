||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/ipv6-addressing-snap-2-7-cli/2766) ~ [UI](/t/ipv6-addressing-snap-2-7-ui/2767)|[CLI](/t/ipv6-addressing-snap-2-8-cli/2768) ~ [UI](/t/ipv6-addressing-snap-2-8-ui/2769)|[CLI](/t/ipv6-addressing-snap-2-9-cli/2770) ~ [UI](/t/ipv6-addressing-snap-2-9-ui/2771)|[CLI](/t/ipv6-addressing-snap-3-0-cli/3969) ~ [UI](/t/ipv6-addressing-snap-3-0-ui/3970)|
Packages|[CLI](/t/ipv6-addressing-deb-2-7-cli/2772) ~ [UI](/t/ipv6-addressing-deb-2-7-ui/2773)|[CLI](/t/ipv6-addressing-deb-2-8-cli/2774) ~ [UI](/t/ipv6-addressing-deb-2-8-ui/2775)|[CLI](/t/ipv6-addressing-deb-2-9-cli/2776) ~ [UI](/t/ipv6-addressing-deb-2-9-ui/2777)|[CLI](/t/ipv6-addressing-deb-3-0-cli/3971) ~ [UI](/t/ipv6-addressing-deb-3-0-ui/3972)|

Support for IPv6 in MAAS is similar to support for IPv4.  A rack controller in an IPv6 context needs to have the region API server URL specified with brackets:

``` nohighlight
http://[::1]:5240/MAAS/
```

You can access the Web UI and the [MAAS CLI](/t/maas-cli/2825) (that is, logging in to the API server) in the same way on both IPv4 and IPv6. To use an IPv6 address in a URL, surround it with square brackets. For example, on the local machine (`::1`, the IPv6 equivalent of `localhost`):

[note]
MAAS can only control most BMCs using IPv4.
[/note]

#### Three questions you may have:

* [What should I know about enabling IPv6?](#heading--enable-ipv6)
* [How do I configure an IPv6 subnet?](#heading--configure-an-ipv6-subnet)
* [What should I know about routing?](#heading--routing)

<a href="#heading--enable-ipv6"><h2 id="heading--enable-ipv6">Enable IPv6</h2></a>

You enable IPv6 networking in the same way that you enable IPv4 networking: configure a separate rack controller interface for your IPv6 subnet. The IPv6 interface must define a static address range. Provided that you already have a functioning IPv6 network, that's all there is to it. The following sections explain requirements, supported operations, and what to do if you don't yet have a functioning IPv6 network.

An IPv6 interface can use the same network interface on the rack controller as an existing IPv4 network interface. It just defines a different subnet, with IPv6 addressing. A machine that's connected to the IPv4 subnet also connected to the IPv6 subnet on the same network segment.

<a href="#heading--configure-an-ipv6-subnet"><h3 id="heading--configure-an-ipv6-subnet">Configure an IPv6 subnet</h3></a>

Define a reserved static IP range and machines deployed on the subnet will get a static address in this range. Since IPv6 networks usually are 64 bits wide you can be generous with the range size. Leave the netmask and broadcast address fields blank.

You may want MAAS to manage DHCP and DNS, but it's not required. Machines do not need a DHCP server at all for IPv6; MAAS configures static IPv6 addresses on a machine's network interface while deploying it. A DHCPv6 server can provide addresses for containers or virtual machines running on the machines, as well as devices on the network that are not managed by MAAS. The machines do not need DHCPv6. MAAS will not be aware of any addresses issued by DHCP, and cannot guarantee that they will stay unchanged.

<a href="#heading--routing"><h3 id="heading--routing">Routing</h3></a>

In IPv6, clients do not discover routes through DHCP. Routers make themselves known on their networks by sending out route advertisements. These RAs also contain other configuration items:

 * Switches that allow stateless configuration of their unique IP addresses, based on MAC addresses. 
* Switches that enable them to request stateless configuration from a DHCP server.
* Switches that In any allow them to request a stateful IP address from a DHCP server. 

Since a network interface can have any number of IPv6 addresses even on a single subnet, several of these address assignment mechanisms can be combined.

However, when MAAS configures IPv6 networking on a machine, it does not rely on RAs. It statically configures a machine's default IPv6 route to use the router that is set on the cluster interface, so that the machine will know their default gateway. They do not need DHCP and will not autoconfigure global addresses.

You may be planning to operate DHCPv6 clients as well, for example, on machines not managed by MAAS, or on virtual machines hosted by MAAS machines.  If this is the case, you may want to configure RAs, so that those clients obtain configuration over DHCP.

If you need RAs but your gateway does not send them, install and configure `radvd` somewhere on the network to advertise its route.
