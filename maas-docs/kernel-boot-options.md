||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/kernel-boot-options-snap-2-7-cli/2778) ~ [UI](/t/kernel-boot-options-snap-2-7-ui/2779)|[CLI](/t/kernel-boot-options-snap-2-8-cli/2780) ~ [UI](/t/kernel-boot-options-snap-2-8-ui/2781)|[CLI](/t/kernel-boot-options-snap-2-9-cli/2782) ~ [UI](/t/kernel-boot-options-snap-2-9-ui/2783)|[CLI](/t/kernel-boot-options-snap-3-0-cli/3973) ~ [UI](/t/kernel-boot-options-snap-3-0-ui/3974)|
Packages|[CLI](/t/kernel-boot-options-deb-2-7-cli/2784) ~ [UI](/t/kernel-boot-options-deb-2-7-ui/2785)|[CLI](/t/kernel-boot-options-deb-2-8-cli/2786) ~ [UI](/t/kernel-boot-options-deb-2-8-ui/2787)|[CLI](/t/kernel-boot-options-deb-2-9-cli/2788) ~ [UI](/t/kernel-boot-options-deb-2-9-ui/2789)|[CLI](/t/kernel-boot-options-deb-3-0-cli/3975) ~ [UI](/t/kernel-boot-options-deb-3-0-ui/3976)|

MAAS can specify kernel boot options to machines on both a global basis (UI and CLI) and a per-machine basis (CLI-only). A full catalogue of available options can be found in the [Linux kernel parameters list](https://www.kernel.org/doc/html/latest/admin-guide/kernel-parameters.html) at [kernel.org](https://www.kernel.org).

#### Two questions you may have:

<!-- deb-2-7-cli
1. [How can I set global kernel boot options for all machines?](#heading--global-kernel-boot-options)
2. [How can I set kernel boot options for a specific machine?](/t/maas-tags-deb-2-7-cli/2892#heading--per-node-kernel-boot-options)
 deb-2-7-cli -->

<!-- deb-2-7-ui
1. [How can I set global kernel boot options for all machines?](#heading--global-kernel-boot-options)
2. [How can I set kernel boot options for a specific machine?](/t/maas-tags-deb-2-7-cli/2892#heading--per-node-kernel-boot-options)
 deb-2-7-ui -->

<!-- deb-2-8-cli
1. [How can I set global kernel boot options for all machines?](#heading--global-kernel-boot-options)
2. [How can I set kernel boot options for a specific machine?](/t/maas-tags-deb-2-8-cli/2894#heading--per-node-kernel-boot-options)
 deb-2-8-cli -->

<!-- deb-2-8-ui
1. [How can I set global kernel boot options for all machines?](#heading--global-kernel-boot-options)
2. [How can I set kernel boot options for a specific machine?](/t/maas-tags-deb-2-8-cli/2894#heading--per-node-kernel-boot-options)
 deb-2-8-ui -->

<!-- deb-2-9-cli
1. [How can I set global kernel boot options for all machines?](#heading--global-kernel-boot-options)
2. [How can I set kernel boot options for a specific machine?](/t/maas-tags-deb-2-9-cli/2896#heading--per-node-kernel-boot-options)
 deb-2-9-cli -->

<!-- deb-2-9-ui
1. [How can I set global kernel boot options for all machines?](#heading--global-kernel-boot-options)
2. [How can I set kernel boot options for a specific machine?](/t/maas-tags-deb-2-9-ui/2897#heading--per-node-kernel-boot-options)
 deb-2-9-ui -->

<!-- deb-3-0-cli
1. [How can I set global kernel boot options for all machines?](#heading--global-kernel-boot-options)
2. [How can I set kernel boot options for a specific machine?](/t/maas-tags-deb-3-0-cli/4023#heading--per-node-kernel-boot-options)
 deb-3-0-cli -->

<!-- deb-3-0-ui
1. [How can I set global kernel boot options for all machines?](#heading--global-kernel-boot-options)
2. [How can I set kernel boot options for a specific machine?](/t/maas-tags-deb-3-0-cli/4024#heading--per-node-kernel-boot-options)
 deb-3-0-ui -->

<!-- snap-2-7-cli
1. [How can I set global kernel boot options for all machines?](#heading--global-kernel-boot-options)
2. [How can I set kernel boot options for a specific machine?](/t/maas-tags-snap-2-7-cli/2886#heading--per-node-kernel-boot-options)
 snap-2-7-cli -->

<!-- snap-2-7-ui
1. [How can I set global kernel boot options for all machines?](#heading--global-kernel-boot-options)
2. [How can I set kernel boot options for a specific machine?](/t/maas-tags-snap-2-7-cli/2886#heading--per-node-kernel-boot-options)
 snap-2-7-ui -->

<!-- snap-2-8-cli
1. [How can I set global kernel boot options for all machines?](#heading--global-kernel-boot-options)
2. [How can I set kernel boot options for a specific machine?](/t/maas-tags-snap-2-8-cli/2888#heading--per-node-kernel-boot-options)
 snap-2-8-cli -->

<!-- snap-2-8-ui
1. [How can I set global kernel boot options for all machines?](#heading--global-kernel-boot-options)
2. [How can I set kernel boot options for a specific machine?](/t/maas-tags-snap-2-8-cli/2888#heading--per-node-kernel-boot-options)
 snap-2-8-ui -->

<!-- snap-2-9-cli
1. [How can I set global kernel boot options for all machines?](#heading--global-kernel-boot-options)
2. [How can I set kernel boot options for a specific machine?](/t/maas-tags-snap-2-9-cli/2890#heading--per-node-kernel-boot-options)
 snap-2-9-cli -->

<!-- snap-2-9-ui
1. [How can I set global kernel boot options for all machines?](#heading--global-kernel-boot-options)
2. [How can I set kernel boot options for a specific machine?](/t/maas-tags-snap-2-9-ui/2891#heading--per-node-kernel-boot-options)
 snap-2-9-ui -->

<!-- snap-3-0-cli
1. [How can I set global kernel boot options for all machines?](#heading--global-kernel-boot-options)
2. [How can I set kernel boot options for a specific machine?](/t/maas-tags-snap-3-0-cli/4021#heading--per-node-kernel-boot-options)
 snap-3-0-cli -->

<!-- snap-3-0-ui
1. [How can I set global kernel boot options for all machines?](#heading--global-kernel-boot-options)
2. [How can I set kernel boot options for a specific machine?](/t/maas-tags-snap-3-0-ui/4022#heading--per-node-kernel-boot-options)
 snap-3-0-ui -->

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 

<a href="#heading--global-kernel-boot-options"><h2 id="heading--global-kernel-boot-options">Global kernel boot options</h2></a>

To set kernel boot options globally, as an admin, open the 'Settings' page and on the 'General' tab scroll down to the 'Global Kernel Parameters' section:

<a href="https://assets.ubuntu.com/v1/8b793b6d-nodes-kernel-options__2.2_global.png" target = "_blank"><img src="https://assets.ubuntu.com/v1/8b793b6d-nodes-kernel-options__2.2_global.png"></a>

Type in the desired (space separated) options and click 'Save'. The contents of the field will be used as-is. Do not use extra characters.
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui  -->

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 


<a href="#heading--cli"><h2 id="heading--cli">Global kernel boot options</h2></a>

You can set kernel boot options and apply them to all machines with the CLI command:

``` bash
maas $PROFILE maas set-config name=kernel_opts value='$KERNEL_OPTIONS'
```
snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli  -->
