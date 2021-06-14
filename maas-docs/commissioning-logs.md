||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/commissioning-logs-snap-2-7-cli/2490) ~ [UI](/t/commissioning-logs-snap-2-7-ui/2491)|[CLI](/t/commissioning-logs-snap-2-8-cli/2492) ~ [UI](/t/commissioning-logs-snap-2-8-ui/2493)|[CLI](/t/commissioning-logs-snap-2-9-cli/2494) ~ [UI](/t/commissioning-logs-snap-2-9-ui/2495)|[CLI](/t/commissioning-logs-snap-3-0-cli/3869) ~ [UI](/t/commissioning-logs-snap-3-0-ui/3870)|
Packages|[CLI](/t/commissioning-logs-deb-2-7-cli/2496) ~ [UI](/t/commissioning-logs-deb-2-7-ui/2497)|[CLI](/t/commissioning-logs-deb-2-8-cli/2498) ~ [UI](/t/commissioning-logs-deb-2-8-ui/2499)|[CLI](/t/commissioning-logs-deb-2-9-cli/2500) ~ [UI](/t/commissioning-logs-deb-2-9-ui/2501)|[CLI](/t/commissioning-logs-deb-3-0-cli/3871) ~ [UI](/t/commissioning-logs-deb-3-0-ui/3872)|

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 
The command line allows you to retrieve the verbatim logs of commissioning script runs, including those that are currently in progress.

If you only want to see the latest or currently-running result, you can use `current-commissioning`, `current-testing`, or `current-installation` instead of an id:

``` bash
maas $PROFILE node-script-result read $SYSTEM_ID $RESULTS
```

You can also limit which results are returned by type (commissioning, testing, or installation), script name, or script run:

``` bash
maas $PROFILE node-script-results read \
 $SYSTEM_ID type=$SCRIPT_TYPE filters=$SCRIPT_NAME,$TAGS
```

You can also suppress failed results, which is useful if you want to ignore a known failure:

``` bash
maas $PROFILE node-script-results update \
 $SYSTEM_ID type=$SCRIPT_TYPE filters=$SCRIPT_NAME,$TAGS suppressed=$SUPPRESSED
```

where `$SUPPRESSED` is either `True` or `False`. The JSON formatted output to the above command will include 'results' dictionary with an entry for `suppressed`:

``` json
"results": [
    {
        "id": 21,
        "created": "Tue, 02 Apr 2019 17:00:36 -0000",
        "updated": "Tue, 02 Apr 2019 20:56:41 -0000",
        "name": "smartctl-validate",
        "status": 5,
        "status_name": "Aborted",
        "exit_status": null,
        "started": "Tue, 02 Apr 2019 20:56:41 -0000",
        "ended": "Tue, 02 Apr 2019 20:56:41 -0000",
        "runtime": "0:00:00",
        "starttime": 1554238601.765214,
        "endtime": 1554238601.765214,
        "estimated_runtime": "0:00:00",
        "parameters": {
            "storage": {
                "argument_format": "{path}",
                "type": "storage",
                "value": {
                    "id_path": "/dev/vda",
                    "model": "",
                    "name": "sda",
                    "physical_blockdevice_id": 1,
                    "serial": ""
                }
            }
        },
        "script_id": 1,
        "script_revision_id": null,
        "suppressed": true
    }
]
```

Finally, results can be downloaded, either to stdout, stderr, as combined output or as a tar.xz:

``` bash
maas $PROFILE node-script-result download $SYSTEM_ID $RUN_ID output=all \
 filetype=tar.xz > $LOCAL_FILENAME
```

[note]
**$RUN_ID** is labelled `id` in the verbose result output.
[/note]
snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli  snap-3-0-cli deb-3-0-cli -->

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
Commissioning logs, which are presented on the "Commissioning" tab for any machine in the "Ready" state, contain a list of commissioning scripts with a timestamp and result.  You can view the detailed logs for each of these scripts from this tab.

When you click on the "Commissioning" tab under a given machine, you will see a screen similar to this one:

<a href="https://discourse.maas.io/uploads/default/original/1X/f2e52a4bf55b37e5ff63e7d1fab1aac32aebc48c.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/f2e52a4bf55b37e5ff63e7d1fab1aac32aebc48c.jpeg"></a> 
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui  snap-3-0-ui deb-3-0-ui -->

<!-- deb-2-7-ui
Each of the items in the "NAME" column is the name of a [commissioning script](/t/commission-machines/2473#heading--commissioning-scripts).  Each entry gives a timestamp and a result (e.g. passed, failed, ...). At the end of each line is a link to view the log. It's worth taking a look at each of the script logs and their typical output.
 deb-2-7-ui -->

<!-- deb-2-8-ui
Each of the items in the "NAME" column is the name of a [commissioning script](/t/commission-machines/2475#heading--commissioning-scripts).  Each entry gives a timestamp and a result (e.g. passed, failed, ...). At the end of each line is a link to view the log. It's worth taking a look at each of the script logs and their typical output.
 deb-2-8-ui -->

<!-- deb-2-9-ui
Each of the items in the "NAME" column is the name of a [commissioning script](/t/commission-machines/2477#heading--commissioning-scripts).  Each entry gives a timestamp and a result (e.g. passed, failed, ...). At the end of each line is a link to view the log. It's worth taking a look at each of the script logs and their typical output.
 deb-2-9-ui -->

<!-- deb-3-0-ui
Each of the items in the "NAME" column is the name of a [commissioning script](/t/commission-machines/3866#heading--commissioning-scripts).  Each entry gives a timestamp and a result (e.g. passed, failed, ...). At the end of each line is a link to view the log. It's worth taking a look at each of the script logs and their typical output.
 deb-3-0-ui -->

<!-- snap-2-7-ui
Each of the items in the "NAME" column is the name of a [commissioning script](/t/commission-machines/2467#heading--commissioning-scripts).  Each entry gives a timestamp and a result (e.g. passed, failed, ...). At the end of each line is a link to view the log. It's worth taking a look at each of the script logs and their typical output.
 snap-2-7-ui -->

<!-- snap-2-8-ui
Each of the items in the "NAME" column is the name of a [commissioning script](/t/commission-machines/2469#heading--commissioning-scripts).  Each entry gives a timestamp and a result (e.g. passed, failed, ...). At the end of each line is a link to view the log. It's worth taking a look at each of the script logs and their typical output.
 snap-2-8-ui -->

<!-- snap-2-9-ui
Each of the items in the "NAME" column is the name of a [commissioning script](/t/commission-machines/2471#heading--commissioning-scripts).  Each entry gives a timestamp and a result (e.g. passed, failed, ...). At the end of each line is a link to view the log. It's worth taking a look at each of the script logs and their typical output.
 snap-2-9-ui -->

<!-- snap-3-0-ui
Each of the items in the "NAME" column is the name of a [commissioning script](/t/commission-machines/3874#heading--commissioning-scripts).  Each entry gives a timestamp and a result (e.g. passed, failed, ...). At the end of each line is a link to view the log. It's worth taking a look at each of the script logs and their typical output.
 snap-3-0-ui -->

<!-- snap-2-8-ui snap-2-8-cli snap-2-7-ui snap-2-7-cli deb-2-8-ui deb-2-8-cli deb-2-7-ui deb-2-7-cli
<a href="#heading--00-maas-00-support-info"><h2 id="heading--00-maas-00-support-info">00-maas-00-support-info</h2></a>

MAAS gathers information that helps to identify and characterise the machine for debugging purposes, such as the kernel, versioning of various components, etc.  This script gathers this information, mostly as a bundle to be provided to a support specialist to help get the baseline for the machine in question.  Typical output, generated when a machine passes this script, is shown in the foldout below.
snap-2-8-ui snap-2-8-cli snap-2-7-ui snap-2-7-cli deb-2-8-ui deb-2-8-cli deb-2-7-ui deb-2-7-cli -->

<!-- snap-2-9-cli snap-2-9-ui deb-2-9-cli deb-2-9-cli snap-3-0-ui deb-3-0-ui snap-3-0-cli deb-3-0-cli 
<a href="#heading--maas-support-info"><h2 id="heading--maas-support-info">maas-support-info</h2></a>

MAAS gathers information that helps to identify and characterise the machine for debugging purposes, such as the kernel, versioning of various components, etc.  This script gathers this information, mostly as a bundle to be provided to a support specialist to help get the baseline for the machine in question.

This script runs in parallel with other scripts to speed commissioning. Typical output, generated when a machine passes this script, is shown in the foldout below.
snap-2-9-cli snap-2-9-ui deb-2-9-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli snap-3-0-ui deb-3-0-ui -->

<details><summary>Typical script output</summary>

````
-----BEGIN KERNEL INFO-----
Linux 52-54-00-0b-6d-8c 4.15.0-91-generic #92-Ubuntu SMP Fri Feb 28 11:09:48 UTC 2020 86_64 x86_64 x86_64 GNU/Linux
-----END KERNEL INFO-----
-----BEGIN KERNEL COMMAND LINE-----
nomodeset ro root=squash:http://192.168.122.2:5248/images/ubuntu/amd64/generic/bionic/daily/squashfs ip=::::52-54-00-0b-6d-8c:BOOTIF ip6=off overlayroot=tmpfs overlayroot_cfgdisk=disabled cc:{'datasource_list': ['MAAS']}end_cc cloud-config-url=http://192-168-122-0--24.maas-internal:5248/MAAS/metadata/latest/by-id/pb6833/?op=get_preseed apparmor=0 log_host=192.168.122.2 log_port=5247 BOOTIF=01-52:54:00:0b:6d:8c
-----END KERNEL COMMAND LINE-----
-----BEGIN CLOUD CONFIG QUERY-----
*   Trying 192.168.122.2...
* TCP_NODELAY set
* Connected to 192-168-122-0--24.maas-internal (192.168.122.2) port 5248 (#0)
> GET /MAAS/metadata/latest/by-id/pb6833/?op=get_preseed HTTP/1.1
> Host: 192-168-122-0--24.maas-internal:5248
> User-Agent: curl/7.58.0
> Accept: */*
> 
< HTTP/1.1 200 OK
< Server: nginx/1.14.0 (Ubuntu)
< Date: Mon, 23 Mar 2020 22:02:01 GMT
< Content-Type: text/plain
< Content-Length: 1638
< Connection: keep-alive
< Vary: Authorization, Accept-Encoding
< X-Maas-Api-Hash: 96b79d21d1b0552c0342b119336f91bf6ce0bcdd
< X-Frame-Options: SAMEORIGIN
< 
{ [1638 bytes data]
* Connection #0 to host 192-168-122-0--24.maas-internal left intact
#cloud-config
apt: {preserve_sources_list: false, proxy: 'http://192-168-122-0--24.maas-internal:8000/',
  sources_list: 'deb http://archive.ubuntu.com/ubuntu $RELEASE multiverse universe
    restricted main
    # deb-src http://archive.ubuntu.com/ubuntu $RELEASE multiverse universe restricted
    main
    deb http://archive.ubuntu.com/ubuntu $RELEASE-updates multiverse universe restricted
    main
    # deb-src http://archive.ubuntu.com/ubuntu $RELEASE-updates multiverse universe
    restricted main
    deb http://archive.ubuntu.com/ubuntu $RELEASE-security multiverse universe restricted
    main
    # deb-src http://archive.ubuntu.com/ubuntu $RELEASE-security multiverse universe
    restricted main
    deb http://archive.ubuntu.com/ubuntu $RELEASE-backports multiverse universe restricted
    main
    # deb-src http://archive.ubuntu.com/ubuntu $RELEASE-backports multiverse universe
    restricted main
    '}
datasource:
  MAAS: {consumer_key: (withheld), metadata_url: 'http://192-168-122-0--24.maas-internal:5248/MAAS/metadata/',
    token_key: (withheld), token_secret: (withheld)}
manage_etc_hosts: true
packages: [python3-yaml, python3-oauthlib, freeipmi-tools, ipmitool, sshpass]
power_state: {condition: test ! -e /tmp/block-poweroff, delay: now, mode: poweroff,
  timeout: 3600}
reporting:
  maas: {consumer_key: (withheld), endpoint: 'http://192-168-122-0--24.maas-internal:5248/MAAS/metadata/status/pb6833',
    token_key: (withheld), token_secret: (withheld),
    type: webhook}
rsyslog:
  remotes: {maas: '192.168.122.2:5247'}
-----END CLOUD CONFIG QUERY-----
-----BEGIN CPU CORE COUNT AND MODEL-----
      1  Intel Core Processor (Skylake, IBRS)
-----BEGIN CPU CORE COUNT AND MODEL-----
-----BEGIN PCI INFO-----
00:00.0 Host bridge [0600]: Intel Corporation 440FX - 82441FX PMC [Natoma] [8086:1237] (rev 02)
00:01.0 ISA bridge [0601]: Intel Corporation 82371SB PIIX3 ISA [Natoma/Triton II] [8086:7000]
00:01.1 IDE interface [0101]: Intel Corporation 82371SB PIIX3 IDE [Natoma/Triton II] [8086:7010]
00:01.3 Bridge [0680]: Intel Corporation 82371AB/EB/MB PIIX4 ACPI [8086:7113] (rev 03)
00:02.0 VGA compatible controller [0300]: Red Hat, Inc. QXL paravirtual graphic card [1b36:0100] (rev 04)
00:03.0 Ethernet controller [0200]: Red Hat, Inc. Virtio network device [1af4:1000]
00:04.0 Audio device [0403]: Intel Corporation 82801FB/FBM/FR/FW/FRW (ICH6 Family) High Definition Audio Controller [8086:2668] (rev 01)
00:05.0 USB controller [0c03]: Intel Corporation 82801I (ICH9 Family) USB UHCI Controller #1 [8086:2934] (rev 03)
00:05.1 USB controller [0c03]: Intel Corporation 82801I (ICH9 Family) USB UHCI Controller #2 [8086:2935] (rev 03)
00:05.2 USB controller [0c03]: Intel Corporation 82801I (ICH9 Family) USB UHCI Controller #3 [8086:2936] (rev 03)
00:05.7 USB controller [0c03]: Intel Corporation 82801I (ICH9 Family) USB2 EHCI Controller #1 [8086:293a] (rev 03)
00:06.0 Communication controller [0780]: Red Hat, Inc. Virtio console [1af4:1003]
00:07.0 Unclassified device [00ff]: Red Hat, Inc. Virtio memory balloon [1af4:1002]
-----END PCI INFO-----
-----BEGIN USB INFO-----
Bus 001 Device 002: ID 0627:0001 Adomax Technology Co., Ltd 
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 004 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
Bus 003 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
Bus 002 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
-----END USB INFO-----
-----BEGIN MODALIASES-----
      1 acpi:ACPI0010:PNP0A05:
      1 acpi:LNXCPU:
      1 acpi:LNXPWRBN:
      2 acpi:LNXSYBUS:
      1 acpi:LNXSYSTM:
      1 acpi:PNP0303:
      1 acpi:PNP0501:
      1 acpi:PNP0700:
      1 acpi:PNP0A03:
      3 acpi:PNP0A06:
      1 acpi:PNP0B00:
      5 acpi:PNP0C0F:
      1 acpi:PNP0F13:
      2 acpi:QEMU0002:
      1 cpu:type:x86,ven0000fam0006mod005E:feature:,0000,0001,0002,0003,0004,0005,0006,0007,0008,0009,000B,000C,000D,000E,000F,0010,0011,0013,0017,0018,0019,001A,001B,002B,0034,003A,003B,003D,0068,006F,0070,0072,0074,0075,0076,0079,007F,0080,0081,0085,0089,008C,008D,0091,0093,0094,0095,0096,0097,0098,0099,009A,009B,009C,009D,009E,009F,00C0,00C5,00C8,00E1,00E7,00F0,00F1,00F3,00F5,00F9,00FA,00FB,00FE,0100,0101,0102,0103,0104,0120,0121,0123,0125,0127,0128,0129,012A,0132,0133,0134,0137,0140,0141,0142,0143,01C2,0202,024A,025A,025B,025D,025F
      1 dmi:bvnSeaBIOS:bvr1.12.0-1:bd04/01/2014:svnQEMU:pnStandardPC(i440FX+PIIX,1996):pvrpc-i440fx-eoan:cvnQEMU:ct1:cvrpc-i440fx-eoan:
      1 hid:b0003g0001v00000627p00000001
      1 input:b0003v0627p0001e0001-e0,1,2,3,4,k110,111,112,r8,a0,1,m4,lsfw
      1 input:b0011v0001p0001eAB41-e0,1,4,11,14,k71,72,73,74,75,76,77,79,7A,7B,7C,7D,7E,7F,80,8C,8E,8F,9B,9C,9D,9E,9F,A3,A4,A5,A6,AC,AD,B7,B8,B9,D9,E2,ram4,l0,1,2,sfw
      1 input:b0011v0002p0006e0000-e0,1,2,k110,111,112,113,114,r0,1,6,8,amlsfw
      1 input:b0019v0000p0001e0000-e0,1,k74,ramlsfw
      1 pci:v00001AF4d00001000sv00001AF4sd00000001bc02sc00i00
      1 pci:v00001AF4d00001002sv00001AF4sd00000005bc00scFFi00
      1 pci:v00001AF4d00001003sv00001AF4sd00000003bc07sc80i00
      1 pci:v00001B36d00000100sv00001AF4sd00001100bc03sc00i00
      1 pci:v00008086d00001237sv00001AF4sd00001100bc06sc00i00
      1 pci:v00008086d00002668sv00001AF4sd00001100bc04sc03i00
      1 pci:v00008086d00002934sv00001AF4sd00001100bc0Csc03i00
      1 pci:v00008086d00002935sv00001AF4sd00001100bc0Csc03i00
      1 pci:v00008086d00002936sv00001AF4sd00001100bc0Csc03i00
      1 pci:v00008086d0000293Asv00001AF4sd00001100bc0Csc03i20
      1 pci:v00008086d00007000sv00001AF4sd00001100bc06sc01i00
      1 pci:v00008086d00007010sv00001AF4sd00001100bc01sc01i80
      1 pci:v00008086d00007113sv00001AF4sd00001100bc06sc80i00
      1 platform:Fixed MDIO bus
      1 platform:alarmtimer
      1 platform:i8042
      1 platform:pcspkr
      1 platform:platform-framebuffer
      1 platform:reg-dummy
      1 platform:serial8250
      1 scsi:t-0x00
      1 serio:ty01pr00id00ex00
      1 serio:ty06pr00id00ex00
      1 usb:v0627p0001d0000dc00dsc00dp00ic03isc00ip00in00
      3 usb:v1D6Bp0001d0415dc09dsc00dp00ic09isc00ip00in00
      1 usb:v1D6Bp0002d0415dc09dsc00dp00ic09isc00ip00in00
      1 virtio:d00000001v00001AF4
      1 virtio:d00000003v00001AF4
      1 virtio:d00000005v00001AF4
-----END MODALIASES-----
-----BEGIN SERIAL PORTS-----
/sys/devices/pnp0/00:04/tty/ttyS0
-----END SERIAL PORTS-----
-----BEGIN NETWORK INTERFACES-----
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000\    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: ens3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP mode DEFAULT group default qlen 1000\    link/ether 52:54:00:0b:6d:8c brd ff:ff:ff:ff:ff:ff
-----END NETWORK INTERFACES-----
-----BEGIN BLOCK DEVICE SUMMARY-----
NAME   MAJ:MIN FSTYPE PHY-SEC SIZE VENDOR   MODEL
sda      8:0              512   5G ATA      QEMU HARDDISK   
└─sda1   8:1   ext4       512   5G          
-----END BLOCK DEVICE SUMMARY-----
# dmidecode 3.1
Getting SMBIOS data from sysfs.
SMBIOS 2.8 present.
9 structures occupying 377 bytes.
Table at 0x000F58E0.
# Writing 377 bytes to /root/dmi.bin.
# Writing 31 bytes to /root/dmi.bin.
-----BEGIN DMI DATA-----
X1NNXycfAghSAAAAAAAAAF9ETUlfnXkBIAAAAAkAKAAAGAAAAQIA6AMACAAAAAAAAAAABAAA//9T
ZWFCSU9TADEuMTIuMC0xADA0LzAxLzIwMTQAAAEbAAEBAgMAk8WKR96p60KI/jQ+QB9PUAYAAFFF
TVUAU3RhbmRhcmQgUEMgKGk0NDBGWCArIFBJSVgsIDE5OTYpAHBjLWk0NDBmeC1lb2FuAAADFgAD
AQECAAADAwMCAAAAAAAAAAAAUUVNVQBwYy1pNDQwZngtZW9hbgAABCoABAEDAQLjBgUA//uLDwMA
AADQB9AHQQH///////8AAAABAQECAAEAQ1BVIDAAUUVNVQBwYy1pNDQwZngtZW9hbgAAEBcAEAED
BgAAEAD+/wEAAAAAAAAAAAAAABEoABEAEP7//////wAECQABAAcCAAAAAgAAAAAAAAAAAAAAAAAA
AABESU1NIDAAUUVNVQAAEx8AEwAAAAD//w8AABABAAAAAAAAAAAAAAAAAAAAAAAAIAsAIAAAAAAA
AAAAAH8EAH8AAA==
-----END DMI DATA-----
-----BEGIN DMI KEYPAIRS-----
bios-vendor=SeaBIOS
bios-version=1.12.0-1
bios-release-date=04/01/2014
system-manufacturer=QEMU
system-product-name=Standard PC (i440FX + PIIX, 1996)
system-version=pc-i440fx-eoan
system-serial-number=Not Specified
system-uuid=478AC593-A9DE-42EB-88FE-343E401F4F50
baseboard-manufacturer=
baseboard-product-name=
baseboard-version=
baseboard-serial-number=
baseboard-asset-tag=
chassis-manufacturer=QEMU
chassis-type=Other
chassis-version=pc-i440fx-eoan
chassis-serial-number=Not Specified
chassis-asset-tag=Not Specified
processor-family=Other
processor-manufacturer=QEMU
processor-version=pc-i440fx-eoan
processor-frequency=2000 MHz
-----END DMI KEYPAIRS-----
````
</details>

Here's a quick breakdown of what you see in the script output:

* **KERNEL INFO:** this is the output of `uname -a` -- the MAC address is the machine name in this case.

* **KERNEL COMMAND LINE:** these are the kernel command line parameters, directed at various modules built into the kernel.  The function `modprobe` parses this kernel command line and collects the relevant module parameters when it loads a module.  Note that this command line could also be used to pull in loadable modules.

* **CLOUD CONFIG QUERY:** a cloud-init query is used to retrieve cloud instance metadata used by cloud-init when booting an instance.  This section shows the specific metadata retrieved during cloud-init query for this machine.

* **CPU CORE COUNT AND MODEL:** the data produced here is similar to the output you could retrieve by running `nproc` and then attempting a `cat /sys/devices/cpu/caps/pmu_name` -- and so on.  There several ways to retrieve this info, but all can produce the number and type of CPU(s) available.

* **PCI INFO:** the devices, real or virtual, that are connected to the machine via PCI (Peripheral Component Interconnect) bus.

* **USB INFO:** the devices, real or virtual, that are connected to the machine via USB bus.

* **MODALIASES:** a modalias is a sysfs technique to capture the information that a hardware item exposes to the kernel, with the file basically providing a template or structure for this information.  Each of the entries in this list describe one particular part of the machine's (real or virtual) hardware, down to the level of alarm timers, framebuffers, and even speakers.  In the event of a bug, this information can help your support engineer (or yourself) understand exactly what hardware is configured for this machine.

* **SERIAL PORTS:** this section just lists the serial devices made available on this machine.

* **NETWORK INTERFACES:** summarises the network interfaces available on this machine -- essentially an abbreviated version of the output from some form of an `ip` command.

* **BLOCK DEVICE SUMMARY:** a thumbnail sketch of the block devices (usually storage) available on this machine.

* **#dmidecode...:** this section presents the basic DMI data, including the BIOS type, extent, size, and table location.

* **DMI DATA:** the raw (undecoded) DMI table for this machine, presented for verification of the following DMI data sections, if desired.

* **DMI KEYPAIRS:** the individual machine specifications, as decoded from the DMI table.  The manpage **dmidecode (8)** gives more details on each of these keypairs.

<!-- snap-2-8-ui snap-2-8-cli snap-2-7-ui snap-2-7-cli deb-2-8-ui deb-2-8-cli deb-2-7-ui deb-2-7-cli
<a href="#heading--00-maas-01-lshw"><h2 id="heading--00-maas-01-lshw">00-maas-01-lshw</h2></a>

This script pulls system BIOS and vendor info, and generates user-defined tags for later use.  Typical script output from a successful run looks something like the foldout below.
snap-2-8-ui snap-2-8-cli snap-2-7-ui snap-2-7-cli deb-2-8-ui deb-2-8-cli deb-2-7-ui deb-2-7-cli -->

<!-- snap-2-9-ui snap-2-9-cli deb-2-9-ui deb-2-9-cli snap-3-0-ui deb-3-0-ui snap-3-0-cli deb-3-0-cli 
<a href="#heading--maas-lshw"><h2 id="heading--maas-lshw">maas-lshw</h2></a>

This script pulls system BIOS and vendor info, and generates user-defined tags for later use.  `maas-lshw` runs in parallel with other scripts to speed up the commissioning process. Typical script output from a successful run looks something like the foldout below.
snap-2-9-ui snap-2-9-cli deb-2-9-ui deb-2-9-cli snap-3-0-ui deb-3-0-ui snap-3-0-cli deb-3-0-cli -->

<details><summary>Typical script output</summary>
````
<?xml version="1.0" standalone="yes" ?>
<!-- generated by lshw-B.02.18 -->
<!-- GCC 7.3.0 -->
<!-- Linux 4.15.0-91-generic #92-Ubuntu SMP Fri Feb 28 11:09:48 UTC 2020 x86_64 -->
<!-- GNU libc 2 (glibc 2.27) -->
<list>
<node id="52-54-00-0b-6d-8c" claimed="true" class="system" handle="DMI:0100">
 <description>Computer</description>
 <product>Standard PC (i440FX + PIIX, 1996)</product>
 <vendor>QEMU</vendor>
 <version>pc-i440fx-eoan</version>
 <width units="bits">64</width>
 <configuration>
  <setting id="boot" value="normal" />
  <setting id="uuid" value="93C58A47-DEA9-EB42-88FE-343E401F4F50" />
 </configuration>
 <capabilities>
  <capability id="smbios-2.8" >SMBIOS version 2.8</capability>
  <capability id="dmi-2.8" >DMI version 2.8</capability>
  <capability id="vsyscall32" >32-bit processes</capability>
 </capabilities>
  <node id="core" claimed="true" class="bus" handle="">
   <description>Motherboard</description>
   <physid>0</physid>
    <node id="firmware" claimed="true" class="memory" handle="">
     <description>BIOS</description>
     <vendor>SeaBIOS</vendor>
     <physid>0</physid>
     <version>1.12.0-1</version>
     <date>04/01/2014</date>
     <size units="bytes">98304</size>
    </node>
    <node id="cpu" claimed="true" class="processor" handle="DMI:0400">
     <description>CPU</description>
     <product>Intel Core Processor (Skylake, IBRS)</product>
     <vendor>Intel Corp.</vendor>
     <physid>400</physid>
     <businfo>cpu@0</businfo>
     <version>pc-i440fx-eoan</version>
     <slot>CPU 0</slot>
     <size units="Hz">2000000000</size>
     <capacity units="Hz">2000000000</capacity>
     <width units="bits">64</width>
     <configuration>
      <setting id="cores" value="1" />
      <setting id="enabledcores" value="1" />
      <setting id="threads" value="1" />
     </configuration>
     <capabilities>
      <capability id="fpu" >mathematical co-processor</capability>
      <capability id="fpu_exception" >FPU exceptions reporting</capability>
      <capability id="wp" />
      <capability id="vme" >virtual mode extensions</capability>
      <capability id="de" >debugging extensions</capability>
      <capability id="pse" >page size extensions</capability>
      <capability id="tsc" >time stamp counter</capability>
      <capability id="msr" >model-specific registers</capability>
      <capability id="pae" >4GB+ memory addressing (Physical Address Extension)</capability>
      <capability id="mce" >machine check exceptions</capability>
      <capability id="cx8" >compare and exchange 8-byte</capability>
      <capability id="apic" >on-chip advanced programmable interrupt controller (APIC)</capability>
      <capability id="sep" >fast system calls</capability>
      <capability id="mtrr" >memory type range registers</capability>
      <capability id="pge" >page global enable</capability>
      <capability id="mca" >machine check architecture</capability>
      <capability id="cmov" >conditional move instruction</capability>
      <capability id="pat" >page attribute table</capability>
      <capability id="pse36" >36-bit page size extensions</capability>
      <capability id="clflush" />
      <capability id="mmx" >multimedia extensions (MMX)</capability>
      <capability id="fxsr" >fast floating point save/restore</capability>
      <capability id="sse" >streaming SIMD extensions (SSE)</capability>
      <capability id="sse2" >streaming SIMD extensions (SSE2)</capability>
      <capability id="ss" >self-snoop</capability>
      <capability id="syscall" >fast system calls</capability>
      <capability id="nx" >no-execute bit (NX)</capability>
      <capability id="pdpe1gb" />
      <capability id="rdtscp" />
      <capability id="x86-64" >64bits extensions (x86-64)</capability>
      <capability id="constant_tsc" />
      <capability id="rep_good" />
      <capability id="nopl" />
      <capability id="xtopology" />
      <capability id="cpuid" />
      <capability id="tsc_known_freq" />
      <capability id="pni" />
      <capability id="pclmulqdq" />
      <capability id="vmx" />
      <capability id="ssse3" />
      <capability id="fma" />
      <capability id="cx16" />
      <capability id="pcid" />
      <capability id="sse4_1" />
      <capability id="sse4_2" />
      <capability id="x2apic" />
      <capability id="movbe" />
      <capability id="popcnt" />
      <capability id="tsc_deadline_timer" />
      <capability id="aes" />
      <capability id="xsave" />
      <capability id="avx" />
      <capability id="f16c" />
      <capability id="rdrand" />
      <capability id="hypervisor" />
      <capability id="lahf_lm" />
      <capability id="abm" />
      <capability id="3dnowprefetch" />
      <capability id="cpuid_fault" />
      <capability id="invpcid_single" />
      <capability id="ssbd" />
      <capability id="ibrs" />
      <capability id="ibpb" />
      <capability id="stibp" />
      <capability id="ibrs_enhanced" />
      <capability id="tpr_shadow" />
      <capability id="vnmi" />
      <capability id="flexpriority" />
      <capability id="ept" />
      <capability id="vpid" />
      <capability id="fsgsbase" />
      <capability id="tsc_adjust" />
      <capability id="bmi1" />
      <capability id="avx2" />
      <capability id="smep" />
      <capability id="bmi2" />
      <capability id="erms" />
      <capability id="invpcid" />
      <capability id="rdseed" />
      <capability id="adx" />
      <capability id="smap" />
      <capability id="clflushopt" />
      <capability id="xsaveopt" />
      <capability id="xsavec" />
      <capability id="xgetbv1" />
      <capability id="xsaves" />
      <capability id="arat" />
      <capability id="umip" />
      <capability id="md_clear" />
      <capability id="arch_capabilities" />
     </capabilities>
    </node>
    <node id="memory" claimed="true" class="memory" handle="DMI:1000">
     <description>System Memory</description>
     <physid>1000</physid>
     <size units="bytes">1073741824</size>
     <capacity units="bytes">1073741824</capacity>
     <configuration>
      <setting id="errordetection" value="multi-bit-ecc" />
     </configuration>
     <capabilities>
      <capability id="ecc" >Multi-bit error-correcting code (ECC)</capability>
     </capabilities>
      <node id="bank" claimed="true" class="memory" handle="DMI:1100">
       <description>DIMM RAM</description>
       <vendor>QEMU</vendor>
       <physid>0</physid>
       <slot>DIMM 0</slot>
       <size units="bytes">1073741824</size>
      </node>
    </node>
    <node id="pci" claimed="true" class="bridge" handle="PCIBUS:0000:00">
     <description>Host bridge</description>
     <product>440FX - 82441FX PMC [Natoma]</product>
     <vendor>Intel Corporation</vendor>
     <physid>100</physid>
     <businfo>pci@0000:00:00.0</businfo>
     <version>02</version>
     <width units="bits">32</width>
     <clock units="Hz">33000000</clock>
      <node id="isa" claimed="true" class="bridge" handle="PCI:0000:00:01.0">
       <description>ISA bridge</description>
       <product>82371SB PIIX3 ISA [Natoma/Triton II]</product>
       <vendor>Intel Corporation</vendor>
       <physid>1</physid>
       <businfo>pci@0000:00:01.0</businfo>
       <version>00</version>
       <width units="bits">32</width>
       <clock units="Hz">33000000</clock>
       <configuration>
        <setting id="latency" value="0" />
       </configuration>
       <capabilities>
        <capability id="isa" />
       </capabilities>
      </node>
      <node id="ide" claimed="true" class="storage" handle="PCI:0000:00:01.1">
       <description>IDE interface</description>
       <product>82371SB PIIX3 IDE [Natoma/Triton II]</product>
       <vendor>Intel Corporation</vendor>
       <physid>1.1</physid>
       <businfo>pci@0000:00:01.1</businfo>
       <version>00</version>
       <width units="bits">32</width>
       <clock units="Hz">33000000</clock>
       <configuration>
        <setting id="driver" value="ata_piix" />
        <setting id="latency" value="0" />
       </configuration>
       <capabilities>
        <capability id="ide" />
        <capability id="isa_compatibility_mode-only_controller__supports_bus_mastering" />
        <capability id="bus_master" >bus mastering</capability>
       </capabilities>
       <resources>
        <resource type="irq" value="0" />
        <resource type="ioport" value="1f0(size=8)" />
        <resource type="ioport" value="3f6" />
        <resource type="ioport" value="170(size=8)" />
        <resource type="ioport" value="376" />
        <resource type="ioport" value="c120(size=16)" />
       </resources>
      </node>
      <node id="bridge" claimed="true" class="bridge" handle="PCI:0000:00:01.3">
       <description>Bridge</description>
       <product>82371AB/EB/MB PIIX4 ACPI</product>
       <vendor>Intel Corporation</vendor>
       <physid>1.3</physid>
       <businfo>pci@0000:00:01.3</businfo>
       <version>03</version>
       <width units="bits">32</width>
       <clock units="Hz">33000000</clock>
       <configuration>
        <setting id="driver" value="piix4_smbus" />
        <setting id="latency" value="0" />
       </configuration>
       <capabilities>
        <capability id="bridge" />
       </capabilities>
       <resources>
        <resource type="irq" value="9" />
       </resources>
      </node>
      <node id="display" class="display" handle="PCI:0000:00:02.0">
       <description>VGA compatible controller</description>
       <product>QXL paravirtual graphic card</product>
       <vendor>Red Hat, Inc.</vendor>
       <physid>2</physid>
       <businfo>pci@0000:00:02.0</businfo>
       <version>04</version>
       <width units="bits">32</width>
       <clock units="Hz">33000000</clock>
       <configuration>
        <setting id="latency" value="0" />
       </configuration>
       <capabilities>
        <capability id="vga_controller" />
       </capabilities>
       <resources>
        <resource type="memory" value="f4000000-f7ffffff" />
        <resource type="memory" value="f8000000-fbffffff" />
        <resource type="memory" value="fc094000-fc095fff" />
        <resource type="ioport" value="c080(size=32)" />
        <resource type="memory" value="c0000-dffff" />
       </resources>
      </node>
      <node id="network" claimed="true" class="network" handle="PCI:0000:00:03.0">
       <description>Ethernet controller</description>
       <product>Virtio network device</product>
       <vendor>Red Hat, Inc.</vendor>
       <physid>3</physid>
       <businfo>pci@0000:00:03.0</businfo>
       <version>00</version>
       <width units="bits">64</width>
       <clock units="Hz">33000000</clock>
       <configuration>
        <setting id="driver" value="virtio-pci" />
        <setting id="latency" value="0" />
       </configuration>
       <capabilities>
        <capability id="msix" >MSI-X</capability>
        <capability id="bus_master" >bus mastering</capability>
        <capability id="cap_list" >PCI capabilities listing</capability>
        <capability id="rom" >extension ROM</capability>
       </capabilities>
       <resources>
        <resource type="irq" value="11" />
        <resource type="ioport" value="c0a0(size=32)" />
        <resource type="memory" value="fc096000-fc096fff" />
        <resource type="memory" value="febf4000-febf7fff" />
        <resource type="memory" value="fc000000-fc07ffff" />
       </resources>
        <node id="virtio0" claimed="true" class="network" handle="">
         <description>Ethernet interface</description>
         <physid>0</physid>
         <businfo>virtio@0</businfo>
         <logicalname>ens3</logicalname>
         <serial>52:54:00:0b:6d:8c</serial>
         <configuration>
          <setting id="autonegotiation" value="off" />
          <setting id="broadcast" value="yes" />
          <setting id="driver" value="virtio_net" />
          <setting id="driverversion" value="1.0.0" />
          <setting id="ip" value="192.168.122.213" />
          <setting id="link" value="yes" />
          <setting id="multicast" value="yes" />
         </configuration>
         <capabilities>
          <capability id="ethernet" />
          <capability id="physical" >Physical interface</capability>
         </capabilities>
        </node>
      </node>
      <node id="multimedia" class="multimedia" handle="PCI:0000:00:04.0">
       <description>Audio device</description>
       <product>82801FB/FBM/FR/FW/FRW (ICH6 Family) High Definition Audio Controller</product>
       <vendor>Intel Corporation</vendor>
       <physid>4</physid>
       <businfo>pci@0000:00:04.0</businfo>
       <version>01</version>
       <width units="bits">32</width>
       <clock units="Hz">33000000</clock>
       <configuration>
        <setting id="latency" value="0" />
       </configuration>
       <capabilities>
        <capability id="msi" >Message Signalled Interrupts</capability>
        <capability id="cap_list" >PCI capabilities listing</capability>
       </capabilities>
       <resources>
        <resource type="memory" value="fc090000-fc093fff" />
       </resources>
      </node>
      <node id="usb:0" claimed="true" class="bus" handle="PCI:0000:00:05.0">
       <description>USB controller</description>
       <product>82801I (ICH9 Family) USB UHCI Controller #1</product>
       <vendor>Intel Corporation</vendor>
       <physid>5</physid>
       <businfo>pci@0000:00:05.0</businfo>
       <version>03</version>
       <width units="bits">32</width>
       <clock units="Hz">33000000</clock>
       <configuration>
        <setting id="driver" value="uhci_hcd" />
        <setting id="latency" value="0" />
       </configuration>
       <capabilities>
        <capability id="uhci" >Universal Host Controller Interface (USB1)</capability>
        <capability id="bus_master" >bus mastering</capability>
       </capabilities>
       <resources>
        <resource type="irq" value="10" />
        <resource type="ioport" value="c0c0(size=32)" />
       </resources>
        <node id="usbhost" claimed="true" class="bus" handle="USB:2:1">
         <product>UHCI Host Controller</product>
         <vendor>Linux 4.15.0-91-generic uhci_hcd</vendor>
         <physid>1</physid>
         <businfo>usb@2</businfo>
         <logicalname>usb2</logicalname>
         <version>4.15</version>
         <configuration>
          <setting id="driver" value="hub" />
          <setting id="slots" value="2" />
          <setting id="speed" value="12Mbit/s" />
         </configuration>
         <capabilities>
          <capability id="usb-1.10" >USB 1.1</capability>
         </capabilities>
        </node>
      </node>
      <node id="usb:1" claimed="true" class="bus" handle="PCI:0000:00:05.1">
       <description>USB controller</description>
       <product>82801I (ICH9 Family) USB UHCI Controller #2</product>
       <vendor>Intel Corporation</vendor>
       <physid>5.1</physid>
       <businfo>pci@0000:00:05.1</businfo>
       <version>03</version>
       <width units="bits">32</width>
       <clock units="Hz">33000000</clock>
       <configuration>
        <setting id="driver" value="uhci_hcd" />
        <setting id="latency" value="0" />
       </configuration>
       <capabilities>
        <capability id="uhci" >Universal Host Controller Interface (USB1)</capability>
        <capability id="bus_master" >bus mastering</capability>
       </capabilities>
       <resources>
        <resource type="irq" value="11" />
        <resource type="ioport" value="c0e0(size=32)" />
       </resources>
        <node id="usbhost" claimed="true" class="bus" handle="USB:3:1">
         <product>UHCI Host Controller</product>
         <vendor>Linux 4.15.0-91-generic uhci_hcd</vendor>
         <physid>1</physid>
         <businfo>usb@3</businfo>
         <logicalname>usb3</logicalname>
         <version>4.15</version>
         <configuration>
          <setting id="driver" value="hub" />
          <setting id="slots" value="2" />
          <setting id="speed" value="12Mbit/s" />
         </configuration>
         <capabilities>
          <capability id="usb-1.10" >USB 1.1</capability>
         </capabilities>
        </node>
      </node>
      <node id="usb:2" claimed="true" class="bus" handle="PCI:0000:00:05.2">
       <description>USB controller</description>
       <product>82801I (ICH9 Family) USB UHCI Controller #3</product>
       <vendor>Intel Corporation</vendor>
       <physid>5.2</physid>
       <businfo>pci@0000:00:05.2</businfo>
       <version>03</version>
       <width units="bits">32</width>
       <clock units="Hz">33000000</clock>
       <configuration>
        <setting id="driver" value="uhci_hcd" />
        <setting id="latency" value="0" />
       </configuration>
       <capabilities>
        <capability id="uhci" >Universal Host Controller Interface (USB1)</capability>
        <capability id="bus_master" >bus mastering</capability>
       </capabilities>
       <resources>
        <resource type="irq" value="11" />
        <resource type="ioport" value="c100(size=32)" />
       </resources>
        <node id="usbhost" claimed="true" class="bus" handle="USB:4:1">
         <product>UHCI Host Controller</product>
         <vendor>Linux 4.15.0-91-generic uhci_hcd</vendor>
         <physid>1</physid>
         <businfo>usb@4</businfo>
         <logicalname>usb4</logicalname>
         <version>4.15</version>
         <configuration>
          <setting id="driver" value="hub" />
          <setting id="slots" value="2" />
          <setting id="speed" value="12Mbit/s" />
         </configuration>
         <capabilities>
          <capability id="usb-1.10" >USB 1.1</capability>
         </capabilities>
        </node>
      </node>
      <node id="usb:3" claimed="true" class="bus" handle="PCI:0000:00:05.7">
       <description>USB controller</description>
       <product>82801I (ICH9 Family) USB2 EHCI Controller #1</product>
       <vendor>Intel Corporation</vendor>
       <physid>5.7</physid>
       <businfo>pci@0000:00:05.7</businfo>
       <version>03</version>
       <width units="bits">32</width>
       <clock units="Hz">33000000</clock>
       <configuration>
        <setting id="driver" value="ehci-pci" />
        <setting id="latency" value="0" />
       </configuration>
       <capabilities>
        <capability id="ehci" >Enhanced Host Controller Interface (USB2)</capability>
        <capability id="bus_master" >bus mastering</capability>
       </capabilities>
       <resources>
        <resource type="irq" value="10" />
        <resource type="memory" value="fc097000-fc097fff" />
       </resources>
        <node id="usbhost" claimed="true" class="bus" handle="USB:1:1">
         <product>EHCI Host Controller</product>
         <vendor>Linux 4.15.0-91-generic ehci_hcd</vendor>
         <physid>1</physid>
         <businfo>usb@1</businfo>
         <logicalname>usb1</logicalname>
         <version>4.15</version>
         <configuration>
          <setting id="driver" value="hub" />
          <setting id="slots" value="6" />
          <setting id="speed" value="480Mbit/s" />
         </configuration>
         <capabilities>
          <capability id="usb-2.00" >USB 2.0</capability>
         </capabilities>
          <node id="usb" claimed="true" class="input" handle="USB:1:2">
           <description>Human interface device</description>
           <product>QEMU USB Tablet</product>
           <vendor>QEMU</vendor>
           <physid>1</physid>
           <businfo>usb@1:1</businfo>
           <version>0.00</version>
           <serial>28754-0000:00:05.7-1</serial>
           <configuration>
            <setting id="driver" value="usbhid" />
            <setting id="maxpower" value="100mA" />
            <setting id="speed" value="480Mbit/s" />
           </configuration>
           <capabilities>
            <capability id="usb-2.00" >USB 2.0</capability>
           </capabilities>
          </node>
        </node>
      </node>
      <node id="communication" claimed="true" class="communication" handle="PCI:0000:00:06.0">
       <description>Communication controller</description>
       <product>Virtio console</product>
       <vendor>Red Hat, Inc.</vendor>
       <physid>6</physid>
       <businfo>pci@0000:00:06.0</businfo>
       <version>00</version>
       <width units="bits">64</width>
       <clock units="Hz">33000000</clock>
       <configuration>
        <setting id="driver" value="virtio-pci" />
        <setting id="latency" value="0" />
       </configuration>
       <capabilities>
        <capability id="msix" >MSI-X</capability>
        <capability id="bus_master" >bus mastering</capability>
        <capability id="cap_list" >PCI capabilities listing</capability>
       </capabilities>
       <resources>
        <resource type="irq" value="11" />
        <resource type="ioport" value="c000(size=64)" />
        <resource type="memory" value="fc098000-fc098fff" />
        <resource type="memory" value="febf8000-febfbfff" />
       </resources>
        <node id="virtio1" class="generic" handle="">
         <description>Virtual I/O device</description>
         <physid>0</physid>
         <businfo>virtio@1</businfo>
         <configuration>
          <setting id="driver" value="virtio_console" />
         </configuration>
        </node>
      </node>
      <node id="generic" claimed="true" class="generic" handle="PCI:0000:00:07.0">
       <description>Unclassified device</description>
       <product>Virtio memory balloon</product>
       <vendor>Red Hat, Inc.</vendor>
       <physid>7</physid>
       <businfo>pci@0000:00:07.0</businfo>
       <version>00</version>
       <width units="bits">64</width>
       <clock units="Hz">33000000</clock>
       <configuration>
        <setting id="driver" value="virtio-pci" />
        <setting id="latency" value="0" />
       </configuration>
       <capabilities>
        <capability id="bus_master" >bus mastering</capability>
        <capability id="cap_list" >PCI capabilities listing</capability>
       </capabilities>
       <resources>
        <resource type="irq" value="11" />
        <resource type="ioport" value="c040(size=64)" />
        <resource type="memory" value="febfc000-febfffff" />
       </resources>
        <node id="virtio2" class="generic" handle="">
         <description>Virtual I/O device</description>
         <physid>0</physid>
         <businfo>virtio@2</businfo>
         <configuration>
          <setting id="driver" value="virtio_balloon" />
         </configuration>
        </node>
      </node>
    </node>
    <node id="scsi" claimed="true" class="storage" handle="">
     <physid>1</physid>
     <logicalname>scsi0</logicalname>
     <capabilities>
      <capability id="emulated" >Emulated device</capability>
     </capabilities>
      <node id="disk" claimed="true" class="disk" handle="SCSI:00:00:00:00">
       <description>ATA Disk</description>
       <product>QEMU HARDDISK</product>
       <physid>0.0.0</physid>
       <businfo>scsi@0:0.0.0</businfo>
       <logicalname>/dev/sda</logicalname>
       <dev>8:0</dev>
       <version>2.5+</version>
       <serial>QM00001</serial>
       <size units="bytes">5368709120</size>
       <configuration>
        <setting id="ansiversion" value="5" />
        <setting id="logicalsectorsize" value="512" />
        <setting id="sectorsize" value="512" />
        <setting id="signature" value="7e8fce00" />
       </configuration>
       <capabilities>
        <capability id="partitioned" >Partitioned disk</capability>
        <capability id="partitioned:dos" >MS-DOS partition table</capability>
       </capabilities>
        <node id="volume" claimed="true" class="volume" handle="">
         <description>EXT4 volume</description>
         <vendor>Linux</vendor>
         <physid>1</physid>
         <businfo>scsi@0:0.0.0,1</businfo>
         <logicalname>/dev/sda1</logicalname>
         <dev>8:1</dev>
         <version>1.0</version>
         <serial>b2eb4dd4-9fd3-44a3-a47a-47933d4bf29c</serial>
         <size units="bytes">5367640064</size>
         <capacity>5367643648</capacity>
         <configuration>
          <setting id="created" value="2020-03-23 20:55:53" />
          <setting id="filesystem" value="ext4" />
          <setting id="label" value="root" />
          <setting id="lastmountpoint" value="/" />
          <setting id="modified" value="2020-03-23 20:58:40" />
          <setting id="mounted" value="2020-03-23 21:00:37" />
          <setting id="state" value="clean" />
         </configuration>
         <capabilities>
          <capability id="primary" >Primary partition</capability>
          <capability id="journaled" />
          <capability id="extended_attributes" >Extended Attributes</capability>
          <capability id="large_files" >4GB+ files</capability>
          <capability id="huge_files" >16TB+ files</capability>
          <capability id="dir_nlink" >directories with 65000+ subdirs</capability>
          <capability id="recover" >needs recovery</capability>
          <capability id="64bit" >64bit filesystem</capability>
          <capability id="extents" >extent-based allocation</capability>
          <capability id="ext4" />
          <capability id="ext2" >EXT2/EXT3</capability>
          <capability id="initialized" >initialized volume</capability>
         </capabilities>
        </node>
      </node>
    </node>
  </node>
</node>
</list>
````
</details>

This output is roughly equivalent to the output of `lshw -xml` on the machine in question.  There are many references to decode this information, so for now, here is a short glossary of most the terms (essentially, the tags) that typically appear in a listing like this:

* **businfo** - the bus information for this device.

* **capacity** - the maximum capacity reported by the device.

* **class** - the device's class.

* **clock** - the bus clock of the device (in Hz).

* **description** - a human-readable description of the hardware node.

* **dev** - the device number (major.minor).

* **id** - the internal identifier used by `lshw`.

* **logicalname** - the logical node name used by the system.

* **physid** - the physical id of the device.

* **product** - the specific product name of the device.

* **serial** - the serial number of the device.

* **size** - the actual size of the device.

* **slot** - location of the physical (or virtual) connection.

* **vendor** - the name of the vendor or manufacturer of the device.

* **version** - the version or release information associated with the device.

* **width** - the address width of the device (32/64 bits).

Some additional fields may be present in this output.  These will be identified and described as necessary for specific instances and situations.

<!-- snap-2-7-ui snap-2-7-cli deb-2-7-ui deb-2-7-cli
<a href="#heading--00-maas-02-virtuality-2-7"><h2 id="heading--00-maas-02-virtuality-2-7">00-maas-02-virtuality</h2></a>

This script checks whether the machine being commissioned is a virtual machine, which may affect how MAAS interacts with it.  The typical output of a successful run does not normally contain a lot of information, as shown below:

````
kvm
````

This script will be phased on in the next release of MAAS, with the functionality being incorporated into `50-maas-01-commissioning`.
snap-2-7-ui snap-2-7-cli deb-2-7-ui deb-2-7-cli -->

<!-- snap-2-8-ui snap-2-8-cli deb-2-8-ui deb-2-8-cli
<a href="#heading--00-maas-02-virtuality-2-8"><h2 id="heading--00-maas-02-virtuality-2-8">00-maas-02-virtuality-2-8</h2></a>

This script, phased out as part of the 2.8 release, checked whether the machine being commissioned was a virtual machine. From MAAS 2.8 going forward, this functionality resides in the script `50-maas-01-commissioning`.  
snap-2-8-ui snap-2-8-cli deb-2-8-ui deb-2-8-cli -->

<!-- snap-2-8-ui snap-2-8-cli snap-2-7-ui snap-2-7-cli deb-2-8-ui deb-2-8-cli deb-2-7-ui deb-2-7-cli

<a href="#heading--00-maas-03-install-lldpd"><h2 id="heading--00-maas-03-install-lldpd">00-maas-03-install-lldpd</h2></a>

This script installs the link layer discovery protocol (LLDP) daemon, which will later capture networking information about the machine. The lldpd needs to be installed early because it requires about a 60-second delay before running.  Under normal conditions, there is typically no output from this script in the logs.
snap-2-8-ui snap-2-8-cli snap-2-7-ui snap-2-7-cli deb-2-8-ui deb-2-8-cli deb-2-7-ui deb-2-7-cli -->

<!-- snap-2-9-ui snap-2-9-cli deb-2-9-ui deb-2-9-cli snap-3-0-cli deb-3-0-cli snap-3-0-ui deb-3-0-ui 

<a href="#heading--20-maas-01-install-lldpd"><h2 id="heading--20-maas-01-install-lldpd">20-maas-01-install-lldpd</h2></a>

This script installs the link layer discovery protocol (LLDP) daemon, which will later capture networking information about the machine.  This logs the basic install process to the commissioning logs in real time.
snap-2-9-ui snap-2-9-cli deb-2-9-ui deb-2-9-cli snap-3-0-ui deb-3-0-ui snap-3-0-cli deb-3-0-cli -->

<!-- snap-2-8-ui snap-2-8-cli snap-2-7-ui snap-2-7-cli deb-2-8-ui deb-2-8-cli deb-2-7-ui deb-2-7-cli

<a href="#heading--00-maas-04-list-modaliases"><h2 id="heading--00-maas-04-list-modaliases">00-maas-04-list-modaliases</h2></a>

This script figures out what hardware modules are loaded, providing a way to autorun certain scripts based on which modules are loaded.  Successful log output looks something like the foldout below.
snap-2-8-ui snap-2-8-cli snap-2-7-ui snap-2-7-cli deb-2-8-ui deb-2-8-cli deb-2-7-ui deb-2-7-cli -->

<!-- snap-2-9-ui snap-2-9-cli deb-2-9-ui deb-2-9-cli snap-3-0-cli deb-3-0-cli snap-3-0-ui deb-3-0-ui  

<a href="#heading--maas-list-modaliases"><h2 id="heading--maas-list-modaliases">maas-list-modaliases</h2></a>

This script figures out what hardware modules are loaded, providing a way to autorun certain scripts based on which modules are loaded.  `maas-list-modaliases` runs in parallel with other scripts to speed up the commissioning process.  Successful log output looks something like the foldout below.
snap-2-9-ui snap-2-9-cli deb-2-9-ui deb-2-9-cli snap-3-0-ui deb-3-0-ui snap-3-0-cli deb-3-0-cli -->

<details><summary>Typical script output</summary>

````
acpi:ACPI0010:PNP0A05:
acpi:LNXCPU:
acpi:LNXPWRBN:
acpi:LNXSYBUS:
acpi:LNXSYSTM:
acpi:PNP0303:
acpi:PNP0501:
acpi:PNP0700:
acpi:PNP0A03:
acpi:PNP0A06:
acpi:PNP0B00:
acpi:PNP0C0F:
acpi:PNP0F13:
acpi:QEMU0002:
cpu:type:x86,ven0000fam0006mod005E:feature:,0000,0001,0002,0003,0004,0005,0006,0007,0008,0009,000B,000C,000D,000E,000F,0010,0011,0013,0017,0018,0019,001A,001B,002B,0034,003A,003B,003D,0068,006F,0070,0072,0074,0075,0076,0079,007F,0080,0081,0085,0089,008C,008D,0091,0093,0094,0095,0096,0097,0098,0099,009A,009B,009C,009D,009E,009F,00C0,00C5,00C8,00E1,00E7,00F0,00F1,00F3,00F5,00F9,00FA,00FB,00FE,0100,0101,0102,0103,0104,0120,0121,0123,0125,0127,0128,0129,012A,0132,0133,0134,0137,0140,0141,0142,0143,01C2,0202,024A,025A,025B,025D,025F
dmi:bvnSeaBIOS:bvr1.12.0-1:bd04/01/2014:svnQEMU:pnStandardPC(i440FX+PIIX,1996):pvrpc-i440fx-eoan:cvnQEMU:ct1:cvrpc-i440fx-eoan:
hid:b0003g0001v00000627p00000001
input:b0003v0627p0001e0001-e0,1,2,3,4,k110,111,112,r8,a0,1,m4,lsfw
input:b0011v0001p0001eAB41-e0,1,4,11,14,k71,72,73,74,75,76,77,79,7A,7B,7C,7D,7E,7F,80,8C,8E,8F,9B,9C,9D,9E,9F,A3,A4,A5,A6,AC,AD,B7,B8,B9,D9,E2,ram4,l0,1,2,sfw
input:b0011v0002p0006e0000-e0,1,2,k110,111,112,113,114,r0,1,6,8,amlsfw
input:b0019v0000p0001e0000-e0,1,k74,ramlsfw
pci:v00001AF4d00001000sv00001AF4sd00000001bc02sc00i00
pci:v00001AF4d00001002sv00001AF4sd00000005bc00scFFi00
pci:v00001AF4d00001003sv00001AF4sd00000003bc07sc80i00
pci:v00001B36d00000100sv00001AF4sd00001100bc03sc00i00
pci:v00008086d00001237sv00001AF4sd00001100bc06sc00i00
pci:v00008086d00002668sv00001AF4sd00001100bc04sc03i00
pci:v00008086d00002934sv00001AF4sd00001100bc0Csc03i00
pci:v00008086d00002935sv00001AF4sd00001100bc0Csc03i00
pci:v00008086d00002936sv00001AF4sd00001100bc0Csc03i00
pci:v00008086d0000293Asv00001AF4sd00001100bc0Csc03i20
pci:v00008086d00007000sv00001AF4sd00001100bc06sc01i00
pci:v00008086d00007010sv00001AF4sd00001100bc01sc01i80
pci:v00008086d00007113sv00001AF4sd00001100bc06sc80i00
platform:Fixed MDIO bus
platform:alarmtimer
platform:i8042
platform:pcspkr
platform:platform-framebuffer
platform:reg-dummy
platform:serial8250
scsi:t-0x00
serio:ty01pr00id00ex00
serio:ty06pr00id00ex00
usb:v0627p0001d0000dc00dsc00dp00ic03isc00ip00in00
usb:v1D6Bp0001d0415dc09dsc00dp00ic09isc00ip00in00
usb:v1D6Bp0002d0415dc09dsc00dp00ic09isc00ip00in00
virtio:d00000001v00001AF4
virtio:d00000003v00001AF4
virtio:d00000005v00001AF4
````
</details>

The output is similar to the modaliases output shown in the `00-maas-00-support-info` output.  Here, we can decode some of the fields for a PCI entry, for example, set off my one or more consecutive letters:

* **v** marks a vendor code.

* **d** indicates a device code.

* **sv** precedes a subvendor code.

* **sd** sets off a subdevice code.

* **bc** indicates a bus class code.

* **sc** denotes a bus subclass code.

* **i** is followed by an interface code.

There are many more fields, depending upon the device type, and a wide variety of codes for every field for every device.  Every bus has its own schema for modalias -- hence, cataloguing these combinations is beyond the scope of this document set.  Understanding the way these codes are constructed, though, may help you know how to find needed information for a specific situation.

<!-- snap-2-8-ui snap-2-8-cli snap-2-7-ui snap-2-7-cli deb-2-8-ui deb-2-8-cli deb-2-7-ui deb-2-7-cli

<a href="#heading--00-maas-05-dhcp-unconfigured-ifaces"><h2 id="heading--00-maas-05-dhcp-unconfigured-ifaces">00-maas-05-dhcp-unconfigured-ifaces</h2></a>

MAAS will want to know all the ways the machine is connected to the network. Only PXE comes online during boot; this script brings all the other networks online so they can be recognised.  Under normal conditions, this script does not produce a significant amount of output.
snap-2-8-ui snap-2-8-cli snap-2-7-ui snap-2-7-cli deb-2-8-ui deb-2-8-cli deb-2-7-ui deb-2-7-cli -->

<!-- snap-2-9-ui snap-2-9-cli deb-2-9-ui deb-2-9-cli snap-3-0-cli deb-3-0-cli snap-3-0-ui deb-3-0-ui 
<a href="#heading--20-maas-02-dhcp-unconfigured-ifaces"><h2 id="heading--20-maas-02-dhcp-unconfigured-ifaces">20-maas-02-dhcp-unconfigured-ifaces</h2></a>

MAAS will want to know all the ways the machine is connected to the network. Only PXE comes online during boot; this script brings all the other networks online so they can be recognised.  This script logs the discovery of these networks to the commissioning logs.
snap-2-9-ui snap-2-9-cli deb-2-9-ui deb-2-9-cli snap-3-0-ui deb-3-0-ui snap-3-0-cli deb-3-0-cli -->

<!-- snap-2-8-ui snap-2-8-cli snap-2-7-ui snap-2-7-cli deb-2-8-ui deb-2-8-cli deb-2-7-ui deb-2-7-cli
<a href="#heading--00-maas-06-get-fruid-api-data"><h2 id="heading--00-maas-06-get-fruid-api-data">00-maas-06-get-fruid-api-data</h2></a>

This script gathers information for the Facebook wedge power type.  Typical output from a successful run looks something like the foldout below.
snap-2-8-ui snap-2-8-cli snap-2-7-ui snap-2-7-cli deb-2-8-ui deb-2-8-cli deb-2-7-ui deb-2-7-cli -->

<!-- snap-2-9-ui snap-2-9-cli deb-2-9-ui deb-2-9-cli snap-3-0-cli deb-3-0-cli snap-3-0-ui deb-3-0-ui 

<a href="#heading--maas-get-fruid-api-data"><h2 id="heading--maas-get-fruid-api-data">maas-get-fruid-api-data</h2></a>

This script gathers information for the Facebook wedge power type, and it runs in parallel with other scripts to improve commissioning speed. Typical output from a successful run looks something like the foldout below.
snap-2-9-ui snap-2-9-cli deb-2-9-ui deb-2-9-cli snap-3-0-ui deb-3-0-ui snap-3-0-cli deb-3-0-cli -->

<details><summary>Typical script output</summary>

````
+ sleep 5
++ ls /sys/class/net
+ for ifname in $(ls /sys/class/net)
+ '[' ens3 '!=' lo ']'
+ curl --max-time 1 -s -f http://fe80::1%ens3:8080/api/sys/mb/fruid
+ for ifname in $(ls /sys/class/net)
+ '[' lo '!=' lo ']'
+ exit 0
````
</details>

You will note that this output does not actually contain any specific information, but rather the echoed commands of a script to gather the information.

<!-- snap-2-8-ui snap-2-8-cli snap-2-7-ui snap-2-7-cli deb-2-8-ui deb-2-8-cli deb-2-7-ui deb-2-7-cli

<a href="#heading--00-maas-08-serial-ports"><h2 id="heading--00-maas-08-serial-ports">00-maas-08-serial-ports</h2></a>

This script lists what serial ports are available on the machine.  Log output from a normal, successful run is simply a list of serial ports, something like the foldout below.
snap-2-8-ui snap-2-8-cli snap-2-7-ui snap-2-7-cli deb-2-8-ui deb-2-8-cli deb-2-7-ui deb-2-7-cli -->

<!-- snap-2-9-ui snap-2-9-cli deb-2-9-ui deb-2-9-cli snap-3-0-cli deb-3-0-cli snap-3-0-ui deb-3-0-ui 
<a href="#heading--maas-serial-ports"><h2 id="heading--maas-serial-ports">maas-serial-ports</h2></a>

This script lists what serial ports are available on the machine; it runs in parallel to speed up commissioning.  Log output from a normal, successful run is simply a list of serial ports, something like the foldout below.
snap-2-9-ui snap-2-9-cli deb-2-9-ui deb-2-9-cli snap-3-0-ui deb-3-0-ui snap-3-0-cli deb-3-0-cli -->

<details><summary>Typical script output</summary>
````
/sys/devices/platform/serial8250/tty/ttyS1
/sys/devices/platform/serial8250/tty/ttyS10
/sys/devices/platform/serial8250/tty/ttyS11
/sys/devices/platform/serial8250/tty/ttyS12
/sys/devices/platform/serial8250/tty/ttyS13
/sys/devices/platform/serial8250/tty/ttyS14
/sys/devices/platform/serial8250/tty/ttyS15
/sys/devices/platform/serial8250/tty/ttyS16
/sys/devices/platform/serial8250/tty/ttyS17
/sys/devices/platform/serial8250/tty/ttyS18
/sys/devices/platform/serial8250/tty/ttyS19
/sys/devices/platform/serial8250/tty/ttyS2
/sys/devices/platform/serial8250/tty/ttyS20
/sys/devices/platform/serial8250/tty/ttyS21
/sys/devices/platform/serial8250/tty/ttyS22
/sys/devices/platform/serial8250/tty/ttyS23
/sys/devices/platform/serial8250/tty/ttyS24
/sys/devices/platform/serial8250/tty/ttyS25
/sys/devices/platform/serial8250/tty/ttyS26
/sys/devices/platform/serial8250/tty/ttyS27
/sys/devices/platform/serial8250/tty/ttyS28
/sys/devices/platform/serial8250/tty/ttyS29
/sys/devices/platform/serial8250/tty/ttyS3
/sys/devices/platform/serial8250/tty/ttyS30
/sys/devices/platform/serial8250/tty/ttyS31
/sys/devices/platform/serial8250/tty/ttyS4
/sys/devices/platform/serial8250/tty/ttyS5
/sys/devices/platform/serial8250/tty/ttyS6
/sys/devices/platform/serial8250/tty/ttyS7
/sys/devices/platform/serial8250/tty/ttyS8
/sys/devices/platform/serial8250/tty/ttyS9
/sys/devices/pnp0/00:04/tty/ttyS0
/sys/devices/virtual/tty/console
/sys/devices/virtual/tty/ptmx
/sys/devices/virtual/tty/tty
/sys/devices/virtual/tty/tty0
/sys/devices/virtual/tty/tty1
/sys/devices/virtual/tty/tty10
/sys/devices/virtual/tty/tty11
/sys/devices/virtual/tty/tty12
/sys/devices/virtual/tty/tty13
/sys/devices/virtual/tty/tty14
/sys/devices/virtual/tty/tty15
/sys/devices/virtual/tty/tty16
/sys/devices/virtual/tty/tty17
/sys/devices/virtual/tty/tty18
/sys/devices/virtual/tty/tty19
/sys/devices/virtual/tty/tty2
/sys/devices/virtual/tty/tty20
/sys/devices/virtual/tty/tty21
/sys/devices/virtual/tty/tty22
/sys/devices/virtual/tty/tty23
/sys/devices/virtual/tty/tty24
/sys/devices/virtual/tty/tty25
/sys/devices/virtual/tty/tty26
/sys/devices/virtual/tty/tty27
/sys/devices/virtual/tty/tty28
/sys/devices/virtual/tty/tty29
/sys/devices/virtual/tty/tty3
/sys/devices/virtual/tty/tty30
/sys/devices/virtual/tty/tty31
/sys/devices/virtual/tty/tty32
/sys/devices/virtual/tty/tty33
/sys/devices/virtual/tty/tty34
/sys/devices/virtual/tty/tty35
/sys/devices/virtual/tty/tty36
/sys/devices/virtual/tty/tty37
/sys/devices/virtual/tty/tty38
/sys/devices/virtual/tty/tty39
/sys/devices/virtual/tty/tty4
/sys/devices/virtual/tty/tty40
/sys/devices/virtual/tty/tty41
/sys/devices/virtual/tty/tty42
/sys/devices/virtual/tty/tty43
/sys/devices/virtual/tty/tty44
/sys/devices/virtual/tty/tty45
/sys/devices/virtual/tty/tty46
/sys/devices/virtual/tty/tty47
/sys/devices/virtual/tty/tty48
/sys/devices/virtual/tty/tty49
/sys/devices/virtual/tty/tty5
/sys/devices/virtual/tty/tty50
/sys/devices/virtual/tty/tty51
/sys/devices/virtual/tty/tty52
/sys/devices/virtual/tty/tty53
/sys/devices/virtual/tty/tty54
/sys/devices/virtual/tty/tty55
/sys/devices/virtual/tty/tty56
/sys/devices/virtual/tty/tty57
/sys/devices/virtual/tty/tty58
/sys/devices/virtual/tty/tty59
/sys/devices/virtual/tty/tty6
/sys/devices/virtual/tty/tty60
/sys/devices/virtual/tty/tty61
/sys/devices/virtual/tty/tty62
/sys/devices/virtual/tty/tty63
/sys/devices/virtual/tty/tty7
/sys/devices/virtual/tty/tty8
/sys/devices/virtual/tty/tty9
/sys/devices/virtual/tty/ttyprintk
````
</details>

The output of this script may be useful when you're trying to verify that a particular serial interface is active and available on your machine.

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui
<a href="#heading--40-maas-01-network-interfaces"><h2 id="heading--40-maas-01-network-interfaces">40-maas-01-network-interfaces</h2></a>

This script is just used to get the IP address, which can then be associated with a VLAN/subnet.  As you can see from the sample (successful) output below, the results are simply the output of a command similar to `ip a`.

````
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: ens3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 52:54:00:0b:6d:8c brd ff:ff:ff:ff:ff:ff
    inet 192.168.122.213/24 brd 192.168.122.255 scope global ens3
       valid_lft forever preferred_lft forever
    inet6 fe80::5054:ff:fe0b:6d8c/64 scope link 
       valid_lft forever preferred_lft forever
````
snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui -->

<a href="#heading--50-maas-01-commissioning"><h2 id="heading--50-maas-01-commissioning">50-maas-01-commissioning</h2></a>

This script is the main MAAS tool, gathering information on machine resources, such as storage, network devices, CPU, RAM, etc. We currently pull this data using lxd: We use a Go binary built from lxd source that just contains the minimum source to gather the resource information we need.

Output from a successful run is fairly robust, and looks something like the foldout below:

<details><summary>Typical script output</summary>

````
--2020-03-23 22:02:15--  http://192.168.122.2:5248/machine-resources/amd64
Connecting to 192.168.122.2:5248... connected.
HTTP request sent, awaiting response... 200 OK
Length: 4373408 (4.2M) [application/octet-stream]
Saving to: ‘/tmp/user_data.sh.EK9wIv/scripts/downloads/50-maas-01-commissioning/amd64’
     0K .......... .......... .......... .......... ..........  1% 12.7M 0s
    50K .......... .......... .......... .......... ..........  2% 19.0M 0s
   100K .......... .......... .......... .......... ..........  3% 19.5M 0s
   150K .......... .......... .......... .......... ..........  4% 20.5M 0s
   200K .......... .......... .......... .......... ..........  5% 15.0M 0s
   250K .......... .......... .......... .......... ..........  7% 11.4M 0s
   300K .......... .......... .......... .......... ..........  8% 19.1M 0s
   350K .......... .......... .......... .......... ..........  9% 19.9M 0s
   400K .......... .......... .......... .......... .......... 10% 17.5M 0s
   450K .......... .......... .......... .......... .......... 11% 19.2M 0s
   500K .......... .......... .......... .......... .......... 12% 17.0M 0s
   550K .......... .......... .......... .......... .......... 14% 19.2M 0s
   600K .......... .......... .......... .......... .......... 15% 11.7M 0s
   650K .......... .......... .......... .......... .......... 16% 19.4M 0s
   700K .......... .......... .......... .......... .......... 17% 20.2M 0s
   750K .......... .......... .......... .......... .......... 18% 20.4M 0s
   800K .......... .......... .......... .......... .......... 19% 10.7M 0s
   850K .......... .......... .......... .......... .......... 21% 17.8M 0s
   900K .......... .......... .......... .......... .......... 22% 19.2M 0s
   950K .......... .......... .......... .......... .......... 23% 20.0M 0s
  1000K .......... .......... .......... .......... .......... 24% 17.2M 0s
  1050K .......... .......... .......... .......... .......... 25% 15.9M 0s
  1100K .......... .......... .......... .......... .......... 26% 16.4M 0s
  1150K .......... .......... .......... .......... .......... 28% 12.4M 0s
  1200K .......... .......... .......... .......... .......... 29% 17.1M 0s
  1250K .......... .......... .......... .......... .......... 30% 20.6M 0s
  1300K .......... .......... .......... .......... .......... 31% 19.9M 0s
  1350K .......... .......... .......... .......... .......... 32% 14.9M 0s
  1400K .......... .......... .......... .......... .......... 33% 16.2M 0s
  1450K .......... .......... .......... .......... .......... 35% 20.4M 0s
  1500K .......... .......... .......... .......... .......... 36% 20.0M 0s
  1550K .......... .......... .......... .......... .......... 37% 19.6M 0s
  1600K .......... .......... .......... .......... .......... 38% 17.9M 0s
  1650K .......... .......... .......... .......... .......... 39% 17.6M 0s
  1700K .......... .......... .......... .......... .......... 40% 16.8M 0s
  1750K .......... .......... .......... .......... .......... 42% 19.0M 0s
  1800K .......... .......... .......... .......... .......... 43% 18.3M 0s
  1850K .......... .......... .......... .......... .......... 44% 18.9M 0s
  1900K .......... .......... .......... .......... .......... 45% 20.7M 0s
  1950K .......... .......... .......... .......... .......... 46% 14.3M 0s
  2000K .......... .......... .......... .......... .......... 47% 13.7M 0s
  2050K .......... .......... .......... .......... .......... 49% 20.1M 0s
  2100K .......... .......... .......... .......... .......... 50% 20.0M 0s
  2150K .......... .......... .......... .......... .......... 51% 20.4M 0s
  2200K .......... .......... .......... .......... .......... 52% 16.7M 0s
  2250K .......... .......... .......... .......... .......... 53% 18.9M 0s
  2300K .......... .......... .......... .......... .......... 55% 15.3M 0s
  2350K .......... .......... .......... .......... .......... 56% 19.8M 0s
  2400K .......... .......... .......... .......... .......... 57% 18.3M 0s
  2450K .......... .......... .......... .......... .......... 58% 18.8M 0s
  2500K .......... .......... .......... .......... .......... 59% 20.4M 0s
  2550K .......... .......... .......... .......... .......... 60% 17.3M 0s
  2600K .......... .......... .......... .......... .......... 62% 18.7M 0s
  2650K .......... .......... .......... .......... .......... 63% 15.1M 0s
  2700K .......... .......... .......... .......... .......... 64% 20.9M 0s
  2750K .......... .......... .......... .......... .......... 65% 20.7M 0s
  2800K .......... .......... .......... .......... .......... 66% 17.6M 0s
  2850K .......... .......... .......... .......... .......... 67% 18.3M 0s
  2900K .......... .......... .......... .......... .......... 69% 14.1M 0s
  2950K .......... .......... .......... .......... .......... 70% 16.3M 0s
  3000K .......... .......... .......... .......... .......... 71% 19.3M 0s
  3050K .......... .......... .......... .......... .......... 72% 18.3M 0s
  3100K .......... .......... .......... .......... .......... 73% 20.5M 0s
  3150K .......... .......... .......... .......... .......... 74% 15.7M 0s
  3200K .......... .......... .......... .......... .......... 76% 16.3M 0s
  3250K .......... .......... .......... .......... .......... 77% 16.9M 0s
  3300K .......... .......... .......... .......... .......... 78% 20.6M 0s
  3350K .......... .......... .......... .......... .......... 79% 18.9M 0s
  3400K .......... .......... .......... .......... .......... 80% 20.1M 0s
  3450K .......... .......... .......... .......... .......... 81% 18.7M 0s
  3500K .......... .......... .......... .......... .......... 83% 13.1M 0s
  3550K .......... .......... .......... .......... .......... 84% 15.7M 0s
  3600K .......... .......... .......... .......... .......... 85% 20.4M 0s
  3650K .......... .......... .......... .......... .......... 86% 17.8M 0s
  3700K .......... .......... .......... .......... .......... 87% 19.7M 0s
  3750K .......... .......... .......... .......... .......... 88% 17.0M 0s
  3800K .......... .......... .......... .......... .......... 90% 13.6M 0s
  3850K .......... .......... .......... .......... .......... 91% 17.4M 0s
  3900K .......... .......... .......... .......... .......... 92% 20.8M 0s
  3950K .......... .......... .......... .......... .......... 93% 16.8M 0s
  4000K .......... .......... .......... .......... .......... 94% 19.9M 0s
  4050K .......... .......... .......... .......... .......... 95% 14.9M 0s
  4100K .......... .......... .......... .......... .......... 97% 17.8M 0s
  4150K .......... .......... .......... .......... .......... 98% 16.6M 0s
  4200K .......... .......... .......... .......... .......... 99% 18.4M 0s
  4250K .......... ..........                                 100% 15.5M=0.2s
2020-03-23 22:02:16 (17.3 MB/s) - ‘/tmp/user_data.sh.EK9wIv/scripts/downloads/50-maas-01-commissioning/amd64’ saved [4373408/4373408]
{
    "cpu": {
        "architecture": "x86_64",
        "sockets": [
            {
                "name": "Intel Core Processor (Skylake, IBRS)",
                "vendor": "GenuineIntel",
                "socket": 0,
                "cache": [
                    {
                        "level": 1,
                        "type": "Data",
                        "size": 32768
                    },
                    {
                        "level": 1,
                        "type": "Instruction",
                        "size": 32768
                    },
                    {
                        "level": 2,
                        "type": "Unified",
                        "size": 4194304
                    },
                    {
                        "level": 3,
                        "type": "Unified",
                        "size": 16777216
                    }
                ],
                "cores": [
                    {
                        "core": 0,
                        "numa_node": 0,
                        "threads": [
                            {
                                "id": 0,
                                "thread": 0,
                                "online": true
                            }
                        ]
                    }
                ]
            }
        ],
        "total": 1
    },
    "memory": {
        "nodes": [
            {
                "numa_node": 0,
                "hugepages_used": 0,
                "hugepages_total": 0,
                "used": 876933120,
                "total": 1032945664
            }
        ],
        "hugepages_total": 0,
        "hugepages_used": 0,
        "hugepages_size": 2097152,
        "used": 164585472,
        "total": 1032945664
    },
    "gpu": {
        "cards": [
            {
                "numa_node": 0,
                "pci_address": "0000:00:02.0",
                "vendor": "Red Hat, Inc.",
                "vendor_id": "1b36",
                "product": "QXL paravirtual graphic card",
                "product_id": "0100"
            }
        ],
        "total": 1
    },
    "network": {
        "cards": [
            {
                "driver": "virtio_net",
                "driver_version": "4.15.0-91-generic",
                "ports": [
                    {
                        "id": "ens3",
                        "address": "52:54:00:0b:6d:8c",
                        "port": 0,
                        "protocol": "ethernet",
                        "port_type": "other",
                        "transceiver_type": "internal",
                        "auto_negotiation": false,
                        "link_detected": true
                    }
                ],
                "numa_node": 0,
                "pci_address": "0000:00:03.0",
                "vendor": "Red Hat, Inc.",
                "vendor_id": "1af4",
                "product_id": "0001"
            }
        ],
        "total": 1
    },
    "storage": {
        "disks": [
            {
                "id": "sda",
                "device": "8:0",
                "model": "QEMU HARDDISK",
                "type": "scsi",
                "read_only": false,
                "size": 5368709120,
                "removable": false,
                "numa_node": 0,
n                "device_path": "pci-0000:00:01.1-ata-1",
                "block_size": 512,
                "firmware_version": "2.5+",
                "rpm": 0,
                "serial": "QM00001",
                "device_id": "ata-QEMU_HARDDISK_QM00001",
                "partitions": [
                    {
                        "id": "sda1",
                        "device": "8:1",
                        "read_only": false,
                        "size": 5367643648,
                        "partition": 1
                    }
                ]
            }
        ],
        "total": 2
    }
}
````
</details>

This output represents a catalogue of the resources available on this machine, in a format readable by both humans and machines.  You can use this to verify that your configuration is what you expected.

<!-- snap-2-8-ui snap-2-8-cli snap-2-7-ui snap-2-7-cli deb-2-8-ui deb-2-8-cli deb-2-7-ui deb-2-7-cli
<a href="#heading--99-maas-01-capture-lldp"><h2 id="heading--99-maas-01-capture-lldp">99-maas-01-capture-lldp</h2></a>

This script gathers LLDP network information to be presented on the logs page; this data is not used by MAAS at all.  Note that the log output from a successful run is uninteresting.

<a href="#heading--99-maas-05-kernel-cmdline"><h2 id="heading--99-maas-05-kernel-cmdline">99-maas-05-kernel-cmdline</h2></a>

This script is used to update the boot devices; it double-checks that the right boot interface is selected.  Successful output is the specific command that boots the machine kernel, something like this:

````
nomodeset ro root=squash:http://192.168.122.2:5248/images/ubuntu/amd64/generic/bionic/daily/squashfs ip=::::52-54-00-0b-6d-8c:BOOTIF ip6=off overlayroot=tmpfs overlayroot_cfgdisk=disabled cc:{'datasource_list': ['MAAS']}end_cc cloud-config-url=http://192-168-122-0--24.maas-internal:5248/MAAS/metadata/latest/by-id/pb6833/?op=get_preseed apparmor=0 log_host=192.168.122.2 log_port=5247 BOOTIF=01-52:54:00:0b:6d:8c
````

These are the kernel command line parameters, which control the invocation of various modules built into the kernel.  The function `modprobe` parses this kernel command line and collects the relevant module parameters when it loads a module.  Note that this command line could also be used to pull in loadable modules.
snap-2-8-ui snap-2-8-cli snap-2-7-ui snap-2-7-cli deb-2-8-ui deb-2-8-cli deb-2-7-ui deb-2-7-cli -->

<!-- snap-2-9-ui snap-2-9-cli deb-2-9-ui deb-2-9-cli snap-3-0-cli deb-3-0-cli snap-3-0-ui deb-3-0-ui 
<a href="#heading--maas-capture-lldp"><h2 id="heading--maas-capture-lldp">maas-capture-lldp</h2></a>

This script gathers LLDP network information to be presented on the logs page; this data is not used by MAAS at all.  The script runs in parallel with other scripts for speed. Note that the log output from a successful run is uninteresting.

<a href="#heading--maas-kernel-cmdline"><h2 id="heading--maas-kernel-cmdline">maas-kernel-cmdline</h2></a>

This script is used to update the boot devices; it double-checks that the right boot interface is selected.  Successful output is the specific command that boots the machine kernel, something like this:

````
nomodeset ro root=squash:http://192.168.122.2:5248/images/ubuntu/amd64/generic/bionic/daily/squashfs ip=::::52-54-00-0b-6d-8c:BOOTIF ip6=off overlayroot=tmpfs overlayroot_cfgdisk=disabled cc:{'datasource_list': ['MAAS']}end_cc cloud-config-url=http://192-168-122-0--24.maas-internal:5248/MAAS/metadata/latest/by-id/pb6833/?op=get_preseed apparmor=0 log_host=192.168.122.2 log_port=5247 BOOTIF=01-52:54:00:0b:6d:8c
````

These are the kernel command line parameters, which control the invocation of various modules built into the kernel.  The function `modprobe` parses this kernel command line and collects the relevant module parameters when it loads a module.  Note that this command line could also be used to pull in loadable modules.
snap-2-9-cli snap-2-9-ui deb-2-9-cli deb-2-9-cli -->
