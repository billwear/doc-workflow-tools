||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/commission-machines-snap-2-7-cli/2466) ~ [UI](/t/commission-machines-snap-2-7-ui/2467)|[CLI](/t/commission-machines-snap-2-8-cli/2468) ~ [UI](/t/commission-machines-snap-2-8-ui/2469)|[CLI](/t/commission-machines-snap-2-9-cli/2470) ~ [UI](/t/commission-machines-snap-2-9-ui/2471)|[CLI](/t/commission-machines-snap-3-0-cli/3873) ~ [UI](/t/commission-machines-snap-3-0-ui/3874)|
Packages|[CLI](/t/commission-machines-deb-2-7-cli/2472) ~ [UI](/t/commission-machines-deb-2-7-ui/2473)|[CLI](/t/commission-machines-deb-2-8-cli/2474) ~ [UI](/t/commission-machines-deb-2-8-ui/2475)|[CLI](/t/commission-machines-deb-2-9-cli/2476) ~ [UI](/t/commission-machines-deb-2-9-ui/2477)|[CLI](/t/commission-machines-deb-3-0-cli/3875) ~ [UI](/t/commission-machines-deb-3-0-ui/3876)|

MAAS is built to manage machines, including the operating systems on those machines. Enlistment and commissioning are features that make it easier to start managing a machine -- as long as that machine has been configured to netboot. Enlistment enables users to simply connect a machine, configure the firmware properly, and power it on so that MAAS can find it and add it.

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 

#### Eight questions you may have:

1. [Tell me about enlistment vs. commissioning.](#heading--enlistment-v-commissioning)
2. [How are machines commissioned?](#heading--commissioning-machines)
3. [How can I commission NUMA and SR-IOV nodes?](#heading--numa-sriov-commissioning)
4. [What are MAAS commissioning scripts?](#heading--commissioning-scripts)
5. [What post-commission configuration is possible?](#heading--post-commission-configuration)
6. [What is a bond interface and how do I create one?](#heading--bond-interfaces)
7. [What is a bridge interface and how do I create one?](#heading--bridge-interfaces)
8. [How do I assign an interface to a fabric?](#heading--assign-a-network-interface-to-a-fabric)

snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui  -->

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 

#### Twelve questions you may have:

1. [Tell me about enlistment vs. commissioning.](#heading--enlistment-v-commissioning)
2. [How are machines commissioned?](#heading--commissioning-machines)
3. [How can I commission NUMA and SR-IOV nodes?](#heading--numa-sriov-commissioning)
4. [What are MAAS commissioning scripts?](#heading--commissioning-scripts)
5. [What post-commission configuration is possible?](#heading--post-commission-configuration)
6. [What is a bond interface and how do I create one?](#heading--bond-interfaces)
7. [What is a bridge interface and how do I create one?](#heading--bridge-interfaces)
8. [How do I assign an interface to a fabric?](#heading--assign-a-network-interface-to-a-fabric)
9. [How do I discover interface identifiers?](#heading--interface-identifiers)
10. [How do I delete an interface?](#heading--delete-an-interface)
11. [How do I create a VLAN interface?](#heading--create-a-vlan-interface)
12. [How do I delete a VLAN interface?](#heading--delete-a-vlan-interface)

snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli  -->

<a href="#heading--enlistment-v-commissioning"><h2 id="heading--enlistment-v-commissioning">Enlistment versus commissioning</h2></a>

Enlistment happens when MAAS starts; it reaches out on connected subnets to locate any nodes -- that is, devices and machines -- that reside on those subnets. MAAS finds a machine that's configured to netboot (e.g., via PXE), boots that machine into Ubuntu, and then sends cloud-init user data which runs standard (i.e., built-in) commissioning scripts. The machine actually adds itself over the MAAS API, and then requests permission to send commissioning data.

Since MAAS doesn't know whether you might intend to actually include these discovered machines in your cloud configuration, it won't automatically take them over, but it will read them to get an idea how they're set up. MAAS then presents these machines to you with a MAAS state of "New." This allows you to examine them and decide whether or not you want MAAS to manage them.

<!-- deb-2-7-cli
When you configure a machine to netboot -- and turn it on while connected to the network -- MAAS will enlist it, giving it a status of "New."  You can also [add a machine manually](/t/add-machines/2280)). In either case, the next step is *commissioning*, which boots the machine into an ephemeral Ubuntu kernel so that resource information can be gathered. This resource information includes (but isn't limited to) information about CPUs, memory, and storage. You can also run [custom commissioning scripts](/t/commissioning-and-hardware-testing-scripts/2484) to meet your specific needs.
deb-2-7-cli -->

<!-- deb-2-7-ui
When you configure a machine to netboot -- and turn it on while connected to the network -- MAAS will enlist it, giving it a status of "New."  You can also [add a machine manually](/t/add-machines/2281)).  In either case, the next step is *commissioning*, which boots the machine into an ephemeral Ubuntu kernel so that resource information can be gathered. This resource information includes (but isn't limited to) information about CPUs, memory, and storage. You can also run [custom commissioning scripts](/t/commissioning-and-hardware-testing-scripts/2485) to meet your specific needs.
 deb-2-7-ui -->

<!-- deb-2-8-cli
When you configure a machine to netboot -- and turn it on while connected to the network -- MAAS will enlist it, giving it a status of "New."  You can also [add a machine manually](/t/add-machines/2282)).  In either case, the next step is *commissioning*, which boots the machine into an ephemeral Ubuntu kernel so that resource information can be gathered. This resource information includes (but isn't limited to) information about CPUs, memory, and storage. You can also run [custom commissioning scripts](/t/commissioning-and-hardware-testing-scripts/2486) to meet your specific needs.
 deb-2-8-cli -->

<!-- deb-2-8-ui
When you configure a machine to netboot -- and turn it on while connected to the network -- MAAS will enlist it, giving it a status of "New."  You can also [add a machine manually](/t/add-machines/2283)).  In either case, the next step is *commissioning*, which boots the machine into an ephemeral Ubuntu kernel so that resource information can be gathered. This resource information includes (but isn't limited to) information about CPUs, memory, and storage. You can also run [custom commissioning scripts](/t/commissioning-and-hardware-testing-scripts/2487) to meet your specific needs.
 deb-2-8-ui -->

<!-- deb-2-9-cli
When you configure a machine to netboot -- and turn it on while connected to the network -- MAAS will enlist it, giving it a status of "New."  You can also [add a machine manually](/t/add-machines/2284)).  In either case, the next step is *commissioning*, which boots the machine into an ephemeral Ubuntu kernel so that resource information can be gathered.  You can also run [custom commissioning scripts](/t/commissioning-and-hardware-testing-scripts/2488) to meet your specific needs.

[note]
Commissioning requires 60 seconds.
[/note]
 deb-2-9-cli -->

<!-- deb-2-9-ui
When you configure a machine to netboot -- and turn it on while connected to the network -- MAAS will enlist it, giving it a status of "New."  You can also [add a machine manually](/t/add-machines/2285)).  In either case, the next step is *commissioning*, which boots the machine into an ephemeral Ubuntu kernel so that resource information can be gathered. This resource information includes (but isn't limited to) information about CPUs, memory, and storage. You can also run [custom commissioning scripts](/t/commissioning-and-hardware-testing-scripts/2489) to meet your specific needs.

[note]
Commissioning requires 60 seconds.
[/note]
 deb-2-9-ui -->

<!-- deb-3-0-cli
When you configure a machine to netboot -- and turn it on while connected to the network -- MAAS will enlist it, giving it a status of "New."  You can also [add a machine manually](/t/add-machines/3823)).  In either case, the next step is *commissioning*, which boots the machine into an ephemeral Ubuntu kernel so that resource information can be gathered.  This resource information includes (but isn't limited to) information about CPUs, memory, storage, and details of any PCE and USB devices attached to the machine. You can also run [custom commissioning scripts](/t/commissioning-and-hardware-testing-scripts/3867) to meet your specific needs.

[note]
Commissioning requires 60 seconds.
[/note]
 deb-3-0-cli -->

<!-- deb-3-0-ui
When you configure a machine to netboot -- and turn it on while connected to the network -- MAAS will enlist it, giving it a status of "New."  You can also [add a machine manually](/t/add-machines/3824)).  In either case, the next step is *commissioning*, which boots the machine into an ephemeral Ubuntu kernel so that resource information can be gathered.  This resource information includes (but isn't limited to) information about CPUs, memory, storage, and details of any PCE and USB devices attached to the machine. You can also run [custom commissioning scripts](/t/commissioning-and-hardware-testing-scripts/3868) to meet your specific needs.

[note]
Commissioning requires 60 seconds.
[/note]
 deb-3-0-ui -->

<!-- snap-2-7-cli
When you configure a machine to netboot -- and turn it on while connected to the network -- MAAS will enlist it, giving it a status of "New."  You can also [add a machine manually](/t/add-machines/2274)).  In either case, the next step is *commissioning*, which boots the machine into an ephemeral Ubuntu kernel so that resource information can be gathered. This resource information includes (but isn't limited to) information about CPUs, memory, and storage. You can also run [custom commissioning scripts](/t/commissioning-and-hardware-testing-scripts/2478) to meet your specific needs.
 snap-2-7-cli -->

<!-- snap-2-7-ui
When you configure a machine to netboot -- and turn it on while connected to the network -- MAAS will enlist it, giving it a status of "New."  You can also [add a machine manually](/t/add-machines/2275)).  In either case, the next step is *commissioning*, which boots the machine into an ephemeral Ubuntu kernel so that resource information can be gathered. This resource information includes (but isn't limited to) information about CPUs, memory, and storage. You can also run [custom commissioning scripts](/t/commissioning-and-hardware-testing-scripts/2479) to meet your specific needs.
 snap-2-7-ui -->

<!-- snap-2-8-cli
When you configure a machine to netboot -- and turn it on while connected to the network -- MAAS will enlist it, giving it a status of "New."  You can also [add a machine manually](/t/add-machines/2276)).  In either case, the next step is *commissioning*, which boots the machine into an ephemeral Ubuntu kernel so that resource information can be gathered. This resource information includes (but isn't limited to) information about CPUs, memory, and storage. You can also run [custom commissioning scripts](/t/commissioning-and-hardware-testing-scripts/2480) to meet your specific needs.
 snap-2-8-cli -->

<!-- snap-2-8-ui
When you configure a machine to netboot -- and turn it on while connected to the network -- MAAS will enlist it, giving it a status of "New."  You can also [add a machine manually](/t/add-machines/2277)).  In either case, the next step is *commissioning*, which boots the machine into an ephemeral Ubuntu kernel so that resource information can be gathered.  You can also run [custom commissioning scripts](/t/commissioning-and-hardware-testing-scripts/2481) to meet your specific needs.
 snap-2-8-ui -->

<!-- snap-2-9-cli
When you configure a machine to netboot -- and turn it on while connected to the network -- MAAS will enlist it, giving it a status of "New."  You can also [add a machine manually](/t/add-machines/2278)).  In either case, the next step is *commissioning*, which boots the machine into an ephemeral Ubuntu kernel so that resource information can be gathered.  This resource information includes (but isn't limited to) information about CPUs, memory, and storage. You can also run [custom commissioning scripts](/t/commissioning-and-hardware-testing-scripts/2482) to meet your specific needs.

[note]
Commissioning requires 60 seconds.
[/note]
 snap-2-9-cli -->

<!-- snap-2-9-ui
When you configure a machine to netboot -- and turn it on while connected to the network -- MAAS will enlist it, giving it a status of "New."  You can also [add a machine manually](/t/add-machines/2279)).  In either case, the next step is *commissioning*, which boots the machine into an ephemeral Ubuntu kernel so that resource information can be gathered.   This resource information includes (but isn't limited to) information about CPUs, memory, and storage. You can also run [custom commissioning scripts](/t/commissioning-and-hardware-testing-scripts/2483) to meet your specific needs.

[note]
Commissioning requires 60 seconds.
[/note]
 snap-2-9-ui -->

<!-- snap-3-0-cli
When you configure a machine to netboot -- and turn it on while connected to the network -- MAAS will enlist it, giving it a status of "New."  You can also [add a machine manually](/t/add-machines/3821)).  In either case, the next step is *commissioning*, which boots the machine into an ephemeral Ubuntu kernel so that resource information can be gathered.   This resource information includes (but isn't limited to) information about CPUs, memory, storage, and details of any PCE and USB devices attached to the machine.You can also run [custom commissioning scripts](/t/commissioning-and-hardware-testing-scripts/3865) to meet your specific needs.

[note]
Commissioning requires 60 seconds.
[/note]
 snap-3-0-cli -->

<!-- snap-3-0-ui
When you configure a machine to netboot -- and turn it on while connected to the network -- MAAS will enlist it, giving it a status of "New."  You can also [add a machine manually](/t/add-machines/3822)).  In either case, the next step is *commissioning*, which boots the machine into an ephemeral Ubuntu kernel so that resource information can be gathered.   This resource information includes (but isn't limited to) information about CPUs, memory, storage, and details of any PCE and USB devices attached to the machine. You can also run [custom commissioning scripts](/t/commissioning-and-hardware-testing-scripts/3866) to meet your specific needs.

[note]
Commissioning requires 60 seconds.
[/note]
 snap-3-0-ui -->

<a href="#heading--commissioning-machines"><h2 id="heading--commissioning-machines">How machines are commissioned</h2></a>

When MAAS commissions a machine, the following sequence of events takes place:

<!-- deb-2-7-cli
1.  DHCP server is contacted
2.  kernel and initrd are received over TFTP
3.  machine boots
4.  initrd mounts a Squashfs image ephemerally over HTTP
5.  cloud-init runs built-in and [custom commissioning scripts](/t/commissioning-and-hardware-testing-scripts/2484)
6.  machine shuts down
 deb-2-7-cli -->

<!-- deb-2-7-ui
1.  DHCP server is contacted
2.  kernel and initrd are received over TFTP
3.  machine boots
4.  initrd mounts a Squashfs image ephemerally over HTTP
5.  cloud-init runs built-in and [custom commissioning scripts](/t/commissioning-and-hardware-testing-scripts/2585)
6.  machine shuts down
 deb-2-7-ui -->

<!-- deb-2-8-cli
1.  DHCP server is contacted
2.  kernel and initrd are received over TFTP
3.  machine boots
4.  initrd mounts a Squashfs image ephemerally over HTTP
5.  cloud-init runs built-in and [custom commissioning scripts](/t/commissioning-and-hardware-testing-scripts/2486)
6.  machine shuts down
 deb-2-8-cli -->

<!-- deb-2-8-ui
1.  DHCP server is contacted
2.  kernel and initrd are received over TFTP
3.  machine boots
4.  initrd mounts a Squashfs image ephemerally over HTTP
5.  cloud-init runs built-in and [custom commissioning scripts](/t/commissioning-and-hardware-testing-scripts/2487)
6.  machine shuts down
 deb-2-8-ui -->

<!-- deb-2-9-cli
1.  DHCP server is contacted
2.  kernel and initrd are received over TFTP
3.  machine boots
4.  initrd mounts a Squashfs image ephemerally over HTTP
5.  cloud-init runs built-in and [custom commissioning scripts](/t/commissioning-and-hardware-testing-scripts/2488)
6.  machine shuts down
 deb-2-9-cli -->

<!-- deb-2-9-ui
1.  DHCP server is contacted
2.  kernel and initrd are received over TFTP
3.  machine boots
4.  initrd mounts a Squashfs image ephemerally over HTTP
5.  cloud-init runs built-in and [custom commissioning scripts](/t/commissioning-and-hardware-testing-scripts/2489)
6.  machine shuts down
 deb-2-9-ui -->

<!-- deb-3-0-cli
1.  DHCP server is contacted
2.  kernel and initrd are received over TFTP
3.  machine boots
4.  initrd mounts a Squashfs image ephemerally over HTTP
5.  cloud-init runs built-in and [custom commissioning scripts](/t/commissioning-and-hardware-testing-scripts/3867)
6.  machine shuts down
 deb-3-0-cli -->

<!-- deb-3-0-ui
1.  DHCP server is contacted
2.  kernel and initrd are received over TFTP
3.  machine boots
4.  initrd mounts a Squashfs image ephemerally over HTTP
5.  cloud-init runs built-in and [custom commissioning scripts](/t/commissioning-and-hardware-testing-scripts/3868)
6.  machine shuts down
 deb-3-0-ui -->

<!-- snap-2-7-cli
1.  DHCP server is contacted
2.  kernel and initrd are received over TFTP
3.  machine boots
4.  initrd mounts a Squashfs image ephemerally over HTTP
5.  cloud-init runs built-in and [custom commissioning scripts](/t/commissioning-and-hardware-testing-scripts/2478)
6.  machine shuts down
 snap-2-7-cli -->

<!-- snap-2-7-ui
1.  DHCP server is contacted
2.  kernel and initrd are received over TFTP
3.  machine boots
4.  initrd mounts a Squashfs image ephemerally over HTTP
5.  cloud-init runs built-in and [custom commissioning scripts](/t/commissioning-and-hardware-testing-scripts/2479)
6.  machine shuts down
 snap-2-7-ui -->

<!-- snap-2-8-cli
1.  DHCP server is contacted
2.  kernel and initrd are received over TFTP
3.  machine boots
4.  initrd mounts a Squashfs image ephemerally over HTTP
5.  cloud-init runs built-in and [custom commissioning scripts](/t/commissioning-and-hardware-testing-scripts/2480)
6.  machine shuts down
 snap-2-8-cli -->

<!-- snap-2-8-ui
1.  DHCP server is contacted
2.  kernel and initrd are received over TFTP
3.  machine boots
4.  initrd mounts a Squashfs image ephemerally over HTTP
5.  cloud-init runs built-in and [custom commissioning scripts](/t/commissioning-and-hardware-testing-scripts/2481)
6.  machine shuts down
 snap-2-8-ui -->

<!-- snap-2-9-cli
1.  DHCP server is contacted
2.  kernel and initrd are received over TFTP
3.  machine boots
4.  initrd mounts a Squashfs image ephemerally over HTTP
5.  cloud-init runs built-in and [custom commissioning scripts](/t/commissioning-and-hardware-testing-scripts/2482)
6.  machine shuts down
 snap-2-9-cli -->

<!-- snap-2-9-ui
1.  DHCP server is contacted
2.  kernel and initrd are received over TFTP
3.  machine boots
4.  initrd mounts a Squashfs image ephemerally over HTTP
5.  cloud-init runs built-in and [custom commissioning scripts](/t/commissioning-and-hardware-testing-scripts/2483)
6.  machine shuts down
 snap-2-9-ui -->

<!-- snap-3-0-cli
1.  DHCP server is contacted
2.  kernel and initrd are received over TFTP
3.  machine boots
4.  initrd mounts a Squashfs image ephemerally over HTTP
5.  cloud-init runs built-in and [custom commissioning scripts](/t/commissioning-and-hardware-testing-scripts/3865)
6.  machine shuts down
 snap-3-0-cli -->

<!-- snap-3-0-ui
1.  DHCP server is contacted
2.  kernel and initrd are received over TFTP
3.  machine boots
4.  initrd mounts a Squashfs image ephemerally over HTTP
5.  cloud-init runs built-in and [custom commissioning scripts](/t/commissioning-and-hardware-testing-scripts/3866)
6.  machine shuts down
 snap-3-0-ui -->

The commissioning scripts will talk to the region API server to ensure that everything is in order and that eventual deployment will succeed.

MAAS chooses the latest Ubuntu LTS release as the default image for commissioning.  If desired, you can select a different image in the "Settings" page of the web UI, by selecting the "General" tab and then scrolling down to the Commissioning section.

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 
To commission a machine:

``` bash
maas $PROFILE machine commission $SYSTEM_ID
```

[note]
To commission a node, it must have a status of "New".
[/note]

To commission all nodes in the "New" state:

``` bash
maas $PROFILE machines accept-all
```

You have the option of setting some parameters to change how commissioning runs:

1. `enable_ssh`: Optional integer. Controls whether to enable SSH for the commissioning environment using the user's SSH key(s). '1' == True, '0' == False. Roughly equivalent to the **Allow SSH access and prevent machine powering off** in the web UI.

2. `skip_bmc_config`: Optional integer.  Controls whether to skip re-configuration of the BMC for IPMI based machines. '1' == True, '0' == False.

3. `skip_networking`: Optional integer.  Controls whether to skip re-configuring the networking on the machine after the commissioning has completed. '1' == True, '0' == False. Roughly equivalent to **Retain network configuration** in the web UI.

4. `skip_storage`: Optional integer.  Controls hether to skip re-configuring the storage on the machine after the commissioning has completed. '1' == True, '0' == False.  Roughly equivalent to **Retain storage configuration** in the web UI.

5. `commissioning_scripts`: Optional string.  A comma separated list of commissioning script names and tags to be run. By default all custom commissioning scripts are run. Built-in commissioning scripts always run. Selecting `update_firmware` or `configure_hba` will run firmware updates or configure HBA's on matching machines.

6. `testing_scripts`: Optional string.  A comma seperated list of testing script names and tags to be run. By default all tests tagged `commissioning` will be run. Set to `none` to disable running tests.

7. `parameters`: Optional string.  Scripts selected to run may define their own parameters. These parameters may be passed using the parameter name. Optionally a parameter may have the script name prepended to have that parameter only apply to that specific script.

snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli  snap-3-0-cli deb-3-0-cli -->

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
To commission, on the "Machines" page, select a machine and choose "Commission" under the "Take action" drop-down menu.

<a href="https://discourse.maas.io/uploads/default/original/1X/5f196ca5e175e3f37d7cffbb2341fb0ee9cee16a.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/5f196ca5e175e3f37d7cffbb2341fb0ee9cee16a.png"></a>

You have the option of selecting some extra parameters (checkboxes) and performing hardware tests.

These options include:

-   **Allow SSH access and prevent machine powering off**: Machines are normally powered off after commissioning. This option keeps the machine on and enables SSH so you can access the machine.
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui -->

<!-- deb-2-7-ui
-   **Retain network configuration**: When enabled, preserves any custom network settings previously configured for the machine. See [Networking](/t/networking/2953) for more information.

-   **Retain storage configuration**: When enabled, preserves any storage settings previously configured for the machine. See [Storage](/t/storage/3109) for more details.

-   **Update firmware**: Runs scripts tagged with `update_firmware`. See [Testing scripts](/t/commissioning-and-hardware-testing-scripts/2485#heading--automatic-script-selection-by-hardware-type) for more details.

-   **Configure HBA**: Runs scripts tagged with `configure_hba`. As above, see [Testing scripts](/t/commissioning-and-hardware-testing-scripts/2485#heading--automatic-script-selection-by-hardware-type) for further details.
 deb-2-7-ui -->

<!-- deb-2-8-ui
-   **Retain network configuration**: When enabled, preserves any custom network settings previously configured for the machine. See [Networking](/t/networking/2955) for more information.

-   **Retain storage configuration**: When enabled, preserves any storage settings previously configured for the machine. See [Storage](/t/storage/3111) for more details.

-   **Update firmware**: Runs scripts tagged with `update_firmware`. See [Testing scripts](/t/commissioning-and-hardware-testing-scripts/2487#heading--automatic-script-selection-by-hardware-type) for more details.

-   **Configure HBA**: Runs scripts tagged with `configure_hba`. As above, see [Testing scripts](/t/commissioning-and-hardware-testing-scripts/2487#heading--automatic-script-selection-by-hardware-type) for further details.
 deb-2-8-ui -->

<!-- deb-2-9-ui
-   **Retain network configuration**: When enabled, preserves any custom network settings previously configured for the machine. See [Networking](/t/networking/2957) for more information.

-   **Retain storage configuration**: When enabled, preserves any storage settings previously configured for the machine. See [Storage](/t/storage/3113) for more details.

-   **Update firmware**: Runs scripts tagged with `update_firmware`. See [Testing scripts](/t/commissioning-and-hardware-testing-scripts/2489#heading--automatic-script-selection-by-hardware-type) for more details.

-   **Configure HBA**: Runs scripts tagged with `configure_hba`. As above, see [Testing scripts](/t/commissioning-and-hardware-testing-scripts/2489#heading--automatic-script-selection-by-hardware-type) for further details.
 deb-2-9-ui -->

<!-- deb-3-0-ui
-   **Retain network configuration**: When enabled, preserves any custom network settings previously configured for the machine. See [Networking](/t/networking/4048) for more information.

-   **Retain storage configuration**: When enabled, preserves any storage settings previously configured for the machine. See [Storage](/t/storage/4108) for more details.

-   **Update firmware**: Runs scripts tagged with `update_firmware`. See [Testing scripts](/t/commissioning-and-hardware-testing-scripts/3868#heading--automatic-script-selection-by-hardware-type) for more details.

-   **Configure HBA**: Runs scripts tagged with `configure_hba`. As above, see [Testing scripts](/t/commissioning-and-hardware-testing-scripts/3868#heading--automatic-script-selection-by-hardware-type) for further details.
 deb-3-0-ui -->

<!-- snap-2-7-ui
-   **Retain network configuration**: When enabled, preserves any custom network settings previously configured for the machine. See [Networking](/t/networking/2947) for more information.

-   **Retain storage configuration**: When enabled, preserves any storage settings previously configured for the machine. See [Storage](/t/storage/3103) for more details.

-   **Update firmware**: Runs scripts tagged with `update_firmware`. See [Testing scripts](/t/commissioning-and-hardware-testing-scripts/2479#heading--automatic-script-selection-by-hardware-type) for more details.

-   **Configure HBA**: Runs scripts tagged with `configure_hba`. As above, see [Testing scripts](/t/commissioning-and-hardware-testing-scripts/2479#heading--automatic-script-selection-by-hardware-type) for further details.
 snap-2-7-ui -->

<!-- snap-2-8-ui
-   **Retain network configuration**: When enabled, preserves any custom network settings previously configured for the machine. See [Networking](/t/networking/2949) for more information.

-   **Retain storage configuration**: When enabled, preserves any storage settings previously configured for the machine. See [Storage](/t/storage/3105) for more details.

-   **Update firmware**: Runs scripts tagged with `update_firmware`. See [Testing scripts](/t/commissioning-and-hardware-testing-scripts/2481#heading--automatic-script-selection-by-hardware-type) for more details.

-   **Configure HBA**: Runs scripts tagged with `configure_hba`. As above, see [Testing scripts](/t/commissioning-and-hardware-testing-scripts/2481#heading--automatic-script-selection-by-hardware-type) for further details.
 snap-2-8-ui -->

<!-- snap-2-9-ui
-   **Retain network configuration**: When enabled, preserves any custom network settings previously configured for the machine. See [Networking](/t/networking/2951) for more information.

-   **Retain storage configuration**: When enabled, preserves any storage settings previously configured for the machine. See [Storage](/t/storage/3107) for more details.

-   **Update firmware**: Runs scripts tagged with `update_firmware`. See [Testing scripts](/t/commissioning-and-hardware-testing-scripts/2483#heading--automatic-script-selection-by-hardware-type) for more details.

-   **Configure HBA**: Runs scripts tagged with `configure_hba`. As above, see [Testing scripts](/t/commissioning-and-hardware-testing-scripts/2483#heading--automatic-script-selection-by-hardware-type) for further details.
 snap-2-9-ui -->

<!-- snap-3-0-ui
-   **Retain network configuration**: When enabled, preserves any custom network settings previously configured for the machine. See [Networking](/t/networking/4046) for more information.

-   **Retain storage configuration**: When enabled, preserves any storage settings previously configured for the machine. See [Storage](/t/storage/4106) for more details.

-   **Update firmware**: Runs scripts tagged with `update_firmware`. See [Testing scripts](/t/commissioning-and-hardware-testing-scripts/3866#heading--automatic-script-selection-by-hardware-type) for more details.

-   **Configure HBA**: Runs scripts tagged with `configure_hba`. As above, see [Testing scripts](/t/commissioning-and-hardware-testing-scripts/3866#heading--automatic-script-selection-by-hardware-type) for further details.
 snap-3-0-ui -->

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
<a href="https://discourse.maas.io/uploads/default/original/1X/5f196ca5e175e3f37d7cffbb2341fb0ee9cee16a.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/5f196ca5e175e3f37d7cffbb2341fb0ee9cee16a.png"></a>
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui  -->

<!-- deb-2-7-ui
Click the Hardware tests field to reveal a drop-down list of tests to add and run during commissioning. See [Hardware testing](/t/hardware-testing/2677)) for more information on hardware testing scripts.
 deb-2-7-ui -->

<!-- deb-2-8-ui
Click the Hardware tests field to reveal a drop-down list of tests to add and run during commissioning. See [Hardware testing](/t/hardware-testing/2679)) for more information on hardware testing scripts.
 deb-2-8-ui -->

<!-- deb-2-9-ui
Click the Hardware tests field to reveal a drop-down list of tests to add and run during commissioning. See [Hardware testing](/t/hardware-testing/2681)) for more information on hardware testing scripts.
 deb-2-9-ui -->

<!-- deb-3-0-ui
Click the Hardware tests field to reveal a drop-down list of tests to add and run during commissioning. See [Hardware testing](/t/hardware-testing/3944)) for more information on hardware testing scripts.
 deb-3-0-ui -->

<!-- snap-2-7-ui
Click the Hardware tests field to reveal a drop-down list of tests to add and run during commissioning. See [Hardware testing](/t/hardware-testing/2671)) for more information on hardware testing scripts.
 snap-2-7-ui -->

<!-- snap-2-8-ui
Click the Hardware tests field to reveal a drop-down list of tests to add and run during commissioning. See [Hardware testing](/t/hardware-testing/2673)) for more information on hardware testing scripts.
 snap-2-8-ui -->

<!-- snap-2-9-ui
Click the Hardware tests field to reveal a drop-down list of tests to add and run during commissioning. See [Hardware testing](/t/hardware-testing/2675)) for more information on hardware testing scripts.
 snap-2-9-ui -->

<!-- snap-3-0-ui
Click the Hardware tests field to reveal a drop-down list of tests to add and run during commissioning. See [Hardware testing](/t/hardware-testing/3942)) for more information on hardware testing scripts.
 snap-3-0-ui -->

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
Finalise the directive by hitting "Commission machine".

While commissioning, the machine status will change to reflect this state (Commissioning).  MAAS discovers the machine's network topology.  MAAS then prompts a machine network interface to connect to the fabric, VLAN, and subnet combination for configuration. Usually, MAAS assigns a static IP address out of the reserved IP range for the subnet ("Auto assign" mode). The next section details several assignment modes.

Once commissioned, a machine's status will change to Ready, and an extra tab for the machine called "Commissioning" will become available. This tab contains the results of the scripts executed during the commissioning process.
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui  -->

<!-- deb-2-7-cli
Once commissioned, you may consider [creating or applying a tag](/t/maas-tags/2892) to this machine.  The next step is [deployment](/t/deploy-machines/2604).
 deb-2-7-cli -->

<!-- deb-2-7-ui
Once commissioned, you may consider [creating or applying a tag](/t/maas-tags/2893) to this machine.  The next step is [deployment](/t/deploy-machines/2605).
 deb-2-7-ui -->

<!-- deb-2-8-cli
Once commissioned, you may consider [creating or applying a tag](/t/maas-tags/2894) to this machine.  The next step is [deployment](/t/deploy-machines/2606).
 deb-2-8-cli -->

<!-- deb-2-8-ui
Once commissioned, you may consider [creating or applying a tag](/t/maas-tags/2895) to this machine.  The next step is [deployment](/t/deploy-machines/2607).
 deb-2-8-ui -->

<!-- deb-2-9-cli
Once commissioned, you may consider [creating or applying a tag](/t/maas-tags/2896) to this machine.  The next step is [deployment](/t/deploy-machines/2608).
 deb-2-9-cli -->

<!-- deb-2-9-ui
Once commissioned, you may consider [creating or applying a tag](/t/maas-tags/2897) to this machine.  The next step is [deployment](/t/deploy-machines/2609).
 deb-2-9-ui -->

<!-- deb-3-0-cli
Once commissioned, you may consider [creating or applying a tag](/t/maas-tags/4023) to this machine.  The next step is [deployment](/t/deploy-machines/3915).
 deb-3-0-cli -->

<!-- deb-3-0-ui
Once commissioned, you may consider [creating or applying a tag](/t/maas-tags/4024) to this machine.  The next step is [deployment](/t/deploy-machines/3916).
 deb-3-0-ui -->

<!-- snap-2-7-cli
Once commissioned, you may consider [creating or applying a tag](/t/maas-tags/2886) to this machine.  The next step is [deployment](/t/deploy-machines/2598).
 snap-2-7-cli -->

<!-- snap-2-7-ui
Once commissioned, you may consider [creating or applying a tag](/t/maas-tags/2887) to this machine.  The next step is [deployment](/t/deploy-machines/2599.
 snap-2-7-ui -->

<!-- snap-2-8-cli
Once commissioned, you may consider [creating or applying a tag](/t/maas-tags/2888) to this machine.  The next step is [deployment](/t/deploy-machines/2600).
 snap-2-8-cli -->

<!-- snap-2-8-ui
Once commissioned, you may consider [creating or applying a tag](/t/maas-tags/2889) to this machine.  The next step is [deployment](/t/deploy-machines/2601).
 snap-2-8-ui -->

<!-- snap-2-9-cli
Once commissioned, you may consider [creating or applying a tag](/t/maas-tags/2890) to this machine.  The next step is [deployment](/t/deploy-machines/2602).
 snap-2-9-cli -->

<!-- snap-2-9-ui
Once commissioned, you may consider [creating or applying a tag](/t/maas-tags/2891) to this machine.  The next step is [deployment](/t/deploy-machines/2603).
 snap-2-9-ui -->

<!-- snap-3-0-cli
Once commissioned, you may consider [creating or applying a tag](/t/maas-tags/4021) to this machine.  The next step is [deployment](/t/deploy-machines/3913).
 snap-3-0-cli -->

<!-- snap-3-0-ui
Once commissioned, you may consider [creating or applying a tag](/t/maas-tags/4022) to this machine.  The next step is [deployment](/t/deploy-machines/3914).
 snap-3-0-ui -->


<a href="#heading--numa-sriov-commissioning"><h3 id="heading--numa-sriov-commissioning">Commission NUMA and SR-IOV nodes</h3></a>

If you are using the NUMA architecture, MAAS versions 2.7 and higher guarantee that machines are assigned to a single NUMA node that contains all the machine's resources. Node boundaries are critical, especially in vNUMA situations.  Splitting nodes can create unnecessary latency.  You want the NUMA node boundaries to match VM boundaries if at all possible.

[note]
You must recommission NUMA/SR-IOV machines that were previously commissioned under version 2.6 or earlier.
[/note]

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
<a href="https://discourse.maas.io/uploads/default/original/1X/7b47235ff57a570ccba6a6ed09186a3d7483f5a4.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/7b47235ff57a570ccba6a6ed09186a3d7483f5a4.png"></a> 

When using these nodes, you can specify a node index for interfaces and physical block devices.  MAAS will display the NUMA node index and details, depending upon your configuration, to include the count of NUMA nodes, number of CPU cores, memory, NICs, and node spaces for bonds and block devices.  You can also filter machines by CPU cores, memory, subnet, VLAN, fabric, space, storage, and RAID, among others.
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui  -->

<a href="#heading--commissioning-scripts"><h2 id="heading--commissioning-scripts">MAAS commissioning scripts</h2></a>

When a machine boots, MAAS first instructs it to run cloud-init to set up SSH keys (during commissioning only), set up NTP, and execute a script that runs other commissioning scripts.  Currently, the sequence of MAAS-provided commissioning scripts proceeds like this:

<!-- snap-2-9-ui snap-2-9-cli deb-2-9-ui deb-2-9-cli snap-3-0-ui deb-3-0-ui snap-3-0-cli deb-3-0-cli
* **maas-support-info:** MAAS gathers information that helps to identify and characterise the machine for debugging purposes, such as the kernel, versioning of various components, etc.  **Runs in parallel with other scripts.**

* **maas-lshw:** this script pulls system BIOS and vendor info, and generates user-defined tags for later use.  **Runs in parallel with other scripts.**

* **20-maas-01-install-lldpd:** this script installs the link layer discovery protocol (LLDP) daemon, which will later capture networking information about the machine.  This script provides some extensive logging.

* **maas-list-modaliases:** this script figures out what hardware modules are loaded, providing a way to autorun certain scripts based on which modules are loaded.  **Runs in parallel with other scripts.**

* **20-maas-02-dhcp-unconfigured-ifaces:** MAAS will want to know all the ways the machine is connected to the network.  Only PXE comes online during boot; this script brings all the other networks online so they can be recognised.  This script provides extensive logging.

* **maas-get-fruid-api-data:** this script gathers information for the Facebook wedge power type.  **Runs in parallel with other scripts.**

* **maas-serial-ports:** this script lists what serial ports are available on the machine.  **Runs in parallel with other scripts.**
snap-2-9-ui snap-2-9-cli deb-2-9-ui deb-2-9-cli snap-3-0-ui deb-3-0-ui snap-3-0-cli deb-3-0-cli -->

<!-- snap-2-9-ui snap-2-9-cli deb-2-9-ui deb-2-9-cli
* **40-maas-01-network-interfaces:** this script is just used to get the IP address, which can then be associated with a VLAN/subnet.
 snap-2-9-ui snap-2-9-cli deb-2-9-ui deb-2-9-cli -->

<!-- snap-2-9-ui snap-2-9-cli deb-2-9-ui deb-2-9-cli 
* **50-maas-01-commissioning:** this script is the main MAAS tool, gathering information on machine resources, such as storage, network devices, CPU, RAM, etc.  We currently pull this data using lxd: We use a Go binary built from lxd source that just contains the minimum source to gather the resource information we need.  This script also checks whether the machine being commissioning is a virtual machine, which may affect how MAAS interacts with it.
 snap-2-9-ui snap-2-9-cli deb-2-9-ui deb-2-9-cli -->

<!-- snap-3-0-ui snap-3-0-cli deb-3-0-ui deb-3-0-cli
* **50-maas-01-commissioning:** this script is the main MAAS tool, gathering information on machine resources, such as storage, network devices, CPU, RAM, details about attached USB and PCI devices, etc.  We currently pull this data using lxd: We use a Go binary built from lxd source that just contains the minimum source to gather the resource information we need.  This script also checks whether the machine being commissioning is a virtual machine, which may affect how MAAS interacts with it.
 snap-3-0-ui snap-3-0-cli deb-3-0-ui deb-3-0-cli -->

<!-- snap-2-9-ui snap-2-9-cli deb-2-9-ui deb-2-9-cli snap-3-0-ui deb-3-0-ui snap-3-0-cli deb-3-0-cli
* **maas-capture-lldp:** this script gathers LLDP network information to be presented on the logs page; this data is not used by MAAS at all.  **Runs in parallel with other scripts.**

* **maas-kernel-cmdline:** this script is used to update the boot devices; it double-checks that the right boot interface is selected. 

Commissioning runs the same dozen or so scripts as enlistment, gathering all the same information, but with these seven caveats: 

1. Commissioning also runs user-supplied commissioning scripts, if present.  Be aware that these scripts run as root, so they can execute any system command.

2. Commissioning runs test scripts which are not run during enlistment.

3. Commissioning scripts can send BMC configuration data, and can be used to configure BMC data.

4. The environment variable BMC_CONFIG_PATH is passed to serially run commissioning scripts; these scripts may write BMC power credentials to BMC_CONFIG_PATH in YAML format, where each key is a power parameter.  The first script to write BMC_CONFIG_PATH is the only script allowed to configure the BMC, allowing you to override MAAS' built-in BMC detection.  If the script returns 0, that value will be send to MAAS.

5. All built-in commissioning scripts have been migrated into the database.

6. `maas-run-remote-scripts` is capable of enlisting machines, so enlistment `user-data` scripts have been removed.

7. The metadata endpoints `http://<MAAS>:5240/<latest or 2012-03-01>/` and `http://<MAAS>:5240/<latest or 2012-03-01>/meta-data/` are now available anonymously for use during enlistment.
snap-2-9-ui snap-2-9-cli deb-2-9-ui deb-2-9-cli snap-3-0-cli deb-3-0-cli snap-3-0-ui deb-3-0-ui -->

<!-- snap-2-8-ui snap-2-8-cli snap-2-7-ui snap-2-7-cli deb-2-8-ui deb-2-8-cli deb-2-7-ui deb-2-7-cli
* **00-maas-00-support-info:** MAAS gathers information that helps to identify and characterise the machine for debugging purposes, such as the kernel, versioning of various components, etc.

* **00-maas-01-lshw:** this script pulls system BIOS and vendor info, and generates user-defined tags for later use.

* **00-maas-03-install-lldpd:** this script installs the link layer discovery protocol (LLDP) daemon, which will later capture networking information about the machine.  The lldpd needs to be installed early because it requires about a 60-second delay before running.

* **00-maas-04-list-modaliases:** this script figures out what hardware modules are loaded, providing a way to autorun certain scripts based on which modules are loaded.

* **00-maas-05-dhcp-unconfigured-ifaces:** MAAS will want to know all the ways the machine is connected to the network.  Only PXE comes online during boot; this script brings all the other networks online so they can be recognised.

* **00-maas-06-get-fruid-api-data:** this script gathers information for the Facebook wedge power type.

* **00-maas-08-serial-ports:** this script lists what serial ports are available on the machine.

* **40-maas-01-network-interfaces:** this script is just used to get the IP address, which can then be associated with a VLAN/subnet.

* **50-maas-01-commissioning:** this script is the main MAAS tool, gathering information on machine resources, such as storage, network devices, CPU, RAM, etc.  We currently pull this data using lxd: We use a Go binary built from lxd source that just contains the minimum source to gather the resource information we need.  This script also checks whether the machine being commissioning is a virtual machine, which may affect how MAAS interacts with it.

* **99-maas-01-capture-lldp:** this script gathers LLDP network information to be presented on the logs page; this data is not used by MAAS at all.

* **99-maas-05-kernel-cmdline:** this script is used to update the boot devices; it double-checks that the right boot interface is selected.

Commissioning runs the same dozen or so scripts as enlistment, gathering all the same information, but with these two caveats: 

1. Commissioning also runs user-supplied commissioning scripts, if present.  Be aware that these scripts run as root, so they can execute any system command.

2. Commissioning runs test scripts which are not run during enlistment.
snap-2-8-ui snap-2-8-cli snap-2-7-ui snap-2-7-cli deb-2-8-ui deb-2-8-cli deb-2-7-ui deb-2-7-cli -->

In both enlistment and commissioning, MAAS uses either the MAC address or the UUID to identify machines.  Currently, because some machine types encountered by MAAS do **not** use unique MAC addresses, we are trending toward using the UUID.

<a href="#heading--post-commission-configuration"><h2 id="heading--post-commission-configuration">Post-commission configuration</h2></a>

<!-- deb-2-7-cli
Once commissioned, you can configure the machine's network interface(s). Specifically, when a machine's status is either "Ready" or "Broken", interfaces can be added/removed, attached to a fabric and linked to a subnet, and provided an IP assignment mode. Tags can also be assigned to specific network interfaces (see [Tags for network interfaces](/t/maas-tags/2892#heading--tags-for-network-interfaces)).
 deb-2-7-cli -->

<!-- deb-2-7-ui
Once commissioned, you can configure the machine's network interface(s). Specifically, when a machine's status is either "Ready" or "Broken", interfaces can be added/removed, attached to a fabric and linked to a subnet, and provided an IP assignment mode. Tags can also be assigned to specific network interfaces (see [Tags for network interfaces](/t/maas-tags/2893#heading--tags-for-network-interfaces)).
 deb-2-7-ui -->

<!-- deb-2-8-cli
Once commissioned, you can configure the machine's network interface(s). Specifically, when a machine's status is either "Ready" or "Broken", interfaces can be added/removed, attached to a fabric and linked to a subnet, and provided an IP assignment mode. Tags can also be assigned to specific network interfaces (see [Tags for network interfaces](/t/maas-tags/2894#heading--tags-for-network-interfaces)).
 deb-2-8-cli -->

<!-- deb-2-8-ui
Once commissioned, you can configure the machine's network interface(s). Specifically, when a machine's status is either "Ready" or "Broken", interfaces can be added/removed, attached to a fabric and linked to a subnet, and provided an IP assignment mode. Tags can also be assigned to specific network interfaces (see [Tags for network interfaces](/t/maas-tags/2895#heading--tags-for-network-interfaces)).
 deb-2-8-ui -->

<!-- deb-2-9-cli
Once commissioned, you can configure the machine's network interface(s). Specifically, when a machine's status is either "Ready" or "Broken", interfaces can be added/removed, attached to a fabric and linked to a subnet, and provided an IP assignment mode. Tags can also be assigned to specific network interfaces (see [Tags for network interfaces](/t/maas-tags/2896#heading--tags-for-network-interfaces)).
 deb-2-9-cli -->

<!-- deb-2-9-ui
Once commissioned, you can configure the machine's network interface(s). Specifically, when a machine's status is either "Ready" or "Broken", interfaces can be added/removed, attached to a fabric and linked to a subnet, and provided an IP assignment mode. Tags can also be assigned to specific network interfaces (see [Tags for network interfaces](/t/maas-tags/2897#heading--tags-for-network-interfaces)).
 deb-2-9-ui -->

<!-- deb-3-0-cli
Once commissioned, you can configure the machine's network interface(s). Specifically, when a machine's status is either "Ready" or "Broken", interfaces can be added/removed, attached to a fabric and linked to a subnet, and provided an IP assignment mode. Tags can also be assigned to specific network interfaces (see [Tags for network interfaces](/t/maas-tags/4023#heading--tags-for-network-interfaces)).
 deb-3-0-cli -->

<!-- deb-3-0-ui
Once commissioned, you can configure the machine's network interface(s). Specifically, when a machine's status is either "Ready" or "Broken", interfaces can be added/removed, attached to a fabric and linked to a subnet, and provided an IP assignment mode. Tags can also be assigned to specific network interfaces (see [Tags for network interfaces](/t/maas-tags/4024#heading--tags-for-network-interfaces)).
 deb-3-0-ui -->

<!-- snap-2-7-cli
Once commissioned, you can configure the machine's network interface(s). Specifically, when a machine's status is either "Ready" or "Broken", interfaces can be added/removed, attached to a fabric and linked to a subnet, and provided an IP assignment mode. Tags can also be assigned to specific network interfaces (see [Tags for network interfaces](/t/maas-tags/2886#heading--tags-for-network-interfaces)).
 snap-2-7-cli -->

<!-- snap-2-7-ui
Once commissioned, you can configure the machine's network interface(s). Specifically, when a machine's status is either "Ready" or "Broken", interfaces can be added/removed, attached to a fabric and linked to a subnet, and provided an IP assignment mode. Tags can also be assigned to specific network interfaces (see [Tags for network interfaces](/t/maas-tags/2887#heading--tags-for-network-interfaces)).
 snap-2-7-ui -->

<!-- snap-2-8-cli
Once commissioned, you can configure the machine's network interface(s). Specifically, when a machine's status is either "Ready" or "Broken", interfaces can be added/removed, attached to a fabric and linked to a subnet, and provided an IP assignment mode. Tags can also be assigned to specific network interfaces (see [Tags for network interfaces](/t/maas-tags/2888#heading--tags-for-network-interfaces)).
 snap-2-8-cli -->

<!-- snap-2-8-ui
Once commissioned, you can configure the machine's network interface(s). Specifically, when a machine's status is either "Ready" or "Broken", interfaces can be added/removed, attached to a fabric and linked to a subnet, and provided an IP assignment mode. Tags can also be assigned to specific network interfaces (see [Tags for network interfaces](/t/maas-tags/2889#heading--tags-for-network-interfaces)).
 snap-2-8-ui -->

<!-- snap-2-9-cli
Once commissioned, you can configure the machine's network interface(s). Specifically, when a machine's status is either "Ready" or "Broken", interfaces can be added/removed, attached to a fabric and linked to a subnet, and provided an IP assignment mode. Tags can also be assigned to specific network interfaces (see [Tags for network interfaces](/t/maas-tags/2890#heading--tags-for-network-interfaces)).
 snap-2-9-cli -->

<!-- snap-2-9-ui
Once commissioned, you can configure the machine's network interface(s). Specifically, when a machine's status is either "Ready" or "Broken", interfaces can be added/removed, attached to a fabric and linked to a subnet, and provided an IP assignment mode. Tags can also be assigned to specific network interfaces (see [Tags for network interfaces](/t/maas-tags/2891#heading--tags-for-network-interfaces)).
 snap-2-9-ui -->

<!-- snap-3-0-cli
Once commissioned, you can configure the machine's network interface(s). Specifically, when a machine's status is either "Ready" or "Broken", interfaces can be added/removed, attached to a fabric and linked to a subnet, and provided an IP assignment mode. Tags can also be assigned to specific network interfaces (see [Tags for network interfaces](/t/maas-tags/4021#heading--tags-for-network-interfaces)).
 snap-3-0-cli -->

<!-- snap-3-0-ui
Once commissioned, you can configure the machine's network interface(s). Specifically, when a machine's status is either "Ready" or "Broken", interfaces can be added/removed, attached to a fabric and linked to a subnet, and provided an IP assignment mode. Tags can also be assigned to specific network interfaces (see [Tags for network interfaces](/t/maas-tags/4022#heading--tags-for-network-interfaces)).
 snap-3-0-ui -->

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
From a machine's "Interfaces" page, click the menu icon for the interface to be edited and select "Edit Physical" from the resulting menu:

<a href="https://discourse.maas.io/uploads/default/original/1X/438475b8906736b45fc809cd105a56be5052397d.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/438475b8906736b45fc809cd105a56be5052397d.png"></a>

The following window will appear:

<a href="https://discourse.maas.io/uploads/default/original/1X/70b21d256df52399ac7ab09c3051f4bf011da55e.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/70b21d256df52399ac7ab09c3051f4bf011da55e.png"></a>

Four modes determine how a subnet address is assigned when MAAS deploys the machine. You can select one of these modes by clicking on the "IP mode" drop-down menu.
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui -->

<!-- deb-2-7-ui
-   **Auto assign**: MAAS will assign a random static address (`iface eth0 inet static`). The pool of available addresses depends on whether the subnet is managed or unmanaged (see [Subnet management](/t/subnet-management/3121)).
 deb-2-7-ui -->

<!-- deb-2-8-ui
-   **Auto assign**: MAAS will assign a random static address (`iface eth0 inet static`). The pool of available addresses depends on whether the subnet is managed or unmanaged (see [Subnet management](/t/subnet-management/3123)).
 deb-2-8-ui -->

<!-- deb-2-9-ui
-   **Auto assign**: MAAS will assign a random static address (`iface eth0 inet static`). The pool of available addresses depends on whether the subnet is managed or unmanaged (see [Subnet management](/t/subnet-management/3125)).
 deb-2-9-ui -->

<!-- deb-3-0-ui
-   **Auto assign**: MAAS will assign a random static address (`iface eth0 inet static`). The pool of available addresses depends on whether the subnet is managed or unmanaged (see [Subnet management](/t/subnet-management/4112)).
 deb-3-0-ui -->

<!-- snap-2-7-ui
-   **Auto assign**: MAAS will assign a random static address (`iface eth0 inet static`). The pool of available addresses depends on whether the subnet is managed or unmanaged (see [Subnet management](/t/subnet-management/3115)).
 snap-2-7-ui -->

<!-- snap-2-8-ui
-   **Auto assign**: MAAS will assign a random static address (`iface eth0 inet static`). The pool of available addresses depends on whether the subnet is managed or unmanaged (see [Subnet management](/t/subnet-management/3117)).
 snap-2-8-ui -->

<!-- snap-2-9-ui
-   **Auto assign**: MAAS will assign a random static address (`iface eth0 inet static`). The pool of available addresses depends on whether the subnet is managed or unmanaged (see [Subnet management](/t/subnet-management/3119)).
 snap-2-9-ui -->

<!-- snap-3-0-ui
-   **Auto assign**: MAAS will assign a random static address (`iface eth0 inet static`). The pool of available addresses depends on whether the subnet is managed or unmanaged (see [Subnet management](/t/subnet-management/4110)).
 snap-3-0-ui -->

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui

-   **Static assign**: The administrator will specify a static address using a secondary field.

-   **DHCP**: The machine leases a dynamic IP address, via either MAAS-managed DHCP or an external DHCP server.

-   **Unconfigured**: The interface is not configured.

Press the "Save" button to apply the changes.
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui -->

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 
If you want to edit the IP assignment mode of a network interface, the existing subnet link first needs to be removed.

Begin by finding the interface ID as well as the interface's subnet link ID with the command:

``` bash
maas $PROFILE node read $SYSTEM_ID
```

Once that's done, proceed to unlink and link:

``` bash
maas $PROFILE interface unlink-subnet $SYSTEM_ID $INTERFACE_ID id=$SUBNET_LINK_ID
maas $PROFILE interface link-subnet $SYSTEM_ID $INTERFACE_ID mode=$IP_MODE subnet=$SUBNET_CIDR [$OPTIONS]
```

For instance, to have interface `58`, with subnet link `146`, on machine `exqn37` use DHCP on subnet `192.168.1.0/24`:

``` bash
maas $PROFILE interface unlink-subnet exqn37 58 id=146
maas $PROFILE interface link-subnet exqn37 58 mode=dhcp subnet=192.168.1.0/24
```

If instead of DHCP, you desire a static address, then the second command would look like this:

``` bash
maas $PROFILE interface link-subnet exqn37 58 mode=static subnet=192.168.1.0/24 ip_address=192.168.1.113
```
snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli  snap-3-0-cli deb-3-0-cli -->

See [Concepts and terms](/t/concepts-and-terms/785#heading--ip-ranges) for the definitions of reserved range types.

<a href="#heading--bond-interfaces"><h3 id="heading--bond-interfaces">Bond interfaces and how to create one</h3></a>

A bond interface is used to aggregate two or more physical interfaces into a single logical interface. Combining multiple network connections in parallel can increase network throughput beyond what a single NIC will allow.  It also provides some redundancy in case one of the NICs should fail.  More information about the theory behind bonded NICs is found in the [relevant IEEE standard](https://1.ieee802.org/tsn/802-1ax-rev/).

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 
A bond can be created with the following command:

```
maas $PROFILE interfaces create-bond $SYSTEM_ID name=$BOND_NAME \
parents=$IFACE1_ID mac_address=$MAC_ADDR \ 
parents=$IFACE2_ID bond_mode=$BOND_MODE \
bond_updelay=$BOND_UP bond_downdelay=$BOND_DOWN mtu=$MTU
```

Use the `parents` parameters to define which interfaces form the aggregate interface.

The `bond_updelay` and `bond_downdelay` parameters specify the number of milliseconds to wait before either enabling or disabling a slave after a failure has been detected.

The following is an example of `create-bond` in action:

```
maas admin interfaces create-bond 4efwb4 name=bond0 parents=4 \
mac_address=52:52:00:00:00:00 parents=15 bond_mode=802.3ad \
bond_updelay=200 bond_downdelay=200 mtu=9000
```

There are a wide range of bond parameters you can choose when creating a bond:

| Parameter | Type and description |
|:----------|:---------------------|
| `mac_address`| Optional string.  MAC address of the interface. |
| `tags`| Optional string.  Tags for the interface. |
| `vlan`| Optional string.  VLAN the interface is connected to. If not provided then the interface is considered disconnected. |
| `parents`| Required integer.  Parent interface ids that make this bond. |
| `bond_miimon`| Optional integer.  The link monitoring freqeuncy in milliseconds. (Default: 100). |
| `bond_downdelay`| Optional integer.  Specifies the time, in milliseconds, to wait before disabling a slave after a link failure has been detected. |
| `bond_updelay`| Optional integer.  Specifies the time, in milliseconds, to wait before enabling a slave after a link recovery has been detected. |
| `bond_lacp_rate`| Optional string.  Option specifying the rate at which to ask the link partner to transmit LACPDU packets in 802.3ad mode. Available options are ``fast`` or ``slow``. (Default: ``slow``). |
| `bond_xmit_hash_policy`| Optional string.  The transmit hash policy to use for slave selection in balance-xor, 802.3ad, and tlb modes. Possible values are: ``layer2``, ``layer2+3``, ``layer3+4``, ``encap2+3``, ``encap3+4``. (Default: ``layer2``) |
| `bond_num_grat_arp`| Optional integer.  The number of peer notifications (IPv4 ARP or IPv6 Neighbour Advertisements) to be issued after a failover. (Default: 1) |
| `mtu`| Optional integer.  Maximum transmission unit. |
| `accept_ra`| Optional boolen.  Accept router advertisements. (IPv6 only) |
| `autoconf`| Optional boolean.  Perform stateless autoconfiguration. (IPv6 only) |
| `bond_mode`| Optional string.  The operating mode of the bond.  (Default: active-backup). |

Supported bonding modes include:

| Mode | Behavior |
|:-----|:---------|
|  `balance-rr`:| Transmit packets in sequential order from the first available slave through the last. This mode provides load balancing and fault tolerance. |
|  `active-backup`| Only one slave in the bond is active. A different slave becomes active if, and only if, the active slave fails. The bond's MAC address is externally visible on only one port (network adapter) to avoid confusing the switch. |
|  `balance-xor`| Transmit based on the selected transmit hash policy. The default policy is a simple [(source MAC address XOR'd with destination MAC address XOR packet type ID) modulo slave count]. |
|  `broadcast`| Transmits everything on all slave interfaces. This mode provides fault tolerance. |
|  `802.3ad`| IEEE 802.3ad dynamic link aggregation. Creates aggregation groups that share the same speed and duplex settings. Uses all slaves in the active aggregator according to the 802.3ad specification. |
|  `balance-tlb`| Adaptive transmit load balancing: channel bonding that does not require any special switch support. |
|  `balance-alb`| Adaptive load balancing: includes balance-tlb plus receive load balancing (rlb) for IPV4 traffic, and does not require any special switch support. The receive load balancing is achieved by ARP negotiation. |

snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli  snap-3-0-cli deb-3-0-cli -->

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
A bond is created by selecting more than one interface and clicking the now-active "Create bond" button:

<a href="https://discourse.maas.io/uploads/default/original/1X/7dd772c961c9f6f871f657b0397646446a4e23e7.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/7dd772c961c9f6f871f657b0397646446a4e23e7.png"></a>

After clicking the "Create bond" button, the bond configuration pane will appear.

From the bond configuration pane, you can rename the bond, select a bond mode (see below), assign a MAC address to the aggregate device and attach one or more tags.

The interfaces aggregated into the bond interface are listed below the "Tags" field. Use the "Primary" column to select the interface to act as the primary device.

<a href="https://discourse.maas.io/uploads/default/original/1X/699a55f98f3e1a81da75d1595e40bb74c99aff8e.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/699a55f98f3e1a81da75d1595e40bb74c99aff8e.png"></a>

You can select from the following bonding modes on the "Bond mode" drop-down menu:

-   **balance-rr**: Transmit packets in sequential order from the first available slave through to the last. This mode provides load balancing and fault tolerance.

-   **active-backup**: Only one slave in the bond is active. A different slave becomes active if, and only if, the active slave fails. The bond's MAC address is externally visible on only one port (network adaptor) to avoid confusing the switch.

-   **balance-xor**: Transmit based on the selected transmit hash policy. The default policy is simple, which means that an XOR operation selects packages.  This XOR compares the source MAC address and the resultant XOR between the destination MAC address, the packet type identifier, and the modulo slave count.

-   **broadcast**: Transmit everything on all slave interfaces. This mode provides fault tolerance.

-   **802.3ad**: Creates aggregation groups that share the same speed and duplex settings. This mode utilises all slaves in the active aggregation, following the IEEE 802.3ad specification.

-   **balance-tlb**: Adaptive transmit load balancing, channel bonding that does not require any special switch support.

-   **balance-alb**: Adaptive load balancing, includes balance-tlb plus receive load balancing (rlb) for IPV4 traffic. This mode does not require any special switch support.  ARP negotiation achieves load balancing in this case.

Press the "Save" button when you're done.

[note]
The MAC address defaults to the MAC address of the primary interface.
[/note]
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui  -->

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 
A bridge interface is created with the following syntax:

```
maas $PROFILE interfaces create-bridge $SYSTEM_ID name=$BRIDGE_NAME \
parent=$IFACE_ID
```

Use `parent` to define the primary interface used for the bridge:

```
maas admin interfaces create-bridge 4efwb4 name=bridged0 parent=4
```

The following parameters may be applied when creating a bridge:

1. `name`: Optional string.  Name of the interface.

2. `mac_address`: Optional string.  MAC address of the interface.

3. `tags`: Optional string.  Tags for the interface.

4. `vlan`: Optional string.  VLAN the interface is connected to.

5. `parent`: Optional integer.  Parent interface id for this bridge interface.

6. `bridge_type`: Optional string.  The type of bridge to create. Possible values are: ``standard``, ``ovs``.

7. `bridge_stp`: Optional boolean.  Turn spanning tree protocol on or off. (Default: False).

8. `bridge_fd`: Optional integer.  Set bridge forward delay to time seconds. (Default: 15).

9. `mtu`: Optional integer.  Maximum transmission unit.

10. `accept_ra`: Optional boolean.  Accept router advertisements. (IPv6 only)

11. `autoconf`: Optional boolean.  Perform stateless autoconfiguration. (IPv6 only)

<a href="#heading--delete-bridge-interface"><h3 id="heading--delete-bridge-interface">Delete a bridge interface</h3></a>

The "delete" command can be used to delete a bridge interface, a bond interface or a physical interface:

```
maas $PROFILE interface delete $SYSTEM_ID $IFACE_ID
```

For example:

```
maas admin interface delete 4efwb4 15
```

The following is output after the successful deletion of an interface:

```
Success.
Machine-readable output follows:
```

Note that while the label is presented, there is no machine-readable output expected after the successful execution of the delete command.
snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli  -->


<a href="#heading--bridge-interfaces"><h3 id="heading--bridge-interfaces">Bridge interfaces and how to create one</h3></a>

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 

A network bridge may be useful if you intend to put virtual machines or containers on the machine.  You can create a bridge by selecting an interface and clicking the now-active "Create bridge" button. A form will appear that allows you to configure a MAC address, STP, and an appropriate tag.

<a href="https://discourse.maas.io/uploads/default/original/1X/83ef3d6f40d5b558396d96717dd2822fc1ce8b68.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/83ef3d6f40d5b558396d96717dd2822fc1ce8b68.png"></a>

Press the "Save" button when you're done.
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui  -->

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 

A bridge interface is created with the following syntax:

``` bash
maas $PROFILE interfaces create-bridge $SYSTEM_ID name=$BRIDGE_NAME \
parent=$IFACE_ID
```

Use 'parent' to define the primary interface used for the bridge:

``` bash
maas admin interfaces create-bridge 4efwb4 name=bridged0 parent=4
```


snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli  -->


<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 

<a href="#heading--assign-a-network-interface-to-a-fabric"><h2 id="heading--assign-a-network-interface-to-a-fabric">Assign a network interface to a fabric</h2></a>

 snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui  -->

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 

<a href="#heading--assign-a-network-interface-to-a-fabric"><h2 id="heading--assign-a-network-interface-to-a-fabric">Assign a network interface to a fabric</h2></a>

This task is made easier with the aid of the `jq` utility. It filters the `maas` command (JSON formatted) output and prints it in the desired way, which allows you to view and compare data quickly. Go ahead and install it:

``` bash
sudo apt install jq
```

In summary, MAAS assigns an interface to a fabric by assigning it to a VLAN. First, we need to gather various bits of data.

List some information on all machines:

``` bash
maas $PROFILE machines read | jq ".[] | \
    {hostname:.hostname, system_id: .system_id, status:.status}" --compact-output
```

Example output:

``` no-highlight
{"hostname":"machine1","system_id":"dfgnnd","status":4}
{"hostname":"machine2","system_id":"bkaf6e","status":6}
{"hostname":"machine4","system_id":"63wqky","status":6}
{"hostname":"machine3","system_id":"qwkmar","status":4}
```

[note]
You can only edit an interface when the corresponding machine has a status of 'Ready'. This state is numerically denoted by the integer '4'.
[/note]

List some information for all interfaces on the machine in question (identified by its system id 'dfgnnd'):

``` bash
maas $PROFILE interfaces read dfgnnd | jq ".[] | \
    {id:.id, name:.name, mac:.mac_address, vid:.vlan.vid, fabric:.vlan.fabric}" --compact-output
```

Example output:

``` no-highlight
{"id":8,"name":"eth0","mac":"52:54:00:01:01:01","vid":0,"fabric":"fabric-1"}
{"id":9,"name":"eth1","mac":"52:54:00:01:01:02","vid":null,"fabric":null}
```

List some information for all fabrics:

``` bash
maas $PROFILE fabrics read | jq ".[] | \
    {name:.name, vlans:.vlans[] | {id:.id, vid:.vid}}" --compact-output
```

Example output:

``` no-highlight
{"name":"fabric-0","vlans":{"id":5001,"vid":0}}
{"name":"fabric-1","vlans":{"id":5002,"vid":0}}
{"name":"fabric-2","vlans":{"id":5003,"vid":0}}
```

This example will show how to move interface '8' (on machine 'dfgnnd') from 'fabric-1' to 'fabric-0'. Based on the gathered information, this will consist of changing the interface's VLAN from '5002' to '5001':

``` bash
maas $PROFILE interface update dfgnnd 8 vlan=5001 >/dev/null
```

Verify the operation by relisting information for the machine's interface:

``` bash
maas $PROFILE interfaces read dfgnnd | jq ".[] | \
    {id:.id, name:.name, mac:.mac_address, vid:.vlan.vid, fabric:.vlan.fabric}" --compact-output
```

The output shows that the interface is now on fabric-0:

``` no-highlight
{"id":8,"name":"eth0","mac":"52:54:00:01:01:01","vid":0,"fabric":"fabric-0"}
{"id":9,"name":"eth1","mac":"52:54:00:01:01:02","vid":null,"fabric":null}
```

<a href="#heading--interface-identifiers"><h2 id="heading--interface-identifiers">Interface identifiers</h2></a>

The MAAS CLI uses a numeric interface identifier for many interface operations. Use the following command to retrieve the identifier(s):

``` bash
maas $PROFILE interfaces read $SYSTEM_ID
```

Look for either id or the number at the end of an interface's resource URI, such as **15** in the following example output:

``` json
"id": 15,
"mac_address": "52:54:00:55:06:40",
...
"name": "ens9",
...
"resource_uri": "/MAAS/api/2.0/nodes/4efwb4/interfaces/15/"
```

<a href="#heading--delete-an-interface"><h2 id="heading--delete-an-interface">Delete an interface</h2></a>

The 'delete' command can be used to delete a bridge interface, a bond interface or a physical interface:

``` bash
maas $PROFILE interface delete $SYSTEM_ID $IFACE_ID
```

For example:

``` bash
maas admin interface delete 4efwb4 15
```

The following is output after the successful deletion of an interface:

``` no-highlight
Success.
Machine-readable output follows:
```

[note]
There is no machine-readable output after the successful execution of the delete command.
[/note]

<a href="#heading--create-a-vlan-interface"><h2 id="heading--create-a-vlan-interface">Create a VLAN interface</h2></a>

To create a VLAN interface, use the following syntax:

``` bash
maas $PROFILE vlans create $FABRIC_ID name=$NAME vid=$VLAN_ID
```

For example, the following command creates a VLAN called 'Storage network:

``` bash
maas admin vlans create 0 name="Storage network" vid=100
```

The above command generates the following output:

``` no-output
Success.
Machine-readable output follows:
{
    "vid": 100,
    "mtu": 1500,
    "dhcp_on": false,
    "external_dhcp": null,
    "relay_vlan": null,
    "name": "Storage network",
    "space": "undefined",
    "fabric": "fabric-0",
    "id": 5004,
    "primary_rack": null,
    "fabric_id": 0,
    "secondary_rack": null,
    "resource_uri": "/MAAS/api/2.0/vlans/5004/"
}
```

Be aware that the $VLAN_ID parameter does not indicate a VLAN ID that corresponds to the VLAN tag. You must first create the VLAN and then associate it with the interface:

``` bash
maas $PROFILE interfaces create-vlan $SYSTEM_ID vlan=$OUTPUT_VLAN_ID \
parent=$IFACE_ID
```

[note]
**OUTPUT_VLAN_ID** corresponds to the id value output when MAAS created the VLAN.
[/note]

The following example contains values that correspond to the output above:

``` bash
maas admin interfaces create-vlan 4efwb4 vlan=5004 parent=4
```

The above command generates the following output:

``` json
Success.
Machine-readable output follows:
{
    "tags": [],
    "type": "vlan",
    "enabled": true,
    "system_id": "4efwb4",
    "id": 21,
    "children": [],
    "mac_address": "52:54:00:eb:f2:29",
    "params": {},
    "vlan": {
        "vid": 100,
        "mtu": 1500,
        "dhcp_on": false,
        "external_dhcp": null,
        "relay_vlan": null,
        "id": 5004,
        "secondary_rack": null,
        "fabric_id": 0,
        "space": "undefined",
        "fabric": "fabric-0",
        "name": "Storage network",
        "primary_rack": null,
        "resource_uri": "/MAAS/api/2.0/vlans/5004/"
    },
    "parents": [
        "ens3"
    ],
    "effective_mtu": 1500,
    "links": [
        {
            "id": 55,
            "mode": "link_up"
        }
    ],
    "discovered": null,
    "name": "ens3.100",
    "resource_uri": "/MAAS/api/2.0/nodes/4efwb4/interfaces/21/"
}
```

<a href="#heading--delete-a-vlan-interface"><h2 id="heading--delete-a-vlan-interface">Delete a VLAN interface</h2></a>

The following command outlines the syntax required to delete a VLAN interface from the command line:

``` bash
maas $PROFILE vlan delete $FABRIC__ID $VLAN_ID
```

Using the values from previous examples, you executed this step as follows:

``` bash
maas admin vlan delete 0 100
```


snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli  -->
