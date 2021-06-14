||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/storage-snap-2-7-cli/3102) ~ [UI](/t/storage-snap-2-7-ui/3103)|[CLI](/t/storage-snap-2-8-cli/3104) ~ [UI](/t/storage-snap-2-8-ui/3105)|[CLI](/t/storage-snap-2-9-cli/3106) ~ [UI](/t/storage-snap-2-9-ui/3107)|[CLI](/t/storage-snap-3-0-cli/4105) ~ [UI](/t/storage-snap-3-0-ui/4106)|
Packages|[CLI](/t/storage-deb-2-7-cli/3108) ~ [UI](/t/storage-deb-2-7-ui/3109)|[CLI](/t/storage-deb-2-8-cli/3110) ~ [UI](/t/storage-deb-2-8-ui/3111)|[CLI](/t/storage-deb-2-9-cli/3112) ~ [UI](/t/storage-deb-2-9-ui/3113)|[CLI](/t/storage-deb-3-0-cli/4107) ~ [UI](/t/storage-deb-3-0-ui/4108)|

You have significant latitude when choosing the final storage configuration of a deployed machine. MAAS supports traditional disk partitioning, as well as more complex options such as LVM, RAID, and bcache. MAAS also supports UEFI as a boot mechanism.  This article explains boot mechanisms and layouts, and offers some advice on how to configure layouts and manage storage.

#### Six questions you may have:

<!-- deb-2-7-cli
1. [How does UEFI booting work?](#heading--uefi)
2. [What kind of storage layouts are available?](#heading--layouts)
3. [How do I set global storage layouts?](#heading--setting-global-layouts)
4. [How do I set per-machine storage layouts?](#heading--per-machine-layouts)
5. [What storage modifications can I make at the filesystem level?](#heading--final-storage-modifications)
6. [How can I erase a disk?](/t/disk-erasure/2616)
 deb-2-7-cli -->

<!-- deb-2-7-ui
1. [How does UEFI booting work?](#heading--uefi)
2. [What kind of storage layouts are available?](#heading--layouts)
3. [How do I set global storage layouts?](#heading--setting-global-layouts)
4. [How do I set per-machine storage layouts?](#heading--per-machine-layouts)
5. [What storage modifications can I make at the filesystem level?](#heading--final-storage-modifications)
6. [How can I erase a disk?](/t/disk-erasure/2617)
 deb-2-7-ui -->

<!-- deb-2-8-cli
1. [How does UEFI booting work?](#heading--uefi)
2. [What kind of storage layouts are available?](#heading--layouts)
3. [How do I set global storage layouts?](#heading--setting-global-layouts)
4. [How do I set per-machine storage layouts?](#heading--per-machine-layouts)
5. [What storage modifications can I make at the filesystem level?](#heading--final-storage-modifications)
6. [How can I erase a disk?](/t/disk-erasure/2618)
 deb-2-8-cli -->

<!-- deb-2-8-ui
1. [How does UEFI booting work?](#heading--uefi)
2. [What kind of storage layouts are available?](#heading--layouts)
3. [How do I set global storage layouts?](#heading--setting-global-layouts)
4. [How do I set per-machine storage layouts?](#heading--per-machine-layouts)
5. [What storage modifications can I make at the filesystem level?](#heading--final-storage-modifications)
6. [How can I erase a disk?](/t/disk-erasure/2619)
 deb-2-8-ui -->

<!-- deb-2-9-cli
1. [How does UEFI booting work?](#heading--uefi)
2. [What kind of storage layouts are available?](#heading--layouts)
3. [How do I set global storage layouts?](#heading--setting-global-layouts)
4. [How do I set per-machine storage layouts?](#heading--per-machine-layouts)
5. [What storage modifications can I make at the filesystem level?](#heading--final-storage-modifications)
6. [How can I erase a disk?](/t/disk-erasure/2620)
 deb-2-9-cli -->

<!-- deb-2-9-ui
1. [How does UEFI booting work?](#heading--uefi)
2. [What kind of storage layouts are available?](#heading--layouts)
3. [How do I set global storage layouts?](#heading--setting-global-layouts)
4. [How do I set per-machine storage layouts?](#heading--per-machine-layouts)
5. [What storage modifications can I make at the filesystem level?](#heading--final-storage-modifications)
6. [How can I erase a disk?](/t/disk-erasure/2621)
 deb-2-9-ui -->

<!-- deb-3-0-cli
1. [How does UEFI booting work?](#heading--uefi)
2. [What kind of storage layouts are available?](#heading--layouts)
3. [How do I set global storage layouts?](#heading--setting-global-layouts)
4. [How do I set per-machine storage layouts?](#heading--per-machine-layouts)
5. [What storage modifications can I make at the filesystem level?](#heading--final-storage-modifications)
6. [How can I erase a disk?](/t/disk-erasure/3923)
 deb-3-0-cli -->

<!-- deb-3-0-ui
1. [How does UEFI booting work?](#heading--uefi)
2. [What kind of storage layouts are available?](#heading--layouts)
3. [How do I set global storage layouts?](#heading--setting-global-layouts)
4. [How do I set per-machine storage layouts?](#heading--per-machine-layouts)
5. [What storage modifications can I make at the filesystem level?](#heading--final-storage-modifications)
6. [How can I erase a disk?](/t/disk-erasure/3924)
 deb-3-0-ui -->

<!-- snap-2-7-cli
1. [How does UEFI booting work?](#heading--uefi)
2. [What kind of storage layouts are available?](#heading--layouts)
3. [How do I set global storage layouts?](#heading--setting-global-layouts)
4. [How do I set per-machine storage layouts?](#heading--per-machine-layouts)
5. [What storage modifications can I make at the filesystem level?](#heading--final-storage-modifications)
6. [How can I erase a disk?](/t/disk-erasure/2610)
 snap-2-7-cli -->

<!-- snap-2-7-ui
1. [How does UEFI booting work?](#heading--uefi)
2. [What kind of storage layouts are available?](#heading--layouts)
3. [How do I set global storage layouts?](#heading--setting-global-layouts)
4. [How do I set per-machine storage layouts?](#heading--per-machine-layouts)
5. [What storage modifications can I make at the filesystem level?](#heading--final-storage-modifications)
6. [How can I erase a disk?](/t/disk-erasure/2611)
 snap-2-7-ui -->

<!-- snap-2-8-cli
1. [How does UEFI booting work?](#heading--uefi)
2. [What kind of storage layouts are available?](#heading--layouts)
3. [How do I set global storage layouts?](#heading--setting-global-layouts)
4. [How do I set per-machine storage layouts?](#heading--per-machine-layouts)
5. [What storage modifications can I make at the filesystem level?](#heading--final-storage-modifications)
6. [How can I erase a disk?](/t/disk-erasure/2612)
 snap-2-8-cli -->

<!-- snap-2-8-ui
1. [How does UEFI booting work?](#heading--uefi)
2. [What kind of storage layouts are available?](#heading--layouts)
3. [How do I set global storage layouts?](#heading--setting-global-layouts)
4. [How do I set per-machine storage layouts?](#heading--per-machine-layouts)
5. [What storage modifications can I make at the filesystem level?](#heading--final-storage-modifications)
6. [How can I erase a disk?](/t/disk-erasure/2613)
 snap-2-8-ui -->

<!-- snap-2-9-cli
1. [How does UEFI booting work?](#heading--uefi)
2. [What kind of storage layouts are available?](#heading--layouts)
3. [How do I set global storage layouts?](#heading--setting-global-layouts)
4. [How do I set per-machine storage layouts?](#heading--per-machine-layouts)
5. [What storage modifications can I make at the filesystem level?](#heading--final-storage-modifications)
6. [How can I erase a disk?](/t/disk-erasure/2614)
 snap-2-9-cli -->

<!-- snap-2-9-ui
1. [How does UEFI booting work?](#heading--uefi)
2. [What kind of storage layouts are available?](#heading--layouts)
3. [How do I set global storage layouts?](#heading--setting-global-layouts)
4. [How do I set per-machine storage layouts?](#heading--per-machine-layouts)
5. [What storage modifications can I make at the filesystem level?](#heading--final-storage-modifications)
6. [How can I erase a disk?](/t/disk-erasure/2615)
 snap-2-9-ui -->

<!-- snap-3-0-cli
1. [How does UEFI booting work?](#heading--uefi)
2. [What kind of storage layouts are available?](#heading--layouts)
3. [How do I set global storage layouts?](#heading--setting-global-layouts)
4. [How do I set per-machine storage layouts?](#heading--per-machine-layouts)
5. [What storage modifications can I make at the filesystem level?](#heading--final-storage-modifications)
6. [How can I erase a disk?](/t/disk-erasure/3921)
 snap-3-0-cli -->

<!-- snap-3-0-ui
1. [How does UEFI booting work?](#heading--uefi)
2. [What kind of storage layouts are available?](#heading--layouts)
3. [How do I set global storage layouts?](#heading--setting-global-layouts)
4. [How do I set per-machine storage layouts?](#heading--per-machine-layouts)
5. [What storage modifications can I make at the filesystem level?](#heading--final-storage-modifications)
6. [How can I erase a disk?](/t/disk-erasure/3922)
 snap-3-0-ui -->

A machine's storage is dependant upon the underlying system's disks, but its configuration (i.e., disk usage) is the result of a storage template. In MAAS, this template is called a layout, and MAAS applies it to a machine during commissioning.  Once a layout is applied, a regular user can make modifications to a machine at the filesystem level to arrive at the machine's final storage configuration.  When a machine is no longer needed, a user can choose from among several disk erasure types before releasing it.

[note]
MAAS supports storage configuration for CentOS and RHEL deployments. Support includes RAID, LVM, and custom partitioning with different file systems (ZFS and bcache excluded). This support requires a newer version of Curtin, [available as a PPA](https://launchpad.net/ubuntu/+source/curtin).
[/note]

<a href="#heading--uefi"><h2 id="heading--uefi">UEFI</h2></a>

Every layout type supports a machine booting with UEFI. In such a case, MAAS automatically creates an EFI boot partition (`/boot/efi`). Other than setting the machine to boot from UEFI, the user does not need to take any additional action.

[note type="negative" status="Warning"]
UEFI must be enabled or disabled for the lifespan of the machine. For example, do not enlist a machine with UEFI enabled, and then disable it before commissioning. It won't work!
[/note]

The EFI partition, if created, will be the first partition (`sda1`) and will have a FAT32 filesystem with a size of 512 MB.

<a href="#heading--layouts"><h2 id="heading--layouts">Layouts</h2></a>

There are three layout types:

1.   Flat layout
2.   LVM layout
3.   bcache layout

The layout descriptions below will include the EFI partition. If your system is not using UEFI, regard `sda2` as `sda1` (with an additional 512 MB available to it).

<a href="#heading--flat-layout"><h3 id="heading--flat-layout">Flat layout</h3></a>

With the Flat layout, a partition spans the entire boot disk. The partition is formatted with the ext4 filesystem and uses the `/` mount point:

| Name | Size        | Type | Filesystem | Mount point |
|:-----|-------------|------|------------|-------------|
| sda  | -           | disk |            |             |
| sda1 | 512 MB      | part | FAT32      | /boot/efi   |
| sda2 | rest of sda | part | ext4       | /           |

The following three options are supported:

1. `boot_size`: Size of the boot partition on the boot disk. Default is 0, meaning not to create the boot partition. The '/boot' will be placed on the root filesystem.

2. `root_device`: The block device on which to place the root partition. The default is the boot disk.

3. `root_size`: Size of the root partition. Default is 100%, meaning the entire size of the root device.

<a href="#heading--lvm-layout"><h3 id="heading--lvm-layout">LVM layout</h3></a>

The LVM layout creates the volume group `vgroot` on a partition that spans the entire boot disk. A logical volume `lvroot` is created for the full size of the volume group; is formatted with the ext4 filesystem; and uses the `/` mount point:

| Name   | Size        | Type | Filesystem     | Mount point |
|:-------|-------------|------|----------------|-------------|
| sda    | -           | disk |                |             |
| sda1   | 512 MB      | part | FAT32          | /boot/efi   |
| sda2   | rest of sda | part | lvm-pv(vgroot) |             |
| lvroot | rest of sda | lvm  | ext4           | /           |
| vgroot | rest of sda | lvm  |                |             |

The following six options are supported:

1. `boot_size`: Size of the boot partition on the boot disk. Default is 0, meaning not to create the boot partition. The '/boot' will be placed on the root filesystem.
2. `root_device`: The block device on which to place the root partition. The default is the boot disk.
3. `root_size`: Size of the root partition. Default is 100%, meaning the entire size of the root device.
4. `vg_name`: Name of the created volume group. Default is `vgroot`.
5. `lv_name`: Name of the created logical volume. Default is `lvroot`.
6. `lv_size`: Size of the created logical volume. Default is 100%, meaning the entire size of the volume group.

<a href="#heading--bcache-layout"><h3 id="heading--bcache-layout">bcache layout</h3></a>

A bcache layout will create a partition that spans the entire boot disk as the backing device. It uses the smallest block device tagged with 'ssd' as the cache device. The bcache device is formatted with the ext4 filesystem and uses the `/` mount point. If there are no 'ssd' tagged block devices on the machine, then the bcache device will not be created, and the Flat layout will be used instead:

| Name      | Size        | Type | Filesystem | Mount point |
|:----------|-------------|------|------------|-------------|
| sda       | -           | disk |            |             |
| sda1      | 512 MB      | part | FAT32      | /boot/efi   |
| sda2      | rest of sda | part | bc-backing |             |
| sdb (ssd) | -           | disk |            |             |
| sdb1      | 100% of sdb | part | bc-cache   |             |
| bcache0   | per sda2    | disk | ext4       | /           |

The following seven options are supported:

1. `boot_size`: Size of the boot partition on the boot disk. Default is 0, meaning not to create the boot partition. The '/boot' will be placed on the root filesystem.
2. `root_device`: The block device upon which to place the root partition. The default is the boot disk.
3. `root_size`: Size of the root partition. Default is 100%, meaning the entire size of the root device.
4. `cache_device`: The block device to use as the cache device. Default is the smallest block device tagged ssd.
5. `cache_mode`: The cache mode to which MAAS should set the created bcache device. The default is `writethrough`.
6. `cache_size`: The size of the partition on the cache device. Default is 100%, meaning the entire size of the cache device.
7. `cache_no_part`: Whether or not to create a partition on the cache device. Default is false, meaning to create a partition using the given `cache_size`. If set to true, no partition will be created, and the raw cache device will be used as the cache.

<a href="#heading--vmfs6-layout"><h3 id="heading--vmfs6-layout">VMFS6 layout</h3></a>

The VMFS6 layout is used for VMware ESXi deployments only. It is required when configuring VMware VMFS Datastores. This layout creates all operating system partitions, in addition to the default datastore. The datastore may be modified.  New datastores may be created or extended to include other storage devices. The base operating system partitions may not be modified because VMware ESXi requires them. Once applied another storage layout must be applied to remove the operating system partitions.

| Name | Size      | Type    | Use               |
|:-----|-----------|---------|-------------------|
| sda  | -         | disk    |                   |
| sda1 | 3 MB      | part    | EFI               |
| sda2 | 4 GB      | part    | Basic Data        |
| sda3 | Remaining | part    | VMFS Datastore 1  |
| sda4 | -         | skipped |                   |
| sda5 | 249 MB    | part    | Basic Data        |
| sda6 | 249 MB    | part    | Basic Data        |
| sda7 | 109 MB    | part    | VMware Diagnostic |
| sda8 | 285 MB    | part    | Basic Data        |
| sda9 | 2.5 GB    | part    | VMware Diagnostic |

The following options are supported:

1. `root_device`: The block device upon which to place the root partition. Default is the boot disk.

2. `root_size`: Size of the default VMFS Datastore. Default is 100%, meaning the remaining size of the root disk.

<a href="#heading--blank-layout"><h3 id="heading--blank-layout">Blank layout</h3></a>

The blank layout removes all storage configuration from all storage devices. It is useful when needing to apply a custom storage configuration.

[note type="negative" status="Warning"]
Machines with the blank layout applied are not deployable; you must first configure storage manually.
[/note]

<a href="#heading--setting-global-layouts"><h2 id="heading--setting-global-layouts">Setting layouts</h2></a>

Layouts can be set globally and on a per-machine basis.

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
All machines will have a default layout applied when commissioned. An administrator can configure the default layout on the 'Settings' page, under the 'Storage' tab.

<a href="https://discourse.maas.io/uploads/default/original/1X/80de3bc701552cd00bec707830accf380c214b17.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/80de3bc701552cd00bec707830accf380c214b17.png"></a>
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui  -->

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 
All machines will have a default layout applied when commissioned. To set the default storage layout for all machines:

```
maas $PROFILE maas set-config name=default_storage_layout value=$LAYOUT_TYPE
```

For example, to set the default layout to Flat:

```
maas $PROFILE maas set-config name=default_storage_layout value=flat
```

Important: The new default will only apply to newly-commissioned machines.

snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli -->

[note type="caution" status="Important"]
The new default will only apply to newly-commissioned machines.
[/note]

<a href="#heading--per-machine-layouts"><h3 id="heading--per-machine-layouts">Machine layout</h3></a>

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
An administrator can change the layout for a single machine as well as customise that layout providing this is done while the machine has a status of 'Ready'. This is only possible via the CLI: to see how, click the "CLI" option for your version and delivery method above.
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui  -->

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 
An administrator can set a storage layout for a machine with a status of ‘Ready’ like this:

```
maas $PROFILE machine set-storage-layout $SYSTEM_ID storage_layout=$LAYOUT_TYPE [$OPTIONS]
```

For example, to set an LVM layout where the logical volume has a size of 5 GB:

```
maas $PROFILE machine set-storage-layout $SYSTEM_ID storage_layout=lvm lv_size=5368709120

```
You must specify all storage sizes in bytes.

This action will remove the configuration that may exist on any block device.
snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli -->

[note]
Only an administrator can modify storage at the block device level (providing the machine has a status of 'Ready').
[/note]

<a href="#heading--final-storage-modifications"><h2 id="heading--final-storage-modifications">Final storage modifications</h2></a>

Once MAAS provisions a machine with block devices, via a layout or administrator customisation, a regular user can modify the resulting storage configuration at the filesystem level.
