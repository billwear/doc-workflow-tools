
||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/configuration-journey-snap-2-7-cli/2526) ~ [UI](/t/configuration-journey-snap-2-7-ui/2527)|[CLI](/t/configuration-journey-snap-2-8-cli/2528) ~ [UI](/t/configuration-journey-snap-2-8-ui/2529)|[CLI](/t/configuration-journey-snap-2-9-cli/2530) ~ [UI](/t/configuration-journey-snap-2-9-ui/2531)|[CLI](/t/configuration-journey-snap-3-0-cli/3885) ~ [UI](/t/configuration-journey-snap-3-0-ui/3886)|
Packages|[CLI](/t/configuration-journey-deb-2-7-cli/2532) ~ [UI](/t/configuration-journey-deb-2-7-ui/2533)|[CLI](/t/configuration-journey-deb-2-8-cli/2534) ~ [UI](/t/configuration-journey-deb-2-8-ui/2535)|[CLI](/t/configuration-journey-deb-2-9-cli/2536) ~ [UI](/t/configuration-journey-deb-2-9-ui/2537)|[CLI](/t/configuration-journey-deb-3-0-cli/3887) ~ [UI](/t/configuration-journey-deb-3-0-ui/3888)|

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 
Once you've successfully installed MAAS (regardless of method), you can login to the MAAS CLI via the following process.  First, generate the API-key for the user you're going to employing:

```
sudo maas apikey --username=$PROFILE > api-key-file
```

Replace $PROFILE with whatever username you set during the `createadmin` part of the install process.  Next, login with the following command:

```
maas login $PROFILE $MAAS_URL < api-key-file
```

Substitute $MAAS_URL with the URL that was returned to you when you initialised MAAS, for example, `192.168.43.251:5240/MAAS`.  Remember that, once you've logged in, you can get extensive CLI help with the command:

```
maas admin --help
```

Sample output is shown in the detail section below.

<details><summary>MAAS CLI help, sample output</summary>
usage: maas admin [-h] COMMAND ...

Issue commands to the MAAS region controller at http://192.168.43.251:5240/MAAS/api/2.0/.

optional arguments:
  -h, --help            show this help message and exit

drill down:
  COMMAND
    account             Manage the current logged-in user.
    bcache-cache-set    Manage bcache cache set on a machine.
    bcache-cache-sets   Manage bcache cache sets on a machine.
    bcache              Manage bcache device on a machine.
    bcaches             Manage bcache devices on a machine.
    block-device        Manage a block device on a machine.
    block-devices       Manage block devices on a machine.
    boot-resource       Manage a boot resource.
    boot-resources      Manage the boot resources.
    boot-source         Manage a boot source.
    boot-source-selection
                        Manage a boot source selection.
    boot-source-selections
                        Manage the collection of boot source selections.
    boot-sources        Manage the collection of boot sources.
    commissioning-script
                        Manage a custom commissioning script.
    commissioning-scripts
                        Manage custom commissioning scripts.
    dhcpsnippet         Manage an individual DHCP snippet.
    dhcpsnippets        Manage the collection of all DHCP snippets in MAAS.
    dnsresource         Manage dnsresource.
    dnsresource-record  Manage dnsresourcerecord.
    dnsresource-records
                        Manage DNS resource records (e.g. CNAME, MX, NS, SRV,
                        TXT)
    dnsresources        Manage dnsresources.
    device              Manage an individual device.
    devices             Manage the collection of all the devices in the MAAS.
    discoveries         Query observed discoveries.
    discovery           Read or delete an observed discovery.
    domain              Manage domain.
    domains             Manage domains.
    events              Retrieve filtered node events.
    fabric              Manage fabric.
    fabrics             Manage fabrics.
    fan-network         Manage Fan Network.
    fan-networks        Manage Fan Networks.
    file                Manage a FileStorage object.
    files               Manage the collection of all the files in this MAAS.
    ipaddresses         Manage IP addresses allocated by MAAS.
    iprange             Manage IP range.
    ipranges            Manage IP ranges.
    interface           Manage a node's or device's interface.
    interfaces          Manage interfaces on a node.
    license-key         Manage a license key.
    license-keys        Manage the license keys.
    maas                Manage the MAAS server.
    machine             Manage an individual machine.
    machines            Manage the collection of all the machines in the MAAS.
    network             Manage a network.
    networks            Manage the networks.
    node                Manage an individual Node.
    node-results        Read the collection of commissioning script results.
    node-script         Manage or view a custom script.
    node-script-result  Manage node script results.
    node-script-results
                        Manage node script results.
    node-scripts        Manage custom scripts.
    nodes               Manage the collection of all the nodes in the MAAS.
    notification        Manage an individual notification.
    notifications       Manage the collection of all the notifications in
                        MAAS.
    package-repositories
                        Manage the collection of all Package Repositories in
                        MAAS.
    package-repository  Manage an individual package repository.
    partition           Manage partition on a block device.
    partitions          Manage partitions on a block device.
    pod                 Manage an individual pod.
    pods                Manage the collection of all the pod in the MAAS.
    rack-controller     Manage an individual rack controller.
    rack-controllers    Manage the collection of all rack controllers in MAAS.
    raid                Manage a specific RAID (Redundant Array of Independent
                        Disks) on a machine.
    raids               Manage all RAIDs (Redundant Array of Independent
                        Disks) on a machine.
    region-controller   Manage an individual region controller.
    region-controllers  Manage the collection of all region controllers in
                        MAAS.
    resource-pool       Manage a resource pool.
    resource-pools      Manage resource pools.
    sshkey              Manage an SSH key.
    sshkeys             Manage the collection of all the SSH keys in this
                        MAAS.
    sslkey              Manage an SSL key.
    sslkeys             Operations on multiple keys.
    space               Manage space.
    spaces              Manage spaces.
    static-route        Manage static route.
    static-routes       Manage static routes.
    subnet              Manage subnet.
    subnets             Manage subnets.
    tag                 Tags are properties that can be associated with a Node
                        and serve as criteria for selecting and allocating
                        nodes.
    tags                Manage all tags known to MAAS.
    user                Manage a user account.
    users               Manage the user accounts of this MAAS.
    version             Information about this MAAS instance.
    vlan                Manage a VLAN on a fabric.
    vlans               Manage VLANs on a fabric.
    vm-host             Manage an individual vm-host.
    vm-hosts            Manage the collection of all the vm-hosts in the MAAS.
    vmfs-datastore      Manage VMFS datastore on a machine.
    vmfs-datastores     Manage VMFS datastores on a machine.
    volume-group        Manage volume group on a machine.
    volume-groups       Manage volume groups on a machine.
    zone                Manage a physical zone.
    zones               Manage physical zones.

This is a profile.  Any commands you issue on this profile will
operate on the MAAS region server.

The command information you see here comes from the region server's
API; it may differ for different profiles.  If you believe the API may
have changed, use the command's 'refresh' sub-command to fetch the
latest version of this help information from the server.
</details>

<a href="#heading--configuration"><h2 id="heading--configuration">Configuration</h2></a>

Configuring MAAS consists of four broad steps:

1. Setting upstream DNS
2. Importing an SSH key for your admin user
3. Importing images
4. Configuring DNS

This section will cover those four operations

<a href="#heading--setting-dns"><h3 id="heading--setting-dns">Setting DNS</h3></a>

After logging in for the first time, you will need to set a number of system-wide configuration options.  First up, you should configure DNS.  You can check out the help for DNS settings, known in the CLI as a "DNS forwarder":

```
maas $PROFILE maas set-config name=upstream_dns value="8.8.8.8"
```

Here, we've set the DNS forwarder to "8.8.8.8" (Google), which is a reliable value.

<a href="#heading--setting-ssh"><h3 id="heading--setting-ssh">Setting SSH for the admin user</h3></a>

To add a public SSH key to a MAAS user account, type the following command:

```
maas $PROFILE sshkeys create "key=$SSH_KEY"
```

<a href="#heading--importing-images"><h3 id="heading--importing-images">Importing images</h3></a>

Before going any further, it's worthwhile to start the image import, as it can sometimes take a few minutes.  You can see what images you already have downloaded with this command:

```
maas $PROFILE boot-resources read | jq -r '.[] | "\(.name)\t\(.architecture)"'
```

This command will return a list similar to the following:

```
grub-efi-signed/uefi        amd64/generic
grub-efi/uefi           arm64/generic
grub-ieee1275/open-firmware ppc64el/generic
pxelinux/pxe            i386/generic
ubuntu/bionic           amd64/ga-18.04
ubuntu/bionic           amd64/ga-18.04-lowlatency
ubuntu/bionic           amd64/hwe-18.04
ubuntu/bionic           amd64/hwe-18.04-edge
ubuntu/bionic           amd64/hwe-18.04-lowlatency
ubuntu/bionic           amd64/hwe-18.04-lowlatency-edge
```

Suppose you also want a version called "Trusty" -- you can import a new image by first selecting it for download, like this:

```
maas $PROFILE boot-source-selections create 1 \ > os="ubuntu" release="trusty" arches="amd64" subarches="*" \ > labels="*"
```

which returns some JSON confirming your action:

```
Success.
Machine-readable output follows:
{
    "os": "ubuntu",
    "release": "trusty",
    "arches": [
        "amd64"
    ],
    "subarches": [
        "*"
    ],
    "labels": [
        "*"
    ],
    "boot_source_id": 1,
    "id": 2,
    "resource_uri": "/MAAS/api/2.0/boot-sources/1/selections/2/"
}
```
Once selected, you can start the image import with this command:

```
maas admin boot-resources import
```

which offers a shorter confirmation message:

```
Success.
Machine-readable output follows:
Import of boot resources started
```

<a href="#heading--enabling-dhcp"><h3 id="heading--enabling-dhcp">Enabling DHCP</h3></a>

Once your image has been imported, you'll want to get DHCP working, which means finding the untagged VLAN. In truth, it shouldn’t be too hard, because at this point, there still should only be one.

In order to turn on DHCP, you need to know two things besides the VLAN name (“untagged”): the fabric ID and the primary rack controller name. To start, all the fabrics will be on the same untagged VLAN, so any fabric will do. You can find a valid fabric ID by reading it from any subnet, so just pick one  (e.g., 192.168.123.0/24) and find a usable fabric ID like this:

```
maas $PROFILE subnet read $SUBNET_CIDR | grep fabric_id
```

which returns (in this example):

```
"fabric_id": $FABRIC_ID,
```

Next, find the name of the primary rack controller. It's usually fairly obvious, but for purposes of argument, assume that it's not known. You can get it this way:

```
maas $PROFILE rack-controllers read | grep hostname | cut -d '"' -f 4
```

This returns a hostname, which we'll call:

```
$RACK_CONTR_HOSTNAME
```

Finally, you need to create an IP range for DHCP, in this case, a dynamic range:

```
maas $PROFILE ipranges create type=dynamic start_ip=$START_IP end_ip=$END_IP
```

This command returns something similar to this sample output:

    Success.
    Machine-readable output follows:
    {
        "subnet": {
            "name": "192.168.123.0/24",
            "description": "",
            "vlan": {
                "vid": 0,
                "mtu": 1500,
                "dhcp_on": false,
                "external_dhcp": null,
                "relay_vlan": null,
                "fabric": "fabric-2",
                "primary_rack": null,
                "name": "untagged",
                "id": 5003,
                "space": "undefined",
                "secondary_rack": null,
                "fabric_id": 2,
                "resource_uri": "/MAAS/api/2.0/vlans/5003/"
            },
            "cidr": "192.168.123.0/24",
            "rdns_mode": 2,
            "gateway_ip": null,
            "dns_servers": [],
            "allow_dns": true,
            "allow_proxy": true,
            "active_discovery": false,
            "managed": true,
            "id": 4,
            "space": "undefined",
            "resource_uri": "/MAAS/api/2.0/subnets/4/"
        },
        "type": "dynamic",
        "start_ip": "192.168.123.190",
        "end_ip": "192.168.123.253",
        "user": {
            "is_superuser": true,
            "username": "admin",
            "email": "admin@admin.com",
            "is_local": true,
            "resource_uri": "/MAAS/api/2.0/users/admin/"
        },
        "comment": "",
        "id": 1,
        "resource_uri": "/MAAS/api/2.0/ipranges/1/"
    }

So you should now be able to turn on DHCP like this:

```
maas $PROFILE vlan update $FABRIC_ID untagged dhcp_on=True primary_rack=$RACK_CONTR_HOSTHNAME
```

If you've done everything correctly, you should see JSON output similar to this sample:

    Success.
    Machine-readable output follows:
    {
        "vid": 0,
        "mtu": 1500,
        "dhcp_on": true,
        "external_dhcp": null,
        "relay_vlan": null,
        "fabric": "fabric-2",
        "space": "undefined",
        "primary_rack": "8dwnne",
        "secondary_rack": null,
        "name": "untagged",
        "fabric_id": 2,
        "id": 5003,
        "resource_uri": "/MAAS/api/2.0/vlans/5003/"
    }

snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli  snap-3-0-cli deb-3-0-cli -->

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
Once you've successfully installed MAAS (regardless of method), you can now login here:

```
http://${API_HOST}:5240/MAAS
```

where $API_HOST is the hostname or IP address of the region API server, which was set during installation.  You will see a screen like this:</p>

<a href="https://discourse.maas.io/uploads/default/original/1X/efd8e3f150dfec28114c452c12e24e320848e075.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/efd8e3f150dfec28114c452c12e24e320848e075.jpeg"></a> 

Log in at the prompts, with the login information you created when initialising MAAS.

<a href="#heading--configuration"><h2 id="heading--configuration">Configuration</h2></a>

After a fresh MAAS installation, the web UI presents a couple of welcome  screens.  From these screens, you can set many system-wide options, including connectivity, image downloads, and authentication keys.

<a href="https://discourse.maas.io/uploads/default/original/1X/337aa15e178b14b0ba9a0646953268bf7adac0bb.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/337aa15e178b14b0ba9a0646953268bf7adac0bb.jpeg"></a>  

Your main concerns for this experiment are the DNS forwarder, the Ubuntu image import section, and the SSH public key, though you might want to set the region name to something memorable, since this text will appear at the bottom of every MAAS screen in this install domain. Set the DNS forwarder to something obvious, e.g., `8.8.8.8`, Google’s DNS server.  Set this to your own internal DNS server if you know the IP address.

<a href="https://discourse.maas.io/uploads/default/original/1X/f9751eb857dcd0c124783edeb1aaf87b8b538127.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/f9751eb857dcd0c124783edeb1aaf87b8b538127.jpeg"></a>  

Select an Ubuntu image to import, noting that you may be required to select at least one LTS version, depending upon the version of MAAS that snap installed.  In this example, we've already chosen an image, and downloading is partially complete.

<a href="https://discourse.maas.io/uploads/default/original/1X/6445cde5ffc1e237a1e6d85d280f451bc0b2ab92.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/6445cde5ffc1e237a1e6d85d280f451bc0b2ab92.jpeg"></a>  

When you click on “Continue,” the screen will shift to a screen labelled, “SSH keys for admin:”  

<a href="https://discourse.maas.io/uploads/default/original/1X/dbdcdce7c8f3b7181f894bdfe987758e0c8635fc.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/dbdcdce7c8f3b7181f894bdfe987758e0c8635fc.jpeg"></a> 

In the source drop-down, select “Launchpad,” “Github,” or “Upload.”  If you choose one of the first two, you will need to enter your username for that service.  For example, if you want to upload your SSH public key from Launchpad, you would enter:

    lp:<username>


<a href="https://discourse.maas.io/uploads/default/original/1X/0e4cbf7c8fae3f21664a4d5fe8d0f90785dd6859.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/0e4cbf7c8fae3f21664a4d5fe8d0f90785dd6859.jpeg"></a> 

Likewise, if you want to upload your github public SSH key, you would enter:

    gh:<username>

If you want to use your existing public key from your home directory, you can select “Upload”and then copy your entire public key from <code>.ssh/id_rsa.pub</code> (or wherever you may have stored the key):

<a href="https://discourse.maas.io/uploads/default/original/1X/a94f1f68db07dd9be9e8eaed50f22828c7bb51e0.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/a94f1f68db07dd9be9e8eaed50f22828c7bb51e0.jpeg"></a> 

and paste it into the block labelled “Public key.”  Finally, press the “Import” button to import this key:

<a href="https://discourse.maas.io/uploads/default/original/1X/ab62bf22308343988016189fbbb851c44caf2e33.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/ab62bf22308343988016189fbbb851c44caf2e33.jpeg"></a> 

With this complete, you’ll see that MAAS has been successfully set up. Click ‘Go to the Dashboard’ to proceed.

[note]
Note that you may have to wait a few moments for your selected images to sync locally.
[/note]

<a href="#heading--enabling-dhcp"><h2 id="heading--enabling-dhcp">Enabling DHCP</h2></a>

Before moving forward with MAAS, you'll want to enable DHCP.  You can do this very easily from the web UI by selecting "Subnets" from the top menu, choosing the VLAN on which you want to enable DHCP, and select the button marked, "Enable DHCP."

<a href="#heading--networking"><h2 id="heading--networking">Networking</h2></a>
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui  snap-3-0-ui deb-3-0-ui -->

<!-- deb-2-7-ui
The Dashboard landing page lists non-registered devices that MAAS detected automatically on the network. This [network discovery](/t/network-discovery/2929) process allows you to easily add or map devices already connected to your network -- devices that you may not necessarily want to manage with MAAS.
 deb-2-7-ui -->

<!-- deb-2-8-ui
The Dashboard landing page lists non-registered devices that MAAS detected automatically on the network. This [network discovery](/t/network-discovery/2931) process allows you to easily add or map devices already connected to your network -- devices that you may not necessarily want to manage with MAAS.
 deb-2-8-ui -->

<!-- deb-2-9-ui
The Dashboard landing page lists non-registered devices that MAAS detected automatically on the network. This [network discovery](/t/network-discovery/2933) process allows you to easily add or map devices already connected to your network -- devices that you may not necessarily want to manage with MAAS.
 deb-2-9-ui -->

<!-- deb-3-0-ui
The Dashboard landing page lists non-registered devices that MAAS detected automatically on the network. This [network discovery](/t/network-discovery/4044) process allows you to easily add or map devices already connected to your network -- devices that you may not necessarily want to manage with MAAS.
 deb-3-0-ui -->

<!-- snap-2-7-ui
The Dashboard landing page lists non-registered devices that MAAS detected automatically on the network. This [network discovery](/t/network-discovery/2923) process allows you to easily add or map devices already connected to your network -- devices that you may not necessarily want to manage with MAAS.
 snap-2-7-ui -->

<!-- snap-2-8-ui
The Dashboard landing page lists non-registered devices that MAAS detected automatically on the network. This [network discovery](/t/network-discovery/2925) process allows you to easily add or map devices already connected to your network -- devices that you may not necessarily want to manage with MAAS.
 snap-2-8-ui -->

<!-- snap-2-9-ui
The Dashboard landing page lists non-registered devices that MAAS detected automatically on the network. This [network discovery](/t/network-discovery/2927) process allows you to easily add or map devices already connected to your network -- devices that you may not necessarily want to manage with MAAS.
 snap-2-9-ui -->

<!-- snap-3-0-ui
The Dashboard landing page lists non-registered devices that MAAS detected automatically on the network. This [network discovery](/t/network-discovery/4042) process allows you to easily add or map devices already connected to your network -- devices that you may not necessarily want to manage with MAAS.
 snap-3-0-ui -->

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
<a href="https://discourse.maas.io/uploads/default/original/1X/902f07b6e96d06dcd072501473ce85ff3d303610.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/902f07b6e96d06dcd072501473ce85ff3d303610.jpeg"></a>  

[note]
Network discovery can be disabled at any time from the button on the Dashboard view.  Also note that you can get back to the dashboard at any time by clicking the MAAS logo.
[/note]
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui -->

<a href="#heading--spaces-fabrics-zones-and-subnets"><h3 id="heading--spaces-fabrics-zones-and-subnets">Spaces, fabrics, zones and subnets</h3></a>

Networks in large data centres can be very complex. MAAS offers comprehensive control over networking so that you have the flexibility to reconfigure racks and deploy machines as you see fit. You can isolate machine deployment not only with DNS domains, but also via [subnets](/t/concepts-and-terms/785#heading--subnets), [spaces](/t/concepts-and-terms/785#heading--spaces), [zones](/t/concepts-and-terms/785#heading--zones), and [fabrics](/t/concepts-and-terms/785#heading--fabrics).  The links provide more details, but these are all basically collections:

* **subnet** has the traditional meaning: a range of IP addresses covering a subset of IP addresses.  Generally speaking , a subnet is a collection of IP addresses which includes at least two addresses.
* a **space** is a collection of subnets that you can create with MAAS, understanding that each subnet can belong to only one space.  Spaces allow multiple subnets to communicate without requiring a direct network path between them.
* a **zone** is also an ad-hoc collection, but one which groups individual nodes, rather than subnets.  MAAS allows you to create and edit zones at will.
* a **fabric** is essentially a collection of trunked switches, allowing you to access a group of VLANs.

Here is a diagram that helps to illustrate these concepts:

<a href="https://discourse.maas.io/uploads/default/original/1X/dd60fdeba34d3cf33d4cf42db1f745ba95542b69.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/dd60fdeba34d3cf33d4cf42db1f745ba95542b69.jpeg"></a> 

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
Be aware that these network settings are spread across several web UI configuration pages. The Zones page, for example, enables you to see how many machines, devices and controllers are using a zone, and allows you to add and edit zones.  The Subnets page, shown below, provides access to fabric, VLAN, subnet and spaces configuration.

<a href="https://discourse.maas.io/uploads/default/original/1X/89d90a15e70a57e6951ee62910b503895e08251e.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/89d90a15e70a57e6951ee62910b503895e08251e.jpeg"></a> 

<a href="#heading--deploy-hardware"><h2 id="heading--deploy-hardware">Deployment</h2></a>

MAAS-managed machines are listed -- and operated on -- from the Machines page, making it one of the most important screens in the MAAS web UI:

<a href="https://discourse.maas.io/uploads/default/original/1X/58a37e0dc29bc233f771c33d07a0e03e8d55cb87.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/58a37e0dc29bc233f771c33d07a0e03e8d55cb87.jpeg"></a> 

If you are testing MAAS using virtual machines, the machines appear here as soon as they boot. New machines are added automatically when they first connect to your network. Alternatively, the ‘Add hardware’ menu lets you add machines manually, via their MAC address.

After you configure power and interfaces, MAAS must commission machines to retrieve CPU, memory and storage information. From this point, you can command MAAS to acquire, test, deploy and release these machines as you work with your MAAS cloud.
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui  -->

<!-- deb-2-7-ui
While you are testing MAAS, be sure to check out filters, which can narrow your view based on both [tags](/t/maas-tags/2893) and hardware characteristics.  You can select and manage machines in either filtered or full views.
 deb-2-7-ui -->

<!-- deb-2-8-ui
While you are testing MAAS, be sure to check out filters, which can narrow your view based on both [tags](/t/maas-tags/2895) and hardware characteristics.  You can select and manage machines in either filtered or full views.
 deb-2-8-ui -->

<!-- deb-2-9-ui
While you are testing MAAS, be sure to check out filters, which can narrow your view based on both [tags](/t/maas-tags/2897) and hardware characteristics.  You can select and manage machines in either filtered or full views.
 deb-2-9-ui -->

<!-- deb-3-0-ui
While you are testing MAAS, be sure to check out filters, which can narrow your view based on both [tags](/t/maas-tags/4024) and hardware characteristics.  You can select and manage machines in either filtered or full views.
 deb-3-0-ui -->

<!-- snap-2-7-ui
While you are testing MAAS, be sure to check out filters, which can narrow your view based on both [tags](/t/maas-tags/2887) and hardware characteristics.  You can select and manage machines in either filtered or full views.
 snap-2-7-ui -->

<!-- snap-2-8-ui
While you are testing MAAS, be sure to check out filters, which can narrow your view based on both [tags](/t/maas-tags/2889) and hardware characteristics.  You can select and manage machines in either filtered or full views.
 snap-2-8-ui -->

<!-- snap-2-9-ui
While you are testing MAAS, be sure to check out filters, which can narrow your view based on both [tags](/t/maas-tags/2891) and hardware characteristics.  You can select and manage machines in either filtered or full views.
 snap-2-9-ui -->

<!-- snap-3-0-ui
While you are testing MAAS, be sure to check out filters, which can narrow your view based on both [tags](/t/maas-tags/4022) and hardware characteristics.  You can select and manage machines in either filtered or full views.
 snap-3-0-ui -->

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 

<a href="#heading--images"><h3 id="heading--images">Images</h3></a>

When it comes to running applications, MAAS can easily deploy any supported variant of Ubuntu, including LTS and non-LTR versions for x86, ARM, PPC and s390x systems. You can also deploy several other operating systems to your machines, including CentOS 7, CentOS 6, Windows, RHEL, and ESXi images, via <a href="https://www.ubuntu.com/support" rel="nofollow noopener">Ubuntu Advantage^</a>.

<a href="https://discourse.maas.io/uploads/default/original/1X/27c47222c1fc0e34ed70134a1007dde067d2de81.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/27c47222c1fc0e34ed70134a1007dde067d2de81.jpeg"></a> 

<a href="#heading--vm-hosts"><h3 id="heading--vm-hosts">VM hosts</h3></a>

snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui -->

<!-- deb-2-7-cli
[VM hosts]( /t/vm-hosting/2748) can give you greater control over your hardware.  A VM host is a collection of individual virtual machines.  You can use a VM host to compose machines into an abstraction of resources that functions like a physical machine -- without building one!
 deb-2-7-cli -->

<!-- deb-2-7-ui
[VM hosts]( /t/vm-hosting/2749) can give you greater control over your hardware.  A VM host is a collection of individual virtual machines.  You can use a VM host to compose machines into an abstraction of resources that functions like a physical machine -- without building one!
 deb-2-7-ui -->

<!-- deb-2-8-cli
[VM hosts]( /t/vm-hosting/2750) can give you greater control over your hardware.  A VM host is a collection of individual virtual machines.  You can use a VM host to compose machines into an abstraction of resources that functions like a physical machine -- without building one!
 deb-2-8-cli -->

<!-- deb-2-8-ui
[VM hosts]( /t/vm-hosting/2751) can give you greater control over your hardware.  A VM host is a collection of individual virtual machines.  You can use a VM host to compose machines into an abstraction of resources that functions like a physical machine -- without building one!
 deb-2-8-ui -->

<!-- deb-2-9-cli
[VM hosts]( /t/vm-hosting/2752) can give you greater control over your hardware.  A VM host is a collection of individual virtual machines.  You can use a VM host to compose machines into an abstraction of resources that functions like a physical machine -- without building one!
 deb-2-9-cli -->

<!-- deb-3-0-ui
[VM hosts](/t/vm-hosting/4164) can give you greater control over your hardware.  A LXD (pronounced "lex-D") VM host is a collection of individual virtual machines.  You can use a LXD VM host to compose machines into an abstraction of resources that functions like a physical machine -- without building one!
 deb-3-0-ui -->

<!-- deb-3-0-cli
[VM hosts](/t/vm-hosting/4163) can give you greater control over your hardware.  A LXD (pronounced "lex-D") VM host is a collection of individual virtual machines.  You can use a LXD VM host to compose machines into an abstraction of resources that functions like a physical machine -- without building one!
 deb-3-0-cli -->

<!-- deb-2-9-ui
[VM hosts](/t/vm-hosting/2753) can give you greater control over your hardware.  A VM host is a collection of individual virtual machines.  You can use a VM host to compose machines into an abstraction of resources that functions like a physical machine -- without building one!
 deb-2-9-ui -->

<!-- snap-2-7-cli
[VM hosts]( /t/vm-hosting/2742) can give you greater control over your hardware.  A VM host is a collection of individual virtual machines.  You can use a VM host to compose machines into an abstraction of resources that functions like a physical machine -- without building one!
 snap-2-7-cli -->

<!-- snap-2-7-ui
[VM hosts]( /t/vm-hosting/2743) can give you greater control over your hardware.  A VM host is a collection of individual virtual machines.  You can use a VM host to compose machines into an abstraction of resources that functions like a physical machine -- without building one!
 snap-2-7-ui -->

<!-- snap-2-8-cli
[VM hosts]( /t/vm-hosting/2744) can give you greater control over your hardware.  A VM host is a collection of individual virtual machines.  You can use a VM host to compose machines into an abstraction of resources that functions like a physical machine -- without building one!
 snap-2-8-cli -->

<!-- snap-2-8-ui
[VM hosts]( /t/vm-hosting/2745) can give you greater control over your hardware.  A VM host is a collection of individual virtual machines.  You can use a VM host to compose machines into an abstraction of resources that functions like a physical machine -- without building one!
 snap-2-8-ui -->

<!-- snap-2-9-cli
[VM hosts]( /t/vm-hosting/2746) can give you greater control over your hardware.  A VM host is a collection of individual virtual machines.  You can use a VM host to compose machines into an abstraction of resources that functions like a physical machine -- without building one!
 snap-2-9-cli -->

<!-- snap-2-9-ui
[VM hosts]( /t/vm-hosting/2747) can give you greater control over your hardware.  A VM host is a collection of individual virtual machines.  You can use a VM host to compose machines into an abstraction of resources that functions like a physical machine -- without building one!
 snap-2-9-ui -->

<!-- snap-3-0-cli
[VM hosts](/t/vm-hosting/4161) can give you greater control over your hardware.  A LXD (pronounced "lex-D") VM host is a collection of individual virtual machines.  You can use a LXD VM host to compose machines into an abstraction of resources that functions like a physical machine -- without building one!
 snap-3-0-cli -->

<!-- snap-3-0-ui
[VM hosts](/t/vm-hosting/4162) can give you greater control over your hardware.  A LXD (pronounced "lex-D") VM host is a collection of individual virtual machines.  You can use a LXD VM host to compose machines into an abstraction of resources that functions like a physical machine -- without building one!
 snap-3-0-ui -->

<!-- deb-2-9-ui snap-2-9-ui
It’s easy to add a virsh VM host: click the "Add KVM" button on the "KVM" page of the web UI, give the VM host a name, and select `virsh` or `lxd` as the VM host type.  You will also need to enter the address for the KVM host: in the case of `virsh`, this address looks something like `qemu+ssh://<yourusername>@10.249.0.2/system`, with password equal to the password for `<yourusername>`; if you're using `lxd`, this address will be the IP of the LXD bridge gateway (.1), with the password being the trust password you entered when initializing LXD.

After you create a VM host, you compose hardware by selecting the VM host, and then selecting "Compose" from the Action menu. You can configure composed hardware as desired, including the number of cores, CPU speed, RAM and combined storage.  Then just click "Compose machine", and MAAS will combine resources to create a new, single entity that can be used just like any other machine.  VM hosts abstract multiple resources:

<a href="https://discourse.maas.io/uploads/default/original/1X/c57d7cf802bfd3f968cc54a829cd1629c45e9f62.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/c57d7cf802bfd3f968cc54a829cd1629c45e9f62.jpeg"></a> 

into pools of composable hardware:

<a href="https://discourse.maas.io/uploads/default/original/1X/763029b5678b6f88317359d28eac3003f7298f37.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/763029b5678b6f88317359d28eac3003f7298f37.jpeg"></a> 
 deb-2-9-ui snap-2-9-ui -->

<!-- snap-2-7-ui snap-2-8-ui deb-2-7-ui deb-2-8-ui
It’s easy to add a virsh VM host: click the "Add KVM" button on the "KVM" page of the web UI, give the VM host a name, and select as the VM host type.  You will also need to enter the address for the KVM host; this address will look something like 'qemu+ssh://<yourusername>@10.249.0.2/system`, where the paasword will be the same password `<yourusername>` uses to log into the host.

After you create a VM host, you compose hardware by selecting the VM host, and then selecting "Compose" from the Action menu. You can configure composed hardware as desired, including the number of cores, CPU speed, RAM and combined storage.  Then just click "Compose machine", and MAAS will combine resources to create a new, single entity that can be used just like any other machine.  VM hosts abstract multiple resources:

<a href="https://discourse.maas.io/uploads/default/original/1X/c57d7cf802bfd3f968cc54a829cd1629c45e9f62.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/c57d7cf802bfd3f968cc54a829cd1629c45e9f62.jpeg"></a> 

into pools of composable hardware:

<a href="https://discourse.maas.io/uploads/default/original/1X/763029b5678b6f88317359d28eac3003f7298f37.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/763029b5678b6f88317359d28eac3003f7298f37.jpeg"></a> 
snap-2-7-ui snap-2-8-ui deb-2-7-ui deb-2-8-ui -->

<!--  snap-3-0-ui deb-3-0-ui snap-3-0-cli deb-3-0-cli 
It’s easy to add a LXD VM host: click the "Add KVM" button on the "KVM" page of the web UI, give the VM host a name, and select "lxd" as the VM host type.  You will also need to enter the IP address for the gateway (.1) of the bridge you're using to connect to LXD.  The password will be the trust password you created when initializing LXD.

<a href="https://discourse.maas.io/uploads/default/original/2X/f/ff398586b76154dd20e4c194e30f5c832a7dac89.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/f/ff398586b76154dd20e4c194e30f5c832a7dac89.png"></a>

After you create a VM host, you compose hardware by selecting the host, and then selecting "Compose" from the Action menu. You can configure composed hardware as desired, including the number of cores, CPU speed, RAM and combined storage.  Then just click "Compose machine", and MAAS will combine resources to create a new, single entity that can be used just like any other machine.  VM hosts abstact multiple resources into pools of composable hardware.
 snap-3-0-ui deb-3-0-ui snap-3-0-cli deb-3-0-cli -->

There you have it: A quick tour of MAAS and its capabilities.  Read on through the documentation to learn more.
