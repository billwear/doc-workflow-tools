||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/availability-zones-snap-2-7-cli/2322) ~ [UI](/t/availability-zones-snap-2-7-ui/2323)|[CLI](/t/availability-zones-snap-2-8-cli/2324) ~ [UI](/t/availability-zones-snap-2-8-ui/2325)|[CLI](/t/availability-zones-snap-2-9-cli/2326) ~ [UI](/t/availability-zones-snap-2-9-ui/2327)|[CLI](/t/availability-zones-snap-3-0-cli/3833) ~ [UI](/t/availability-zones-snap-3-0-ui/3834)|
Packages|[CLI](/t/availability-zones-deb-2-7-cli/2328) ~ [UI](/t/availability-zones-deb-2-7-ui/2329)|[CLI](/t/availability-zones-deb-2-8-cli/2330) ~ [UI](/t/availability-zones-deb-2-8-ui/2331)|[CLI](/t/availability-zones-deb-2-9-cli/2332) ~ [UI](/t/availability-zones-deb-2-9-ui/2333)|[CLI](/t/availability-zones-deb-3-0-cli/3835) ~ [UI](/t/availability-zones-deb-3-0-ui/3836)|

<!-- deb-2-7-cli
An availability zone is an organisational unit containing nodes, where each node is in exactly one zone. While in production, a machine can be allocated from a specific zone.  Availability zones can be used for fault-tolerance, service performance, and power management. See [Zone examples](/t/zone-examples/3276) for more details.
 deb-2-7-cli -->

<!-- deb-2-7-ui
An availability zone is an organisational unit containing nodes, where each node is in exactly one zone. While in production, a machine can be allocated from a specific zone.  Availability zones can be used for fault-tolerance, service performance, and power management. See [Zone examples](/t/zone-examples/3277) for more details.
 deb-2-7-ui -->

<!-- deb-2-8-cli
An availability zone is an organisational unit containing nodes, where each node is in exactly one zone. While in production, a machine can be allocated from a specific zone.  Availability zones can be used for fault-tolerance, service performance, and power management. See [Zone examples](/t/zone-examples/3278) for more details.
 deb-2-8-cli -->

<!-- deb-2-8-ui
An availability zone is an organisational unit containing nodes, where each node is in exactly one zone. While in production, a machine can be allocated from a specific zone.  Availability zones can be used for fault-tolerance, service performance, and power management. See [Zone examples](/t/zone-examples/3279) for more details.
 deb-2-8-ui -->

<!-- deb-2-9-cli
An availability zone is an organisational unit containing nodes, where each node is in exactly one zone. While in production, a machine can be allocated from a specific zone.  Availability zones can be used for fault-tolerance, service performance, and power management. See [Zone examples](/t/zone-examples/3280) for more details.
 deb-2-9-cli -->

<!-- deb-2-9-ui
An availability zone is an organisational unit containing nodes, where each node is in exactly one zone. While in production, a machine can be allocated from a specific zone.  Availability zones can be used for fault-tolerance, service performance, and power management. See [Zone examples](/t/zone-examples/3281) for more details.
 deb-2-9-ui -->

<!-- deb-3-0-cli
An availability zone is an organisational unit containing nodes, where each node is in exactly one zone. While in production, a machine can be allocated from a specific zone.  Availability zones can be used for fault-tolerance, service performance, and power management. See [Zone examples](/t/zone-examples/4191) for more details.
 deb-3-0-cli -->

<!-- deb-3-0-ui
An availability zone is an organisational unit containing nodes, where each node is in exactly one zone. While in production, a machine can be allocated from a specific zone.  Availability zones can be used for fault-tolerance, service performance, and power management. See [Zone examples](/t/zone-examples/4192) for more details.
 deb-3-0-ui -->

<!-- snap-2-7-cli
An availability zone is an organisational unit containing nodes, where each node is in exactly one zone. While in production, a machine can be allocated from a specific zone.  Availability zones can be used for fault-tolerance, service performance, and power management. See [Zone examples](/t/zone-examples/3270) for more details.
 snap-2-7-cli -->

<!-- snap-2-7-ui
An availability zone is an organisational unit containing nodes, where each node is in exactly one zone. While in production, a machine can be allocated from a specific zone.  Availability zones can be used for fault-tolerance, service performance, and power management. See [Zone examples](/t/zone-examples/3271) for more details.
 snap-2-7-ui -->

<!-- snap-2-8-cli
An availability zone is an organisational unit containing nodes, where each node is in exactly one zone. While in production, a machine can be allocated from a specific zone.  Availability zones can be used for fault-tolerance, service performance, and power management. See [Zone examples](/t/zone-examples/3272) for more details.
 snap-2-8-cli -->

<!-- snap-2-8-ui
An availability zone is an organisational unit containing nodes, where each node is in exactly one zone. While in production, a machine can be allocated from a specific zone.  Availability zones can be used for fault-tolerance, service performance, and power management. See [Zone examples](/t/zone-examples/3273) for more details.
 snap-2-8-ui -->

<!-- snap-2-9-cli
An availability zone is an organisational unit containing nodes, where each node is in exactly one zone. While in production, a machine can be allocated from a specific zone.  Availability zones can be used for fault-tolerance, service performance, and power management. See [Zone examples](/t/zone-examples/3274) for more details.
 snap-2-9-cli -->

<!-- snap-2-9-ui
An availability zone is an organisational unit containing nodes, where each node is in exactly one zone. While in production, a machine can be allocated from a specific zone.  Availability zones can be used for fault-tolerance, service performance, and power management. See [Zone examples](/t/zone-examples/3275) for more details.
 snap-2-9-ui -->

<!-- snap-3-0-cli
An availability zone is an organisational unit containing nodes, where each node is in exactly one zone. While in production, a machine can be allocated from a specific zone.  Availability zones can be used for fault-tolerance, service performance, and power management. See [Zone examples](/t/zone-examples/4189) for more details.
 snap-3-0-cli -->

<!-- snap-3-0-ui
An availability zone is an organisational unit containing nodes, where each node is in exactly one zone. While in production, a machine can be allocated from a specific zone.  Availability zones can be used for fault-tolerance, service performance, and power management. See [Zone examples](/t/zone-examples/4190) for more details.
 snap-3-0-ui -->

A newly installed MAAS comes with a default zone which initially contains all nodes. You cannot remove the 'default' zone or change its name, but you can create new zones and assign machine to them.  You can safely ignore this article if you're not interested in leveraging zones.

#### Six questions you may have:

1. [How do I list availability zones?](#heading--list-zones)
2. [How do I add an availability zone?](#heading--add-a-zone)
3. [How do I edit an existing availability zone?](#heading--edit-a-zone)
4. [How do I delete an existing availability zone?](#heading--delete-a-zone)
5. [How do I assign a machine to an availability zone?](#heading--assign-a-node-to-a-zone)
6. [How do I allocate a machine in a particular zone?](#heading--allocate-a-node-in-a-zone)

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 

<a href="#heading--list-zones"><h2 id="heading--list-zones">List availabilty zones</h2></a>

To see a list of availability zones, choose "AZs" from the top menu:

<a href="https://discourse.maas.io/uploads/default/original/1X/5ac446f2bda76276069fe5a1c302ff2acbf425a2.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/5ac446f2bda76276069fe5a1c302ff2acbf425a2.jpeg"></a>

<a href="#heading--add-a-zone"><h2 id="heading--add-a-zone">Add a zone</h2></a>

To create a zone, navigate to the 'AZs' page of the web UI and use the 'Add AZ' button. Enter a name for the zone and click 'Add AZ'.

<a href="https://assets.ubuntu.com/v1/f4032f39-manage-zones__2.4_add-zone.png" target = "_blank"><img src="https://assets.ubuntu.com/v1/f4032f39-manage-zones__2.4_add-zone.png"></a>

<a href="#heading--edit-a-zone"><h2 id="heading--edit-a-zone">Edit a zone</h2></a>

To edit a zone, on the 'AZs' page, select a zone and use the 'Edit' button:

<a href="https://discourse.maas.io/uploads/default/original/1X/cf5c2b91e0c3e97ec3f5a813c8a2ed85e9139e19.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/cf5c2b91e0c3e97ec3f5a813c8a2ed85e9139e19.jpeg"></a>

This selection allows you to change the name and description for the added (or edited) zone:

<a href="https://discourse.maas.io/uploads/default/original/1X/11fb5b6c13609a7ef976aa301e02f43422080066.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/11fb5b6c13609a7ef976aa301e02f43422080066.jpeg"></a>

<a href="#heading--delete-a-zone"><h2 id="heading--delete-a-zone">Delete a zone</h2></a>

To delete a zone, on the 'AZs' page, select a zone and use the 'Delete AZ' button. Doing so will also move any potential machine associations to the default zone.

<a href="https://discourse.maas.io/uploads/default/original/1X/afb0576940f2e20266dc907911f837378958a64a.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/afb0576940f2e20266dc907911f837378958a64a.jpeg"></a>

<a href="#heading--assign-a-node-to-a-zone"><h2 id="heading--assign-a-node-to-a-zone">Assign a machine to a zone</h2></a>

To assign a machine to a zone, from the 'Machines' page, select a machine (or multiple machines) and choose 'Set zone' using the 'Take action' button:

<a href="https://discourse.maas.io/uploads/default/original/1X/97db7cbfd8059d2c67566a065e08c56a20b58071.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/97db7cbfd8059d2c67566a065e08c56a20b58071.jpeg"></a>

After selecting a zone hit the 'Set zone...' button to apply the change.

You can also edit a machine's 'Configuration' page to change its zone.
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui  snap-3-0-ui deb-3-0-ui -->

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 

<a href="#heading--list-zones"><h2 id="heading--list-zones">List availability zones</h2></a>

To see a list of availability zones, enter the following command:

```
maas $PROFILE zones read \
| jq -r '(["ZONE","NAME","DESCRIPTION"]
| (., map(length*"-"))), (.[] | [.id, .name, .description])
| @tsv' | column -t
```

which produces output similar to:

```
ZONE  NAME         DESCRIPTION
----  ----         -----------
5     BizOffice
1     default
4     Inventory
2     Medications
3     Payroll
6     ProServ
```

<a href="#heading--add-a-zone"><h2 id="heading--add-a-zone">Add a zone</h2></a>

To create a zone, enter the following command:

```
maas $PROFILE zones create name=$ZONE_NAME description=$ZONE_DESCRIPTION
```

<a href="#heading--edit-a-zone"><h2 id="heading--edit-a-zone">Edit a zone</h2></a>

To edit a zone, enter a command similar to the following:

```
maas $PROFILE zone update $OLD_ZONE_NAME name=$NEW_ZONE_NAME \
description=$ZONE_DESCRIPTION
```

<a href="#heading--delete-a-zone"><h2 id="heading--delete-a-zone">Delete a zone</h2></a>

To delete a zone, enter a command like this:

```
maas $PROFILE zone delete $ZONE_NAME
```

<a href="#heading--assign-a-node-to-a-zone"><h2 id="heading--assign-a-node-to-a-zone">Assign a machine to a zone</h2></a>

To assign a machine to a zone, first retrieve the machine's system ID like this:

```
maas PROFILE machines read | jq '.[] | .hostname, .system_id'
```

Then enter the following command, using the system ID you just retrieved:

```
maas admin machine update $SYSTEM_ID zone=$ZONE_NAME
```

<a href="#heading--allocate-a-node-in-a-zone"><h2 id="heading--allocate-a-node-in-a-zone">Allocate a machine in a zone</h2></a>

To deploy in a particular zone, call the `acquire` method in the region-controller API &lt;region-controller-api&gt; as before, but pass the `zone` parameter with the name of the zone. This method will allocate a machine in that zone, or fail with an HTTP 409 ("conflict") error if the zone has no machines available that match your request.

Alternatively, you may want to request a machine that is not in a particular zone or one that is not in any of several zones. To do that, specify the `not_in_zone` parameter to `acquire`. This parameter takes a list of zone names; the allocated machine will not be in any of them. Again, if that leaves no machines available that match your request, the call will return a "conflict" error.

It is possible, though not usually useful, to combine the `zone` and `not_in_zone` parameters. If your choice for `zone` is also present in `not_in_zone`, no machine will ever match your request. Or if it's not, then the `not_in_zone` values will not affect the result of the call at all.
snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli  snap-3-0-cli deb-3-0-cli -->
