||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/power-management-snap-2-7-cli/3006) ~ [UI](/t/power-management-snap-2-7-ui/3007)|[CLI](/t/power-management-snap-2-8-cli/3008) ~ [UI](/t/power-management-snap-2-8-ui/3009)|[CLI](/t/power-management-snap-2-9-cli/3010) ~ [UI](/t/power-management-snap-2-9-ui/3011)|[CLI](/t/power-management-snap-3-0-cli/4069) ~ [UI](/t/power-management-snap-3-0-ui/4070)|
Packages|[CLI](/t/power-management-deb-2-7-cli/3012) ~ [UI](/t/power-management-deb-2-7-ui/3013)|[CLI](/t/power-management-deb-2-8-cli/3014) ~ [UI](/t/power-management-deb-2-8-ui/3015)|[CLI](/t/power-management-deb-2-9-cli/3016) ~ [UI](/t/power-management-deb-2-9-ui/3017)|[CLI](/t/power-management-deb-3-0-cli/4071) ~ [UI](/t/power-management-deb-3-0-ui/4072)|

To manage a machine, MAAS must be able to power cycle it, usually through the machine's [BMC](https://en.wikipedia.org/wiki/Intelligent_Platform_Management_Interface#Baseboard_management_controller) card.  Until you configure the power type, a newly-added machine can't be enlisted and used by MAAS.


<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli 
#### Four questions you may have:

1. [How do I configure a machine's power type?](#heading--config-power-type)
2. [Show me a catalogue of power parameters, by type.](#heading--power-catalogue)
3. [Can you give me an example of the virsh power type?](#heading--example-virsh-kvm-power-type)
4. [Which BMC drivers are supported?](#heading--bmc-driver-support)
 snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli -->

<!-- snap-3-0-ui snap-3-0-cli deb-3-0-ui deb-3-0-cli
#### Five questions you may have:

1. [How do I configure a machine's power type?](#heading--config-power-type)
2. [Show me a catalogue of power parameters, by type.](#heading--power-catalogue)
3. [Can you give me an example of the virsh power type?](#heading--example-virsh-kvm-power-type)
4. [Which BMC drivers are supported?](#heading--bmc-driver-support)
5. [How do I configure and use IBM Z with MAAS?](#heading--configure-use-ibm-z)
 snap-3-0-ui snap-3-0-cli deb-3-0-ui deb-3-0-cli -->

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
<a href="#heading--config-power-type"><h2 id="heading--config-power-type">Configure a machine's power type</h2></a>

To configure a machine's power type, click on the machine from the 'Machines' page of the web UI, then select its 'Configuration' tab. Scroll down until you find the Power configuration. If the power type is undefined, the following will be displayed:

<a href="https://assets.ubuntu.com/v1/4fae5977-nodes-power-types__2.4_undefined.png" target = "_blank"><img src="https://assets.ubuntu.com/v1/4fae5977-nodes-power-types__2.4_undefined.png"></a>

Choose a type in the drop-down menu that corresponds to the machine's underlying machine's BMC card.

<a href="https://assets.ubuntu.com/v1/b53c6613-nodes-power-types__2.4_selection.png" target = "_blank"><img src="https://assets.ubuntu.com/v1/b53c6613-nodes-power-types__2.4_selection.png"></a>

Fill in the resulting form; the information required will depends on the power type:
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui  snap-3-0-ui deb-3-0-ui -->

<!-- snap-2-7-ui deb-2-7-ui
| CLI power_type code | Description |
|-----|-----|
| [amt](#heading--amt) |Intel AMT |
| [apc](#heading--apc) | American Power Conversion (APC) PDU |
| [dli](#heading--dli) | Digital Loggers, Inc. PDU |
| [hmc](#heading--hmc) | IBM Hardware Management Console (HMC) |
| [ipmi](#heading--ipmi) | IPMI |
| [manual](#heading--manual) | Manual power configuration |
| [moonshot](#heading--moonshot) | HP Moonshot - iLO4 (IPMI) |
| [mscm](#heading--mscm) | HP Moonshot - iLO Chassis Manager |
| [msftocs](#heading--mscm) | Microsoft OCS - Chassis Manager |
| [nova](#heading--nova) | OpenStack Nova |
| [openbmc](#heading--openbmc) | OpenBMC Power Driver |
| [recs_box](#heading--recs_box) | Christmann RECS-Box Power Driver |
| [redfish](#heading--redfish) | Redfish |
| [sm15k](#heading--sm15k) | SeaMicro 15000 |
| [ucsm](#heading--ucsm) | Cisco UCS Manager |
| [virsh](#heading--virsh) | libvirt KVM |
| [vmware](#heading--vmware) | VMware |
| [wedge](#heading--wedge) | Facebook's Wedge |
snap-2-7-ui deb-2-7-ui -->

<!-- snap-2-8-ui deb-2-8-ui 
| CLI power_type code | Description |
|-----|-----|
| [amt](#heading--amt) |Intel AMT |
| [apc](#heading--apc) | American Power Conversion (APC) PDU |
| [dli](#heading--dli) | Digital Loggers, Inc. PDU |
| [hmc](#heading--hmc) | IBM Hardware Management Console (HMC) |
| [lxd](#heading--lxd) | LXD VM |
| [ipmi](#heading--ipmi) | IPMI |
| [manual](#heading--manual) | Manual power configuration |
| [moonshot](#heading--moonshot) | HP Moonshot - iLO4 (IPMI) |
| [mscm](#heading--mscm) | HP Moonshot - iLO Chassis Manager |
| [msftocs](#heading--mscm) | Microsoft OCS - Chassis Manager |
| [nova](#heading--nova) | OpenStack Nova |
| [openbmc](#heading--openbmc) | OpenBMC Power Driver |
| [recs_box](#heading--recs_box) | Christmann RECS-Box Power Driver |
| [redfish](#heading--redfish) | Redfish |
| [sm15k](#heading--sm15k) | SeaMicro 15000 |
| [ucsm](#heading--ucsm) | Cisco UCS Manager |
| [virsh](#heading--virsh) | libvirt KVM |
| [vmware](#heading--vmware) | VMware |
| [wedge](#heading--wedge) | Facebook's Wedge |
snap-2-8-ui deb-2-8-ui -->

<!-- snap-2-9-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
| CLI power_type code | Description |
|-----|-----|
| [amt](#heading--amt) |Intel AMT |
| [apc](#heading--apc) | American Power Conversion (APC) PDU |
| [dli](#heading--dli) | Digital Loggers, Inc. PDU |
| [hmc](#heading--hmc) | IBM Hardware Management Console (HMC) |
| [lxd](#heading--lxd) | LXD VM |
| [ipmi](#heading--ipmi) | IPMI |
| [manual](#heading--manual) | Manual power configuration |
| [moonshot](#heading--moonshot) | HP Moonshot - iLO4 (IPMI) |
| [mscm](#heading--mscm) | HP Moonshot - iLO Chassis Manager |
| [msftocs](#heading--mscm) | Microsoft OCS - Chassis Manager |
| [nova](#heading--nova) | OpenStack Nova |
| [openbmc](#heading--openbmc) | OpenBMC Power Driver |
| [proxmox](#heading--proxmox) | ProxMox Power Driver |
| [recs_box](#heading--recs_box) | Christmann RECS-Box Power Driver |
| [redfish](#heading--redfish) | Redfish |
| [sm15k](#heading--sm15k) | SeaMicro 15000 |
| [ucsm](#heading--ucsm) | Cisco UCS Manager |
| [virsh](#heading--virsh) | libvirt KVM |
| [vmware](#heading--vmware) | VMware |
| [webhook](#heading--webhook) | Webhook |
| [wedge](#heading--wedge) | Facebook's Wedge |
 snap-2-9-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui -->

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
Click 'Save changes' to finish. Once that's done, MAAS performs a power check on the machine. A successful power check is a good indication that MAAS can properly communicate with the machine, that is, it should quickly result in a power status of "Power off". A failed attempt will show:

<a href="https://assets.ubuntu.com/v1/3bd5e93b-nodes-power-types__2.4_power-error.png" target = "_blank"><img src="https://assets.ubuntu.com/v1/3bd5e93b-nodes-power-types__2.4_power-error.png"></a>

If you see this error, double-check your entered values by editing the power type, or  consider another power type altogether.

Another possible cause for this error may be the networking: traffic may be getting filtered between the rack controller and the BMC card.

<a href="#heading--power-catalogue"><h2 id="heading--power-catalogue">Power catalogue</h2></a>

The following catalogue helps to explain the fields in the "create machine" dialogue above.  Note that most of the multiple-choice fields have drop-down menus to assist with your choice.

<a href="#heading--amt"><h3 id="heading--amt">Intel AMT</h3></a>

| Form field | Description | Required |
|-----|-----|-----|
| Power password | Password to access unit | Optional |
| Power address | IP address of unit | Required |

<a href="#heading--apc"><h3 id="heading--apc">American Power Conversion (APC) PDU</h3></a>

| Form field | Description | Required |
|-----|-----|-----|
| IP for APC PDU | IP address of unit | Required |
| APU PDU node outlet number (1-16) | PDU node outlet number | Required |
| Power ON outlet delay (seconds) | outlet power ON delay | Optional, default=5 |

<a href="#heading--dli"><h3 id="heading--dli">Digital Loggers, Inc. PDU</h3></a>

| Form field | Description | Required |
|-----|-----|-----|
| Outlet ID | outlet ID | Required |
| Power address | IP address of unit | Required |
| Power user | Username to login | Optional |
| Power password | Password to access unit | Optional |

<a href="#heading--hmc"><h3 id="heading--hmc">IBM Hardware Management Console (HMC)</h3></a>

| Form field | Description | Required |
|-----|-----|-----|
| IP for HMC | IP address of unit | Required |
| HMC username | Username to login | Optional |
| HMC password | Password to access unit | Optional |
| HMC Managed System server name | HMC managed server name | Required |
| HMC logical partition | HMC logical partition of unit | Required |
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui -->

<!-- snap-2-8-ui snap-2-9-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
<a href="#heading--lxd"><h3 id="heading--lxd">LXD VMs</h3></a>

| Form field | Description | Required |
|-----|-----|-----|
| LXD address | IP address of unit | Required |
| Instance name | LXD container instance name | Required |
| LXD password | Password to access unit | Optional |
snap-2-8-ui snap-2-9-ui deb-2-8-ui deb-2-9-ui  snap-3-0-ui deb-3-0-ui -->

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 

<a href="#heading--ipmi"><h3 id="heading--ipmi">IPMI</h3></a>

snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui  snap-3-0-ui deb-3-0-ui -->

<!-- snap-2-7-ui deb-2-7-ui snap-2-8-ui deb-2-8-ui

Some of the fields for this power type have fixed choices, indicated in the "Choices" column.

| Form field | Description | Choices | Required |
|-----|-----|-----|-----|
| Power driver | Power driver |`LAN [IPMI 1.5]` | Required |
| | | `LAN_2_0 [IPMI 2.0]`|
| Power boot type | Boot type | `Automatic` | Required |
| | | `Legacy boot` | |
| | | `EFI boot` | |
| IP address | IP address of unit || Required |
| Power user | Username to login || Optional |
| Power password | Password to access unit || Optional |
| Power MAC | MAC address of unit || Optional |
snap-2-8-ui deb-2-8-ui snap-2-7-ui deb-2-7-ui -->

<!-- snap-2-9-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 

Some of the fields for this power type have fixed choices, indicated in the "Choices" column.

| Form field | Description | Choices | Required |
|-----|-----|-----|-----|
| Power driver | Power driver |`LAN [IPMI 1.5]` | Required |
| | | `LAN_2_0 [IPMI 2.0]`|
| Power boot type | Boot type | `Automatic` | Required |
| | | `Legacy boot` | |
| | | `EFI boot` | |
| IP address | IP address of unit || Required |
| Power user | Username to login || Optional |
| Power password | Password to access unit || Optional |
| Power MAC | MAC address of unit || Optional |
| K_g | K_g BMC key | | Optional (BETA) |
| Cipher suite | Cipher suite ID | - `17` <small>(17 - HMAC-SHA256::HMAC_SHA256_128::AES-CBC-128)</small> | Optional (BETA) |
| | |`3` <small>(3 - HMAC-SHA1::HMAC-SHA1-96::AES-CBC-128)</small> | |
| | |` ` (blank) <small>(freeipmi-tools default)</small> | |
| | |`8` <small>(8 - HMAC-MD5::HMAC-MD5-128::AES-CBC-128)</small> | |
| | |`12` <small>(12 - HMAC-MD5::MD5-128::AES-CBC-128)</small> | |
| Privilege level | IPMI privilege level | `User` | Optional (BETA) |
| | | `Operator` | |
| | | `Administrator` | |
snap-2-9-ui deb-2-9-ui  snap-3-0-ui deb-3-0-ui -->

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 

<a href="#heading--manual"><h3 id="heading--manual">Manual power configuration</h3></a>

Manual power configuration means exactly that -- manually configured at the unit -- hence there are no parameters to set in the "create machine" UI.

snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui -->

<a href="#heading--moonshot"><h3 id="heading--moonshot">HP Moonshot - iLO4 (IPMI)</h3></a>

| Form field | Description | Required |
|-----|-----|-----|
| Power address | IP address of unit | Required |
| Power user | Username to login | Optional |
| Power password | Password to access unit | Optional |
| Power hardware address | Hardware address of unit | Required |

<a href="#heading--mscm"><h3 id="heading--mscm">HP Moonshot - iLO Chassis Manager</h3></a>

| Form field | Description | Required |
|-----|-----|-----|
| IP for MSCM CLI API | IP address of unit | Required |
| MSCM CLI API user | Username to login | Optional |
| MSCM CLI API password | Password to access unit | Optional |
| Node ID | cXnY | Required |
|  - where  | X = cartridge number | |
|           | Y = node number | |

<a href="#heading--mscm"><h3 id="heading--mscm">Microsoft OCS - Chassis Manager</h3></a>

| Form field | Description | Required |
|-----|-----|-----|
| Power address | IP address of unit | Required |
| Power port | Port where unit is attached | Optional |
| Power user | Username to login | Optional |
| Power password | Password to access unit | Optional |
| Blade ID | Blade ID (usu. 1-24) | Required |

<a href="#heading--nova"><h3 id="heading--nova">OpenStack Nova</h3></a>

| Form field | Description | Required |
|-----|-----|-----|
| Host UUID | Host UUID | Required |
| Tenant name | Tenant name | Required |
| Username | Username to login | Required |
| Password | Password to access unit | Required |
| Auth URL | URL to access unit | Required |

<!-- snap-2-9-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
<a href="#heading--proxmox"><h3 id="heading--proxmox">Proxmox</h3></a>

| Form field | Description | Required |
|-----|-----|-----|
| Power type | Proxmox | Required |
| Host name or IP | Power address for the Proxmox driver | Required |
| Username, including realm | Power user, along with realm (i.e., Username@Realm | Required |
| Password | Required if a token name and secret aren't given | Provisional |
| API token name | Token name: must include Username without realm (i.e., Username!Token-name | Provisional |
| API token secret | Token secret | Provisional |
| Node ID | VM name or ID | Optional |
| Verify SSL connections... | Boolean, whether or not to verify SSL connections with the system's root CA certificate | Required |

 snap-2-9-ui deb-2-9-ui  snap-3-0-ui deb-3-0-ui -->

<a href="#heading--openbmc"><h3 id="heading--openbmc">OpenBMC Power Driver</h3></a>

| Form field | Description | Required |
|-----|-----|-----|
| OpenBMC address | IP address of unit | Required |
| OpenBMC user | Username to login | Required |
| OpenBMC password | Password to access unit | Required |

<a href="#heading--recs_box"><h3 id="heading--recs_box">Christmann RECS-Box Power Driver</h3></a>

| Form field | Description | Required |
|-----|-----|-----|
| Node ID | Node ID | Required |
| Power address | IP address of unit | Required |
| Power port | Port where unit is attached | Optional |
| Power user | Username to login | Optional |
| Power password | Password to access unit | Optional |

<a href="#heading--redfish"><h3 id="heading--redfish">Redfish</h3></a>

| Form field | Description | Required |
|-----|-----|-----|
| Redfish address | IP address of unit | Required |
| Redfish user | Username to login | Required |
| Redfish password | Password to access unit | Required |
| Node ID | Node ID | Optional |

<a href="#heading--sm15k"><h3 id="heading--sm15k">SeaMicro 15000</h3></a>

Some of the fields for this power type have fixed choices, indicated in the "Choices" column.

| Form field | Description | Choices | Required |
|-----|-----|-----|-----|
| System ID | System ID || Required |
| Power address | IP address of unit || Required |
| Power user | Username to login || Optional |
| Power password | Password to access unit || Optional |
| Power control type | Password to access unit| IPMI | Required |
|  |  | REST API v0.9 | |
|  |  | REST API v2.0 | |

<a href="#heading--ucsm"><h3 id="heading--ucsm">Cisco UCS Manager</h3></a>

| Form field | Description | Required |
|-----|-----|-----|
| Server UUID | Server UUID | Required |
| URL for XML API | XML API URL | Required |
| API user | API user | Optional |
| API password | API password | Optional |

<a href="#heading--virsh"><h3 id="heading--virsh">virsh - libvirt KVM</h3></a>

| Form field | Description | Required |
|-----|-----|-----|
| Address | URL of VM | Required |
| Password | API password | Optional |
| Virsh VM ID | libvirt VM UUID | Required |

<a href="#heading--vmware"><h3 id="heading--vmware">VMware</h3></a>

| Form field | Description | Required |
|-----|-----|-----|
| VM Name | VM name (if UUID unknown) | Optional |
| VM UUID | VM UUID (if known) | Optional |
| VMware IP | IP address of VM | Required |
| VMware username | Username to access VM | Required |
| VMware password | Password to access VM | Required |
| VMware API port | VMware API port number | Optional |
| VMware API protocol | VMware API protocol | Optional |

<a href="#heading--wedge"><h3 id="heading--wedge">Facebook's Wedge</h3></a>

| Form field | Description | Required |
|-----|-----|-----|
| IP address | IP address of unit | Required |
| Power user | Username to access unit | Optional |
| Power password | Password to access unit | Optional |

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui  snap-3-0-ui deb-3-0-ui 
<a href="#heading--example-virsh-kvm-power-type"><h2 id="heading--example-virsh-kvm-power-type">An example: the Virsh power type</h2></a>

Consider a machine backed by VM. Below, a 'Power type' of `Virsh` has been selected, and the 'Power address' of `qemu+ssh://ubuntu@192.168.1.2/system` has been entered (replace values as appropriate).  The value of 'Power ID' is the VM domain (guest) name, here `node2`.

<a href="https://assets.ubuntu.com/v1/c75e00a8-nodes-power-types__2.4_example-virsh.png" target = "_blank"><img src="https://assets.ubuntu.com/v1/c75e00a8-nodes-power-types__2.4_example-virsh.png"></a>

[note]
The machine's hostname -- according to MAAS -- is a randomly chosen string (here `dear.ant`). You should change this hostname to something descriptive, that helps you remember why this machine is in your MAAS network.
[/note]
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui  snap-3-0-ui deb-3-0-ui -->

<!-- snap-2-9-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
<a href="#heading--webhook"><h3 id="heading--webhook">Webhook</h3></a>

It's important to understand that the Webhook power driver is more generic than other drivers, so it has some flexibility that the underlying power driver may not support.  For example, Webhook doesn't require a username or password for the power driver, because not all power drivers work that way.  Nevertheless, the power driver you're connecting to Webhook may actually require a username and/or password.  Understanding and implementing these fields correctly for the chosen back-end power driver is the user's responsibility.

To that end, the "Required" column for this driver refers only to whether Webhook requires a value in each field.  Just because a field is optional for Webhook itself does not mean that the underlying power driver will ultimately allow that field to be unspecified.

| Form field | Description | Required (by Webhook) |
|-----|-----|-----|
| Power type | Webhook (from drop-down list) | Required |
| URI to power on the node | URI to access power driver's API for power on | Required |
| URI to power off the node | URI to access power driver's API for power off | Required |
| URI to query the nodes power status | URI to access power driver's API for power status | Required |
| Regex to confirm the node is on | Regex expression that will return a string if the power is on, and no string if the power is off | Required, defaults supplied |
| Regex to confirm the node is off | Regex expression that will return a string if the power is off, and no string if the power is on | Required, defaults supplied |
| Power user | Username to log into the power driver | Optional |
| Power password | Password to access unit | Optional |
| Power token | Power driver API token (used instead of user and password, if set) | Optional |
| Verify SSL connections... | Boolean, whether or not to verify SSL connections with the system's root CA certificate | Required |

 snap-2-9-ui deb-2-9-ui  snap-3-0-ui deb-3-0-ui -->
 
<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 
<a href="#heading--config-power-type"><h2 id="heading--config-power-type">Configure a machine's power type</h2></a>

To (re)configure a machine's power type, first find the machine's $SYSTEM_ID with the following recipe:

```
maas admin machines read | jq -r '(["HOSTNAME","SIS'S"] | (., map(length*"-"))),
(.[] | [.hostname, .system_id]) | @tsv' | column -t
```

Next, use the [MAAS CLI](/t/maas-cli/802) command `maas machines...` to (re)set the machine's power type, like this:

    maas $PROFILE machine update $SYSTEM_ID power_type="$POWER_TYPE"

where $POWER_TYPE can have the following values:
snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli  snap-3-0-cli deb-3-0-cli -->

<!-- snap-2-7-cli deb-2-7-cli
| CLI power_type code | Description |
|-----|-----|
| [amt](#heading--amt) |Intel AMT |
| [apc](#heading--apc) | American Power Conversion (APC) PDU |
| [dli](#heading--dli) | Digital Loggers, Inc. PDU |
| [eaton](#heading--eaton) | Eaton PDU |
| [hmc](#heading--hmc) | IBM Hardware Management Console (HMC) |
| [ipmi](#heading--ipmi) | IPMI |
| [manual](#heading--manual) | Manual power configuration |
| [moonshot](#heading--moonshot) | HP Moonshot - iLO4 (IPMI) |
| [mscm](#heading--mscm) | HP Moonshot - iLO Chassis Manager |
| [msftocs](#heading--mscm) | Microsoft OCS - Chassis Manager |
| [nova](#heading--nova) | OpenStack Nova |
| [openbmc](#heading--openbmc) | OpenBMC Power Driver |
| [recs_box](#heading--recs_box) | Christmann RECS-Box Power Driver |
| [redfish](#heading--redfish) | Redfish |
| [sm15k](#heading--sm15k) | SeaMicro 15000 |
| [ucsm](#heading--ucsm) | Cisco UCS Manager |
| [virsh](#heading--virsh) | libvirt KVM |
| [vmware](#heading--vmware) | VMware |
| [wedge](#heading--wedge) | Facebook's Wedge |
snap-2-7-cli deb-2-7-cli -->

<!-- snap-2-8-cli deb-2-8-cli snap-2-9-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 
| CLI power_type code | Description |
|-----|-----|
| [amt](#heading--amt) |Intel AMT |
| [apc](#heading--apc) | American Power Conversion (APC) PDU |
| [dli](#heading--dli) | Digital Loggers, Inc. PDU |
| [eaton](#heading--eaton) | Eaton PDU |
| [hmc](#heading--hmc) | IBM Hardware Management Console (HMC) |
| [lxd](#heading--lxd) | LXD VM |
| [ipmi](#heading--ipmi) | IPMI |
| [manual](#heading--manual) | Manual power configuration |
| [moonshot](#heading--moonshot) | HP Moonshot - iLO4 (IPMI) |
| [mscm](#heading--mscm) | HP Moonshot - iLO Chassis Manager |
| [msftocs](#heading--mscm) | Microsoft OCS - Chassis Manager |
| [nova](#heading--nova) | OpenStack Nova |
| [openbmc](#heading--openbmc) | OpenBMC Power Driver |
| [recs_box](#heading--recs_box) | Christmann RECS-Box Power Driver |
| [redfish](#heading--redfish) | Redfish |
| [sm15k](#heading--sm15k) | SeaMicro 15000 |
| [ucsm](#heading--ucsm) | Cisco UCS Manager |
| [virsh](#heading--virsh) | libvirt KVM |
| [vmware](#heading--vmware) | VMware |
| [wedge](#heading--wedge) | Facebook's Wedge |
snap-2-8-cli deb-2-8-cli snap-2-9-cli deb-2-9-cli  snap-3-0-cli deb-3-0-cli -->

<!-- snap-2-9-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 
| CLI power_type code | Description |
|-----|-----|
| [amt](#heading--amt) |Intel AMT |
| [apc](#heading--apc) | American Power Conversion (APC) PDU |
| [dli](#heading--dli) | Digital Loggers, Inc. PDU |
| [eaton](#heading--eaton) | Eaton PDU |
| [hmc](#heading--hmc) | IBM Hardware Management Console (HMC) |
| [lxd](#heading--lxd) | LXD VM |
| [ipmi](#heading--ipmi) | IPMI |
| [manual](#heading--manual) | Manual power configuration |
| [moonshot](#heading--moonshot) | HP Moonshot - iLO4 (IPMI) |
| [mscm](#heading--mscm) | HP Moonshot - iLO Chassis Manager |
| [msftocs](#heading--mscm) | Microsoft OCS - Chassis Manager |
| [nova](#heading--nova) | OpenStack Nova |
| [openbmc](#heading--openbmc) | OpenBMC Power Driver |
| [recs_box](#heading--recs_box) | Christmann RECS-Box Power Driver |
| [redfish](#heading--redfish) | Redfish |
| [sm15k](#heading--sm15k) | SeaMicro 15000 |
| [ucsm](#heading--ucsm) | Cisco UCS Manager |
| [virsh](#heading--virsh) | libvirt KVM |
| [vmware](#heading--vmware) | VMware |
| [wedge](#heading--wedge) | Facebook's Wedge |
 snap-2-9-cli deb-2-9-cli  snap-3-0-cli deb-3-0-cli -->

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 
Note the required and optional parameters associated with each power type.

Once you've successfully processed the command (as indicated by a stream of JSON, headed by "Success!"), MAAS performs a power check on the machine. A successful power check is a good indication that MAAS can properly communicate with the machine, that is, it should quickly result in a power status of "Power off". A failed attempt will return errors that should guide you to fix your power_parameters.

<a href="#heading--power-catalogue"><h2 id="heading--power-catalogue">Power catalogue</h2></a>

<a href="#heading--amt"><h3 id="heading--amt">Intel AMT</h3></a>

All parameters are entered as `key=value`, e.g., `power_type=amt`.  The MAAS CLI will refuse the request with informative errors if required parameters are excluded.

| Parameter | Description | Required |
|-----|-----|-----|
| `power_type` | `amt` | Required |
| `power_address` | IP address of unit | Required |
| `power_pass` | Password to access unit | Optional |

<a href="#heading--apc"><h3 id="heading--apc">American Power Conversion (APC) PDU</h3></a>

All parameters are entered as `key=value`, e.g., `power_type=apc`.  The MAAS CLI will refuse the request with informative errors if required parameters are excluded.

| Parameter | Description | Required |
|-----|-----|-----|
| `power_type` | `apc` | Required |
| `power_address` | IP address of unit | Required |
| `node_outlet` | PDU node outlet number | Required |
| `power_on_delay` | outlet power ON delay | Optional, default=5 |

<a href="#heading--dli"><h3 id="heading--dli">Digital Loggers, Inc. PDU</h3></a>

All parameters are entered as `key=value`, e.g., `power_type=dli`.  The MAAS CLI will refuse the request with informative errors if required parameters are excluded.

| Parameter | Description | Required |
|-----|-----|-----|
| `power_type` | `dli` | Required |
| `outlet_id` | outlet ID | Required |
| `power_address` | IP address of unit | Required |
| `power_user` | Username to login | Optional |
| `power_pass` | Password to access unit | Optional |

<a href="#heading--eaton"><h3 id="heading--eaton">Eaton PDU</h3></a>

All parameters are entered as `key=value`, e.g., `power_type=eaton`.  The MAAS CLI will refuse the request with informative errors if required parameters are excluded.

| Parameter | Description | Required |
|-----|-----|-----|
| `power_type` | `eaton` | Required |
| `power_address` | IP address of unit | Required |
| `node_outlet` | PDU node outlet number | Required |
| `power_on_delay` | outlet power ON delay | Optional, default=5 |

<a href="#heading--hmc"><h3 id="heading--hmc">IBM Hardware Management Console (HMC)</h3></a>

All parameters are entered as `key=value`, e.g., `power_type=hmc`.  The MAAS CLI will refuse the request with informative errors if required parameters are excluded.

| Parameter | Description | Required |
|-----|-----|-----|
| `power_type` | `hmc` | Required |
| `power_address` | IP address of unit | Required |
| `server_name` | HMC managed server name | Required |
| `lpar` | HMC logical partition of unit | Required |
| `power_user` | Username to login | Optional |
| `power_pass` | Password to access unit | Optional |
snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli  snap-3-0-cli deb-3-0-cli -->

<!-- snap-2-8-cli snap-2-9-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 
<a href="#heading--lxd"><h3 id="heading--lxd">LXD VMs</h3></a>

All parameters are entered as `key=value`, e.g., `power_type=lxd`.  The MAAS CLI will refuse the request with informative errors if required parameters are excluded.

| Parameter | Description | Required |
|-----|-----|-----|
| `power_type` | `lxd` | Required |
| `power_address` | IP address of unit | Required |
| `instance_name` | LXD container instance name | Required |
| `power_pass` | Password to access unit | Optional |
snap-2-8-cli snap-2-9-cli deb-2-8-cli deb-2-9-cli  snap-3-0-cli deb-3-0-cli -->

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 

<a href="#heading--ipmi"><h3 id="heading--ipmi">IPMI</h3></a>

snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli  snap-3-0-cli deb-3-0-cli -->

<!-- snap-2-7-cli deb-2-7-cli snap-2-8-cli deb-2-8-cli
All parameters are entered as `key=value`, e.g., `power_type=ipmi`.  The MAAS CLI will refuse the request with informative errors if required parameters are excluded.

Some of the fields for this power type have fixed choices, indicated in the "Choices" column.

| Parameter | Description | Choices | Required |
|-----|-----|-----|-----|
| `power_type` | `ipmi` | | Required |
| `power_driver` | Power driver |`LAN [IPMI 1.5]` | Required |
| | | `LAN_2_0 [IPMI 2.0]`|
| `power_boot_type` | Boot type | `Automatic` | Required |
| | | `Legacy boot` | |
| | | `EFI boot` | |
| `power_address` | IP address of unit || Required |
| `power_user` | Username to login || Optional |
| `power_pass` | Password to access unit || Optional |
| `mac_address` | MAC address of unit || Optional |
snap-2-8-cli deb-2-8-cli snap-2-7-cli deb-2-7-cli -->

<!-- snap-2-9-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 
All parameters are entered as `key=value`, e.g., `power_type=amt`.  The MAAS CLI will refuse the request with informative errors if required parameters are excluded.

Some of the fields for this power type have fixed choices, indicated in the "Choices" column.

| Parameter | Description | Choices | Required |
|-----|-----|-----|-----|
| `power_type` | `ipmi` | | Required |
| `power_driver` | Power driver |`LAN [IPMI 1.5]` | Required |
| | | `LAN_2_0 [IPMI 2.0]`|
| `power_boot_type` | Boot type | `Automatic` | Required |
| | | `Legacy boot` | |
| | | `EFI boot` | |
| `power_address` | IP address of unit || Required |
| `power_user` | Username to login || Optional |
| `power_pass` | Password to access unit || Optional |
| `mac_address` | MAC address of unit || Optional |
| `k_g` | K_g BMC key | | Optional |
| `cipher_suite_id` | Cipher suite ID | - `17` <small>(17 - HMAC-SHA256::HMAC_SHA256_128::AES-CBC-128)</small> | Optional |
| | |`3` <small>(3 - HMAC-SHA1::HMAC-SHA1-96::AES-CBC-128)</small> | |
| | |` ` (blank) <small>(freeipmi-tools default)</small> | |
| | |`8` <small>(8 - HMAC-MD5::HMAC-MD5-128::AES-CBC-128)</small> | |
| | |`12` <small>(12 - HMAC-MD5::MD5-128::AES-CBC-128)</small> | |
| `privilege_level` | IPMI privilege level | `User` | Optional |
| | | `Operator` | |
| | | `Administrator` | |
| `mac_address` | MAC address of unit || Optional |
snap-2-9-cli deb-2-9-cli  snap-3-0-cli deb-3-0-cli -->

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 

<a href="#heading--manual"><h3 id="heading--manual">Manual power configuration</h3></a>

Manual power configuration means exactly that -- manually configured at the unit.  The only MAAS CLI parameter is `power_type=amt`. 

<a href="#heading--moonshot"><h3 id="heading--moonshot">HP Moonshot - iLO4 (IPMI)</h3></a>

All parameters are entered as `key=value`, e.g., `power_type=moonshot`.  The MAAS CLI will refuse the request with informative errors if required parameters are excluded.

| Parameter | Description | Required |
|-----|-----|-----|
| `power_type | `moonshot` | Required |
| `power_address` | IP address of unit | Required |
| `power_hwaddress` | Hardware address of unit | Required |
| `power_user` | Username to login | Optional |
| `power_pass` | Password to access unit | Optional |

<a href="#heading--mscm"><h3 id="heading--mscm">HP Moonshot - iLO Chassis Manager</h3></a>

All parameters are entered as `key=value`, e.g., `power_type=mscm`.  The MAAS CLI will refuse the request with informative errors if required parameters are excluded.

| Parameter | Description | Required |
|-----|-----|-----|
| `power_type | `mscm` | Required |
| `power_address` | IP address of unit | Required |
| `node_id` | cXnY | Required |
|  - where  | X = cartridge number | |
|           | Y = node number | |
| `power_user` | Username to login | Optional |
| `power_pass` | Password to access unit | Optional |

<a href="#heading--mscm"><h3 id="heading--mscm">Microsoft OCS - Chassis Manager</h3></a>

All parameters are entered as `key=value`, e.g., `power_type=msftocs`.  The MAAS CLI will refuse the request with informative errors if required parameters are excluded.

| Parameter | Description | Required |
|-----|-----|-----|
| `power_type | `msftocs` | Required |
| `power_address` | IP address of unit | Required |
| `blade_id` | Blade ID (usu. 1-24) | Required |
| `power_port` | Port where unit is attached | Optional |
| `power_user` | Username to login | Optional |
| `power_pass` | Password to access unit | Optional |

<a href="#heading--nova"><h3 id="heading--nova">OpenStack Nova</h3></a>

All parameters are entered as `key=value`, e.g., `power_type=nova`.  The MAAS CLI will refuse the request with informative errors if required parameters are excluded.

| Parameter | Description | Required |
|-----|-----|-----|
| `power_type | `nova` | Required |
| `nova_id` | Host UUID | Required |
| `os_tenantname` | Tenant name | Required |
| `os_username` | Username to login | Required |
| `os_password` | Password to access unit | Required |
| `os_authurl` | URL to access unit | Required |

<a href="#heading--openbmc"><h3 id="heading--openbmc">OpenBMC Power Driver</h3></a>

All parameters are entered as `key=value`, e.g., `power_type=openbmc`.  The MAAS CLI will refuse the request with informative errors if required parameters are excluded.

| Parameter | Description | Required |
|-----|-----|-----|
| `power_type` | `openbmc` | Required |
| `power_address` | IP address of unit | Required |
| `power_user` | Username to login | Required |
| `power_pass` | Password to access unit | Required |

<a href="#heading--recs_box"><h3 id="heading--recs_box">Christmann RECS-Box Power Driver</h3></a>

All parameters are entered as `key=value`, e.g., `power_type=recs_box`.  The MAAS CLI will refuse the request with informative errors if required parameters are excluded.

| Parameter | Description | Required |
|-----|-----|-----|
| `power_type | `recs_box` | Required |
| `node_id` | Node ID | Required |
| `power_address` | IP address of unit | Required |
| `power_port` | Port where unit is attached | Optional |
| `power_user` | Username to login | Optional |
| `power_pass` | Password to access unit | Optional |

<a href="#heading--redfish"><h3 id="heading--redfish">Redfish</h3></a>

All parameters are entered as `key=value`, e.g., `power_type=redfish`.  The MAAS CLI will refuse the request with informative errors if required parameters are excluded.

| Parameter | Description | Required |
|-----|-----|-----|
| `power_type | `redfish` | Required |
| `power_address` | IP address of unit | Required |
| `power_user` | Username to login | Required |
| `power_pass` | Password to access unit | Required |
| `node_id` | Node ID | Optional |

<a href="#heading--sm15k"><h3 id="heading--sm15k">SeaMicro 15000</h3></a>

All parameters are entered as `key=value`, e.g., `power_type=sm15k`.  The MAAS CLI will refuse the request with informative errors if required parameters are excluded.

Some of the fields for this power type have fixed choices, indicated in the "Choices" column.

| Parameter | Description | Choices | Required |
|-----|-----|-----|-----|
| `power_type` | `sm15k` | | Required |
| `system_id` | System ID || Required |
| `power_address` | IP address of unit || Required |
| `power_control` | Password to access unit| ipmi | Required |
|  |  | restapi | |
|  |  | restapi2 | |
| `power_user` | Username to login || Optional |
| `power_pass` | Password to access unit || Optional |

<a href="#heading--ucsm"><h3 id="heading--ucsm">Cisco UCS Manager</h3></a>

All parameters are entered as `key=value`, e.g., `power_type=ucsm`.  The MAAS CLI will refuse the request with informative errors if required parameters are excluded.

| Parameter | Description | Required |
|-----|-----|-----|
| `power_type` | `ucsm` | Required |
| `uuid` | Server UUID | Required |
| `power_address` | URL for XML API | Required |
| `power_user` | API user | Optional |
| `power_pass` | API password | Optional |

<a href="#heading--virsh"><h3 id="heading--virsh">virsh - libvirt KVM</h3></a>

All parameters are entered as `key=value`, e.g., `power_type=virsh`.  The MAAS CLI will refuse the request with informative errors if required parameters are excluded.

| Parameter | Description | Required |
|-----|-----|-----|
| `power_type` | `virsh` | Required |
| `power_id` | libvirt VM UUID | Required |
| `power_address` | URL of VM | Required |
| `power_pass` | API password | Optional |

<a href="#heading--vmware"><h3 id="heading--vmware">VMware</h3></a>

All parameters are entered as `key=value`, e.g., `power_type=vmware`.  The MAAS CLI will refuse the request with informative errors if required parameters are excluded.

| Parameter | Description | Required |
|-----|-----|-----|
| `power_type` | `vmware` | Required |
| `power_vm_name` | VM name (if UUID unknown) | Optional |
| `power_uuid` | VM UUID (if known) | Optional |
| `power_address` | IP address of VM | Required |
| `power_user` | Username to access VM | Required |
| `power_pass` | Password to access VM | Required |
| `power_port` | VMware API port number | Optional |
| `power_protocol` | VMware API protocol | Optional |

<a href="#heading--wedge"><h3 id="heading--wedge">Facebook's Wedge</h3></a>

All parameters are entered as `key=value`, e.g., `power_type=amt`.  The MAAS CLI will refuse the request with informative errors if required parameters are excluded.

| Parameter | Description | Required |
|-----|-----|-----|
| `power_type` | `wedge` | Required |
| `power_address` | IP address of unit | Required |
| `power_user` | Username to access unit | Optional |
| `power_pass` | Password to access unit | Optional |



<a href="#heading--example-virsh-kvm-power-type"><h2 id="heading--example-virsh-kvm-power-type">An example: the Virsh power type</h2></a>

Consider a machine backed by a KVM, accessed via `virsh`.  You can create a corresponding MAAS machine and set its power parameters with a command like this one:

    maas admin machines create \
    architecture=amd64 \
    mac_addresses=52:54:00:15:36:f2 \
    power_type=virsh \
    power_parameters_power_id=f677a842-571c-4e65-adc9-11e2cf92d363 \
    power_parameters_power_address=qemu+ssh://stormrider@192.168.123.1/system \
    power_parameters_power_pass=xxxxxxxx

If successful, this will return: 

    Success.

Machine-readable output follows this announcement.  The JSON generated by this command is shown in the detail block.

<details><summary>MAAS command JSON response</summary>
```
{
    "storage": 0.0,
    "tag_names": [],
    "special_filesystems": [],
    "memory": 0,
    "boot_disk": null,
    "virtualblockdevice_set": [],
    "hardware_info": {
        "system_vendor": "Unknown",
        "system_product": "Unknown",
        "system_family": "Unknown",
        "system_version": "Unknown",
        "system_sku": "Unknown",
        "system_serial": "Unknown",
        "cpu_model": "Unknown",
        "mainboard_vendor": "Unknown",
        "mainboard_product": "Unknown",
        "mainboard_serial": "Unknown",
        "mainboard_version": "Unknown",
        "mainboard_firmware_vendor": "Unknown",
        "mainboard_firmware_date": "Unknown",
        "mainboard_firmware_version": "Unknown",
        "chassis_vendor": "Unknown",
        "chassis_type": "Unknown",
        "chassis_serial": "Unknown",
        "chassis_version": "Unknown"
    },
    "address_ttl": null,
    "memory_test_status": -1,
    "other_test_status_name": "Unknown",
    "osystem": "",
    "status_message": "Commissioning",
    "netboot": true,
    "physicalblockdevice_set": [],
    "node_type": 0,
    "cpu_test_status": -1,
    "memory_test_status_name": "Unknown",
    "bcaches": [],
    "storage_test_status": 0,
    "system_id": "bhxws3",
    "status": 1,
    "commissioning_status": 0,
    "power_type": "virsh",
    "locked": false,
    "numanode_set": [
        {
            "index": 0,
            "memory": 0,
            "cores": []
        }
    ],
    "bios_boot_method": null,
    "fqdn": "ace-swan.maas",
    "node_type_name": "Machine",
    "hostname": "ace-swan",
    "volume_groups": [],
    "testing_status": 0,
    "network_test_status": -1,
    "other_test_status": -1,
    "interface_test_status": -1,
    "hwe_kernel": null,
    "blockdevice_set": [],
    "testing_status_name": "Pending",
    "power_state": "unknown",
    "min_hwe_kernel": "",
    "owner": "admin",
    "distro_series": "",
    "storage_test_status_name": "Pending",
    "cpu_speed": 0,
    "swap_size": null,
    "cpu_test_status_name": "Unknown",
    "hardware_uuid": null,
    "architecture": "amd64/generic",
    "pool": {
        "name": "default",
        "description": "Default pool",
        "id": 0,
        "resource_uri": "/MAAS/api/2.0/resourcepool/0/"
    },
    "cache_sets": [],
    "pod": null,
    "iscsiblockdevice_set": [],
    "disable_ipv4": false,
    "status_action": "",
    "boot_interface": {
        "name": "eth0",
        "id": 10,
        "product": null,
        "system_id": "bhxws3",
        "effective_mtu": 1500,
        "children": [],
        "link_connected": true,
        "enabled": true,
        "interface_speed": 0,
        "numa_node": 0,
        "firmware_version": null,
        "parents": [],
        "discovered": null,
        "params": "",
        "links": [],
        "sriov_max_vf": 0,
        "tags": [],
        "type": "physical",
        "vlan": null,
        "vendor": null,
        "link_speed": 0,
        "mac_address": "52:54:00:15:36:f2",
        "resource_uri": "/MAAS/api/2.0/nodes/bhxws3/interfaces/10/"
    },
    "cpu_count": 0,
    "domain": {
        "authoritative": true,
        "ttl": null,
        "resource_record_count": 0,
        "name": "maas",
        "is_default": true,
        "id": 0,
        "resource_uri": "/MAAS/api/2.0/domains/0/"
    },
    "current_testing_result_id": 7,
    "default_gateways": {
        "ipv4": {
            "gateway_ip": null,
            "link_id": null
        },
        "ipv6": {
            "gateway_ip": null,
            "link_id": null
        }
    },
    "interface_set": [
        {
            "name": "eth0",
            "id": 10,
            "product": null,
            "system_id": "bhxws3",
            "effective_mtu": 1500,
            "children": [],
            "link_connected": true,
            "enabled": true,
            "interface_speed": 0,
            "numa_node": 0,
            "firmware_version": null,
            "parents": [],
            "discovered": null,
            "params": "",
            "links": [],
            "sriov_max_vf": 0,
            "tags": [],
            "type": "physical",
            "vlan": null,
            "vendor": null,
            "link_speed": 0,
            "mac_address": "52:54:00:15:36:f2",
            "resource_uri": "/MAAS/api/2.0/nodes/bhxws3/interfaces/10/"
        }
    ],
    "status_name": "Commissioning",
    "commissioning_status_name": "Pending",
    "owner_data": {},
    "ip_addresses": [],
    "raids": [],
    "network_test_status_name": "Unknown",
    "description": "",
    "current_commissioning_result_id": 6,
    "interface_test_status_name": "Unknown",
    "current_installation_result_id": null,
    "zone": {
        "name": "default",
        "description": "",
        "id": 1,
        "resource_uri": "/MAAS/api/2.0/zones/default/"
    },
    "resource_uri": "/MAAS/api/2.0/machines/bhxws3/"
}
```
</details>

snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli  snap-3-0-cli deb-3-0-cli -->

<a href="#heading--bmc-driver-support"><h2 id="heading--bmc-driver-support">Which BMC drivers are supported</h2></a>

MAAS supports many types of BMC hardware, though not all the drivers have the same capabilities. See the below table for a feature comparison of the BMC drivers currently supported by MAAS.

<details><summary>Tell me about BMC</summary>

BMC, or "Baseboard Management Controller," is an extra micro-controller on the motherboard of a server which forms the interface between system-management software and the device's hardware.  The BMC can collect data from attached sensors, alert administrators to issues, and respond to remote-control commands to control system operation or power state, independent of the system's CPU.

In the context of MAAS, the BMC is generally controlled by SNMP commands.  Any given BMC will function in the context of one or more "power types," which are physical interfaces that permit use of the IPMI ("Intelligent Platform Management Interface") protocol.  Each power type has a different set of expected parameters required to access and command the BMC.

</details>

<table>
<colgroup>
<col width="35%" />
<col width="12%" />
<col width="10%" />
<col width="14%" />
<col width="15%" />
<col width="11%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Power Driver (<em>X=supported</em>)</th>
<th>PXE Next Boot</th>
<th>Power Querying</th>
<th>Chassis/Pod Configuration</th>
<th>Enhanced UI Error Reporting</th>
<th>BMC Enlistment</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">American Power Conversion (APC) - PDU</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td align="left">Cisco UCS Manager</td>
<td>X</td>
<td>X</td>
<td>X</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td align="left">Digital Loggers, Inc. - PDU</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td align="left">Facebook's Wedge <code>*</code></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td align="left">HP Moonshot - iLO Chassis Manager</td>
<td>X</td>
<td>X</td>
<td>X</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td align="left">HP Moonshot - iLO4 (IPMI)</td>
<td>X</td>
<td>X</td>
<td></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td align="left">IBM Hardware Management Console (HMC)</td>
<td>X</td>
<td>X</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td align="left">IPMI</td>
<td>X</td>
<td>X</td>
<td></td>
<td>X</td>
<td>X</td>
</tr>
<tr class="odd">
<td align="left">Intel AMT</td>
<td>X</td>
<td>X</td>
<td></td>
<td>X</td>
<td></td>
</tr>
<tr class="even">
<td align="left">Manual</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td align="left">Microsoft OCS - Chassis Manager</td>
<td>X</td>
<td>X</td>
<td>X</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td align="left">OpenStack Nova</td>
<td></td>
<td>X</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td align="left">Rack Scale Design</td>
<td>X</td>
<td>X</td>
<td>X</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td align="left">SeaMicro 15000</td>
<td>X</td>
<td>X</td>
<td>X</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td align="left">Sentry Switch CDU - PDU</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td align="left">VMWare</td>
<td>X</td>
<td>X</td>
<td>X</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td align="left">Virsh (virtual systems)</td>
<td>X</td>
<td>X</td>
<td>X</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

`*` The 'Facebook's Wedge' OpenBMC power driver is considered experimental at this time.

<!-- snap-3-0-ui snap-3-0-cli deb-3-0-ui deb-3-0-cli 
<a href="#heading--configure-use-ibm-z"><h2 id="heading--configure-use-ibm-z">How do I configure and use IBM Z with MAAS?</h2></a>

The IBM Z or LinuxONE system can host MAAS controllers and is able to deploy predefined logical partitions (LPARs) KVM host(s), and virtual machines, if the mainframe is set up properly for MAAS.

The basic architecture is similar to this:

<a href="https://discourse.maas.io/uploads/default/original/2X/d/d78aec0bd5d5f485697701ed7316944f918fef94.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/d/d78aec0bd5d5f485697701ed7316944f918fef94.png"></a>

Networking would be structured like this:

<a href="https://discourse.maas.io/uploads/default/original/2X/8/841305949182ba64037f9806396a0e60fdc46d23.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/8/841305949182ba64037f9806396a0e60fdc46d23.png"></a>

Note that net-booting the KVM guests (through the two bridges) can be problematic.  There are two options:

1. Adding VNIC characteristics to enable "learning" on the network interface that's the base for bridge "br2."  This is the recommended approach.

2. Enable full promiscuous bridge port mode at the network interface that's the base for bridge "br2."  This approach is not recommended because it has some built-in limitations.

MAAS will automatically configure option 1 for you, in case an LPAR is deployed as KVM host (the bridge names may differ).

In order to achieve this configuration, there are a number of steps that must be executed; specifically, you must know how to:

* [Evaluate IBM Z requirements](#heading--ibm-z-requirements)
* [Login to the IBM Z](#heading--ibm-z-login)
* [Set up a suitable partition for MAAS](#heading--set-up-ibm-z-partition)
* [Set up networking for MAAS](#heading--set-up-ibm-z-networking)
* [Set up storage for MAAS](#heading--set-up-ibm-z-storage)
* [Set the partition boot parameters](#heading--set-the-boot-parameters)
* [Set up your IBM Z virtual machines for enlistment](#heading--set-up-ibm-z-enlistment)

The MAAS controller does not necessarily need to run on an LPAR on the IBM Z system itself, but can also run on a different system outside. But since the MAAS controller requires a network connection to the hardware management console (HMC), it is recommended to keep it co-located and (for security reasons) as close as possible to the HMC and run it in a dedicated LPAR.

Such a MAAS controller LPAR should have at least two SMT hardware threads (one IFL), since it runs several services (bind, rack-, region-controller and more), 16 GB RAM and 100 GB disk space - recommended is to use the double amount of these resources.

The resources of the LPARs to deploy on ('machines' in terms of MAAS) depending on the use case. LPARs that are deployed as KVM host would of course require significantly more resources to be able to host KVM guest on top.

There are several constraints on the definition and setup of the 'machine' LPARs - please see below.

<a href="#heading--ibm-z-requirements"><h3 id="heading--ibm-z-requirements">Evaluate IBM Z requirements</h3></a>

The system requirements to host MAAS and its virtual machines on the IBM Z platform are as follows:

* IBM z14 GA2 (or newer) or IBM LinuxONE III (or newer)
* HMC running in DPM mode (mandatory, traditional mode is not supported!)
* HMC firmware level H39 - (HMC at H40 and SE at S55) 
* HMCs Rest-API enabled 
* python-zhmcclient (0.29 or later) running on the MAAS controller system, connected to the HMC
* HMC user ID for the zhmcclient access to the HMC API (must have permissions for the “Manage Web Services API Logs” role and “Manage Web Services API Logs” role)
* I/O auto-configuration enabled for the ‘machine’ LPARs
* zFCP (SCSI) disk storage (only, no DASD support), recommended are two disks, one defined as type ‘boot,’ the second as type ‘data’
* a dedicated storage group per ‘machine’ LPAR; these must include the dedicated zFCP storage for this particular managed LPAR only (‘boot’ and ‘data’ for LPAR n) - but no additional shared storage!
* qeth network devices (Hipersockets or OSA, recommended); at least one qeth NIC, recommended two (or more)
* Ubuntu Server 20.04 installed on a dedicated system (LPAR or PC), that acts as MAAS Controller
* one or more LPARs as ‘machines’ (aka MAAS deployment targets)

Be aware that these are minimum system requirements.

<a href="#heading--ibm-z-login"><h3 id="heading--ibm-z-login">Access the HMC and login to the IBM Z</h3></a>

To login to the HMC, you must have at least “system programmer” privileges. Gaining that level of access is beyond the scope of this document. Once you are sure that you have the necessary access, you first need to navigate to the Hardware Management Console (HMC) application in your Web browser:

<a href="https://discourse.maas.io/uploads/default/original/2X/d/d085c8113e403546484778c858c27344e8986597.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/d/d085c8113e403546484778c858c27344e8986597.png"></a>

Click on the "Log on..." link, which will bring you to a login screen:

<a href="https://discourse.maas.io/uploads/default/original/2X/5/5ccdfac4dc985260dcedd01284d24c5e8e5199d9.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/5/5ccdfac4dc985260dcedd01284d24c5e8e5199d9.png"></a>

Upon successfully logging on, you will land on the Welcome Screen:

<a href="https://discourse.maas.io/uploads/default/original/2X/d/d18afe140a1971621ed44fa5fae36033927e293e.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/d/d18afe140a1971621ed44fa5fae36033927e293e.png"></a>

Select the "Tasks Index" on the left-hand navigation:

<a href="https://discourse.maas.io/uploads/default/original/2X/c/c030c8280b0a6dcfdd0365f9cf50238ae708e34b.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/c/c030c8280b0a6dcfdd0365f9cf50238ae708e34b.jpeg"></a>

From here, you will be able to access the commands needed to prepare your IBM Z to host MAAS.

<a href="#heading--set-up-ibm-z-partition"><h3 id="heading--set-up-ibm-z-partition">Set up a suitable IBM Z partition for a MAAS machine</h3></a>

In order to prevent MAAS from taking over the entire system, you must assign both the controller and the ‘machines’ / KVM hosts to specific partitions, with suitable limitations. To set up suitable IBM Z partitions for hosting MAAS, you must choose “Partition Details” from the “Tasks Index,” which will bring you to a screen like this one:

<a href="https://discourse.maas.io/uploads/default/original/2X/2/29e0cc00d68a5add1b13b1d50313ff6966f251a9.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/2/29e0cc00d68a5add1b13b1d50313ff6966f251a9.png"></a>

You must then choose the “target object” (in this case we’ve chosen TA05) to be operated upon:

<a href="https://discourse.maas.io/uploads/default/original/2X/7/754c4926ecf5d9330b60c9b58bdd15bde6f24144.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/7/754c4926ecf5d9330b60c9b58bdd15bde6f24144.png"></a>

Click “OK,” and you’ll arrive at a screen similar to the one below:

<a href="https://discourse.maas.io/uploads/default/original/2X/0/0ecf9bd89c132fd2c7ff8b879dd6c1b4d3090a99.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/0/0ecf9bd89c132fd2c7ff8b879dd6c1b4d3090a99.png"></a>

Make sure you’re on the “Partitions” tab, and select the desired object (“TA05…”):

<a href="https://discourse.maas.io/uploads/default/original/2X/0/018d8309a1a16571df56a6672cff26e60f42075a.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/0/018d8309a1a16571df56a6672cff26e60f42075a.jpeg"></a>

Right-click on the selected object and select “Partition Details:”

<a href="https://discourse.maas.io/uploads/default/original/2X/5/5a7f696435b504eb212234acdd09c928f16b1670.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/5/5a7f696435b504eb212234acdd09c928f16b1670.jpeg"></a>

On the “General” tab, edit the partition details to suit your proposed MAAS deployment:

<a href="https://discourse.maas.io/uploads/default/original/2X/6/60ff5ca98d8b615ee4a947607872c973cf2c7f41.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/6/60ff5ca98d8b615ee4a947607872c973cf2c7f41.png"></a>

Next, you will set up the networking details for this partition, as shown in the following section.

<a href="#heading--set-up-ibm-z-networking"><h3 id="heading--set-up-ibm-z-networking">Set up IBM Z networking for a MAAS machine</h3></a>

To properly enable networking within the IBMZ partitions, you must change to the “Network” tab under “Partition Details:”

<a href="https://discourse.maas.io/uploads/default/original/2X/d/daf386497781df42ba7ffaa518c1f186ebef66ee.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/d/daf386497781df42ba7ffaa518c1f186ebef66ee.png"></a>

Click on the NIC of interest to bring up the “NIC Details” screen:

<a href="https://discourse.maas.io/uploads/default/original/2X/e/e9b65711cf97dd722db1b1df4b69d4f590166a99.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/e/e9b65711cf97dd722db1b1df4b69d4f590166a99.png"></a>

Confirm that the parameters on this screen are consistent with your planned MAAS deployment, then bring up the network adapter(either OSA or Hipersockets) by selecting it:

<a href="https://discourse.maas.io/uploads/default/original/2X/0/0a0873d7cd40147884c861d1fcde15ddc37c8853.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/0/0a0873d7cd40147884c861d1fcde15ddc37c8853.png"></a>

Ensure that all settings on the “General” tab conform to your planned MAAS deployment; then select the “Network Interface Cards” tab on the left-hand navigation:

<a href="https://discourse.maas.io/uploads/default/original/2X/0/0a0873d7cd40147884c861d1fcde15ddc37c8853.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/0/0a0873d7cd40147884c861d1fcde15ddc37c8853.png"></a>

Again, ensure that the parameters associated with the networking arrangement are consistent with your planned MAAS deployment.

Next, you will set up the storage layout for your MAAS partition(s).

<a href="#heading--set-up-ibm-z-storage"><h3 id="heading--set-up-ibm-z-storage">Set up IBM Z storage for a MAAS machine</h3></a>

To set up suitable storage for a MAAS deployment, you should bring up the “Partition Details” for your chosen MAAS partition and select the “Storage” tab from the left-hand navigation:

<a href="https://discourse.maas.io/uploads/default/original/2X/c/c25792eeacd5aef57ca74a68b203c23ed74268d7.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/c/c25792eeacd5aef57ca74a68b203c23ed74268d7.png"></a>

Choose the “VOLUMES” sub-tab, and lick on the hyperlinked partition name to bring up the storage configuration tab:

<a href="https://discourse.maas.io/uploads/default/original/2X/c/cf8d1427abda94ccd3b79966d06bee210ac1240b.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/c/cf8d1427abda94ccd3b79966d06bee210ac1240b.png"></a>

Click on “GET DETAILS” for the Boot Volume in the Volume list to bring up the “Configuration details” screen:

<a href="https://discourse.maas.io/uploads/default/original/2X/a/a081c97b8196e708495156187b983b70c32fcdc5.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/a/a081c97b8196e708495156187b983b70c32fcdc5.png"></a>

Ensure that the Boot Volume is configured appropriately for your planned MAAS deployment, then click “Done.” Then return to the storage configuration tab and choose the Data Volume, and tune it to the appropriate parameters.

Next, choose the “ADAPTERS” sub-tab to bring up information on the storage adapters:

<a href="https://discourse.maas.io/uploads/default/original/2X/8/821edff17e3fe8f2fbf9b5cb1682928dc9bb34d7.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/8/821edff17e3fe8f2fbf9b5cb1682928dc9bb34d7.png"></a>

Set any necessary parameters to conform to your planned MAAS deployment.

<a href="#heading--set-the-boot-parameters"><h3 id="heading--set-the-boot-parameters">Set the partition boot parameters</h3></a>

Return to the “Partition Details” screen and select the “Boot” tab in the left-hand navigation:

<a href="https://discourse.maas.io/uploads/default/original/2X/c/c5df4937135c1a9a1758b20855742bd038700c65.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/c/c5df4937135c1a9a1758b20855742bd038700c65.png"></a>

Change any settings as necessary to support your planned MAAS deployment.

<a href="#heading--set-up-ibm-z-enlistment"><h3 id="heading--set-up-ibm-z-enlistment">Set up your IBM Z virtual machine for enlistment</h3></a>

To cause IBM Z KVM partition guests to enlist, it’s necessary to manually put in the BMC information for each guest. MAAS can then detect the guest, enlist it, and boot it as necessary.

 snap-3-0-ui snap-3-0-cli deb-3-0-ui deb-3-0-cli -->
