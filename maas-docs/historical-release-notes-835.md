<h2 id="heading--2-7">2.7</h2>

If you are using the MAAS 2.6 snap, which had to be installed with `--devmode`, you can update to 2.7 with the following parameters:

    snap refresh maas --devmode --channel=2.7

Be aware that you will still be in `--devmode`, which means the snap won't automatically upgrade.  You'll have to check manually for updates (via `snap refresh`).  Once you’re upgraded to MAAS 2.7 using this method, future snap updates won’t require the devmode parameter. So, for example, when a later version of 2.7 (or even 2.8) is released, you will be able to `snap refresh` to those channels and get out of devmode.  Once refreshed out of devmode in this way, you'll get updates for point releases automatically.

An alternative to avoid devmode would be to do a clean install of MAAS 2.7, that is, removing 2.6 with `snap remove maas` and reinstalling MAAS 2.7 with:

    snap install --channel=2.7 maas

Note that you can check the devmode status of your snap with:

    snap list maas


---

Following on from MAAS 2.6.2, we are happy to announce that MAAS 2.7 is now available. This release features some critical bug fixes, along with some exciting new features:

## CentOS 8 image support

Users can now deploy CentOS 8 images in MAAS. The Images page in the MAAS UI will now offer a choice to select and download CentOS 8. Note that users of previous versions may see CentOS 8 as an available option, but cannot download or deploy it.

## Network testing features

MAAS 2.7 brings a slate of new network testing and link detection features, as detailed below.

### Network link disconnect detection

MAAS 2.7 can check whether links are connected or disconnected. Previously, when commissioning, you couldn’t detect unplugged cables. Now you can. You will have to take a couple of steps for existing MAAS deployments: First, you will have to upgrade to 2.7, then run commissioning again to see if a link is disconnected. But you no longer have to puzzle over what’s broken when this happens.

MAAS will report disconnected network cables, and users will receive a warning when trying to configure a disconnected interface. Administrators will be able to change cable connection status through both API and UI after manually rectifying the situation.

### Slow network link detection

MAAS 2.7 makes sure you’re getting the most out of your link speed. As servers and hardware get faster — 10G, 40G, even 100G NICS — the chances increase that you might plug your 10G NIC into a 1G switch, for example. Previously, with MAAS, you’d be stuck with the speed of the slowest link, but there wasn’t a way to verify your link speed without recommissioning. Depending on your physical hardware, that might still be an issue, but the MAAS UI can now warn you if your interface is connected to a link slower than what the interface supports. And all information shown in the UI is available via the API, as well. You can still replace a slow switch without recommissioning.

MAAS will automatically detect link and interface speed during commissioning and report them via the API/UI. Administrators will be able to change or update the link and interface speeds via the API/UI after manual changes to the connection. MAAS 2.7 will also report link speed, allowing users to filter and list machines by their link speed in the UI. Users can also employ this information to allocate machines by their link speed in the API.

### Network validation scripts and testing

MAAS 2.7 allows you to configure network connectivity testing in a number of ways. If you’ve used MAAS, you know that if it can’t connect to the rack controller, deployment can’t complete. Now MAAS can check connectivity to the rack controller and warn you if there’s no link, long before you have to try and debug it. For example, if you can’t connect to your gateway controller, traffic can’t leave your network. MAAS can now check this link and recognise that there’s no connectivity, which alleviates a lot of annoying (and sometimes hard-to-detect) network issues.

Users can now test their network configuration to check for:

* Interfaces which have a broken network configuration
* Bonds that are not fully operational
* Broken gateways, rack controllers, and Internet links

In addition, Internet connectivity testing has been greatly expanded. Previously, MAAS gave a yes/no link check during network testing. Now you can give a list of URLs or IP addresses to check. In the ephemeral environment, standard DHCP is still applied, but when network testing runs, we can apply your specific configuration for the duration of the test. While all URLs / IPs are tested with all interfaces, we do test each of your interfaces individually, including breaking apart bonded NICS and testing each side of your redundant interfaces. You can also run different tests on each pass, e.g., a different set of URLs, although each run would be a different testing cycle. For testing individual interfaces, you can use the API.

Of course, the main network feature available in 2.7 is improved — and customisable — network testing. You can now create your own commissioning scripts and tests related to networking. You can create your own network tests (e.g., a network throughput test) and run them during the network testing portion of the MAAS workflow. There are no particular restrictions on these scripts, so you can test a wide variety of possible conditions and situations.

Administrators can upload network tests and test scripts, as well as create tests which accept an interface parameter, or scripts which apply custom network configurations. Users can then specify (unique) parameters using the API, override machines which fail network testing (allowing their use), and suppress individual failed network tests. All users benefit from enhanced reporting, as they are now able to see the overall status of all interfaces via the API, the UI Machine list, and the UI Interfaces tab; review the health status from all interface tests; and view the interface test results by interface name and MAC.

### Live IP address detection to prevent address conflicts

In some cases, MAAS connects with subnet which are not empty. Normally, the user has to tell MAAS about IP addresses which are already assigned on that subnet, and if that step is skipped, MAAS may assign and in-use IP address to one of the machines under its control, leading to an IP conflict.

MAAS 2.7 alleviates this problem by detecting IPs in use on a subnet, so that it can avoid assigning that IP to a MAAS-managed machine. The system is not perfect; for example, if NIC on a subnet-connected machine is in a quiescent state -- or turned off -- MAAS may not detect it before duplicating the IP. Note that at least one rack controller must have access to the previously-assigned machine in order for this feature to work. MAAS 2.7 will also recognise when the subnet ARP cache is full and re-check the oldest IPs added to the cache to search for free IP addresses.

## Introductory NUMA / SR-IOV support

NUMA (Non-Uniform Memory Access) is a useful way of achieving high-efficiency computing, by pairing a CPU core with a very fast connection to RAM and PCI buses. Typically the CPU socket and the closest banks of DIMM constitute a NUMA node. Obviously, if you’re deploying a MAAS machine under NUMA to get maximum performance, you would like for that machine to be confined to a single NUMA node. MAAS 2.7 introduces this capability.

MAAS will display the NUMA node index and details. Users can also see the count of available NUMA nodes, along with CPU cores, memory, NICS, and node spans for bonds and block devices (although node-spanning may not produce suitable performance). From a reporting standpoint, users can filter machines by CPU cores, memory, subnet, VLAN, fabric, space, storage, and RAID.

Similarly, the SR-IOV (Single Root I/O Virtualisation) allows a PCIe device (e.g, a NIC) to appear to be multiple separate devices. A network adaptor can be subdivided into multiple adaptors by adding a Virtual Function (VF). MAAS 2.7 supports the use of multiple VF adaptors to intelligently use SR-IOV edge clouds, by allowing users to see that a NIC supports SR-IOV, along with the supported VF counts.

The goal of this feature is to help users choose the right machine to deploy an edge cloud.

## Settings and user preferences redesign

As part of our efforts to make the UI faster and more responsive, we have completely redesigned the Settings and User preferences within the MAAS UI.

## Strictly-confined Snap support

With 2.7, MAAS is fully confined within the Snap container. No need for installation qualifiers (such as “--devmode”) to permit use of external resources, i.e., outside the Snap container. This means that we will begin to transition to recommending the Snap install as the default (and primary) MAAS install method. This also means that MAAS now gains the benefit of confined snap security features.

## Update to hardware information gathering methods

MAAS has switched hardware information gathering from lshw/lsblk to lxd output during commissioning, because it more easily provides the information needed to complete resource discovery. Note that this information may not be particularly reliable for your use, so you may need to create your own commissioning scripts if you need something more detailed or specific.

## Bug fixes

A number of bug fixes (see the [list in Launchpad (external link)](https://bugs.launchpad.net/maas/+bugs?field.milestone%3Alist=87757&field.milestone%3Alist=89662&field.milestone%3Alist=89714&field.milestone%3Alist=89840&field.milestone%3Alist=89954&field.milestone%3Alist=89682&field.status%3Alist=FIXRELEASED)).

<h2 id="heading--270">2.6</h2>

See [2.6 release notes](https://discourse.maas.io/t/whats-new-in-maas-2-6/1305) for details on the 2.6 release tree.

<h2 id="heading--240">2.4.0</h2>

<h3 id="heading--important-announcements">Important announcements</h3>

<h4 id="heading--dependency-on-tgt-iscsi-has-been-dropped">Dependency on tgt (iSCSI) has been dropped</h4>

MAAS 2.3 moved away from using iSCSI to run ephemeral environments and deployments, adding the ability to perform the same functions with a *squashfs* image. While this removed the requirement for *tgt*, the dependency wasn't dropped from 2.3. As of 2.4, however, tgt has been completely removed.

<h4 id="heading--apache2-dependency-dropped-from-debian-packages">Apache2 dependency dropped from Debian packages</h4>

MAAS 2.0 changed the web UI to port 5240 and deprecated the use of port 80. However, so as to not break deployments when upgrading from the previous LTS release, MAAS continued to have *apache2* as a dependency. This was purely to provide a reverse proxy to allow users to connect via port 80.

The availability of the MAAS *snap* changes that behaviour, no longer providing web UI access on port 80. To remain consistent with the snap, the Debian package removes its dependency on *apache2* and drops proxy access via port 80.

<h4 id="heading--debian-package-maas-dns-no-longer-needed">Debian package `maas-dns` no longer needed</h4>

The Debian package, *maas-dns*, has been made a transitional package. This package previously provided some post-installation configuration to prepare *bind* to be managed by MAAS, but it required *maas-region-api* to be installed first.

To streamline the installation and make it easier for users to install MAAS within high-availability environments, the configuration of *bind* has been integrated into the ‘maas-region-api’ package itself. Subsequently, ‘maas-dns’ is now a dummy transitional package that can be removed.

<h4 id="heading--ntp-services-provided-by-chrony">NTP services provided by Chrony</h4>

In common with changes made to Ubuntu Server, *ntpd* has been replaced with [Chrony (external link)](https://chrony.tuxfamily.org/) for the NTP protocol. MAAS will handle the upgrade process automatically and resume NTP service operation.

<h3 id="heading--new-features--improvements">New Features & Improvements</h3>

<h4 id="heading--maas-internals-optimisation">MAAS Internals optimisation</h4>

Major internal surgery to MAAS 2.4 has improved various areas not visible to the user. These updates advance the overall performance of MAAS in larger environments and include:

**Backend improvements**

-   The image download process has been improved to ensure rack controllers start to download images immediately after the region controller has finished downloading images.
-   The service monitor interval has been reduced to 30 seconds. The monitor tracks the status of the various services provided alongside MAAS (DNS, NTP, Proxy).

**AsyncIO based event loop**

-   MAAS has an event loop which performs various internal actions. In older versions of MAAS, the event loop was managed by the default *Twisted* loop. MAAS now uses an AsyncIO based event loop, driven by uvloop, which is targeted at improving internal performance.

**Improved daemon management**

-   MAAS has changed the way daemons are run to allow users to see both *regiond* and *rackd* as processes in the process list.
-   As part of these changes, regiond workers are now managed by a master regiond process. In older versions of MAAS, each worker was directly run by systemd. The master process is now in charge of ensuring workers are running at all times, re-spawning new workers in case of failures. This also allows users to see the worker hierarchy in the process list.

**Ability to increase the number of regiond workers**

-   Following the improved way MAAS daemons are run, further internal changes have been made to allow the number of regiond workers to be increased automatically. This allows MAAS to scale to handle an increased number of internal operations in larger environments.

**Database query optimisation**

Internal improvements have been made to reduce the footprint and number of database queries. Some areas that have been addressed in this release include:

-   When saving node objects (e.g. making any update of a machine, device, rack controller, etc), MAAS validated changes across various fields. This required an increased number of queries for fields, even when they were not being updated. MAAS now tracks specific fields that change and only performs queries for those fields. For example, to update a power state, MAAS would perform 11 queries. After these improvements, only 1 query is now performed.
-   On every transaction, MAAS performed 2 queries to update the timestamp. This has now been consolidated into a single query per transaction.
-   Further reductions in the number of database queries have been made, significantly cutting the queries made by the boot source cache image import process from over 100 to just under 5. These changes greatly improve MAAS performance and database utilisation in larger environments. More improvements will continue to be made as we continue to examine various areas in MAAS.

**UI optimisation**

MAAS has been optimised to reduce the amount of data loaded in the WebSocket API to render the UI. This is targeted at only processing data for viewable information, improving various legacy areas. The work done in this area includes:

-   Various web UI performance improvements include better filtering of node types for machines, pods and zones.
-   Script results are only loaded for viewable nodes in the machine listing page, reducing the overall amount of data loaded.
-   The node object is updated in the WebSocket only when something has changed in the database, reducing the data transferred to the clients as well as the amount of internal queries.
-   Only load historic script results (e.g. old commissioning/testing results) when requested / accessed by the user, instead of always making them available over the websocket.
-   Only load node objects in listing pages when the specific object type is requested. For instance, only load machines when accessing the machines tab instead of also loading devices and controllers.
-   Change the UI mechanism to only request OS details only on initial page load rather than every 10 seconds.

<h4 id="heading--kvm-pod-improvements">KVM pod improvements</h4>

KVM pods were initially created to help developers quickly iterate and test new functionality while developing MAAS. But KVM pods have also become an essential tool for administrators, allowing them to make better use of resources across the data centre. As KVM pods were initially targeted at developers, MAAS lacked features more useful for administrators. MAAS 2.4 rectifies these shortcomings with the following improvements:

**Pod AZs**

-   The physical zone for a pod can now be defined. This helps administrators by conceptually placing KVM pods in an AZ, enabling them to request/allocate machines on demand based on its AZ. All VMs created from a pod will inherit the AZ.

**Pod tagging**

-   MAAS now adds the ability to set tags for a pod. This allows administrators to use tags to allow/prevent the creation of a VM inside the pod using tags. For example, if the administrator would like a machine with a ‘tag’ named ‘virtual’, MAAS will filter all physical machines and only consider other VMs or a KVM pod for machine allocation.

**Added over-commit ratios for CPU and memory.**

-   When composing or allocating machines, previous versions of MAAS allow the user to request resources regardless of resource availability. This caused problems when dynamically allocating machines as it allowed users to create an infinite number of machines when the physical host was over committed. This new feature allows administrators to control the amount of resources they want to over commit.

**Added filter for which pods or pod types to avoid when allocating machines,**

-   Provides users with the ability to select which pods, or pod types, *not* to allocate resources from. This makes it particularly useful when dynamically allocating machines when MAAS has a large number of pods.

**Define a default storage pool**

-   This feature allows users to select the default storage pool to use when composing machines, in case multiple pools have been defined. Otherwise, MAAS will pick the storage pool automatically, depending which pool has the most available space.

**Allow machines to be allocated with different storage pools**

-   From the API, you can now request a machine with multiple storage devices from different storage pools. This feature uses storage tags to automatically map a storage pool in *libvirt* with a storage tag in MAAS.

<h4 id="heading--ntp-services-now-provided-by-chrony">NTP services now provided by Chrony</h4>

In common with changes made to Ubuntu Server, *ntpd* has been replaced with Chrony for the NTP protocol. MAAS will handle the upgrade process automatically and resume NTP service operation.

-   MAAS will configure chrony as peers on all Region Controllers
-   MAAS will configure chrony as a client of peers for all Rack Controllers
-   Machines will use the Rack Controllers as they do today

<h4 id="heading--machine-locking">Machine locking</h4>

MAAS adds the ability to lock machines, preventing the user from performing actions that could change their state. This gives MAAS a prevention mechanism for potentially catastrophic actions. For example, it prevents powering off machines by mistake, or releasing machines that could bring workloads down.

<h4 id="heading--audit-logging">Audit logging</h4>

With the introduction of audit logging, MAAS 2.4 allows the administrators to audit the user’s actions.

The audit logs are available to administrators via the MAAS CLI/API, giving administrators a centralised location to access these logs.

See [Audit Event Logs](/t/audit-event-logs/791) for further details.

<h4 id="heading--commissioning-harness">Commissioning Harness</h4>

**Support for firmware upgrades and hardware specific scripts**

The *commissioning harness* has been expanded with various improvements to help administrators write their own firmware upgrades and hardware specific scripts. These improvements addresses some of the challenges administrators face when performing such tasks at scale.

Improvements include:

-   auto-select all firmware upgrade/storage hardware changes (API only, UI will be available soon)
-   write and run scripts for specific hardware
-   reboot machines from the commissioning environment without disrupting the commissioning process

These improvements allow administrators to:

-   target specific hardware specific by specifying PCI ID, modalias, vendor or model of the machine or device
-   use script metadata to create firmware upgrade scripts that require a reboot before the machine finishes the commissioning process
-   define where a script can obtain proprietary firmware and/or proprietary tools to perform any operations required.

See [Commissioning and Hardware Testing Scripts](/t/commissioning-and-hardware-testing-scripts/833) for more details.

<h4 id="heading--ui-improvements">UI improvements</h4>

**DNS UI improvements**

MAAS 2.0 introduced the ability to manage DNS and to create resources records such as A, AAA and CNAME. However, as the UI only supported adding and removing domains, most of this functionality was only available via the API.

This release adds the ability to manage not only DNS domains but also the following resource records within the web UI:

-   Edit domains (e.g. TTL, name, authoritative).
-   Create and delete resource records (A, AAA, CNAME, TXT, etc).
-   Edit resource records.

**YUI finally dropped in favour of AngularJS**

-   MAAS has now fully dropped the use of [YUI (external link)](https://en.wikipedia.org/wiki/YUI_Library) for the web UI. The final sections using this were the Settings and login pages. Both have now been transitioned to use AngularJS instead.

**Vanilla framework upgrade**

We would like to thank the Ubuntu web team for their continued hard work upgrading MAAS to the latest version of the Vanilla framework. MAAS is looking better and more consistent every day!

**Navigation UI improvements**

Top-level navigation has now changed to:

-   *Zones* renamed to *AZs* (Availability Zones).
-   *Machines*, *Devices* and *Controllers* have been moved from *Hardware* to the top-level menu.

**Settings page reorganisation**

-   The web UI MAAS setting pages have been reorganised into tabs, making configuration options easier to find.

<h4 id="heading--other-improvements">Other improvements</h4>

Other notable improvements in MAAS 2.4 include:

**IPMI machines boot type can now be forced**

Hardware manufactures have been upgrading their BMC firmware versions to be more compliant with the Intel IPMI 2.0 spec. Unfortunately, the IPMI 2.0 spec has made changes that provide a non-backward compatible user experience. For example, if the administrator configures their machine to always PXE boot over EFI, and the user executes an IPMI command without specifying the boot type, the machine would use the value of the configured BIOS. However, with these new changes, the user is required to always specify a boot type, avoiding a fallback to the BIOS.

As such, MAAS now allows the selection of a boot type (auto, legacy, EFI) to force the machine to always PXE-boot with the desired type (on the next boot only) .

**API to Skip BMC configuration on commissioning**

The API now provides an option to skip BMC auto-configuration during commissioning for IPMI systems. This option helps admins keep the credentials provided over the API when adding new nodes.

**Gather information about BIOS & firmware**

MAAS now probes for more underlying system details, including the model, serial number, BIOS and firmware of a machine (where available). It also gathers details on storage devices and network interfaces.

**API for default DNS domain selection**

A default DNS domain can now be defined from the API.

<h3 id="heading--bug-fixes">Bug fixes</h3>

For all bug fixes in this release, please refer to all of these milestones (all external links):

-   <https://launchpad.net/maas/+milestone/2.4.0alpha1>
-   <https://launchpad.net/maas/+milestone/2.4.0alpha2>
-   <https://launchpad.net/maas/+milestone/2.4.0beta1>
-   <https://launchpad.net/maas/+milestone/2.4.0beta2>
-   <https://launchpad.net/maas/+milestone/2.4.0beta3>
-   <https://launchpad.net/maas/+milestone/2.4.0rc1>
-   <https://launchpad.net/maas/+milestone/2.4.0rc2>

<h2 id="heading--maas-client-library-python-libmaas">MAAS Client Library (python-libmaas)</h2>

The official Python client library for MAAS is available in the Ubuntu 18.04 LTS package archive or you can download the source from this external link:

<https://github.com/maas/python-libmaas/releases>

Recent updates have added the following features:

-   add/read/update/delete storage devices attached to machines
-   configure partitions and mount points
-   configure bcache
-   configure RAID
-   configure LVM

<h2 id="heading--get-in-touch">Get in touch</h2>

We'd love to hear about how you're using MAAS, whether it's at the smallest of scales or the largest. Our team is always approachable and can usually be found in the following locations:

-   Join us on IRC. We can be found on the [maas (external link)](http://webchat.freenode.net/?channels=maas) channel on [freenode (external link)](https://freenode.net/).
-   Subscribe to the [maas-devel (external link)](https://lists.ubuntu.com/mailman/listinfo/Maas-devel) mailing list, a great place to ask questions.

# 2.3

<h2 id="heading--important-announcements">Important announcements</h2>

<h3 id="heading--machine-network-configuration-now-deferred-to-cloud-init">Machine network configuration now deferred to cloud-init</h3>

Machine network configuration is now handled by cloud-init.

With previous versions of MAAS (and curtin), network configuration was performed directly by curtin during the installation process. In an effort to improve robustness, this network configuration has been consolidated with cloud-init.

MAAS continues to pass network configuration to curtin which in turn delegates the configuration to cloud-init.

<h3 id="heading--ephemeral-images-over-http">Ephemeral images over HTTP</h3>

To reduce the number of dependencies and improve reliability, MAAS ephemeral (network boot) images are no longer loaded using iSCSI (tgt). By default, these images are now obtained using HTTP requests to the rack controller.

After upgrading to MAAS 2.3, please ensure you have the latest available images. For more information please refer to Ephemeral images now use HTTP below.

<h3 id="heading--centos-and-windows-advanced-network-configuration">CentOS and Windows advanced network configuration</h3>

MAAS 2.3 now supports the ability to perform network configuration for CentOS and Windows via cloud-init. The MAAS CentOS images now use the latest available version of cloud-init to support these features.

<h2 id="heading--new-features-and-improvements">New features and improvements</h2>

<h3 id="heading--centos-network-configuration">CentOS network configuration</h3>

MAAS now performs machine network configuration for CentOS 6 and 7, providing those operating systems with networking feature parity with Ubuntu.

The following can now be configured for MAAS deployed CentOS images:

-   Bonds, VLAN and bridge interfaces.
-   Static network configuration.

Our thanks to the cloud-init team for improving the network configuration support for CentOS.

<h3 id="heading--windows-network-configuration">Windows network configuration</h3>

MAAS can now configure NIC teaming (bonding) and VLAN interfaces for Windows deployments. This uses the native NetLBFO in Windows 2008+.

Contact us for more information.

<h3 id="heading--improved-hardware-testing">Improved hardware testing</h3>

MAAS 2.3 introduces a new hardware testing framework that significantly improves the granularity and provision of hardware testing feedback. These improvements include:

-   **Run individual tests**. The new framework allows MAAS to run each component individually. This enables MAAS to run tests against storage devices, for example, and capture results separately.
-   **Define a custom testing script with a YAML definition**. The ability to describe custom hardware tests with a YAML definition enables MAAS do the following:
    -   Collate details about the tests, such as script name, description, required packages, and other metadata about what information the script will gather. All of which will be used by MAAS to render in the UI.
    -   Determine whether the test supports a parameter, such as storage, that lets the test to be run against individual storage devices.
    -   The option to run tests in parallel.
-   **Performance metrics**. Capture performance metrics for the tests that can provide them:
    -   CPU performance now offers a new *7zip* test which includes metrics.
    -   Storage performance now include a new *fio* test with metrics.
    -   The storage test *badblocks* has been improved to provide the number of badblocks found as a metric.
-   **Failed testing override**. The ability to override a machine that has been marked ‘Failed testing’. This allows administrators to acknowledge that a machine is usable despite it having failed testing.

Hardware testing improvements include the following web UI changes:

-   **Machine Listing page**:
    -   Displays whether a test is pending, running or failed for the machine components (CPU, Memory or Storage.)
    -   Displays whether a test not related to CPU, Memory or Storage has failed.
    -   Displays a warning when the machine has been overridden and has failed tests but is in a ‘Ready’ or ‘Deployed’ state.
-   **Machine Details page**:
    -   The *Summary tab* now provides hardware testing information about the different components (CPU, Memory, Storage).
    -   The *Hardware Tests /Commission tab* now displays an improved view of the latest test run, its run time as well as an improved view of previous results. It also adds more detailed information about specific tests, such as status, exit code, tags, runtime and logs/output (such as stdout and stderr).
    -   The *Storage tab* now displays the status of specific disks, including whether a test is OK or failed after running hardware tests.

For more information, please refer to this external link:  <https://docs.ubuntu.com/maas/2.3/en/nodes-hw-testing>

<h3 id="heading--network-discovery-and-beaconing">Network discovery and beaconing</h3>

In order to confirm network connectivity and aide with the discovery of VLANs, fabrics and subnets, MAAS 2.3 introduces network beaconing.

MAAS now sends out encrypted beacons to facilitate network discovery and monitoring. Beacons are sent using IPv4 and IPv6 multicast (and unicast) to UDP port 5240.

When registering a new controller, MAAS uses the information gathered from the beaconing protocol to ensure that newly registered interfaces on each controller are associated with existing known networks in MAAS.

Using network beaconing, MAAS can better correlate which networks are connected to its controllers, even if interfaces on those controllers are not configured with IP addresses.

Future uses for beaconing could include validation of networks from commissioning nodes, MTU verification and a better user experience when registering new controllers.

<h3 id="heading--upstream-proxy">Upstream proxy</h3>

MAAS 2.3 enables an upstream HTTP proxy to allow MAAS-deployed machines to continue to use a caching proxy for repositories. This provides greater flexibility for closed environments, including:

-   Enabling MAAS itself to use a corporate proxy while allowing machines to continue to use the MAAS proxy.
-   Allowing machines that don’t have access to a corporate proxy to gain network access using the MAAS proxy.

Upstream proxy support includes an improved configuration pane on the settings page. See *Settings &gt; Proxy* for more details.

<h3 id="heading--ephemeral-images-now-use-http">Ephemeral images now use HTTP</h3>

Historically, MAAS used tgt to provide images over iSCSI for the ephemeral environments (such as during commissioning, the deployment environment and rescue mode). MAAS 2.3 changes the default behaviour by now providing images over HTTP instead.

This change means that *initrd* (run via PXE) will contact the rack controller to download the image to load in the ephemeral environment directly.

Support for using 'tgt' is being phased out in MAAS 2.3 and will no longer be supported from MAAS 2.4 onward.

Users who would like to continue to use and load their ephemeral images via 'tgt' they can disable http boot with the following command.

``` bash
maas $PROFILE maas set-config name=http_boot value=False
```

<h3 id="heading--usability-improvements-web-ui">Usability improvements (web UI)</h3>

Alongside the UI improvements outlined above, MAAS 2.3 introduces an improved web UI design for the machines, devices and controllers detail pages that include the following changes:

-   **Summary tab**. Now only displays details on a specific node (machine, device or controller), organised across cards.
-   **Configuration**. This includes all editable settings for the specific node (machine, device or controllers).

<h4 id="heading--controller-versions-and-notifications">Controller versions and notifications</h4>

The MAAS web UI now displays the version of each running controller and notifies the users of any version mismatch between the region and rack controllers.

This helps administrators identify potential problems when upgrading MAAS on a multi-node MAAS cluster, such as within a HA setup.

<h4 id="heading--other-ui-improvements">Other UI improvements</h4>

-   Added DHCP status column on the *Subnets* tab.
-   Added architecture filters
-   VLAN and Space details page no longer allows inline editing.
-   VLAN page adds the IP ranges tables.
-   Zones page converted to AngularJS (away from YUI).
-   New warnings when changing a subnet’s mode (*Unmanaged* or *Managed*).
-   Renamed *Device Discovery* to *Network Discovery*.
-   When MAAS cannot determine the hostname for discovered devices, it will show the hostname as 'unknown' and greyed-out rather than using the MAC address manufacturer as the hostname.

<h3 id="heading--rack-controller-deployment">Rack controller deployment</h3>

MAAS 2.3 can now automatically deploy rack controllers when deploying a machine.

This is accomplished by providing cloud-init user data. Cloud-init will install and configure the rack controller after a machine has been deployed. Upon rack controller registration, MAAS will automatically detect whether the machine is a rack controller and process the transition automatically.

To deploy a rack controller, users can do so via the API (or CLI), e.g:

``` bash
maas $PROFILE machine deploy $SYSTEM_ID install_rackd=True
```

[note]
This features makes use of the MAAS snap to configure the rack controller on the deployed machine. 'snap store' mirrors are not yet available, which means the machine will need access to the internet.
[/note]

<h3 id="heading--improved-dns-reloading">Improved DNS reloading</h3>

This release includes various improvements to the DNS reload mechanism, allowing MAAS to be smarter about when to reload DNS after changes have been automatically detected or made.

<h3 id="heading--api-improvements">API improvements</h3>

The machines API endpoint now provide more information on configured storage and provides additional output that includes *volume_groups*, *raids*, *cache_sets*, and *bcaches* fields.

<h3 id="heading--django-111-support">Django 1.11 support</h3>

MAAS 2.3 now supports the latest Django LTS version, Django 1.11. This allows MAAS to work with the newer Django version in Ubuntu Artful, which serves as a preparation for the next Ubuntu LTS release.

-   Users running MAAS in Ubuntu Artful will use Django 1.11.
-   Users running MAAS in Ubuntu Xenial will continue to use Django 1.9.

<h3 id="heading--issues-fixed-with-this-release">Issues fixed with this release</h3>

For issues fixed in MAAS 2.3, please refer to the following milestone (external link):

-   <https://launchpad.net/maas/+milestone/2.3.0>

For more information on previous bug fixes across 2.3, please refer to the following milestones, all external links:

-   <https://launchpad.net/maas/+milestone/2.3.0rc2>
-   <https://launchpad.net/maas/+milestone/2.3.0rc1>
-   <https://launchpad.net/maas/+milestone/2.3.0beta3>
-   <https://launchpad.net/maas/+milestone/2.3.0beta2>
-   <https://launchpad.net/maas/+milestone/2.3.0beta1>
-   <https://launchpad.net/maas/+milestone/2.3.0alpha3>
-   <https://launchpad.net/maas/+milestone/2.3.0alpha2>
-   <https://launchpad.net/maas/+milestone/2.3.0alpha1>

# 2.2

<h2 id="heading--important-announcements">Important announcements</h2>

<h3 id="heading--support-for-composable-hardware---intel-rack-scale-design">Support for composable hardware - Intel Rack Scale Design</h3>

The MAAS team is excited to announce the support for the Intel Rack Scale Design (RSD). Intel Rack Scale Design (RSD) is a hardware architecture that allows for the dynamic composition of physical systems from a pool of available hardware resources.

MAAS, as a cloud-like, scale-out bare-metal provisioning system, will leverage the use of Intel RSD to compose (create) and provision systems. With the support for RSD, MAAS introduces the ability to manually or dynamically compose (create) new machines from an available pool of resources. It will allow administrators to request machines with specific resources on demand and be able to deploy their workloads on them.

<h3 id="heading--migrating-spaces-from-subnets-to-vlans">Migrating spaces from subnets to VLANs</h3>

The definition of spaces has changed from a Layer 3 concept to a Layer 2 concept.

The spaces definition in MAAS (first introduced in MAAS 1.9) is "a set of subnets that can mutually communicate". The assumption is that these spaces can route to each other, and have appropriate firewall rules for their purposes. (For example, a "dmz" space might contain subnets with internet access, or a "storage" space might contain subnets that can access the same storage networks.) Juju uses the current definition in order to ensure that deployed applications have access to networks appropriate for the services they provide.

The current definition of spaces as a L3 concept is problematic, in that sometimes Juju wants to deploy applications that themselves create a Layer 3 subnet. Therefore, it was decided that the concept of spaces will be pushed down a layer (to apply to VLANs in MAAS).

With spaces as a Layer 2 concept, it is now "a set of VLANs whose subnets can mutually communicate". As such:

-   VLANs will gain a 'space' reference, and subnets will have their spaces migrated to the VLANs they are on.
    -   On upgrades, if two subnets on the same VLAN are in different spaces, the most recently created space will be used for both.
-   Spaces will become optional.
    -   Fresh installs will not have a default space (e.g. space-0).
    -   On upgrades, if only the default space (space-0) exists, it will be removed.

The following API changes will occur in MAAS 2.2:

-   Editing a subnet's space will no longer be possible. Spaces must now be assigned on a per-VLAN basis. (Note: this is an API-breaking change; any usage of the MAAS API involving assigning subnets to spaces must be updated.)
-   For backward compatibility, a subnet's endpoint will present the underlying VLAN's space as a read-only value.

Recommended actions for MAAS administrators prior to upgrading to MAAS 2.2:

-   Ensure that no two subnets in the same VLAN are in different spaces, so that the upgrade path migrates the expected space to the VLAN.
-   In order to preserve backward compatibility with Juju charms that use the subnet-based definition of a space, ensure that each space contains subnets capable of mutual communication. It may be helpful to view the list of subnets grouped by space (using the "Group by: Spaces" option on the Subnets page in the web UI) in order to verify that each space is defined correctly.

Please note that MAAS and Juju make assumptions about the security and isolation of a network based on the space defined for a VLAN (and, by extension, each subnet in that VLAN). Since a VLAN containing subnets in multiple spaces implies lack of network isolation, MAAS and Juju cannot support that use model.

<h2 id="heading--new-features--improvements">New features & improvements</h2>

<h3 id="heading--maas-pods--composable-hardware-and-vms">MAAS Pods & composable hardware (and VMs)</h3>

MAAS 2.2 introduces a new concept called *pods*. In MAAS, pods are an abstraction to describe the availability of resources that allows MAAS to create or compose a machine with a set of those resources.

Pods refer to a combination of hardware resources that can be used to construct a machine. Each pod can be thought of as a pool of hardware with various available resources, such as CPU, RAM, and (local or remote) storage capacity. MAAS allows the manual allocation of physical hardware based on resources available in the pod. Users can use the MAAS UI or the API to allocate hardware from a pod.

In addition, MAAS will now make more efficient use of resources by *dynamically allocating hardware* (using Juju or the MAAS API). That is, machines can be allocated "just in time", based on CPU, RAM, and storage constraints.

The MAAS 2.2 release supports two types of pods:

-   Physical systems with Intel RSD
-   Virtual Machines with libvirt and qemu-kvm

<h3 id="heading--maas-pods---intel-rsd">MAAS Pods - Intel RSD</h3>

MAAS now supports Intel Rack Scale Design (RSD). The supported version of Intel RSD is with the Intel OEM PODM/PSME software version 1.2.5, which is APIv1 and based on Redfish.

MAAS Intel RSD support includes the following features:

-   Ability to discover all available resources
-   Ability to discover all pre-composed (pre-existing) resources or machines
-   Ability to compose machines (manually) via the API or the web UI
-   Ability to compose machines (manually and dynamically) with remote attached storage (iSCSI)
-   Ability to (dynamically) compose machines

<h3 id="heading--maas-pods---libvirt-with-qemu-kvm">MAAS Pods - libvirt with qemu-kvm</h3>

MAAS supports using a given qemu-kvm system as a pod, using libvirt. MAAS will treat the libvirt hypervisor as a pod, including the following features:

-   Ability to discover all available resources
-   Ability to discover all pre-composed (pre-existing) resources or machines
-   Ability to compose (create) machines (manually) via the API or the web UI
-   Ability to (dynamically) compose machines

<h3 id="heading--hardware-testing">Hardware testing</h3>

Hardware Testing in MAAS allows administrators to perform a series of tests to ensure the reliability of CPU, RAM, storage, and network environment. Therefore, MAAS administrators can now easily identify hardware issues before placing hardware into production.

Users can run hardware testing as part the commissioning processes, or as a separate action available on machines in "Ready" or "Deployed" state. When hardware tests are run as part of the commissioning process, machines that fail testing will not transition to the "Ready" state, and cannot be used for deployment.

The available tests are described below:

<h4 id="heading--disk-testing">Disk testing</h4>

-   **smartctl-validate** - uses the smartctl tool to verify existing SMART data on all drives has not detected any errors.
-   **smartctl-short & smartctl-long** - runs the SMART self tests to validate health on all disks. It provides a long running and a short running test.
-   **smartctl-conveyance** - runs the conveyance SMART self tests to validate health on all disks.
-   **badblocks** - runs badblocks testing on all disks in parallel.
-   **badblocks-destructive** - runs badblocks destructive tests on all disks in parallel. This means that badblocks will overwrite any date currently on the disks.

<h4 id="heading--cpu-and-ram-testing">CPU and RAM testing</h4>

-   **stress-ng-cpu-short/long** - stress tests the CPU of a machine for 5 minutes/12 hours respectively.
-   **stress-ng-memory-short/long** - stress tests the memory of a machine for 5 minutes/12 hours.
-   **memtester** - runs memtester over all available RAM.

<h4 id="heading--environment-testing">Environment testing</h4>

-   **Internet connectivity** - ensures machines can connect to the Internet.
-   **NTP connectivity** - ensures that machines can connect to the configured NTP server, whether this is MAAS or an external NTP server.

<h3 id="heading--dhcp-relay-support">DHCP relay support</h3>

MAAS now supports the modelling of DHCP relays in your network. For example, if an edge switch is forwarding DHCP traffic to a MAAS DHCP server, an administrator can tell MAAS that the VLAN at the edge will have its DHCP traffic forwarded to a particular destination VLAN. This allows MAAS to configure the DHCP server running on the primary and/or secondary rack controller to include a shared-network statement for that VLAN.

Please note that MAAS does not provide a DHCP relay service. Network administrators must configure a DHCP relay service to forward DHCP traffic from edge networks to the IP addresses of of the primary and/or secondary rack controller(s), on the VLAN where DHCP is enabled.

<h3 id="heading--unmanaged-subnets">Unmanaged subnets</h3>

In MAAS 2.0, the concept of a "static range" (a specific range of addresses in which MAAS was allowed to freely allocate addresses from) was removed from MAAS, in favour of the idea that MAAS managing entire subnets. As such, the only way to tell MAAS to not allocate certain sections of a subnet is to add a reserved IP range.

MAAS 2.2 now enhances this functionality by introducing *unmanaged subnets*. By setting a subnet in MAAS to "unmanaged", administrators prevent MAAS from using that subnet for automatic IP assignment. On unmanaged subnets, MAAS will only allocate IP addresses from reserved ranges. If no reserved range exists on an unmanaged subnet, IP allocation will fail.

<h3 id="heading--notifications-web-ui">Notifications (web UI)</h3>

MAAS 2.2 introduces a new notification system that surfaces messages to the user via the web UI, providing more visibility to the user when:

-   Rack controllers get disconnected
-   Image imports fail on your region controller
-   Rack controllers have images that the region controller does not
-   Static IP address allocations on a subnet are close to exhaustion

<h3 id="heading--switch-discovery-and-deployment-facebook-wedge-40-wedge-100">Switch discovery and deployment (Facebook Wedge 40, Wedge 100)</h3>

MAAS now has the ability to automatically discover and manage the Facebook Wedge 40 and Wedge 100 switches. When enlisting a Wedge switch, MAAS will identify OpenBMC-compatible management, provide power management, and allow the deployment of Ubuntu. MAAS will also automatically tag the fact that the device is a switch (and which particular model was found) for easy identification.

Additionally, MAAS will automatically identify if the Trident or Tomahawk ASICs are connected to the switch, and will automatically identify them via tags.

<h3 id="heading--maas-on-mobile-devices">MAAS on mobile devices</h3>

The MAAS web UI is now more responsive on mobile devices, resulting in a better user experience for users working from their phone or tablet. These users will see a slick new design for these devices. Thanks goes to the Ubuntu Web team for making MAAS look great on small devices.

<h3 id="heading--windows-deployments">Windows deployments</h3>

MAAS 2.2 improves the ability to configure storage configuration for Windows. This includes the ability to select the root device where Windows will be installed. Note that this ability extends to all DD images that MAAS can deploy.

<h3 id="heading--device-details-web-ui">Device details (web UI)</h3>

MAAS 2.2 provides a 'Details Page' for 'Devices' allowing administrators to add new interfaces as well as modifying existing ones. It also provides the ability to update a device hostname and domain name.

<h3 id="heading--package-repositories">Package repositories</h3>

MAAS 2.2 improves its package repositories support for Ubuntu mirrors by adding the ability to disable components. These components are Universe, Multiverse, and Restricted.

<h3 id="heading--commissioning-improvements">Commissioning improvements</h3>

Several improvements have been made to the commissioning process in MAAS 2.2:

-   **Ability to select custom commissioning scripts**
    As of 2.1, MAAS would run all uploaded custom commissioning scripts that. MAAS 2.2 now provides the ability to select which custom commissioning scripts to run. By default, however, all custom commissioning scripts will be run.

-   **Commissioning no longer dependent on a 20 minute timeout**
    In 2.1, if the entire commissioning process took longer than 20 minutes to run, the machine would fail to commission.

    As of 2.2, this is no longer the case. MAAS now has the ability to track both, builtin and custom commissioning scripts. This provides the flexibility to add custom commissioning scripts that would take longer than the initial 20 minute timeout, allowing them to fully run their scripts without marking a node 'Failed Commissioning'.

<h3 id="heading--usability-improvements-web-ui">Usability improvements (web UI)</h3>

Several web UI improvements have been made:

-   **Navigation improvements - adding tabs**
    Following the UX improvements from our design team, the web UI now has improved navigation. This includes a new tab-based approach for second level navigation items (for example, machines, devices, and controllers on the Nodes page).

-   **Better error surfacing**
    Added error surfacing when editing node interfaces (including both machine and devices interfaces).

<h2 id="heading--other-features">Other features</h2>

<h3 id="heading--maas-client-library--libmaas-041">MAAS Client Library — libmaas (0.4.1)</h3>

The MAAS team is happy to announce the introduction of a new and improved MAAS client library (python-libmaas). The MAAS team has started work on an asyncio-based client library to allow developers, integrators, and administrators to better interact with MAAS.

While this is an initial client library release and does not support all MAAS endpoints (nor all operations), we encourage all of our users to try it out and provide feedback. The currently supported releases include both MAAS 2.1 & 2.2.

If you wish to contribute to the development of the client library, please see below!

**Available endpoints**
The library currently has the following endpoints:

-   Account
-   Boot-resources, boot-sources (manages images)
-   Machines, devices, region-controllers & rack-controllers (manages nodes)
-   Events (manages machine events)
-   Configuration (settings)
-   Tags
-   Version
-   Zones

**Documentation**
If you would like to know more about python-libmaas, please refer to the below resources:

For installation and initial steps (external link): http://maas.github.io/python-libmaas/index.html

For a few examples, see these external links:

-   http://maas.github.io/python-libmaas/client/index.html
-   http://maas.github.io/python-libmaas/client/nodes/index.html

For pypi information, try this external link: https://pypi.python.org/pypi/python-libmaas

**Contribute**
If you would like to contribute you can find the source code in GitHub, at this external link:

https://github.com/maas/python-libmaas

For more questions, please find us:

-   `#maas` on freenode
-   `maas-devel` mailing list is a good place for questions

<!-- ===================================================================== -->
# 2.1

<h2 id="heading--important-announcements">Important announcements</h2>

<h3 id="heading--new-maas-dashboard">New MAAS dashboard</h3>

In MAAS 2.1, administrators will be shown the new MAAS dashboard after they log in to the web UI for the first time. Here, they are prompted to answer a few questions in order to get MAAS up and running quickly (see configuration journey section for details). In addition, administrators can view hosts that have been discovered on the network and quickly convert them to a device in MAAS.

<h3 id="heading--image-streams-have-been-upgraded-to-v3-local-mirror-update-required">Image streams have been upgraded to v3 (local mirror update required)</h3>

In order to support new kernels, MAAS has moved to a new format for image streams. Previous releases used stream in 'v2' format. Starting with MAAS 2.1, the 'v3' format image stream will be used.

Users upgrading from earlier versions of MAAS who are using the default image source will be automatically migrated to the v3 format.

MAAS will not migrate the URL of a non-default image source (i.e. a mirror) as it must first contain the v3 stream, which is available at this external link: `http://images.maas.io/ephemeral-v3/`.

Old images downloaded from the v2 stream will continue to work but the MAAS team only supports MAAS 2.1 users using the v3 stream. Note that the default image source may eventually drop the v2 stream.

Bootloaders are now included in the default image source (see bootloaders section for details). Mirrors should be updated accordingly.

<h3 id="heading--new-hwe-and-ga-kernel-naming-convention">New HWE and GA kernel naming convention</h3>

Starting with MAAS 2.1 and Ubuntu 16.04 LTS (Xenial), MAAS is adhering to a new naming convention for hardware enablement (HWE) kernels and general availability (GA) kernels. MAAS will no longer support the old naming convention for HWE kernels (e.g. hwe-y) when selecting images (Xenial and newer) to import. The new nomenclature is as follows:

-   `ga-<version>`: The GA kernel has the major kernel version of the kernel which the corresponding Ubuntu release shipped with. For example, ‘ga-16.04’ is the kernel which shipped with 16.04 yet comes with all the bug fixes provided by the Ubuntu archives. As per Ubuntu policy, a GA kernel will never have its major version upgraded (until the release itself is upgraded).

-   `hwe-<version>`: The latest HWE kernel available for a given LTS release. As new HWE kernels become available (from newly shipped Ubuntu releases), the hwe-<version> kernel will be correspondingly changed (up to, and including, the next LTS). For example, at time of writing, 'hwe-16.04' is equivalent to 'ga-16.04'. Soon after Ubuntu 16.10 is released, 'hwe-16.04' will point to 'ga-16.10'.

<h3 id="heading--commissioning-user-data-and-pxeuefi-templates-no-longer-available">Commissioning-user-data and pxe/uefi templates no longer available</h3>

In the past, MAAS stored `commissioning-user-data` and `pxe/uefi` templates in `/etc/maas/templates`. As of MAAS 2.1, these templates are no longer available in that location as they are not intended to be modified by users.

<h2 id="heading--major-new-features">Major new features</h2>

<h3 id="heading--first-user-configuration-journey-web-ui">First user configuration journey (web UI)</h3>

Administrators can now perform some initial configuration upon logging in to the web UI for the first time. This includes:

-   Ability to change the name of your MAAS
-   Ability to configure options that affect connectivity:
    -   Select an upstream DNS Server (Optional)
    -   Input different Ubuntu mirrors (Required)
    -   Input an external proxy (Optional)
    -   Ability to select additional images to download
    -   Ability to import SSH keys from Launchpad or GitHub

<h3 id="heading--device-discovery">Device discovery</h3>

MAAS now automatically listens to the network and reports any discovered devices. Devices are identified when the rack controller observes them communicating on an attached IPv4 subnet. Discovered devices that do not correspond to machines and devices already known to MAAS are shown on the dashboard. If a device advertises a hostname using `mDNS` (such as with `avahi` or `Bonjour`), MAAS will also present the discovered hostname in the dashboard. Using the dashboard, a discovery can quickly be added to MAAS as a device or as a network interface to a machine or device.

<h3 id="heading--active-subnet-mapping">Active subnet mapping</h3>

The device discovery feature was designed to operate passively by default. While MAAS will not send any traffic on attached networks for discovery purposes unless instructed to, there are two ways to instruct MAAS to map your networks:

-   **On-demand**: Administrators can choose to map their subnet using an action on the subnet details page. This action will scan the subnet just once, so that observed devices on that subnet may quickly be seen in the dashboard. This feature is useful after initially installing MAAS, to quickly populate the list of discoveries with active devices on the network.

-   **Periodically** (recommended): By enabling active discovery on a per-subnet basis, subnets will be scanned at a user-specified interval (default is every three hours). This allows MAAS to maintain current information about which IP addresses are in use on each subnet.

Before actively mapping any networks, it is recommended that the `nmap` package be installed on each rack controller. Doing so results in faster scans that require less network traffic. If nmap is not installed, MAAS will resort to scanning using the `ping` utility.

<h3 id="heading--offline-deployment-and-customisable-apt-repositories">Offline deployment and customisable APT repositories</h3>

MAAS 2.1 improves offline deployment by adding support for *Ubuntu derived repositories*, PPAs, and custom APT repositories. This enables MAAS to configure deployed machines with the correct APT repositories and keyrings, without being dependent on Internet connectivity.

-   Prior to 2.1, MAAS only allowed users to change the Ubuntu archive to use. This was limited to defining the location of an official Ubuntu mirror.

-   Derived repositories are based on an Ubuntu mirror, but have had packages added or removed, which requires signing the repository with an unofficial GPG key. MAAS now allow users to provide GPG key fingerprints to support this type of repository. These fingerprints are required in order for the derived repository to be trusted, and will be added to the APT keyring on each machine.

-   PPAs can now be specified, which will be added to the APT sources on deployed machines. Users may define a GPG key fingerprint in order for the machine to trust the PPA, for cases where the deployed machine cannot access the Ubuntu key server.

-   Custom repositories can be specified to add additional packages to deployed machines. The distribution and component can be customised as appropriate. For example, users would be able to add the Google Chrome repository, which is as follows:

    `deb http://dl.google.com/linux/chrome/deb/ stable main`

    In this case, the distribution is 'stable', and the component is 'main'.

<h3 id="heading--new-ntp-service">New NTP service</h3>

MAAS now provides managed NTP services (with `ntpd`) for all region and rack controllers. This allows MAAS to both keep its own controllers synchronised, and keep deployed machines synchronised as well.

-   The region controller configures the NTP service (ntpd) to keep its time synchronised from one or more external sources. By default, the MAAS region controller uses ntp.ubuntu.com. This can be customised on the Settings page.

-   The rack controllers also configure the NTP service (ntpd). They synchronise their time with the region controllers.

-   Rack controllers also configure DHCP with the correct NTP information. Any machine on the network that obtains a DHCP lease from MAAS will benefit from NTP support.

-   External sites can be used as a time source for both controllers and machines. An existing NTP infrastructure can be used so that all machines and controllers sync their time from it. This is done by selecting the 'External Only' option on the Settings page.

<h3 id="heading--advanced-networking-static-routes">Advanced networking: static routes</h3>

MAAS 2.1 introduces the ability to define static routes. This allows administrators to configure reachability to a subnet from a source subnet. Administrators can define routes on a per-subnet basis to use a particular gateway, using a configured destination and metric.

<h3 id="heading--machine-networking-bridge-configuration">Machine networking: bridge configuration</h3>

MAAS 2.1 supports the creation of bridge interfaces. This support is limited to the ability to create a bridge against a single interface, such as for the purpose of eventually deploying virtual machines or containers on the machine.

Automatic bridge creation on all configured interfaces can also be performed at allocation time using the API.

<h3 id="heading--new-rescue-mode">New Rescue mode</h3>

MAAS 2.1 supports a new state in the machine life-cycle: Rescue mode. This allows users to boot a Deployed or a Broken node using an ephemeral image (Ubuntu running in memory on the underlying machine). This allows administrators to SSH to the machine for maintenance purposes.

<h3 id="heading--enhanced-images-user-interface">Enhanced images user interface</h3>

The MAAS images page has been completely redesigned. Improvements include:

-   Supports selecting the image source (maas.io or custom repository).
-   Now shows the image releases and architectures available in a repository before the import starts.
-   Now displays detailed status throughout the image import process.
-   The Boot Images section in the Settings page has been removed.

<h2 id="heading--minor-new-features">Minor new features</h2>

<h3 id="heading--disk-erasing-improvements-and-secure-erase">Disk erasing improvements and secure erase</h3>

MAAS 1.7 introduced the ability to erase disks when a machine is Released. This support was limited to erasing the whole disk and could only be enabled (or disabled) globally.

Starting with 2.1, MAAS supports the ability to request disk erasure on a per-machine basis, at the time the machine is released. In addition, new options for the disk erase mode have been added:

-   **Secure erase**: MAAS will attempt to erase via secure erase (if the storage device supports it), otherwise, it will perform a full erase or a quick erase (depending on the options provided).
-   **Quick erase**: MAAS will only erase the beginning and the end of each storage device.

<h3 id="heading--machine-networking-sr-iov-auto-tagging-and-web-ui-tag-improvements">Machine networking: SR-IOV auto-tagging and web UI tag improvements</h3>

MAAS now attempts to auto-detect and tag SR-IOV NIC cards.

MAAS now allows the definition of tags per network interface via the web UI.

<h3 id="heading--support-for-low-latency-kernels">Support for low latency kernels</h3>

Starting with Ubuntu 16.04 LTS, low latency kernels are available on i386 and amd64 for both GA and HWE kernels. The currently available low latency kernels are:

-   hwe-x-lowlatency: the Xenial low latency HWE kernel for Trusty
-   ga-16.04-lowlatency: the low latency GA kernel for Xenial
-   hwe-16.04-lowlatency: the low latency HWE kernel for Xenial

[note]
As time of writing, the last 2 kernels are the same.
[/note]

<h3 id="heading--bootloaders-are-now-provided-in-the-image-stream">Bootloaders are now provided in the image stream</h3>

Previously, bootloaders were downloaded on the rack controller from the Ubuntu archives for each architecture MAAS had images for. Starting with MAAS 2.1, bootloaders are downloaded with the images from where rack controllers retrieve them, as they do with images. So MAAS no longer directly interacts with the Ubuntu archives.

In the case that bootloaders are missing from the stream, MAAS will attempt to locate previous downloads of the bootloader as well as package installs of the bootloader. Users with image mirrors must ensure image their mirrors include the bootloaders in order to be running the latest supported versions.

<h3 id="heading--ssh-keys-can-be-imported-from-launchpad-or-github">SSH keys can be imported from Launchpad or GitHub</h3>

Users can now initiate the import of SSH public keys from the web UI. Users who log in to MAAS for the first time will be given the opportunity to import their SSH keys. Alternatively, users can import keys later into their user profile page, or continue to upload keys manually.

<h2 id="heading--other-notable-changes">Other notable changes</h2>

<h3 id="heading--better-error-surfacing-for-dhcp-snippets-and-package-repositories">Better error surfacing for DHCP snippets and package repositories</h3>

Both the DHCP Snippets section and the Package Repositories section have been improved in order to show errors in a more user-friendly way.

<h3 id="heading--vanilla-framework-html-and-css-updates-smoother-look-and-feel">Vanilla framework: HTML and CSS updates, smoother look and feel</h3>

The HTML templates and CSS frameworks in MAAS have been completely rebuilt with the Vanilla CSS framework. Icons and interactions in MAAS have greatly improved; users will notice smoother, more intuitive interactions with the web UI.

The MAAS team would like to thank the Canonical design and web teams for their contributions in this area.

<h3 id="heading--networks-page-renamed">Networks page renamed</h3>

The Networks page has been renamed to Subnets.

<!-- ===================================================================== -->
# 2.0

<h2 id="heading--important-announcements">Important announcements</h2>

<h3 id="heading--maas-20-supported-on-ubuntu-1604-lts-xenial">MAAS 2.0 supported on Ubuntu 16.04 LTS (Xenial)</h3>

MAAS version 2.0 is supported on Ubuntu 16.04 LTS. MAAS 2.0 and greater will NOT be supported on Ubuntu 14.04 LTS. The latest MAAS 1.9 point release will continue to be supported on Ubuntu 14.04 LTS (Trusty) until it reaches end-of-life.

Upgrades are supported for users running Ubuntu 14.04 systems running MAAS 1.9 or earlier. Upon upgrading to Ubuntu 16.04, the MAAS database and configuration will be seamlessly migrated to the supported MAAS version.

Please see the “Other Notable Changes” section below for more details regarding the reasons for this change.

<h3 id="heading--terminology-changes">Terminology Changes</h3>

Cluster controllers have been renamed to rack controllers.

Starting from MAAS 2.0, MAAS cluster controllers have been deprecated, along with the legacy `nodegroups` API. The new API endpoint is `rackcontrollers`, which provides feature parity with earlier versions of MAAS.

For more information on rack controllers, refer to the Major new Features section bellow or refer to rack-configuration.

<h3 id="heading--api-10-has-been-deprecated-introducing-api-20">API 1.0 has been deprecated, introducing API 2.0</h3>

Starting from MAAS 2.0, the MAAS REST API version 1.0 has been deprecated. MAAS 2.0 drops support for the legacy 1.0 API, in favour of API version 2.0. With the introduction of the new API version, various endpoints have now been deprecated, and new end-points have been introduced. API users will need to update their client tools to reflect the changes.

For more information on API 2.0, refer to API documentation &lt;region-controller-api&gt;.

<h3 id="heading--static-ip-ranges-have-been-deprecated">Static IP ranges have been deprecated</h3>

Starting from MAAS 2.0, static IP ranges (previously found on the cluster interface page) have been deprecated. MAAS now assumes total control of a subnet. MAAS will automatically assign IP addresses to deployed machines, as long as those IP addresses are not within a dynamic or a reserved IP range. Users are now only required to specify one or more dynamic ranges per subnet. Dynamic ranges are used for auto-enlistment, commissioning, and any other systems configured for DHCP. IP addresses in-use for purposes such as devices, default gateways, DNS servers, rack and region controllers, and BMCs are automatically avoided when assigning IP addresses. Reserved IP ranges may be added if MAAS should avoid certain ranges of IP addresses in the subnet.

<h3 id="heading--maas-region-controller-min-has-been-renamed-to-maas-region-api">maas-region-controller-min has been renamed to maas-region-api</h3>

The `maas-region-controller-min` package has been renamed to `maas-region-api`. This package provides API services for MAAS (`maas-regiond`) and can be used to scale out the API front-end of a MAAS region.

<h3 id="heading--maas-user-creation-been-moved-to-maas-command">MAAS user creation been moved to 'maas' command</h3>

Starting from MAAS 2.0, the `maas` command now provides the ability to create admin users. The `maas-region createadmin` command has been deprecated. New administrators should now be created with `maas createadmin`.

<h3 id="heading--maas-provision-command-has-been-replaced">maas-provision command has been replaced</h3>

The MAAS rack controller command-line interface (`maas-provision`) has been replaced by the `maas-rack` command.

<h3 id="heading--maas-region-admin-command-has-been-replaced-with-maas-region">maas-region-admin command has been replaced with maas-region</h3>

The MAAS region controller command-line interface (`maas-region-admin`) has been replaced by the `maas-region` command. Note that this command provides an interface to interact directly with Django, which should only be used for debugging purposes.

<h3 id="heading--debian-installer-is-no-longer-installed-or-supported">Debian Installer is no longer installed or supported</h3>

Because support for the Debian Installer (DI) has been dropped (as of MAAS 1.9), MAAS no longer downloads DI-related files from simplestreams. Upon upgrading to MAAS 2.0, DI-related files will be removed from the MAAS region (and all rack controllers).

<h2 id="heading--major-new-features">Major new features</h2>

<h3 id="heading--maas-rack-controllers-and-high-availability">MAAS Rack Controllers and High Availability</h3>

Starting from MAAS 2.0, MAAS **cluster controllers** have been renamed to **rack controllers**.

-   The `nodegroups` and `nodegroups/(group)/interfaces` API endpoints have been deprecated. In MAAS 2.0, the `rackcontrollers` interface partially replaces this functionality. For defining dynamic and reserved ranges, or specifying default gateways, use the `subnets` endpoint. For enabling or disabling DHCP, use the `fabrics/(fabric)/vlans` endpoint.
-   The **Clusters** tab is no longer available in the Web UI. Controllers are now found under the **Nodes** tab, where each region and/or rack controller can be found. Other cluster interface properties have been moved to the Subnet and VLAN details pages under the **Networks** tab.
-   Machines no longer belong to a specific controller. In earlier versions of MAAS, machines would directly assigned to a cluster controller. The cluster controller that the machine belonged to would not only perform DHCP for that machine, but also all the PXE booting and power management.

    In order to support high availability for rack controllers, (starting from MAAS 2.0) machines no longer belong to a specific rack controller. The best controller to manage a machine is now determined at runtime.

-   DHCP is now configured per-VLAN. In earlier versions of MAAS, DHCP was directly linked and configured per cluster interface. As of MAAS 2.0, DHCP is now configured and managed per-VLAN, which allows any rack controller to potentially provide DHCP in a high-availability environment.
-   Rack controllers have been enabled for high availability. Starting from MAAS 2.0, rack controllers in the same VLAN become candidates to manage DHCP, PXE/TFTP, and power control for machines on the VLAN. MAAS now supports the concept of a **primary** and a **secondary** rack controller. If a secondary controller determines that the primary controller is unavailable, it will assume control of those services.
-   Added `maas-rack support-dump` command. For increased support observability, users can now dump the contents of several internal MAAS data structures by executing `sudo maas-rack support-dump`. This command will dump networking diagnostics, rack configuration, and image information. Information can be restricted to a particular category by using the `--networking`, `--config`, or `--images` options.
-   Rack controllers can now be found under the **Nodes** tab in the Web UI. MAAS 2.0 Adds a new **Controllers** section under thee **Nodes** tab. This section will now list all rack and region controllers. Under a rack controller, the user will be able to see service tracking, connected VLANs, rack interfaces and other relevant information.

<h3 id="heading--region-controller-redundancy-high-availability">Region Controller Redundancy (High Availability)</h3>

Starting from MAAS 2.0, MAAS provides the ability to scale out (provide redundancy for) the MAAS region controller API, HTTP server, and DNS. This will allow administrators to set up multiple MAAS region controllers (`maas-region-api`) against a common database, providing redundancy of services. With further manual configuration, users will be able to setup the MAAS region controller in high availability mode.

<h3 id="heading--new-networks-web-ui">New Networks Web UI</h3>

MAAS 2.0 introduces a few new Web UI features that were not available in previous versions of MAAS.

-   Added fabric and space details pages.
-   Added the ability to add and remove fabrics, spaces, subnets and VLANs. This can be done using the actions menu on the **Networks** tab. The ability to delete fabrics, spaces, subnets and VLANs is also available from the details page for each respective object.

<h3 id="heading--dns-management">DNS Management</h3>

MAAS 2.0 extends DNS management by adding the following features:

-   Ability to create multiple DNS domains.
-   Ability to add multiple records (`CNAME`, `TXT`, `MX`, `SRV`) per domain. (API only)
-   Ability to select the domain for machines and devices.
-   Ability to assign (additional) names to IP addresses. (API only)
-   For deployed machines, `A` records continue to be created for the IP of the PXE interface.
-   Additional PTR records are now created for all non-PXE interfaces in the form: `<interface>.<machine fully-qualified-domain-name>`
-   Reverse DNS is now generated for only the subnet specified, rather than the parent /24 or /16. By default, RFC2137 glue is provided for networks smaller than /24. This can be disabled or changed on a per-subnet basis via the API.

<h3 id="heading--ip-ranges">IP Ranges</h3>

Previous versions of MAAS used the concepts of a **dynamic range** and **static range**, which were properties of each cluster interface. This has been redesigned for MAAS 2.0 as follows:

-   Dynamic ranges have been migrated from earlier MAAS releases as-is.
-   Because static ranges have been removed from MAAS, each static range has been migrated to one or more reserved ranges, which represent the opposite of the previous static range. (MAAS now assumes it has full control of each managed subnet, and is free to assign IP addresses as it sees fit, unless told otherwise.)

    For example, if in an earlier MAAS release a cluster interface was configured on 192.168.0.1/24, with a dynamic range of 192.168.0.2 through 192.168.0.99, and a static range of 192.168.0.100 through 192.168.0.199, this will be migrated to:

        IP range #1 (dynamic): 192.168.0.2 - 192.168.0.99
        IP range #2 (reserved): 192.168.0.200 - 192.168.0.254

    Since 192.168.0.100 - 192.168.0.199 (the previous static range) is not accounted for, MAAS assumes it is free to allocate static IP addresses from that range.

-   Scalability is now possible by means of adding a second dynamic IP range to a VLAN. (To deal with IP address exhaustion, MAAS supports multiple dynamic ranges on one or more subnets within a DHCP-enabled VLAN.)
-   Reserved ranges can now be allocated to a particular MAAS user.
-   A comment field has been added, so that users can indicate why a particular range of IP addresses is reserved.
-   IP ranges can be configured in the Web UI via the Subnet details page, or using the `subnets` REST API endpoint.

<h3 id="heading--api-20-and-maas-cli-updates">API 2.0 and MAAS CLI Updates</h3>

Version 1.0 of the MAAS REST API has been removed and replaced with the 2.0 version of the REST API. As such, new endpoints and commands have been introduced:

-   RackControllers - This endpoint/command has the following operations in addition to the base operations provided by nodes: `import-boot-images` - Import the boot images on all rack controllers `describe-power-types` - Query all of the rack controllers for power information

-   RackController - This endpoint/command has the following operations in addition to the base operations provided by nodes
    -   `import-boot-images` - Import boot images on the given rack controller
    -   `refresh` - refresh the hardware information for the given rack controller
-   Machines - This endpoint/command replaces many of the operations previously found in the nodes endpoint/command. The machines endpoint/command has the following operations in addition to the base operations provided by nodes.
    -   `power-parameters` - Retrieve power parameters for multiple machines
    -   `list-allocated` - Fetch machines that were allocated to the user/oauth token.
    -   `allocate` - Allocate an available machine for deployment.
    -   `accept` - Accept declared machine into MAAS.
    -   `accept-all` - Accept all declared machines into MAAS.
    -   `create` - Create a new machine.
    -   `add-chassis` - Add special hardware types.
    -   `release` - Release multiple machines.
-   Machine - This endpoint/command replaces many of the operations previously found in the node endpoint/command. The machine endpoint/command has the following operations in addition to the base operations provided by node.
    -   `power-parameters` - Obtain power parameters for the given machine.
    -   `deploy` - Deploy an operating system to a given machine.
    -   `abort` - Abort the machines current operation.
    -   `get-curtin-config` - Return the rendered curtin configuration for the machine.
    -   `power-off` - Power off the given machine.
    -   `set-storage-layout` - Change the storage layout of the given machine.
    -   `power-on` - Turn on the given machine.
    -   `release` - Release a given machine.
    -   `clear-default-gateways` - Clear any set default gateways on the machine.
    -   `update` - Change machine configuration.
    -   `query-power-state` - Query the power state of a machine.
    -   `commission` - Begin commissioning process for a machine

<h4 id="heading--other-endpointscommands-have-changed">Other endpoints/commands have changed:</h4>

-   All list commands/operations have been converted to read
-   All new and add commands/operations have been converted to create
-   Nodes - The nodes endpoint/command is now a base endpoint/command for all other node types(devices, machines, and rack-controllers). As such most operations have been moved to the machines endpoint/command.The following operations remain as they can be used on all node types.
    -   `is-registered` - Returns whether or not the given MAC address is registered with this MAAS.
    -   `set-zone` - Assign multiple nodes to a physical zone at once.
    -   `read` - List nodes visible to the user, optionally filtered by criteria.
-   Node - The node endpoint/command is now a base endpoint/command for all other node types(devices, machines, and rack-controllers). As such most operations have been moved to the machine endpoint/command. The following operations remain as they can be used on all node types.
    -   `read` - Read information about a specific node
    -   `details` - Obtain various system details.
    -   `delete` - Delete a specific node.
-   With the migration of nodes to machines the following items previously outputted with the list command have been changed or removed from the machines read command:
    -   ``status - Will now show all status types
    -   `substatus`, `substatus_action`, `substatus_message`, `substatus_name` - Replaced by `status`, `status_action`, `status_message`, `status_name`.
    -   ``boot_type - Removed, MAAS 2.0 only supports fastpath.
    -   `pxe_mac` - Replaced by `boot_interface`.
    -   `hostname` - Now only displays the hostname (without the domain) of the machine. `fqdn` and `domain` attributes can now be used instead.
-   And other endpoints/commands have been deprecated:
    -   NodeGroups - Replacement operations are found in the RackControllers, Machines, and BootResources endpoints/commands.
    -   NodeGroupInterfaces - replacement operations are found in the RackController, IPRanges, Subnets, and VLANS endpoints/commands.

<h3 id="heading--extended-storage-support">Extended Storage Support</h3>

MAAS 2.0 Storage Model has been extended to support:

-   XFS as a filesystem.
-   Mount options.
-   Swap partitions. (MAAS 1.9 only supported the creation of a swap file in the filesystem.)
-   `tmps`/`ramfs` support.

All of these options are currently available over the CLI.

<h3 id="heading--dhcp-snippets">DHCP Snippets</h3>

MAAS 2.0 introduces the ability to define DHCP snippets. This feature allows administrators to manage DHCP directly from MAAS, removing the need to manually modify template files. The following types of DHCP snippets can be defined:

> -   **Host snippets** - used for configuration for a particular node in MAAS.
> -   **Subnet snippets** - used for configuration for a specific subnet in MAAS.
> -   **Global snippets** - used for configuration that will affect DHCP (isc-dhcp) as a whole.

For more information, see DHCP Snippets &lt;dhcpsnippets&gt;.

<h2 id="heading--minor-new-features">Minor new features</h2>

<h3 id="heading--maas-proxy-is-now-managed">MAAS proxy is now managed</h3>

Starting from MAAS 2.0, MAAS now manages the configuration for `maas-proxy`. This allows MAAS to lock down the proxy so that it only allows traffic from networks MAAS knows about. For more information, see MAAS Proxy &lt;proxy&gt;.

<h3 id="heading--rsyslog-during-enlistment-and-commissioning">rsyslog during enlistment and commissioning</h3>

MAAS 2.0 now enables `rsyslog` for the enlistment and commissioning environment (when using Xenial as the commissioning image). This allows users to see `cloud-init`'s syslog information in `/var/log/maas/rsyslog/`.

<h3 id="heading--ability-to-change-a-machines-domain-name-from-the-ui">Ability to change a machine’s domain name from the UI</h3>

MAAS 2.0 introduces the ability to change a machine’s DNS domain via the Web UI. It was previously supported on the API only.

<h3 id="heading--networks-listing-page">Networks listing page</h3>

In the **Networks** tab, a new networks overview has been introduced, which provides a high-level view of the MAAS networking mode. The network model can be grouped by either fabrics or spaces.

<h3 id="heading--service-tracking">Service Tracking</h3>

MAAS now tracks the status of the services required for its operation, such as `bind`, `maas-dhcpd`, `maas-dhcpd6`, `tgt`, and `maas-proxy`.

<h2 id="heading--other-notable-changes">Other notable changes</h2>

<h3 id="heading--maas-20-requires-python-35">MAAS 2.0 requires Python 3.5</h3>

Starting with MAAS 2.0, MAAS has now been ported to Python 3.5 (the default version of Python in Ubuntu 16.04 "Xenial").

<h3 id="heading--maas-20-now-fully-supports-native-django-18-migration-system">MAAS 2.0 now fully supports native Django 1.8 migration system</h3>

MAAS is now based on Django 1.8. Django 1.8 has dropped support for the South migration system in favour of the native Django migration system, which breaks backwards compatibility with previous versions of Django.

MAAS continues to support a full upgrade path. MAAS versions 1.5, 1.7, 1.8, and 1.9 have been tested and confirmed to upgrade seamlessly to MAAS 2.0.

<h3 id="heading--instant-dhcp-lease-notifications">Instant DHCP lease notifications</h3>

MAAS no longer scans the leases file every 5 minutes. `isc-dhcp-server` now directly notifies MAAS if a lease is committed, released, or expires.

<h3 id="heading--host-entries-in-dhcp">Host entries in DHCP</h3>

Host entries are now rendered in the DHCP configuration instead of placed in the leases file. This removes any state that previously existed in the DHCP lease database on the cluster controller.

Starting with MAAS 2.0, if the dhcpd.leases file is lost (such as during a failure scenario in a high availability environment), MAAS will be able to reconstruct it.

<h3 id="heading--power-control-is-no-longer-specific-to-a-rack-controller">Power control is no longer specific to a rack controller</h3>

MAAS selects one of the available rack controllers to power control or query a BMC. The same rack controller that powers the BMC does not need to be the rack controller that the machine PXE boots from.

# Get in touch

We'd love to hear about how you're using MAAS, whether it's at the smallest of scales or the largest. Our team is always approachable and can usually be found in the following locations:

-   Join us on IRC. We can be found on the maas channel on freenode.
-   Subscribe to the maas-devel mailing list, a great place to ask questions.

<!-- LINKS -->

------
****
------
