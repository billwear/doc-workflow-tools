<a href="#heading--create-machine-tags"><h4 id="heading--create-machine-tags">tags create</h4></a>

Command format:

```bash
maas $PROFILE tags create name=$NAME
```

Optional parameters:

* `comment`: a description of the tag in natural language free text; presumably a string that identifies how the tag will be used.

* `definition`: an `XPATH` query that will be evaluated against the `hardware_details` stored for all nodes, that is, the output of ```lshw -xml```; formatted as a string. Review the [explanation of XPATH bindings with tags](/t/discourse/maas-project/4460#heading--tags-and-xpath-entries) for more details about this parameter.

* ```kernel_opts```: all nodes associated with this tag will add this string to their kernel options when booting.  This value overrides the global ```kernel_opts``` setting.  If more than one associated tag has attached kernel options, all the applied options will be concatenated for the machine, in alphabetical order.  Review the [explanation of per-machine kernel boot options](/t/discourse/maas-project/4460#heading--tags-and-kernel-boot-options), or see the section on [per-machine kernel boot options](#heading--assign-per-machine-kernel-boot-options) for more detailed instructions about using this parameter.

<a href="#heading--tags-and-kernel-parameters"><h4 id="heading--tags-and-kernel-parameters">Machine tags and kernel parameters</h4></a>

Per-machine boot options take precedence to global ones. Please also note that, even though a deployed machine has a `kernel_opt` tag applied, MAAS won't apply the `kernel_opt` associated with that tag until the next deployment.  This means that a machine that has been deployed for a long time can (possibly) inherit kernel options that were applied in the distant past.

If multiple tags attached to a machine have the `kernel_opts` defined, MAAS uses the first one found, in alphabetical order.

<a href="#heading--tag-update-nodes"><h4 id="heading--tag-update-nodes">tags update-nodes</h4></a>

The various key-value pairs are somewhat optional, although at least one `add=$SYSTEM_ID` or `remove=$SYSTEM_ID` follow the `$TAG_NAME` in this command.  The possible key-value pairs are as follows:

* `add=$SYSTEM_ID`: this pair causes MAAS to add $TAG_NAME to the machine $SYSTEM_ID.  You can use as many of these key-value pairs as needed, so it's possible to tag many machines at once with a single command-line invocation.

* `remove=$SYSTEM_ID`: this pair causes MAAS to remove $TAG_NAME from the machine $SYSTEM_ID.  You can use as many of these key-value pairs as needed, so it's possible to remove tags from many machines at once with a single command-line invocation.

[note]
Note that both "add" and "remove" key-value pairs can be combined in a single command-line invocation, so it's possible to add and remove tags from various machines, at the same time, in a single command.
[/note]

* `definition=$XPATH_EXPRESSION`: If given, the entered XPATH expression will be validated against the current definition of the tag.  If the value does not match, MAAS assumes the worker is out of date and will not do the update.

* 'rack_controller=$SYSTEM_ID`: If given, the system ID of the rack controller that processed the given tag initially is used, requiring that the requester be the rack controller.  If not given, the requester must be a MAAS admin.

For example, to assign a *existing* tag named "new-tag" to a machine with system ID "xmprry," the following command would be executed:

```
maas admin tag update-nodes new-tag add=xmprry
```

A successful result should look like this:

```
Success.
Machine-readable output follows:
{
    "added": 1,
    "removed": 0
}
```

If you try to assign a tag that hasn't been created yet, you'll get a "Not Found" error message.  For example:

```
maas admin tag update-nodes revolution add=dtanap
Not Found
```
