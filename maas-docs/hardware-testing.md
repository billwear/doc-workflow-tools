||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/hardware-testing-snap-2-7-cli/2670) ~ [UI](/t/hardware-testing-snap-2-7-ui/2671)|[CLI](/t/hardware-testing-snap-2-8-cli/2672) ~ [UI](/t/hardware-testing-snap-2-8-ui/2673)|[CLI](/t/hardware-testing-snap-2-9-cli/2674) ~ [UI](/t/hardware-testing-snap-2-9-ui/2675)|[CLI](/t/hardware-testing-snap-3-0-cli/3941) ~ [UI](/t/hardware-testing-snap-3-0-ui/3942)|
Packages|[CLI](/t/hardware-testing-deb-2-7-cli/2676) ~ [UI](/t/hardware-testing-deb-2-7-ui/2677)|[CLI](/t/hardware-testing-deb-2-8-cli/2678) ~ [UI](/t/hardware-testing-deb-2-8-ui/2679)|[CLI](/t/hardware-testing-deb-2-9-cli/2680) ~ [UI](/t/hardware-testing-deb-2-9-ui/2681)|[CLI](/t/hardware-testing-deb-3-0-cli/3943) ~ [UI](/t/hardware-testing-deb-3-0-ui/3944)|

If you wish, you can tell MAAS to test machine hardware using well-known Linux utilities.  MAAS can test machines that have  a status of **Ready**, **Broken**, or **Deployed**.  You can include testing as part of the commissioning process. When you choose the 'Commission' action, MAAS will display the dialog described below.  Be aware, though, that if the hardware tests fail, the machine will become unavailable for Deployment.

[note]
The majority of testing scripts only work with machines that are backed by physical hardware (e.g. they may be incompatible with VM-based machines).
[/note]

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 
With MAAS, you can easily write, upload and execute your hardware testing scripts and see the results.

#### Three questions you may have:

1. [How do I upload hardware test scripts?](#heading--upload-test-scripts)
2. [How do I use tags to help with hardware test scripts?](#heading--tags)
3. [How do I view test results?](#heading--results)

<a href="#heading--upload-test-scripts"><h2 id="heading--upload-test-scripts">Uploading hardware test scripts</h2></a>

To upload a hardware testing script to MAAS, enter the following:

``` bash
maas $PROFILE node-scripts create name=$SCRIPT_NAME name> \
 script=$PATH_TO_SCRIPT type=testing
```

Changing the type to commissioning adds the test script to the commissioning process.

You can list all uploaded scripts with the following command:

``` bash
maas $PROFILE node-scripts read type=testing filters=$TAG
```

The optional filters argument lets you search for tags assigned to a script, such as using `TAG=cpu` with the above example.

A script's metadata, and even the script itself, can be updated from the command line:

``` bash
maas $PROFILE node-script update \
 $SCRIPT_NAME script=$PATH_TO_SCRIPT comment=$COMMENT
```

The JSON formatted output to the above command will include 'history' dictionary entries, detailing script modification times and associated comments:

``` json
"history": [
    {
        "id": 40,
        "created": "Tue, 12 Sep 2017 12:12:08 -0000",
        "comment": "Updated version"
    },
    {
        "id": 34,
        "created": "Fri, 08 Sep 2017 17:07:46 -0000",
        "comment": null
    }
]
```

MAAS keeps a history of all uploaded script versions, allowing you to easily revert to a previous version using the `id` of the version you wish to revert to:

``` bash
maas $PROFILE node-script revert $SCRIPT_NAME to=$VERSION_ID
```

[note type="negative" status="Warning"]
The history for later modifications will be lost when reverting to an earlier version of the script.
[/note]

To download a script, enter the following:

``` bash
maas $PROFILE node-script download $SCRIPT_NAME > $LOCAL_FILENAME
```

To delete a script, use `delete`:

``` bash
maas $PROFILE node-script delete $SCRIPT_NAME
```

<a href="#heading--tags"><h2 id="heading--tags">Tags</h2></a>

Tags make scripts easier to manage; grouping scripts together for commissioning and testing, for example:

``` bash
maas $PROFILE node-script add-tag $SCRIPT_NAME tag=$TAG
maas $PROFILE node-script remove-tag $SCRIPT_NAME tag=$TAG
```

MAAS runs all commissioning scripts by default. However, you can select which custom scripts to run during commissioning by name or tag:

``` bash
maas $PROFILE machine commission \
 commissioning_scripts=$SCRIPT_NAME,$SCRIPT_TAG
```

You can also select which testing scripts to run by name or tag:

``` bash
maas $PROFILE machine commission \
 testing_scripts=$SCRIPT_NAME,$SCRIPT_TAG
```

Any testing scripts tagged with commissioning will also run during commissioning.

<a href="#heading--results"><h2 id="heading--results">Results</h2></a>

The command line allows you to not only view the current script's progress but also retrieve the verbatim output from any previous runs too.

If you only want to see the latest or currently-running result, you can use `current-commissioning`, `current-testing`, or `current-installation` instead of an id:

``` bash
maas $PROFILE node-script-result read $SYSTEM_ID $RESULTS
```

You can also limit which results are returned by type (commissioning, testing, or installation), script name, or script run:

``` bash
maas $PROFILE node-script-results read \
 $SYSTEM_ID type=$SCRIPT_TYPE filters=$SCRIPT_NAME,$TAGS
```

You can also suppress failed results, which is useful if you want to ignore a known failure:

``` bash
maas $PROFILE node-script-results update \
 $SYSTEM_ID type=$SCRIPT_TYPE filters=$SCRIPT_NAME,$TAGS suppressed=$SUPPRESSED
```

where `$SUPPRESSED` is either `True` or `False`. The JSON formatted output to the above command will include 'results' dictionary with an entry for `suppressed`:

``` json
"results": [
    {
        "id": 21,
        "created": "Tue, 02 Apr 2019 17:00:36 -0000",
        "updated": "Tue, 02 Apr 2019 20:56:41 -0000",
        "name": "smartctl-validate",
        "status": 5,
        "status_name": "Aborted",
        "exit_status": null,
        "started": "Tue, 02 Apr 2019 20:56:41 -0000",
        "ended": "Tue, 02 Apr 2019 20:56:41 -0000",
        "runtime": "0:00:00",
        "starttime": 1554238601.765214,
        "endtime": 1554238601.765214,
        "estimated_runtime": "0:00:00",
        "parameters": {
            "storage": {
                "argument_format": "{path}",
                "type": "storage",
                "value": {
                    "id_path": "/dev/vda",
                    "model": "",
                    "name": "sda",
                    "physical_blockdevice_id": 1,
                    "serial": ""
                }
            }
        },
        "script_id": 1,
        "script_revision_id": null,
        "suppressed": true
    }
]
```

Finally, results can be downloaded, either to stdout, stderr, as combined output or as a tar.xz:

``` bash
maas $PROFILE node-script-result download $SYSTEM_ID $RUN_ID output=all \
 filetype=tar.xz > $LOCAL_FILENAME
```

[note]
**$RUN_ID** is labelled `id` in the verbose result output.
[/note]
snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli -->


<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
#### Two questions you may have: 

1. [How do I apply a hardware test?](#heading--apply-a-hardware-test)
2. [What scripts are available for testing?](#heading--included-scripts)

<a href="#heading--apply-a-hardware-test"><h2 id="heading--apply-a-hardware-test">Apply a hardware test</h2></a>

To launch a test, select the target machine from the 'Machines' page and use the 'Take action' drop-down menu to select 'Test hardware'. When ready, hit the 'Test machine' button. Here, a test is applied to a deployed machine:

<a href="https://assets.ubuntu.com/v1/8e876889-nodes-hw-testing__2.4_deployed.png" target = "_blank"><img src="https://assets.ubuntu.com/v1/8e876889-nodes-hw-testing__2.4_deployed.png"></a>

There is the option of not powering off the machine and to allow SSH access.

A default test will be selected (`smartctl-validate`, a hard drive test) but you can choose others by clicking the 'Select scripts' label. Doing so will reveal the following choices:

<a href="https://assets.ubuntu.com/v1/ccfefe25-nodes-hw-testing__2.4_deployed-choices.png" target = "_blank"><img src="https://assets.ubuntu.com/v1/ccfefe25-nodes-hw-testing__2.4_deployed-choices.png"></a>

<a href="#heading--included-scripts"><h2 id="heading--included-scripts">Scripts available for testing</h2></a>

The following hardware testing scripts can be selected from the web UI:

<table style="width:100%;">
<thead>
<tr class="header">
<th align="center">Name</th>
<th align="center">Category Tags</th>
<th align="center">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="center"><strong>smartctl-short</strong></td>
<td align="center">storage</td>
<td align="center">Run the short SMART self-test and validate SMART health on all drives in parallel</td>
</tr>
<tr class="even">
<td align="center"><strong>smartctl-long</strong></td>
<td align="center">storage</td>
<td align="center">Run the long SMART self-test and validate SMART health on all drives in parallel</td>
</tr>
<tr class="odd">
<td align="center"><strong>smartctl-conveyance</strong></td>
<td align="center">storage</td>
<td align="center">Run the conveyance SMART self-test and validate SMART health on all drives in parallel</td>
</tr>
<tr class="even">
<td align="center"><strong>memtester</strong></td>
<td align="center">memory</td>
<td align="center">Run memtester against all available userspace memory.</td>
</tr>
<tr class="odd">
<td align="center"><strong>internet-connectivity</strong></td>
<td align="center">network, internet, node</td>
<td align="center">Check if the system has access to the internet.</td>
</tr>
<tr class="even">
<td align="center"><strong>stress-ng-cpu-long</strong></td>
<td align="center">cpu</td>
<td align="center">Run stress-ng memory tests for 12 hours.</td>
</tr>
<tr class="odd">
<td align="center"><strong>stress-ng-cpu-short</strong></td>
<td align="center">cpu</td>
<td align="center">Run stress-ng memory tests for 5 minutes.</td>
</tr>
<tr class="even">
<td align="center"><strong>stress-ng-memory-long</strong></td>
<td align="center">memory</td>
<td align="center">Run stress-ng memory tests for 12 hours.</td>
</tr>
<tr class="odd">
<td align="center"><strong>stress-ng-memory-short</strong></td>
<td align="center">memory</td>
<td align="center">Run stress-ng memory tests for 5 minutes.</td>
</tr>
<tr class="even">
<td align="center"><strong>ntp</strong></td>
<td align="center">network, ntp, node</td>
<td align="center">Run ntp clock set to verify NTP connectivity.</td>
</tr>
<tr class="odd">
<td align="center"><strong>badblocks</strong></td>
<td align="center">storage</td>
<td align="center">Run badblocks on disk in read-only mode.</td>
</tr>
<tr class="even">
<td align="center"><strong>badblocks-destructive</strong></td>
<td align="center">destructive, storage</td>
<td align="center">Run badblocks on a disk in read/write destructive mode.</td>
</tr>
<tr class="odd">
<td align="center"><strong>7z</strong></td>
<td align="center">cpu</td>
<td align="center">Run <em>7zip</em> CPU benchmarking.</td>
</tr>
<tr class="even">
<td align="center"><strong>fio</strong></td>
<td align="center">storage, destructive</td>
<td align="center">Run Fio benchmarking against selected storage devices.</td>
</tr>
</tbody>
</table>

After either commissioning, testing, or installation has started, MAAS reports in real-time which script is running.

You can access the verbatim output from any test by selecting a machine, selecting the 'Hardware tests' page and clicking on the 'Log view' link in the 'Results' column for the specific test.
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui -->

<!-- deb-2-7-cli
See [Commissioning and Hardware Testing Scripts](/t/commissioning-and-hardware-testing-scripts/2484) for more details on how these scripts work and how you can write your own.
 deb-2-7-cli -->

<!-- deb-2-7-ui
See [Commissioning and Hardware Testing Scripts](/t/commissioning-and-hardware-testing-scripts/2485) for more details on how these scripts work and how you can write your own.
 deb-2-7-ui -->

<!-- deb-2-8-cli
See [Commissioning and Hardware Testing Scripts](/t/commissioning-and-hardware-testing-scripts/2486) for more details on how these scripts work and how you can write your own.
 deb-2-8-cli -->

<!-- deb-2-8-ui
See [Commissioning and Hardware Testing Scripts](/t/commissioning-and-hardware-testing-scripts/2487) for more details on how these scripts work and how you can write your own.
 deb-2-8-ui -->

<!-- deb-2-9-cli
See [Commissioning and Hardware Testing Scripts](/t/commissioning-and-hardware-testing-scripts/2488) for more details on how these scripts work and how you can write your own.
 deb-2-9-cli -->

<!-- deb-2-9-ui
See [Commissioning and Hardware Testing Scripts](/t/commissioning-and-hardware-testing-scripts/2489) for more details on how these scripts work and how you can write your own.
 deb-2-9-ui -->

<!-- deb-3-0-cli
See [Commissioning and Hardware Testing Scripts](/t/commissioning-and-hardware-testing-scripts/3867) for more details on how these scripts work and how you can write your own.
 deb-3-0-cli -->

<!-- deb-3-0-ui
See [Commissioning and Hardware Testing Scripts](/t/commissioning-and-hardware-testing-scripts/3868) for more details on how these scripts work and how you can write your own.
 deb-3-0-ui -->

<!-- snap-2-7-cli
See [Commissioning and Hardware Testing Scripts](/t/commissioning-and-hardware-testing-scripts/2478) for more details on how these scripts work and how you can write your own.
 snap-2-7-cli -->

<!-- snap-2-7-ui
See [Commissioning and Hardware Testing Scripts](/t/commissioning-and-hardware-testing-scripts/2479) for more details on how these scripts work and how you can write your own.
 snap-2-7-ui -->

<!-- snap-2-8-cli
See [Commissioning and Hardware Testing Scripts](/t/commissioning-and-hardware-testing-scripts/2480) for more details on how these scripts work and how you can write your own.
 snap-2-8-cli -->

<!-- snap-2-8-ui
See [Commissioning and Hardware Testing Scripts](/t/commissioning-and-hardware-testing-scripts/2481) for more details on how these scripts work and how you can write your own.
 snap-2-8-ui -->

<!-- snap-2-9-cli
See [Commissioning and Hardware Testing Scripts](/t/commissioning-and-hardware-testing-scripts/2482) for more details on how these scripts work and how you can write your own.
 snap-2-9-cli -->

<!-- snap-2-9-ui
See [Commissioning and Hardware Testing Scripts](/t/commissioning-and-hardware-testing-scripts/2483) for more details on how these scripts work and how you can write your own.
 snap-2-9-ui -->

<!-- snap-3-0-cli
See [Commissioning and Hardware Testing Scripts](/t/commissioning-and-hardware-testing-scripts/3865) for more details on how these scripts work and how you can write your own.
 snap-3-0-cli -->

<!-- snap-3-0-ui
See [Commissioning and Hardware Testing Scripts](/t/commissioning-and-hardware-testing-scripts/3866) for more details on how these scripts work and how you can write your own.
 snap-3-0-ui -->
