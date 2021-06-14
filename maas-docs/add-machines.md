||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/add-machines-snap-2-7-cli/2274) ~ [UI](/t/add-machines-snap-2-7-ui/2275)|[CLI](/t/add-machines-snap-2-8-cli/2276) ~ [UI](/t/add-machines-snap-2-8-ui/2277)|[CLI](/t/add-machines-snap-2-9-cli/2278) ~ [UI](/t/add-machines-snap-2-9-ui/2279)|[CLI](/t/add-machines-snap-3-0-cli/3821) ~ [UI](/t/add-machines-snap-3-0-ui/3822)|
Packages|[CLI](/t/add-machines-deb-2-7-cli/2280) ~ [UI](/t/add-machines-deb-2-7-ui/2281)|[CLI](/t/add-machines-deb-2-8-cli/2282) ~ [UI](/t/add-machines-deb-2-8-ui/2283)|[CLI](/t/add-machines-deb-2-9-cli/2284) ~ [UI](/t/add-machines-deb-2-9-ui/2285)|[CLI](/t/add-machines-deb-3-0-cli/3823) ~ [UI](/t/add-machines-deb-3-0-ui/3824)|

There are two ways to add a machine to MAAS:

1. If you place the machine on a connected network, and the machine is configured to netboot, MAAS will automatically enlist it.
2. If you add a machine manually, MAAS will automatically commission it.

This article will explain more about both methods.

#### Four or five questions you may have:

<!-- deb-2-7-cli
1. [How does enlistment work?](#heading--enlistment)
2. [How do VM host nodes work?](/t/introduction-to-vm-hosting/2748)
3. [How do I add virtual machines?](/t/adding-a-vm-host/2292)
4. [How do I add a machine manually?](#heading--add-a-node-manually)
 deb-2-7-cli -->

<!-- deb-2-7-ui
1. [How does enlistment work?](#heading--enlistment)
2. [How do VM host nodes work?](/t/introduction-to-vm-hosting/2749)
3. [How do I add virtual machines?](/t/adding-a-vm-host/2293)
4. [How do I add a machine manually?](#heading--add-a-node-manually)
5. [How do I add a machine via a chassis?](#heading--add-nodes-via-a-chassis)
 deb-2-7-ui -->

<!-- deb-2-8-cli
1. [How does enlistment work?](#heading--enlistment)
2. [How do VM host nodes work?](/t/introduction-to-vm-hosting/2750)
3. [How do I add virtual machines?](/t/adding-a-vm-host/2294)
4. [How do I add a machine manually?](#heading--add-a-node-manually)
 deb-2-8-cli -->

<!-- deb-2-8-ui
1. [How does enlistment work?](#heading--enlistment)
2. [How do VM host nodes work?](/t/introduction-to-vm-hosting/2751)
3. [How do I add virtual machines?](/t/adding-a-vm-host/2295)
4. [How do I add a machine manually?](#heading--add-a-node-manually)
5. [How do I add a machine via a chassis?](#heading--add-nodes-via-a-chassis)
 deb-2-8-ui -->

<!-- deb-2-9-cli
1. [How does enlistment work?](#heading--enlistment)
2. [How do VM host nodes work?](/t/introduction-to-vm-hosting/2752)
3. [How do I add virtual machines?](/t/adding-a-vm-host/2296)
4. [How do I add a machine manually?](#heading--add-a-node-manually)
 deb-2-9-cli -->

<!-- deb-2-9-ui
1. [How does enlistment work?](#heading--enlistment)
2. [How do VM host nodes work?](/t/introduction-to-vm-hosting/2753)
3. [How do I add virtual machines?](/t/adding-a-vm-host/2297)
4. [How do I add a machine manually?](#heading--add-a-node-manually)
5. [How do I add a machine via a chassis?](#heading--add-nodes-via-a-chassis)
 deb-2-9-ui -->

<!-- deb-3-0-cli
1. [How does enlistment work?](#heading--enlistment)
2. [How do VM host nodes work?](/t/introduction-to-vm-hosting/4163)
3. [How do I add virtual machines?](/t/adding-a-vm-host/3819)
4. [How do I add a machine manually?](#heading--add-a-node-manually)
 deb-3-0-cli -->

<!-- deb-3-0-ui
1. [How does enlistment work?](#heading--enlistment)
2. [How do VM host nodes work?](/t/introduction-to-vm-hosting/4164)
3. [How do I add virtual machines?](/t/adding-a-vm-host/3820)
4. [How do I add a machine manually?](#heading--add-a-node-manually)
5. [How do I add a machine via a chassis?](#heading--add-nodes-via-a-chassis)
 deb-3-0-ui -->

<!-- snap-2-7-cli
1. [How does enlistment work?](#heading--enlistment)
2. [How do VM host nodes work?](/t/introduction-to-vm-hosting/2742)
3. [How do I add virtual machines?](/t/adding-a-vm-host/2286)
4. [How do I add a machine manually?](#heading--add-a-node-manually)
 snap-2-7-cli -->

<!-- snap-2-7-ui
1. [How does enlistment work?](#heading--enlistment)
2. [How do VM host nodes work?](/t/introduction-to-vm-hosting/2743)
3. [How do I add virtual machines?](/t/adding-a-vm-host/2287)
4. [How do I add a machine manually?](#heading--add-a-node-manually)
5. [How do I add a machine via a chassis?](#heading--add-nodes-via-a-chassis)
 snap-2-7-ui -->

<!-- snap-2-8-cli
1. [How does enlistment work?](#heading--enlistment)
2. [How do VM host nodes work?](/t/introduction-to-vm-hosting/2744)
3. [How do I add virtual machines?](/t/adding-a-vm-host/2288)
4. [How do I add a machine manually?](#heading--add-a-node-manually)
 snap-2-8-cli -->

<!-- snap-2-8-ui
1. [How does enlistment work?](#heading--enlistment)
2. [How do VM host nodes work?](/t/introduction-to-vm-hosting/2745)
3. [How do I add virtual machines?](/t/adding-a-vm-host/2289)
4. [How do I add a machine manually?](#heading--add-a-node-manually)
5. [How do I add a machine via a chassis?](#heading--add-nodes-via-a-chassis)
 snap-2-8-ui -->

<!-- snap-2-9-cli
1. [How does enlistment work?](#heading--enlistment)
2. [How do VM host nodes work?](/t/introduction-to-vm-hosting/2746)
3. [How do I add virtual machines?](/t/adding-a-vm-host/2290)
4. [How do I add a machine manually?](#heading--add-a-node-manually)
 snap-2-9-cli -->

<!-- snap-2-9-ui
1. [How does enlistment work?](#heading--enlistment)
2. [How do VM host nodes work?](/t/introduction-to-vm-hosting/2747)
3. [How do I add virtual machines?](/t/adding-a-vm-host/2291)
4. [How do I add a machine manually?](#heading--add-a-node-manually)
5. [How do I add a machine via a chassis?](#heading--add-nodes-via-a-chassis)
 snap-2-9-ui -->

<!-- snap-3-0-cli
1. [How does enlistment work?](#heading--enlistment)
2. [How do VM host nodes work?](/t/introduction-to-vm-hosting/4161)
3. [How do I add virtual machines?](/t/adding-a-vm-host/3817)
4. [How do I add a machine manually?](#heading--add-a-node-manually)
5. [How do I disable individual boot methods?](#heading--disable-individual-boot-methods)
 snap-3-0-cli -->

<!-- snap-3-0-ui
1. [How does enlistment work?](#heading--enlistment)
2. [How do VM host nodes work?](/t/introduction-to-vm-hosting/4162)
3. [How do I add virtual machines?](/t/adding-a-vm-host/3818)
4. [How do I add a machine manually?](#heading--add-a-node-manually)
5. [How do I add a machine via a chassis?](#heading--add-nodes-via-a-chassis)
6. [How do I disable individual boot methods?](#heading--disable-individual-boot-methods)
 snap-3-0-ui -->

MAAS typically adds a machine via a combination of DHCP, TFTP, and PXE. By now, you should have enabled MAAS to automatically add devices and machines to your environment. This unattended method of adding machines is called enlistment.

[note]
Configuring a computer to boot over PXE is done via its BIOS, often referred to as "netboot" or "network boot".
[/note]

Regardless of how MAAS adds a machine, there are no special requirements for the underlying machine. In particular, there is no need to install an operating system on it.

Once MAAS is working to the point of adding machines, you'll probably want to understand statuses and actions. See [Node statuses](/t/concepts-and-terms/785#heading--node-statuses) and [Machine actions](/t/concepts-and-terms/785#heading--machine-actions) respectively.

<a href="#heading--enlistment"><h2 id="heading--enlistment">How enlistment works</h2></a>

When MAAS enlists a machine, it first contacts the DHCP server, so that the machine can be assigned an IP address.  An IP address is necessary to download a kernel and initrd via TFTP, since these functions can't accept domain names.  Once the machine has a bootable kernel, MAAS boots it:

<a href="https://discourse.maas.io/uploads/default/original/1X/76f7113545e6950fec60bdeac06cfaf79b14b3ff.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/76f7113545e6950fec60bdeac06cfaf79b14b3ff.jpeg"></a> 

Next, initrd mounts a Squashfs image, ephemerally via HTTP, so that cloud-init can execute:

<a href="https://discourse.maas.io/uploads/default/original/1X/500f9bd2d070790a4007085705035366bee88a4a.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/500f9bd2d070790a4007085705035366bee88a4a.jpeg"></a> 

Finally, cloud-init runs enlistment and setup scripts:

<a href="https://discourse.maas.io/uploads/default/original/1X/bd87f78c8ee668a22640bf15607c9e3e532d46bb.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/bd87f78c8ee668a22640bf15607c9e3e532d46bb.jpeg"></a> 

<!-- deb-2-7-cli
The enlistment scripts send information about the machine to the region API server, including the architecture, MAC address and other details.  The API server, in turn, stores these details in the database. This information-gathering process is known as [automatic discovery or network discovery](/t/network-discovery/2928).
 deb-2-7-cli -->

<!-- deb-2-7-ui
The enlistment scripts send information about the machine to the region API server, including the architecture, MAC address and other details.  The API server, in turn, stores these details in the database. This information-gathering process is known as [automatic discovery or network discovery](/t/network-discovery/2929).
 deb-2-7-ui -->

<!-- deb-2-8-cli
The enlistment scripts send information about the machine to the region API server, including the architecture, MAC address and other details.  The API server, in turn, stores these details in the database. This information-gathering process is known as [automatic discovery or network discovery](/t/network-discovery/2930).
 deb-2-8-cli -->

<!-- deb-2-8-ui
The enlistment scripts send information about the machine to the region API server, including the architecture, MAC address and other details.  The API server, in turn, stores these details in the database. This information-gathering process is known as [automatic discovery or network discovery](/t/network-discovery/2931).
 deb-2-8-ui -->

<!-- deb-2-9-cli
The enlistment scripts send information about the machine to the region API server, including the architecture, MAC address and other details.  The API server, in turn, stores these details in the database. This information-gathering process is known as [automatic discovery or network discovery](/t/network-discovery/2932).
 deb-2-9-cli -->

<!-- deb-2-9-ui
The enlistment scripts send information about the machine to the region API server, including the architecture, MAC address and other details.  The API server, in turn, stores these details in the database. This information-gathering process is known as [automatic discovery or network discovery](/t/network-discovery/2933).
 deb-2-9-ui -->

<!-- deb-3-0-cli
The enlistment scripts send information about the machine to the region API server, including the architecture, MAC address and other details.  The API server, in turn, stores these details in the database. This information-gathering process is known as [automatic discovery or network discovery](/t/network-discovery/4043).
 deb-3-0-cli -->

<!-- deb-3-0-ui
The enlistment scripts send information about the machine to the region API server, including the architecture, MAC address and other details.  The API server, in turn, stores these details in the database. This information-gathering process is known as [automatic discovery or network discovery](/t/network-discovery/4044).
 deb-3-0-ui -->

<!-- snap-2-7-cli
The enlistment scripts send information about the machine to the region API server, including the architecture, MAC address and other details.  The API server, in turn, stores these details in the database. This information-gathering process is known as [automatic discovery or network discovery](/t/network-discovery/2922).
 snap-2-7-cli -->

<!-- snap-2-7-ui
The enlistment scripts send information about the machine to the region API server, including the architecture, MAC address and other details.  The API server, in turn, stores these details in the database. This information-gathering process is known as [automatic discovery or network discovery](/t/network-discovery/2923).
 snap-2-7-ui -->

<!-- snap-2-8-cli
The enlistment scripts send information about the machine to the region API server, including the architecture, MAC address and other details.  The API server, in turn, stores these details in the database. This information-gathering process is known as [automatic discovery or network discovery](/t/network-discovery/2924).
 snap-2-8-cli -->

<!-- snap-2-8-ui
The enlistment scripts send information about the machine to the region API server, including the architecture, MAC address and other details.  The API server, in turn, stores these details in the database. This information-gathering process is known as [automatic discovery or network discovery](/t/network-discovery/2925).
 snap-2-8-ui -->

<!-- snap-2-9-cli
The enlistment scripts send information about the machine to the region API server, including the architecture, MAC address and other details.  The API server, in turn, stores these details in the database. This information-gathering process is known as [automatic discovery or network discovery](/t/network-discovery/2926).
 snap-2-9-cli -->

<!-- snap-2-9-ui
The enlistment scripts send information about the machine to the region API server, including the architecture, MAC address and other details.  The API server, in turn, stores these details in the database. This information-gathering process is known as [automatic discovery or network discovery](/t/network-discovery/2927).
 snap-2-9-ui -->

<!-- snap-3-0-cli
The enlistment scripts send information about the machine to the region API server, including the architecture, MAC address and other details.  The API server, in turn, stores these details in the database. This information-gathering process is known as [automatic discovery or network discovery](/t/network-discovery/4041).
 snap-2-9-cli -->

<!-- snap-3-0-ui
The enlistment scripts send information about the machine to the region API server, including the architecture, MAC address and other details.  The API server, in turn, stores these details in the database. This information-gathering process is known as [automatic discovery or network discovery](/t/network-discovery/4042).
 snap-2-9-ui -->

After the enlistment process, MAAS places the machine in the 'Ready' state.  'Ready' is a holding state for machines that are enlisted (or commissioned), waiting to be deployed when needed.

<!-- deb-2-7-cli
Typically, the next step will be to [commission the machine](/t/commission-machines/2472). As an alternative to enlistment, an administrator can add a machine manually (see [below](#heading--add-a-node-manually)). Typically this is done when enlistment doesn't work for some reason. Note that when you manually add a machine, MAAS automatically commissions the machine as soon as you've added it.
 deb-2-7-cli -->

<!-- deb-2-7-ui
Typically, the next step will be to [commission the machine](/t/commission-machines/2473). As an alternative to enlistment, an administrator can add a machine manually (see [below](#heading--add-a-node-manually)). Typically this is done when enlistment doesn't work for some reason. Note that when you manually add a machine, MAAS automatically commissions the machine as soon as you've added it.
 deb-2-7-ui -->

<!-- deb-2-8-cli
Typically, the next step will be to [commission the machine](/t/commission-machines/2474). As an alternative to enlistment, an administrator can add a machine manually (see [below](#heading--add-a-node-manually)). Typically this is done when enlistment doesn't work for some reason. Note that when you manually add a machine, MAAS automatically commissions the machine as soon as you've added it.
 deb-2-8-cli -->

<!-- deb-2-8-ui
Typically, the next step will be to [commission the machine](/t/commission-machines/2475). As an alternative to enlistment, an administrator can add a machine manually (see [below](#heading--add-a-node-manually)). Typically this is done when enlistment doesn't work for some reason. Note that when you manually add a machine, MAAS automatically commissions the machine as soon as you've added it.
 deb-2-8-ui -->

<!-- deb-2-9-cli
Typically, the next step will be to [commission the machine](/t/commission-machines/2476). As an alternative to enlistment, an administrator can add a machine manually (see [below](#heading--add-a-node-manually)). Typically this is done when enlistment doesn't work for some reason. Note that when you manually add a machine, MAAS automatically commissions the machine as soon as you've added it.
 deb-2-9-cli -->

<!-- deb-2-9-ui
Typically, the next step will be to [commission the machine](/t/commission-machines/2477). As an alternative to enlistment, an administrator can add a machine manually (see [below](#heading--add-a-node-manually)). Typically this is done when enlistment doesn't work for some reason. Note that when you manually add a machine, MAAS automatically commissions the machine as soon as you've added it.
 deb-2-9-ui -->

<!-- deb-3-0-cli
Typically, the next step will be to [commission the machine](/t/commission-machines/3875). As an alternative to enlistment, an administrator can add a machine manually (see [below](#heading--add-a-node-manually)). Typically this is done when enlistment doesn't work for some reason. Note that when you manually add a machine, MAAS automatically commissions the machine as soon as you've added it.
 deb-3-0-cli -->

<!-- deb-3-0-ui
Typically, the next step will be to [commission the machine](/t/commission-machines/3876). As an alternative to enlistment, an administrator can add a machine manually (see [below](#heading--add-a-node-manually)). Typically this is done when enlistment doesn't work for some reason. Note that when you manually add a machine, MAAS automatically commissions the machine as soon as you've added it.
 deb-3-0-ui -->

<!-- snap-2-7-cli
Typically, the next step will be to [commission the machine](/t/commission-machines/2466). As an alternative to enlistment, an administrator can add a machine manually (see [below](#heading--add-a-node-manually)). Typically this is done when enlistment doesn't work for some reason. Note that when you manually add a machine, MAAS automatically commissions the machine as soon as you've added it.
 snap-2-7-cli -->

<!-- snap-2-7-ui
Typically, the next step will be to [commission the machine](/t/commission-machines/2467). As an alternative to enlistment, an administrator can add a machine manually (see [below](#heading--add-a-node-manually)). Typically this is done when enlistment doesn't work for some reason. Note that when you manually add a machine, MAAS automatically commissions the machine as soon as you've added it.
 snap-2-7-ui -->

<!-- snap-2-8-cli
Typically, the next step will be to [commission the machine](/t/commission-machines/2468). As an alternative to enlistment, an administrator can add a machine manually (see [below](#heading--add-a-node-manually)). Typically this is done when enlistment doesn't work for some reason. Note that when you manually add a machine, MAAS automatically commissions the machine as soon as you've added it.
 snap-2-8-cli -->

<!-- snap-2-8-ui
Typically, the next step will be to [commission the machine](/t/commission-machines/2469). As an alternative to enlistment, an administrator can add a machine manually (see [below](#heading--add-a-node-manually)). Typically this is done when enlistment doesn't work for some reason. Note that when you manually add a machine, MAAS automatically commissions the machine as soon as you've added it.
 snap-2-8-ui -->

<!-- snap-2-9-cli
Typically, the next step will be to [commission the machine](/t/commission-machines/2470). As an alternative to enlistment, an administrator can add a machine manually (see [below](#heading--add-a-node-manually)). Typically this is done when enlistment doesn't work for some reason. Note that when you manually add a machine, MAAS automatically commissions the machine as soon as you've added it.
 snap-2-9-cli -->

<!-- snap-2-9-ui
Typically, the next step will be to [commission the machine](/t/commission-machines/2471). As an alternative to enlistment, an administrator can add a machine manually (see [below](#heading--add-a-node-manually)). Typically this is done when enlistment doesn't work for some reason. Note that when you manually add a machine, MAAS automatically commissions the machine as soon as you've added it.
 snap-2-9-ui -->

<!-- snap-3-0-cli
Typically, the next step will be to [commission the machine](/t/commission-machines/3873). As an alternative to enlistment, an administrator can add a machine manually (see [below](#heading--add-a-node-manually)). Typically this is done when enlistment doesn't work for some reason. Note that when you manually add a machine, MAAS automatically commissions the machine as soon as you've added it.
 snap-3-0-cli -->

<!-- snap-3-0-ui
Typically, the next step will be to [commission the machine](/t/commission-machines/3874). As an alternative to enlistment, an administrator can add a machine manually (see [below](#heading--add-a-node-manually)). Typically this is done when enlistment doesn't work for some reason. Note that when you manually add a machine, MAAS automatically commissions the machine as soon as you've added it.
 snap-3-0-ui -->

[note]
MAAS runs built-in commissioning scripts during the enlistment phase. When you commission a machine, any customised commissioning scripts you add will have access to data collected during enlistment. Follow the link above for more information about commissioning and commission scripts.
[/note]

<a href="#heading--add-a-node-manually"><h2 id="heading--add-a-node-manually">Add a machine manually</h2></a>

Enlistment can be done manually if the hardware specifications of the underlying machine are known.

<!-- deb-2-7-ui snap-2-7-ui
On the 'Machines' page of the web UI, click the 'Add hardware' button and then select 'Machine'.

Fill in the form and hit 'Save machine'. In this example, you are adding an IPMI machine:

<a href="https://assets.ubuntu.com/v1/20aa36b2-nodes-add__2.5_add-node-manually.png" target = "_blank"><img src="https://assets.ubuntu.com/v1/20aa36b2-nodes-add__2.5_add-node-manually.png"></a>

The fields on the "Add machine" screen include the following seven items:

1. **Machine name**: This field is used to identify the machine to the user.  It can be set to anything, though it is often set to the MAC address of the machine in question.  This field is optional, in that MAAS will assign a unique, nonsense name if you leave it blank.  You can change this nonsense name later, if desired.

2. **Domain**: This field sets the domain name of the domain managed by MAAS.  It can be set to anything; MAAS assigns the domain name "maas" by default.

3. **Architecture**: This field refers to the architecture of the machine being added.

4. **Minimum Kernel**: This field supplies a drop-down of possible kernels available for deployment on this machine.

5. **Zone**: This field allows you to set the availability zone, selected from AZs that you have already created (if any).

6. **Resource pool**: This field allows you to set the resource pool for this machine, selected from pools you have already created (if any).

7. **MAC Address**: You should fill in this field with the MAC address of the machine you are adding.  Note that the MAC address entered here must use a colon (":") separator, although some MAC addresses are written with dash ("-") separators.
deb-2-7-ui snap-2-7-ui -->

<!-- snap-2-7-ui 
type**: You must select the power type supported by the machine you are adding, and fill in additional required fields that appear.  See [Power management](/t/power-management/3007) for details on the available power types and the relevant parameters for each type.
snap-2-7-ui -->

<!-- deb-2-7-ui 
type**: You must select the power type supported by the machine you are adding, and fill in additional required fields that appear.  See [Power management](/t/power-management/3103) for details on the available power types and the relevant parameters for each type.
deb-2-7-ui -->

<!-- deb-2-8-ui snap-2-8-ui deb-2-9-ui snap-2-9-ui snap-3-0-ui deb-3-0-ui 
On the 'Machines' page of the web UI, click the 'Add hardware' button and then select 'Machine'.

Fill in the form and hit 'Save machine'. In this example, you are adding an IPMI machine:

<a href="https://discourse.maas.io/uploads/default/original/1X/faebe2fb37cd73252eaf9521ed1bcf31fb0e76f6.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/faebe2fb37cd73252eaf9521ed1bcf31fb0e76f6.jpeg"></a>

The fields on the "Add machine" screen include the following items:

* **Machine name**: This field is used to identify the machine to the user.  It can be set to anything, though it is often set to the MAC address of the machine in question.  This field is optional, in that MAAS will assign a unique, nonsense name if you leave it blank.  You can change this nonsense name later, if desired.

* **Domain**: This field sets the domain name of the domain managed by MAAS.  It can be set to anything; MAAS assigns the domain name "maas" by default.

* **Architecture**: This field refers to the architecture of the machine being added.

* **Minimum Kernel**: This field supplies a drop-down of possible kernels available for deployment on this machine.

* **Zone**: This field allows you to set the availability zone, selected from AZs that you have already created (if any).

* **Resource pool**: This field allows you to set the resource pool for this machine, selected from pools you have already created (if any).

* **MAC Address**: You should fill in this field with the MAC address of the machine you are adding.  Note that the MAC address entered here must use a colon (":") separator, although some MAC addresses are written with dash ("-") separators.
deb-2-8-ui snap-2-8-ui deb-2-9-ui snap-2-9-ui  snap-3-0-ui deb-3-0-ui -->

<!-- deb-2-8-ui
* **Power type**: You must select the power type supported by the machine you are adding, and fill in additional required fields that appear.  See [Power management](/t/power-management/3015) for details on the available power types and the relevant parameters for each type.
 deb-2-8-ui -->

<!-- deb-2-9-ui
* **Power type**: You must select the power type supported by the machine you are adding, and fill in additional required fields that appear.  See [Power management](/t/power-management/3017) for details on the available power types and the relevant parameters for each type.
 deb-2-9-ui -->

<!-- deb-3-0-ui
* **Power type**: You must select the power type supported by the machine you are adding, and fill in additional required fields that appear.  See [Power management](/t/power-management/4072) for details on the available power types and the relevant parameters for each type.
 deb-3-0-ui -->

<!-- snap-2-8-ui
* **Power type**: You must select the power type supported by the machine you are adding, and fill in additional required fields that appear.  See [Power management](/t/power-management/3009) for details on the available power types and the relevant parameters for each type.
 snap-2-8-ui -->

<!-- snap-2-9-ui
* **Power type**: You must select the power type supported by the machine you are adding, and fill in additional required fields that appear.  See [Power management](/t/power-management/3011) for details on the available power types and the relevant parameters for each type.
 snap-2-9-ui -->

<!-- snap-3-0-ui
* **Power type**: You must select the power type supported by the machine you are adding, and fill in additional required fields that appear.  See [Power management](/t/power-management/4070) for details on the available power types and the relevant parameters for each type.
 snap-2-9-ui -->

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 
At the command line, enter the following information:

```
stormrider@wintermute:~$ maas admin machines create \
> architecture=$ARCH \
> max_addresses=$MAC_ADDRESS \
> power_type=$POWER_TYPE \
> power_parameters_power_id=$POWER_ID \
> power_parameters_power_address=$POWER_ADDRESS \
> power_parameters_power_pass=$POWER_PASSWORD
```

When you enter the command (substituting the `$...` parameters for your own particulars), the screen will pause for a moment, and then return a stream of JSON relating to the added machine.

Here's an example with a local laptop MAAS install, using KVMs as virtual machines:

```
stormrider@wintermute:~$ maas admin machines create \
> architecture=amd64 \
> max_addresses=52:54:00:6f:b4:af \
> power_type=virsh \
> power_parameters_power_id=50f6cca2-5d89-43b9-941c-90c9fcd7c156 \
> power_parameters_power_address=qemu+ssh://stormrider@192.168.123.1/system \
> power_parameters_power_pass=xxxxxxx
```

The variable fields in the `machines create` command (the `$...` items) are as follows, in this example: 

```
> architecture=$ARCH \
> mac_addresses=$MAC_ADDRESS \
> power_type=$POWER_TYPE \
> power_parameters_power_id=$POWER_ID \
> power_parameters_power_address=$POWER_ADDRESS \
> power_parameters_power_pass=$POWER_PASSWORD
```

* `$ARCH`: This field refers to the architecture of the machine being added, `amd64` in the local laptop example.

* `$MAC_ADDRESS`: This is the MAC address of the boot-enabled NIC for the machine being added.  Note that the MAC address entered here must use a colon (":") separator, although some MAC addresses are written with dash ("-") separators.
snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli  -->

<!-- deb-2-7-cli
* `$POWER_TYPE`: You must select the power type supported by the machine you are adding, and fill in additional required fields that appear.  See [Power management](/t/power-management/3012) for details on the available power types and the relevant parameters for each type. In this example, we've used a "virsh" power type (a libvirt KVM), but your choice will depend on your hardware.
 deb-2-7-cli -->

<!-- deb-2-8-cli
* `$POWER_TYPE`: You must select the power type supported by the machine you are adding, and fill in additional required fields that appear.  See [Power management](/t/power-management/3014) for details on the available power types and the relevant parameters for each type. In this example, we've used a "virsh" power type (a libvirt KVM), but your choice will depend on your hardware.
 deb-2-8-cli -->

<!-- deb-2-9-cli
* `$POWER_TYPE`: You must select the power type supported by the machine you are adding, and fill in additional required fields that appear.  See [Power management](/t/power-management/3016) for details on the available power types and the relevant parameters for each type. In this example, we've used a "virsh" power type (a libvirt KVM), but your choice will depend on your hardware.
 deb-2-9-cli -->

<!-- deb-3-0-cli
* `$POWER_TYPE`: You must select the power type supported by the machine you are adding, and fill in additional required fields that appear.  See [Power management](/t/power-management/4071) for details on the available power types and the relevant parameters for each type. In this example, we've used a "virsh" power type (a libvirt KVM), but your choice will depend on your hardware.
 deb-3-0-cli -->

<!-- snap-2-7-cli
* `$POWER_TYPE`: You must select the power type supported by the machine you are adding, and fill in additional required fields that appear.  See [Power management](/t/power-management/3006) for details on the available power types and the relevant parameters for each type. In this example, we've used a "virsh" power type (a libvirt KVM), but your choice will depend on your hardware.
 snap-2-7-cli -->

<!-- snap-2-8-cli
* `$POWER_TYPE`: You must select the power type supported by the machine you are adding, and fill in additional required fields that appear.  See [Power management](/t/power-management/3008) for details on the available power types and the relevant parameters for each type. In this example, we've used a "virsh" power type (a libvirt KVM), but your choice will depend on your hardware.
 snap-2-8-cli -->

<!-- snap-2-9-cli
* `$POWER_TYPE`: You must select the power type supported by the machine you are adding, and fill in additional required fields that appear.  See [Power management](/t/power-management/3010) for details on the available power types and the relevant parameters for each type. In this example, we've used a "virsh" power type (a libvirt KVM), but your choice will depend on your hardware.
 snap-2-9-cli -->

<!-- snap-3-0-cli
* `$POWER_TYPE`: You must select the power type supported by the machine you are adding, and fill in additional required fields that appear.  See [Power management](/t/power-management/4069) for details on the available power types and the relevant parameters for each type. In this example, we've used a "virsh" power type (a libvirt KVM), but your choice will depend on your hardware.
 snap-3-0-cli -->

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 
* `$POWER_ID`: This is generally the UUID of the machine being added.

* `$POWER_ADDRESS/$POWER_PASSWORD`: In the case of a KVM, these are the only parameters that need to be entered.  See [Power types](https://maas.io/docs/api#power-types) in the API reference for details on the available power types and the relevant parameters for each type.
snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli  -->

Normally, when you add a machine manually, MAAS will immediately attempt to commission the machine. Note that you will need to configure the underlying machine to boot over the network, or commissioning will fail. MAAS cannot handle this configuration for you.  While the correct method for configuring network boot depends heavily on your server, there are two common elements:

1. The network card on your server must be able to support PXE, i.e., your NIC -- whether independent or integrated on a motherboard -- must have a boot PROM that supports network booting.  You'll need to consult the documentation for the machine in question to determine this.

2. You usually have to interrupt the boot process and enter the BIOS/UEFI menu to configure the network card's PXE stack.  Again, you may need to consult your machine's documentation to pin down this step.

Additional steps will vary widely by machine type and architecture.

<a href="#heading--bmc-enlistment"><h3 id="heading--bmc-enlistment">BMC enlistment</h3></a>

[note status="2.4"]
Note that in MAAS versions before 2.5, you are required to provide the MAC address of the PXE interface when adding a new machine manually.
[/note]

##### IPMI machines

For IPMI machines, you only need to provide IPMI credentials. MAAS automatically discovers the machine and runs enlistment configuration by matching the BMC address.

##### Non-IPMI machines

For non-IPMI machines, you must specify a non-PXE MAC address. MAAS automatically discovers the machine and runs enlistment configuration by matching the non-PXE MAC address.

<!-- deb-2-7-ui snap-2-7-ui
<a href="#heading--add-nodes-via-a-chassis"><h2 id="heading--add-nodes-via-a-chassis">Add a machine via a chassis</h2></a>

Use the chassis feature to add multiple machines at once. To do this, instead of selecting 'Machine' as above, choose 'Chassis' from the drop-down menu. In the following example, MAAS will add all available VMs from the given  virsh address:

<a href="https://assets.ubuntu.com/v1/d5314a8a-nodes-add__2.4_add-node-chassis.png" target = "_blank"><img src="https://assets.ubuntu.com/v1/d5314a8a-nodes-add__2.4_add-node-chassis.png"></a>

The required fields will change based on the type of chassis you choose.

[note]
As with the manual method, the underlying machines will require netbooting.
[/note]
deb-2-7-ui snap-2-7-ui -->

<!-- snap-2-8-ui snap-2-9-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
<a href="#heading--add-nodes-via-a-chassis"><h2 id="heading--add-nodes-via-a-chassis">Add a machine via a chassis</h2></a>

Use the chassis feature to add multiple machines at once. To do this, instead of selecting 'Machine' as above, choose 'Chassis' from the drop-down menu. In the following example, MAAS will add all available VMs from the given  virsh address:

<a href="https://discourse.maas.io/uploads/default/original/1X/e7f88bce68318cf3c6a8e97b4d31d0b6980e0f32.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/e7f88bce68318cf3c6a8e97b4d31d0b6980e0f32.jpeg"></a>

The required fields will change based on the type of chassis you choose.

[note]
As with the manual method, the underlying machines will require netbooting.
[/note]
snap-2-8-ui snap-2-9-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui  -->

<!-- snap-3-0-ui snap-3-0-cli

<a href="#heading--disable-individual-boot-methods"><h2 id="heading--disable-individual-boot-methods">How do I disable individual boot methods?</h2></a>

In MAAS 3.0, it is possible to diable individual boot methods.  This must be done via the CLI. When a boot method is disabled MAAS will configure MAAS controlled `isc-dhcpd` to not respond to the associated [boot architecture code](https://www.iana.org/assignments/dhcpv6-parameters/dhcpv6-parameters.xhtml#processor-architecture). External DHCP servers must be configured manually.

To allow different boot methods to be in different states on separate physical networks using the same VLAN ID configuration is done on the subnet in the UI or API. When using the API boot methods to be disabled may be specified using the MAAS internal name or [boot architecture code](https://www.iana.org/assignments/dhcpv6-parameters/dhcpv6-parameters.xhtml#processor-architecture) in octet or hex form. For example the following disabled i386/AMD64 PXE, AMD64 UEFI TFTP, and AMD64 UEFI HTTP

```bash 
maas $PROFILE subnet \
update $SUBNET \
disabled_boot_architectures="0x00 uefi_amd64_tftp 00:10"
```

Specifically, for MAAS 3.0, the following changes have been implemented:

* UEFI AMD64 HTTP(00:10) has been reenabled.
* UEFI ARM64 HTTP(00:13) has been enabled.
* UEFI ARM64 TFTP(00:0B) and UEFI ARM64 HTTP(00:13) will now provide a shim and GRUB signed with the Microsoft boot loader keys.
* grub.cfg for all UEFI platforms has been updated to replace the deprecated `linuxefi` and `initrdefi` commands with the standard `linux` and `initrd` commands.
* GRUB debug may now be enabled by enabling [rackd debug logging](https://discourse.maas.io/t/running-installed-maas-in-debug-logging-mode/168).

snap-3-0-ui snap-3-0-cli -->

