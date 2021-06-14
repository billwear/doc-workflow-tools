||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/resource-pools-snap-2-7-cli/3078) ~ [UI](/t/resource-pools-snap-2-7-ui/3079)|[CLI](/t/resource-pools-snap-2-8-cli/3080) ~ [UI](/t/resource-pools-snap-2-8-ui/3081)|[CLI](/t/resource-pools-snap-2-9-cli/3082) ~ [UI](/t/resource-pools-snap-2-9-ui/3083)|[CLI](/t/resource-pools-snap-3-0-cli/4097) ~ [UI](/t/resource-pools-snap-3-0-ui/4098)|
Packages|[CLI](/t/resource-pools-deb-2-7-cli/3084) ~ [UI](/t/resource-pools-deb-2-7-ui/3085)|[CLI](/t/resource-pools-deb-2-8-cli/3086) ~ [UI](/t/resource-pools-deb-2-8-ui/3087)|[CLI](/t/resource-pools-deb-2-9-cli/3088) ~ [UI](/t/resource-pools-deb-2-9-ui/3089)|[CLI](/t/resource-pools-deb-3-0-cli/4099) ~ [UI](/t/resource-pools-deb-3-0-ui/4100)|

Resource pools allow administrators to logically group resources -- machines and VM hosts -- into pools. Pools can help you budget machines for a particular set of functions.  For example, if you're using MAAS to manage a hospital data centre, you may want to keep a certain number of machines reserved for provider use, whether that be for the charts, documentation, or orders application.  You can use resource pools to reserve those machines, regardless of which of the three applications you end up loading onto a particular machine at any given time. 

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 

#### Seven questions you may have:

1. [How can I create a resource pool?](#heading--creating-a-resource-pool)
2. [How can I list available resource pools?](#heading--list-available-resource-pools)
3. [How can I list a single resource pool?](#heading--list-a-single-resource-pool)
4. [How can I update a resource pool?](#heading--update-a-resource-pool)
5. [How can I delete a resource pool?](#heading--delete-a-resource-pool)
6. [How can I add a machine to a resource pool?](#heading--add-a-machine-to-a-resource-pool)
7. [How can I get started with MAAS CLI?](/t/maas-cli/802)

<a href="#heading--creating-a-resource-pool"><h2 id="heading--creating-a-resource-pool">Creating a resource pool</h2></a>

Here's an example that demonstrates how to create a new resource pool named `myresource`.

``` bash
maas $PROFILE resource-pools create name=myresource description="A new resource pool."
```

[note]
The `description` field is optional.
[/note]

<a href="#heading--list-available-resource-pools"><h2 id="heading--list-available-resource-pools">List available resource pools</h2></a>

``` bash
maas $PROFILE resource-pools read
```

<a href="#heading--list-a-single-resource-pool"><h2 id="heading--list-a-single-resource-pool">List a single resource pool</h2></a>

``` bash
maas $PROFILE resource-pool read $RESOURCE_POOL_ID
```

<a href="#heading--update-a-resource-pool"><h2 id="heading--update-a-resource-pool">Update a resource pool</h2></a>

``` bash
maas $PROFILE resource-pool update $RESOURCE_POOL_ID name=newname description="A new description."
```

[note]
The `name` and `description` fields are optional.
[/note]

<a href="#heading--delete-a-resource-pool"><h2 id="heading--delete-a-resource-pool">Delete a resource pool</h2></a>

``` bash
maas $PROFILE resource-pool delete $RESOURCE_POOL_ID
```

<a href="#heading--add-a-machine-to-a-resource-pool"><h2 id="heading--add-a-machine-to-a-resource-pool">Add a machine to a resource pool</h2></a>

``` bash
maas $PROFILE machine update $SYSTEM_ID pool=$POOL_NAME
```

snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli  snap-3-0-cli deb-3-0-cli -->

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
#### Six questions you may have:

1. [How can I add a resource pool?](#heading--add-a-resource-pool)
2. [How can I delete a resource pool?](#heading--deleting-a-resource-pool)
3. [How do I add a node to a resource pool?](#heading--add-a-node-to-a-resource-pool)
4. [How do I remove a node from a resource pool?](#heading--removing-a-node-from-a-resource-pool)
5. [How do I add a VM host to a resource pool?](#heading--add-a-vm-host-to-a-resource-pool)
6. [How do I remove a VM host from a resource pool?](#heading--removing-a-vm-host-from-a-resource-pool)

Administrators can manage resource pools on the Machines page in the web UI, under the Resource pools tab.   Also note that all MAAS installations have a resource pool named "default." MAAS automatically adds new machines to the default resource pool.

<a href="#heading--add-a-resource-pool"><h2 id="heading--add-a-resource-pool">Add a resource pool</h2></a>

Use the Add pool button to add a new resource pool.

After giving your new pool a name and description, click the Add pool button:

<a href="https://assets.ubuntu.com/v1/2f010325-nodes-resource-pools__2.5_add-pool.png" target = "_blank"><img src="https://assets.ubuntu.com/v1/2f010325-nodes-resource-pools__2.5_add-pool.png"></a>

<a href="#heading--deleting-a-resource-pool"><h2 id="heading--deleting-a-resource-pool">Deleting a resource pool</h2></a>

To delete a resource pool, click the trashcan icon next to the pool.

<a href="https://assets.ubuntu.com/v1/630ed938-nodes-resource-pools__2.5_delete-pool.png" target = "_blank"><img src="https://assets.ubuntu.com/v1/630ed938-nodes-resource-pools__2.5_delete-pool.png"></a>

[note]
If you delete a resource pool, all machines that belong to that resource pool will return to the default pool.
[/note]

<a href="#heading--add-a-node-to-a-resource-pool"><h2 id="heading--add-a-node-to-a-resource-pool">Add a machine to a resource pool</h2></a>

To add a machine to a resource pool, on the Machines page, select the machine you want to add to the resource pool. Next, select the Configuration tab. Now select the resource pool and click the Save changes button.

<a href="https://assets.ubuntu.com/v1/648e7a8e-nodes-resource-pools__2.5_add-machine.png" target = "_blank"><img src="https://assets.ubuntu.com/v1/648e7a8e-nodes-resource-pools__2.5_add-machine.png"></a>

<a href="#heading--removing-a-node-from-a-resource-pool"><h2 id="heading--removing-a-node-from-a-resource-pool">Removing a machine from a resource pool</h2></a>

To remove a machine from a resource pool, follow the same procedure you would use to add a machine, but select "default" as the new resource pool. This action will return the machine to the default resource pool.

<a href="#heading--add-a-vm-host-to-a-resource-pool"><h2 id="heading--add-a-vm-host-to-a-resource-pool">Add a VM host to a resource pool</h2></a>

You can add a VM host to a resource pool when you create a new VM host, or you can edit a VM host's configuration:

<a href="https://assets.ubuntu.com/v1/84a89952-nodes-resource-pools__2.5_pod_to_pool.png" target = "_blank"><img src="https://assets.ubuntu.com/v1/84a89952-nodes-resource-pools__2.5_pod_to_pool.png"></a>

<a href="#heading--removing-a-vm-host-from-a-resource-pool"><h2 id="heading--removing-a-vm-host-from-a-resource-pool">Removing a VM host from a resource pool</h2></a>

To remove a VM host from a resource pool, follow the same procedure you would use to add a VM host to a resource pool, except select "default" as the new resource pool. This action will return the machine to the default resource pool.

snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui  snap-3-0-ui deb-3-0-ui -->
