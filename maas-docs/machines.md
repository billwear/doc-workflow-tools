||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/machines-snap-2-7-cli/2730) ~ [UI](/t/machines-snap-2-7-ui/2731)|[CLI](/t/machines-snap-2-8-cli/2732) ~ [UI](/t/machines-snap-2-8-ui/2733)|[CLI](/t/machines-snap-2-9-cli/2734) ~ [UI](/t/machines-snap-2-9-ui/2735)|[CLI](/t/machines-snap-3-0-cli/4029) ~ [UI](/t/machines-snap-3-0-ui/4030)|
Packages|[CLI](/t/machines-deb-2-7-cli/2736) ~ [UI](/t/machines-deb-2-7-ui/2737)|[CLI](/t/machines-deb-2-8-cli/2738) ~ [UI](/t/machines-deb-2-8-ui/2739)|[CLI](/t/machines-deb-2-9-cli/2740) ~ [UI](/t/machines-deb-2-9-ui/2741)|[CLI](/t/machines-deb-3-0-cli/4031) ~ [UI](/t/machines-deb-3-0-ui/4032)|

Machines are the heart of MAAS. They are the backbone of your data centre application(s), providing the functions that are relevant to your customers. MAAS manages their transit through a life-cycle, from adding and enlistment, through commissioning, allocation, and deployment, finally being released back to the pool, or retired altogether.  You can move them around, create redundant versions (even in other geographies you can access), and basically rearrange them to the extent that your network allows.

<!-- deb-2-7-ui snap-2-7-ui deb-2-8-ui snap-2-8-ui deb-2-9-ui snap-2-9-ui
#### Eleven questions you may have:

1. [How are the machine states and actions related?](#heading--machine-life-cycle)
2. [How can I view the machine list?](#heading--machine-list)
3. [How can I view machine details?](#heading--node-details)
4. [How can I view a machine summary?](#heading--machine-summary)
5. [Where can I find network info for a machine?](#heading--machine-interfaces-h3)
6. [Where can I find storage info for a machine?](#heading--machine-storage-h3)
7. [Where can I find the commissioning log for a machine?](#heading--commissioning-log-h3)
8. [Where can I find machine hardware & test logs?](#heading--hardware-tests-h3)
9. [Where can I find raw log output for a machine?](#heading--raw-log-output-h3)
10. [Where can I find a machine's event log?](#heading--event-logs-h3)
11. [Where can I find machine configuration info?](#heading--machine-config-h3)
 deb-2-7-ui snap-2-7-ui deb-2-8-ui snap-2-8-ui deb-2-9-ui snap-2-9-ui -->

<!-- snap-3-0-ui deb-3-0-ui 
#### Twelve questions you may have:

1. [How are the machine states and actions related?](#heading--machine-life-cycle)
2. [How can I view the machine list?](#heading--machine-list)
3. [How can I view machine details?](#heading--node-details)
4. [How can I view a machine summary?](#heading--machine-summary)
5. [How does MAAS handle attached USB/PCI devices?](#heading--usb-pci-devices)
6. [Where can I find network info for a machine?](#heading--machine-interfaces-h3)
7. [Where can I find storage info for a machine?](#heading--machine-storage-h3)
8. [Where can I find the commissioning log for a machine?](#heading--commissioning-log-h3)
9. [Where can I find machine hardware & test logs?](#heading--hardware-tests-h3)
10. [Where can I find raw log output for a machine?](#heading--raw-log-output-h3)
11. [Where can I find a machine's event log?](#heading--event-logs-h3)
12. [Where can I find machine configuration info?](#heading--machine-config-h3)
 snap-3-0-ui deb-3-0-ui -->

<!-- snap-3-0-cli deb-3-0-cli 
#### Four questions you may have:

1. [How are the machine states and actions related?](#heading--machine-life-cycle)
2. [How can I view the machine list?](#heading--machine-list)
3. [How can I view machine details?](#heading--node-details)
4. [How does MAAS handle attached USB/PCI devices?](#heading--usb-pci-devices)
 snap-3-0-cli deb-3-0-cli -->

<!-- deb-2-7-cli snap-2-7-cli deb-2-8-cli snap-2-8-cli deb-2-9-cli snap-2-9-cli 
#### Three questions you may have:

1. [How are the machine states and actions related?](#heading--machine-life-cycle)
2. [How can I view the machine list?](#heading--machine-list)
3. [How can I view machine details?](#heading--node-details)
 deb-2-7-cli snap-2-7-cli deb-2-8-cli snap-2-8-cli deb-2-9-cli snap-2-9-cli -->

For example, in the illustration below, you see a typical small hospital data centre, including servers ready and allocated for functions like Pharmacy, Orders, Charts, and so on:

<!-- deb-2-7-ui snap-2-7-ui deb-2-8-ui snap-2-8-ui deb-2-9-ui snap-2-9-ui snap-3-0-ui deb-3-0-ui 
<a href="https://discourse.maas.io/uploads/default/original/1X/30df04b0bcec5fcf6538590ed795cb0514a64675.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/30df04b0bcec5fcf6538590ed795cb0514a64675.jpeg"></a> 
 deb-2-7-ui snap-2-7-ui deb-2-8-ui snap-2-8-ui deb-2-9-ui snap-2-9-ui snap-3-0-ui deb-3-0-ui  -->

<!-- deb-2-7-cli snap-2-7-cli deb-2-8-cli snap-2-8-cli deb-2-9-cli snap-2-9-cli snap-3-0-cli deb-3-0-cli 
```
FQDN               POWER  STATUS  OWNER  TAGS     POOL       NOTE  ZONE
----               -----  ------  -----  ----     ----       ----  ----
52-54-00-15-36-f2  off    Ready   -      Orders   Prescrbr   -     default
52-54-00-17-64-c8  off    Ready   -      HRMgmt   StaffComp  -     default
52-54-00-1d-47-95  off    Ready   -      MedSupp  SuppServ   -     default
52-54-00-1e-06-41  off    Ready   -      PatPrtl  BusOfc     -     default
52-54-00-1e-a5-7e  off    Ready   -      Pharm    Prescrbr   -     default
52-54-00-2e-b7-1e  off    Ready   admin  NursOrd  NurServ    -     default
52-54-00-2e-c4-40  off    Ready   admin  MedAdmn  NurServ    -     default
52-54-00-2e-ee-17  off    Ready   admin  Charts   ProServ    -     default
```
 deb-2-7-cli snap-2-7-cli deb-2-8-cli snap-2-8-cli deb-2-9-cli snap-2-9-cli  snap-3-0-cli deb-3-0-cli -->

These example machines would typically be duplicated in several different geographies, with a quick way to switch to a redundant node, should anything go wrong (e.g., high availability).  We used the word node there because, In the network language of MAAS, machines are one of several different types of nodes.  A node is simply a network-connected object or, more specifically, an object that can independently communicate on a network. MAAS nodes include controllers, network devices, and of course, machines.   

Looking back at the example above, you can see that there are several columns in the machine list:

<!-- deb-2-7-ui snap-2-7-ui deb-2-8-ui snap-2-8-ui deb-2-9-ui snap-2-9-ui snap-3-0-ui deb-3-0-ui 
<a href="https://discourse.maas.io/uploads/default/original/1X/e6339dd1439b3b54be7a75f7239d1981754a07f6.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/e6339dd1439b3b54be7a75f7239d1981754a07f6.jpeg"></a> 

The columns list eight details for each machine:

1.   **FQDN | MAC**: The fully qualified domain name or the MAC address of the machine.
2.   **Power**: 'On', 'Off' or 'Error' to highlight an error state.
3.   **Status**: The current status of the machine, such as 'Ready', 'Commissioning' or 'Failed testing'.
4.   **Owner**: The MAAS account responsible for the machine.
5.   **Cores**: The number of CPU cores detected on the machine.
6.   **RAM**: The amount of RAM, in GiB, discovered on the machine.
7.   **Disks**: The number of drives detected on the machine.
8.   **Storage**: The amount of storage, in GB, identified on the machine.

deb-2-7-ui snap-2-7-ui deb-2-8-ui snap-2-8-ui deb-2-9-ui snap-2-9-ui  snap-3-0-ui deb-3-0-ui -->

<!-- deb-2-7-cli snap-2-7-cli deb-2-8-cli snap-2-8-cli deb-2-9-cli snap-2-9-cli snap-3-0-cli deb-3-0-cli 
```
FQDN               POWER  STATUS  OWNER  TAGS     POOL       NOTE  ZONE
----               -----  ------  -----  ----     ----       ----  ----
52-54-00-15-36-f2  off    Ready   -      Orders   Prescrbr   -     default
52-54-00-17-64-c8  off    Ready   -      HRMgmt   StaffComp  -     default
```

These particular columns list eight details for each machine:

1.   **FQDN | MAC**: The fully qualified domain name or the MAC address of the machine.
2.   **Power**: 'On', 'Off' or 'Error' to highlight an error state.
3.   **Status**: The current status of the machine, such as 'Ready', 'Commissioning' or 'Failed testing'.
4.   **Owner**: The MAAS account responsible for the machine.
5.   **Tags**: Any tags assigned to a machine; these tags not only help identify how the machine is being used, they can also be used to modify kernel parameters as the machine is being (re-)deployed.
6.   **Pool**: The resource pool to which this machine is assigned; these help to reserve machines for specific functions or groups of functions.
7.   **Note**: Any notes you've elected to assign to this machine.
8.   **Zone**: The availabilty zone in which this machine is placed.

You can change the visible columns by changing the way you execute the relevant CLI command; for example, this listing can be generated with the following command:

```
maas $PROFILE machines read | jq -r '(["HOSTNAME","POWER","STATUS",
"OWNER", "TAGS", "POOL", "NOTE","ZONE"] | (., map(length*"-"))),
(.[] | [.hostname, .power_state, .status_name, .owner // "-", 
.tag_names[0] // "-", .pool.name, .note, .zone.name]) | @tsv' | column -t
```

You could easily produce a different set of columns by using this command, for example:

```
maas $PROFILE machines read | jq -r '(["HOSTNAME","SYSID","POWER","STATUS",
"OWNER", "TAGS", "POOL", "VLAN","FABRIC","SUBNET"] | (., map(length*"-"))),
(.[] | [.hostname, .system_id, .power_state, .status_name, .owner // "-", 
.tag_names[0] // "-", .pool.name,
.boot_interface.vlan.name, .boot_interface.vlan.fabric,
.boot_interface.links[0].subnet.name]) | @tsv' | column -t
```

producing a listing something like this:

```
HOSTNAME           SYSID   POWER  STATUS     OWNER  TAGS     POOL     VLAN      FABRIC   SUBNET
--------           -----   -----  ------     -----  ----     ----     ----      ------   ------
52-54-00-15-36-f2  hfqgmw  off    Allocated  admin  virtual  default  untagged  default  192.168.123.0/24
52-54-00-17-64-c8  bdn3qn  off    Allocated  admin  virtual  default
52-54-00-1d-47-95  8d8bxk  off    Allocated  admin  virtual  default  untagged  default  192.168.123.0/24
52-54-00-1e-06-41  wennwm  off    Ready      -      virtual  default  untagged  default  192.168.123.0/24
52-54-00-1e-a5-7e  ekf7ae  off    Ready      -      virtual  default  untagged  default  192.168.123.0/24
52-54-00-2e-b7-1e  y47pka  off    Ready      -      virtual  default  untagged  default  192.168.123.0/24
52-54-00-2e-c4-40  cbgkxg  off    Ready      -      virtual  default  untagged  default  192.168.123.0/24
52-54-00-2e-ee-17  ap3ttw  off    Ready      -      virtual  default  untagged  default  192.168.123.0/24
52-54-00-2f-6d-3c  c3aybg  off    Ready      -      virtual  default  untagged  default  192.168.123.0/24
52-54-00-4a-2a-30  4a33wk  off    Ready      -      virtual  default  untagged  default  192.168.123.0/24
52-54-00-4e-60-b2  a488pw  off    Ready      -      virtual  default  untagged  default  192.168.123.0/24
52-54-00-52-93-10  hhnq8x  off    Ready      -      virtual  default  untagged  default  192.168.123.0/24
52-54-00-5d-b5-a1  hxy44m  off    Ready      -      virtual  default  untagged  default  192.168.123.0/24
52-54-00-60-1e-6f  bk7mck  off    Ready      -      virtual  default  untagged  default  192.168.123.0/24
52-54-00-60-8d-4b  typh3r  off    Ready      -      virtual  default  untagged  default  192.168.123.0/24
52-54-00-62-22-e3  774dk8  off    Ready      -      virtual  default  untagged  default  192.168.123.0/24
52-54-00-65-2e-20  t8me3x  off    Ready      -      virtual  default  untagged  default  192.168.123.0/24
52-54-00-6a-ac-23  tybxhr  off    Ready      -      virtual  default  untagged  default  192.168.123.0/24
52-54-00-6f-b4-af  bs7ye8  off    Ready      -      virtual  default  untagged  default  192.168.123.0/24
52-54-00-71-0c-53  hp7pp4  off    Ready      -      virtual  default  untagged  default  192.168.123.0/24
52-54-00-77-4e-53  nq36ky  off    Ready      -      virtual  default  untagged  default  192.168.123.0/24
52-54-00-98-42-ef  gagbqp  off    Broken     -      -        default  untagged  default
52-54-00-9b-e4-9a  apkp4n  off    Ready      -      virtual  default  untagged  default  192.168.123.0/24
52-54-00-9c-51-00  rxfkqt  off    Ready      -      virtual  default  untagged  default  192.168.123.0/24
```

 deb-2-7-cli snap-2-7-cli deb-2-8-cli snap-2-8-cli deb-2-9-cli snap-2-9-cli snap-3-0-cli deb-3-0-cli  -->


<a href="#heading--machine-life-cycle"><h2 id="heading--machine-life-cycle">Machine life-cycle</h2></a>

One of the most important things to understand about machines is their life-cycle.  Machines can be discovered or added, commissioned by MAAS, acquired, deployed, released, marked broken, tested, put into rescue mode, and deleted.  In addition, pools, zones, and tags can be set for machines.

All of these states and actions represent the possible life-cycle of a machine.  This life-cycle isn't strict or linear -- it depends on how you use a machine -- but it's useful to give a general overview of how machines tend to change states.  In the discussion that follows, states and actions are shown in **bold** type.

1. Machines start as servers in your environment, attached to a network or subnet MAAS can manage.

2. If machines are configured to netboot, MAAS can **discover** them and present them to you for possible commissioning, changing their state to **New**.

3. When you select a machine that is marked **New**, you can choose to **commission** it.  If you add a machine manually, it is automatically **commissioned**.

4. Machines that have successfully commissioned can be **acquired** and **deployed**.  Machines that don't successfully commission can be **marked broken** (and later recovered when the issues are resolved).

5. Resolving problems with machines usually involve **testing** the machine.

6. Once you've deployed a machine, and you're done with it, you can **release** it.

7. You can place a machine in **rescue mode**, which allows you to SSH to a machine to make configuration changes or do other maintenance. Once you're done, you can **exit rescue mode***.

8. Any time a machine is on, you have the option to select it and **power off** that machine.

9. You can **abort** any operation that's in progress.

10. You also have the option to set tags, availability zone, or resource pool at various stages along the way.

Since these actions are not necessarily sequential, and the available actions change as the machine state changes, it's not very useful to make a state diagram or flowchart.  Instead, consider the following table:

| Action/State | New | Ready | Acquired | Deployed | Locked | Rescue | Broken |
|--------------|:---:|:-----:|:--------:|:--------:|:------:|:------:|:------:|
| Commission   | X   | X     |          |          |        |        |   X    |
| Acquire      |     | X     |          |          |        |        |        |
| Deploy       |     | X     |   X      |          |        |        |        |
| Release      |     |       |   X      |    X     |        |        |        |
| Power on     |     |       |          |    X     |        |        |   X    |
| Power off    |     |       |          |          |        |        |        |
| Test         | X   | X     |   X      |    X     |        |        |   X    |
| Rescue mode  | X   | X     |   X      |    X     |        |        |   X    |
| Exit rescue  |     |       |          |          |        |   X    |        |
| Mark broken  |     |       |   X      |    X     |        |        |        |
| Mark fixed   |     |       |          |          |        |        |   X    |
| Lock         |     |       |          |    X     |        |        |        |
| Unlock       |     |       |          |          |   X    |        |        |
| Tag          | X   | X     |   X      |    X     |        |   X    |   X    |
| Set zone     | X   | X     |   X      |    X     |        |   X    |   X    |
| Set...pool   | X   | X     |   X      |    X     |        |   X    |   X    |
| Delete       | X   | X     |   X      |    X     |        |   X    |   X    |

When a machine is in the state listed in a column, it is possible to take the row actions marked with an "X."  You access these actions from the "Take action" menu in the upper right corner of the machine listing.  Note that some actions, such as "Mark broken" or "Lock," may be hidden when they are not available.

<a href="#heading--machine-list"><h2 id="heading--machine-list">View the machine list</h2></a>

<!-- snap-2-7-ui deb-2-7-ui snap-2-8-ui deb-2-8-ui snap-2-9-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
You can view the list of machines from the choice "Machines" on the top menu of the MAAS web UI.  This action will display a table like the one above, listing all the machines that are currently visible to your MAAS installation.  During commissioning and deployment, MAAS updates the table to reflect the changing state of each machine. These values are augmented with green, amber and red icons to represent successful, in-progress and failed transitions, respectively. The MAAS web UI employs similar icons and colours throughout the interface to reflect a machine's status. 

<a href="https://discourse.maas.io/uploads/default/original/1X/19e038dbc6e669bfffc0ea5a9946432a75142bfb.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/19e038dbc6e669bfffc0ea5a9946432a75142bfb.jpeg"></a> 

Rolling the cursor over status icons often reveals more details. For example, a failed hardware test script will place a warning icon alongside the hardware type tested by the script. Rolling the cursor over this will reveal which test failed.  Likewise, you can find some immediate options by rolling over the column data items in the machines table.

<a href="https://discourse.maas.io/uploads/default/original/1X/8f78a8877a029e7a44bcd4cf3d138499637fe790.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/8f78a8877a029e7a44bcd4cf3d138499637fe790.jpeg"></a> 

The 'Add hardware' drop-down menu is used to add either new machines or a new chassis. This menu changes context when one or more machines are selected from the table, using either the individual checkboxes in the first column or the column title checkbox to select all.

<a href="https://discourse.maas.io/uploads/default/original/1X/9a0747649e6aff999d3c04335eb752accedaf3de.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/9a0747649e6aff999d3c04335eb752accedaf3de.jpeg"></a> 

With one or more machines selected, the 'Add hardware' drop-down menu moves to the left, and is joined by the 'Take action' menu.  This menu provides access to the various [machine actions](/t/concepts-and-terms/785#node-actions) that can be applied to the selected machine(s):

<a href="https://discourse.maas.io/uploads/default/original/1X/e03d5ac8de9ea4f4827ed057bb2dd83e241aac3b.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/e03d5ac8de9ea4f4827ed057bb2dd83e241aac3b.jpeg"></a> 

[note]
The 'Filter by' section limits the machines listed in the table to selected keywords and machine attributes.
[/note]
 snap-2-7-ui deb-2-7-ui snap-2-8-ui deb-2-8-ui snap-2-9-ui deb-2-9-ui  snap-3-0-ui deb-3-0-ui -->

<!-- snap-2-7-cli deb-2-7-cli snap-2-8-cli deb-2-8-cli snap-2-9-cli deb-2-9-cli  snap-3-0-cli deb-3-0-cli 
You can view a basic machine list with a command such as this one:

```
maas $PROFILE machines read | jq -r '(["HOSTNAME","SYSID","POWER","STATUS",
"OWNER", "TAGS", "POOL", "VLAN","FABRIC","SUBNET"] | (., map(length*"-"))),
(.[] | [.hostname, .system_id, .power_state, .status_name, .owner // "-", 
.tag_names[0] // "-", .pool.name,
.boot_interface.vlan.name, .boot_interface.vlan.fabric,
.boot_interface.links[0].subnet.name]) | @tsv' | column -t \
| sort -k 1
```

This action will display a table similar to this one, listing all the machines that are currently visible to your MAAS installation:

```
HOSTNAME           SYSID   POWER  STATUS     OWNER  TAGS     POOL     VLAN      FABRIC   SUBNET
--------           -----   -----  ------     -----  ----     ----     ----      ------   ------
52-54-00-15-36-f2  hfqgmw  off    Allocated  admin  virtual  default  untagged  default  192.168.123.0/24
52-54-00-17-64-c8  bdn3qn  off    Allocated  admin  virtual  default
52-54-00-1d-47-95  8d8bxk  off    Allocated  admin  virtual  default  untagged  default  192.168.123.0/24
52-54-00-1e-06-41  wennwm  off    Ready      -      virtual  default  untagged  default  192.168.123.0/24
52-54-00-1e-a5-7e  ekf7ae  off    Ready      -      virtual  default  untagged  default  192.168.123.0/24
52-54-00-2e-b7-1e  y47pka  off    Ready      -      virtual  default  untagged  default  192.168.123.0/24
52-54-00-2e-c4-40  cbgkxg  off    Ready      -      virtual  default  untagged  default  192.168.123.0/24
52-54-00-2e-ee-17  ap3ttw  off    Ready      -      virtual  default  untagged  default  192.168.123.0/24
52-54-00-2f-6d-3c  c3aybg  off    Ready      -      virtual  default  untagged  default  192.168.123.0/24
52-54-00-4a-2a-30  4a33wk  off    Ready      -      virtual  default  untagged  default  192.168.123.0/24
52-54-00-4e-60-b2  a488pw  off    Ready      -      virtual  default  untagged  default  192.168.123.0/24
52-54-00-52-93-10  hhnq8x  off    Ready      -      virtual  default  untagged  default  192.168.123.0/24
52-54-00-5d-b5-a1  hxy44m  off    Ready      -      virtual  default  untagged  default  192.168.123.0/24
52-54-00-60-1e-6f  bk7mck  off    Ready      -      virtual  default  untagged  default  192.168.123.0/24
52-54-00-60-8d-4b  typh3r  off    Ready      -      virtual  default  untagged  default  192.168.123.0/24
52-54-00-62-22-e3  774dk8  off    Ready      -      virtual  default  untagged  default  192.168.123.0/24
52-54-00-65-2e-20  t8me3x  off    Ready      -      virtual  default  untagged  default  192.168.123.0/24
52-54-00-6a-ac-23  tybxhr  off    Ready      -      virtual  default  untagged  default  192.168.123.0/24
52-54-00-6f-b4-af  bs7ye8  off    Ready      -      virtual  default  untagged  default  192.168.123.0/24
52-54-00-71-0c-53  hp7pp4  off    Ready      -      virtual  default  untagged  default  192.168.123.0/24
52-54-00-77-4e-53  nq36ky  off    Ready      -      virtual  default  untagged  default  192.168.123.0/24
52-54-00-98-42-ef  gagbqp  off    Broken     -      -        default  untagged  default
52-54-00-9b-e4-9a  apkp4n  off    Ready      -      virtual  default  untagged  default  192.168.123.0/24
52-54-00-9c-51-00  rxfkqt  off    Ready      -      virtual  default  untagged  default  192.168.123.0/24
```

During commissioning and deployment, you can re-read the table to reflect the changing state of each machine:

```
HOSTNAME           SYSID   POWER  STATUS         OWNER  TAGS     POOL     VLAN      FABRIC   SUBNET
--------           -----   -----  ------         -----  ----     ----     ----      ------   ------
52-54-00-15-36-f2  hfqgmw  off    Allocated      admin  virtual  default  untagged  default  192.168.123.0/24
52-54-00-17-64-c8  bdn3qn  off    Allocated      admin  virtual  default
52-54-00-1d-47-95  8d8bxk  off    Allocated      admin  virtual  default  untagged  default  192.168.123.0/24
52-54-00-1e-06-41  wennwm  off    Commissioning  -      virtual  default  untagged  default  192.168.123.0/24
52-54-00-1e-a5-7e  ekf7ae  off    Commissioning  -      virtual  default  untagged  default  192.168.123.0/24
52-54-00-2e-b7-1e  y47pka  off    Deployed       -      virtual  default  untagged  default  192.168.123.0/24
52-54-00-2e-c4-40  cbgkxg  off    Deploying      -      virtual  default  untagged  default  192.168.123.0/24
52-54-00-2e-ee-17  ap3ttw  off    Deploying      -      virtual  default  untagged  default  192.168.123.0/24
52-54-00-2f-6d-3c  c3aybg  off    Ready          -      virtual  default  untagged  default  192.168.123.0/24
52-54-00-4a-2a-30  4a33wk  off    Ready          -      virtual  default  untagged  default  192.168.123.0/24
52-54-00-4e-60-b2  a488pw  off    Ready          -      virtual  default  untagged  default  192.168.123.0/24
52-54-00-52-93-10  hhnq8x  off    Ready          -      virtual  default  untagged  default  192.168.123.0/24
52-54-00-5d-b5-a1  hxy44m  off    Ready          -      virtual  default  untagged  default  192.168.123.0/24
52-54-00-60-1e-6f  bk7mck  off    Ready          -      virtual  default  untagged  default  192.168.123.0/24
```

You can also add machines; at the command line, enter the following information:

```
maas $PROFILE machines create \
> architecture=$ARCH \
> max_addresses=$MAC_ADDRESS \
> power_type=$POWER_TYPE \
> power_parameters_power_id=$POWER_ID \
> power_parameters_power_address=$POWER_ADDRESS \
> power_parameters_power_pass=$POWER_PASSWORD
```

When you enter the command (substituting the $... parameters for your own particulars), the screen will pause for a moment, and then return a stream of JSON relating to the added machine.

Here’s an example with a local laptop MAAS install, using KVMs as virtual machines:

```
stormrider@wintermute:~$ maas admin machines create \
> architecture=amd64 \
> max_addresses=52:54:00:6f:b4:af \
> power_type=virsh \
> power_parameters_power_id=50f6cca2-5d89-43b9-941c-90c9fcd7c156 \
> power_parameters_power_address=qemu+ssh://stormrider@192.168.123.1/system \
> power_parameters_power_pass=xxxxxxx
```

The variable fields in the machines create command (the $... items) are as follows, in this example:

```
> architecture=$ARCH \
> mac_addresses=$MAC_ADDRESS \
> power_type=$POWER_TYPE \
> power_parameters_power_id=$POWER_ID \
> power_parameters_power_address=$POWER_ADDRESS \
> power_parameters_power_pass=$POWER_PASSWORD
```

**$ARCH:** This field refers to the architecture of the machine being added, amd64 in the local laptop example.

**$MAC_ADDRESS:** This is the MAC address of the boot-enabled NIC for the machine being added. Note that the MAC address entered here must use a colon (":") separator, although some MAC addresses are written with dash ("-") separators.

**$POWER_TYPE:** You must select the power type supported by the machine you are adding, and fill in additional required fields that appear. See Power management for details on the available power types and the relevant parameters for each type. In this example, we’ve used a “virsh” power type (a libvirt KVM), but your choice will depend on your hardware.

**$POWER_ID:** This is generally the UUID of the machine being added.

**$POWER_ADDRESS/$POWER_PASSWORD:** In the case of a KVM, these are the only parameters that need to be entered. See Power types in the API reference for details on the available power types and the relevant parameters for each type.

You can commission, acquire, or deploy a machine these commands:

```
maas $PROFILE machine commission $SYSTEM_ID

maas $PROFILE machines allocate system_id=$SYSTEM_ID

maas $PROFILE machine deploy $SYSTEM_ID
```

The `$SYSTEM_ID` is the text in the "SYSID" field in the machine listing above.  These commands are described in more detail later on in this section of articles.
 snap-2-7-cli deb-2-7-cli snap-2-8-cli deb-2-8-cli snap-2-9-cli deb-2-9-cli  snap-3-0-cli deb-3-0-cli -->

<a href="#heading--node-details"><h2 id="heading--node-details">View machine details</h2></a>

<!-- snap-2-7-cli deb-2-7-cli snap-2-8-cli deb-2-8-cli snap-2-9-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 
Enter a command similar to the following to get a detailed view of a machine's status and configuration:

```
maas $PROFILE machine read $SYSTEM_ID | \
jq -r '([.hostname, .status_name, "Power", .power_state]),
[(120*"-")],
(["OVERVIEW", "|", "CPU", "", "", .architecture, "|", "MEMORY", "|", "STORAGE"]),
([.status_name, "|", "\(.cpu_count) core(s)", "", "", "", "|", "\(.memory) MB", "|",
"\(.blockdevice_set[].partitions[].size/(1024*1024*1024)) GiB"]),
(["", "", "|", .hardware_info.cpu_model, "|","","|"]), ([(120*"-")]),
(["Owner", "", "Domain", "", "Zone", "", "Resource pool", "", "Power type", "", "Tags"]),
([.owner // "-", "", .domain.name, "", .zone.name, "", .pool.name,
"", "", .power_type, "", "", .tag_names[0]]) | @tsv'
```

The above command produces output similar to this:

```
52-54-00-15-36-f2	Allocated	Power: off
---------------------------------------------------------------------------------------
OVERVIEW        | CPU                    amd64/generic  | MEMORY   | STORAGE
Allocated       | 1 core(s)                             | 1024 MB  | 4.9921875 GiB
                | Intel Core Processor (Skylake, IBRS)  |          |
---------------------------------------------------------------------------------------
Owner        Domain       Zone        Resource pool        Power type        Tags
admin        maas         default     default              virsh             virtual
```

You can customize this command at length by examining the entire JSON output stream, like this:

```
maas $PROFILE machine read $SYSTEM_ID | jq .
```

snap-2-7-cli deb-2-7-cli snap-2-8-cli deb-2-8-cli snap-2-9-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli  -->

<!-- snap-2-7-ui deb-2-7-ui snap-2-8-ui deb-2-8-ui snap-2-9-ui deb-2-9-ui 
Click a machine's FQDN or MAC address to open a detailed view of a machine's status and configuration.

<a href="https://discourse.maas.io/uploads/default/original/1X/c9684bf883d01d3fe610ec27e95618075c44b324.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/c9684bf883d01d3fe610ec27e95618075c44b324.jpeg"></a>

The default view is 'Machine summary', presented as a series of cards detailing the CPU, memory, storage and tag characteristics of the machine, as well as an overview of its current status. When relevant, 'Edit' links take you directly to the settings pane for the configuration referenced within the card.  The machine menu bar within the web UI also includes links to logs, events, and configuration options:

<a href="https://discourse.maas.io/uploads/default/original/1X/2efac92fca2c90f53ac86bd98485d8e98a1f91d4.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/2efac92fca2c90f53ac86bd98485d8e98a1f91d4.jpeg"></a> 

The menu includes links to a number of additional forms and controls, as described in the following sections.

<a href="#heading--machine-summary-h3"><h3 id="heading--machine-summary-h3">View a machine summary</h3></a>

As shown above, the Machine summary presents an overview of CPU, memory, storage, tags, and general settings:

<a href="https://discourse.maas.io/uploads/default/original/1X/c9684bf883d01d3fe610ec27e95618075c44b324.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/c9684bf883d01d3fe610ec27e95618075c44b324.jpeg"></a>

The first card presents some basics of the machine resources and configuration:

<a href="https://discourse.maas.io/uploads/default/original/1X/3e50fb21f4985db0a85519e2e933e24658770b9e.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/3e50fb21f4985db0a85519e2e933e24658770b9e.jpeg"></a> 

Here are some details on what this card presents, with details on in-card links described in following sections:

- **OVERVIEW** the machine status (in this case "Deployed"), and lists OS version information.  

- **CPU** shows the specifics of the CPU(s), including a link to test the processor(s).

- **MEMORY** gives the total available RAM for this machine, along with a test link.

- **STORAGE** presents the total amount of storage available and the number of disks that provide that storage.  There are two links here: one gives the storage layout (with the opportunity to change it for devices that are in 'Ready' or 'Allocated' states.

- **Owner** identifies the owner of the machine.

- **Domain** indicates the domain in which the machine exists.

- **Zone** shows the AZ in which this machine resides, along with a link to edit the machine configuration (to change the AZ, if desired).

- **Resource pool** shows the pool to which this machine has been assigned, and an edit link.

- **Power type** gives the current power type, which links to the relevant edit form.

- **Tags** presents the list of tags associated with this machine, editable via the link.

Note that clicking any of the links in this card will either present a pop-up form or take you to another item in the machine menu -- so using the browser "back" button will take you completely away from this machine's page.  For example, you can choose the "Test CPU" option, which brings up this overlay:

<a href="https://discourse.maas.io/uploads/default/original/1X/4fe98db93dd34f3b167b56286b06ec6d244d5848.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/4fe98db93dd34f3b167b56286b06ec6d244d5848.jpeg"></a> 

From this screen, you can choose test scripts and run the tests (in the background) as the interface returns to the Machine summary.  A linked note in the CPU block lets you know that the tests are in progress:

<a href="https://discourse.maas.io/uploads/default/original/1X/3d6996b32a5193dab76b112c864a216c845aa985.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/3d6996b32a5193dab76b112c864a216c845aa985.jpeg"></a> 

And you can watch the results under the "Tests" option in the Machine menu:

<a href="https://discourse.maas.io/uploads/default/original/1X/89d287347928d6adb039ca582d4a94c3b54588e1.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/89d287347928d6adb039ca582d4a94c3b54588e1.jpeg"></a> 
 snap-2-7-ui deb-2-7-ui snap-2-8-ui deb-2-8-ui snap-2-9-ui deb-2-9-ui -->

<!-- snap-3-0-ui deb-3-0-ui
Click a machine's FQDN or MAC address to open a detailed view of a machine's status and configuration.

<a href="https://discourse.maas.io/uploads/default/original/2X/a/a8ff4caf6362a3d695682499a74d64cb189dfc37.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/a/a8ff4caf6362a3d695682499a74d64cb189dfc37.png"></a>

The default view is 'Machine summary', presented as a series of cards detailing the CPU, memory, storage and tag characteristics of the machine, as well as an overview of its current status. When relevant, 'Edit' links take you directly to the settings pane for the configuration referenced within the card.  The machine menu bar within the web UI also includes links to logs, events, and configuration options:

<a href="https://discourse.maas.io/uploads/default/original/2X/2/21e9f4dca3a3e0a6657b5b2a570c9fc68a3e4961.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/2/21e9f4dca3a3e0a6657b5b2a570c9fc68a3e4961.png"></a> 

The menu includes links to a number of additional forms and controls, as described in the following sections.

<a href="#heading--machine-summary-h3"><h3 id="heading--machine-summary-h3">View a machine summary</h3></a>

As shown above, the Machine summary presents an overview of CPU, memory, storage, tags, and general settings:

<a href="https://discourse.maas.io/uploads/default/original/2X/a/a8ff4caf6362a3d695682499a74d64cb189dfc37.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/a/a8ff4caf6362a3d695682499a74d64cb189dfc37.png"></a>

The first card presents some basics of the machine resources and configuration:

<a href="https://discourse.maas.io/uploads/default/original/1X/3e50fb21f4985db0a85519e2e933e24658770b9e.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/3e50fb21f4985db0a85519e2e933e24658770b9e.jpeg"></a> 

Here are some details on what this card presents, with details on in-card links described in following sections:

- **OVERVIEW** the machine status (in this case "Deployed"), and lists OS version information.  

- **CPU** shows the specifics of the CPU(s), including a link to test the processor(s).

- **MEMORY** gives the total available RAM for this machine, along with a test link.

- **STORAGE** presents the total amount of storage available and the number of disks that provide that storage.  There are two links here: one gives the storage layout (with the opportunity to change it for devices that are in 'Ready' or 'Allocated' states.

- **Owner** identifies the owner of the machine.

- **Domain** indicates the domain in which the machine exists.

- **Zone** shows the AZ in which this machine resides, along with a link to edit the machine configuration (to change the AZ, if desired).

- **Resource pool** shows the pool to which this machine has been assigned, and an edit link.

- **Power type** gives the current power type, which links to the relevant edit form.

- **Tags** presents the list of tags associated with this machine, editable via the link.

Note that clicking any of the links in this card will either present a pop-up form or take you to another item in the machine menu -- so using the browser "back" button will take you completely away from this machine's page.  For example, you can choose the "Test CPU" option, which brings up this overlay:

<a href="https://discourse.maas.io/uploads/default/original/2X/6/6d7fe50e5b296a37a03269a1f5be3d25a2a2481a.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/6/6d7fe50e5b296a37a03269a1f5be3d25a2a2481a.png"></a> 

From this screen, you can choose test scripts and run the tests (in the background) as the interface returns to the Machine summary.  A linked note in the CPU block lets you know that the tests are in progress:

<a href="https://discourse.maas.io/uploads/default/original/2X/3/3e140872c407e5b9eb06960b5b42353765567192.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/3/3e140872c407e5b9eb06960b5b42353765567192.png"></a> 

And you can watch the results under the "Tests" option in the Machine menu:

<a href="https://discourse.maas.io/uploads/default/original/2X/f/f398c9ed670af8c0886ccc1ed8bf586e3faf1e53.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/f/f398c9ed670af8c0886ccc1ed8bf586e3faf1e53.png"></a> 
 snap-3-0-ui deb-3-0-ui -->
 
<!-- deb-2-7-ui
The rest of the cards on the Machine summary are either self-explanatory, or they're covered in the sections below.  The main point is this: You can see that nearly everything about machines takes place within the main menu's "Machines" option.  Incidentally, you can learn more about testing by visiting the [Hardware testing](/t/hardware-testing/2677) page.
 deb-2-7-ui -->

<!-- deb-2-8-ui
The rest of the cards on the Machine summary are either self-explanatory, or they're covered in the sections below.  The main point is this: You can see that nearly everything about machines takes place within the main menu's "Machines" option.  Incidentally, you can learn more about testing by visiting the [Hardware testing](/t/hardware-testing/2679) page.
 deb-2-8-ui -->

<!-- deb-2-9-ui
The rest of the cards on the Machine summary are either self-explanatory, or they're covered in the sections below.  The main point is this: You can see that nearly everything about machines takes place within the main menu's "Machines" option.  Incidentally, you can learn more about testing by visiting the [Hardware testing](/t/hardware-testing/2681) page.
 deb-2-9-ui -->

<!-- deb-3-0-ui
The rest of the cards on the Machine summary are either self-explanatory, or they're covered in the sections below.  The main point is this: You can see that nearly everything about machines takes place within the main menu's "Machines" option.  Incidentally, you can learn more about testing by visiting the [Hardware testing](/t/hardware-testing/3844) page.
 deb-3-0-ui -->

<!-- snap-2-7-ui
The rest of the cards on the Machine summary are either self-explanatory, or they're covered in the sections below.  The main point is this: You can see that nearly everything about machines takes place within the main menu's "Machines" option.  Incidentally, you can learn more about testing by visiting the [Hardware testing](/t/hardware-testing/2671) page.
 snap-2-7-ui -->

<!-- snap-2-8-ui
The rest of the cards on the Machine summary are either self-explanatory, or they're covered in the sections below.  The main point is this: You can see that nearly everything about machines takes place within the main menu's "Machines" option.  Incidentally, you can learn more about testing by visiting the [Hardware testing](/t/hardware-testing/2673) page.
 snap-2-8-ui -->

<!-- snap-2-9-ui
The rest of the cards on the Machine summary are either self-explanatory, or they're covered in the sections below.  The main point is this: You can see that nearly everything about machines takes place within the main menu's "Machines" option.  Incidentally, you can learn more about testing by visiting the [Hardware testing](/t/hardware-testing/2675) page.
 snap-2-9-ui -->

<!-- snap-3-0-ui
The rest of the cards on the Machine summary are either self-explanatory, or they're covered in the sections below.  The main point is this: You can see that nearly everything about machines takes place within the main menu's "Machines" option.  Incidentally, you can learn more about testing by visiting the [Hardware testing](/t/hardware-testing/3942) page.
 snap-3-0-ui -->

<!-- snap-3-0-ui deb-3-0-ui snap-3-0-cli deb-3-0-cli
<a href="#heading--usb-pci-devices"><h3 id="heading--usb-pci-devices">Handling attached USB and PCI devices</h3></a>

The machines in your MAAS may have devices attached to them via USB or PCI interface, such as keyboards, cameras, network cards, GPUs, etc.  MAAS will recognize these devices and make them visible to you when a machine is commissioned.

 snap-3-0-ui deb-3-0-ui snap-3-0-cli deb-3-0-cli-->

<!-- snap-3-0-ui deb-3-0-ui

For example, the machine details presents USB and PCI devices like this:

<a href="https://discourse.maas.io/uploads/default/original/2X/8/87f42bafe321d45af94d73216f933a9067f01df2.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/8/87f42bafe321d45af94d73216f933a9067f01df2.png"></a>

Note that this page now includes two new tabs: "PCI devices" and "USB."  For each USB/PCI device attached to your machine, these tabs will list:

* device type
* vendor ID
* a product description
* a product ID
* the driver name
* the containing NUMA node (if any)
* the device address

A typical PCI device tab would look something like this:

<a href="https://discourse.maas.io/uploads/default/original/2X/8/82e1e6f8bc511047ac5f773430f7e5812c7a24d4.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/8/82e1e6f8bc511047ac5f773430f7e5812c7a24d4.png"></a>

The USB tab presents similar information in the same format.

[note]
If you are upgrading from a previous version of MAAS, PCI and USB devices aren't modeled, so you will have to recommission the machine to capture these devices.
[/note]

 snap-3-0-ui deb-3-0-ui -->

<!-- snap-3-0-cli deb-3-0-cli
Using the MAAS CLI, you can obtain a list of the USB/PCI devices available in a commissioned machine with the following command:

```
maas $PROFILE node-devices read $SYSTEM_ID
```

where:

* $PROFILE   = your user profile (e.g., "admin")
* $SYSTEM_ID = the ID of the machine in question (e.g., "ngx7ry")

Note that USB/PCI devices are referred to as "node-devices" in the MAAS CLI.

The JSON output that is returned from this command will contain the following information about each USB/PCI device on the machine in question:

* the node-device ID
* the bus to which the device is attached (PCIE/USB)
* the hardware_type, which can be "node," "cpu,"" "memory," "storage," or "gpu."
* the vendor_id
* the product_id
* vendor_name
* the product_name
* the commissioning_driver (i.e., the driver)
 
These parameters may vary greatly between device types.

 snap-3-0-cli deb-3-0-cli -->

<!-- snap-3-0-ui deb-3-0-ui snap-3-0-cli deb-3-0-cli
Once you've commissioned the machine, you have the option of deleting PCI/USB devices from the machine in any machine state, via the CLI only, using the following command:

```
maas $PROFILE node-device delete $SYSTEM_ID $DEVICE_ID
```

where:

* $PROFILE   = your user profile (e.g., "admin")
* $SYSTEM_ID = the ID of the machine in question (e.g., "ngx7ry")
* $DEVICE_ID = the ID of the device you want to delete 

If the device is still present in the system, it will be recogized again (and thus "recreated")
when the machine is commissioned again.
 snap-3-0-ui deb-3-0-ui snap-3-0-cli deb-3-0-cli -->


<!-- snap-2-8-ui deb-2-8-ui snap-2-7-ui deb-2-7-ui snap-2-9-ui deb-2-9-ui 
<a href="#heading--machine-interfaces-h3"><h3 id="heading--machine-interfaces-h3">Find network info for a machine</h3></a>

The Network "tab" provides you with a way to view/edit the network and interface configuration for a machine: 

<a href="https://discourse.maas.io/uploads/default/original/1X/7a7b22ee7202b50df09c7bef598250db0eb1cc15.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/7a7b22ee7202b50df09c7bef598250db0eb1cc15.jpeg"></a> 

In the case of this deployed machine, there are not many editing options.  If the machine is in a 'Ready' state, though, altering the network configuration is possible:

<a href="https://discourse.maas.io/uploads/default/original/1X/01d53759105647d71786154e99ff210f8c71d2e7.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/01d53759105647d71786154e99ff210f8c71d2e7.jpeg"></a> 
 snap-2-8-ui deb-2-8-ui snap-2-7-ui deb-2-7-ui snap-2-9-ui deb-2-9-ui -->

<!-- snap-3-0-ui deb-3-0-ui
<a href="#heading--machine-interfaces-h3"><h3 id="heading--machine-interfaces-h3">Find network info for a machine</h3></a>

The Network "tab" provides you with a way to view/edit the network and interface configuration for a machine: 

<a href="https://discourse.maas.io/uploads/default/original/2X/c/c5316db130ae05a9cdabcd49ffaa69f0bb405d1d.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/c/c5316db130ae05a9cdabcd49ffaa69f0bb405d1d.png"></a> 

In the case of this deployed machine, there are not many editing options.  If the machine is in a 'Ready' state, though, altering the network configuration is possible, as shown in the screenshot above.

 snap-3-0-ui deb-3-0-ui -->

<!-- deb-2-7-ui
Options on this tab are described in the introduction to [Networking](/t/networking/2953) article in this documentation set.
 deb-2-7-ui -->

<!-- deb-2-8-ui
Options on this tab are described in the introduction to [Networking](/t/networking/2955) article in this documentation set.
 deb-2-8-ui -->

<!-- deb-2-9-ui
Options on this tab are described in the introduction to [Networking](/t/networking/2957) article in this documentation set.
 deb-2-9-ui -->

<!-- deb-3-0-ui
Options on this tab are described in the introduction to [Networking](/t/networking/4048) article in this documentation set.
 deb-3-0-ui -->

<!-- snap-2-7-ui
Options on this tab are described in the introduction to [Networking](/t/networking/2947) article in this documentation set.
 snap-2-7-ui -->

<!-- snap-2-8-ui
Options on this tab are described in the introduction to [Networking](/t/networking/2949) article in this documentation set.
 snap-2-8-ui -->

<!-- snap-2-9-ui
Options on this tab are described in the introduction to [Networking](/t/networking/2951) article in this documentation set.
 snap-2-9-ui -->

<!-- snap-3-0-ui
Options on this tab are described in the introduction to [Networking](/t/networking/4046) article in this documentation set.
 snap-3-0-ui -->

<!-- deb-2-7-ui
<a href="#heading--machine-storage-h3"><h3 id="heading--machine-storage-h3">Find storage info for a machine</h3></a>

The Storage tab on the machine list brings up a form that allows you to view/edit the file system, partitioning and storage parameters for the selected machine:

<a href="https://discourse.maas.io/uploads/default/original/1X/9dc30aedf5ed173bb7b474910fa9939f7f066c95.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/9dc30aedf5ed173bb7b474910fa9939f7f066c95.jpeg"></a> 

This tab describes the filesystem(s) in use, as well as the available and used partitions for this machine.  See the article [Storage](/t/storage/3109) for a detailed discussion on how to use this screen, as well as many other considerations for machine storage configurations.
 deb-2-7-ui -->

<!-- deb-2-8-ui
<a href="#heading--machine-storage-h3"><h3 id="heading--machine-storage-h3">Find storage info for a machine</h3></a>

The Storage tab on the machine list brings up a form that allows you to view/edit the file system, partitioning and storage parameters for the selected machine:

<a href="https://discourse.maas.io/uploads/default/original/1X/9dc30aedf5ed173bb7b474910fa9939f7f066c95.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/9dc30aedf5ed173bb7b474910fa9939f7f066c95.jpeg"></a> 

This tab describes the filesystem(s) in use, as well as the available and used partitions for this machine.  See the article [Storage](/t/storage/3111) for a detailed discussion on how to use this screen, as well as many other considerations for machine storage configurations.
 deb-2-8-ui -->

<!-- deb-2-9-ui
<a href="#heading--machine-storage-h3"><h3 id="heading--machine-storage-h3">Find storage info for a machine</h3></a>

The Storage tab on the machine list brings up a form that allows you to view/edit the file system, partitioning and storage parameters for the selected machine:

<a href="https://discourse.maas.io/uploads/default/original/1X/9dc30aedf5ed173bb7b474910fa9939f7f066c95.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/9dc30aedf5ed173bb7b474910fa9939f7f066c95.jpeg"></a> 

This tab describes the filesystem(s) in use, as well as the available and used partitions for this machine.  See the article [Storage](/t/storage/3113) for a detailed discussion on how to use this screen, as well as many other considerations for machine storage configurations.
 deb-2-9-ui -->

<!-- deb-3-0-ui
<a href="#heading--machine-storage-h3"><h3 id="heading--machine-storage-h3">Find storage info for a machine</h3></a>

The Storage tab on the machine list brings up a form that allows you to view/edit the file system, partitioning and storage parameters for the selected machine:

<a href="https://discourse.maas.io/uploads/default/original/2X/6/658f4814716a1347fda62ab799ba0d72506c128e.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/6/658f4814716a1347fda62ab799ba0d72506c128e.png"></a> 

This tab describes the filesystem(s) in use, as well as the available and used partitions for this machine.  See the article [Storage](/t/storage/4108) for a detailed discussion on how to use this screen, as well as many other considerations for machine storage configurations.
 deb-3-0-ui -->

<!-- snap-2-7-ui
<a href="#heading--machine-storage-h3"><h3 id="heading--machine-storage-h3">Find storage info for a machine</h3></a>

The Storage tab on the machine list brings up a form that allows you to view/edit the file system, partitioning and storage parameters for the selected machine:

<a href="https://discourse.maas.io/uploads/default/original/1X/9dc30aedf5ed173bb7b474910fa9939f7f066c95.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/9dc30aedf5ed173bb7b474910fa9939f7f066c95.jpeg"></a> 

This tab describes the filesystem(s) in use, as well as the available and used partitions for this machine.  See the article [Storage](/t/storage/3103) for a detailed discussion on how to use this screen, as well as many other considerations for machine storage configurations.
 snap-2-7-ui -->

<!-- snap-2-8-ui
<a href="#heading--machine-storage-h3"><h3 id="heading--machine-storage-h3">Find storage info for a machine</h3></a>

The Storage tab on the machine list brings up a form that allows you to view/edit the file system, partitioning and storage parameters for the selected machine:

<a href="https://discourse.maas.io/uploads/default/original/1X/9dc30aedf5ed173bb7b474910fa9939f7f066c95.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/9dc30aedf5ed173bb7b474910fa9939f7f066c95.jpeg"></a> 

This tab describes the filesystem(s) in use, as well as the available and used partitions for this machine.  See the article [Storage](/t/storage/3105) for a detailed discussion on how to use this screen, as well as many other considerations for machine storage configurations.
 snap-2-8-ui -->

<!-- snap-2-9-ui
<a href="#heading--machine-storage-h3"><h3 id="heading--machine-storage-h3">Find storage info for a machine</h3></a>

The Storage tab on the machine list brings up a form that allows you to view/edit the file system, partitioning and storage parameters for the selected machine:

<a href="https://discourse.maas.io/uploads/default/original/1X/9dc30aedf5ed173bb7b474910fa9939f7f066c95.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/9dc30aedf5ed173bb7b474910fa9939f7f066c95.jpeg"></a> 

This tab describes the filesystem(s) in use, as well as the available and used partitions for this machine.  See the article [Storage](/t/storage/3107) for a detailed discussion on how to use this screen, as well as many other considerations for machine storage configurations.
 snap-2-9-ui -->

<!-- snap-3-0-ui
<a href="#heading--machine-storage-h3"><h3 id="heading--machine-storage-h3">Find storage info for a machine</h3></a>

The Storage tab on the machine list brings up a form that allows you to view/edit the file system, partitioning and storage parameters for the selected machine:

<a href="https://discourse.maas.io/uploads/default/original/2X/6/658f4814716a1347fda62ab799ba0d72506c128e.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/6/658f4814716a1347fda62ab799ba0d72506c128e.png"></a> 

This tab describes the filesystem(s) in use, as well as the available and used partitions for this machine.  See the article [Storage](/t/storage/4106) for a detailed discussion on how to use this screen, as well as many other considerations for machine storage configurations.
 snap-3-0-ui -->

<!-- deb-2-7-ui
<a href="#heading--commissioning-log-h3"><h3 id="heading--commissioning-log-h3">Find the commissioning log for you</h3></a>

The "Commissioning" tab brings up a summary log of commissioning events:

<a href="https://discourse.maas.io/uploads/default/original/1X/b3d6248013fb5186d3ea61931816fe688b94a6a2.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/b3d6248013fb5186d3ea61931816fe688b94a6a2.jpeg"></a> 

Clicking on any of the "View log" links will take you to specific, detailed logs for that particular event or milestone:

<a href="https://discourse.maas.io/uploads/default/original/1X/13fce404b9bb304e08a7c5de5a395c514e98b9b0.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/13fce404b9bb304e08a7c5de5a395c514e98b9b0.jpeg"></a> 

These logs present an extremely detailed, timestamped record of completion and status items from the commissioning process.  See the article on [Logging](/t/maas-logging/2869) for more details on how to read and interpret these logs.
 deb-2-7-ui -->

<!-- deb-2-8-ui
<a href="#heading--commissioning-log-h3"><h3 id="heading--commissioning-log-h3">Find the commissioning log for you</h3></a>

The "Commissioning" tab brings up a summary log of commissioning events:

<a href="https://discourse.maas.io/uploads/default/original/1X/b3d6248013fb5186d3ea61931816fe688b94a6a2.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/b3d6248013fb5186d3ea61931816fe688b94a6a2.jpeg"></a> 

Clicking on any of the "View log" links will take you to specific, detailed logs for that particular event or milestone:

<a href="https://discourse.maas.io/uploads/default/original/1X/13fce404b9bb304e08a7c5de5a395c514e98b9b0.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/13fce404b9bb304e08a7c5de5a395c514e98b9b0.jpeg"></a> 

These logs present an extremely detailed, timestamped record of completion and status items from the commissioning process.  See the article on [Logging](/t/maas-logging/2871) for more details on how to read and interpret these logs.
 deb-2-8-ui -->

<!-- deb-2-9-ui
<a href="#heading--commissioning-log-h3"><h3 id="heading--commissioning-log-h3">Find the commissioning log for you</h3></a>

The "Commissioning" tab brings up a summary log of commissioning events:

<a href="https://discourse.maas.io/uploads/default/original/1X/b3d6248013fb5186d3ea61931816fe688b94a6a2.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/b3d6248013fb5186d3ea61931816fe688b94a6a2.jpeg"></a> 

Clicking on any of the "View log" links will take you to specific, detailed logs for that particular event or milestone:

<a href="https://discourse.maas.io/uploads/default/original/1X/13fce404b9bb304e08a7c5de5a395c514e98b9b0.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/13fce404b9bb304e08a7c5de5a395c514e98b9b0.jpeg"></a> 

These logs present an extremely detailed, timestamped record of completion and status items from the commissioning process.  See the article on [Logging](/t/maas-logging/2873) for more details on how to read and interpret these logs.
 deb-2-9-ui -->

<!-- deb-3-0-ui snap-3-0-ui
<a href="#heading--commissioning-log-h3"><h3 id="heading--commissioning-log-h3">Find the commissioning log for you</h3></a>

The "Commissioning" tab brings up a summary log of commissioning events:

<a href="https://discourse.maas.io/uploads/default/original/2X/e/e98766009f32972dfe29293f9bc850b99a9a941f.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/e/e98766009f32972dfe29293f9bc850b99a9a941f.png"></a> 

Click on the dropdown at the end of the row you're interested in, and click on "View details":

<a href="https://discourse.maas.io/uploads/default/original/2X/8/8f7b4c02ce301fb867e7af33267be62498095bb5.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/8/8f7b4c02ce301fb867e7af33267be62498095bb5.png"></a>

This will bring up a detailed log view for that row:

<a href="https://discourse.maas.io/uploads/default/original/2X/4/41a385cdf948dada8bb8d8f94a3137a2b64d46e0.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/4/41a385cdf948dada8bb8d8f94a3137a2b64d46e0.png"></a>

These logs present an extremely detailed, timestamped record of completion and status items from the commissioning process.  
 deb-3-0-ui snap-3-0-ui -->

<!-- snap-2-7-ui
<a href="#heading--commissioning-log-h3"><h3 id="heading--commissioning-log-h3">Find the commissioning log for you</h3></a>

The "Commissioning" tab brings up a summary log of commissioning events:

<a href="https://discourse.maas.io/uploads/default/original/1X/b3d6248013fb5186d3ea61931816fe688b94a6a2.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/b3d6248013fb5186d3ea61931816fe688b94a6a2.jpeg"></a> 

Clicking on any of the "View log" links will take you to specific, detailed logs for that particular event or milestone:

<a href="https://discourse.maas.io/uploads/default/original/1X/13fce404b9bb304e08a7c5de5a395c514e98b9b0.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/13fce404b9bb304e08a7c5de5a395c514e98b9b0.jpeg"></a> 

These logs present an extremely detailed, timestamped record of completion and status items from the commissioning process.  See the article on [Logging](/t/maas-logging/2863) for more details on how to read and interpret these logs.
 snap-2-7-ui -->

<!-- snap-2-8-ui
<a href="#heading--commissioning-log-h3"><h3 id="heading--commissioning-log-h3">Find the commissioning log for you</h3></a>

The "Commissioning" tab brings up a summary log of commissioning events:

<a href="https://discourse.maas.io/uploads/default/original/1X/b3d6248013fb5186d3ea61931816fe688b94a6a2.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/b3d6248013fb5186d3ea61931816fe688b94a6a2.jpeg"></a> 

Clicking on any of the "View log" links will take you to specific, detailed logs for that particular event or milestone:

<a href="https://discourse.maas.io/uploads/default/original/1X/13fce404b9bb304e08a7c5de5a395c514e98b9b0.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/13fce404b9bb304e08a7c5de5a395c514e98b9b0.jpeg"></a> 

These logs present an extremely detailed, timestamped record of completion and status items from the commissioning process.  See the article on [Logging](/t/maas-logging/2865) for more details on how to read and interpret these logs.
 snap-2-8-ui -->

<!-- snap-2-9-ui
<a href="#heading--commissioning-log-h3"><h3 id="heading--commissioning-log-h3">Find the commissioning log for you</h3></a>

The "Commissioning" tab brings up a summary log of commissioning events:

<a href="https://discourse.maas.io/uploads/default/original/1X/b3d6248013fb5186d3ea61931816fe688b94a6a2.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/b3d6248013fb5186d3ea61931816fe688b94a6a2.jpeg"></a> 

Clicking on any of the "View log" links will take you to specific, detailed logs for that particular event or milestone:

<a href="https://discourse.maas.io/uploads/default/original/1X/13fce404b9bb304e08a7c5de5a395c514e98b9b0.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/13fce404b9bb304e08a7c5de5a395c514e98b9b0.jpeg"></a> 

These logs present an extremely detailed, timestamped record of completion and status items from the commissioning process.  See the article on [Logging](/t/maas-logging/2867) for more details on how to read and interpret these logs.
 snap-2-9-ui -->

<!-- deb-2-7-ui
<a href="#heading--hardware-tests-h3"><h3 id="heading--hardware-tests-h3">Find machine hardware & test logs</h3></a>

This tab presents a summary of tests run against this particular machine:  

<a href="https://discourse.maas.io/uploads/default/original/1X/b6a6ff3c8fae4a638c18a18bf65c4aa51f29e984.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/b6a6ff3c8fae4a638c18a18bf65c4aa51f29e984.jpeg"></a> 

You can view the summary report, or click on a "View log" link to get details on any particular tests:

<a href="https://discourse.maas.io/uploads/default/original/1X/8113eba28a3f08279ff2b5f7593e30db05d00824.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/8113eba28a3f08279ff2b5f7593e30db05d00824.jpeg"></a> 

The format of these screens is very similar to the Configuration logs shown above.  For more information, please see the article on [Hardware testing](/t/hardware-testing/2677).
 deb-2-7-ui -->

<!-- deb-2-8-ui
<a href="#heading--hardware-tests-h3"><h3 id="heading--hardware-tests-h3">Find machine hardware & test logs</h3></a>

This tab presents a summary of tests run against this particular machine:  

<a href="https://discourse.maas.io/uploads/default/original/1X/b6a6ff3c8fae4a638c18a18bf65c4aa51f29e984.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/b6a6ff3c8fae4a638c18a18bf65c4aa51f29e984.jpeg"></a> 

You can view the summary report, or click on a "View log" link to get details on any particular tests:

<a href="https://discourse.maas.io/uploads/default/original/1X/8113eba28a3f08279ff2b5f7593e30db05d00824.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/8113eba28a3f08279ff2b5f7593e30db05d00824.jpeg"></a> 

The format of these screens is very similar to the Configuration logs shown above.  For more information, please see the article on [Hardware testing](/t/hardware-testing/2679).
 deb-2-8-ui -->

<!-- deb-2-9-ui
<a href="#heading--hardware-tests-h3"><h3 id="heading--hardware-tests-h3">Find machine hardware & test logs</h3></a>

This tab presents a summary of tests run against this particular machine:  

<a href="https://discourse.maas.io/uploads/default/original/1X/b6a6ff3c8fae4a638c18a18bf65c4aa51f29e984.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/b6a6ff3c8fae4a638c18a18bf65c4aa51f29e984.jpeg"></a> 

You can view the summary report, or click on a "View log" link to get details on any particular tests:

<a href="https://discourse.maas.io/uploads/default/original/1X/8113eba28a3f08279ff2b5f7593e30db05d00824.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/8113eba28a3f08279ff2b5f7593e30db05d00824.jpeg"></a> 

The format of these screens is very similar to the Configuration logs shown above.  For more information, please see the article on [Hardware testing](/t/hardware-testing/2681).
 deb-2-9-ui -->

<!-- deb-3-0-ui
<a href="#heading--hardware-tests-h3"><h3 id="heading--hardware-tests-h3">Find machine hardware & test logs</h3></a>

This tab presents a summary of tests run against this particular machine:  

<a href="See the article on [Logging](/t/maas-logging/4012) for more details on how to read and interpret these logs." target = "_blank"><img src="See the article on [Logging](/t/maas-logging/4012) for more details on how to read and interpret these logs."></a> 

You can view the summary report, or choose the "View details" dropdown to get details on any particular tests:

<a href="https://discourse.maas.io/uploads/default/original/2X/e/e53a2c01b57df49e56bb4d95552b6a038249aa97.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/e/e53a2c01b57df49e56bb4d95552b6a038249aa97.png"></a> 

The format of these screens is very similar to the Configuration logs shown above.  For more information, please see the article on [Hardware testing](/t/hardware-testing/3944).
 deb-3-0-ui -->

<!-- snap-2-7-ui
<a href="#heading--hardware-tests-h3"><h3 id="heading--hardware-tests-h3">Find machine hardware & test logs</h3></a>

This tab presents a summary of tests run against this particular machine:  

<a href="https://discourse.maas.io/uploads/default/original/1X/b6a6ff3c8fae4a638c18a18bf65c4aa51f29e984.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/b6a6ff3c8fae4a638c18a18bf65c4aa51f29e984.jpeg"></a> 

You can view the summary report, or click on a "View log" link to get details on any particular tests:

<a href="https://discourse.maas.io/uploads/default/original/1X/8113eba28a3f08279ff2b5f7593e30db05d00824.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/8113eba28a3f08279ff2b5f7593e30db05d00824.jpeg"></a> 

The format of these screens is very similar to the Configuration logs shown above.  For more information, please see the article on [Hardware testing](/t/hardware-testing/2671).
 snap-2-7-ui -->

<!-- snap-2-8-ui
<a href="#heading--hardware-tests-h3"><h3 id="heading--hardware-tests-h3">Find machine hardware & test logs</h3></a>

This tab presents a summary of tests run against this particular machine:  

<a href="https://discourse.maas.io/uploads/default/original/1X/b6a6ff3c8fae4a638c18a18bf65c4aa51f29e984.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/b6a6ff3c8fae4a638c18a18bf65c4aa51f29e984.jpeg"></a> 

You can view the summary report, or click on a "View log" link to get details on any particular tests:

<a href="https://discourse.maas.io/uploads/default/original/1X/8113eba28a3f08279ff2b5f7593e30db05d00824.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/8113eba28a3f08279ff2b5f7593e30db05d00824.jpeg"></a> 

The format of these screens is very similar to the Configuration logs shown above.  For more information, please see the article on [Hardware testing](/t/hardware-testing/2673).
 snap-2-8-ui -->

<!-- snap-2-9-ui
<a href="#heading--hardware-tests-h3"><h3 id="heading--hardware-tests-h3">Find machine hardware & test logs</h3></a>

This tab presents a summary of tests run against this particular machine:  

<a href="https://discourse.maas.io/uploads/default/original/1X/b6a6ff3c8fae4a638c18a18bf65c4aa51f29e984.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/b6a6ff3c8fae4a638c18a18bf65c4aa51f29e984.jpeg"></a> 

You can view the summary report, or click on a "View log" link to get details on any particular tests:

<a href="https://discourse.maas.io/uploads/default/original/1X/8113eba28a3f08279ff2b5f7593e30db05d00824.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/8113eba28a3f08279ff2b5f7593e30db05d00824.jpeg"></a> 

The format of these screens is very similar to the Configuration logs shown above.  For more information, please see the article on [Hardware testing](/t/hardware-testing/2675).
 snap-2-9-ui -->

<!-- snap-3-0-ui
<a href="#heading--hardware-tests-h3"><h3 id="heading--hardware-tests-h3">Find machine hardware & test logs</h3></a>

This tab presents a summary of tests run against this particular machine:  

<a href="See the article on [Logging](/t/maas-logging/4012) for more details on how to read and interpret these logs." target = "_blank"><img src="See the article on [Logging](/t/maas-logging/4012) for more details on how to read and interpret these logs."></a> 

You can view the summary report, or choose the "View details" dropdown to get details on any particular tests:

<a href="https://discourse.maas.io/uploads/default/original/2X/e/e53a2c01b57df49e56bb4d95552b6a038249aa97.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/e/e53a2c01b57df49e56bb4d95552b6a038249aa97.png"></a> 

The format of these screens is very similar to the Configuration logs shown above.  For more information, please see the article on [Hardware testing](/t/hardware-testing/3841).
 snap-3-0-ui -->

<!-- deb-2-7-ui
<a href="#heading--raw-log-output-h3"><h3 id="heading--raw-log-output-h3">Find raw log output for a machine</h3></a>

The "Logs" tab shows raw log output, switchable between YAML and XML formats:

<a href="https://discourse.maas.io/uploads/default/original/1X/02b4bc35c8985fe0b954d8deb0afba18866cfe66.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/02b4bc35c8985fe0b954d8deb0afba18866cfe66.jpeg"></a> 

Help interpreting these logs can be found under the [Logging](/t/maas-logging/2869) section of this documentation.
 deb-2-7-ui -->

<!-- deb-2-8-ui
<a href="#heading--raw-log-output-h3"><h3 id="heading--raw-log-output-h3">Find raw log output for a machine</h3></a>

The "Logs" tab shows raw log output, switchable between YAML and XML formats:

<a href="https://discourse.maas.io/uploads/default/original/1X/02b4bc35c8985fe0b954d8deb0afba18866cfe66.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/02b4bc35c8985fe0b954d8deb0afba18866cfe66.jpeg"></a> 

Help interpreting these logs can be found under the [Logging](/t/maas-logging/2871) section of this documentation.
 deb-2-8-ui -->

<!-- deb-2-9-ui
<a href="#heading--raw-log-output-h3"><h3 id="heading--raw-log-output-h3">Find raw log output for a machine</h3></a>

The "Logs" tab shows raw log output, switchable between YAML and XML formats:

<a href="https://discourse.maas.io/uploads/default/original/1X/02b4bc35c8985fe0b954d8deb0afba18866cfe66.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/02b4bc35c8985fe0b954d8deb0afba18866cfe66.jpeg"></a> 

Help interpreting these logs can be found under the [Logging](/t/maas-logging/2873) section of this documentation.
 deb-2-9-ui -->

<!-- deb-3-0-ui
<a href="#heading--raw-log-output-h3"><h3 id="heading--raw-log-output-h3">Find raw log output for a machine</h3></a>

By choosing "Installation output" on the "Logs" tab, you can see the "raw" log output:

<a href="https://discourse.maas.io/uploads/default/original/2X/d/dc5bb5e6489a382e257dac605f2dbdc6fa1ca630.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/d/dc5bb5e6489a382e257dac605f2dbdc6fa1ca630.png"></a> 

Help interpreting these logs can be found under the [Logging](/t/maas-logging/4012) section of this documentation.
 deb-3-0-ui -->

<!-- snap-2-7-ui
<a href="#heading--raw-log-output-h3"><h3 id="heading--raw-log-output-h3">Find raw log output for a machine</h3></a>

The "Logs" tab shows raw log output, switchable between YAML and XML formats:

<a href="https://discourse.maas.io/uploads/default/original/1X/02b4bc35c8985fe0b954d8deb0afba18866cfe66.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/02b4bc35c8985fe0b954d8deb0afba18866cfe66.jpeg"></a> 

Help interpreting these logs can be found under the [Logging](/t/maas-logging/2863) section of this documentation.
 snap-2-7-ui -->

<!-- snap-2-8-ui
<a href="#heading--raw-log-output-h3"><h3 id="heading--raw-log-output-h3">Find raw log output for a machine</h3></a>

The "Logs" tab shows raw log output, switchable between YAML and XML formats:

<a href="https://discourse.maas.io/uploads/default/original/1X/02b4bc35c8985fe0b954d8deb0afba18866cfe66.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/02b4bc35c8985fe0b954d8deb0afba18866cfe66.jpeg"></a> 

Help interpreting these logs can be found under the [Logging](/t/maas-logging/2865) section of this documentation.
 snap-2-8-ui -->

<!-- snap-2-9-ui
<a href="#heading--raw-log-output-h3"><h3 id="heading--raw-log-output-h3">Find raw log output for a machine</h3></a>

The "Logs" tab shows raw log output, switchable between YAML and XML formats:

<a href="https://discourse.maas.io/uploads/default/original/1X/02b4bc35c8985fe0b954d8deb0afba18866cfe66.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/02b4bc35c8985fe0b954d8deb0afba18866cfe66.jpeg"></a> 

Help interpreting these logs can be found under the [Logging](/t/maas-logging/2867) section of this documentation.
 snap-2-9-ui -->

<!-- snap-3-0-ui
By choosing "Installation output" on the "Logs" tab, you can see the "raw" log output:

<a href="https://discourse.maas.io/uploads/default/original/2X/d/dc5bb5e6489a382e257dac605f2dbdc6fa1ca630.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/d/dc5bb5e6489a382e257dac605f2dbdc6fa1ca630.png"></a> 

Help interpreting these logs can be found under the [Logging](/t/maas-logging/4010) section of this documentation.
 snap-3-0-ui -->

<!-- deb-2-7-ui snap-2-7-ui deb-2-8-ui snap-2-8-ui deb-2-9-ui snap-2-9-ui 
<a href="#heading--event-logs-h3"><h3 id="heading--event-logs-h3">Find a machine's event logs</h3></a>

The "Event" tab displays a list of timestamped status updates for events and actions performed on the machine:

<a href="https://discourse.maas.io/uploads/default/original/1X/114ada7188f8ebf12883a54c0976ad8abda1d211.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/114ada7188f8ebf12883a54c0976ad8abda1d211.jpeg"></a> 
 deb-2-7-ui snap-2-7-ui deb-2-8-ui snap-2-8-ui deb-2-9-ui snap-2-9-ui -->

<!-- snap-3-0-ui deb-3-0-ui
<a href="#heading--event-logs-h3"><h3 id="heading--event-logs-h3">Find a machine's event logs</h3></a>

To view the Event log for a machine, choose the "Event" tab under "Logs."  This displays a list of timestamped status updates for events and actions performed on the machine:

<a href="https://discourse.maas.io/uploads/default/original/2X/9/981a1aced2a4c231fa9e4fe1b70e77aeb816f133.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/9/981a1aced2a4c231fa9e4fe1b70e77aeb816f133.png"></a> 
 snap-3-0-ui deb-3-0-ui -->

<!-- deb-2-7-ui
There is a button that allows you to see the next 10 events, and a link to show the entire history.  Detailed discussion of this event log can be found under the [Logging](/t/maas-logging/2869) section of this documentation.
 deb-2-7-ui -->

<!-- deb-2-8-ui
There is a button that allows you to see the next 10 events, and a link to show the entire history.  Detailed discussion of this event log can be found under the [Logging](/t/maas-logging/2871) section of this documentation.
 deb-2-8-ui -->

<!-- deb-2-9-ui
There is a button that allows you to see the next 10 events, and a link to show the entire history.  Detailed discussion of this event log can be found under the [Logging](/t/maas-logging/2873) section of this documentation.
 deb-2-9-ui -->

<!-- deb-3-0-ui
There is a dropdown on the upper right which allows you to choose how many events per page you wish to view.  Detailed discussion of this event log can be found under the [Logging](/t/maas-logging/4012) section of this documentation.
 deb-3-0-ui -->

<!-- snap-2-7-ui
There is a button that allows you to see the next 10 events, and a link to show the entire history.  Detailed discussion of this event log can be found under the [Logging](/t/maas-logging/2863) section of this documentation.
 snap-2-7-ui -->

<!-- snap-2-8-ui
There is a button that allows you to see the next 10 events, and a link to show the entire history.  Detailed discussion of this event log can be found under the [Logging](/t/maas-logging/2865) section of this documentation.
 snap-2-8-ui -->

<!-- snap-2-9-ui
There is a button that allows you to see the next 10 events, and a link to show the entire history.  Detailed discussion of this event log can be found under the [Logging](/t/maas-logging/2867) section of this documentation.
 snap-2-9-ui -->

<!-- snap-3-0-ui
There is a dropdown on the upper right which allows you to choose how many events per page you wish to view. Detailed discussion of this event log can be found under the [Logging](/t/maas-logging/4010) section of this documentation.
 snap-3-0-ui -->

<!-- deb-2-7-ui snap-2-7-ui deb-2-8-ui snap-2-8-ui deb-2-9-ui snap-2-9-ui 
<a href="#heading--machine-config-h3"><h3 id="heading--machine-config-h3">Find machine configuration info</h3></a>

The final tab from the Machine menu allows you to update machine and power configuration options: 

<a href="https://discourse.maas.io/uploads/default/original/1X/13bb1352103c759365fc6b923672f021982a10c3.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/13bb1352103c759365fc6b923672f021982a10c3.jpeg"></a> 

There are two sections to this tab.  The "Machine configuration" section offers some general parameters, mostly related to how this machine is grouped and categorised.  More information on these options are found in the relevant sections of the documentation (e.g., tags, resource pools, and so forth). 

The "Power configuration" supplies the parameters necessary for MAAS to access the machine to PXE-boot it. Note that this machine failed testing.  Editing the "Power configuration" section gives us a clue as to what might be wrong:
<a href="https://discourse.maas.io/uploads/default/original/1X/8f4c4ae8ec07f42551bad654375f513debc53ef1.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/8f4c4ae8ec07f42551bad654375f513debc53ef1.jpeg"></a> 

After entering the correct password and recycling things, the problem goes away:

<a href="https://discourse.maas.io/uploads/default/original/1X/635e27e87bcac0c3cb3ce3085bd2fa55f60ff137.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/635e27e87bcac0c3cb3ce3085bd2fa55f60ff137.jpeg"></a> 
 deb-2-7-ui snap-2-7-ui deb-2-8-ui snap-2-8-ui deb-2-9-ui snap-2-9-ui -->

<!-- snap-3-0-ui deb-3-0-ui
<a href="#heading--machine-config-h3"><h3 id="heading--machine-config-h3">Find machine configuration info</h3></a>

The final tab from the Machine menu allows you to update machine and power configuration options: 

<a href="https://discourse.maas.io/uploads/default/original/2X/7/7cfd77228a5cf1a6f779897d501f14fbf78fd4b4.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/7/7cfd77228a5cf1a6f779897d501f14fbf78fd4b4.png"></a> 

There are two sections to this tab.  The "Machine configuration" section, shown above, offers some general parameters, mostly related to how this machine is grouped and categorised.  More information on these options are found in the relevant sections of the documentation (e.g., tags, resource pools, and so forth). 

The "Power configuration" supplies the parameters necessary for MAAS to access the machine to PXE-boot it: 

<a href="https://discourse.maas.io/uploads/default/original/2X/1/198898362285e4a1308535a4aa701156a67c9616.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/1/198898362285e4a1308535a4aa701156a67c9616.png"></a> 
 snap-3-0-ui deb-3-0-ui -->

<!-- deb-2-7-ui
More information on Power configuration will be found in the [Power management](/t/power-management/3013) section of this documentation.
 deb-2-7-ui -->

<!-- deb-2-8-ui
More information on Power configuration will be found in the [Power management](/t/power-management/3015) section of this documentation.
 deb-2-8-ui -->

<!-- deb-2-9-ui
More information on Power configuration will be found in the [Power management](/t/power-management/3017) section of this documentation.
 deb-2-9-ui -->

<!-- deb-3-0-ui
More information on Power configuration will be found in the [Power management](/t/power-management/4072) section of this documentation.
 deb-3-0-ui -->

<!-- snap-2-7-ui
More information on Power configuration will be found in the [Power management](/t/power-management/3007) section of this documentation.
 snap-2-7-ui -->

<!-- snap-2-8-ui
More information on Power configuration will be found in the [Power management](/t/power-management/3009) section of this documentation.
 snap-2-8-ui -->

<!-- snap-2-9-ui
More information on Power configuration will be found in the [Power management](/t/power-management/3011) section of this documentation.
 snap-2-9-ui -->

<!-- snap-3-0-ui
More information on Power configuration will be found in the [Power management](/t/power-management/4070) section of this documentation.
 snap-3-0-ui -->

<h2>Summary</h2>

This article has offered you a cursory glimpse into machines and how they are configured and managed in MAAS.  Read on through this section of the documentation to learn more.
