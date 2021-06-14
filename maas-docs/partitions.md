||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/partitions-snap-2-7-cli/2982) ~ [UI](/t/partitions-snap-2-7-ui/2983)|[CLI](/t/partitions-snap-2-8-cli/2984) ~ [UI](/t/partitions-snap-2-8-ui/2985)|[CLI](/t/partitions-snap-2-9-cli/2986) ~ [UI](/t/partitions-snap-2-9-ui/2987)|[CLI](/t/partitions-snap-3-0-cli/4061) ~ [UI](/t/partitions-snap-3-0-ui/4062)|
Packages|[CLI](/t/partitions-deb-2-7-cli/2988) ~ [UI](/t/partitions-deb-2-7-ui/2989)|[CLI](/t/partitions-deb-2-8-cli/2990) ~ [UI](/t/partitions-deb-2-8-ui/2991)|[CLI](/t/partitions-deb-2-9-cli/2992) ~ [UI](/t/partitions-deb-2-9-ui/2993)|[CLI](/t/partitions-deb-3-0-cli/4063) ~ [UI](/t/partitions-deb-3-0-ui/4064)|

<!-- deb-2-7-cli
As with block devices (see [Block devices](/t/block-devices/2352)), MAAS and the MAAS API offer a great deal of control over the creation, formatting, mounting and deletion of partitions.
 deb-2-7-cli -->

<!-- deb-2-7-ui
As with block devices (see [Block devices](/t/block-devices/2353)), MAAS and the MAAS API offer a great deal of control over the creation, formatting, mounting and deletion of partitions.
 deb-2-7-ui -->

<!-- deb-2-8-cli
As with block devices (see [Block devices](/t/block-devices/2354)), MAAS and the MAAS API offer a great deal of control over the creation, formatting, mounting and deletion of partitions.
 deb-2-8-cli -->

<!-- deb-2-8-ui
As with block devices (see [Block devices](/t/block-devices/2355)), MAAS and the MAAS API offer a great deal of control over the creation, formatting, mounting and deletion of partitions.
 deb-2-8-ui -->

<!-- deb-2-9-cli
As with block devices (see [Block devices](/t/block-devices/2356)), MAAS and the MAAS API offer a great deal of control over the creation, formatting, mounting and deletion of partitions.
 deb-2-9-cli -->

<!-- deb-2-9-ui
As with block devices (see [Block devices](/t/block-devices/2357)), MAAS and the MAAS API offer a great deal of control over the creation, formatting, mounting and deletion of partitions.
 deb-2-9-ui -->

<!-- deb-3-0-cli
As with block devices (see [Block devices](/t/block-devices/3843)), MAAS and the MAAS API offer a great deal of control over the creation, formatting, mounting and deletion of partitions.
 deb-3-0-cli -->

<!-- deb-3-0-ui
As with block devices (see [Block devices](/t/block-devices/3844)), MAAS and the MAAS API offer a great deal of control over the creation, formatting, mounting and deletion of partitions.
 deb-3-0-ui -->

<!-- snap-2-7-cli
As with block devices (see [Block devices](/t/block-devices/2346)), MAAS and the MAAS API offer a great deal of control over the creation, formatting, mounting and deletion of partitions.
 snap-2-7-cli -->

<!-- snap-2-7-ui
As with block devices (see [Block devices](/t/block-devices/2347)), MAAS and the MAAS API offer a great deal of control over the creation, formatting, mounting and deletion of partitions.
 snap-2-7-ui -->

<!-- snap-2-8-cli
As with block devices (see [Block devices](/t/block-devices/2348)), MAAS and the MAAS API offer a great deal of control over the creation, formatting, mounting and deletion of partitions.
 snap-2-8-cli -->

<!-- snap-2-8-ui
As with block devices (see [Block devices](/t/block-devices/2349)), MAAS and the MAAS API offer a great deal of control over the creation, formatting, mounting and deletion of partitions.
 snap-2-8-ui -->

<!-- snap-2-9-cli
As with block devices (see [Block devices](/t/block-devices/2350)), MAAS and the MAAS API offer a great deal of control over the creation, formatting, mounting and deletion of partitions.
 snap-2-9-cli -->

<!-- snap-2-9-ui
As with block devices (see [Block devices](/t/block-devices/2351)), MAAS and the MAAS API offer a great deal of control over the creation, formatting, mounting and deletion of partitions.
 snap-2-9-ui -->

<!-- snap-3-0-cli
As with block devices (see [Block devices](/t/block-devices/3841)), MAAS and the MAAS API offer a great deal of control over the creation, formatting, mounting and deletion of partitions.
 snap-3-0-cli -->

<!-- snap-3-0-ui
As with block devices (see [Block devices](/t/block-devices/3842)), MAAS and the MAAS API offer a great deal of control over the creation, formatting, mounting and deletion of partitions.
 snap-3-0-ui -->


<a href="#heading--list-partitions"><h3 id="heading--list-partitions">List Partitions</h3></a>

To view all the partitions on a block device, use the 'partitions read' API call:

``` bash
maas admin partitions read <node-id> 10
```

``` nohighlight
Success.
Machine-readable output follows:
[
    {
        "bootable": false,
        "id": 9,
        "resource_uri":
"/MAAS/api/2.0/nodes/4y3h8a/blockdevices/10/partition/9",
        "path": "/dev/disk/by-dname/vda-part1",
        "uuid": "aae082cd-8be0-4a64-ab49-e998abd6ea43",
        "used_for": "LVM volume for vgroot",
        "size": 5360320512,
        "type": "partition",
        "filesystem": {
            "uuid": "a56ebfa6-8ef4-48b5-b6bc-9f9d27065d24",
            "mount_options": null,
            "label": null,
            "fstype": "lvm-pv",
            "mount_point": null
        }
    }
]
```

To view the metadata for a specific partition on a block device, rather than all partitions, use the singular 'partition' API call with an endpoint:

``` bash
maas admin partition read <node-id> 10 9
```

<a href="#heading--create-partition"><h3 id="heading--create-partition">Create Partition</h3></a>

To create a new partition on a block device, use the 'create' API call:

``` bash
maas admin partitions create <node-id> 10 size=5360320512
```

In addition to bytes, as shown above, the 'size' of a partition can also be defined with a 'G' for gigabytes or 'M' for megabytes. The output from the previous command will look like this:

``` nohighlight
Success.
Machine-readable output follows:
{
    "bootable": false,
    "path": "/dev/disk/by-dname/vda-part1",
    "filesystem": null,
    "used_for": "Unused",
    "type": "partition",
    "id": 10,
    "size": 5360320512,
    "resource_uri": "/MAAS/api/2.0/nodes/4y3h8a/blockdevices/10/partition/10",
    "uuid": "3d32adbf-9943-4785-ab38-963758338c6c"
}
```

<a href="#heading--delete-partition"><h3 id="heading--delete-partition">Delete Partition</h3></a>

Partitions can be deleted from a block device with the 'delete' API call. Make sure you double check the partition details as the partition is deleted immediately, with no further confirmation:

``` bash
maas admin partition delete <node-id> 10 9
```

Successful output from the 'delete' command will look like this:

``` bash
Success.
Machine-readable output follows:
```

<a href="#heading--format-partition"><h3 id="heading--format-partition">Format Partition</h3></a>

Partitions can be formatted in a similar way to block devices:

``` bash
maas admin partition format <node-id> 10 9 fstype=ext4
```

The output from the 'format' command will be similar to the following:

``` nohighlight
Success.
Machine-readable output follows:
{
    "id": 9,
    "used_for": "Unmounted ext4 formatted filesystem",
    "resource_uri": "/MAAS/api/2.0/nodes/4y3h8a/blockdevices/10/partition/9",
    "path": "/dev/disk/by-dname/vda-part1",
    "uuid": "aae082cd-8be0-4a64-ab49-e998abd6ea43",
    "size": 5360320512,
    "bootable": false,
    "type": "partition",
    "filesystem": {
        "uuid": "ea593366-be43-4ea3-b2d5-0adf82085a62",
        "mount_point": null,
        "mount_options": null,
        "fstype": "ext4",
        "label": ""
    }
}
```

[note]
You cannot format partitions that are used to make another virtual block device.
[/note]

<a href="#heading--unformat-partition"><h3 id="heading--unformat-partition">Unformat Partition</h3></a>

You can also remove the filesystem from a partition with the 'unformat' API call:

``` bash
maas admin partition unformat <node-id> 10 10 fstype=ext4
```

``` nohighlight
Success.
Machine-readable output follows:
{
    "bootable": false,
    "path": "/dev/disk/by-dname/vda-part1",
    "filesystem": null,
    "used_for": "Unused",
    "type": "partition",
    "id": 10,
    "size": 5360320512,
    "resource_uri": "/MAAS/api/2.0/nodes/4y3h8a/blockdevices/10/partition/10",
    "uuid": "3d32adbf-9943-4785-ab38-963758338c6c"
}
```

<a href="#heading--mount-partition"><h3 id="heading--mount-partition">Mount Partition</h3></a>

A formatted partition can be mounted at a given mount point with the 'mount' command.

``` bash
maas admin partition mount <node-id> 10 10 mount_point=/srv
```

The mount point and the filesystem is visible in the output from the command:

``` nohighlight
Success.
Machine-readable output follows:
{
    "bootable": false,
    "id": 10,
    "resource_uri": "/MAAS/api/2.0/nodes/4y3h8a/blockdevices/10/partition/10",
    "path": "/dev/disk/by-dname/vda-part1",
    "uuid": "3d32adbf-9943-4785-ab38-963758338c6c",
    "used_for": "ext4 formatted filesystem mounted at /srv",
    "size": 5360320512,
    "type": "partition",
    "filesystem": {
        "uuid": "1949a5fb-f7bd-4ada-8ba5-d06d3f5857a8",
        "mount_options": "",
        "label": "",
        "fstype": "ext4",
        "mount_point": "/srv"
    }
}
```

<a href="#heading--unmount-partition"><h3 id="heading--unmount-partition">Unmount Partition</h3></a>

A previous mounted partition can be unmounted with the 'unmount' command:

``` bash
maas admin partition unmount 4y3h8a 10 10
```

After successfully running this command, the mount point will show as 'null' in the output:

``` nohighlight
Success.
Machine-readable output follows:
{
    "bootable": false,
    "id": 10,
    "resource_uri": "/MAAS/api/2.0/nodes/4y3h8a/blockdevices/10/partition/10",
    "path": "/dev/disk/by-dname/vda-part1",
    "uuid": "3d32adbf-9943-4785-ab38-963758338c6c",
    "used_for": "Unmounted ext4 formatted filesystem",
    "size": 5360320512,
    "type": "partition",
    "filesystem": {
        "uuid": "1949a5fb-f7bd-4ada-8ba5-d06d3f5857a8",
        "mount_options": null,
        "label": "",
        "fstype": "ext4",
        "mount_point": null
    }
    "type": "partition",
    "id": 3,
    "size": 2000003072
}
```

<a href="#heading--restrictions"><h2 id="heading--restrictions">Restrictions</h2></a>

There are three restrictions for the storage configuration:

1.   An EFI partition is required to be on the boot disk for UEFI.
2.   You cannot place partitions on logical volumes.
3.   You cannot use a logical volume as a Bcache backing device.

Violating these restrictions will prevent a successful deployment.
