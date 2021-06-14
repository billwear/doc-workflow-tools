||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/vm-host-storage-pools-snap-2-7-cli/3222) ~ [UI](/t/vm-host-storage-pools-snap-2-7-ui/3223)|[CLI](/t/vm-host-storage-pools-snap-2-8-cli/3224) ~ [UI](/t/vm-host-storage-pools-snap-2-8-ui/3225)|[CLI](/t/vm-host-storage-pools-snap-2-9-cli/3226) ~ [UI](/t/vm-host-storage-pools-snap-2-9-ui/3227)|[CLI](/t/vm-host-storage-pools-snap-3-0-cli/4169) ~ [UI](/t/vm-host-storage-pools-snap-3-0-ui/4170)|
Packages|[CLI](/t/vm-host-storage-pools-deb-2-7-cli/3228) ~ [UI](/t/vm-host-storage-pools-deb-2-7-ui/3229)|[CLI](/t/vm-host-storage-pools-deb-2-8-cli/3230) ~ [UI](/t/vm-host-storage-pools-deb-2-8-ui/3231)|[CLI](/t/vm-host-storage-pools-deb-2-9-cli/3232) ~ [UI](/t/vm-host-storage-pools-deb-2-9-ui/3233)|[CLI](/t/vm-host-storage-pools-deb-3-0-cli/4171) ~ [UI](/t/vm-host-storage-pools-deb-3-0-ui/4172)|

"Storage pools” are storage resources managed by a VM host. A storage pool is a given amount of storage set aside for use by VMs. A pool can be organised into storage volumes, assigned to VMs as individual block devices. More information is available for both [libvirt](https://libvirt.org/storage.html) and [LXD](https://lxd.readthedocs.io/en/latest/storage/) storage pools.

[note]
For LXD VM hosts, each VM can be assigned a single block device from the storage pool.
[/note]

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
The MAAS web UI displays information about each VM host's storage pools so you can understand your resource usage at a glance:

<a href="https://discourse.maas.io/uploads/default/original/1X/3387f256f9bd02f7fc2079f119377305256973c8.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/3387f256f9bd02f7fc2079f119377305256973c8.jpeg"></a>
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui  snap-3-0-ui deb-3-0-ui -->

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 
Retrieve VM host storage pool information with the following command:

```
maas $PROFILE vm-host read $VM_HOST_ID
```

or, to get tabular output, try:

```
maas admin vm-host read 5 \
| jq -r '(["NAME","TYPE","PATH","TOTAL","USED","AVAIL"]) 
| (,. map(length*"-"))), (.storage_pools[] 
| [.name, .type, .path, .total, used, .available]) | @tsv' \
| column -t
```

snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli  snap-3-0-cli deb-3-0-cli -->
