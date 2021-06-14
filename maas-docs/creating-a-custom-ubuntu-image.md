||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/creating-a-custom-ubuntu-image-snap-2-7-cli/2562) ~ [UI](/t/creating-a-custom-ubuntu-image-snap-2-7-ui/2563)|[CLI](/t/creating-a-custom-ubuntu-image-snap-2-8-cli/2564) ~ [UI](/t/creating-a-custom-ubuntu-image-snap-2-8-ui/2565)|[CLI](/t/creating-a-custom-ubuntu-image-snap-2-9-cli/2566) ~ [UI](/t/creating-a-custom-ubuntu-image-snap-2-9-ui/2567)|[CLI](/t/creating-a-custom-ubuntu-image-snap-3-0-cli/3901) ~ [UI](/t/creating-a-custom-ubuntu-image-snap-3-0-ui/3902)|
Packages|[CLI](/t/creating-a-custom-ubuntu-image-deb-2-7-cli/2568) ~ [UI](/t/creating-a-custom-ubuntu-image-deb-2-7-ui/2569)|[CLI](/t/creating-a-custom-ubuntu-image-deb-2-8-cli/2570) ~ [UI](/t/creating-a-custom-ubuntu-image-deb-2-8-ui/2571)|[CLI](/t/creating-a-custom-ubuntu-image-deb-2-9-cli/2572) ~ [UI](/t/creating-a-custom-ubuntu-image-deb-2-9-ui/2573)|[CLI](/t/creating-a-custom-ubuntu-image-deb-3-0-cli/3903) ~ [UI](/t/creating-a-custom-ubuntu-image-deb-3-0-ui/3904)|

# Introduction

<!-- deb-2-7-cli
MAAS supports deploying custom DD or TGZ images. Canonical provides both [lp:maas-image-builder](https://launchpad.net/maas-image-builder) and [gh:canonical/packer-maas](https://github.com/canonical/packer-maas) to support creating custom images however these tools do not currently support Ubuntu. Instead Canonical suggests customising Ubuntu using [cloud-init user_data](https://discourse.maas.io/t/customizing-maas-deployments-with-cloud-init/165) or [Curtin preseed data](/t/custom-machine-setup/2592).
 deb-2-7-cli -->

<!-- deb-2-7-ui
MAAS supports deploying custom DD or TGZ images. Canonical provides both [lp:maas-image-builder](https://launchpad.net/maas-image-builder) and [gh:canonical/packer-maas](https://github.com/canonical/packer-maas) to support creating custom images however these tools do not currently support Ubuntu. Instead Canonical suggests customising Ubuntu using [cloud-init user_data](https://discourse.maas.io/t/customizing-maas-deployments-with-cloud-init/165) or [Curtin preseed data](/t/custom-machine-setup/2593).
 deb-2-7-ui -->

<!-- deb-2-8-cli
MAAS supports deploying custom DD or TGZ images. Canonical provides both [lp:maas-image-builder](https://launchpad.net/maas-image-builder) and [gh:canonical/packer-maas](https://github.com/canonical/packer-maas) to support creating custom images however these tools do not currently support Ubuntu. Instead Canonical suggests customising Ubuntu using [cloud-init user_data](https://discourse.maas.io/t/customizing-maas-deployments-with-cloud-init/165) or [Curtin preseed data](/t/custom-machine-setup/2594).
 deb-2-8-cli -->

<!-- deb-2-8-ui
MAAS supports deploying custom DD or TGZ images. Canonical provides both [lp:maas-image-builder](https://launchpad.net/maas-image-builder) and [gh:canonical/packer-maas](https://github.com/canonical/packer-maas) to support creating custom images however these tools do not currently support Ubuntu. Instead Canonical suggests customising Ubuntu using [cloud-init user_data](https://discourse.maas.io/t/customizing-maas-deployments-with-cloud-init/165) or [Curtin preseed data](/t/custom-machine-setup/2595).
 deb-2-8-ui -->

<!-- deb-2-9-cli
MAAS supports deploying custom DD or TGZ images. Canonical provides both [lp:maas-image-builder](https://launchpad.net/maas-image-builder) and [gh:canonical/packer-maas](https://github.com/canonical/packer-maas) to support creating custom images however these tools do not currently support Ubuntu. Instead Canonical suggests customising Ubuntu using [cloud-init user_data](https://discourse.maas.io/t/customizing-maas-deployments-with-cloud-init/165) or [Curtin preseed data](/t/custom-machine-setup/2596).
 deb-2-9-cli -->

<!-- deb-2-9-ui
MAAS supports deploying custom DD or TGZ images. Canonical provides both [lp:maas-image-builder](https://launchpad.net/maas-image-builder) and [gh:canonical/packer-maas](https://github.com/canonical/packer-maas) to support creating custom images however these tools do not currently support Ubuntu. Instead Canonical suggests customising Ubuntu using [cloud-init user_data](https://discourse.maas.io/t/customizing-maas-deployments-with-cloud-init/165) or [Curtin preseed data](/t/custom-machine-setup/2597).
 deb-2-9-ui -->

<!-- deb-3-0-cli
MAAS supports deploying custom DD or TGZ images. Canonical provides both [lp:maas-image-builder](https://launchpad.net/maas-image-builder) and [gh:canonical/packer-maas](https://github.com/canonical/packer-maas) to support creating custom images however these tools do not currently support Ubuntu. Instead Canonical suggests customising Ubuntu using [cloud-init user_data](https://discourse.maas.io/t/customizing-maas-deployments-with-cloud-init/165) or [Curtin preseed data](/t/custom-machine-setup/3911).
 deb-3-0-cli -->

<!-- deb-3-0-ui
MAAS supports deploying custom DD or TGZ images. Canonical provides both [lp:maas-image-builder](https://launchpad.net/maas-image-builder) and [gh:canonical/packer-maas](https://github.com/canonical/packer-maas) to support creating custom images however these tools do not currently support Ubuntu. Instead Canonical suggests customising Ubuntu using [cloud-init user_data](https://discourse.maas.io/t/customizing-maas-deployments-with-cloud-init/165) or [Curtin preseed data](/t/custom-machine-setup/3912).
 deb-3-0-ui -->

<!-- snap-2-7-cli
MAAS supports deploying custom DD or TGZ images. Canonical provides both [lp:maas-image-builder](https://launchpad.net/maas-image-builder) and [gh:canonical/packer-maas](https://github.com/canonical/packer-maas) to support creating custom images however these tools do not currently support Ubuntu. Instead Canonical suggests customising Ubuntu using [cloud-init user_data](https://discourse.maas.io/t/customizing-maas-deployments-with-cloud-init/165) or [Curtin preseed data](/t/custom-machine-setup/2586).
 snap-2-7-cli -->

<!-- snap-2-7-ui
MAAS supports deploying custom DD or TGZ images. Canonical provides both [lp:maas-image-builder](https://launchpad.net/maas-image-builder) and [gh:canonical/packer-maas](https://github.com/canonical/packer-maas) to support creating custom images however these tools do not currently support Ubuntu. Instead Canonical suggests customising Ubuntu using [cloud-init user_data](https://discourse.maas.io/t/customizing-maas-deployments-with-cloud-init/165) or [Curtin preseed data](/t/custom-machine-setup/2587).
 snap-2-7-ui -->

<!-- snap-2-8-cli
MAAS supports deploying custom DD or TGZ images. Canonical provides both [lp:maas-image-builder](https://launchpad.net/maas-image-builder) and [gh:canonical/packer-maas](https://github.com/canonical/packer-maas) to support creating custom images however these tools do not currently support Ubuntu. Instead Canonical suggests customising Ubuntu using [cloud-init user_data](https://discourse.maas.io/t/customizing-maas-deployments-with-cloud-init/165) or [Curtin preseed data](/t/custom-machine-setup/2588).
 snap-2-8-cli -->

<!-- snap-2-8-ui
MAAS supports deploying custom DD or TGZ images. Canonical provides both [lp:maas-image-builder](https://launchpad.net/maas-image-builder) and [gh:canonical/packer-maas](https://github.com/canonical/packer-maas) to support creating custom images however these tools do not currently support Ubuntu. Instead Canonical suggests customising Ubuntu using [cloud-init user_data](https://discourse.maas.io/t/customizing-maas-deployments-with-cloud-init/165) or [Curtin preseed data](/t/custom-machine-setup/2589).
 snap-2-8-ui -->

<!-- snap-2-9-cli
MAAS supports deploying custom DD or TGZ images. Canonical provides both [lp:maas-image-builder](https://launchpad.net/maas-image-builder) and [gh:canonical/packer-maas](https://github.com/canonical/packer-maas) to support creating custom images however these tools do not currently support Ubuntu. Instead Canonical suggests customising Ubuntu using [cloud-init user_data](https://discourse.maas.io/t/customizing-maas-deployments-with-cloud-init/165) or [Curtin preseed data](/t/custom-machine-setup/2590).
 snap-2-9-cli -->

<!-- snap-2-9-ui
MAAS supports deploying custom DD or TGZ images. Canonical provides both [lp:maas-image-builder](https://launchpad.net/maas-image-builder) and [gh:canonical/packer-maas](https://github.com/canonical/packer-maas) to support creating custom images however these tools do not currently support Ubuntu. Instead Canonical suggests customising Ubuntu using [cloud-init user_data](https://discourse.maas.io/t/customizing-maas-deployments-with-cloud-init/165) or [Curtin preseed data](/t/custom-machine-setup/2591).
 snap-2-9-ui -->

<!-- snap-3-0-cli
MAAS supports deploying custom DD or TGZ images. Canonical provides both [lp:maas-image-builder](https://launchpad.net/maas-image-builder) and [gh:canonical/packer-maas](https://github.com/canonical/packer-maas) to support creating custom images however these tools do not currently support Ubuntu. Instead Canonical suggests customising Ubuntu using [cloud-init user_data](https://discourse.maas.io/t/customizing-maas-deployments-with-cloud-init/165) or [Curtin preseed data](/t/custom-machine-setup/3911).
 snap-3-0-cli -->

<!-- snap-3-0-ui
MAAS supports deploying custom DD or TGZ images. Canonical provides both [lp:maas-image-builder](https://launchpad.net/maas-image-builder) and [gh:canonical/packer-maas](https://github.com/canonical/packer-maas) to support creating custom images however these tools do not currently support Ubuntu. Instead Canonical suggests customising Ubuntu using [cloud-init user_data](https://discourse.maas.io/t/customizing-maas-deployments-with-cloud-init/165) or [Curtin preseed data](/t/custom-machine-setup/3912).
 snap-3-0-ui -->

# Why customised Ubuntu deployments aren't supported
When the [MAAS stream](https://images.maas.io/ephemeral-v3/stable/) is generated by [lp:maas-images](https://launchpad.net/maas-images) it starts by downloading the base SquashFS rootfs from cloud-images.ubuntu.com that is used for all clouds. The SquashFS does not contain a kernel so [lp:maas-images](https://launchpad.net/maas-images) mounts the SquashFS with an overlay and chroots in. It then  installs a kernel and extra initramfs scripts from the cloud-initramfs-rooturl and cloud-initramfs-copymods packages to allow network booting. Once everything is installed the kernel and newly generated initramfs are pulled out of the overlay and everything is unmounted. [lp:maas-images](https://launchpad.net/maas-images) provides the unmodified SquashFS, installed kernel, and generated initramfs as separate files on images.maas.io.

MAAS uses the kernel, initramfs, and SquashFS to perform network booting which allows commissioning, testing, and deployments. When deploying Ubuntu MAAS uses the same version of Ubuntu to network boot into and perform the deployment. This ensures there are no compatibility issues. Other operating systems use the Ubuntu version selected for the ephemeral environment for deployment.

Currently MAAS only allows custom images to be loaded as a single TGZ or DD.GZ, there is no way to upload a kernel, `initrd`, and `rootfs` as separate files. Even if MAAS was modified to allow the kernel, `initrd`, and `rootfs` as separate files MAAS requires `cloud-initramfs-copymods` and `cloud-initramfs-rooturl` to be included in the initrd. It is difficult for MAAS to detect if these scripts are missing and even harder for users to debug if they are missing.

# Warnings on creating a custom Ubuntu image
1. Custom images are always deployed with the ephemeral operating system. This can cause hard to debug errors. For example CentOS 6 can only be deployed by Ubuntu Xenial due to advances in the ext4 filesystem.
2. MAAS will still install and configure the GA kernel. If your custom image contains a kernel it most likely won't be used. MAAS will not allow you to select which kernel(GA, HWE, lowlatency, etc) when deploying a custom Ubuntu image.
3. All GNU/Linux custom images should be created as a TGZ to enable storage customisation. When a DD.GZ is used MAAS/Curtin simply writes the file to the filesystem.

# How to create a custom Ubuntu image for MAAS

Note: LXD may prevent device files from being created when extracting the rootfs, it is suggested to do this on metal or on a VM:

1. Download the rootfs from images.maas.io
    `wget http://cloud-images.ubuntu.com/focal/current/focal-server-cloudimg-amd64-root.tar.xz`
2. Create a work directory
    `mkdir /tmp/work`
3. Extract the rootfs
    `cd /tmp/work`
    `sudo tar xf ../focal-server-cloudimg-amd64-root.tar.xz`

    or

   `unsquashfs ../focal-server-cloudimg-amd64-root.squash`
4. Setup chroot
   `sudo mount -o bind /proc /tmp/work/proc`
   `sudo mount -o bind /dev /tmp/work/dev`
   `sudo mount -o bind /sys /tmp/work/sys`
   `sudo mv /tmp/work/etc/resolv.conf /tmp/work/etc/resolv.conf.bak`
   `sudo cp /etc/resolv.conf /tmp/work/etc/`
5. Chroot in
    `sudo chroot /tmp/work /bin/bash`
6. Customise image
    `apt update`
    `apt dist-upgrade`
   `apt install emacs-nox jq tree`
    `apt autoremove`
7. Exit chroot and unmount binds
  `exit`
   `sudo umount /tmp/work/proc`
   `sudo umount /tmp/work/dev`
   `sudo umount /tmp/work/sys`
   `sudo mv /tmp/work/etc/resolv.conf.bak /tmp/work/etc/resolv.conf`
8. Create TGZ
   `sudo tar -czf /tmp/focal-custom.tgz -C /tmp/work .`
9. Upload it to MAAS
    Note: Ubuntu release names and versions are reserved
    `maas $PROFILE boot-resources create name='custom/focal-custom' title='Ubuntu 20.04 Custom Image' architecture='amd64/generic' filetype='tgz' content@=focal-custom.tgz`
10. Configure and deploy as normal
