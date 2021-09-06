MAAS is an open-source tool that lets you create a data centre from bare-metal servers. You can discover, commission, deploy, and dynamically reconfigure a large network of individual units.  MAAS converts your hardware investment into a cohesive, flexible, distributed data centre, with a minimum of time and effort.

#### Questions you may have:

1. [What is MAAS?](#heading--what-is-maas)
2. [What does MAAS offer me?](#heading--what-maas-offers)
3. [Can MAAS co-locate key components to conserve  resources?](#heading--colocation-of-key-components)
4. [How does MAAS work?](#heading--how-maas-works)

<a href="#heading--what-is-maas"><h2 id="heading--what-is-maas">What is MAAS?</h2></a>

MAAS expands to "Metal As A Service" -- it converts bare-metal servers into cloud instances of virtual machines. There is no need to manage individual units. You can quickly provision or destroy machines, as if they were instances hosted in a public cloud like Amazon AWS, Google GCE, or Microsoft Azure.

MAAS can act as a standalone PXE/preseed service or integrate with other technologies. It works exceptionally well with [Juju](https://juju.is/docs/olm/maas), the service and model management tool. MAAS manages the machines and Juju manages the services running on those machines -- a perfect arrangement.  Virtual machines (VMs) can even act as MAAS machines if they boot from the network via PXE.

<a href="https://discourse.maas.io/uploads/default/original/1X/d19eff9ef45c554d085ee1d657e4ddd810eac6df.jpeg" target="_blank"><img width="690" src="https://discourse.maas.io/uploads/default/original/1X/d19eff9ef45c554d085ee1d657e4ddd810eac6df.jpeg"></a>

<details><summary>Tell me about PXE booting</summary>

PXE stands for "Preboot Execution Environment," usually pronounced "pixie."  The term refers to a way of booting an OS image (or other software assembly) downloaded to a client via a NIC.  The NIC must be PXE-capable for this to work.  Many NICs can be configured to support PXE boot with a software switch.

</details>

<a href="#heading--what-maas-offers"><h2 id="heading--what-maas-offers">What MAAS offers</h2></a>

MAAS can manage a large number of physical machines by merging them into user-defined resource pools. MAAS automatically provisions participating machines and makes them available for use. You can return unused machines to the assigned pool at any time.

rad-begin /deb/3.0/ui /deb/3.0/cli /snap/3.0/ui /snap/3.0/cli
MAAS also discovers all of the USB and PCI devices attached to your physical or virtual machines, and allows you to delete them from the machine's visible configuration, prior to deployment, if you so desire.
rad-end

rad-begin   /deb/2.9/ui /deb/3.0/ui   /snap/2.9/ui /snap/3.0/ui 
MAAS integrates all the tools you need into a smooth system-management experience. It includes the following thirteen features:

1. web UI (optimised for mobile devices)
2. Ubuntu, CentOS, Windows, and RHEL installation support
3.  open-source IP address management (IPAM)
4. full API/CLI support
5. high availability (optional)
6. IPv6 support
7. inventory of components
8. DHCP and DNS for other devices on the network
9. DHCP relay integration
10. VLAN and fabric support
11. NTP for the entire infrastructure
12. hardware testing
13. composable hardware support

These tools can be controlled from a responsive web UI.  You can easily (re)configure and scale your data centre with MAAS.

<a href="https://discourse.maas.io/uploads/default/original/1X/00968a71b82ce01c45ae3b345ed6b1270d0927bf.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/00968a71b82ce01c45ae3b345ed6b1270d0927bf.jpeg"></a> 

rad-end

rad-begin   /deb/2.9/cli /deb/3.0/cli   /snap/2.9/cli /snap/3.0/cli
MAAS integrates all the tools you need into a smooth system-management experience. It includes the following eleven features:

1. Ubuntu, CentOS, Windows, and RHEL installation support
2. open-source IP address management (IPAM)
3. high availability (optional)
4. IPv6 support
5. inventory of components
6. DHCP and DNS for other devices on the network
7. DHCP relay integration
8. VLAN and fabric support
9. NTP for the entire infrastructure
10. hardware testing
11. composable hardware support


<a href="https://discourse.maas.io/uploads/default/original/1X/40fdae53957095e5a830458dc5c7a62ea5d78c10.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/40fdae53957095e5a830458dc5c7a62ea5d78c10.jpeg"></a> 

rad-end

MAAS works with any system configuration tools. Both the [Chef](https://www.chef.io/chef) and [Juju](https://jaas.ai/) teams recommend MAAS as a physical provisioning system.

[note]
Please note that Windows and RHEL images require [Ubuntu Advantage](https://www.ubuntu.com/support) to work correctly with MAAS.
[/note]

<a href="#heading--colocation-of-key-components"><h3 id="heading--colocation-of-key-components">Colocation of key components</h3></a>

MAAS relies on two key components: the *region controller* and the *rack controller*. The region controller handles operator requests; the rack controller provides high-bandwidth services to multiple racks. In essence, rack controllers manage racks, while the region controller manages the data centre. We generally recommended installing both controllers on the same system.  The default MAAS install delivers this co-located configuration automatically. This all-in-one solution also provides DHCP. 

See [Concepts and terms](/t/concepts-and-terms/785#heading--controllers) for a deeper understanding of these components. Note that in special cases, such as [high availability or load balancing](/t/high-availability/nnnn), you will want to install multiple region and rack controllers.  You should also review your existing network design to determine whether [MAAS-managed DHCP](/t/managing-dhcp/nnnn) will cause problems.

<a href="https://discourse.maas.io/uploads/default/original/1X/3ad2b128fbc034e9f575f21c0415a6e6c55baea3.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/3ad2b128fbc034e9f575f21c0415a6e6c55baea3.jpeg"></a>

<a href="#heading--how-maas-works"><h2 id="heading--how-maas-works">How MAAS works</h2></a>

When you [add a new machine](/t/how-to-manage-machines/nnnn#heading--how-to-add-a-machine-manually) to MAAS, or elect to add a machine that MAAS has [enlisted](/t/machines/nnnn#heading--about-enlistment), MAAS [commissions](/t/machines/nnnn#heading--about-commissioning-machines) it for service and adds it to the pool.  At that point, the machine is ready for use. MAAS keeps things simple, marking machines as "New," "Commissioning," "Ready," and so on.

<details><summary>Tell me, quickly, about enlistment and commissioning.</summary>

There are two ways to add a machine to MAAS.  Assuming it's on the network and capable of PXE-booting, you can add it explicitly -- or MAAS can simply discover it when you turn it on.

Enlistment just means that MAAS discovers a machine when you turn it on, and presents it to the MAAS administrator, so that they can choose whether or not to commission it.  Machines that have only been enlisted will show up in the machine list as "New."

Commissioning means that MAAS has successfully booted the machine, scanned and recorded its resources, and prepared it for eventual deployment.  Machines that you explicitly dd are automatically commissioned.  MAAS marks a successfully-commissioned machine as "Ready" in the machine list.

</details>

rad-begin   /deb/2.9/ui   /snap/2.9/ui /deb/3.0/ui /snap/3.0/ui
<a href="https://discourse.maas.io/uploads/default/original/1X/605019de31078dd70df72ff199d812de13a30d00.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/605019de31078dd70df72ff199d812de13a30d00.jpeg"></a>
rad-end

rad-begin   /deb/2.9/cli   /snap/2.9/cli /deb/3.0/cli /snap/3.0/cli
<a href="https://discourse.maas.io/uploads/default/original/1X/6aec9b567022216d80596411e689a14e1f594674.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/6aec9b567022216d80596411e689a14e1f594674.jpeg"></a>
rad-end

MAAS controls machines through IPMI (or another BMC). It can also manage machines through a converged chassis controller, such as Cisco UCS.  You can choose how you want to control power on your machines based on what is available.  MAAS overwrites the machine's disk space with your chosen, pre-cached OS images.

[note type="negative" status="Warning"]
*The above comment about disk space bears repeating: MAAS will overwrite the disk space of all machines it enlists. All pool machines are under the control of MAAS; you should provision them using other methods.*
[/note]

MAAS users allocate ("acquire") machines for use when needed. The web UI also allows you to acquire machines manually, such as when you are reserving specific hardware for certain users. You can remotely access and customise the installed operating system via SSH.

rad-begin   /deb/2.9/ui   /snap/2.9/ui /deb/3.0/ui /snap/3.0/ui
<a href="https://discourse.maas.io/uploads/default/original/1X/8101d641c55d912cd66646bd99bbee9bb8f196ab.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/8101d641c55d912cd66646bd99bbee9bb8f196ab.jpeg"></a>
rad-end

rad-begin   /deb/2.9/cli   /snap/2.9/cli /deb/3.0/cli /snap/3.0/cli
<a href="https://discourse.maas.io/uploads/default/original/1X/ac3b251a916bb18a7e7e463d7fa3c57ef32628da.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/ac3b251a916bb18a7e7e463d7fa3c57ef32628da.jpeg"></a>

When acquiring machines from the API/CLI, you can specify requirements ("constraints"). Common constraints are memory, CPU cores, connected networks, and assigned physical zone.
rad-end

An acquired MAAS machine is more flexible than a virtual instance in a cloud. You have complete control, including hardware drivers and root access. If you want to upgrade the BIOS, for example, you can allocate a machine to yourself and complete the upgrade.  Once you have completed the upgrade, you can send the machine back to the pool.

Note that [Juju](https://juju.is/docs/olm/maas) is designed to work with MAAS. MAAS becomes a back-end Juju resource pool with all functionality fully available. For instance, if Juju removes a machine, then MAAS will release that machine to the pool.  With Juju, MAAS can become an integral part of your data centre strategy and operations.
