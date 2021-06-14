||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/ip-ranges-snap-2-7-cli/2754) ~ [UI](/t/ip-ranges-snap-2-7-ui/2755)|[CLI](/t/ip-ranges-snap-2-8-cli/2756) ~ [UI](/t/ip-ranges-snap-2-8-ui/2757)|[CLI](/t/ip-ranges-snap-2-9-cli/2758) ~ [UI](/t/ip-ranges-snap-2-9-ui/2759)|[CLI](/t/ip-ranges-snap-3-0-cli/3965) ~ [UI](/t/ip-ranges-snap-3-0-ui/3966)|
Packages|[CLI](/t/ip-ranges-deb-2-7-cli/2760) ~ [UI](/t/ip-ranges-deb-2-7-ui/2761)|[CLI](/t/ip-ranges-deb-2-8-cli/2762) ~ [UI](/t/ip-ranges-deb-2-8-ui/2763)|[CLI](/t/ip-ranges-deb-2-9-cli/2764) ~ [UI](/t/ip-ranges-deb-2-9-ui/2765)|[CLI](/t/ip-ranges-deb-3-0-cli/3967) ~ [UI](/t/ip-ranges-deb-3-0-ui/3968)|

In MAAS-managed networks, you can further manage your subnets with a reserved range of IP addresses.  You can reserve IP addresses by adding one or more reserved ranges to a subnet configuration. You can define two types of ranges: reserved ranges and reserved dynamic ranges.  

A reserved range operates differently depending on whether the subnet is managed or unmanaged.  For a managed (subnet), MAAS will never assign IP addresses inside this range.  You can use this range for anything, such as infrastructure systems, network hardware, external DHCP, or an OpenStack namespace.  For an unmanaged (subnet), MAAS will only assign IP addresses inside this range -- but MAAS can assign any IP within this range.

A reserved dynamic range is used by MAAS for enlisting, commissioning and, if enabled, MAAS-managed DHCP on the machine's VLAN during commissioning and deployment. If created with the Web UI, an initial range is created as part of the DHCP enablement process. MAAS never uses IP addresses from this range for an unmanaged subnet.

This article gives specific instructions about creating and managing IP ranges.

#### Three questions you may have:

1. [How do I create an IP range?](#heading--create-a-range)
2. [How do I edit an existing IP range?](#heading--edit-a-range)
3. [How do I delete an existing IP range?](#heading--delete-a-range)

<a href="#heading--create-a-range"><h2 id="heading--create-a-range">Create a range</h2></a>

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
To create a range with the web UI, choose the "Subnets" option across the top:

<a href="https://discourse.maas.io/uploads/default/original/1X/2bc3b241b917325dac57a42771a0f9cfeb411bde.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/2bc3b241b917325dac57a42771a0f9cfeb411bde.jpeg"></a>

In the "SUBNET" column, choose the subnet for which you want to create an IP range(s):

<a href="https://discourse.maas.io/uploads/default/original/1X/051bf1e56a31c7e7dcb196b12ddf55435b3f0571.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/051bf1e56a31c7e7dcb196b12ddf55435b3f0571.jpeg"></a>

Scroll down to "Reserved ranges" on the subnet screen and click on the "Reserve range" drop-down:

<a href="https://discourse.maas.io/uploads/default/original/1X/a76e24de7c65d3553f853bc2b6a96671d756651b.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/a76e24de7c65d3553f853bc2b6a96671d756651b.jpeg"></a>

snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui -->

<!-- deb-2-7-ui
Choose 'Reserve range' or 'Reserve dynamic range'. If you choose the latter, MAAS will automatically provide DHCP for enlistment and commissioning provided that the associated VLAN has DHCP enabled. Read the [DHCP page](/t/managing-dhcp/2905).
 deb-2-7-ui -->

<!-- deb-2-8-ui
Choose 'Reserve range' or 'Reserve dynamic range'. If you choose the latter, MAAS will automatically provide DHCP for enlistment and commissioning provided that the associated VLAN has DHCP enabled. Read the [DHCP page](/t/managing-dhcp/2907).
 deb-2-8-ui -->

<!-- deb-2-9-ui
Choose 'Reserve range' or 'Reserve dynamic range'. If you choose the latter, MAAS will automatically provide DHCP for enlistment and commissioning provided that the associated VLAN has DHCP enabled. Read the [DHCP page](/t/managing-dhcp/2909).
 deb-2-9-ui -->

<!-- deb-3-0-ui
Choose 'Reserve range' or 'Reserve dynamic range'. If you choose the latter, MAAS will automatically provide DHCP for enlistment and commissioning provided that the associated VLAN has DHCP enabled. Read the [DHCP page](/t/managing-dhcp/4035).
 deb-3-0-ui -->

<!-- snap-2-7-ui
Choose 'Reserve range' or 'Reserve dynamic range'. If you choose the latter, MAAS will automatically provide DHCP for enlistment and commissioning provided that the associated VLAN has DHCP enabled. Read the [DHCP page](/t/managing-dhcp/2899).
 snap-2-7-ui -->

<!-- snap-2-8-ui
Choose 'Reserve range' or 'Reserve dynamic range'. If you choose the latter, MAAS will automatically provide DHCP for enlistment and commissioning provided that the associated VLAN has DHCP enabled. Read the [DHCP page](/t/managing-dhcp/2901).
 snap-2-8-ui -->

<!-- snap-2-9-ui
Choose 'Reserve range' or 'Reserve dynamic range'. If you choose the latter, MAAS will automatically provide DHCP for enlistment and commissioning provided that the associated VLAN has DHCP enabled. Read the [DHCP page](/t/managing-dhcp/2903).
 snap-2-9-ui -->

<!-- snap-3-0-ui
Choose 'Reserve range' or 'Reserve dynamic range'. If you choose the latter, MAAS will automatically provide DHCP for enlistment and commissioning provided that the associated VLAN has DHCP enabled. Read the [DHCP page](/t/managing-dhcp/4033).
 snap-3-0-ui -->

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
When you choose either of those two options, a window will appear allowing you to enter start and end addresses for the range as well as a comment.

Below is an example window when creating a 'reserved range' (the windows are identical):

<a href="https://assets.ubuntu.com/v1/be85b7d6-installconfig-network-ipranges__2.4_add-reserved-iprange.png" target = "_blank"><img src="https://assets.ubuntu.com/v1/be85b7d6-installconfig-network-ipranges__2.4_add-reserved-iprange.png"></a>

Click the 'Reserve' button when done.
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui -->

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 
See [Concepts and terms](/t/concepts-and-terms/785#heading--ip-ranges) for an explanation of the two kinds of reserved IP ranges MAAS uses.

To create a range of dynamic IP addresses that will be used by MAAS for node enlistment, commissioning, and possibly deployment:

``` bash
maas $PROFILE ipranges create type=dynamic \
    start_ip=$IP_DYNAMIC_RANGE_LOW end_ip=$IP_DYNAMIC_RANGE_HIGH \
    comment='This is a reserved dynamic range'
```

To create a range of IP addresses that will not be used by MAAS:

``` bash
maas $PROFILE ipranges create type=reserved \
    start_ip=$IP_STATIC_RANGE_LOW end_ip=$IP_STATIC_RANGE_HIGH \
    comment='This is a reserved range'
```

To reserve a single IP address that will not be used by MAAS:

``` bash
maas $PROFILE ipaddresses reserve ip_address=$IP_STATIC_SINGLE
```

To remove such a single reserved IP address:

``` bash
maas $PROFILE ipaddresses release ip=$IP_STATIC_SINGLE
```

snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli -->

<a href="#heading--edit-a-range"><h2 id="heading--edit-a-range">Edit a range</h2></a>

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 
To edit an IP range, first find the ID of the desired IP range with the command:

```
maas admin ipranges read
```

Examine the JSON output to find the ID corresponding to the IP range you want to edit, then enter:

```
maas admin iprange update $ID start_ip="<start ip>" end_ip="<end ip>" comment="freeform comment"
```

This command will update the IP range associated with $ID.
snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli  -->

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
Click the 'Menu' button at the far right of the row corresponding to the subnet in question and select 'Edit reserved range' from the menu that appears. Edit the fields as desired and click the 'Save' button.

<a href="#heading--delete-a-range"><h2 id="heading--delete-a-range">Delete a range</h2></a>

Select 'Remove range' from the menu that appears when clicking the 'Menu' button at the far right of the row corresponding to the subnet in question.

snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui -->
