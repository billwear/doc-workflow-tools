||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/maas-image-builder-snap-2-7-cli/2850) ~ [UI](/t/maas-image-builder-snap-2-7-ui/2851)|[CLI](/t/maas-image-builder-snap-2-8-cli/2852) ~ [UI](/t/maas-image-builder-snap-2-8-ui/2853)|[CLI](/t/maas-image-builder-snap-2-9-cli/2854) ~ [UI](/t/maas-image-builder-snap-2-9-ui/2855)|[CLI](/t/maas-image-builder-snap-3-0-cli/3997) ~ [UI](/t/maas-image-builder-snap-3-0-ui/3998)|
Packages|[CLI](/t/maas-image-builder-deb-2-7-cli/2856) ~ [UI](/t/maas-image-builder-deb-2-7-ui/2857)|[CLI](/t/maas-image-builder-deb-2-8-cli/2858) ~ [UI](/t/maas-image-builder-deb-2-8-ui/2859)|[CLI](/t/maas-image-builder-deb-2-9-cli/2860) ~ [UI](/t/maas-image-builder-deb-2-9-ui/2861)|[CLI](/t/maas-image-builder-deb-3-0-cli/3999) ~ [UI](/t/maas-image-builder-deb-3-0-ui/4000)|

MAAS Image Builder is an alternative to [Packer](https://www.packer.io/) for creating MAAS images.

[note]
In order to use MAAS Image Builder, you must purchase [Ubuntu Advantage for Infrastructure](https://support.canonical.com/ua/s/article/How-to-access-the-MAAS-Image-Builder-tool).
[/note]

<!-- awaiting review
[note]
In order to use MAAS Image Builder, you must purchase [Ubuntu Advantage for Infrastructure](https://support.canonical.com/ua/s/article/How-to-access-the-MAAS-Image-Builder-tool).
That said, you may want to try Packer first, before committing to MAAS Image Builder, as Packer is free and open-source. You should note, though, that Packer is offered by another firm.  Canonical has no special channel to request features or bug fixes, and no insight into their release and maintenance schedules.  Packer is not rigorously tested with all images used by MAAS, and may not work with all images deployed by MAAS users.  We feel it's important to help you make an informed decision on this -- but we encourage you to try Packer first, with the caveat that Canonical can't make any particular guarantees about whether or not it will serve your particular needs.
[/note]
 -->

With the MAAS Image Builder, you can do five key operations:

1. <a href="#imib">install MAAS Image Builder</a> via a private Canonical PPA (which you can request)
2. <a href="#bci">create custom CentOS images</a>
3. <a href="#bri">create custom RHEL images</a>
4. <a href="#bwi">create Windows images</a>
5. <a href="#doci">create other kinds of custom images</a>

You can customise most images as much or as little as you wish, then use them to commission machines with MAAS. 

<h2 id="heading--install-mib">Install MAAS Image Builder</h2></a>

To get MAAS Image Builder, you must be subscribed to a private PPA provided by Canonical Support to those customers who have purchased [Ubuntu Advantage for Infrastructure](https://support.canonical.com/ua/s/article/How-to-access-the-MAAS-Image-Builder-tool).  Note that the steps below will fail if you have not purchased Ubuntu Advantage and been subscribed to the private PPA by your Canonical support rep.

Once subscribed, you need to obtain your credentials at this external link:

https://launchpad.net/~/+archivesubscriptions

Also, you must add the repository with the <code>add-apt-repository</code> command.  Note: Be sure to substitute your unique URL in the command below:

    $ sudo add-apt-repository \
    “https://LaunchpadID:Password@private-ppa.launchpad.net/maas-image-builder-partners/stable/ubuntu"

Once you have added the private PPA, you can install the Image Builder like this:

    $ sudo apt-get install maas-image-builder

All done? Great!  Now you can build and customise images for MAAS machines, as shown in the sections below.

<h2 id="heading--custom-centos-images">Create custom CentOS images</h2></a>

MAAS already provides the latest available CentOS 6, CentOS 7, and CentOS 8 for automatic download. If you need something else, though, MAAS Image Builder supports the ability to create various CentOS images.

<h3 id="heading--centos-nw-rqmts">Network Requirements</h3>

Access to the Internet is required, since you will need to start with one of these three sites:

1. http://mirror.centos.org  - OS, updates, and extra repositories
2. https://download.fedoraproject.org  - EPEL
3. https://copr-be.cloud.fedoraproject.org - Canonical maintained cloud-init repository

<h3 id="heading--images-behind-proxy">Creating images behind a proxy</h3>

MAAS Image Builder can create CentOS images behind a proxy -- just set the ‘http_proxy’ environment variable to _your_ particular proxy. Once deployed, <code>yum</code> will use this MAAS-configured proxy.

<h3 id="heading--centos-create-images">Creating the images</h3>

<code>maas-image-builder</code> is designed to automate the process of generating the images for MAAS and <code>curtin</code>.  Here are some specific examples:

    $ sudo maas-image-builder -o centos6-amd64-root-tgz --arch amd64 centos --edition 6 
    $ sudo maas-image-builder -o centos6-i386-root-tgz --arch i386 centos --edition 6
    $ sudo maas-image-builder -o centos7-amd64-root-tgz --arch amd64 centos --edition 7

<h3 id="heading--centos-customize-images">Customising CentOS images</h3>

Starting from MAAS Image Builder 1.0.4, customisation of CentOS images is now supported.  You can provide a custom kickstart, in _addition_ to the kickstart that MAAS Image Builder uses to create the images. You can customise your image like this:

    $ sudo maas-image-builder -o centos7-amd64-root-tgz --arch amd64 centos --edition 7 --custom-kickstart ./custom.ks

<h3 id="heading--centos-upload-images">Uploading the image into MAAS</h3>

Custom CentOS images can be uploaded to MAAS as shown in the command below.  _Do note_ that the name **must** start with ‘centos’ and **must** be one line:

    maas admin boot-resources create name=centos/centos6-custom architecture=amd64/generic content@=./build-output/centos-amd64-root-tgz

You can use the MAAS WebUI to check that your custom CentOS image is valid and selectable for deployment.

<h2 id="heading--custom-rhel-images">Building RHEL images</h2></a>

Currently, MAAS _only_ supports RHEL as a custom image. In future versions of MAAS, RHEL will be natively supported.

<h3 id="heading--rhel-requirements">Some Requirements</h3>

In order to create RHEL images, you will need access to these three sites:

1. A RHEL DVD ISO - Contains all RHEL archives which are not available without a license
2. https://download.fedoraproject.org - Access to the EPEL repository to install required deps
3. https://copr-be.cloud.fedoraproject.org - Access to the Canonical maintained cloud-init copr repository

<h3 id="heading--rhel-behind-proxy">Creating images behind a proxy</h3>

MAAS image builder supports creating RHEL images behind a proxy. To use a proxy when building a RHEL image, just set the ‘http_proxy’ environment variable to _your_ local proxy. Once deployed, <code>yum</code> will use the MAAS-configured proxy.

<h3 id="heading--rhel-create-images">Creating the images</h3>

To generate a usable RHEL image, <code>maas-image-builder</code> automates image generation; these images can be used by MAAS and <code>curtin</code>.

     $ sudo maas-image-builder -a amd64 -o rhel7-amd64-root-tgz rhel --rhel-iso blah.iso

<h3 id="heading--rhel-install">Install into MAAS</h3>

The custom RHEL image can be uploaded to MAAS, but note that the name **must** start with ‘rhel’ and **must** be expressed as a single line, like this:

    maas admin boot-resources create name=rhel/7 title="RedHat Enterprise Linux 7" architecture=amd64/generic content@=rhel7-amd64-root-tgz

<h2 id="heading--custom-windows-images">Building Windows Images</h2></a>

Since Windows is a proprietary operating system, MAAS can't download these images. You need to manually generate images to use with MAAS.  On the upside, the end result will be much simpler, since there are CLI and WebUI tools to upload a Windows ISO -- which _helps_ automate the process.

<b>Hyper-V 2012 R2</b>
In this example, Windows Hyper-V 2012 R2 is used, but rest assured that multiple versions are supported. Download the Hyper-V 2012 R2 ISO from Microsoft, so it can be used in the image generation process.  You can obtain the download at:

http://technet.microsoft.com/en-US/evalcenter/dn205299.aspx

There are six other supported versions (for --windows-edition):

1. win2012
2. win2012r2
3. win2012hv
4. win2012hvr2
5. win2016
6. win2016hv

<h3 id="heading--mib-windows">Image Builder</h3>

MAAS Image builder can automate the process of generating images for MAAS and <code>curtin</code>.  In this instance,  though, you need Windows drivers for your specific hardware.  You can obtain these windows drivers with the following command:

    sudo maas-image-builder -o windows-win2012hvr2-amd64-root-dd  windows \
    --windows-iso ~/Downloads/2012hvr2.ISO \
    --windows-edition win2012hvr2 [--windows-updates] \
    [--windows-drivers <folder/>]  [--windows-language en-US]

As an example, consider:

    sudo maas-image-builder -o windows-win2012hvr2-amd64-root-dd windows \
    --windows-iso win2012hvr2.iso  --windows-edition win2012hvr2 \
    --windows-updates --windows-drivers ~/Win2012hvr2_x64/DRIVERS/  --windows-language en-US

Please note that this will not <em>install</em> any Windows updates. In order to obtain an up-to-date image of Windows, be sure provide the <code>--windows-updates</code> flag. This requires access to a bridged connection with a DHCP server, an interface that can be specified with <code>-i</code>.

Also note that you may be required to have specific Windows drivers for this image to work in your hardware. Be sure you inject those drivers when installing them. Those drivers are the default <code>*.inf</code> files.

<h3 id="heading--mib-debug-windows">Debug</h3>

You can debug the Windows installation process by connecting to <code>localhost:5901</code> using a VNC client.

<h3 id="heading--windows-image-install">Install into MAAS</h3>

The generated images need to be placed into the correct directories so MAAS can deploy them onto a node:

    maas admin boot-resources create name=windows/win2012hvr2 \
    architecture=amd64/generic filetype=ddtgz \ 
    content@=./build-output/windows-win2012hvr2-amd64-root-dd 

Now, using the MAAS WebUI, a node can be selected to use Windows Hyper-V 2012 R2. This selection gets reset when a node is stopped, so make sure to set it _before_ starting nodes. You can also set the default operating system (and release) in the settings menu, which removes the need to set it per-node.

<h2 id="heading--other-custom-images">Dealing with other custom images</h2></a>

To install other custom images, use the following command sequence:

    maas <user> boot-resources create name=<custom-image-codename> title="Ubuntu Custom Image" \
    architecture=amd64/generic content@=/location/of/custom/image/ubuntu-custom-root-tgz

As an example:

    maas admin boot-resources create name=custom1 \
    title=”Ubuntu Custom Image” architecture=amd64/generic \
    content@=/home/ubuntu/ubuntu-custom-root-tgz
