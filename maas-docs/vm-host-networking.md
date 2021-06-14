||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/vm-host-networking-snap-2-7-cli/3210) ~ [UI](/t/vm-host-networking-snap-2-7-ui/3211)|[CLI](/t/vm-host-networking-snap-2-8-cli/3212) ~ [UI](/t/vm-host-networking-snap-2-8-ui/3213)|[CLI](/t/vm-host-networking-snap-2-9-cli/3214) ~ [UI](/t/vm-host-networking-snap-2-9-ui/3215)|[CLI](/t/vm-host-networking-snap-3-0-cli/4165) ~ [UI](/t/vm-host-networking-snap-3-0-ui/4166)|
Packages|[CLI](/t/vm-host-networking-deb-2-7-cli/3216) ~ [UI](/t/vm-host-networking-deb-2-7-ui/3217)|[CLI](/t/vm-host-networking-deb-2-8-cli/3218) ~ [UI](/t/vm-host-networking-deb-2-8-ui/3219)|[CLI](/t/vm-host-networking-deb-2-9-cli/3220) ~ [UI](/t/vm-host-networking-deb-2-9-ui/3221)|[CLI](/t/vm-host-networking-deb-3-0-cli/4167) ~ [UI](/t/vm-host-networking-deb-3-0-ui/4168)|

In order to  deploy a VM host in your MAAS network, you first need to set up a bridge to connect between your VM host and MAAS itself.  This section explains several ways of accomplishing this.

<!-- snap-2-7-ui deb-2-7-ui
#### Four questions you may have:

1. [How do I set up a VM host bridge with the web UI?](#heading--maas-bridge-web-ui)
2. [How do I set up a VM host bridge with netplan?](#heading--maas-bridge-netplan)
3. [How do I set up a VM host bridge with libvirt?](#heading--maas-bridge-libvirt)
4. [How do I set up SSH for use by libvirt?](#heading--set-up-ssh)
 snap-2-7-ui deb-2-7-ui -->
 
<!-- snap-2-8-ui snap-2-9-ui deb-2-8-ui deb-2-9-ui  snap-3-0-ui deb-3-0-ui 
#### Five questions you may have:

1. [How do I set up a VM host bridge with the web UI?](#heading--maas-bridge-web-ui)
2. [How do I set up a VM host bridge with netplan?](#heading--maas-bridge-netplan)
3. [How do I set up a VM host bridge with libvirt?](#heading--maas-bridge-libvirt)
4. [How do I set up SSH for use by libvirt?](#heading--set-up-ssh)
5. [How do I make LXD available for hosting?](#heading--lxd-setup)

LXD sets up a bridge as part of the [initialisation process](#heading--lxd-setup); note that you will have to perform a couple of additional steps to prevent LXD from offering DHCP, which will interfere with the normal operation of MAAS.  Everything you need to know is described at the initialisation link.
 snap-2-8-ui snap-2-9-ui deb-2-8-ui deb-2-9-ui  snap-3-0-ui deb-3-0-ui -->

<!-- snap-2-7-cli deb-2-7-cli 
#### Four questions you may have:

1. [How do I set up a VM host bridge with the MAAS CLI/API?](#heading--maas-bridge-cli)
2. [How do I set up a VM host bridge with netplan?](#heading--maas-bridge-netplan)
3. [How do I set up a VM host bridge with libvirt?](#heading--maas-bridge-libvirt)
4. [How do I set up SSH for use by libvirt?](#heading--set-up-ssh)
 snap-2-7-cli deb-2-7-cli -->

<!-- snap-2-8-cli snap-2-9-cli deb-2-8-cli deb-2-9-cli  snap-3-0-cli deb-3-0-cli 
#### Five questions you may have:

1. [How do I set up a VM host bridge with the MAAS CLI/API?](#heading--maas-bridge-cli)
2. [How do I set up a VM host bridge with netplan?](#heading--maas-bridge-netplan)
3. [How do I set up a VM host bridge with libvirt?](#heading--maas-bridge-libvirt)
4. [How do I set up SSH for use by libvirt?](#heading--set-up-ssh)
5. [How do I make LXD available for hosting?](#heading--lxd-setup)

LXD sets up a bridge as part of the [initialisation process](#heading--lxd-setup); note that you will have to perform a couple of additional steps to prevent LXD from offering DHCP, which will interfere with the normal operation of MAAS.  Everything you need to know is described at the initialisation link.
snap-2-8-cli snap-2-9-cli deb-2-8-cli deb-2-9-cli  snap-3-0-cli deb-3-0-cli -->

To enable VM host networking features, MAAS must match the VM host IP address of a potential VM host with a known device (a machine or controller). For example, if a machine not known to MAAS is set up as a VM host, enhanced interface selection features will not be available.

[note]
It's essential to enforce usage of IP addresses to avoid domain name conflicts, should different controllers resolve the same domain name with different IP addresses. You should also avoid using 127.0.0.1 when running multiple controllers, as it would confuse MAAS.
[/note]

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui  snap-3-0-ui deb-3-0-ui 
<a href="#heading--maas-bridge-web-ui"><h2 id="heading--maas-bridge-web-ui">Set up VM host bridge with MAAS UI</h2></a>

You can use the MAAS UI to configure a bridge to connect a VM host to MAAS:

Select the machine you want to use as a VM host, switch to the "Network" tab. Select the network where you want to create the bridge and click "Create bridge:"

<a href="https://discourse.maas.io/uploads/default/original/1X/29624d737106c5bad777aee9d2c8cad9c3de7151.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/29624d737106c5bad777aee9d2c8cad9c3de7151.jpeg"></a> 

Configure the bridge on a subnet MAAS controls.  You may use any IP mode for the bridge:

<a href="https://discourse.maas.io/uploads/default/original/1X/dd8567ff1cd76606c5ce1751e606fcfab2bc7ce2.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/dd8567ff1cd76606c5ce1751e606fcfab2bc7ce2.jpeg"></a> 

When you're done, it should look something like this:

<a href="https://discourse.maas.io/uploads/default/original/1X/e392d638f0acecb9d54c81bbca4ee17cbcd05445.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/e392d638f0acecb9d54c81bbca4ee17cbcd05445.jpeg"></a> 

Then you can deploy Ubuntu.

snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui  snap-3-0-ui deb-3-0-ui -->

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli  snap-3-0-cli deb-3-0-cli 
<a href="#heading--maas-bridge-cli"><h2 id="heading--maas-bridge-cli">Use the MAAS API to configure a bridge</h2></a>

You can also use the MAAS CLI/API to configure a VM host bridge, with the following procedure:

1. Select the interface you wish to configure the bridge on. This example uses the boot interface, since the boot interface must be connected to a MAAS controlled network -- but any interface is allowed:

        INTERFACE_ID=$(maas $PROFILE machine read $SYSTEM_ID | jq .boot_interface.id)

2. Create the bridge:

         BRIDGE_ID=$(maas $PROFILE interfaces create-bridge $SYSTEM_ID name=br0 parent=$INTERFACE_ID | jq .id)

3. Select the subnet where you want the bridge (this should be a MAAS controlled subnet):

        SUBNET_ID=$(maas $PROFILE subnets read | jq -r '.[] | select(.cidr == "10.0.0.0/24" and .managed == true).id')

4. Connect the bridge to the subnet:

          maas $PROFILE interface link-subnet $SYSTEM_ID $BRIDGE_ID subnet=$SUBNET_ID mode="STATIC" ip_address="10.0.0.101"

snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli  snap-3-0-cli deb-3-0-cli -->

<a href="#heading--maas-bridge-netplan"><h2 id="heading--maas-bridge-netplan">Use netplan to configure a bridge</h2></a>

You can also use netplan to configure a VM host bridge:

Open your netplan configuration file.  This should be in `/etc/netplan`.  It could be called `50-cloud-init.yaml`, `netplan.yaml`, or something else.  Modify the file to add a bridge, using the example below to guide you:

```
network:
    bridges:
        br0:
            addresses:
            - 10.0.0.101/24
            gateway4: 10.0.0.1
            interfaces:
            - enp1s0
            macaddress: 52:54:00:39:9d:f9
            mtu: 1500
            nameservers:
                addresses:
                - 10.0.0.2
                search:
                - maas
            parameters:
                forward-delay: 15
                stp: false
    ethernets:
        enp1s0:
            match:
                macaddress: 52:54:00:39:9d:f9
            mtu: 1500
            set-name: enp1s0
        enp2s0:
            match:
                macaddress: 52:54:00:df:87:ac
            mtu: 1500
            set-name: enp2s0
        enp3s0:
            match:
                macaddress: 52:54:00:a7:ac:46
            mtu: 1500
            set-name: enp3s0
    version: 2
```

Apply the new configuration with `netplan apply`.

<a href="#heading--maas-bridge-libvirt"><h2 id="heading--maas-bridge-libvirt">Use libvirt to configure a bridge</h2></a>

It is also possible to use [libvirt](https://ubuntu.com/server/docs/virtualization-libvirt) to configure a virtual bridge.  This method will also work for LXD VM hosts running on Ubuntu.  Be aware that other methods may be required if you are configuring LXD on an OS other than Ubuntu.

By default, libvirt creates a virtual bridge, `virbr0`, through which VMs communicate with each other and the Internet. DHCP, supplied by libvirt, automatically assigns an IP address to each VM.  However, to enable network booting in MAAS, you’ll need to provide DHCP in MAAS and either:

1.  Disable DHCP on libvirt’s `default` network, or
2.  Create a new libvirt network `maas` with DHCP disabled.

You can set up such a `maas` network like this:

``` bash
cat << EOF > maas.xml
<network>
 <name>maas</name>
 <forward mode='nat'>
   <nat>
     <port start='1024' end='65535'/>
   </nat>
 </forward>
 <dns enable="no" />
 <bridge name='virbr1' stp='off' delay='0'/>
 <domain name='testnet'/>
 <ip address='172.16.99.1' netmask='255.255.255.0'>
 </ip>
</network>
EOF
virsh net-define maas.xml
```

Note that this network also has NAT port forwarding enabled to allow VMs to communicate with the Internet at large. Port forwarding is very useful in test environments.

<a href="#heading--set-up-ssh"><h2 id="heading--set-up-ssh">Set up SSH</h2></a>

For MAAS to successfully communicate with libvirt on your VM host machine -- whether you're running from snap or package, or running rack controllers in LXD containers or on localhost -- this example command must succeed from every rack controller:

``` bash
virsh -c qemu+ssh://$USER@$VM_HOST_IP/system list --all
```

Here, `$USER` is a user on your VM host who is a member of the `libvirtd` Unix group on the VM host, and `$VM_HOST_IP` is the IP of your VM host.  **Note** that insufficient permissions for `$USER` may cause the `virsh` command to fail with an error such as `failed to connect to the hypervisor`. Check the `$USER` group membership to make sure `$USER` is a member of the `libvirtd` group.

<!-- deb-2-7-ui deb-2-7-cli deb-2-8-ui deb-2-8-cli deb-2-9-ui deb-2-9-cli deb-3-0-cli deb-3-0-ui  
<a href="#heading--libvirt-ssh"><h3 id="heading--libvirt-ssh">Set up SSH (libvirt only)</h3></a>

The `maas` user on your rack controllers will issue all libvirt commands. Therefore, you'll need to set up SSH public keys on every rack controller for user `maas`.  First create SSH keys on all rack controllers:

``` bash
$ sudo -i
root@maas:~$ mkdir -p /var/snap/maas/current/root/.ssh
root@maas:~$ cd /var/snap/maas/current/root/.ssh
root@maas:~$ ssh-keygen -f id_rsa
```

Next, add the contents of `~maas/.ssh/id_rsa.pub` to the VM host user's `~$USER/.ssh/authorized_keys`. To accomplish this, log into your VM host node, via SSH, from a host for which MAAS has a matching public SSH key.
 deb-2-7-ui deb-2-7-cli deb-2-8-ui deb-2-8-cli deb-2-9-ui deb-2-9-cli deb-3-0-ui deb-3-0-cli -->

<!-- snap-2-7-ui snap-2-7-cli snap-2-8-ui snap-2-8-cli snap-2-9-ui snap-2-9-cli snap-3-0-ui snap-3-0-cli 
<a href="#heading--set-up-ssah-lv"><h3 id="heading--set-up-ssah-lv">Set up SSH (libvirt only)</h3></a>

If you installed MAAS via snap, then create the needed SSH keys this way:

``` bash
sudo mkdir -p /var/snap/maas/current/root/.ssh
cd /var/snap/maas/current/root/.ssh
sudo ssh-keygen -f id_rsa
```

Finally, you'll need to add `id_rsa.pub` to the `authorized_keys` file in `/home/<vm-host-user-homedir-name>/.ssh/`,  where `<vm-host-user-homedir-name>` is the name of your VM host user.
 snap-2-7-ui snap-2-7-cli snap-2-8-ui snap-2-8-cli snap-2-9-ui snap-2-9-cli snap-3-0-ui snap-3-0-cli -->

<!-- snap-2-8-ui snap-2-8-cli deb-2-8-ui deb-2-8-cli snap-2-9-ui snap-2-9-cli deb-2-9-ui deb-2-9-cli snap-3-0-cli snap-3-0-ui deb-3-0-cli deb-3-0-ui
<a href="#heading--lxd-setup"><h2 id="heading--lxd-setup">Make LXD available for VM hosting</h2></a>

Assuming that you want to use LXD VM hosts, you need to install the correct version of LXD. Prior to the release of Ubuntu 20.04 LXD was installed using Debian packages. The Debian packaged version of LXD is too old to use with MAAS. If this is the case, you’ll need to remove the LXD Debian packages and install the Snap version.  Note that you cannot install both Debian and snap versions, as this creates a conflict.

<a href="#heading--reinstalling-lxd"><h3 id="heading--reinstalling-lxd">Removing older versions of LXD</h3></a>

If you're on a version of Ubuntu older than 20.04, or you have the Debian version of LXD, start the uninstall process with the following command:

``` bash
sudo apt-get purge -y *lxd* *lxc*
```

This command should result in output that looks something like this:

``` bash
Reading package lists... Done
Building dependency tree      
Reading state information... Done
Note, selecting 'lxde-core' for glob '*lxd*'
Note, selecting 'python-pylxd-doc' for glob '*lxd*'
Note, selecting 'python3-pylxd' for glob '*lxd*'
Note, selecting 'python-nova-lxd' for glob '*lxd*'
Note, selecting 'lxde-common' for glob '*lxd*'
Note, selecting 'lxde-icon-theme' for glob '*lxd*'
Note, selecting 'lxde-settings-daemon' for glob '*lxd*'
Note, selecting 'lxde' for glob '*lxd*'
Note, selecting 'lxdm' for glob '*lxd*'
Note, selecting 'lxd' for glob '*lxd*'
Note, selecting 'lxd-tools' for glob '*lxd*'
Note, selecting 'python-pylxd' for glob '*lxd*'
Note, selecting 'lxdm-dbg' for glob '*lxd*'
Note, selecting 'lxde-session' for glob '*lxd*'
Note, selecting 'nova-compute-lxd' for glob '*lxd*'
Note, selecting 'openbox-lxde-session' for glob '*lxd*'
Note, selecting 'python-nova.lxd' for glob '*lxd*'
Note, selecting 'lxd-client' for glob '*lxd*'
Note, selecting 'openbox-lxde-session' instead of 'lxde-session'
Note, selecting 'lxctl' for glob '*lxc*'
Note, selecting 'lxc-common' for glob '*lxc*'
Note, selecting 'python3-lxc' for glob '*lxc*'
Note, selecting 'libclxclient-dev' for glob '*lxc*'
Note, selecting 'lxc-templates' for glob '*lxc*'
Note, selecting 'lxc1' for glob '*lxc*'
Note, selecting 'lxc-dev' for glob '*lxc*'
Note, selecting 'lxc' for glob '*lxc*'
Note, selecting 'liblxc1' for glob '*lxc*'
Note, selecting 'lxc-utils' for glob '*lxc*'
Note, selecting 'vagrant-lxc' for glob '*lxc*'
Note, selecting 'libclxclient3' for glob '*lxc*'
Note, selecting 'liblxc-dev' for glob '*lxc*'
Note, selecting 'nova-compute-lxc' for glob '*lxc*'
Note, selecting 'python-lxc' for glob '*lxc*'
Note, selecting 'liblxc-common' for glob '*lxc*'
Note, selecting 'golang-gopkg-lxc-go-lxc.v2-dev' for glob '*lxc*'
Note, selecting 'lxcfs' for glob '*lxc*'
Note, selecting 'liblxc-common' instead of 'lxc-common'
Package 'golang-gopkg-lxc-go-lxc.v2-dev' is not installed, so not removed
Package 'libclxclient-dev' is not installed, so not removed
Package 'libclxclient3' is not installed, so not removed
Package 'lxc-templates' is not installed, so not removed
Package 'lxctl' is not installed, so not removed
Package 'lxde' is not installed, so not removed
Package 'lxde-common' is not installed, so not removed
Package 'lxde-core' is not installed, so not removed
Package 'lxde-icon-theme' is not installed, so not removed
Package 'lxde-settings-daemon' is not installed, so not removed
Package 'lxdm' is not installed, so not removed
Package 'lxdm-dbg' is not installed, so not removed
Package 'openbox-lxde-session' is not installed, so not removed
Package 'python-lxc' is not installed, so not removed
Package 'python3-lxc' is not installed, so not removed
Package 'vagrant-lxc' is not installed, so not removed
Package 'liblxc-dev' is not installed, so not removed
Package 'lxc-dev' is not installed, so not removed
Package 'nova-compute-lxc' is not installed, so not removed
Package 'nova-compute-lxd' is not installed, so not removed
Package 'python-nova-lxd' is not installed, so not removed
Package 'python-pylxd' is not installed, so not removed
Package 'python-pylxd-doc' is not installed, so not removed
Package 'lxc' is not installed, so not removed
Package 'lxc-utils' is not installed, so not removed
Package 'lxc1' is not installed, so not removed
Package 'lxd-tools' is not installed, so not removed
Package 'python-nova.lxd' is not installed, so not removed
Package 'python3-pylxd' is not installed, so not removed
The following packages were automatically installed and are no longer required:
  dns-root-data dnsmasq-base ebtables libuv1 uidmap xdelta3
Use 'sudo apt autoremove' to remove them.
The following packages will be REMOVED:
  liblxc-common* liblxc1* lxcfs* lxd* lxd-client*
0 upgraded, 0 newly installed, 5 to remove and 21 not upgraded.
pAfter this operation, 34.1 MB disk space will be freed.
(Reading database ... 67032 files and directories currently installed.)
Removing lxd (3.0.3-0ubuntu1~18.04.1) ...
Removing lxd dnsmasq configuration
Removing lxcfs (3.0.3-0ubuntu1~18.04.2) ...
Removing lxd-client (3.0.3-0ubuntu1~18.04.1) ...
Removing liblxc-common (3.0.3-0ubuntu1~18.04.1) ...
Removing liblxc1 (3.0.3-0ubuntu1~18.04.1) ...
Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
Processing triggers for libc-bin (2.27-3ubuntu1) ...
(Reading database ... 66786 files and directories currently installed.)
Purging configuration files for liblxc-common (3.0.3-0ubuntu1~18.04.1) ...
Purging configuration files for lxd (3.0.3-0ubuntu1~18.04.1) ...
Purging configuration files for lxcfs (3.0.3-0ubuntu1~18.04.2) ...
Processing triggers for systemd (237-3ubuntu10.40) ...
Processing triggers for ureadahead (0.100.0-21) ...
```

You should also autoremove packages no longer needed by LXD:

``` bash
$ sudo apt-get autoremove -y
```

Output from this command should be similar to:

``` bash
Reading package lists... Done
Building dependency tree      
Reading state information... Done
The following packages will be REMOVED:
  dns-root-data dnsmasq-base ebtables libuv1 uidmap xdelta3
0 upgraded, 0 newly installed, 6 to remove and 21 not upgraded.
After this operation, 1860 kB disk space will be freed.
(Reading database ... 66769 files and directories currently installed.)
Removing dns-root-data (2018013001) ...
Removing dnsmasq-base (2.79-1) ...
Removing ebtables (2.0.10.4-3.5ubuntu2.18.04.3) ...
Removing libuv1:amd64 (1.18.0-3) ...
Removing uidmap (1:4.5-1ubuntu2) ...
Removing xdelta3 (3.0.11-dfsg-1ubuntu1) ...
Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
Processing triggers for libc-bin (2.27-3ubuntu1) ...
```

Now install LXD from the Snap:

``` bash
$ sudo snap install lxd
2020-05-20T22:02:57Z INFO Waiting for restart...
lxd 4.1 from Canonical✓ installed
```

<a href="#heading--newer-lxd"><h3 id="heading--newer-lxd">Refreshing LXD on 20.04</h3></a>

If you are on 20.04 or above LXD should be installed by default, but it's a good idea to make sure it's up to date:

``` bash
$ sudo snap refresh
All snaps up to date.
```

<a href="#heading--lxd-init"><h3 id="heading--lxd-init">Initialise LXD prior to use</h3></a>

Once LXD is installed it needs to be configured with `lxd init` before first use:

``` bash
$ sudo lxd init
```

Your interactive output should look something like the following. Note a few points important points about these questions:

1. `Would you like to use LXD clustering? (yes/no) [default=no]: no` - MAAS does not currently support LXD clusters.

2. `Name of the storage back-end to use (btrfs, dir, lvm, zfs, ceph) [default=zfs]: dir` - testing has primarily been with dir; other options should work, but less testing has been done, so use at your own risk.

3. `Would you like to connect to a MAAS server? (yes/no) [default=no]: no` - When LXD is connected to MAAS containers or virtual machines created by LXD will be automatically added to MAAS as devices.  This feature should work, but has limited testing thus far.

4. `Would you like to configure LXD to use an existing bridge or host interface? (yes/no) [default=no]: yes` - The bridge LXD creates is isolated and not managed by MAAS. If this bridge is used, you would be able to add the LXD VM host and compose virtual machines, but commissioning, deploying, and any other MAAS action which uses the network will fail -- so `yes` is the correct answer here.

5. `Name of the existing bridge or host interface: br0` - br0 is the name of the bridge the user configured (see sections above) which is connected to a MAAS-managed network.

6. `Trust password for new clients:` - This is the password the user will enter when connecting with MAAS.


``` bash
Would you like to use LXD clustering? (yes/no) [default=no]: no
Do you want to configure a new storage pool? (yes/no) [default=yes]: yes
Name of the new storage pool [default=default]:  
Name of the storage back-end to use (btrfs, dir, lvm, zfs, ceph) [default=zfs]: dir
Would you like to connect to a MAAS server? (yes/no) [default=no]: no
Would you like to create a new local network bridge? (yes/no) [default=yes]: no
Would you like to configure LXD to use an existing bridge or host interface? (yes/no) [default=no]: yes
Name of the existing bridge or host interface: br0
Would you like LXD to be available over the network? (yes/no) [default=no]: yes
pAddress to bind LXD to (not including port) [default=all]:
Port to bind LXD to [default=8443]:
Trust password for new clients:
Again:
Would you like stale cached images to be updated automatically? (yes/no) [default=yes]
Would you like a YAML "lxd init" preseed to be printed? (yes/no) [default=no]:
```

After initialising LXD, you will also want to make sure that LXD is not trying to provide DHCP for the new local network bridge.  You can check this with the following command:

```
lxc network show lxdbr0
```

If you didn't accept the default bridge name (lxdbr0), substitute your name for that new bridge in the command above. This will produce output something like this:

```
config:
  dns.mode: managed
  ipv4.address: 10.146.214.1/24
  ipv4.dhcp: "true"
  ipv4.nat: "true"
  ipv6.address: fd42:c560:ee59:bb2::1/64
  ipv6.dhcp: "true"
  ipv6.nat: "true"
description: ""
name: lxdbr0
type: bridge
used_by:
- /1.0/profiles/default
managed: true
status: Created
locations:
- none
```

There is a [quick tutorial](https://github.com/lxc/lxd/blob/master/doc/networks.md) on the possible settings here.  For simplicity, to turn off LXD-provided DHCP, you need to change three settings, as follows:

```
lxc network set lxdbr0 dns.mode=none
lxc network set lxdbr0 ipv4.dhcp=false
lxc network set lxdbr0 ipv6.dhcp=false
```

You can check your work by repeating the `show` command:

```
$ lxc network show lxdbr0
config:
  dns.mode: none
  ipv4.address: 10.146.214.1/24
  ipv4.dhcp: "false"
  ipv4.nat: "true"
  ipv6.address: fd42:c560:ee59:bb2::1/64
  ipv6.dhcp: "false"
  ipv6.nat: "true"
description: ""
name: lxdbr0
type: bridge
used_by:
- /1.0/profiles/default
managed: true
status: Created
locations:
- none
```

Once that's done, the LXD host is now ready to be added to MAAS as an LXD VM host. Upon adding the VM host, its own commissioning information will be refreshed.

When composing a virtual machine with LXD, MAAS uses either the 'maas' LXD profile, or (if that doesn't exist) the 'default' LXD profile. The profile is used to determine which bridge to use. Users may also add additional LXD options to the profile which are not yet supported in MAAS.

 snap-2-8-ui snap-2-8-cli deb-2-8-ui deb-2-8-cli snap-2-9-ui snap-2-9-cli deb-2-9-ui deb-2-9-cli snap-3-0-ui snap-3-0-cli deb-3-0-ui deb-3-0-cli  -->


