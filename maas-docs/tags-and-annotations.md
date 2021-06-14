||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/tags-and-annotations-snap-2-7-cli/2886) ~ [UI](/t/tags-and-annotations-snap-2-7-ui/2887)|[CLI](/t/tags-and-annotations-snap-2-8-cli/2888) ~ [UI](/t/tags-and-annotations-snap-2-8-ui/2889)|[CLI](/t/tags-and-annotations-snap-2-9-cli/2890) ~ [UI](/t/tags-and-annotations-snap-2-9-ui/2891)|[CLI](/t/tags-and-annotations-snap-3-0-cli/4021) ~ [UI](/t/tags-and-annotations-snap-3-0-ui/4022)|
Packages|[CLI](/t/tags-and-annotations-deb-2-7-cli/2892) ~ [UI](/t/tags-and-annotations-deb-2-7-ui/2893)|[CLI](/t/tags-and-annotations-deb-2-8-cli/2894) ~ [UI](/t/tags-and-annotations-deb-2-8-ui/2895)|[CLI](/t/tags-and-annotations-deb-2-9-cli/2896) ~ [UI](/t/tags-and-annotations-deb-2-9-ui/2897)|[CLI](/t/tags-and-annotations-deb-3-0-cli/4023) ~ [UI](/t/tags-and-annotations-deb-3-0-ui/4024)|

Tags are short, descriptive, searchable words that can be applied to various MAAS objects, including:

* machines (physical and virtual)
* VM hosts
* controllers (rack and region)
* storage (virtual and physical; block devices or partitions)
* network interfaces
* devices
* nodes (in the CLI only)

Tags serve to help you identify, group, and find objects easily, especially when you routinely deploy hundreds of machines.

Annotations are descriptive, searchable phrases that apply only to machines.  There are two types of annotations: static (always present in any machine state), and dynamic (only present in allocated or deployed states).  Annotations help you identify, characterise, and inform others about your machines.

This article will show you how to:

<!-- snap-2-7-ui deb-2-7-ui snap-2-8-ui deb-2-8-ui snap-2-9-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui
* [Work with tags](#heading--work-with-tags)
 snap-2-7-ui deb-2-7-ui snap-2-8-ui deb-2-8-ui snap-2-9-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui -->
<!-- snap-2-7-ui deb-2-7-ui snap-2-8-ui deb-2-8-ui snap-2-9-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui
* [Work with annotations](#heading--work-with-annotations)
 snap-2-7-ui deb-2-7-ui snap-2-8-ui deb-2-8-ui snap-2-9-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui -->
<!-- snap-2-7-cli deb-2-7-cli snap-2-8-cli deb-2-8-cli snap-2-9-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli
* [Work with tags](#heading--work-with-tags)
 snap-2-7-cli deb-2-7-cli snap-2-8-cli deb-2-8-cli snap-2-9-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli -->
<!-- snap-2-7-cli deb-2-7-cli snap-2-8-cli deb-2-8-cli snap-2-9-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli
* [Work with annotations](#heading--work-with-annotations)
 snap-2-7-cli deb-2-7-cli snap-2-8-cli deb-2-8-cli snap-2-9-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli -->

All headings have been hyperlinked for easy bookmarking.  Note that not all functions for tags and annotations can be accessed via one interface (UI/CLI), so you will occasionally encounter cross-links.

<!-- snap-2-7-ui deb-2-7-ui snap-2-8-ui deb-2-8-ui snap-2-9-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui

<a href="#heading--work-with-tags"><h2 id="heading--work-with-tags">Work with tags</h2></a>

This section is devoted to procedures for working with tags.  We begin with some general operations that apply to all tag types, such as naming conventions and basic mechanics.  We then walk through the various tag types, providing procedures that will help you create, assign, remove, delete, list, view, and filter tags, covering the nuances of each type.

Specifically, this section will show you how to:

 snap-2-7-ui deb-2-7-ui snap-2-8-ui deb-2-8-ui snap-2-9-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui -->
<!-- deb-2-7-ui
* [Work with tags in general](#heading--work-with-tags-in-general)
* [Work with machine and VM tags](#heading--work-with-machine-and-vm-tags)
* [Work with controller tags](#heading--work-with-controller-tags)
* [Work with block device tags](#heading--work-with-block-device-tags)
* [Work with partition tags](#heading--work-with-partition-tags)
* [Work with network tags](#heading--work-with-network-tags)
* [Work with device tags](#heading--work-with-device-tags)
* [Work with node tags (CLI only)](/t/-/2892#heading--work-with-node-tags)
 deb-2-7-ui -->
<!-- deb-2-8-ui
* [Work with tags in general](#heading--work-with-tags-in-general)
* [Work with machine and VM tags](#heading--work-with-machine-and-vm-tags)
* [Work with controller tags](#heading--work-with-controller-tags)
* [Work with block device tags](#heading--work-with-block-device-tags)
* [Work with partition tags](#heading--work-with-partition-tags)
* [Work with network tags](#heading--work-with-network-tags)
* [Work with device tags](#heading--work-with-device-tags)
* [Work with node tags (CLI only)](/t/-/2894#heading--work-with-node-tags)
 deb-2-8-ui -->
<!-- deb-2-9-ui
* [Work with tags in general](#heading--work-with-tags-in-general)
* [Work with machine and VM tags](#heading--work-with-machine-and-vm-tags)
* [Work with controller tags](#heading--work-with-controller-tags)
* [Work with block device tags](#heading--work-with-block-device-tags)
* [Work with partition tags](#heading--work-with-partition-tags)
* [Work with network tags](#heading--work-with-network-tags)
* [Work with device tags](#heading--work-with-device-tags)
* [Work with node tags (CLI only)](/t/-/2896#heading--work-with-node-tags)
 deb-2-9-ui -->
<!-- deb-3-0-ui
* [Work with tags in general](#heading--work-with-tags-in-general)
* [Work with machine and VM tags](#heading--work-with-machine-and-vm-tags)
* [Work with controller tags](#heading--work-with-controller-tags)
* [Work with block device tags](#heading--work-with-block-device-tags)
* [Work with partition tags](#heading--work-with-partition-tags)
* [Work with network tags](#heading--work-with-network-tags)
* [Work with device tags](#heading--work-with-device-tags)
* [Work with node tags (CLI only)](/t/-/4023#heading--work-with-node-tags)
 deb-3-0-ui -->
<!-- snap-2-7-ui
* [Work with tags in general](#heading--work-with-tags-in-general)
* [Work with machine and VM tags](#heading--work-with-machine-and-vm-tags)
* [Work with controller tags](#heading--work-with-controller-tags)
* [Work with block device tags](#heading--work-with-block-device-tags)
* [Work with partition tags](#heading--work-with-partition-tags)
* [Work with network tags](#heading--work-with-network-tags)
* [Work with device tags](#heading--work-with-device-tags)
* [Work with node tags (CLI only)](/t/-/2886#heading--work-with-node-tags)
 snap-2-7-ui -->
<!-- snap-2-8-ui
* [Work with tags in general](#heading--work-with-tags-in-general)
* [Work with machine and VM tags](#heading--work-with-machine-and-vm-tags)
* [Work with controller tags](#heading--work-with-controller-tags)
* [Work with block device tags](#heading--work-with-block-device-tags)
* [Work with partition tags](#heading--work-with-partition-tags)
* [Work with network tags](#heading--work-with-network-tags)
* [Work with device tags](#heading--work-with-device-tags)
* [Work with node tags (CLI only)](/t/-/2888#heading--work-with-node-tags)
 snap-2-8-ui -->
<!-- snap-2-9-ui
* [Work with tags in general](#heading--work-with-tags-in-general)
* [Work with machine and VM tags](#heading--work-with-machine-and-vm-tags)
* [Work with controller tags](#heading--work-with-controller-tags)
* [Work with block device tags](#heading--work-with-block-device-tags)
* [Work with partition tags](#heading--work-with-partition-tags)
* [Work with network tags](#heading--work-with-network-tags)
* [Work with device tags](#heading--work-with-device-tags)
* [Work with node tags (CLI only)](/t/-/2890#heading--work-with-node-tags)
 snap-2-9-ui -->
<!-- snap-3-0-ui
* [Work with tags in general](#heading--work-with-tags-in-general)
* [Work with machine and VM tags](#heading--work-with-machine-and-vm-tags)
* [Work with controller tags](#heading--work-with-controller-tags)
* [Work with block device tags](#heading--work-with-block-device-tags)
* [Work with partition tags](#heading--work-with-partition-tags)
* [Work with network tags](#heading--work-with-network-tags)
* [Work with device tags](#heading--work-with-device-tags)
* [Work with node tags (CLI only)](/t/-/4021#heading--work-with-node-tags)
 snap-3-0-ui -->
<!-- snap-2-7-ui deb-2-7-ui snap-2-8-ui deb-2-8-ui snap-2-9-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui

Tags for these different objects have similar purposes, but they aren't necessarily administered in the same way -- so we've included detailed sections for each tag type.

<a href="#heading--work-with-tags-in-general"><h3 id="heading--work-with-tags-in-general">Work with tags in general</h3></a>

There are a few general procedures for working with tags, centred around naming conventions and basic mechanics.  These procedures apply to nearly all tag types.  They will be referenced often in the subsections that follow.

As a general rule, you'll want to know how to:

* [Name tags](#heading--name-tags)
* [Create and assign tags](#heading--create-and-assign-tags)
* [Delete and remove tags](#heading--delete-and-remove-tags)

<a href="#heading--name-tags"><h4 id="heading--name-tags">Name tags</h4></a>

When working with tags, there are some universal rules you need to follow:

1. Tag names can include any combination of alphabetic letters (a-zA-Z), numbers (0-9), dashes (-) and underscores (_).
2. Tag names can be a maximum of 256 characters in length.
3. Tag names *cannot* include spaces.

In general, names that do not conform to these rules cannot be created.

<a href="#heading--create-and-assign-tags"><h4 id="heading--create-and-assign-tags">Create and assign tags</h4></a>

In the MAAS UI, creating and assigning tags is a combined operation; that is, you create tags as you assign them, rather than creating them first.  Creating tags in the UI is a little different user experience: there is a self-loading completion menu that collects all tags of a similar type.  This completion menu helps you avoid misspelling tags when entering them more than once; otherwise, you might not be able to group and filter tags properly. It also makes tag entry more efficient.

The process for creating and assigning tags in the UI is generally the same for all tag types:

1. Place the cursor in the "Tags" box, wherever it is located on the screen, and type the name of the new tag:

<a href="https://discourse.maas.io/uploads/default/original/2X/7/7be5f2bebbba9a09f70a7dea092d091ef45228e2.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/7/7be5f2bebbba9a09f70a7dea092d091ef45228e2.png"></a>

2. Hit the return key to add the new tag:

<a href="https://discourse.maas.io/uploads/default/original/2X/3/3d151d772aae0f8688d0a40e71cfb3c97bc6e8fc.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/3/3d151d772aae0f8688d0a40e71cfb3c97bc6e8fc.png"></a>

>The auto complete list will re-appear after you've entered the tag, in case you'd like to enter another tag.

3. When you're done, click on the appropriate completion button to complete the operation.

>The tag you just entered will now be added to the tag auto complete list, in alphabetical order, for re-use with other machines.


<a href="#heading--delete-and-remove-tags"><h4 id="heading--delete-and-remove-tags">Delete and remove tags</h4></a>

With the MAAS UI, you remove tags, rather than explicitly deleting them.  Tags are "deleted" when you have removed them from all machines.   

To remove (unassign) a tag:

1. Find the "Tags" box, wherever it is located on the screen:

<a href="https://discourse.maas.io/uploads/default/original/2X/7/7be5f2bebbba9a09f70a7dea092d091ef45228e2.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/7/7be5f2bebbba9a09f70a7dea092d091ef45228e2.png"></a>

2. Click the "X" next to the tag you wish to remove.

3. When you're done, click on the appropriate completion button to complete the operation.

>Note that the tag you just removed will be deleted from  the tag auto complete list when it is no longer assigned to any  machines.

<a href="#heading--work-with-machine-and-vm-tags"><h3 id="heading--work-with-machine-and-vm-tags">Work with machine and VM tags</h3></a>

This subsection will show you how to:
 snap-2-7-ui deb-2-7-ui snap-2-8-ui deb-2-8-ui snap-2-9-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui -->

<!-- deb-2-7-ui
* [Create machine tags with built-in kernel options (CLI only)](/t/-/2892#heading--create-tags-with-built-in-kernel-options)
* [Create and assign machine tags to machines](#heading--create-and-assign-machine-tags-to-machines)
* [Remove and delete machine tags from machines](#heading--remove-and-delete-machine-tags-from-machines)
* [List machine tags for multiple machines](#heading--list-machine-tags-for-multiple-machines)
* [View machine tags for one machine](#heading--view-machine-tags-for-one-machine)
* [View machine tags for a VM host](#heading--view-machine-tags-for-a-vm-host)
 deb-2-7-ui -->
<!-- deb-2-8-ui
* [Create machine tags with built-in kernel options (CLI only)](/t/-/2894#heading--create-tags-with-built-in-kernel-options)
* [Create and assign machine tags to machines](#heading--create-and-assign-machine-tags-to-machines)
* [Remove and delete machine tags from machines](#heading--remove-and-delete-machine-tags-from-machines)
* [List machine tags for multiple machines](#heading--list-machine-tags-for-multiple-machines)
* [View machine tags for one machine](#heading--view-machine-tags-for-one-machine)
* [View machine tags for a VM host](#heading--view-machine-tags-for-a-vm-host)
 deb-2-8-ui -->
<!-- deb-2-9-ui
* [Create machine tags with built-in kernel options (CLI only)](/t/-/2896#heading--create-tags-with-built-in-kernel-options)
* [Create and assign machine tags to machines](#heading--create-and-assign-machine-tags-to-machines)
* [Remove and delete machine tags from machines](#heading--remove-and-delete-machine-tags-from-machines)
* [List machine tags for multiple machines](#heading--list-machine-tags-for-multiple-machines)
* [View machine tags for one machine](#heading--view-machine-tags-for-one-machine)
* [View machine tags for a VM host](#heading--view-machine-tags-for-a-vm-host)
 deb-2-9-ui -->
<!-- deb-3-0-ui
* [Create machine tags with built-in kernel options (CLI only)](/t/-/4023#heading--create-tags-with-built-in-kernel-options)
* [Create and assign machine tags to machines](#heading--create-and-assign-machine-tags-to-machines)
* [Remove and delete machine tags from machines](#heading--remove-and-delete-machine-tags-from-machines)
* [List machine tags for multiple machines](#heading--list-machine-tags-for-multiple-machines)
* [View machine tags for one machine](#heading--view-machine-tags-for-one-machine)
* [View machine tags for a VM host](#heading--view-machine-tags-for-a-vm-host)
 deb-3-0-ui -->
<!-- snap-2-7-ui
* [Create machine tags with built-in kernel options (CLI only)](/t/-/2886#heading--create-tags-with-built-in-kernel-options)
* [Create and assign machine tags to machines](#heading--create-and-assign-machine-tags-to-machines)
* [Remove and delete machine tags from machines](#heading--remove-and-delete-machine-tags-from-machines)
* [List machine tags for multiple machines](#heading--list-machine-tags-for-multiple-machines)
* [View machine tags for one machine](#heading--view-machine-tags-for-one-machine)
* [View machine tags for a VM host](#heading--view-machine-tags-for-a-vm-host)
 snap-2-7-ui -->
<!-- snap-2-8-ui
* [Create machine tags with built-in kernel options (CLI only)](/t/-/2888#heading--create-tags-with-built-in-kernel-options)
* [Create and assign machine tags to machines](#heading--create-and-assign-machine-tags-to-machines)
* [Remove and delete machine tags from machines](#heading--remove-and-delete-machine-tags-from-machines)
* [List machine tags for multiple machines](#heading--list-machine-tags-for-multiple-machines)
* [View machine tags for one machine](#heading--view-machine-tags-for-one-machine)
* [View machine tags for a VM host](#heading--view-machine-tags-for-a-vm-host)
 snap-2-8-ui -->
<!-- snap-2-9-ui
* [Create machine tags with built-in kernel options (CLI only)](/t/-/2890#heading--create-tags-with-built-in-kernel-options)
* [Create and assign machine tags to machines](#heading--create-and-assign-machine-tags-to-machines)
* [Remove and delete machine tags from machines](#heading--remove-and-delete-machine-tags-from-machines)
* [List machine tags for multiple machines](#heading--list-machine-tags-for-multiple-machines)
* [View machine tags for one machine](#heading--view-machine-tags-for-one-machine)
* [View machine tags for a VM host](#heading--view-machine-tags-for-a-vm-host)
 snap-2-9-ui -->
<!-- snap-3-0-ui
* [Create machine tags with built-in kernel options (CLI only)](/t/-/4021#heading--create-tags-with-built-in-kernel-options)
* [Create and assign machine tags to machines](#heading--create-and-assign-machine-tags-to-machines)
* [Remove and delete machine tags from machines](#heading--remove-and-delete-machine-tags-from-machines)
* [List machine tags for multiple machines](#heading--list-machine-tags-for-multiple-machines)
* [View machine tags for one machine](#heading--view-machine-tags-for-one-machine)
* [View machine tags for a VM host](#heading--view-machine-tags-for-a-vm-host)
 snap-3-0-ui -->
<!-- snap-2-7-ui deb-2-7-ui snap-2-8-ui deb-2-8-ui snap-2-9-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui

<a href="#heading--create-and-assign-machine-tags-to-machines"><h4 id="heading--create-and-assign-machine-tags-to-machines">Create and assign machine tags to machines</h4></a>

If you want to create a new tag, and simultaneously assign it to a machine, use the following steps:

1. Go to the machine list and select the machine you're interested in modifying, by checking the box next to the machine name:

<a href="https://discourse.maas.io/uploads/default/original/2X/8/86ee8529206fcfa297865198a55b976e1002b6bf.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/8/86ee8529206fcfa297865198a55b976e1002b6bf.png"></a>

2. Select the "Take action" drop-down menu and select "Tag":

<a href="https://discourse.maas.io/uploads/default/original/2X/f/f77f19b7aef9f880c12a4d710b91cc3abdc03154.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/f/f77f19b7aef9f880c12a4d710b91cc3abdc03154.png"></a>

3. Create and/or assign the desired tag, as described in the [general tagging procedure](#heading--create-and-assign-tags) above.

4. Don't forget to hit the "Tag machine" button when you're done, to apply your changes to the machine.

<a href="#heading--tag-multiple-machines"><h5 id="heading--tag-multiple-machines">Tagging multiple machines at once</h5></a>

In the first step of the above procedure, you can select more than one machine:

<a href="https://discourse.maas.io/uploads/default/original/2X/0/0c04973e76012c780035a4ea11a588f341148445.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/0/0c04973e76012c780035a4ea11a588f341148445.png"></a>

Any tags you add in the "Tags" box will be applied to all selected machines, as noted by the change in the "Tag machine" button:

<a href="https://discourse.maas.io/uploads/default/original/2X/a/a503261eb7faa17478b09aa70f48f838b4b0fb87.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/a/a503261eb7faa17478b09aa70f48f838b4b0fb87.png"></a>

Other than the scope of the transaction (e.g., tagging three machines, in this case), everything else about this operation conforms to the [general tag assignment procedure](#heading--create-and-assign-tags).

<a href="#heading--remove-and-delete-machine-tags-from-machines"><h4 id="heading--remove-and-delete-machine-tags-from-machines">Remove and delete machine tags from machines</h4></a>

To remove machine tags from a machine:

1. View a machine's currently assigned tags: stay on the 'Machines' page and click on the machine in question. MAAS will display currently-assigned tags in the *Tags* pane of the 'Machine summary'.

2. Select the 'Configuration' tab and then the 'Edit' button alongside 'Machine configuration' to edit tags:

3. Follow the [general tag removal procedure](#heading--delete-and-remove-tags).


<a href="#heading--list-machine-tags-for-multiple-machines"><h4 id="heading--list-machine-tags-for-multiple-machines">List machine tags for multiple machines</h4></a>

In the MAAS UI, you don't explicitly list all machine tags; instead, you filter by them using the "Filter by" drop-down.  This filtered list does not distinguish between virtual machines (VMs) and physical machines, unless you've assigned tags to help with that distinction.
 snap-2-7-ui deb-2-7-ui snap-2-8-ui deb-2-8-ui snap-2-9-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui -->

<!-- deb-2-7-ui
Of course, if you need to do so, you can see a list of all the tags assigned to machines by opening the "tags" section of the filter drop-down.  With the UI, you can't see a list of tags assigned to all virtual machine hosts (VM hosts), or filter VM hosts by tag. It is possible to get a more comprehensive list of machine tags [using the CLI](/t/-/2892#heading--list-machine-tags-for-all-machines), and [retrieve a list of VM host tags](/t/-/2892#heading--list-tags-for-all-vm-hosts).
 deb-2-7-ui -->
<!-- deb-2-8-ui
Of course, if you need to do so, you can see a list of all the tags assigned to machines by opening the "tags" section of the filter drop-down.  With the UI, you can't see a list of tags assigned to all virtual machine hosts (VM hosts), or filter VM hosts by tag. It is possible to get a more comprehensive list of machine tags [using the CLI](/t/-/2894#heading--list-machine-tags-for-all-machines), and [retrieve a list of VM host tags](/t/-/2894#heading--list-tags-for-all-vm-hosts).
 deb-2-8-ui -->
<!-- deb-2-9-ui
Of course, if you need to do so, you can see a list of all the tags assigned to machines by opening the "tags" section of the filter drop-down.  With the UI, you can't see a list of tags assigned to all virtual machine hosts (VM hosts), or filter VM hosts by tag. It is possible to get a more comprehensive list of machine tags [using the CLI](/t/-/2896#heading--list-machine-tags-for-all-machines), and [retrieve a list of VM host tags](/t/-/2896#heading--list-tags-for-all-vm-hosts).
 deb-2-9-ui -->
<!-- deb-3-0-ui
Of course, if you need to do so, you can see a list of all the tags assigned to machines by opening the "tags" section of the filter drop-down.  With the UI, you can't see a list of tags assigned to all virtual machine hosts (VM hosts), or filter VM hosts by tag. It is possible to get a more comprehensive list of machine tags [using the CLI](/t/-/4023#heading--list-machine-tags-for-all-machines), and [retrieve a list of VM host tags](/t/-/4023#heading--list-tags-for-all-vm-hosts).
 deb-3-0-ui -->
<!-- snap-2-7-ui
Of course, if you need to do so, you can see a list of all the tags assigned to machines by opening the "tags" section of the filter drop-down.  With the UI, you can't see a list of tags assigned to all virtual machine hosts (VM hosts), or filter VM hosts by tag. It is possible to get a more comprehensive list of machine tags [using the CLI](/t/-/2886#heading--list-machine-tags-for-all-machines), and [retrieve a list of VM host tags](/t/-/2886#heading--list-tags-for-all-vm-hosts).
 snap-2-7-ui -->
<!-- snap-2-8-ui
Of course, if you need to do so, you can see a list of all the tags assigned to machines by opening the "tags" section of the filter drop-down.  With the UI, you can't see a list of tags assigned to all virtual machine hosts (VM hosts), or filter VM hosts by tag. It is possible to get a more comprehensive list of machine tags [using the CLI](/t/-/2888#heading--list-machine-tags-for-all-machines), and [retrieve a list of VM host tags](/t/-/2888#heading--list-tags-for-all-vm-hosts).
 snap-2-8-ui -->
<!-- snap-2-9-ui
Of course, if you need to do so, you can see a list of all the tags assigned to machines by opening the "tags" section of the filter drop-down.  With the UI, you can't see a list of tags assigned to all virtual machine hosts (VM hosts), or filter VM hosts by tag. It is possible to get a more comprehensive list of machine tags [using the CLI](/t/-/2890#heading--list-machine-tags-for-all-machines), and [retrieve a list of VM host tags](/t/-/2890#heading--list-tags-for-all-vm-hosts).
 snap-2-9-ui -->
<!-- snap-3-0-ui
Of course, if you need to do so, you can see a list of all the tags assigned to machines by opening the "tags" section of the filter drop-down.  With the UI, you can't see a list of tags assigned to all virtual machine hosts (VM hosts), or filter VM hosts by tag. It is possible to get a more comprehensive list of machine tags [using the CLI](/t/-/4021#heading--list-machine-tags-for-all-machines), and [retrieve a list of VM host tags](/t/-/4021#heading--list-tags-for-all-vm-hosts).
 snap-3-0-ui -->
<!-- snap-2-7-ui deb-2-7-ui snap-2-8-ui deb-2-8-ui snap-2-9-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 

Here's how you can filter the machine list by machine tags, using the MAAS UI:

1. To list all tags, visit the 'Machines' tab and expand the 'Tags' subsection in the left pane. In this view, you can use tags as machine search filters.

2. Select one or several tags. The machines that satisfy all selected tags will display on the right pane. Notice there is a search field at the top of the right pane. You can type a search expression into this field.

Below, tag 'virtual' has been selected (with the mouse), and the search field automatically reflects this. Five machines satisfy this search filter.

<a href="https://assets.ubuntu.com/v1/69aa9997-nodes-tags__2.6-tags-filter.png" target = "_blank"><img src="https://assets.ubuntu.com/v1/69aa9997-nodes-tags__2.6-tags-filter.png"></a>

Remove a tag from the search filter by either hitting the 'x' character alongside a tag or editing the search expression.

<a href="#heading--view-machine-tags-for-one-machine"><h4 id="heading--view-machine-tags-for-one-machine">View machine tags for one machine</h4></a>

To view the tags assigned to a specific machine, use the following procedure:

1. On the machine list, select the machine of interest by clicking on its name.

2. On the machine detail screen that comes up, look for the tags on one of the cards presented there: the tags for that machine should be listed there.

<a href="#heading--view-machine-tags-for-a-vm-host"><h4 id="heading--view-machine-tags-for-a-vm-host">View machine tags for a VM host</h4></a>

To view the machine tags assigned to a VM host, here's the procedure you'll follow:

1. Click on the KVM tab at the top of the screen.  This will bring you to a list of active KVMs for your system:

<a href="https://discourse.maas.io/uploads/default/original/2X/5/559f0ed9250524792fda93457bc1876304915599.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/5/559f0ed9250524792fda93457bc1876304915599.png"></a>

2. On the detail screen that comes up, choose the "Settings" tab at the top:

<a href="https://discourse.maas.io/uploads/default/original/2X/8/8c8454d576b4b49dd99c3f6c6bb2735252591010.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/8/8c8454d576b4b49dd99c3f6c6bb2735252591010.png"></a>

3. In the settings tab, you'll see a box labelled "Tags."  You can use this box to view, assign, edit, or remove tags for the KVM:

<a href="https://discourse.maas.io/uploads/default/original/2X/e/e7953d2c5d153b82eac3cb1a3ba105ec194eb077.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/e/e7953d2c5d153b82eac3cb1a3ba105ec194eb077.png"></a>

Note that you can only see the tags for a VM host in the same place that you change it.  For a more comprehensive list of VM host tags, use the [MAAS CLI]({r3}).

<a href="#heading--work-with-controller-tags"><h3 id="heading--work-with-controller-tags">Work with controller tags</h3></a>

This subsection will show you how to:
 
* [Create and assign controller tags ](#heading--create-and-assign-controller-tags-)
* [Remove and delete controller tags](#heading--remove-and-delete-controller-tags)
* [List controller tags](#heading--list-controller-tags)
* [View controller tags](#heading--view-controller-tags)

<a href="#heading--create-and-assign-controller-tags-"><h4 id="heading--create-and-assign-controller-tags-">Create and assign controller tags </h4></a>

To create and assign a controller tag, you can use the following procedure:

1. Click on the "Controllers" tab to open the controllers page:

<a href="https://discourse.maas.io/uploads/default/original/2X/0/00c569161f52ed83349e8ec9e63b65fa8215f89f.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/0/00c569161f52ed83349e8ec9e63b65fa8215f89f.png"></a>

2. Click on the hyperlinked name of the controller to which you want to assign tags.  You will see a screen with several cards, like this one:

<a href="https://discourse.maas.io/uploads/default/original/2X/0/00c569161f52ed83349e8ec9e63b65fa8215f89f.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/0/00c569161f52ed83349e8ec9e63b65fa8215f89f.png"></a>

3. Find the "Tags" card and click on "Edit."  You will be brought to that controller's "Configuration" tab.

4. Click on the "Edit" button for "Controller configuration."
You'll be presented with an editing screen similar to this one:
 
<a href="https://discourse.maas.io/uploads/default/original/2X/3/37401271d0ab3aa130127a251222e5eaf557b20c.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/3/37401271d0ab3aa130127a251222e5eaf557b20c.png"></a>

5.  Follow the [general procedure](#heading--create-and-assign-tags) to assign a tag to the controller.

<a href="#heading--remove-and-delete-controller-tags"><h4 id="heading--remove-and-delete-controller-tags">Remove and delete controller tags</h4></a>

To remove (and possibly delete) a controller tag, you can use the following procedure:

1. Click on the "Controllers" tab to open the controllers page:

<a href="https://discourse.maas.io/uploads/default/original/2X/0/00c569161f52ed83349e8ec9e63b65fa8215f89f.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/0/00c569161f52ed83349e8ec9e63b65fa8215f89f.png"></a>

2. Click on the hyperlinked name of the controller to which you want to assign tags.  You will see a screen with several cards, like this one:

<a href="https://discourse.maas.io/uploads/default/original/2X/0/00c569161f52ed83349e8ec9e63b65fa8215f89f.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/0/00c569161f52ed83349e8ec9e63b65fa8215f89f.png"></a>

3. Find the "Tags" card and click on "Edit."  You will be brought to that controller's "Configuration" tab.

4. Click on the "Edit" button for "Controller configuration."
You'll be presented with an editing screen similar to this one:
 
<a href="https://discourse.maas.io/uploads/default/original/2X/3/37401271d0ab3aa130127a251222e5eaf557b20c.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/3/37401271d0ab3aa130127a251222e5eaf557b20c.png"></a>

5.  Follow the [general procedure](#heading--delete-and-remove-tags) to remove a tag from the controller.

<a href="#heading--list-controller-tags"><h4 id="heading--list-controller-tags">List controller tags</h4></a>
 snap-2-7-ui deb-2-7-ui snap-2-8-ui deb-2-8-ui snap-2-9-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui -->

<!-- deb-2-7-ui
There is no explicit means of listing tags for all controllers in the MAAS UI; see the [relevant procedure](/t/-/2892#heading--list-tags-for-all-region-controllers) in the MAAS CLI to do this.  If you click on a tag assigned to a controller, though,  you will see a filtered list of machines with that matching tag.  
 deb-2-7-ui -->
<!-- deb-2-8-ui
There is no explicit means of listing tags for all controllers in the MAAS UI; see the [relevant procedure](/t/-/2894#heading--list-tags-for-all-region-controllers) in the MAAS CLI to do this.  If you click on a tag assigned to a controller, though,  you will see a filtered list of machines with that matching tag.  
 deb-2-8-ui -->
<!-- deb-2-9-ui
There is no explicit means of listing tags for all controllers in the MAAS UI; see the [relevant procedure](/t/-/2896#heading--list-tags-for-all-region-controllers) in the MAAS CLI to do this.  If you click on a tag assigned to a controller, though,  you will see a filtered list of machines with that matching tag.  
 deb-2-9-ui -->
<!-- deb-3-0-ui
There is no explicit means of listing tags for all controllers in the MAAS UI; see the [relevant procedure](/t/-/4023#heading--list-tags-for-all-region-controllers) in the MAAS CLI to do this.  If you click on a tag assigned to a controller, though,  you will see a filtered list of machines with that matching tag.  
 deb-3-0-ui -->
<!-- snap-2-7-ui
There is no explicit means of listing tags for all controllers in the MAAS UI; see the [relevant procedure](/t/-/2886#heading--list-tags-for-all-region-controllers) in the MAAS CLI to do this.  If you click on a tag assigned to a controller, though,  you will see a filtered list of machines with that matching tag.  
 snap-2-7-ui -->
<!-- snap-2-8-ui
There is no explicit means of listing tags for all controllers in the MAAS UI; see the [relevant procedure](/t/-/2888#heading--list-tags-for-all-region-controllers) in the MAAS CLI to do this.  If you click on a tag assigned to a controller, though,  you will see a filtered list of machines with that matching tag.  
 snap-2-8-ui -->
<!-- snap-2-9-ui
There is no explicit means of listing tags for all controllers in the MAAS UI; see the [relevant procedure](/t/-/2890#heading--list-tags-for-all-region-controllers) in the MAAS CLI to do this.  If you click on a tag assigned to a controller, though,  you will see a filtered list of machines with that matching tag.  
 snap-2-9-ui -->
<!-- snap-3-0-ui
There is no explicit means of listing tags for all controllers in the MAAS UI; see the [relevant procedure](/t/-/4021#heading--list-tags-for-all-region-controllers) in the MAAS CLI to do this.  If you click on a tag assigned to a controller, though,  you will see a filtered list of machines with that matching tag.  
 snap-3-0-ui -->
<!-- snap-2-7-ui deb-2-7-ui snap-2-8-ui deb-2-8-ui snap-2-9-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui

<a href="#heading--view-controller-tags"><h4 id="heading--view-controller-tags">View controller tags</h4></a>

To view a list of tags assigned to a particular controller, you can use the following procedure:

1. Click on the "Controllers" tab to open the controllers page:

<a href="https://discourse.maas.io/uploads/default/original/2X/0/00c569161f52ed83349e8ec9e63b65fa8215f89f.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/0/00c569161f52ed83349e8ec9e63b65fa8215f89f.png"></a>

2. Click on the hyperlinked name of the controller of interest..  You will see a screen with several cards, like this one:

<a href="https://discourse.maas.io/uploads/default/original/2X/0/00c569161f52ed83349e8ec9e63b65fa8215f89f.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/0/00c569161f52ed83349e8ec9e63b65fa8215f89f.png"></a>

3. Find the "Tags" card; this card will list all the tags assigned to this controller.

<a href="#heading--work-with-block-device-tags"><h3 id="heading--work-with-block-device-tags">Work with block device tags</h3></a>

In the parlance of MAAS, a block device is generally an unassigned and unpartitioned physical or virtual disk. This subsection will show you how to:
 

* [Create and assign block device tags](#heading--create-and-assign-block-device-tags)
* [Remove and delete block device tags](#heading--remove-and-delete-block-device-tags)
* [List block device tags](#heading--list-block-device-tags)
* [View block device tags](#heading--view-block-device-tags)

<a href="#heading--create-and-assign-block-device-tags"><h4 id="heading--create-and-assign-block-device-tags">Create and assign block device tags</h4></a>

In order to create and assign tags to a block device, the device has to be in an "available" state, with no active partitions. To create and assign tags to block devices:

1. Go to the machine list:

<a href="https://discourse.maas.io/uploads/default/original/2X/c/c4069963ad134416ba8fe9e436317f48b8fa2f46.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/c/c4069963ad134416ba8fe9e436317f48b8fa2f46.png"></a>

2. Select that machine that has the block-device you want to tag:

<a href="https://discourse.maas.io/uploads/default/original/2X/9/9dc953000f245311b4e3f4751adb1d2973d0fe38.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/9/9dc953000f245311b4e3f4751adb1d2973d0fe38.png"></a>

3. Click on the "Storage" tab and focus on the block labelled "Available disks and partitions:"

<a href="https://discourse.maas.io/uploads/default/original/2X/0/0b78891d0933af01489304c778c6168f2c6776f9.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/0/0b78891d0933af01489304c778c6168f2c6776f9.png"></a>

4. Click the drop-down arrow at the right end of the row containing the block device you want to tag. Choose the "Edit..." option (the wording may vary, e.g, "Edit physical..."). This will take you to an editing screen for that block device:

<a href="https://discourse.maas.io/uploads/default/original/2X/2/2912877532c3ea0b744ff3c88c7ef2046598bebc.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/2/2912877532c3ea0b744ff3c88c7ef2046598bebc.png"></a>

5. Add tags as described in the [general procedure](#heading--create-and-assign-tags).

6. Be sure to click on the "Save" button when you're done.

<a href="#heading--remove-and-delete-block-device-tags"><h4 id="heading--remove-and-delete-block-device-tags">Remove and delete block device tags</h4></a>

In order to remove tags from a block device, the device has to be in an "available" state, with no active partitions. To remove and delete tags from a block devices:

1. Go to the machine list:

<a href="https://discourse.maas.io/uploads/default/original/2X/c/c4069963ad134416ba8fe9e436317f48b8fa2f46.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/c/c4069963ad134416ba8fe9e436317f48b8fa2f46.png"></a>

2. Select that machine that has the block-device with the tag you want to remove:

<a href="https://discourse.maas.io/uploads/default/original/2X/9/9dc953000f245311b4e3f4751adb1d2973d0fe38.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/9/9dc953000f245311b4e3f4751adb1d2973d0fe38.png"></a>

3. Click on the "Storage" tab and focus on the block labelled "Available disks and partitions:"

<a href="https://discourse.maas.io/uploads/default/original/2X/0/0b78891d0933af01489304c778c6168f2c6776f9.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/0/0b78891d0933af01489304c778c6168f2c6776f9.png"></a>

4. Click the drop-down arrow at the right end of the row containing the block device you want to tag. Choose the "Edit..." option (the wording may vary, e.g, "Edit physical..."). This will take you to an editing screen for that block device:

<a href="https://discourse.maas.io/uploads/default/original/2X/2/2912877532c3ea0b744ff3c88c7ef2046598bebc.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/2/2912877532c3ea0b744ff3c88c7ef2046598bebc.png"></a>

5. Delete tags by clicking the "X" next to them, as described in the [general procedure](#heading--create-and-assign-tags).

6. Be sure to click on the "Save" button when you're done.

<a href="#heading--list-block-device-tags"><h4 id="heading--list-block-device-tags">List block device tags</h4></a>

<!-- deb-2-7-ui
There is no explicit way to list all block device tags in the UI; see the [MAAS CLI](/t/-/2892#heading--list-tags-for-all-block-devices) for a more comprehensive procedure. You can list all storage links, though -- block device and partition -- by using the filter tool on the machine list.  Here's how:
 deb-2-7-ui -->
<!-- deb-2-8-ui
There is no explicit way to list all block device tags in the UI; see the [MAAS CLI](/t/-/2894#heading--list-tags-for-all-block-devices) for a more comprehensive procedure. You can list all storage links, though -- block device and partition -- by using the filter tool on the machine list.  Here's how:
 deb-2-8-ui -->
<!-- deb-2-9-ui
There is no explicit way to list all block device tags in the UI; see the [MAAS CLI](/t/-/2896#heading--list-tags-for-all-block-devices) for a more comprehensive procedure. You can list all storage links, though -- block device and partition -- by using the filter tool on the machine list.  Here's how:
 deb-2-9-ui -->
<!-- deb-3-0-ui
There is no explicit way to list all block device tags in the UI; see the [MAAS CLI](/t/-/4023#heading--list-tags-for-all-block-devices) for a more comprehensive procedure. You can list all storage links, though -- block device and partition -- by using the filter tool on the machine list.  Here's how:
 deb-3-0-ui -->
<!-- snap-2-7-ui
There is no explicit way to list all block device tags in the UI; see the [MAAS CLI](/t/-/2886#heading--list-tags-for-all-block-devices) for a more comprehensive procedure. You can list all storage links, though -- block device and partition -- by using the filter tool on the machine list.  Here's how:
 snap-2-7-ui -->
<!-- snap-2-8-ui
There is no explicit way to list all block device tags in the UI; see the [MAAS CLI](/t/-/2888#heading--list-tags-for-all-block-devices) for a more comprehensive procedure. You can list all storage links, though -- block device and partition -- by using the filter tool on the machine list.  Here's how:
 snap-2-8-ui -->
<!-- snap-2-9-ui
There is no explicit way to list all block device tags in the UI; see the [MAAS CLI](/t/-/2890#heading--list-tags-for-all-block-devices) for a more comprehensive procedure. You can list all storage links, though -- block device and partition -- by using the filter tool on the machine list.  Here's how:
 snap-2-9-ui -->
<!-- snap-3-0-ui
There is no explicit way to list all block device tags in the UI; see the [MAAS CLI](/t/-/4021#heading--list-tags-for-all-block-devices) for a more comprehensive procedure. You can list all storage links, though -- block device and partition -- by using the filter tool on the machine list.  Here's how:
 snap-3-0-ui -->
<!-- snap-2-7-ui deb-2-7-ui snap-2-8-ui deb-2-8-ui snap-2-9-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui

1. Go to the machine list:

<a href="https://discourse.maas.io/uploads/default/original/2X/c/c4069963ad134416ba8fe9e436317f48b8fa2f46.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/c/c4069963ad134416ba8fe9e436317f48b8fa2f46.png"></a>

2. Select the "Filters" drop-down and open the section titled "Storage tags:"

<a href="https://discourse.maas.io/uploads/default/original/2X/c/c03216c0c2b6097f73b8161922b602aac4fdc3d6.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/c/c03216c0c2b6097f73b8161922b602aac4fdc3d6.png"></a>

Here you will see a list of all block device and partition tags currently assigned to machines in this MAAS.  If you wish to filter the machine list by a given tag, just make sure that it's checked (and other storage tags unchecked) in the filter list.

<a href="#heading--view-block-device-tags"><h4 id="heading--view-block-device-tags">View block device tags</h4></a>

To view all tags associated with block devices on a given machine:

1. Go to the machine list:

<a href="https://discourse.maas.io/uploads/default/original/2X/c/c4069963ad134416ba8fe9e436317f48b8fa2f46.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/c/c4069963ad134416ba8fe9e436317f48b8fa2f46.png"></a>

2. Select that machine that has the block device that interests you:

<a href="https://discourse.maas.io/uploads/default/original/2X/9/9dc953000f245311b4e3f4751adb1d2973d0fe38.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/9/9dc953000f245311b4e3f4751adb1d2973d0fe38.png"></a>

3. Click on the "Storage" tab and check the page for tags:

<a href="https://discourse.maas.io/uploads/default/original/2X/f/feb789078b8f5f2f6f23acc056f8c037381d2cfc.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/f/feb789078b8f5f2f6f23acc056f8c037381d2cfc.png"></a>

<a href="#heading--work-with-partition-tags"><h3 id="heading--work-with-partition-tags">Work with partition tags</h3></a>

This subsection will show you how to:

<!-- deb-2-7-ui
* [Assign partition tags (CLI only)](/t/-/2892#heading--assign-tags-to-a-partition)
* [Remove partition tags (CLI only)](/t/-/2892#heading--remove-tags-from-a-partition)
* [List partition tags](#heading--list-partition-tags)
* [View partition tags](#heading--view-partition-tags)
 deb-2-7-ui -->
<!-- deb-2-8-ui
* [Assign partition tags (CLI only)](/t/-/2894#heading--assign-tags-to-a-partition)
* [Remove partition tags (CLI only)](/t/-/2894#heading--remove-tags-from-a-partition)
* [List partition tags](#heading--list-partition-tags)
* [View partition tags](#heading--view-partition-tags)
 deb-2-8-ui -->
<!-- deb-2-9-ui
* [Assign partition tags (CLI only)](/t/-/2896#heading--assign-tags-to-a-partition)
* [Remove partition tags (CLI only)](/t/-/2896#heading--remove-tags-from-a-partition)
* [List partition tags](#heading--list-partition-tags)
* [View partition tags](#heading--view-partition-tags)
 deb-2-9-ui -->
<!-- deb-3-0-ui
* [Assign partition tags (CLI only)](/t/-/4023#heading--assign-tags-to-a-partition)
* [Remove partition tags (CLI only)](/t/-/4023#heading--remove-tags-from-a-partition)
* [List partition tags](#heading--list-partition-tags)
* [View partition tags](#heading--view-partition-tags)
 deb-3-0-ui -->
<!-- snap-2-7-ui
* [Assign partition tags (CLI only)](/t/-/2886#heading--assign-tags-to-a-partition)
* [Remove partition tags (CLI only)](/t/-/2886#heading--remove-tags-from-a-partition)
* [List partition tags](#heading--list-partition-tags)
* [View partition tags](#heading--view-partition-tags)
 snap-2-7-ui -->
<!-- snap-2-8-ui
* [Assign partition tags (CLI only)](/t/-/2888#heading--assign-tags-to-a-partition)
* [Remove partition tags (CLI only)](/t/-/2888#heading--remove-tags-from-a-partition)
* [List partition tags](#heading--list-partition-tags)
* [View partition tags](#heading--view-partition-tags)
 snap-2-8-ui -->
<!-- snap-2-9-ui
* [Assign partition tags (CLI only)](/t/-/2890#heading--assign-tags-to-a-partition)
* [Remove partition tags (CLI only)](/t/-/2890#heading--remove-tags-from-a-partition)
* [List partition tags](#heading--list-partition-tags)
* [View partition tags](#heading--view-partition-tags)
 snap-2-9-ui -->
<!-- snap-3-0-ui
* [Assign partition tags (CLI only)](/t/-/4021#heading--assign-tags-to-a-partition)
* [Remove partition tags (CLI only)](/t/-/4021#heading--remove-tags-from-a-partition)
* [List partition tags](#heading--list-partition-tags)
* [View partition tags](#heading--view-partition-tags)
 snap-3-0-ui -->
<!-- snap-2-7-ui deb-2-7-ui snap-2-8-ui deb-2-8-ui snap-2-9-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui

<a href="#heading--list-partition-tags"><h4 id="heading--list-partition-tags">List partition tags</h4></a>

 snap-2-7-ui deb-2-7-ui snap-2-8-ui deb-2-8-ui snap-2-9-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui -->
<!-- deb-2-7-ui
There is no explicit way to list all partition tags in the UI; see the [MAAS CLI](/t/-/2892#heading--list-tags-for-all-partitions) for a more comprehensive procedure.
 deb-2-7-ui -->
<!-- deb-2-8-ui
There is no explicit way to list all partition tags in the UI; see the [MAAS CLI](/t/-/2894#heading--list-tags-for-all-partitions) for a more comprehensive procedure.
 deb-2-8-ui -->
<!-- deb-2-9-ui
There is no explicit way to list all partition tags in the UI; see the [MAAS CLI](/t/-/2896#heading--list-tags-for-all-partitions) for a more comprehensive procedure.
 deb-2-9-ui -->
<!-- deb-3-0-ui
There is no explicit way to list all partition tags in the UI; see the [MAAS CLI](/t/-/4023#heading--list-tags-for-all-partitions) for a more comprehensive procedure.
 deb-3-0-ui -->
<!-- snap-2-7-ui
There is no explicit way to list all partition tags in the UI; see the [MAAS CLI](/t/-/2886#heading--list-tags-for-all-partitions) for a more comprehensive procedure.
 snap-2-7-ui -->
<!-- snap-2-8-ui
There is no explicit way to list all partition tags in the UI; see the [MAAS CLI](/t/-/2888#heading--list-tags-for-all-partitions) for a more comprehensive procedure.
 snap-2-8-ui -->
<!-- snap-2-9-ui
There is no explicit way to list all partition tags in the UI; see the [MAAS CLI](/t/-/2890#heading--list-tags-for-all-partitions) for a more comprehensive procedure.
 snap-2-9-ui -->
<!-- snap-3-0-ui
There is no explicit way to list all partition tags in the UI; see the [MAAS CLI](/t/-/4021#heading--list-tags-for-all-partitions) for a more comprehensive procedure.
 snap-3-0-ui -->
<!-- snap-2-7-ui deb-2-7-ui snap-2-8-ui deb-2-8-ui snap-2-9-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui

You can list all storage links (block device and partition) by using the filter tool on the machine list.  Here's how:

1. Go to the machine list:

<a href="https://discourse.maas.io/uploads/default/original/2X/c/c4069963ad134416ba8fe9e436317f48b8fa2f46.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/c/c4069963ad134416ba8fe9e436317f48b8fa2f46.png"></a>

2. Select the "Filters" drop-down and open the section titled "Storage tags:"

<a href="https://discourse.maas.io/uploads/default/original/2X/c/c03216c0c2b6097f73b8161922b602aac4fdc3d6.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/c/c03216c0c2b6097f73b8161922b602aac4fdc3d6.png"></a>

Here you will see a list of all block device and partition tags currently assigned to machines in this MAAS.

<a href="#heading--view-partition-tags"><h4 id="heading--view-partition-tags">View partition tags</h4></a>

To view all tags associated with partitions on a given machine:

1. Go to the machine list:

<a href="https://discourse.maas.io/uploads/default/original/2X/c/c4069963ad134416ba8fe9e436317f48b8fa2f46.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/c/c4069963ad134416ba8fe9e436317f48b8fa2f46.png"></a>

2. Select that machine that has the block device that interests you:

<a href="https://discourse.maas.io/uploads/default/original/2X/9/9dc953000f245311b4e3f4751adb1d2973d0fe38.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/9/9dc953000f245311b4e3f4751adb1d2973d0fe38.png"></a>

3. Click on the "Storage" tab and check the page for tags:

<a href="https://discourse.maas.io/uploads/default/original/2X/f/feb789078b8f5f2f6f23acc056f8c037381d2cfc.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/f/feb789078b8f5f2f6f23acc056f8c037381d2cfc.png"></a>

<a href="#heading--work-with-network-tags"><h3 id="heading--work-with-network-tags">Work with network tags</h3></a>

This subsection will show you how to:
 snap-2-7-ui deb-2-7-ui snap-2-8-ui deb-2-8-ui snap-2-9-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui -->

<!-- deb-2-7-ui
* [Create and assign network interface tags](#heading--create-and-assign-network-interface-tags)
* [Remove and delete network interface tags](#heading--remove-and-delete-network-interface-tags)
* [List network interface tags (CLI only)](/t/-/2892#heading--list-tags-for-all-network-interfaces)
* [View network interface tags](#heading--view-network-interface-tags)
 deb-2-7-ui -->
<!-- deb-2-8-ui
* [Create and assign network interface tags](#heading--create-and-assign-network-interface-tags)
* [Remove and delete network interface tags](#heading--remove-and-delete-network-interface-tags)
* [List network interface tags (CLI only)](/t/-/2894#heading--list-tags-for-all-network-interfaces)
* [View network interface tags](#heading--view-network-interface-tags)
 deb-2-8-ui -->
<!-- deb-2-9-ui
* [Create and assign network interface tags](#heading--create-and-assign-network-interface-tags)
* [Remove and delete network interface tags](#heading--remove-and-delete-network-interface-tags)
* [List network interface tags (CLI only)](/t/-/2896#heading--list-tags-for-all-network-interfaces)
* [View network interface tags](#heading--view-network-interface-tags)
 deb-2-9-ui -->
<!-- deb-3-0-ui
* [Create and assign network interface tags](#heading--create-and-assign-network-interface-tags)
* [Remove and delete network interface tags](#heading--remove-and-delete-network-interface-tags)
* [List network interface tags (CLI only)](/t/-/4023#heading--list-tags-for-all-network-interfaces)
* [View network interface tags](#heading--view-network-interface-tags)
 deb-3-0-ui -->
<!-- snap-2-7-ui
* [Create and assign network interface tags](#heading--create-and-assign-network-interface-tags)
* [Remove and delete network interface tags](#heading--remove-and-delete-network-interface-tags)
* [List network interface tags (CLI only)](/t/-/2886#heading--list-tags-for-all-network-interfaces)
* [View network interface tags](#heading--view-network-interface-tags)
 snap-2-7-ui -->
<!-- snap-2-8-ui
* [Create and assign network interface tags](#heading--create-and-assign-network-interface-tags)
* [Remove and delete network interface tags](#heading--remove-and-delete-network-interface-tags)
* [List network interface tags (CLI only)](/t/-/2888#heading--list-tags-for-all-network-interfaces)
* [View network interface tags](#heading--view-network-interface-tags)
 snap-2-8-ui -->
<!-- snap-2-9-ui
* [Create and assign network interface tags](#heading--create-and-assign-network-interface-tags)
* [Remove and delete network interface tags](#heading--remove-and-delete-network-interface-tags)
* [List network interface tags (CLI only)](/t/-/2890#heading--list-tags-for-all-network-interfaces)
* [View network interface tags](#heading--view-network-interface-tags)
 snap-2-9-ui -->
<!-- snap-3-0-ui
* [Create and assign network interface tags](#heading--create-and-assign-network-interface-tags)
* [Remove and delete network interface tags](#heading--remove-and-delete-network-interface-tags)
* [List network interface tags (CLI only)](/t/-/4021#heading--list-tags-for-all-network-interfaces)
* [View network interface tags](#heading--view-network-interface-tags)
 snap-3-0-ui -->
<!-- snap-2-7-ui deb-2-7-ui snap-2-8-ui deb-2-8-ui snap-2-9-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui

<a href="#heading--create-and-assign-network-interface-tags"><h4 id="heading--create-and-assign-network-interface-tags">Create and assign network interface tags</h4></a>

To assign a tag to a network interface, use the following procedure:

1. Go to the machine list and select the machine where that interface resides, by clicking on that machine's name:

<a href="https://discourse.maas.io/uploads/default/original/2X/1/1030782316875c112b9e56586a79478a566fe33a.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/1/1030782316875c112b9e56586a79478a566fe33a.png"></a>

2. Click on the "Network" tab:

<a href="https://discourse.maas.io/uploads/default/original/2X/9/9aebbe5708683d937c682e64e22c72d537629cf8.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/9/9aebbe5708683d937c682e64e22c72d537629cf8.png"></a>

3. Choose the interface you'd like to tag, by selecting the checkbox next to its name:

<a href="https://discourse.maas.io/uploads/default/original/2X/f/fb2fb338372ac16229dd9acf00aae545660865f2.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/f/fb2fb338372ac16229dd9acf00aae545660865f2.png"></a>

>The checkbox isn't strictly needed to apply the tag, but it helps prevent you from choosing the wrong one when multiple interfaces are available.

4. Select the drop-down under "ACTIONS" at the end of the row, and select "Edit Physical" to edit the parameters of the physical interface:

<a href="https://discourse.maas.io/uploads/default/original/2X/8/8694d71a49ae8171ac2088005af8b71101894abb.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/8/8694d71a49ae8171ac2088005af8b71101894abb.png"></a>

5. Edit the "Tags" field as desired, as described in the [general tagging procedure](#heading--create-and-assign-tags) above.

6. Be sure to select the "Tag machine" button to apply your changes to the interface for that machine.

Note that different machines may have the same physical interface name, but different MAC addresses, so it's not typical that interface tags carry over from one machine to the next -- so auto complete menus will be sparse or non-existent most of the time for these tag types.

<a href="#heading--remove-and-delete-network-interface-tags"><h4 id="heading--remove-and-delete-network-interface-tags">Remove and delete network interface tags</h4></a>

To remove a tag from a network interface, use the following procedure:

1. Go to the machine list and select the machine where that interface resides, by clicking on that machine's name:

<a href="https://discourse.maas.io/uploads/default/original/2X/1/1030782316875c112b9e56586a79478a566fe33a.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/1/1030782316875c112b9e56586a79478a566fe33a.png"></a>

2. Click on the "Network" tab:

<a href="https://discourse.maas.io/uploads/default/original/2X/9/9aebbe5708683d937c682e64e22c72d537629cf8.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/9/9aebbe5708683d937c682e64e22c72d537629cf8.png"></a>

3. Choose the interface you'd like to un-tag, by selecting the checkbox next to its name:

<a href="https://discourse.maas.io/uploads/default/original/2X/f/fb2fb338372ac16229dd9acf00aae545660865f2.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/f/fb2fb338372ac16229dd9acf00aae545660865f2.png"></a>

>The checkbox isn't strictly needed to apply the tag, but it helps prevent you from choosing the wrong one when multiple interfaces are available.

4. Select the drop-down under "ACTIONS" at the end of the row, and select "Edit Physical" to edit the parameters of the physical interface:

<a href="https://discourse.maas.io/uploads/default/original/2X/8/8694d71a49ae8171ac2088005af8b71101894abb.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/8/8694d71a49ae8171ac2088005af8b71101894abb.png"></a>

5. Edit the "Tags" field as desired, as described in the [general tagging procedure](#heading--create-and-assign-tags) above.

6. Be sure to select the "Tag machine" button to apply your changes to the interface for that machine.

Note that different machines may have the same physical interface name, but different MAC addresses, so it's not typical that interface tags carry over from one machine to the next -- so auto complete menus will be sparse or non-existent most of the time for these tag types.

<a href="#heading--view-network-interface-tags"><h4 id="heading--view-network-interface-tags">View network interface tags</h4></a>

To view the tags associated with a network interface, use the following procedure:

1. Go to the machine list and select the machine where that interface resides, by clicking on that machine's name:

<a href="https://discourse.maas.io/uploads/default/original/2X/1/1030782316875c112b9e56586a79478a566fe33a.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/1/1030782316875c112b9e56586a79478a566fe33a.png"></a>

2. Click on the "Network" tab:

<a href="https://discourse.maas.io/uploads/default/original/2X/9/9aebbe5708683d937c682e64e22c72d537629cf8.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/9/9aebbe5708683d937c682e64e22c72d537629cf8.png"></a>

3. Choose the interface you'd like to see, by selecting the checkbox next to its name:

<a href="https://discourse.maas.io/uploads/default/original/2X/f/fb2fb338372ac16229dd9acf00aae545660865f2.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/f/fb2fb338372ac16229dd9acf00aae545660865f2.png"></a>

>The checkbox isn't strictly needed to apply the tag, but it helps prevent you from choosing the wrong one when multiple interfaces are available.

4. Select the drop-down under "ACTIONS" at the end of the row, and select "Edit Physical" to edit the parameters of the physical interface:

<a href="https://discourse.maas.io/uploads/default/original/2X/8/8694d71a49ae8171ac2088005af8b71101894abb.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/8/8694d71a49ae8171ac2088005af8b71101894abb.png"></a>

5. Be sure to cancel the operation when you're done.

Note that different machines may have the same physical interface name, but different MAC addresses, so it's not typical that interface tags carry over from one machine to the next.

<a href="#heading--work-with-device-tags"><h3 id="heading--work-with-device-tags">Work with device tags</h3></a>

This subsection will show you how to:
 
* [Create and assign device tags](#heading--create-and-assign-device-tags)
* [Remove and delete device tags](#heading--remove-and-delete-device-tags)
* [List device tags](#heading--list-device-tags)
* [View device tags](#heading--view-device-tags)

<a href="#heading--create-and-assign-device-tags"><h4 id="heading--create-and-assign-device-tags">Create and assign device tags</h4></a>

To add a tag to a device, follow this procedure:

1. Select the "Devices" tab; it may be in a drop-down labelled "Hardware," if your browser window is not very large:

<a href="https://discourse.maas.io/uploads/default/original/2X/2/22b17d4827f82c103e958205011ca13934fe2f3f.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/2/22b17d4827f82c103e958205011ca13934fe2f3f.png"></a>

2. Select the device you'd like to tag, by clicking on its name:

<a href="https://discourse.maas.io/uploads/default/original/2X/9/94717b99a4cea205099e3fdfd492daefe683e68d.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/9/94717b99a4cea205099e3fdfd492daefe683e68d.png"></a>

3. In the "Tags" card, select the "Edit" link, or choose the "Configuration" tab under the device name:

<a href="https://discourse.maas.io/uploads/default/original/2X/9/901e7bd556f26560e44b4b74c41b506399e86375.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/9/901e7bd556f26560e44b4b74c41b506399e86375.png"></a>

4. Select the "Edit" button on the "Configuration" tab which comes up:

<a href="https://discourse.maas.io/uploads/default/original/2X/d/d80039410bfeba4b6feb35490ccf82b3be80904f.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/d/d80039410bfeba4b6feb35490ccf82b3be80904f.png"></a>

5. Edit the "Tags" field, as explained in the [general tagging procedure](#heading--create-assign-tag-general) above.

6. Be sure to hit the "Save changes" button to apply your changes to the device.

<a href="#heading--remove-and-delete-device-tags"><h4 id="heading--remove-and-delete-device-tags">Remove and delete device tags</h4></a>

To remove a tag from a device, follow this procedure:

1. Select the "Devices" tab; it may be in a drop-down labelled "Hardware," if your browser window is not very large:

<a href="https://discourse.maas.io/uploads/default/original/2X/2/22b17d4827f82c103e958205011ca13934fe2f3f.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/2/22b17d4827f82c103e958205011ca13934fe2f3f.png"></a>

2. Select the device you'd like to un-tag, by clicking on its name:

<a href="https://discourse.maas.io/uploads/default/original/2X/9/94717b99a4cea205099e3fdfd492daefe683e68d.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/9/94717b99a4cea205099e3fdfd492daefe683e68d.png"></a>

3. In the "Tags" card, select the "Edit" link, or choose the "Configuration" tab under the device name:

<a href="https://discourse.maas.io/uploads/default/original/2X/9/901e7bd556f26560e44b4b74c41b506399e86375.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/9/901e7bd556f26560e44b4b74c41b506399e86375.png"></a>

4. Select the "Edit" button on the "Configuration" tab which comes up:

<a href="https://discourse.maas.io/uploads/default/original/2X/d/d80039410bfeba4b6feb35490ccf82b3be80904f.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/d/d80039410bfeba4b6feb35490ccf82b3be80904f.png"></a>

5. Edit the "Tags" field, as explained in the [general tagging procedure](#heading--create-assign-tag-general) above.

6. Be sure to hit the "Save changes" button to apply your changes to the device.

<a href="#heading--list-device-tags"><h4 id="heading--list-device-tags">List device tags</h4></a>

1. Go to the device list:

<a href="https://discourse.maas.io/uploads/default/original/2X/8/8748ed53d5a24425e808698c902a22536a08f994.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/8/8748ed53d5a24425e808698c902a22536a08f994.png"></a>

2. Select the "Filters" drop-down and open the section titled "Tags:"

<a href="https://discourse.maas.io/uploads/default/original/2X/9/957ff8874fb8336335ec5073c14068f36a7aeeb6.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/9/957ff8874fb8336335ec5073c14068f36a7aeeb6.png"></a>

Here you will see a list of all device tags currently assigned to devices in this MAAS.

<a href="#heading--view-device-tags"><h4 id="heading--view-device-tags">View device tags</h4></a>

1. Go to the device list:

<a href="https://discourse.maas.io/uploads/default/original/2X/8/8748ed53d5a24425e808698c902a22536a08f994.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/8/8748ed53d5a24425e808698c902a22536a08f994.png"></a>

2. Select the device that has your interest by clicking on its name.  A device summary will appear:

<a href="https://discourse.maas.io/uploads/default/original/2X/e/eadc32f46c714080005faa0be7f744d4143df379.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/e/eadc32f46c714080005faa0be7f744d4143df379.png"></a>

The "Tags" card on that screen with show you all the tags currently associated with this device.

<a href="#heading--work-with-annotations"><h2 id="heading--work-with-annotations">Work with annotations</h2></a>

This section will explain how to:
 snap-2-7-ui deb-2-7-ui snap-2-8-ui deb-2-8-ui snap-2-9-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui -->
<!-- snap-3-0-ui deb-3-0-ui 

* [Work with static annotations](#heading--work-with-static-annotations)
* [Work with dynamic (workload) annotations](#heading--work-with-dynamic-workload-annotations)

<a href="#heading--work-with-static-annotations"><h3 id="heading--work-with-static-annotations">Work with static annotations</h3></a>

This subsection will show you how to:
 snap-3-0-ui deb-3-0-ui -->
<!-- snap-2-7-ui deb-2-7-ui snap-2-8-ui deb-2-8-ui snap-2-9-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui
 
* [Create and assign static annotations](#heading--create-and-assign-static-annotations)
* [Delete static annotations](#heading--delete-static-annotations)
* [View static annotations](#heading--view-static-annotations)

<a href="#heading--create-and-assign-static-annotations"><h4 id="heading--create-and-assign-static-annotations">Create and assign static annotations</h4></a>

To create and assign static annotations (a note) to a machine, follow this procedure:

1. Go to the machine list and click on the machine of interest:

<a href="https://discourse.maas.io/uploads/default/original/2X/c/c4069963ad134416ba8fe9e436317f48b8fa2f46.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/c/c4069963ad134416ba8fe9e436317f48b8fa2f46.png"></a>

2. This will bring up a machine summary for that machine:

<a href="https://discourse.maas.io/uploads/default/original/2X/a/a083bd0b3253839df3a57fc21e26439ce2e114dd.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/a/a083bd0b3253839df3a57fc21e26439ce2e114dd.png"></a>

3. Select "Configuration" and click the "Edit" button to the right of the "Machine configuration" section:

<a href="https://discourse.maas.io/uploads/default/original/2X/e/e9fda18183c567e62dea80fce01497227727e7bb.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/e/e9fda18183c567e62dea80fce01497227727e7bb.png"></a>

4. Add free-form notes in the "Note" field, as desired.

5. Click "Save changes" to update the machine's configuration.

<a href="#heading--delete-static-annotations"><h4 id="heading--delete-static-annotations">Delete static annotations</h4></a>

To delete static annotations (a note) from a machine, follow this procedure:

1. Go to the machine list and click on the machine of interest:

<a href="https://discourse.maas.io/uploads/default/original/2X/c/c4069963ad134416ba8fe9e436317f48b8fa2f46.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/c/c4069963ad134416ba8fe9e436317f48b8fa2f46.png"></a>

2. This will bring up a machine summary for that machine:

<a href="https://discourse.maas.io/uploads/default/original/2X/a/a083bd0b3253839df3a57fc21e26439ce2e114dd.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/a/a083bd0b3253839df3a57fc21e26439ce2e114dd.png"></a>

3. Select "Configuration" and click the "Edit" button to the right of the "Machine configuration" section:

<a href="https://discourse.maas.io/uploads/default/original/2X/e/e9fda18183c567e62dea80fce01497227727e7bb.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/e/e9fda18183c567e62dea80fce01497227727e7bb.png"></a>

4. Edit the free-form notes in the "Note" field, as desired.

5. Click "Save changes" to update the machine's configuration.

<a href="#heading--view-static-annotations"><h4 id="heading--view-static-annotations">View static annotations</h4></a>

To view static annotations, you can follow this procedure:

1. Go to the machine list and look at the machine of interest; you should see the first few characters of a note in the bottom half of the column marked "POOL/NOTE:"

<a href="https://discourse.maas.io/uploads/default/original/2X/3/3286feef733f4b56a94708d3af044c1523e78369.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/3/3286feef733f4b56a94708d3af044c1523e78369.png"></a>

2. Click on the machine, which will bring up a machine summary for that machine. Switch to the configuration tab to see the full note:

<a href="https://discourse.maas.io/uploads/default/original/2X/e/e9a324a428a3374b616b2986ee5f56d13eb1e07d.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/e/e9a324a428a3374b616b2986ee5f56d13eb1e07d.png"></a>

 snap-2-7-ui deb-2-7-ui snap-2-8-ui deb-2-8-ui snap-2-9-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui -->

<!-- snap-3-0-ui deb-3-0-ui
<a href="#heading--work-with-dynamic-workload-annotations"><h3 id="heading--work-with-dynamic-workload-annotations">Work with dynamic (workload) annotations</h3></a>
 
This subsection will show you how to:

 snap-3-0-ui deb-3-0-ui -->
<!-- deb-3-0-ui 
* [Create dynamic (workload) annotations (CLI only)](/t/-/4023#heading--set-dynamic-annotations-for-a-machine)
* [Delete dynamic (workload) annotations (CLI only)](/t/-/4023#heading--clear-and-change-dynamic-annotations-for-a-machine)
* [View dynamic (workload) annotations for one machine](#heading--view-dynamic-workload-annotations-for-one-machine)
* [Filter on dynamic (workload) annotations](#heading--filter-on-dynamic-workload-annotations)
 deb-3-0-ui -->
<!-- snap-3-0-ui 
* [Create dynamic (workload) annotations (CLI only)](/t/-/4021#heading--set-dynamic-annotations-for-a-machine)
* [Delete dynamic (workload) annotations (CLI only)](/t/-/4021#heading--clear-and-change-dynamic-annotations-for-a-machine)
* [View dynamic (workload) annotations for one machine](#heading--view-dynamic-workload-annotations-for-one-machine)
* [Filter on dynamic (workload) annotations](#heading--filter-on-dynamic-workload-annotations)
 snap-3-0-ui -->

<!-- snap-3-0-ui deb-3-0-ui
<a href="#heading--view-dynamic-workload-annotations-for-one-machine"><h4 id="heading--view-dynamic-workload-annotations-for-one-machine">View dynamic (workload) annotations for one machine</h4></a>

To view the dynamic (workload) annotations for one machine, do the following:

1. Go to the machine list and select the machine of interest by clicking on its hyperlinked name.

2. In the machine summary that comes up, look for the "Workload Annotations" card, in the lower, right-hand corner:

<a href="https://discourse.maas.io/uploads/default/original/2X/e/e7def7a50f9c854f7aae0efc34897338c46c32c0.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/e/e7def7a50f9c854f7aae0efc34897338c46c32c0.png"></a>

<a href="#heading--filter-on-dynamic-workload-annotations"><h4 id="heading--filter-on-dynamic-workload-annotations">Filter on dynamic (workload) annotations</h4></a>

To filter machines by dynamic (workload) annotations, use the following procedure:

1. Go to the machine list and select the "Filter" drop-down; open the "Workload" segment:

<a href="https://discourse.maas.io/uploads/default/original/2X/9/946fb41e9cefb10a0b59787ce22b70a91b248d01.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/9/946fb41e9cefb10a0b59787ce22b70a91b248d01.jpeg"></a>

2. Select one or more values from this list to filter the machine list by these workload annotations.

snap-3-0-ui deb-3-0-ui -->

<!-- snap-2-7-cli deb-2-7-cli snap-2-8-cli deb-2-8-cli snap-2-9-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli

<a href="#heading--work-with-tags"><h2 id="heading--work-with-tags">Work with tags</h2></a>

This section is devoted to procedures for working with tags.  We begin with some general operations that apply to all tags types, such as naming conventions and basic mechanics.  We then walk through the various tag types, providing procedures that will help you create, assign, remove, delete, list, view, and filter tags, covering the nuances of each type.

Specifically, this section will show you how to:

* [Work with tags, independent of application](#heading--work-with-tags-independent-of-application)
* [Work with machine tags](#heading--work-with-machine-tags)
* [Work with virtual machine host tags](#heading--work-with-virtual-machine-host-tags)
* [Work with region controller tags](#heading--work-with-region-controller-tags)
* [Work with rack controller tags](#heading--work-with-rack-controller-tags)
* [Work with block device tags](#heading--work-with-block-device-tags)
* [Work with partition tags](#heading--work-with-partition-tags)
* [Work with network tags](#heading--work-with-network-tags)
* [Work with device tags](#heading--work-with-device-tags)
* [Work with node tags](#heading--work-with-node-tags)

<a href="#heading--work-with-tags-independent-of-application"><h3 id="heading--work-with-tags-independent-of-application">Work with tags, independent of application</h3></a>

This subsection will explain how to:

* [Create a tag](#heading--create-a-tag)
* [Create tags with built-in kernel options](#heading--create-tags-with-built-in-kernel-options)
* [Delete a tag](#heading--delete-a-tag)
* [Update a tag](#heading--update-a-tag)
* [List all tags available on this MAAS](#heading--list-all-tags-available-on-this-maas)
* [Rebuild a tag](#heading--rebuild-a-tag)

<a href="#heading--create-a-tag"><h4 id="heading--create-a-tag">Create a tag</h4></a>

With the CLI, you can create a tag with the following command:

```bash
maas $PROFILE tags create name=$TAG_NAME comment='$TAG_COMMENT'
```

For example, depending upon your system configuration, you might type a command similar to this one:

```bash
maas admin tags create name="new_tag" comment="a new tag for test purposes"
```

When the command is successful, you should see output similar to this:

```nohighlight
Success.
Machine-readable output follows:
{
    "name": "new_tag",
    "definition": "",
    "comment": "a new tag for test purposes",
    "kernel_opts": "",
    "resource_uri": "/MAAS/api/2.0/tags/new_tag/"
}
```

You can verify your work by [listing all the tags on this MAAS](#heading--list-all-tags-available-on-this-maas).

<a href="#heading--create-tags-with-built-in-kernel-options"><h4 id="heading--create-tags-with-built-in-kernel-options">Create tags with built-in kernel options</h4></a>

You can create tags with embedded kernel boot options.  When you apply such tags to a machine, those kernel boot options will be applied to that machine on the next deployment.

To create a tag with embedded kernel boot options, use the following command:

```bash
maas $PROFILE tags create name='$TAG_NAME' \
    comment='$TAG_COMMENT' kernel_opts='$KERNEL_OPTIONS'
```

For example:

```bash
maas admin tags create name='nomodeset_tag' \
    comment='nomodeset_kernel_option' kernel_opts='nomodeset vga'
```

This command yields the following results:

```nohighlight
Success.
Machine-readable output follows:
{
    "name": "nomodeset_tag",
    "definition": "",
    "comment": "nomodeset_kernel_option",
    "kernel_opts": "nomodeset vga",
    "resource_uri": "/MAAS/api/2.0/tags/nomodeset_tag/"
}
```

You can check your work with a modified form of the listing command:

```bash
maas admin tags read | jq -r \
'(["tag_name","tag_comment","kernel_options"]
|(.,map(length*"-"))),(.[]|[.name,.comment,.kernel_opts]) 
| @tsv' | column -t
```

This should give you results something like this:

```nohighlight
tag_name             tag_comment                  kernel_options                     
--------             -----------                  --------------                     
virtual                                                                              
new_tag              a-new-tag-for-test-purposes                                     
pod-console-logging  console=tty1                 console=ttyS0                      
nomodeset_tag        nomodeset_kernel_option      nomodeset       vga
```

<a href="#heading--delete-a-tag"><h4 id="heading--delete-a-tag">Delete a tag</h4></a>

With the CLI, you can delete a tag with the following command:

```bash
maas $PROFILE tag delete $TAG_NAME
```

For example, depending upon your system configuration, you might type a command similar to this one:

```bash
maas admin tag delete zorko
```

When the command is successful, you should see output similar to this:

```nohighlight
Success.
Machine-readable output follows:
```

Note that there is no actual "Machine-readable output" produced by this command, in most cases. Also note that remove a tag removes it from any nodes where you may have assigned it, but does not affect those nodes in any other way.

You can check your work by [listing all the tags on this MAAS](#heading--list-all-tags-available-on-this-maas).

<a href="#heading--update-a-tag"><h4 id="heading--update-a-tag">Update a tag</h4></a>

You can update a tag (e.g., a tag comment) like this:

```bash
maas $PROFILE tag update $TAG_NAME comment='$TAG_COMMENT'
```

For example:

```bash
maas admin tag update new_tag comment="a-new-tag-for-test-purposes"
```

This should return an output similar to this one:

```nohighlight
Success.
Machine-readable output follows:
{
    "name": "new_tag",
    "definition": "",
    "comment": "a-new-tag-for-test-purposes",
    "kernel_opts": "",
    "resource_uri": "/MAAS/api/2.0/tags/new_tag/"
}
```

You can always verify by [listing all the tags on this MAAS](#heading--list-all-tags-available-on-this-maas).

<a href="#heading--list-all-tags-available-on-this-maas"><h4 id="heading--list-all-tags-available-on-this-maas">List all tags available on this MAAS</h4></a>

You can list all tags that currently exist in this MAAS with a command of the form:

```bash
maas $PROFILE tags read | jq -r '(["tag_name","tag_comment"]|(.,map(length*"-"))),(.[]|[.name,.comment]) | @tsv' | column -t
```

For example:

```bash
maas admin tags read | jq -r '(["tag_name","tag_comment"]|(.,map(length*"-"))),(.[]|[.name,.comment]) | @tsv' | column -t
```

Your output might look like this:

```nohighlight
tag_name  tag_comment
--------  -----------
virtual   
new_tag   a-new-tag-for-test-purposes
```

<a href="#heading--rebuild-a-tag"><h4 id="heading--rebuild-a-tag">Rebuild a tag</h4></a>

If you need to update tags for all machines – without having to recommission them – you can accomplish this with the rebuild command:

```
maas $PROFILE tag rebuild $TAG
```

This command automatically applies the tag to all machines regardless of state, even machines that are actively deployed. For example:

```
maas admin tag rebuild virtual
```

This command would produce output similar to the following:

```
Success.
Machine-readable output follows:
{
    "rebuilding": "virtual"
}
```

<a href="#heading--work-with-machine-tags"><h3 id="heading--work-with-machine-tags">Work with machine tags</h3></a>

This subsection will explain how to:

* [Assign machine tags to a machine](#heading--assign-machine-tags-to-a-machine)
* [Remove machine tags from a machine](#heading--remove-machine-tags-from-a-machine)
* [List machine tags for all machines](#heading--list-machine-tags-for-all-machines)
* [View machine tags for one machine](#heading--view-machine-tags-for-one-machine)

<a href="#heading--assign-machine-tags-to-a-machine"><h4 id="heading--assign-machine-tags-to-a-machine">Assign machine tags to a machine</h4></a>

You can assign tags to a physical or virtual machine with the following command:

```bash
maas $PROFILE tag update-nodes $TAG_NAME add=$SYSTEM_ID
```

For example:

```bash
maas admin tag update-nodes new_tag add=g6arwg
```

This returns something like the following:

```nohighlight
Success.
Machine-readable output follows:
{
   "added": 1,
   "removed": 0
}
```

You can check your work by listing machine tags, like this:

```bash
maas admin machines read | jq -r \
'(["hostname","sysid","machine_tags"]
|(.,map(length*"-"))),(.[]|[.hostname,.system_id,.tag_names[]])
| @tsv' | column -t
```

This should yield output similar to the following:

```nohighlight
hostname       sysid   machine_tags
--------       -----   ------------
divine-stork   8b3ypp  pod-console-logging  virtual
casual-prawn   4end6r  pod-console-logging  virtual
driven-teal    tgaat6  pod-console-logging  virtual
immune-beetle  43xand  pod-console-logging  virtual
good-osprey    napfxk  pod-console-logging  virtual
smart-hen      c4rwq7  pod-console-logging  virtual
boss-satyr     xn8taa  pod-console-logging  androko
golden-martin  8fxery  pod-console-logging  virtual
crack-guinea   qk4b3g  pod-console-logging  virtual
finer-leech    cy3dtr  pod-console-logging  virtual
free-mouse     gxtbq4  pod-console-logging  virtual
humble-bunny   srqnnb  pod-console-logging  virtual
wanted-muskox  ekw7fh  pod-console-logging  virtual
one-boa        by477d  pod-console-logging  virtual
great-urchin   srnx4g  pod-console-logging  virtual
ace-frog       g6arwg  pod-console-logging  virtual  barbar  farquar  new_tag
alive-marlin   gbwnfb  pod-console-logging  virtual
picked-parrot  am77wn  pod-console-logging  virtual
tough-kit      ke3wc7  pod-console-logging  virtual
legal-whale    8nq3mt  pod-console-logging  virtual
game-sponge    76pdc6  pod-console-logging  virtual
fun-ghoul      qxfm7k  pod-console-logging  virtual
aware-earwig   8m8hs7  pod-console-logging  virtual
chief-crane    7fapx7  pod-console-logging  virtual
select-tapir   4ascbr  pod-console-logging  virtual
on-slug        snfs8d  pod-console-logging  virtual
polite-llama   dbqd4m  pod-console-logging  virtual
frank-coyote   wcmk48  pod-console-logging  virtual
usable-condor  ed8hmy  pod-console-logging  virtual
still-imp      h6ra6d  pod-console-logging  virtual
```

<a href="#heading--remove-machine-tags-from-a-machine"><h4 id="heading--remove-machine-tags-from-a-machine">Remove machine tags from a machine</h4></a>

You can remove a tag from a physical or virtual machine with this command:

```bash
maas $PROFILE tag update-nodes $TAG_NAME remove=$SYSTEM_ID
```

For example:

```bash
maas admin tag update-nodes new_tag remove=g6arwg
```

This would produce output similar to the following:

```nohighlight
Success.
Machine-readable output follows:
{
    "added": 0,
    "removed": 1
}
```

A quick check to verify results should yield something like this:

```nohighlight
hostname       sysid   machine_tags
--------       -----   ------------
ace-frog       g6arwg  pod-console-logging  virtual  barbar  farquar
```

<a href="#heading--adding-and-removing-machine-tags-simultaneously"><h5 id="heading--adding-and-removing-machine-tags-simultaneously">Adding and removing machine tags simultaneously from multiple machines</h5></a>

You can simultaneously add and remove tags from multiple machines, as long as you are only modifying one tag, with a command like this one:

```bash
maas $PROFILE tag update-nodes $TAG_NAME add=$SYSTEM_ID1 add=$SYSTEM_ID2 remove=$SYSTEM_ID3
```

For example, to remove the tag "barbar" from machine "g6arwg," but add it to machines "8fxery" and "by477d," you could use a command like this:

```bash
maas admin tag update-nodes barbar add=8fxery add=by477d remove=g6arwg
```

This compound operation would yield a response similar to this:

```nohighlight
Success.
Machine-readable output follows:
{
    "added": 2,
    "removed": 1
}
```

Again, verifying by checking the list of machine tags, we enter a command like this:

```bash
maas admin machines read | jq -r \
'(["hostname","sysid","machine_tags"]
|(.,map(length*"-"))),(.[]|[.hostname,.system_id,.tag_names[]])
| @tsv' | column -t
```

The resulting response looks something like this:

```nohighlight
hostname       sysid   machine_tags
--------       -----   ------------
divine-stork   8b3ypp  pod-console-logging  virtual
casual-prawn   4end6r  pod-console-logging  virtual
driven-teal    tgaat6  pod-console-logging  virtual
immune-beetle  43xand  pod-console-logging  virtual
good-osprey    napfxk  pod-console-logging  virtual
smart-hen      c4rwq7  pod-console-logging  virtual
boss-satyr     xn8taa  pod-console-logging  androko
golden-martin  8fxery  pod-console-logging  virtual  barbar
crack-guinea   qk4b3g  pod-console-logging  virtual
finer-leech    cy3dtr  pod-console-logging  virtual
free-mouse     gxtbq4  pod-console-logging  virtual
humble-bunny   srqnnb  pod-console-logging  virtual
wanted-muskox  ekw7fh  pod-console-logging  virtual
one-boa        by477d  pod-console-logging  virtual  barbar
great-urchin   srnx4g  pod-console-logging  virtual
ace-frog       g6arwg  pod-console-logging  virtual  farquar
alive-marlin   gbwnfb  pod-console-logging  virtual
picked-parrot  am77wn  pod-console-logging  virtual
tough-kit      ke3wc7  pod-console-logging  virtual
legal-whale    8nq3mt  pod-console-logging  virtual
game-sponge    76pdc6  pod-console-logging  virtual
fun-ghoul      qxfm7k  pod-console-logging  virtual
aware-earwig   8m8hs7  pod-console-logging  virtual
chief-crane    7fapx7  pod-console-logging  virtual
select-tapir   4ascbr  pod-console-logging  virtual
on-slug        snfs8d  pod-console-logging  virtual
polite-llama   dbqd4m  pod-console-logging  virtual
frank-coyote   wcmk48  pod-console-logging  virtual
usable-condor  ed8hmy  pod-console-logging  virtual
still-imp      h6ra6d  pod-console-logging  virtual
```

<a href="#heading--list-machine-tags-for-all-machines"><h4 id="heading--list-machine-tags-for-all-machines">List machine tags for all machines</h4></a>

To list machine tags for all physical and virtual machines, just enter a command similar to this one:

```bash
maas $PROFILE machines read | jq -r '(["hostname","sysid","machine_tags"]|(.,map(length*"-"))),(.[]|[.hostname,.system_id,.tag_names[]]) | @tsv' | column -t
```

For example:

```bash
maas admin machines read | jq -r \
'(["hostname","sysid","machine_tags"]
|(.,map(length*"-"))),(.[]|[.hostname,.system_id,.tag_names[]])
| @tsv' | column -t
```

This gives us a listing similar to this:

```nohighlight
hostname       sysid   machine_tags
--------       -----   ------------
divine-stork   8b3ypp  pod-console-logging  virtual
casual-prawn   4end6r  pod-console-logging  virtual
driven-teal    tgaat6  pod-console-logging  virtual
immune-beetle  43xand  pod-console-logging  virtual
good-osprey    napfxk  pod-console-logging  virtual
smart-hen      c4rwq7  pod-console-logging  virtual
boss-satyr     xn8taa  pod-console-logging  androko
golden-martin  8fxery  pod-console-logging  virtual  barbar
crack-guinea   qk4b3g  pod-console-logging  virtual
finer-leech    cy3dtr  pod-console-logging  virtual
free-mouse     gxtbq4  pod-console-logging  virtual
humble-bunny   srqnnb  pod-console-logging  virtual
wanted-muskox  ekw7fh  pod-console-logging  virtual
one-boa        by477d  pod-console-logging  virtual  barbar
great-urchin   srnx4g  pod-console-logging  virtual
ace-frog       g6arwg  pod-console-logging  virtual  farquar
alive-marlin   gbwnfb  pod-console-logging  virtual
picked-parrot  am77wn  pod-console-logging  virtual
tough-kit      ke3wc7  pod-console-logging  virtual
legal-whale    8nq3mt  pod-console-logging  virtual
game-sponge    76pdc6  pod-console-logging  virtual
fun-ghoul      qxfm7k  pod-console-logging  virtual
aware-earwig   8m8hs7  pod-console-logging  virtual
chief-crane    7fapx7  pod-console-logging  virtual
select-tapir   4ascbr  pod-console-logging  virtual
on-slug        snfs8d  pod-console-logging  virtual
polite-llama   dbqd4m  pod-console-logging  virtual
frank-coyote   wcmk48  pod-console-logging  virtual
usable-condor  ed8hmy  pod-console-logging  virtual
still-imp      h6ra6d  pod-console-logging  virtual
```

<a href="#heading--view-machine-tags-for-one-machine"><h4 id="heading--view-machine-tags-for-one-machine">View machine tags for one machine</h4></a>

To view tags for one physical or machine, you can enter a command like this:

```bash
maas $PROFILE machine read $SYSTEM_ID | jq -r '(["hostname","sysid","machine_tags"]|(.,map(length*"-"))),([.hostname,.system_id,.tag_names[]]) | @tsv' | column -t
```

For example:

```bash
maas admin machine read 8fxery | jq -r \
'(["hostname","sysid","machine_tags"]
|(.,map(length*"-"))),([.hostname,.system_id,.tag_names[]])
| @tsv' | column -t
```

Typical output from this command might look like this:

```nohighlight
hostname       sysid   machine_tags
--------       -----   ------------
golden-martin  8fxery  pod-console-logging  virtual  barbar
```

<a href="#heading--work-with-virtual-machine-host-tags"><h3 id="heading--work-with-virtual-machine-host-tags">Work with virtual machine host tags</h3></a>

This subsection will show you how to:

* [Discover your virtual machine host ID](#heading--discover-your-vm-host-id)
* [Assign tags to a virtual machine host](#heading--assign-tags-to-a-vm-host)
* [Remove tags from a virtual machine](#heading--remove-tags-from-a-vm-host)
* [List tags for all virtual machines](#heading--list-tags-for-all-vm-hosts)
* [View tags for one virtual machine](#heading--view-tags-for-one-vm-host)

<a href="#heading--discover-your-vm-host-id"><h4 id="heading--discover-your-vm-host-id">Discover your virtual machine host ID</h4></a>

If you don't know your VM host ID, you can discover it with this command:

```bash
maas $PROFILE vmhosts read \
| jq -r '(["vm_host_name","id"]
|(.,map(length*"-"))),(.[]|[.name,.id])
| @tsv' | column -t
```

For example:

```bash
maas admin vmhosts read \
| jq -r '(["vm_host_name","id"]
|(.,map(length*"-"))),(.[]|[.name,.id])
| @tsv' | column -t
```

This should produce output similar to the following:

```nohighlight
vm_host_name      id
------------      --
my-lxd-vm-host-1  1
```

<a href="#heading--assign-tags-to-a-vm-host"><h4 id="heading--assign-tags-to-a-vm-host">Assign tags to a virtual machine host</h4></a>

To assign a tag to a virtual machine host, enter the following command:

```bash
maas $PROFILE vmhost add-tag $VMHOST_ID	tag=$TAG_NAME
```

If you don't know the ID of your VM host, you can [look it up beforehand](#heading--discover-your-vm-host-id).

As an example of assigning a tag to a VM host:

```
maas admin vmhost add-tag 1 tag=virtual
```

If it worked, this should return `Success`, followed by the JSON that describes the VM host. You can check your work by [listing all VM host tags](#heading--list-tags-for-all-vm-hosts).

<a href="#heading--remove-tags-from-a-vm-host"><h4 id="heading--remove-tags-from-a-vm-host">Remove tags from a virtual machine host</h4></a>

To remove a tag from a virtual machine host, enter the following command:

```
maas $PROFILE vmhost remove-tag $VMHOST_ID tag=$TAG_NAME
```

If you don't know the ID of your VM host, you can [look it up beforehand](#heading--discover-your-vm-host-id).

As an example of removing a tag from a VM host:

```
maas admin vmhost remove-tag 1 tag=virtual
```

If it worked, this should return `Success`, followed by the JSON that describes the VM host. You can check your work by [listing all VM host tags](#heading--list-tags-for-all-vm-hosts).


<a href="#heading--list-tags-for-all-vm-hosts"><h4 id="heading--list-tags-for-all-vm-hosts">List tags for all virtual machine hosts</h4></a>

You can list tags for all VM hosts with the following command:

```
maas $PROFILE vmhosts read | jq -r '(["vm_host_name","id","tags"]|(.,map(length*"-"))),(.[]|[.name,.id,.tags[]]) | @tsv' | column -t
```

For example:

```
maas admin vmhosts read | jq -r '(["vm_host_name","id","tags"]|(.,map(length*"-"))),(.[]|[.name,.id,.tags[]]) | @tsv' | column -t
```

This should yield output similar to the following:

```
vm_host_name      id  tags
------------      --  ----
my-lxd-vm-host-1  1   morkopongo  pod-console-logging  virtual
```

<a href="#heading--view-tags-for-one-vm-host"><h4 id="heading--view-tags-for-one-vm-host">View tags for one virtual machine host</h4></a>

If you want to list the tags for just one VM host, you can use a command like this one:

```
maas $PROFILE vmhost read $VMHOST_ID \
| jq -r '(["name","id","tags"]
|(.,map(length*"-"))),([.name,.id,.tags[]])
| @tsv' | column -t
```
If you don't know the ID of your VM host, you can [look it up beforehand](#heading--discover-your-vm-host-id).

As an example of viewing tags for one VM host:

```
maas admin vmhost read 1 | jq -r '("name","id","tags"]|(.,map(length*"-"))),([.name,.id,.tags[]]) | @tsv' @ column -t
```

Typical output might look something like this:

```
name              id  tags
----              --  ----
my-lxd-vm-host-1  1   morkopongo  pod-console-logging
```

<a href="#heading--work-with-region-controller-tags"><h3 id="heading--work-with-region-controller-tags">Work with region controller tags</h3></a>

This subsection will show you how to:

* [Discover the ID of your region controller(s)](#heading--discover-the-id-of-your-region-controllers)
* [Assign tags to a region controller](#heading--assign-tags-to-a-region-controller)
* [Remove tags from a region controller](#heading--remove-tags-from-a-region-controller)
* [List tags for all region controllers](#heading--list-tags-for-all-region-controllers)
* [View tags for one region controller](#heading--view-tags-for-one-region-controller)

<a href="#heading--discover-the-id-of-your-region-controllers"><h4 id="heading--discover-the-id-of-your-region-controllers">Discover the ID of your region controller(s)</h4></a>

You can discover the ID of your region controller(s) with the following command:

```bash
maas $PROFILE region-controllers read \
| jq -r '(["name","id"]
|(.,map(length*"-"))),(.[]|[.hostname,.system_id])
| @tsv' | column -t
```

For example:

```bash
maas admin region-controllers read \
| jq -r '(["name","id"]
|(.,map(length*"-"))),(.[]|[.hostname,.system_id])
| @tsv' | column -t
```

Typical output would look something like this:

```nohighlight
name                         id
----                         --
bill-Lenovo-Yoga-C740-15IML  86xya8
```

<a href="#heading--assign-tags-to-a-region-controller"><h4 id="heading--assign-tags-to-a-region-controller">Assign tags to a region controller</h4></a>

To add tags to a region controller, you can use a command of this form:

```bash
maas $PROFILE tag update-nodes $TAG_NAME add=$SYSTEM_ID
```

If you need to find the ID of your region controller(s), you can [look it up](#heading--discover-the-id-of-your-region-controllers).

For example:

```bash
maas admin tag update-nodes virtual add=86xya8
```

This command produces output similar to the following:

```nohighlight
Success.
Machine-readable output follows:
{
    "added": 1,
    "removed": 0
}
```

You can check your work by [listing all tags for your region controllers](#heading--list-tags-for-all-region-controllers).

<a href="#heading--remove-tags-from-a-region-controller"><h4 id="heading--remove-tags-from-a-region-controller">Remove tags from a region controller</h4></a>

To remove tags from a region controller, you can use a command like this:

```bash
maas $PROFILE tag update-nodes $TAG_NAME remove=$SYSTEM_ID
```

If you need to find the ID of your region controller(s), you can [look it up](#heading--discover-the-id-of-your-region-controllers).

For example:

```bash
maas admin tag update-nodes virtual remove=86xya8
```

This command produces output similar to the following:

```nohighlight
Success.
Machine-readable output follows:
{
    "added": 0,
    "removed": 1
}
```

You can check your work by [listing all tags for your region controllers](#heading--list-tags-for-all-region-controllers).

<a href="#heading--list-tags-for-all-region-controllers"><h4 id="heading--list-tags-for-all-region-controllers">List tags for all region controllers</h4></a>

To list tags for all region controllers, you can use a command similar to this:

```bash
maas $PROFILE region-controllers read | jq -r '(["hostname","sysid","tags"]|(.,map(length*"-"))),(.[]|[.hostname,.system_id,.tag_names[]]) | @tsv' | column -t
```

For example:

```bash
maas admin region-controllers read | jq -r '(["hostname","sysid","tags"]|(.,map(length*"-"))),(.[]|[.hostname,.system_id,.tag_names[]]) | @tsv' | column -t
```

This will produce output something like this:

```nohighlight
hostname                     sysid   tags
--------                     -----   ----
bill-Lenovo-Yoga-C740-15IML  86xya8  virtual  lxd-vm-host
```

<a href="#heading--view-tags-for-one-region-controller"><h4 id="heading--view-tags-for-one-region-controller">View tags for one region controller</h4></a>

To view tags for a specific region controller, you can try a command like this:

```bash
maas $PROFILE region-controller read $SYSTEM_ID | jq -r '(["hostname","sysid","tags"]|(.,map(length*"-"))),([.hostname,.system_id,.tag_names[]]) | @tsv' | column -t
'''

If you need to find the ID of your region controller(s), you can [look it up](#heading--discover-the-id-of-your-region-controllers).

For example:

```bash
maas admin region-controller read 86xya8 \
| jq -r '(["hostname","sysid","tags"]
|(.,map(length*"-"))),([.hostname,.system_id,.tag_names[]])
| @tsv' | column -t
```

This should produce output similar to the following:

```nohighlight
hostname                     sysid   tags
--------                     -----   ----
bill-Lenovo-Yoga-C740-15IML  86xya8  virtual  lxd-vm-host
```

<a href="#heading--work-with-rack-controller-tags"><h3 id="heading--work-with-rack-controller-tags">Work with rack controller tags</h3></a>

This subsection will show you how to:

* [Discover the ID of your rack controller(s)](#heading--discover-the-id-of-your-rack-controllers)
* [Assign tags to a rack controller](#heading--assign-tags-to-a-rack-controller)
* [Remove tags from a rack controller](#heading--remove-tags-from-a-rack-controller)
* [List tags for all rack controllers](#heading--list-tags-for-all-rack-controllers)
* [View tags for one rack controller](#heading--view-tags-for-one-rack-controller)

<a href="#heading--discover-the-id-of-your-rack-controllers"><h4 id="heading--discover-the-id-of-your-rack-controllers">Discover the ID of your rack controller(s)</h4></a>

You can discover the ID of your rack controller(s) with the following command:

```bash
maas $PROFILE rack-controllers read \
| jq -r '(["name","id"]
|(.,map(length*"-"))),(.[]|[.hostname,.system_id])
| @tsv' | column -t
```

For example:

```bash
maas admin rack-controllers read \
| jq -r '(["name","id"]
|(.,map(length*"-"))),(.[]|[.hostname,.system_id])
| @tsv' | column -t
```

Typical output would look something like this:

```nohighlight
name                         id
----                         --
bill-Lenovo-Yoga-C740-15IML  86xya8
```

<a href="#heading--assign-tags-to-a-rack-controller"><h4 id="heading--assign-tags-to-a-rack-controller">Assign tags to a rack controller</h4></a>

To add tags to a rack controller, you can use a command of this form:

```bash
maas $PROFILE tag update-nodes $TAG_NAME add=$SYSTEM_ID
```

If you need to find the ID of your rack controller(s), you can [look it up](#heading--discover-the-id-of-your-rack-controllers).

For example:

```bash
maas admin tag update-nodes virtual add=86xya8
```

This command produces output similar to the following:

```nohighlight
Success.
Machine-readable output follows:
{
    "added": 1,
    "removed": 0
}
```

You can check your work by [listing all tags for your rack controllers](#heading--list-tags-for-all-rack-controllers).

<a href="#heading--remove-tags-from-a-rack-controller"><h4 id="heading--remove-tags-from-a-rack-controller">Remove tags from a rack controller</h4></a>

To remove tags from a rack controller, you can use a command like this:

```bash
maas $PROFILE tag update-nodes $TAG_NAME remove=$SYSTEM_ID
```

If you need to find the ID of your rack controller(s), you can [look it up](#heading--discover-the-id-of-your-rack-controllers).

For example:

```bash
maas admin tag update-nodes virtual remove=86xya8
```

This command produces output similar to the following:

```nohighlight
Success.
Machine-readable output follows:
{
    "added": 0,
    "removed": 1
}
```

You can check your work by [listing all tags for your rack controllers](#heading--list-tags-for-all-rack-controllers).

<a href="#heading--list-tags-for-all-rack-controllers"><h4 id="heading--list-tags-for-all-rack-controllers">List tags for all rack controllers</h4></a>

To list tags for all rack controllers, you can use a command similar to this:

```bash
maas $PROFILE rack-controllers read | jq -r '(["hostname","sysid","tags"]|(.,map(length*"-"))),(.[]|[.hostname,.system_id,.tag_names[]]) | @tsv' | column -t
```

For example:

```bash
maas admin rack-controllers read | jq -r '(["hostname","sysid","tags"]|(.,map(length*"-"))),(.[]|[.hostname,.system_id,.tag_names[]]) | @tsv' | column -t
```

This will produce output something like this:

```nohighlight
hostname                     sysid   tags
--------                     -----   ----
bill-Lenovo-Yoga-C740-15IML  86xya8  virtual  lxd-vm-host
```

<a href="#heading--view-tags-for-one-rack-controller"><h4 id="heading--view-tags-for-one-rack-controller">View tags for one rack controller</h4></a>

To view tags for a specific rack controller, you can try a command like this:

```bash
maas $PROFILE rack-controller read $SYSTEM_ID | jq -r '(["hostname","sysid","tags"]|(.,map(length*"-"))),([.hostname,.system_id,.tag_names[]]) | @tsv' | column -t
'''

If you need to find the ID of your rack controller(s), you can [look it up](#heading--discover-the-id-of-your-rack-controllers).

For example:

```bash
maas admin rack-controller read 86xya8 \
| jq -r '(["hostname","sysid","tags"]
|(.,map(length*"-"))),([.hostname,.system_id,.tag_names[]])
| @tsv' | column -t
```

This should produce output similar to the following:

```nohighlight
hostname                     sysid   tags
--------                     -----   ----
bill-Lenovo-Yoga-C740-15IML  86xya8  virtual  lxd-vm-host
```

<a href="#heading--work-with-block-device-tags"><h3 id="heading--work-with-block-device-tags">Work with block device tags</h3></a>

This subsection will show you how to:

* [Discover the ID of your block device](#heading--discover-the-id-of-your-block-device) 
* [Assign tags to a block device](#heading--assign-tags-to-a-block-device)
* [Remove tags from a block device](#heading--remove-tags-from-a-block-device)
* [List tags for all block devices](#heading--list-tags-for-all-block-devices)
* [View tags for one block device](#heading--view-tags-for-one-block-device)

<a href="#heading--discover-the-id-of-your-block-device"><h4 id="heading--discover-the-id-of-your-block-device">Discover the ID of your block device</h4></a>

Block devices do not exist apart from the physical or virtual machines to which they are attached.  Finding the ID of the block device that interests you requires starting with a particular machine, in a command form that looks like this:

```bash
maas $PROFILE block-devices read $SYSTEM_ID \
| jq -r '(["system_id","block_device_id","path","avail_size"]
|(.,map(length*"-"))),(.[]|[.system_id,.id,.path,.available_size])
| @tsv' | column -t
```

For example:

```bash
maas admin block-devices read qk4b3g \
| jq -r '(["system_id","block_device_id","path","avail_size"]
|(.,map(length*"-"))),(.[]|[.system_id,.id,.path,.available_size])
| @tsv' | column -t
```

This example would produce output that looks something like this:

```nohighlight
system_id  block_device_id  path                    avail_size
---------  ---------------  ----                    ----------
qk4b3g     10               /dev/disk/by-dname/sda  0
```

The `path` component is printed to help you confirm that you are choosing the right block device, when there are several present.  The `avail-size` column will tell you whether you can operate on that block device at all: If the available size is "0," for example, you can't set a block device tag on any part of that drive.  Instead, you'd want to see something like this:

```nohighlight
system_id  block_device_id  path                    avail_size
---------  ---------------  ----                    ----------
xn8taa     8                /dev/disk/by-dname/sda  1996488704
```

<a href="#heading--assign-tags-to-a-block-device"><h4 id="heading--assign-tags-to-a-block-device">Assign tags to a block device</h4></a>

You can only assign tags to a block device that is available. You can find out whether the block device is available at all when you [discover its ID](#heading--discover-the-id-of-your-block-device).

To assign an existing tag to a block device, you would type a command formulated like this:

```bash
maas $PROFILE block-device add-tag $SYSTEM_ID $BLOCK_DEVICE_ID tag=$TAG_NAME
```

If you're not sure about the ID of your block device, you can [look it up](#heading--discover-the-id-of-your-block-device).

For example:

```
maas admin block-device add-tag xn8taa 8 tag=farquar
```

If this command succeeds, it will display `Success`, followed by a JSON sequence describing the new state of the block device.

Note that if you try to add a tag to a block device that is not available, that is, to a block device that is in use, you will get a result like this:

```nohighlight
Not Found
```

<a href="#heading--remove-tags-from-a-block-device"><h4 id="heading--remove-tags-from-a-block-device">Remove tags from a block device</h4></a>

You can only remove tags from a block device that is available. You can find out whether the block device is available at all when you [discover its ID](#heading--discover-the-id-of-your-block-device).

To remove an assigned tag from a block device, you would type a command formulated like this:

```bash
maas $PROFILE block-device remove-tag $SYSTEM_ID $BLOCK_DEVICE_ID tag=$TAG_NAME
```

If you're not sure about the ID of your block device, you can [look it up](#heading--discover-the-id-of-your-block-device).

For example:

```
maas admin block-device remove-tag xn8taa 8 tag=farquar
```

If this command succeeds, it will display `Success`, followed by a JSON sequence describing the new state of the block device.

Note that if you try to remove a tag from a block device that is not available, that is, to a block device that is in use, you will get a result like this:

```nohighlight
Not Found
```

<a href="#heading--list-tags-for-all-block-devices"><h4 id="heading--list-tags-for-all-block-devices">List tags for all block devices</h4></a>

To list tags for all block devices associated with a physical or virtual machine, you can use a command of this form:

```bash
maas $PROFILE block-devices read $SYSTEM_ID | jq -r '(["id","tags"]|(.,map(length*"-"))),(.[]|[.id,.tags[]]) | @tsv' | column -t
```

For example:

```bash
maas admin block-devices read xn8taa | jq -r '(["id","tags"]|(.,map(length*"-"))),(.[]|[.id,.tags[]]) | @tsv' | column -t
```

This command would produce output similar to this:

```nohighlight
id  tags
--  ----
8   hello  ssd  trinkoplinko
```

<a href="#heading--view-tags-for-one-block-device"><h4 id="heading--view-tags-for-one-block-device">View tags for one block device</h4></a>

To view tags for one specific block device, you can enter a command like this:

```bash
maas $PROFILE block-device read $SYSTEM_ID $BLOCK_DEVICE_ID | jq -r '(["id","tags"]|(.,map(length*"-"))),([.id,.tags[]]) | @tsv' | column -t
```

If you're not sure about the ID of your block device, you can [look it up](#heading--discover-the-id-of-your-block-device).

For example:

```bash
maas admin block-device read xn8taa 8 | jq -r '(["id","tags"]|(.,map(length*"-"))),([.id,.tags[]]) | @tsv' | column -t
```

This command would produce output similar to this:

```nohighlight
id  tags
--  ----
8   hello  ssd  trinkoplinko
9   20gig  ssd
10  250Gs  ssd
```

<a href="#heading--work-with-partition-tags"><h3 id="heading--work-with-partition-tags">Work with partition tags</h3></a>

This subsection will show you how to:

* [Discover the ID of your partition](#heading--discover-the-id-of-your-partition)
* [Assign tags to a partition](#heading--assign-tags-to-a-partition)
* [Remove tags from a partition](#heading--remove-tags-from-a-partition)
* [List tags for all partitions](#heading--list-tags-for-all-partitions)
* [View tags for one partition](#heading--view-tags-for-one-partition)

<a href="#heading--discover-the-id-of-your-partition"><h4 id="heading--discover-the-id-of-your-partition">Discover the ID of your partition</h4></a>

Partitions do not exist apart from the block devices on which they reside.  Finding the ID of the partition that interests you requires starting with a particular machine and block device, similar to this command:

```bash
maas $PROFILE partitions read $SYSTEM_ID $BLOCK_DEVICE_ID \
| jq -r '(["system_id","block_dev_id","part_id","path"]
|(.,map(length*"-"))),(.[]|[.system_id,.device_id,.id,.path])
|@tsv' | column -t
```

For example:

```bash
maas admin partitions read xn8taa 8 \
| jq -r '(["system_id","block_dev_id","part_id","path"]
|(.,map(length*"-"))),(.[]|[.system_id,.device_id,.id,.path])
|@tsv' | column -t
 ```

This example would produce output that looks something like this:

```nohighlight
system_id  block_dev_id  part_id  path
---------  ------------  -------  ----
xn8taa     8             67       /dev/disk/by-dname/sda-part1
```

The `path` component is printed to help you confirm that you are choosing the right partition, when there are several present.  

<a href="#heading--assign-tags-to-a-partition"><h4 id="heading--assign-tags-to-a-partition">Assign tags to a partition</h4></a>

You can only assign tags to a partition that is available.  To assign an existing tag to a partition, you would type a command formulated like this:

```bash
maas $PROFILE partition add-tag $SYSTEM_ID $BLOCK_DEVICE_ID $PARTITION_ID tag=$TAG_NAME
```

If you're not sure about the ID of your partition, you can [look it up](#heading--discover-the-id-of-your-partition).

For example:

```bash
maas admin partition add-tag xn8taa 8 67 tag=farquar
```

If this command succeeds, it will display `Success`, followed by a JSON sequence describing the new state of the partition.

Note that if you try to add a tag to a partition that is not available, that is, to a partition that is in use, you will get a result like this:

```nohighlight
Not Found
```

<a href="#heading--remove-tags-from-a-partition"><h4 id="heading--remove-tags-from-a-partition">Remove tags from a partition</h4></a>

You can only remove tags from a partition that is available.  To remove a existing tag from a partition, you would type a command formulated like this:

```bash
maas $PROFILE partition remove-tag $SYSTEM_ID $BLOCK_DEVICE_ID $PARTITION_ID tag=$TAG_NAME
```

If you're not sure about the ID of your partition, you can [look it up](#heading--discover-the-id-of-your-partition).

For example:

```bash
maas admin partition remove-tag xn8taa 8 67 tag=farquar
```

If this command succeeds, it will display `Success`, followed by a JSON sequence describing the new state of the partition.

Note that if you try to remove a tag from a partition that is not available, that is, to a partition that is in use, you will get a result like this:

```nohighlight
Not Found
```

On the other hand, if you try to remove a tag that is not assigned to the partition you've chosen, MAAS will simply return `Success`, followed by a JSON sequence describing the current state of the partition.

<a href="#heading--list-tags-for-all-partitions"><h4 id="heading--list-tags-for-all-partitions">List tags for all partitions</h4></a>

To list tags for all partitions of a particular block device, use a command like this one:

```bash
maas $PROFILE partitions read $SYSTEM_ID $BLOCK_DEVICE_ID \
| jq -r '(["id","tags"]
|(.,map(length*"-"))),(.[]|[.id,.tags[]])
| @tsv' | column -t
```

For example:

```bash
maas admin partitions read xn8taa 8 \
| jq -r '(["id","tags"]
|(.,map(length*"-"))),(.[]|[.id,.tags[]])
| @tsv' | column -t
```

A command like this should return output similar to the following:

```nohighlight
id  tags
--  ----
54  farquar swap opendisk
67  foobar  farquar
97  foobar
```

<a href="#heading--view-tags-for-one-partition"><h4 id="heading--view-tags-for-one-partition">View tags for one partition</h4></a>

To view tags for one partition, enter a command similar to this:

```bash
maas $PROFILE partition read $SYSTEM_ID $BLOCK_DEVICE_ID $PARTITION_ID | jq -r '(["id","tags"]|(.,map(length*"-"))),([.id,.tags[]]) | @tsv' | column -t
```

If you're not sure about the ID of your partition, you can [look it up](#heading--discover-the-id-of-your-partition).

For example:

```bash
maas admin partition read xn8taa 8 67 | jq -r '(["id","tags"]|(.,map(length*"-"))),([.id,.tags[]]) | @tsv' | column -t
```

This command should produce output similar to this:

```nohighlight
id  tags
--  ----
67  foobar  farquar
```

<a href="#heading--work-with-network-tags"><h3 id="heading--work-with-network-tags">Work with network tags</h3></a>

This subsection will show you how to:

* [Discover the ID of your network interface](#heading--discover-the-id-of-your-network-interface)
* [Assign tags to a network interface](#heading--assign-tags-to-a-network-interface)
* [Remove tags from a network interface](#heading--remove-tags-from-a-network-interface)
* [List tags for all network interfaces](#heading--list-tags-for-all-network-interfaces)
* [View tags for one network interface](#heading--view-tags-for-one-network-interface)

<a href="#heading--discover-the-id-of-your-network-interface"><h4 id="heading--discover-the-id-of-your-network-interface">Discover the ID of your network interface</h4></a>

You can use a command of the following form to identify the interfaces associated with a particular device on your MAAS:

```bash
maas $PROFILE interfaces read $SYSTEM_ID \
| jq -r '(["mac_address","type","id","tags"]
|(.,map(length*"-"))),(.[]|[.mac_address,.type,.id,.tags[]])
|@tsv'| column -t
```

For example:

```bash
maas admin interfaces read xn8taa \
| jq -r '(["mac_address","type","id","tags"]
|(.,map(length*"-"))),(.[]|[.mac_address,.type,.id,.tags[]])
|@tsv'| column -t
```

This would produce output similar to the following:

```nohighlight
mac_address        type      id  tags
-----------        ----      --  ----
00:16:3e:18:7f:ee  physical  9   andrpko  plinko  cochise
```

<a href="#heading--assign-tags-to-a-network-interface"><h4 id="heading--assign-tags-to-a-network-interface">Assign tags to a network interface</h4></a>

To assign a tag to a network interface, using both the device system ID and the interface ID, use a command of the following form:

```bash
maas $PROFILE interface add-tag $SYSTEM_ID $INTERFACE_ID tag=$TAG_NAME
```

For example:

```bash
maas admin interface add-tag xn8taa 9 tag=farquar
```

This command, if successful, will produce a long sequence of JSON describing the interface, including the changes introduced by the command above.  You can also check your work by [listing the tags](#heading--list-tags-for-all-network-interfaces) associated with the device.

<a href="#heading--remove-tags-from-a-network-interface"><h4 id="heading--remove-tags-from-a-network-interface">Remove tags from a network interface</h4></a>

To remove a tag from a network interface, use both the device system ID and the interface ID in a command similar to this one:

```bash
maas $PROFILE interface remove-tag $SYSTEM_ID $INTERFACE_ID tag=$TAG_NAME
```

For example:

```bash
maas admin interface remove-tag xn8taa 9 tag=farquar
```

This command, if successful, will produce a long sequence of JSON describing the interface, including the changes introduced by the command above.  You can also check your work by [listing the tags](#heading--list-tags-for-all-network-interfaces) associated with the device.

<a href="#heading--list-tags-for-all-network-interfaces"><h4 id="heading--list-tags-for-all-network-interfaces">List tags for all network interfaces</h4></a>

To list all the tags for a given network interface on a given device, use a command like this one:

```bash
maas $PROFILE interfaces read $SYSTEM_ID \
| jq -r '(["mac_address","type","id","tags"]
|(.,map(length*"-"))),(.[]|[.mac_address,.type,.id,.tags[]])
|@tsv'| column -t
```

For example:

```bash
maas admin interfaces read xn8taa \
| jq -r '(["mac_address","type","id","tags"]
|(.,map(length*"-"))),(.[]|[.mac_address,.type,.id,.tags[]])
|@tsv'| column -t
```

This would produce output similar to the following:

```nohighlight
mac_address        type      id  tags
-----------        ----      --  ----
00:16:3e:18:7f:ee  physical  9   andrpko  plinko  cochise  farquar
```

<a href="#heading--view-tags-for-one-network-interface"><h4 id="heading--view-tags-for-one-network-interface">View tags for one network interface</h4></a>

To view tags for one particular network interface on a specific device, try a command formulated like this:

```bash
maas $PROFILE interface read $SYSTEM_ID $INTERFACE_ID \
| jq -r '(["mac_address","type","id","tags"]
|(.,map(length*"-"))),([.mac_address,.type,.id,.tags[]])
|@tsv'| column -t
```

For example:

```bash
maas admin interface read xn8taa 9 \
| jq -r '(["mac_address","type","id","tags"]
|(.,map(length*"-"))),([.mac_address,.type,.id,.tags[]])
|@tsv'| column -t
```

Typical output might look like this:

```nohighlight
mac_address        type      id  tags
-----------        ----      --  ----
00:16:3e:18:7f:ee  physical  9   andrpko  plinko  cochise
```

<a href="#heading--work-with-device-tags"><h3 id="heading--work-with-device-tags">Work with device tags</h3></a>

This subsection will show you how to:

* [Identify your devices](#heading--identify-your-devices)
* [Assign tags to a device](#heading--assign-tags-to-a-device)
* [Remove tags from a device](#heading--remove-tags-from-a-device)
* [List tags for all devices](#heading--list-tags-for-all-devices)
* [View tags for one device](#heading--view-tags-for-one-device)

<a href="#heading--identify-your-devices"><h4 id="heading--identify-your-devices">Identify your devices</h4></a>

You can use a command similar to the following to identify your devices:

```bash
maas $PROFILE devices read \
| jq -r '(["hostname","system_id"]
|(.,map(length*"-"))),(.[]|[.hostname,.system_id])
|@tsv' | column -t
```

For example:

```bash
maas admin devices read \
| jq -r '(["hostname","system_id"]
|(.,map(length*"-"))),(.[]|[.hostname,.system_id])
|@tsv' | column -t
```

This command produces a result similar to the following:

```nohighlight
hostname     system_id
--------     ---------
better-sole  t8pmrs
light-aphid  76b6tt
```

<a href="#heading--assign-tags-to-a-device"><h4 id="heading--assign-tags-to-a-device">Assign tags to a device</h4></a>

To assign tags to a device, you can use a command of the following form:

```
maas $PROFILE tag update-nodes $TAG_NAME add=$SYSTEM_ID
```

For example:

```bash
maas admin tag update-nodes farquar add=t8pmrs
```

A successful command like this might produce output similar to this:

```
Success.
Machine-readable output follows:
{
    "added": 1,
    "removed": 0
}
```

You can also check your work by [listing tags for all devices](#heading--list-tags-for-all-devices).

<a href="#heading--remove-tags-from-a-device"><h4 id="heading--remove-tags-from-a-device">Remove tags from a device</h4></a>

To remove tags from a device, you can use a command of the following form:

```
maas $PROFILE tag update-nodes $TAG_NAME remove=$SYSTEM_ID
```

For example:

```bash
maas admin tag update-nodes farquar remove=t8pmrs
```

A successful command like this might produce output similar to this:

```nohighlight
Success.
Machine-readable output follows:
{
    "added": 0,
    "removed": 1
}
```

You can also check your work by [listing tags for all devices](#heading--list-tags-for-all-devices).

<a href="#heading--list-tags-for-all-devices"><h4 id="heading--list-tags-for-all-devices">List tags for all devices</h4></a>

If you want to list tags for all devices, you could use a command similar to this one:

```bash
maas $PROFILE devices read \
| jq -r '(["hostname","system_id","tags"]
|(.,map(length*"-"))),(.[]|[.hostname,.system_id,.tag_names[]])
|@tsv' | column -t
```

For example:

```bash
maas admin devices read \
| jq -r '(["hostname","system_id","tags"]
|(.,map(length*"-"))),(.[]|[.hostname,.system_id,.tag_names[]])
|@tsv' | column -t
```

Such a command would produce output that looks something like this:

```nohighlight
hostname     system_id  tags
--------     ---------  ----
better-sole  t8pmrs     farquar
light-aphid  76b6tt
```

<a href="#heading--view-tags-for-one-device"><h4 id="heading--view-tags-for-one-device">View tags for one device</h4></a>

You can view the tags for a single device with the command:

```bash
maas $PROFILE device read $SYSTEM_ID \
| jq -r '(["hostname","system_id","tags"]
|(.,map(length*"-"))),([.hostname,.system_id,.tag_names[]])
|@tsv' | column -t
```

If you need to know the system ID of your device, you can [look it up](#heading--identify-your-devices).

[note]
Note that this command differs in that (1) it uses the singular "device" instead of "devices;" (2) it gives the system ID of a specific device; and (3) it uses the single-record form of the ```jq``` tag list ("([.hostname,.system_id,.tag_names[]]", rather than "(.[]|[.hostname....").
[/note]

For example:

```bash
maas admin device read t8pmrs \
| jq -r '(["hostname","system_id","tags"]
|(.,map(length*"-"))),([.hostname,.system_id,.tag_names[]])
|@tsv' | column -t
```

Sample output might look like this:

```nohighlight
hostname     system_id  tags
--------     ---------  ----
better-sole  t8pmrs     farquar
```

<a href="#heading--work-with-node-tags"><h3 id="heading--work-with-node-tags">Work with node tags</h3></a>

* [Identify your nodes](#heading--identify-your-nodes)
* [Assign tags to a node](#heading--assign-tags-to-a-node)
* [Remove tags from a node](#heading--remove-tags-from-a-node)
* [List tags for all nodes](#heading--list-tags-for-all-nodes)
* [View tags for one node](#heading--view-tags-for-one-node)

<a href="#heading--identify-your-nodes"><h4 id="heading--identify-your-nodes">Identify your nodes</h4></a>

If you need to identify the system ID of your nodes, you can do so with a command like this one:

```bash
maas $PROFILE nodes read \
| jq -r '(["hostname","system_id"]
|(.,map(length*"-"))),(.[]|[.hostname,.system_id])
|@tsv'|column -t
```

For example:

```bash
```

When listing nodes, you should expect a large output, similar to this or larger:

```nohighlight
hostname                     system_id
--------                     ---------
better-sole                  t8pmrs
light-aphid                  76b6tt
divine-stork                 8b3ypp
casual-prawn                 4end6r
driven-teal                  tgaat6
immune-beetle                43xand
good-osprey                  napfxk
smart-hen                    c4rwq7
boss-satyr                   xn8taa
golden-martin                8fxery
crack-guinea                 qk4b3g
finer-leech                  cy3dtr
free-mouse                   gxtbq4
humble-bunny                 srqnnb
wanted-muskox                ekw7fh
one-boa                      by477d
great-urchin                 srnx4g
ace-frog                     g6arwg
alive-marlin                 gbwnfb
picked-parrot                am77wn
tough-kit                    ke3wc7
legal-whale                  8nq3mt
game-sponge                  76pdc6
fun-ghoul                    qxfm7k
aware-earwig                 8m8hs7
chief-crane                  7fapx7
select-tapir                 4ascbr
on-slug                      snfs8d
polite-llama                 dbqd4m
frank-coyote                 wcmk48
usable-condor                ed8hmy
still-imp                    h6ra6d
bill-Lenovo-Yoga-C740-15IML  86xya8
```

A node listing will show all the machines, controllers, and devices in the system.

<a href="#heading--assign-tags-to-a-node"><h4 id="heading--assign-tags-to-a-node">Assign tags to a node</h4></a>

To assign tags to any node (regardless of its type), you can use a command of this form:

'''bash
maas $PROFILE tag update-nodes $TAG_NAME add=$SYSTEM_ID
'''

For example, 

```
maas $PROFILE tag update-nodes $TAG_NAME add=$SYSTEM_ID
```

For example:

```bash
maas admin tag update-nodes farquar add=t8pmrs
```

A successful command like this might produce output similar to this:

```
Success.
Machine-readable output follows:
{
    "added": 1,
    "removed": 0
}
```

You can also check your work by [listing tags for all devices](#heading--list-tags-for-all-nodes).

<a href="#heading--remove-tags-from-a-node"><h4 id="heading--remove-tags-from-a-node">Remove tags from a node</h4></a>

To remove tags from a node, regardless of type, you can use a command like this one:

```
maas $PROFILE tag update-nodes $TAG_NAME remove=$SYSTEM_ID
```

For example:

```bash
maas admin tag update-nodes farquar remove=t8pmrs
```

A successful command like this might produce output similar to this:

```nohighlight
Success.
Machine-readable output follows:
{
    "added": 0,
    "removed": 1
}
```

You can also check your work by [listing tags for all devices](#heading--list-tags-for-all-nodes).

<a href="#heading--list-tags-for-all-nodes"><h4 id="heading--list-tags-for-all-nodes">List tags for all nodes</h4></a>

If you want to list tags for all nodes, you could use a command similar to this one:

```bash
maas $PROFILE nodes read \
| jq -r '(["hostname","system_id","tags"]
|(.,map(length*"-"))),(.[]|[.hostname,.system_id,.tag_names[]])
|@tsv' | column -t
```

For example:

```bash
maas admin nodes read \
| jq -r '(["hostname","system_id","tags"]
|(.,map(length*"-"))),(.[]|[.hostname,.system_id,.tag_names[]])
|@tsv' | column -t
```

Such a command would produce output that looks something like this:

```nohighlight
hostname                     system_id  tags
--------                     ---------  ----
better-sole                  t8pmrs     farquar
light-aphid                  76b6tt
divine-stork                 8b3ypp     pod-console-logging  virtual
casual-prawn                 4end6r     pod-console-logging  virtual
driven-teal                  tgaat6     pod-console-logging  virtual
immune-beetle                43xand     pod-console-logging  virtual
good-osprey                  napfxk     pod-console-logging  virtual
smart-hen                    c4rwq7     pod-console-logging  virtual
boss-satyr                   xn8taa     pod-console-logging  androko
golden-martin                8fxery     pod-console-logging  virtual
crack-guinea                 qk4b3g     pod-console-logging  virtual
finer-leech                  cy3dtr     pod-console-logging  virtual
free-mouse                   gxtbq4     pod-console-logging  virtual
humble-bunny                 srqnnb     pod-console-logging  virtual
wanted-muskox                ekw7fh     pod-console-logging  virtual
one-boa                      by477d     pod-console-logging  virtual
great-urchin                 srnx4g     pod-console-logging  virtual
ace-frog                     g6arwg     pod-console-logging  virtual  farquar
alive-marlin                 gbwnfb     pod-console-logging  virtual
picked-parrot                am77wn     pod-console-logging  virtual
tough-kit                    ke3wc7     pod-console-logging  virtual
legal-whale                  8nq3mt     pod-console-logging  virtual
game-sponge                  76pdc6     pod-console-logging  virtual
fun-ghoul                    qxfm7k     pod-console-logging  virtual
aware-earwig                 8m8hs7     pod-console-logging  virtual
chief-crane                  7fapx7     pod-console-logging  virtual
select-tapir                 4ascbr     pod-console-logging  virtual
on-slug                      snfs8d     pod-console-logging  virtual
polite-llama                 dbqd4m     pod-console-logging  virtual
frank-coyote                 wcmk48     pod-console-logging  virtual
usable-condor                ed8hmy     pod-console-logging  virtual
still-imp                    h6ra6d     pod-console-logging  virtual
bill-Lenovo-Yoga-C740-15IML  86xya8     lxd-vm-host
```

<a href="#heading--view-tags-for-one-node"><h4 id="heading--view-tags-for-one-node">View tags for one node</h4></a>

You could use a command with a form like this to view the tags for one node:

```bash
maas $PROFILE node read $SYSTEM_ID \
| jq -r '(["hostname","system_id","tags"]
|(.,map(length*"-"))),([.hostname,.system_id,.tag_names[]])
|@tsv' | column -t
```

For example:

```bash
maas admin node read xn8taa \
| jq -r '(["hostname","system_id","tags"]
|(.,map(length*"-"))),([.hostname,.system_id,.tag_names[]])
|@tsv' | column -t
```

This command produces output that looks something like this:

```nohighlight
hostname    system_id  tags
--------    ---------  ----
boss-satyr  xn8taa     pod-console-logging  androko
```

 snap-2-7-cli deb-2-7-cli snap-2-8-cli deb-2-8-cli snap-2-9-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli -->
<!-- snap-2-7-cli deb-2-7-cli snap-2-8-cli deb-2-8-cli snap-2-9-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli

<a href="#heading--work-with-annotations"><h2 id="heading--work-with-annotations">Work with annotations</h2></a>

This section will show you how to:

* [Work with static annotations](#heading--work-with-static-annotations)
* [Work with dynamic (workload) annotations](#heading--work-with-dynamic-workload-annotations)

<a href="#heading--work-with-static-annotations"><h3 id="heading--work-with-static-annotations">Work with static annotations</h3></a>

This subsection will show you how to:

* [Identify your machines](#heading--identify-your-machines)
* [Set a static annotation for a machine](#heading--set-a-static-annotation-for-a-machine)
* [Change or clear a static annotation for a machine](#heading--change-or-clear-a-static-annotation-for-a-machine)
* [List static annotations for all machines](#heading--list-static-annotations-for-all-machines)
* [View a static annotation for one machine](#heading--view-a-static-annotation-for-one-machine)


<a href="#heading--identify-your-machines"><h4 id="heading--identify-your-machines">Identify your machines</h4></a>

To identify your available machines, use a command like this one:

```bash
maas $PROFILE machines read \
| jq -r '(["hostname","system_id"]
|(.,map(length*"-"))),(.[]|[.hostname,.system_id])
|@tsv' | column -t
```

For example:

```bash
maas admin machines read \
| jq -r '(["hostname","system_id"]
|(.,map(length*"-"))),(.[]|[.hostname,.system_id])
|@tsv' | column -t
```

Typical output might look something like this:

```nohighlight
hostname       system_id
--------       ---------
divine-stork   8b3ypp
casual-prawn   4end6r
driven-teal    tgaat6
immune-beetle  43xand
good-osprey    napfxk
smart-hen      c4rwq7
boss-satyr     xn8taa
golden-martin  8fxery
crack-guinea   qk4b3g
finer-leech    cy3dtr
free-mouse     gxtbq4
humble-bunny   srqnnb
wanted-muskox  ekw7fh
one-boa        by477d
great-urchin   srnx4g
ace-frog       g6arwg
alive-marlin   gbwnfb
picked-parrot  am77wn
tough-kit      ke3wc7
legal-whale    8nq3mt
game-sponge    76pdc6
fun-ghoul      qxfm7k
aware-earwig   8m8hs7
chief-crane    7fapx7
select-tapir   4ascbr
on-slug        snfs8d
polite-llama   dbqd4m
frank-coyote   wcmk48
usable-condor  ed8hmy
still-imp      h6ra6d
```

<a href="#heading--set-a-static-annotation-for-a-machine"><h4 id="heading--set-a-static-annotation-for-a-machine">Set a static annotation for a machine</h4></a>

If you want to set the static annotation for a given machine, you can do so with a command that looks like this:

```bash
maas $PROFILE machine update $SYSTEM_ID description="$STATIC_ANNOTATION"
```

For example:

```bash
maas admin machine update ke3wc7 description="kilo-echo-3-whisky-charlie-7"
```

You can check your work by [viewing the static annotations for one machine](#heading--view-a-static-annotation-for-one-machine).

<a href="#heading--change-or-clear-a-static-annotation-for-a-machine"><h4 id="heading--change-or-clear-a-static-annotation-for-a-machine">Change or clear a static annotation for a machine</h4></a>

If you want to set the static annotation for a given machine, use the same command you'd use to set a static annotation:

```bash
maas $PROFILE machine update $SYSTEM_ID description="$STATIC_ANNOTATION"
```

The existing annotation will be overwritten by the new one you enter.  For example:

```bash
maas admin machine update ke3wc7 description=""
```

You can check your work by [viewing the static annotations for one machine](#heading--view-a-static-annotation-for-one-machine).


<a href="#heading--list-static-annotations-for-all-machines"><h4 id="heading--list-static-annotations-for-all-machines">List static annotations for all machines</h4></a>

To list static annotations for all machines, enter a command similar to this one:

```bash
maas $PROFILE machines read \
| jq -r '(["hostname","system_id","description"]
|(.,map(length*"-"))),(.[]|[.hostname,.system_id,.description])
|@tsv' | column -t
```

For example:

```bash
maas admin machines read \
| jq -r '(["hostname","system_id","description"]
|(.,map(length*"-"))),(.[]|[.hostname,.system_id,.description])
|@tsv' | column -t
```

Output might look something like this:

```nohighlight
hostname       system_id  description
--------       ---------  -----------
driven-teal    tgaat6     tango-golf
humble-bunny   srqnnb     sierra-romeo
tough-kit      ke3wc7     kilo-echo
```

<a href="#heading--view-a-static-annotation-for-one-machine"><h4 id="heading--view-a-static-annotation-for-one-machine">View a static annotation for one machine</h4></a>

To view a static annotation for one machine, try a command like this:

```bash
 maas $PROFILE machine read $SYSTEM_ID \
| jq -r '(["hostname","system_id","description"]
|(.,map(length*"-"))),([.hostname,.system_id,.description])
|@tsv' | column -t
```

For example:

```bash
 maas admin machine read tgaat6 \
| jq -r '(["hostname","system_id","description"]
|(.,map(length*"-"))),([.hostname,.system_id,.description])
|@tsv' | column -t
```

A command like this might produce output as follows:

```nohighlight
hostname     system_id  description
--------     ---------  -----------
driven-teal  tgaat6     tango-golf
```

<a href="#heading--work-with-dynamic-workload-annotations"><h3 id="heading--work-with-dynamic-workload-annotations">Work with dynamic (workload) annotations</h3></a>

This section will show you how to:

* [Identify machines that can receive dynamic annotations](#heading--identify-machines-that-can-receive-dynamic-annotations)
* [Set dynamic annotations for a machine](#heading--set-dynamic-annotations-for-a-machine)
* [Clear and change dynamic annotations for a machine](#heading--clear-and-change-dynamic-annotations-for-a-machine)
* [List dynamic annotations for all machines](#heading--list-dynamic-annotations-for-all-machines)
* [List dynamic allocations for one machine](#heading--list-dynamic-annotations-for-one-machine)

<a href="#heading--identify-machines-that-can-receive-dynamic-annotations"><h4 id="heading--identify-machines-that-can-receive-dynamic-annotations">Identify machines that can receive dynamic annotations</h4></a>

You can only set dynamic annotations for machines that are in the "Allocated" or "Deployed" state.  To identify which of your machines are in these states, you can execute the following command:

```bash
maas $PROFILE machines read \
| jq -r '(["hostname","system_id","status"]
|(.,map(length*"-"))),(.[]|[.hostname,.system_id,.status_name])
|@tsv' | column -t
```

For example:

```bash
maas admin machines read \
| jq -r '(["hostname","system_id","status"]
|(.,map(length*"-"))),(.[]|[.hostname,.system_id,.status_name])
|@tsv' | column -t
```

Output should look something like this:

```nohighlight
hostname       system_id  status
--------       ---------  ------
divine-stork   8b3ypp     Deployed
casual-prawn   4end6r     Ready
driven-teal    tgaat6     Allocated
immune-beetle  43xand     Allocated
good-osprey    napfxk     Allocated
smart-hen      c4rwq7     Allocated
boss-satyr     xn8taa     Ready
golden-martin  8fxery     Allocated
crack-guinea   qk4b3g     Allocated
finer-leech    cy3dtr     Deployed
free-mouse     gxtbq4     Allocated
humble-bunny   srqnnb     Allocated
wanted-muskox  ekw7fh     Deployed
one-boa        by477d     Allocated
great-urchin   srnx4g     Allocated
ace-frog       g6arwg     Ready
alive-marlin   gbwnfb     Deployed
picked-parrot  am77wn     Allocated
tough-kit      ke3wc7     Deployed
legal-whale    8nq3mt     Allocated
game-sponge    76pdc6     Allocated
fun-ghoul      qxfm7k     Allocated
aware-earwig   8m8hs7     Deployed
chief-crane    7fapx7     Ready
select-tapir   4ascbr     Allocated
on-slug        snfs8d     Allocated
polite-llama   dbqd4m     Allocated
frank-coyote   wcmk48     Allocated
usable-condor  ed8hmy     Deployed
still-imp      h6ra6d     Allocated
```

<a href="#heading--set-dynamic-annotations-for-a-machine"><h4 id="heading--set-dynamic-annotations-for-a-machine">Set dynamic annotations for a machine</h4></a>

Dynamic annotations, otherwise known as "workload annotations" or "owner data," can be used to keep track of the runtime status of machines that are acquired or deployed.  These annotations are set using `key=value` pairs.  You can set any `key=value` pair that you wish for any machine, although it's probably more useful if you standardise your key names.

To set a dynamic annotation for a machine, you can enter a command like this:

```bash
maas $PROFILE machine set-owner-data $SYSTEM_ID $KEY=$VALUE
```

For example:

```bash
maas admin machine set-owner-data tgaat6 owner=gsmith@zorko.com
```

This command will return a JSON string representative of the machine's new configuration, including the dynamic annotations you've added. You can check your work by [listing the dynamic annotations for the one machine](#heading--list-dynamic-annotations-for-one-machine) you just edited, or by [listing dynamic annotations for all machines](#heading--list-dynamic-annotations-for-all-machines).

<a href="#heading--clear-and-change-dynamic-annotations-for-a-machine"><h4 id="heading--clear-and-change-dynamic-annotations-for-a-machine">Clear and change dynamic annotations for a machine</h4></a>

You can change dynamic annotations for a machine simply by executing a new `set-owner-data` command:

```bash
maas $PROFILE machine set-owner-data $SYSTEM_ID $KEY=$NEW_VALUE
```

You can clear a dynamic annotation by entering the empty string (`""`) as the $VALUE:

```bash
maas $PROFILE machine set-owner-data $SYSTEM_ID $KEY=""
```

These commands will return a JSON string representative of the machine's new configuration, including the dynamic annotations you've changed or cleared. You can check your work by [listing the dynamic annotations for the one machine](#heading--list-dynamic-annotations-for-one-machine) you just edited, or by [listing dynamic annotations for all machines](#heading--list-dynamic-annotations-for-all-machines).

<a href="#heading--list-dynamic-annotations-for-all-machines"><h4 id="heading--list-dynamic-annotations-for-all-machines">List dynamic annotations for all machines</h4></a>

You can list the current dynamic annotations for all machines with a command like this:

```bash
maas $PROFILE machines read \
| jq -r '(["hostname","system_id","owner_data"]
|(.,map(length*"-"))),(.[]|[.hostname,.system_id,.owner_data[]])
|@tsv' | column -t
```

For example:

```bash
maas admin machines read \
| jq -r '(["hostname","system_id","owner_data"]
|(.,map(length*"-"))),(.[]|[.hostname,.system_id,.owner_data[]])
|@tsv' | column -t
```

This command output might look something like this:

```nohighlight
hostname       system_id  owner_data
--------       ---------  ----------
divine-stork   8b3ypp
casual-prawn   4end6r
driven-teal    tgaat6     farquar     foobar
immune-beetle  43xand
good-osprey    napfxk
smart-hen      c4rwq7
```

<a href="#heading--list-dynamic-annotations-for-one-machine"><h4 id="heading--list-dynamic-annotations-for-one-machine">List dynamic allocations for one machine</h4></a>

You can list the dynamic annotations for one machine by entering a command of the form:

```bash
maas $PROFILE machine read $SYSTEM_ID \
| jq -r '(["hostname","system_id","owner_data"]
|(.,map(length*"-"))),(.[]|[.hostname,.system_id,.owner_data[]])
|@tsv' | column -t
```

For example:

```bash
maas admin machine read tgaat6 \
| jq -r '(["hostname","system_id","owner_data"]
|(.,map(length*"-"))),(.[]|[.hostname,.system_id,.owner_data[]])
|@tsv' | column -t
```

This will produce output similar to the following:

```nohighlight
hostname     system_id  owner_data
--------     ---------  ----------
driven-teal  tgaat6     farquar     foobar
```
 snap-2-7-cli deb-2-7-cli snap-2-8-cli deb-2-8-cli snap-2-9-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli -->

