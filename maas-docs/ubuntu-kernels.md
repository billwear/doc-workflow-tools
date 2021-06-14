||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/ubuntu-kernels-snap-2-7-cli/3174) ~ [UI](/t/ubuntu-kernels-snap-2-7-ui/3175)|[CLI](/t/ubuntu-kernels-snap-2-8-cli/3176) ~ [UI](/t/ubuntu-kernels-snap-2-8-ui/3177)|[CLI](/t/ubuntu-kernels-snap-2-9-cli/3178) ~ [UI](/t/ubuntu-kernels-snap-2-9-ui/3179)|[CLI](/t/ubuntu-kernels-snap-3-0-cli/4137) ~ [UI](/t/ubuntu-kernels-snap-3-0-ui/4138)|
Packages|[CLI](/t/ubuntu-kernels-deb-2-7-cli/3180) ~ [UI](/t/ubuntu-kernels-deb-2-7-ui/3181)|[CLI](/t/ubuntu-kernels-deb-2-8-cli/3182) ~ [UI](/t/ubuntu-kernels-deb-2-8-ui/3183)|[CLI](/t/ubuntu-kernels-deb-2-9-cli/3184) ~ [UI](/t/ubuntu-kernels-deb-2-9-ui/3185)|[CLI](/t/ubuntu-kernels-deb-3-0-cli/4139) ~ [UI](/t/ubuntu-kernels-deb-3-0-ui/4140)|

MAAS supports four types of kernels for its Ubuntu machines:

1.   General availability kernels
2.   Hardware enablement kernels
3.   Hardware enablement kernels (pre-release)
4.   Low latency kernels

This article explains each of these kernels, and offers instructions and further references regarding their use.

#### Seven questions you may have:

1. [What is a general availability kernel?](#heading--general-availability-kernels)
2. [What is a hardware enablement kernel?](#heading--hardware-enablement-kernels)
3. [What is a pre-release hardware enablement kernel?](#heading--hardware-enablement-kernels-pre-release)
4. [What is a low latency kernel?](#heading--low-latency-kernels)
5. [How do I set a minimum kernel for enlistment and commissioning?](#heading--set-a-default-minimum-kernel-for-enlistment-and-commissioning)
6. [How to I set a minimum deploy kernel for a machine?](#heading--set-a-minimum-deploy-kernel-for-a-machine)
7. [How do I set a specific kernel during machine deployment?](#heading--set-a-specific-kernel-during-machine-deployment)

<a href="#heading--general-availability-kernels"><h2 id="heading--general-availability-kernels">General availability kernels</h2></a>

The *general availability* (GA) kernel is based on the *generic* kernel that ships with a new Ubuntu version. Subsequent fixes are applied regularly by the 'stable' *stream* used when setting up the global image source for MAAS.

MAAS denotes a GA kernel like this:

`ga-<version>`: The GA kernel reflects the major kernel version of the shipped Ubuntu release. For example, 'ga-16.04' is based on the 'generic' 4.4 Ubuntu kernel. As per Ubuntu policy, a GA kernel will never have its major version upgraded until the underlying release is upgraded.

<a href="#heading--hardware-enablement-kernels"><h2 id="heading--hardware-enablement-kernels">Hardware enablement kernels</h2></a>

New hardware gets released all the time. If an Ubuntu host runs an older kernel, it's unlikely that MAAS can support the hardware. Canonical does make every effort to back-port more recent kernels enabling more hardware. The acronym HWE stands for "Hardware Enablement."

You also gain kernel improvements and new features when installing an HWE kernel.

[note]
There is the notion of an HWE *stack*, which refers to the window manager and kernel when the Ubuntu host is running a desktop environment. HWE stacks do not apply to MAAS since machines are provisioned strictly as non-graphical servers.
[/note]

Note that these back-ported/HWE kernels are only available for LTS releases (e.g. Trusty, Xenial, etc.). For example, the first available HWE kernel for Ubuntu 16.04 LTS (Xenial) will be the GA kernel from Ubuntu 16.10 (Yakkety).

Before MAAS 2.1 on Xenial, HWE kernels are referred to by the notation `hwe-<release letter>`. So, to install the Yakkety HWE kernel on Xenial, the `hwe-y` kernel is used. By default, when using the web UI, MAAS imports all available HWE kernels along with its generic boot images. So if you are importing Trusty images, then the following HWE kernels are included: `hwe-u`, `hwe-v`, `hwe-w`, `hwe-x` (presuming the Xenial HWE kernel is available).

In MAAS 2.1, starting with Xenial kernels, the notation has changed. The following is used to refer to the latest HWE kernel available for Xenial: `hwe-16.04`.

See [LTS Enablement Stack](https://wiki.ubuntu.com/Kernel/LTSEnablementStack) (Ubuntu wiki) for the latest information on HWE.

<a href="#heading--hardware-enablement-kernels-pre-release"><h2 id="heading--hardware-enablement-kernels-pre-release">Hardware enablement kernels (pre-release)</h2></a>

The pre-release HWE kernel is known as the *edge* HWE kernel.

MAAS denotes the edge kernel like this: `hwe-<version>-edge`.

So 'hwe-16.04' is considered older than 'hwe-16.04-edge'.

See [Rolling LTS Enablement Stack](https://wiki.ubuntu.com/Kernel/RollingLTSEnablementStack#hwe-16.04-edge) (Ubuntu wiki) for more information.

<a href="#heading--low-latency-kernels"><h2 id="heading--low-latency-kernels">Low latency kernels</h2></a>

The low-latency kernel is based on the GA kernel, but uses a more aggressive configuration to reduce latency. It is categorised as a soft real-time kernel. For more information, see [Criteria for real-time computing](https://en.wikipedia.org/wiki/Real-time_computing#Criteria_for_real-time_computing) (Wikipedia).

MAAS denotes a low latency kernel in three ways:

1.   `hwe-x-lowlatency`: the Xenial low latency HWE kernel for Trusty
2.   `ga-16.04-lowlatency`: the low latency GA kernel for Xenial
3.   `hwe-16.04-lowlatency`: the low latency HWE kernel for Xenial

<a href="#heading--using-kernels"><h2 id="heading--using-kernels">Using kernels</h2></a>

The kernel installed on a machine during deployment is, by default, the Ubuntu release's native kernel (GA). However, it is possible to tell MAAS to use a different kernel. Via the Web UI, MAAS can help you choose one of these kernels.  There are three different contexts for your choice:

1.   globally (default minimum enlistment and commissioning kernel)
2.   per machine (minimum deploy kernel)
3.   per machine during deployment (specific deploy kernel)

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
<a href="#heading--set-a-default-minimum-kernel-for-enlistment-and-commissioning"><h2 id="heading--set-a-default-minimum-kernel-for-enlistment-and-commissioning">Set a default minimum kernel for enlistment and commissioning</h2></a>

To set the default minimum enlistment and commissioning kernel (based on Ubuntu release: GA kernel) for all machines visit the 'General' tab of the 'Settings' page and select a kernel in the 'Default Minimum Kernel Version' field of the *Commissioning* section. Don't forget to click 'Save'.

<a href="https://assets.ubuntu.com/v1/e0c7f298-nodes-kernels__2.6-default-minimum-kernel.png" target = "_blank"><img src="https://assets.ubuntu.com/v1/e0c7f298-nodes-kernels__2.6-default-minimum-kernel.png"></a>

<a href="#heading--set-a-minimum-deploy-kernel-for-a-machine"><h2 id="heading--set-a-minimum-deploy-kernel-for-a-machine">Set a minimum deploy kernel for a machine</h2></a>

To set the minimum deploy kernel on a machine basis, click on a machine from the 'Machines' page of the web UI and switch to its 'Configuration' page. Click 'Edit' in the 'Machine configuration' section, select a kernel in the 'Minimum Kernel' field followed by 'Save changes'.

<a href="https://assets.ubuntu.com/v1/e1016632-nodes-kernels__2.6-machine-minimum-kernel.png" target = "_blank"><img src="https://assets.ubuntu.com/v1/e1016632-nodes-kernels__2.6-machine-minimum-kernel.png"></a>

<a href="#heading--set-a-specific-kernel-during-machine-deployment"><h2 id="heading--set-a-specific-kernel-during-machine-deployment">Set a specific kernel during machine deployment</h2></a>

To set a specific kernel during deployment, select a machine from the 'Machines' page and choose 'Deploy' under 'Take action'. Then choose a kernel from the (third) kernel field. Hit 'Deploy machine' to initiate the deployment.

<a href="https://assets.ubuntu.com/v1/0d25737f-nodes-kernels__2.6-machine-during-deploy-kernel.png" target = "_blank"><img src="https://assets.ubuntu.com/v1/0d25737f-nodes-kernels__2.6-machine-during-deploy-kernel.png"></a>

MAAS verifies that the specified kernel is available for the given Ubuntu release (series) before deploying the machine.
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui  snap-3-0-ui deb-3-0-ui -->

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 
<a href="#heading--set-a-default-minimum-kernel-for-enlistment-and-commissioning"><h2 id="heading--set-a-default-minimum-kernel-for-enlistment-and-commissioning">Set a default minimum kernel for enlistment and commissioning</h2></a>

To set a default minimum kernel for all new and commissioned machines:

``` bash
maas $PROFILE maas set-config name=default_min_hwe_kernel value=$KERNEL
```

For example, to set it to the 16.04 GA kernel:

``` bash
maas $PROFILE maas set-config name=default_min_hwe_kernel value=ga-16.04
```

[note]
The command option `default_min_hwe_kernel` appears to apply to only HWE kernels but this is not the case.
[/note]

<a href="#heading--set-a-minimum-deploy-kernel-for-a-machine"><h2 id="heading--set-a-minimum-deploy-kernel-for-a-machine">Set a minimum deploy kernel for a machine</h2></a>

To set the minimum deploy kernel on a per-machine basis:

``` bash
maas $PROFILE machine update $SYSTEM_ID min_hwe_kernel=$HWE_KERNEL
```

For example, to set it to the HWE 16.04 kernel:

``` bash
maas $PROFILE machine update $SYSTEM_ID min_hwe_kernel=hwe-16.04
```

[note]
The command option `default_min_hwe_kernel` appears to apply to only HWE kernels but this is not the case.
[/note]

<a href="#heading--set-a-specific-kernel-during-machine-deployment"><h2 id="heading--set-a-specific-kernel-during-machine-deployment">Set a specific kernel during machine deployment</h2></a>

To set a specific kernel during the deployment of a machine:

``` bash
maas $PROFILE machine deploy $SYSTEM_ID distro_series=$SERIES hwe_kernel=$KERNEL
```

The operation will fail if the kernel specified by `hwe_kernel` is older than the kernel (possibly) given by `default_min_hwe_kernel`. Similarly, it will not work if the kernel is not available for the given distro series (such as 'hwe-16.10' for 'xenial').

For example, to deploy a Xenial node with the HWE 16.04 edge kernel:

``` bash
maas $PROFILE machine deploy $SYSTEM_ID distro_series=xenial hwe_kernel=hwe-16.04-edge
```

[note]
The command option `hwe_kernel` appears to apply to only HWE kernels but this is not the case.
[/note]
snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli  snap-3-0-cli deb-3-0-cli -->
