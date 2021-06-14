||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/creating-and-deleting-vms-snap-2-7-cli/2574) ~ [UI](/t/creating-and-deleting-vms-snap-2-7-ui/2575)|[CLI](/t/creating-and-deleting-vms-snap-2-8-cli/2576) ~ [UI](/t/creating-and-deleting-vms-snap-2-8-ui/2577)|[CLI](/t/creating-and-deleting-vms-snap-2-9-cli/2578) ~ [UI](/t/creating-and-deleting-vms-snap-2-9-ui/2579)|[CLI](/t/creating-and-deleting-vms-snap-3-0-cli/3905) ~ [UI](/t/creating-and-deleting-vms-snap-3-0-ui/3906)|
Packages|[CLI](/t/creating-and-deleting-vms-deb-2-7-cli/2580) ~ [UI](/t/creating-and-deleting-vms-deb-2-7-ui/2581)|[CLI](/t/creating-and-deleting-vms-deb-2-8-cli/2582) ~ [UI](/t/creating-and-deleting-vms-deb-2-8-ui/2583)|[CLI](/t/creating-and-deleting-vms-deb-2-9-cli/2584) ~ [UI](/t/creating-and-deleting-vms-deb-2-9-ui/2585)|[CLI](/t/creating-and-deleting-vms-deb-3-0-cli/3907) ~ [UI](/t/creating-and-deleting-vms-deb-3-0-ui/3908)|

If you have already created a VM host, you will want to create and delete virtual machines (VMs); this article explains how to do so.

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 

#### Three questions you may have:

1. [How do LXD projects work?](https://ubuntu.com/tutorials/introduction-to-lxd-projects#1-overview)
2. [How do I add a VM?](#heading--add-vm-from-ui)
3. [How do I delete a VM?](#heading--delete-a-machine)

<a href="#heading--add-vm-from-ui"><h2 id="heading--add-vm-from-ui">Adding a VM from the Web UI</h2></a>

While on VM host's details view, select 'Compose' from the 'Take action' drop-down menu to compose a machine.

<a href="https://discourse.maas.io/uploads/default/original/1X/937726bb839eefb28e9297e8f97bd48556c1014c.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/937726bb839eefb28e9297e8f97bd48556c1014c.jpeg"></a> 

You can choose which storage pool to use from a drop-down list. 

Click the 'Compose machine' button when you're finished. MAAS will present the VM host detail view. In a few moments, your new machine will be auto-commissioned. The 'Machines' page will reflect this as well.

MAAS will deduct the new machine's resources from the VM host's resources:

<a href="https://discourse.maas.io/uploads/default/original/1X/3b621ab0e7b4f6a86963d2b7c50b677b815956ab.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/3b621ab0e7b4f6a86963d2b7c50b677b815956ab.jpeg"></a> 

<a href="#heading--delete-a-machine"><h2 id="heading--delete-a-machine">Deleting a VM from the Web UI</h2></a>

To delete a VM, delete it as you would any other MAAS machine. Select the desired machine from the list of machines and select 'Delete' from the 'Take Action' menu.

<a href="https://discourse.maas.io/uploads/default/original/1X/34d3f5fcd8a86bfa827bab5383209ea9ca117f50.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/34d3f5fcd8a86bfa827bab5383209ea9ca117f50.jpeg"></a> 
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui  snap-3-0-ui deb-3-0-ui -->

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 

#### Eight questions you may have:

1. [How do I add a VM?](#heading--adding-a-vm-from-the-cli)
2. [How do LXD projects work?](https://ubuntu.com/tutorials/introduction-to-lxd-projects#1-overview)
3. [How do I set resources while adding a VM?](#heading--set-resources)
4. [How do I set the architecture while adding a VM?](#heading--architecture)
5. [How do I set storage while adding a VM?](#heading--storage)
6. [How do I specify interfaces while adding a VM?](#heading--interfaces)
7. [How do I find a VM host ID?](#heading--find-vm-host-ids)
8. [How do I delete a VM?](#heading--delete-a-vm)

<a href="#heading--adding-a-vm-from-the-cli"><h2 id="heading--adding-a-vm-from-the-cli">Adding a VM from the CLI</h2></a>

To compose a basic VM:

    maas $PROFILE vm-host compose $VM_HOST_ID

Example output for default composing:

    {
        "system_id": "73yxmc",
        "resource_uri": "/MAAS/api/2.0/machines/73yxmc/"
    }

<a href="#heading--set-resources"><h3 id="heading--set-resources">Set resources while adding a VM</h3></a>

Compose with resources specified:

    maas $PROFILE vm-host compose $VM_HOST_ID $RESOURCES

Where $RESOURCES is a space-separated list of six constraints:

1. *cores=* requested cores
2. *cpu_speed=* requested minimum cpu speed in MHz
3. *memory=* requested memory in MB
4. *architecture=* See [Architecture](#heading--architecture) below 
5. *storage=* See [Storage](#heading--storage) below
6. *interfaces=* See [Interfaces](#heading--interfaces) below

<a href="#heading--architecture"><h3 id="heading--architecture">Setting the architecture while adding a VM</h3></a>

To list available architectures:

    maas $PROFILE boot-resources read

Then, for example:

    maas $PROFILE vm-host compose $VM_HOST_ID \
        cores=40 cpu_speed=2000 memory=7812 architecture="amd64/generic"

<a href="#heading--storage"><h3 id="heading--storage">Setting storage parameters while adding a VM</h3></a>


Storage parameters look like this:

    storage="<label>:<size in GB>(<storage pool name>),<label>:<size in GB>(<storage pool name>)"

For example, let's examine how to compose a machine with the following two disks:

1.   32 GB disk from storage pool `pool1`
2.   64 GB disk from storage pool `pool2`

where we want the first disk to be a bootable root partition `/` and the second to be a home directory.

First, create the VM:

    maas $PROFILE vm-host compose $VM_HOST_ID "storage=mylabel:32(pool1),mylabel:64(pool2)"

Note that the labels, here `mylabel`, are an ephemeral convenience that you might find useful in scripting MAAS actions.

MAAS will create a VM with 2 disks, `/dev/vda` (32 GB) and `/dev/vdb` (64 GB). After MAAS enlists, commissions and acquires the machine, you can edit the disks before deploying to suit your needs. For example, we'll set a boot, root, and home partition.

We'll start by deleting the `/` partition MAAS created because we want a separate `/boot` partition to demonstrate how yo.

    maas admin partition delete $VM_HOST_ID $DISK1_ID $PARTITION_ID

[note]
To find `$DISK1_ID` and `$PARTITION_ID`, use `maas admin machine read $VM_HOST_ID`.
[/note]

Now, create a boot partition (~512MB):

    maas admin partitions create $VM_HOST_ID $DISK1_ID size=512000000 bootable=True

We'll use the remaining space for the root partition, so create another without specifying size:

    maas admin partitions create $VM_HOST_ID $DISK1_ID

Finally, create a partition to use as the home directory. Here we'll use the entire space:

    maas admin partitions create $VM_HOST_ID $DISK2_ID

[note]
To find `$DISK2_ID`, use `maas admin machine read $VM_HOST_ID`.
[/note]

Now, format the partitions. This requires three commands:

    maas admin partition format $VM_HOST_ID $DISK1_ID $BOOT_PARTITION_ID fstype=ext2
    maas admin partition format $VM_HOST_ID $DISK1_ID $ROOT_PARTITION_ID fstype=ext4
    maas admin partition format $VM_HOST_ID $DISK2_ID $HOME_PARTITION_ID fstype=ext4

[note]
To find the partition IDs, use `maas admin partitions read $VM_HOST_ID $DISK1_ID` and `maas admin partitions read $VM_HOST_ID $DISK2_ID`
[/note]

Before you can deploy the machine with our partition layout, you need to mount the new partitions. Here, we'll do that in three commands:

    maas admin partition mount $SYSTEM_ID $DISK1_ID $BOOT_PARTITION_ID     "mount_point=/boot"
    maas admin partition mount $SYSTEM_ID $DISK1_ID $ROOT_PARTITION_ID "mount_point=/"
    maas admin partition mount $SYSTEM_ID $DISK2_ID $HOME_PARTITION_ID "mount_point=/home"

Finally, we deploy the machine. MAAS will use the partitions as we have defined them, similar to a normal Ubuntu desktop install:

    maas admin machine deploy $SYSTEM_ID

<a href="#heading--interfaces"><h3 id="heading--interfaces">Specifying interfaces while adding a VM</h3></a>

Using the `interfaces` constraint, you can compose virtual machines with interfaces, allowing the selection of VM host NICs.

If you don't specify an `interfaces` constraint, MAAS maintains backward compatibility by checking for a `maas` network, then a `default` network to which to connect the virtual machine.

If you specify an `interfaces` constraint, MAAS creates a `bridge` or `macvlan` attachment to the networks that match the given constraint. MAAS prefers `bridge` interface attachments when possible since this typically results in successful communication.

Consider the following interfaces constraint:

    interfaces=eth0:space=maas;eth1:space=storage

Assuming you deploy the VM host on a machine or controller with access to the `maas` and `storage` [spaces](/t/concepts-and-terms/785#heading--spaces), MAAS will create an `eth0` interface bound to the `maas` space and an `eth1` interface bound to the `storage` space.

Another example tells MAAS to assign unallocated IP addresses:

    interfaces=eth0:ip=172.16.99.42

MAAS automatically converts the `ip` constraint to a VLAN constraint (matching the VLAN which corresponds to the subnet can be found -- e.g. `172.16.99.0/24`.) and assigns the IP address to the newly-composed machine upon allocation.

See the Machines [MAAS API documentation](https://maas.io/docs/api#machines) for a list of all constraint keys.

<a href="#heading--find-vm-host-ids"><h3 id="heading--find-vm-host-ids">Find VM host IDs</h3></a>

Here's a simple way to find a VM host's ID by name using `jq`:

    maas $PROFILE vm-hosts read | jq '.[] | select (.name=="MyVMHost") | .name, .id'

Example output:

    "MyVMHost"
    1

<a href="#heading--delete-a-vm"><h2 id="heading--delete-a-vm">Deleting a VM with the CLI</h2></a>

    maas $PROFILE machine delete $SYSTEM_ID

After you delete a machine, its resources will be available for other VMs.
snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli  snap-3-0-cli deb-3-0-cli -->
