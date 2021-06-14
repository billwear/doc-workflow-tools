||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/vmware-images-snap-2-7-cli/3234) ~ [UI](/t/vmware-images-snap-2-7-ui/3235)|[CLI](/t/vmware-images-snap-2-8-cli/3236) ~ [UI](/t/vmware-images-snap-2-8-ui/3237)|[CLI](/t/vmware-images-snap-2-9-cli/3238) ~ [UI](/t/vmware-images-snap-2-9-ui/3239)|[CLI](/t/vmware-images-snap-3-0-cli/4173) ~ [UI](/t/vmware-images-snap-3-0-ui/4174)|
Packages|[CLI](/t/vmware-images-deb-2-7-cli/3240) ~ [UI](/t/vmware-images-deb-2-7-ui/3241)|[CLI](/t/vmware-images-deb-2-8-cli/3242) ~ [UI](/t/vmware-images-deb-2-8-ui/3243)|[CLI](/t/vmware-images-deb-2-9-cli/3244) ~ [UI](/t/vmware-images-deb-2-9-ui/3245)|[CLI](/t/vmware-images-deb-3-0-cli/4175) ~ [UI](/t/vmware-images-deb-3-0-ui/4176)|

MAAS 2.5 and above can deploy VMware ESXi as a custom image. MAAS cannot directly deploy the VMware ESXi ISO; you must create a specialised image from an official VMWare ISO. Canonical created a [packer](https://www.packer.io/) template to automate the image creation process.

#### Five questions you may have:

1. [What are the prerequisite requirements for creating an image?](#heading--prerequisites-to-create-the-images)
2. [How can I customise these images?](#heading--customizing-the-image)
3. [How do I build an image?](#heading--building-an-image)
4. [How do I upload an image?](#heading--uploading-an-image)
5. [What are the features and limitations of VMWare images in MAAS?](#heading--features-and-limitations)

<a href="#heading--prerequisites-to-create-the-images"><h2 id="heading--prerequisites-to-create-the-images">Prerequisites to image creation</h2></a>

<a href="#heading--image-creation"><h3 id="heading--image-creation">Image creation</h3></a>

1.   A physical machine running Ubuntu 18.04+
2.   **CPU**: 4 2GHz cores
3.   **Memory**: 8 GB RAM (16 GB RAM recommended)
4.   **Disk space**: 11 GB
5.   [The VMWare ESxi ISO](https://my.vmware.com/en/web/vmware/evalcenter?p=free-esxi6)
6.   [Packer - https://www.packer.io/intro/getting-started/install.html](https://www.packer.io/intro/getting-started/install.html)
7.   Procedure was tested with precompiled 64-bit Packer 1.3.4 Linux binaries
8.   <a href="https://github.com/canonical/packer-maas">Packer template</a> for MAAS custom image

<a href="#heading--image-deployment"><h3 id="heading--image-deployment">Image deployment</h3></a>

1.   MAAS 2.5.0+

<a href="#heading--customizing-the-image"><h2 id="heading--customizing-the-image">Customizing the Image</h2></a>

The image may be customized by modifying packer-maas/vmware-esxi/http/vmware-esxi-ks.cfg see Installation and Upgrade Scripts in the [VMware ESXi installation and Setup manual](https://docs.vmware.com/en/VMware-vSphere/6.7/vsphere-esxi-67-installation-setup-guide.pdf) for more information.

<a href="#heading--building-an-image"><h2 id="heading--building-an-image">Building an Image</h2></a>

Before an image is built the nbd kernel module must be loaded

    sudo modprobe nbd

Once the nbd kernel module is loaded your current working directory must be in the packer-maas/vmware-esxi directory

    cd /path/to/packer-maas/vmware-esxi

You can now start the image building process using packer with the following command:

    sudo packer build -var
    'vmware_esxi_iso_path=/path/to/VMware-VMvisor-Installer-6.7.0-8169922.x86_64.iso'
    vmware-esxi.json

<a href="#heading--uploading-an-image"><h2 id="heading--uploading-an-image">Uploading an Image</h2></a>

Once you have created the image, upload it to MAAS, using the CLI, with the following command:

    maas $PROFILE boot-resources create name='esxi/6.7' title='VMware ESXi 6.7'
    architecture='amd64/generic' filetype='ddgz' content@=vmware-esxi.dd.gz

<a href="#heading--features-and-limitations"><h2 id="heading--features-and-limitations">Features and Limitations</h2></a>

<a href="#heading--networking"><h3 id="heading--networking">Networking</h3></a>

1.   VMware ESXi does not support Linux bridges
2.   Bonds - MAAS maps the following bond modes to VMware ESXi NIC team sharing with load balancing as follows:
3.   balance-rr - portid
4.   active-backup - explicit
5.   802.3ad - iphash, LACP rate and XMIT hash policy settings are ignored.
6.   No other bond modes are currently supported.
7.   VMware ESXi does not allow VMs to use a PortGroup that has a VMK attached to it. All configured devices will have a VMK attached. To use a vSwitch with VMs, you must leave a device or alias unconfigured in MAAS.

<a href="#heading--storage"><h3 id="heading--storage">Storage</h3></a>

Custom storage configuration is not supported because VMware ESXi expects specific disk formats. MAAS will extend datastore1 to the full size of the deployment disk. After deployment, VMware tools may be used to access the other disks.

<a href="#heading--esxi-hardware-support"><h3 id="heading--esxi-hardware-support">ESXi Hardware Support</h3></a>

VMware has [very specific hardware requirements](https://www.vmware.com/resources/compatibility/search.php). In particular, running VMware ESXi is not supported in a virtual machine or MAAS virsh Pod.
