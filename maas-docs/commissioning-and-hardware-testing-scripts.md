||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/commissioning-and-hardware-testing-scripts-snap-2-7-cli/2478) ~ [UI](/t/commissioning-and-hardware-testing-scripts-snap-2-7-ui/2479)|[CLI](/t/commissioning-and-hardware-testing-scripts-snap-2-8-cli/2480) ~ [UI](/t/commissioning-and-hardware-testing-scripts-snap-2-8-ui/2481)|[CLI](/t/commissioning-and-hardware-testing-scripts-snap-2-9-cli/2482) ~ [UI](/t/commissioning-and-hardware-testing-scripts-snap-2-9-ui/2483)|[CLI](/t/commissioning-and-hardware-testing-scripts-snap-3-0-cli/3865) ~ [UI](/t/commissioning-and-hardware-testing-scripts-snap-3-0-ui/3866)|
Packages|[CLI](/t/commissioning-and-hardware-testing-scripts-deb-2-7-cli/2484) ~ [UI](/t/commissioning-and-hardware-testing-scripts-deb-2-7-ui/2485)|[CLI](/t/commissioning-and-hardware-testing-scripts-deb-2-8-cli/2486) ~ [UI](/t/commissioning-and-hardware-testing-scripts-deb-2-8-ui/2487)|[CLI](/t/commissioning-and-hardware-testing-scripts-deb-2-9-cli/2488) ~ [UI](/t/commissioning-and-hardware-testing-scripts-deb-2-9-ui/2489)|[CLI](/t/commissioning-and-hardware-testing-scripts-deb-3-0-cli/3867) ~ [UI](/t/commissioning-and-hardware-testing-scripts-deb-3-0-ui/3868)|

MAAS runs scripts during enlistment, commissioning and testing to collect data about nodes. Both enlistment and commissioning run all builtin commissioning scripts, though enlistment runs only built-ins. Commissioning also runs any user-uploaded commissioning scripts by default, unless the user manually provides a list of scripts to run. MAAS uses these commissioning scripts to configure hardware and perform other tasks during commissioning, such as updating the firmware. Similarly, MAAS employs hardware testing scripts to evaluate system hardware and report its status. 

<h4>Quick questions you may have:</h4>

1. [What metadata fields exist, and how do they control the scripts?](#heading--metadata-fields)
2. [What parameters can I use to control the scripts?](#heading--parameters)
3. [ What environment variables are available to me?](#heading--environment-variables)
4. [How can I control the results output from the scripts?](#heading--results)
5. [What would some example scripts look like?](#heading--script-examples)
6. [How do I upload scripts to MAAS?](#heading--upload-procedure)

---

<!-- deb-2-7-cli
Scripts can be selected to run from web UI [during commissioning](/t/commission-machines/2472), by [testing hardware](/t/hardware-testing/2676) or from the command line. Note that MAAS only runs built-in commissioning scripts during enlistment. Custom scripts can be run when you explicitly choose to commission a machine.  A typical administrator workflow (with machine states), using customised commissioning scripts, can be represented as:
 deb-2-7-cli -->

<!-- deb-2-7-ui
Scripts can be selected to run from web UI [during commissioning](/t/commission-machines/2473), by [testing hardware](/t/hardware-testing/2677) or from the command line (select the "CLI" option from the top menu). Note that MAAS only runs built-in commissioning scripts during enlistment. Custom scripts can be run when you explicitly choose to commission a machine.  A typical administrator workflow (with machine states), using customised commissioning scripts, can be represented as:
 deb-2-7-ui -->

<!-- deb-2-8-cli
Scripts can be selected to run from web UI [during commissioning](/t/commission-machines/2474), by [testing hardware](/t/hardware-testing/2678) or from the command line. Note that MAAS only runs built-in commissioning scripts during enlistment. Custom scripts can be run when you explicitly choose to commission a machine.  A typical administrator workflow (with machine states), using customised commissioning scripts, can be represented as:
 deb-2-8-cli -->

<!-- deb-2-8-ui
Scripts can be selected to run from web UI [during commissioning](/t/commission-machines/2475), by [testing hardware](/t/hardware-testing/2679) or from the command line (select the "CLI" option from the top menu). Note that MAAS only runs built-in commissioning scripts during enlistment. Custom scripts can be run when you explicitly choose to commission a machine.  A typical administrator workflow (with machine states), using customised commissioning scripts, can be represented as:
 deb-2-8-ui -->

<!-- deb-2-9-cli
Scripts can be selected to run from web UI [during commissioning](/t/commission-machines/2476), by [testing hardware](/t/hardware-testing/2680) or from the command line. Note that MAAS only runs built-in commissioning scripts during enlistment. Custom scripts can be run when you explicitly choose to commission a machine.  A typical administrator workflow (with machine states), using customised commissioning scripts, can be represented as:
 deb-2-9-cli -->

<!-- deb-2-9-ui
Scripts can be selected to run from web UI [during commissioning](/t/commission-machines/2677), by [testing hardware](/t/hardware-testing/2681) or from the command line (select the "CLI" option from the top menu). Note that MAAS only runs built-in commissioning scripts during enlistment. Custom scripts can be run when you explicitly choose to commission a machine.  A typical administrator workflow (with machine states), using customised commissioning scripts, can be represented as:
 deb-2-9-ui -->

<!-- deb-3-0-cli
Scripts can be selected to run from web UI [during commissioning](/t/commission-machines/3875), by [testing hardware](/t/hardware-testing/3943) or from the command line. Note that MAAS only runs built-in commissioning scripts during enlistment. Custom scripts can be run when you explicitly choose to commission a machine.  A typical administrator workflow (with machine states), using customised commissioning scripts, can be represented as:
 deb-3-0-cli -->

<!-- deb-3-0-ui
Scripts can be selected to run from web UI [during commissioning](/t/commission-machines/3876), by [testing hardware](/t/hardware-testing/3944) or from the command line (select the "CLI" option from the top menu). Note that MAAS only runs built-in commissioning scripts during enlistment. Custom scripts can be run when you explicitly choose to commission a machine.  A typical administrator workflow (with machine states), using customised commissioning scripts, can be represented as:
 deb-3-0-ui -->

<!-- snap-2-7-cli
Scripts can be selected to run from web UI [during commissioning](/t/commission-machines/2466), by [testing hardware](/t/hardware-testing/2670) or from the command line. Note that MAAS only runs built-in commissioning scripts during enlistment. Custom scripts can be run when you explicitly choose to commission a machine.  A typical administrator workflow (with machine states), using customised commissioning scripts, can be represented as:
 snap-2-7-cli -->

<!-- snap-2-7-ui
Scripts can be selected to run from web UI [during commissioning](/t/commission-machines/2467), by [testing hardware](/t/hardware-testing/2671) or from the command line (select the "CLI" option from the top menu).  Note that MAAS only runs built-in commissioning scripts during enlistment. Custom scripts can be run when you explicitly choose to commission a machine.  A typical administrator workflow (with machine states), using customised commissioning scripts, can be represented as:
 snap-2-7-ui -->

<!-- snap-2-8-cli
Scripts can be selected to run from web UI [during commissioning](/t/commission-machines/2468), by [testing hardware](/t/hardware-testing/2672) or from the command line. Note that MAAS only runs built-in commissioning scripts during enlistment. Custom scripts can be run when you explicitly choose to commission a machine.  A typical administrator workflow (with machine states), using customised commissioning scripts, can be represented as:
 snap-2-8-cli -->

<!-- snap-2-8-ui
Scripts can be selected to run from web UI [during commissioning](/t/commission-machines/2469), by [testing hardware](/t/hardware-testing/2673) or from the command line (select the "CLI" option from the top menu). Note that MAAS only runs built-in commissioning scripts during enlistment. Custom scripts can be run when you explicitly choose to commission a machine.  A typical administrator workflow (with machine states), using customised commissioning scripts, can be represented as:
 snap-2-8-ui -->

<!-- snap-2-9-cli
Scripts can be selected to run from web UI [during commissioning](/t/commission-machines/2470), by [testing hardware](/t/hardware-testing/2674) or from the command line. Note that MAAS only runs built-in commissioning scripts during enlistment. Custom scripts can be run when you explicitly choose to commission a machine.  A typical administrator workflow (with machine states), using customised commissioning scripts, can be represented as:
 snap-2-9-cli -->

<!-- snap-2-9-ui
Scripts can be selected to run from web UI [during commissioning](/t/commission-machines/2471), by [testing hardware](/t/hardware-testing/2675) or from the command line (select the "CLI" option from the top menu). Note that MAAS only runs built-in commissioning scripts during enlistment. Custom scripts can be run when you explicitly choose to commission a machine.  A typical administrator workflow (with machine states), using customised commissioning scripts, can be represented as:
 snap-2-9-ui -->

<!-- snap-3-0-cli
Scripts can be selected to run from web UI [during commissioning](/t/commission-machines/3873), by [testing hardware](/t/hardware-testing/3941) or from the command line. Note that MAAS only runs built-in commissioning scripts during enlistment. Custom scripts can be run when you explicitly choose to commission a machine.  A typical administrator workflow (with machine states), using customised commissioning scripts, can be represented as:
 snap-3-0-cli -->

<!-- snap-3-0-ui
Scripts can be selected to run from web UI [during commissioning](/t/commission-machines/3874), by [testing hardware](/t/hardware-testing/3942) or from the command line (select the "CLI" option from the top menu). Note that MAAS only runs built-in commissioning scripts during enlistment. Custom scripts can be run when you explicitly choose to commission a machine.  A typical administrator workflow (with machine states), using customised commissioning scripts, can be represented as:
 snap-3-0ui -->

Add machine -&gt; Enlistment (runs built-in commissioning scripts MAAS) -&gt; New -&gt; Commission (runs built-in and custom commissioning scripts) -&gt; Ready -&gt; Deploy

NOTE: Scripts are run in alphabetical order in an ephemeral environment.  We recommend running your scripts after any MAAS built-in scripts.  This can be done by naming your scripts 99-z*.  It is possible to reboot the system during commissioning using a script, however, as the environment is ephemeral, any changes to the environment will be destroyed upon reboot (barring, of course, firmware type updates).

This article explains script metadata, parameter passing, and results-reporting.  It also offers examples of both commissioning and hardware testing scripts.

<a href="#heading--metadata-fields"><h2 id="heading--metadata-fields">Metadata fields</h2></a>

Metadata fields tell MAAS when to use the script, how it should run, and what information it's gathering. A script can employ some combination of the following seventeen fields:

| Field | Description |
|:------|:------------|
| `name`| The name of the script.|
| `title`| Human-friendly descriptive version of the name, used within the web UI.|
| `description`| Brief outline of what the script does.|
| `tags`| List of tags associated with the script.|
| `type`| Either commissioning or testing.|
| `timeout`| Length of time before MAAS automatically fails and kills execution of the script. The time may be specified in seconds or using the HH:MM:SS format. |
| `destructive`| True or False, depending on whether the script will overwrite system data. You can't run destructive tests on a deployed machine. |
| `comment`| Describes changes made in this revision of the script.  A comment can be passed via the API when uploading the script.  MAAS doesn’t look at the script metadata for this field. |
| `hardware_type`| Defines the type of hardware the script configures or tests. If the script returns results, hardware types associate the results with specific hardware. The following types are valid: |
| | `node`: Not associated with any hardware type; this is the default. |
| | `cpu`: Configures or tests the CPUs on the machine. |
| | `memory`: Configures or tests memory on the machine. |
| | `storage`: Configures or tests storage on the machine. |
| | `network`: Configures or tests network on the machine. |
|   `parallel`| Enables scripts to be run in parallel and can be one of the following: |
| | `disabled`: The script will run serially on its own. |
| | `instance`: Runs in parallel only with other instances of the same script. |
| | `any`: Runs in parallel alongside any other scripts with parallel set to any. |
| `parameters`| What [parameters](#heading--parameters) the script accepts. |
| `results`| What [results](#heading--results) the script will return. |
| `packages`| List of packages to be installed or extracted before running the script. Packages must be specified as a dictionary. For example, `packages: {apt: stress-ng}`, would ask `apt` to install stress-ng. Package sources can be any of the following: |
| | `apt`: Use the Ubuntu apt repositories as configured by MAAS to install a package. |
| | `snap`: Installs packages using [snap][snapcraft]. May also be a list of dictionaries. The dictionary must define the name of the  package to be installed, and optionally, the `channel`, `mode` and `revision`.|
| | `url`: The archive will be downloaded and, if possible, extracted or installed when a Debian package or [snap][snapcraft]. |
|   `for_hardware`| Specifies the hardware that must be on the machine for the script to run. May be a single string or list of strings of the following:
| | `modalias`: Starts with 'modalias:' may optionally contain wild cards. |
| | `PCI ID`: Must be in the format of 'pci:VVVV:PPPP' where VVVV is the vendor ID, and PPPP is the product ID. |
| | `USB ID`: Must be in the format of 'usb:VVVV:PPPP' where VVVV is the vendor ID, and PPPP is the product ID. |
| | `System Vendor`: Starts with 'system_vendor:'. |
| | `System Product`: Starts with 'system_product:'. |
| | `System Version`: Starts with 'system_version:'. |
| | `Mainboard Vendor`: Starts with 'mainboard_vendor:'. |
| | `Mainboard Product`: Starts with 'mainboard_product:'. |
|   `may_reboot` |When True, indicates to MAAS that the script may reboot the machine. MAAS will allow up to 20 minutes between heartbeats while running a script with `may_reboot` set to True. |
| `recommission`| After all commissioning scripts have finished running rerun |
|   `script_type` | commissioning or test. Indicates whether the script should run during commissioning or hardware testing. |

<a href="#heading--parameters"><h2 id="heading--parameters">Parameters</h2></a>

Scripts can accept exactly three types of parameters, and only three types:

1. storage.
2. interface.
3. URL.

The values of these parameters are strictly checked against existing disks (storage), working interfaces (interface), and valid URLs (URL)  No other types of information can be passed as parameters; they are not configured to pass user-specified data.

Parameters are automatically switched by MAAS to match the device being tested, to allow one test to be run against multiple devices at the same time while keeping separate logs.  For this reason, you may only specify parameters within the embedded YAML of the script, and they must take the form of a dictionary of dictionaries.

The key of the dictionary must be a string, and it's this string that's used by the UI and API when users are setting parameter values during commissioning or testing.  The value is a dictionary with the following five fields:

| Field | Description |
|:------|:------------|
|   `type`: Every parameter must contain a type field, which describes what the parameter may accept and its default values. It may be one of the following: |
| |   `storage`: Allows the selection of a storage device on the currently running machine.|
| |   `interface`: Allows the selection of an interface on the currently running machine.|
| |   `url`: Allows the the passing of a valid URL.|
| |   `runtime`: Specifies how long the script may run. This overrides the timeout value. It is currently only passed as the environment variable RUNTIME.|
|   `title`: The title of the parameter field when displayed in the UI. The following types have the following default values:|
| |   `storage`: storage device.|
| |   `interface`: interface specifier.|
| |   `url`: valid URL.|
|   `argument-format`: Specifies how the argument should be passed to the script. Input is described as `{input}`. The storage type may also use `{name}`, `{path}`, `{model}` or `{serial}`. MAAS will look up the values of path, model, and serial based on user selection. For storage, `{input}` is synonymous with `{path}`. The interface type may also use `{name}`, `{mac_address}`, `{product}`, or `{vendor}`. For interface `{input}` is synonymous with `{name}`. The following types have the following default values:|
| |   `storage`: `--storage={path}`|
| |   `interface`: `--interface={name}`|
| |   `url`: `--url={input}`|
|   `default`: The default value of the parameter. The following types have the following default values. Setting these to '' or None will override these values:|
| |   `storage`: all.|
| |   `interface`: all.|
|   `required`: Whether or not user input is required. A value of false sets no default, and no user input will mean no parameters passed to the script. Defaults to `true`.|
|   `results`: What results the script will return on completion. You can only define this parameter within the embedded YAML of the script. Results may be a list of strings or a dictionary of dictionaries.|

Example script using default values:

``` python
#!/usr/bin/env python3

# --- Start MAAS 1.0 script metadata ---
# name: example
# parallel: instance
# parameters:
#   storage: {type: storage}
# --- End MAAS 1.0 script metadata ---

import argparse

parser = argparse.ArgumentParser(description='')
parser.add_argument(
    '--storage', dest='storage', required=True,
    help='path to storage device you want to test. e.g. /dev/sda')
args = parser.parse_args()

print("Testing: %s" % args.storage)
```

Example script using customised parameters:

``` bash
#!/bin/bash

# --- Start MAAS 1.0 script metadata ---
# name: example
# parallel: instance
# parameters:
#   storage:
#     type: storage
#     argument-format: '{model}' '{serial}'
# --- End MAAS 1.0 script metadata ---

echo "Model: $1"
echo "Serial: $2"
```

<a href="#heading--environment-variables"><h2 id="heading--environment-variables">Environment variables</h2></a>

The following seven environment variables are available when a script runs within the MAAS environment:

1.   `OUTPUT_STDOUT_PATH`: The path to the log of STDOUT from the script.
2.   `OUTPUT_STDERR_PATH`: The path to the log of STDERR from the script.
3.   `OUTPUT_COMBINED_PATH`: The path to the log of the combined STDOUT and STDERR from the script.
4.   `RESULT_PATH`: Path for the script to write a result YAML.
5.   `DOWNLOAD_PATH`: The path where MAAS will download all files.
6.   `RUNTIME`: The amount of time the script has to run in seconds.
7.   `HAS_STARTED`: When 'True', MAAS has run the script once before but not to completion. Indicates the machine has rebooted.

<a href="#heading--results"><h2 id="heading--results">Results</h2></a>

A script can output its results to a YAML file, and those results will be associated with the hardware type defined within the script. MAAS provides the path for the results file in an environment variable, `RESULT_PATH`. Scripts should write YAML to this file before exiting.

If the hardware type is storage, for example, and the script accepts a storage type parameter, the result will be associated with a specific storage device.

The YAML file must represent a dictionary with these two fields:

1.   `result`: The completion status of the script. This status can be `passed`, `failed`, `degraded`, or `skipped`. If no status is defined, an exit code of `0` indicates a pass while a non-zero value indicates a failure.
2.   `results`: A dictionary of results. The key may map to a results key defined as embedded YAML within the script. The value of each result must be a string or a list of strings.

Optionally, a script may define what results to return in the YAML file in the [Metadata fields](#Metadata%20fields). The `results` field should contain a dictionary of dictionaries. The key for each dictionary is a name which is returned by the results YAML. Each dictionary may contain the following two fields:

1.   `title` - The title for the result, used in the UI.
2.   `description` - The description of the field used as a tool-tip in the UI.

Example degrade detection:

``` python
#!/usr/bin/env python3

# --- Start MAAS 1.0 script metadata ---
# name: example
# results:
#   memspeed:
#     title: Memory Speed
#     description: Bandwidth speed of memory while performing random read writes
# --- End MAAS 1.0 script metadata ---

import os
import yaml

memspeed = some_test()

print('Memspeed: %s' % memspeed)
results = {
    'results': {
        'memspeed': memspeed,
    }
}
if memspeed < 100:
    print('WARN: Memory test passed but performance is low!')
    results['status'] = 'degraded'

result_path = os.environ.get("RESULT_PATH")
if result_path is not None:
    with open(result_path, 'w') as results_file:
        yaml.safe_dump(results, results_file)
```

<a href="#heading--script-examples"><h2 id="heading--script-examples">Script examples</h2></a>

<a href="#heading--built-in-scripts"><h3 id="heading--built-in-scripts">Built-in scripts</h3></a>

You can download the source for all commissioning and test scripts via the API with the following command:

``` bash
maas $PROFILE node-script download $SCRIPT_NAME
```

The source code to all built-in scripts is available on [launchpad](https://git.launchpad.net/maas/tree/src/metadataserver/builtin_scripts).

<a href="#heading--commissioning-script-configure-hpa"><h3 id="heading--commissioning-script-configure-hpa">Commissioning script: Configure HPA</h3></a>

Below is a sample script to configure an Intel C610/X99 HPA controller on an HP system. The script will only run on systems with an Intel C610/X99 controller identified by the PCI ID 8086:8d06.

Before the scrixpt runs, MAAS will download and install the [HP RESTful Interface Tool](https://downloads.linux.hpe.com/SDR/project/hprest/) package from HP. After the script completes, the built-in commissioning scripts will be re-run to capture the new configuration.

``` bash
#!/bin/bash -ex
# --- Start MAAS 1.0 script metadata ---
# name: hp_c610_x99_ahci
# title: Configure Intel C610/X99 controller on HP systems
# description: Configure Intel C610/X99 controller on HP systems to AHCI
# script_type: commissioning
# tags: configure_hpa
# packages:
#  url: http://downloads.linux.hpe.com/SDR/repo/hprest/pool/non-free/hprest-1.5-26_amd64.deb
# for_hardware: pci:8086:8d06
# recommission: True
# --- End MAAS 1.0 script metadata ---
output=$(sudo hprest get EmbeddedSata --selector HpBios.)
echo $output
if [ $(echo $output | grep -c 'EmbeddedSata=Raid') ]; then
    echo "Server is in Dynamic Smart Array RAID mode. Changing to SATA AHCI support mode."
    sudo hprest set EmbeddedSata=Ahci --selector HpBios. --commit
else:
    echo "No changes made to the system, Server is Already in AHCI Mode"
fi
```

<a href="#heading--commissioning-script-update-firmware"><h3 id="heading--commissioning-script-update-firmware">Commissioning script: Update firmware</h3></a>

Below is a sample script to update the mainboard firmware on an ASUS P8P67 Pro using a vendor-provided tool. The tool will is automatically downloaded and extracted by MAAS. The script reboots the system to complete the update. The system will boot back into the MAAS ephemeral environment to finish commissioning and optionally testing.

[note]
Vendor tools which use UEFI boot capsules or need to store resource files on disk while rebooting are not currently supported.
[/note]

``` bash
#!/bin/bash -ex
# --- Start MAAS 1.0 script metadata ---
# name: update_asus_p8p67_firmware
# title: Firmware update for the ASUS P8P67 mainboard
# description: Firmware update for the ASUS P8P67 mainboard
# script_type: commissioning
# tags: update_firmware
# packages:
#  url: http://example.com/firmware.tar.gz
# for_hardware: mainboard_product:P8P67 PRO
# may_reboot: True
# --- End MAAS 1.0 script metadata ---
$DOWNLOAD_PATH/update_firmware
reboot
```

<a href="#heading--hardware-test-script-cpu-stress-test"><h3 id="heading--hardware-test-script-cpu-stress-test">Hardware test script: CPU stress test</h3></a>

As a simple example, here's a functional Bash script replicating part of the stress-ng script bundled with MAAS:

``` bash
#!/bin/bash -e
# --- Start MAAS 1.0 script metadata ---
# name: stress-ng-cpu-test
# title: CPU validation
# description: Run stress-ng memory tests for 5 minutes.
# script_type: test
# hardware_type: cpu
# packages: {apt: stress-ng}
# tags: cpu
# timeout: 00:05:00
# --- End MAAS 1.0 script metadata ---

sudo -n stress-ng --matrix 0 --ignite-cpu --log-brief --metrics-brief --times \
    --tz --verify --timeout 2m
```

This Bash script contains comment-delineated metadata, which configures the script environment and installs any dependencies.  There is also a single line that runs **stress-ng** (a CPU stress-test utility) with various arguments.

<a href="#heading--automatic-script-selection-by-hardware-type"><h3 id="heading--automatic-script-selection-by-hardware-type">Automatic script selection by hardware type</h3></a>

<!-- deb-2-7-cli
When selecting [multiple machines](/t/machines/2736), scripts which declare the `for_hardware` field will only run on machines with matching hardware. To automatically run a script when 'Update firmware' or 'Configure HBA' is selected, you must tag the script with 'update_firmware' or 'configure_hba'.
 deb-2-7-cli -->

<!-- deb-2-7-ui
When selecting [multiple machines](/t/machines/2737), scripts which declare the `for_hardware` field will only run on machines with matching hardware. To automatically run a script when 'Update firmware' or 'Configure HBA' is selected, you must tag the script with 'update_firmware' or 'configure_hba'.
 deb-2-7-ui -->

<!-- deb-2-8-cli
When selecting [multiple machines](/t/machines/2738), scripts which declare the `for_hardware` field will only run on machines with matching hardware. To automatically run a script when 'Update firmware' or 'Configure HBA' is selected, you must tag the script with 'update_firmware' or 'configure_hba'.
 deb-2-8-cli -->

<!-- deb-2-8-ui
When selecting [multiple machines](/t/machines/2739), scripts which declare the `for_hardware` field will only run on machines with matching hardware. To automatically run a script when 'Update firmware' or 'Configure HBA' is selected, you must tag the script with 'update_firmware' or 'configure_hba'.
 deb-2-8-ui -->

<!-- deb-2-9-cli
When selecting [multiple machines](/t/machines/2740), scripts which declare the `for_hardware` field will only run on machines with matching hardware. To automatically run a script when 'Update firmware' or 'Configure HBA' is selected, you must tag the script with 'update_firmware' or 'configure_hba'.
 deb-2-9-cli -->

<!-- deb-2-9-ui
When selecting [multiple machines](/t/machines/2741), scripts which declare the `for_hardware` field will only run on machines with matching hardware. To automatically run a script when 'Update firmware' or 'Configure HBA' is selected, you must tag the script with 'update_firmware' or 'configure_hba'.
 deb-2-9-ui -->

<!-- deb-3-0-cli
When selecting [multiple machines](/t/machines/4031), scripts which declare the `for_hardware` field will only run on machines with matching hardware. To automatically run a script when 'Update firmware' or 'Configure HBA' is selected, you must tag the script with 'update_firmware' or 'configure_hba'.
 deb-3-0-cli -->

<!-- deb-3-0-ui
When selecting [multiple machines](/t/machines/4032), scripts which declare the `for_hardware` field will only run on machines with matching hardware. To automatically run a script when 'Update firmware' or 'Configure HBA' is selected, you must tag the script with 'update_firmware' or 'configure_hba'.
 deb-3-0-ui -->

<!-- snap-2-7-cli
When selecting [multiple machines](/t/machines/2730), scripts which declare the `for_hardware` field will only run on machines with matching hardware. To automatically run a script when 'Update firmware' or 'Configure HBA' is selected, you must tag the script with 'update_firmware' or 'configure_hba'.
 snap-2-7-cli -->

<!-- snap-2-7-ui
When selecting [multiple machines](/t/machines/2731), scripts which declare the `for_hardware` field will only run on machines with matching hardware. To automatically run a script when 'Update firmware' or 'Configure HBA' is selected, you must tag the script with 'update_firmware' or 'configure_hba'.
 snap-2-7-ui -->

<!-- snap-2-8-cli
When selecting [multiple machines](/t/machines/2732), scripts which declare the `for_hardware` field will only run on machines with matching hardware. To automatically run a script when 'Update firmware' or 'Configure HBA' is selected, you must tag the script with 'update_firmware' or 'configure_hba'.
 snap-2-8-cli -->

<!-- snap-2-8-ui
When selecting [multiple machines](/t/machines/2733), scripts which declare the `for_hardware` field will only run on machines with matching hardware. To automatically run a script when 'Update firmware' or 'Configure HBA' is selected, you must tag the script with 'update_firmware' or 'configure_hba'.
 snap-2-8-ui -->

<!-- snap-2-9-cli
When selecting [multiple machines](/t/machines/2734), scripts which declare the `for_hardware` field will only run on machines with matching hardware. To automatically run a script when 'Update firmware' or 'Configure HBA' is selected, you must tag the script with 'update_firmware' or 'configure_hba'.
 snap-2-9-cli -->

<!-- snap-2-9-ui
When selecting [multiple machines](/t/machines/2735), scripts which declare the `for_hardware` field will only run on machines with matching hardware. To automatically run a script when 'Update firmware' or 'Configure HBA' is selected, you must tag the script with 'update_firmware' or 'configure_hba'.
 snap-2-9-ui -->

<!-- snap-3-0-cli
When selecting [multiple machines](/t/machines/4029), scripts which declare the `for_hardware` field will only run on machines with matching hardware. To automatically run a script when 'Update firmware' or 'Configure HBA' is selected, you must tag the script with 'update_firmware' or 'configure_hba'.
 snap-3-0-cli -->

<!-- snap-3-0-ui
When selecting [multiple machines](/t/machines/4030), scripts which declare the `for_hardware` field will only run on machines with matching hardware. To automatically run a script when 'Update firmware' or 'Configure HBA' is selected, you must tag the script with 'update_firmware' or 'configure_hba'.
 snap-3-0-ui -->

Similarly, scripts selected by tag on the command line which specify the `for_hardware` field will only run on matching hardware.

<a href="#heading--upload-procedure"><h2 id="heading--upload-procedure">Upload procedure</h2></a>

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 
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

A [script's metadata](#hardware-test-script-sample), and even the script itself, can be updated from the command line:

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

<!-- deb-2-7-cli
As with general [tag management](/t/maas-tags/2892), tags make scripts easier to manage; grouping scripts together for commissioning and testing, for example:
 deb-2-7-cli -->

<!-- deb-2-7-ui
As with general [tag management](/t/maas-tags/2893), tags make scripts easier to manage; grouping scripts together for commissioning and testing, for example:
 deb-2-7-ui -->

<!-- deb-2-8-cli
As with general [tag management](/t/maas-tags/2894), tags make scripts easier to manage; grouping scripts together for commissioning and testing, for example:
 deb-2-8-cli -->

<!-- deb-2-8-ui
As with general [tag management](/t/maas-tags/2895), tags make scripts easier to manage; grouping scripts together for commissioning and testing, for example:
 deb-2-8-ui -->

<!-- deb-2-9-cli
As with general [tag management](/t/maas-tags/2896), tags make scripts easier to manage; grouping scripts together for commissioning and testing, for example:
 deb-2-9-cli -->

<!-- deb-2-9-ui
As with general [tag management](/t/maas-tags/2897), tags make scripts easier to manage; grouping scripts together for commissioning and testing, for example:
 deb-2-9-ui -->

<!-- deb-3-0-cli
As with general [tag management](/t/maas-tags/4023), tags make scripts easier to manage; grouping scripts together for commissioning and testing, for example:
 deb-3-0-cli -->

<!-- deb-3-0-ui
As with general [tag management](/t/maas-tags/4024), tags make scripts easier to manage; grouping scripts together for commissioning and testing, for example:
 deb-3-0-ui -->
 
<!-- snap-2-7-cli
As with general [tag management](/t/maas-tags/2886), tags make scripts easier to manage; grouping scripts together for commissioning and testing, for example:
 snap-2-7-cli -->

<!-- snap-2-7-ui
As with general [tag management](/t/maas-tags/2887), tags make scripts easier to manage; grouping scripts together for commissioning and testing, for example:
 snap-2-7-ui -->

<!-- snap-2-8-cli
As with general [tag management](/t/maas-tags/2888), tags make scripts easier to manage; grouping scripts together for commissioning and testing, for example:
 snap-2-8-cli -->

<!-- snap-2-8-ui
As with general [tag management](/t/maas-tags/2889), tags make scripts easier to manage; grouping scripts together for commissioning and testing, for example:
 snap-2-8-ui -->

<!-- snap-2-9-cli
As with general [tag management](/t/maas-tags/2890), tags make scripts easier to manage; grouping scripts together for commissioning and testing, for example:
 snap-2-9-cli -->

<!-- snap-2-9-ui
As with general [tag management](/t/maas-tags/2891), tags make scripts easier to manage; grouping scripts together for commissioning and testing, for example:
 snap-2-9-ui -->

<!-- snap-3-0-cli
As with general [tag management](/t/maas-tags/4021), tags make scripts easier to manage; grouping scripts together for commissioning and testing, for example:
 snap-3-0-cli -->

<!-- snap-3-0-ui
As with general [tag management](/t/maas-tags/4022), tags make scripts easier to manage; grouping scripts together for commissioning and testing, for example:
 snap-3-0-ui -->

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

snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli  snap-3-0-cli deb-3-0-cli -->

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
Scripts can be uploaded to MAAS using the web UI. Select the 'User scripts' tab of the 'Settings' page - the 'Commissioning scripts' section is near the top. Within the Commissioning scripts section, click the Upload script button followed by 'Choose file' to open a requester, locate the script, and select Upload to upload it to MAAS.
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui  snap-3-0-ui deb-3-0-ui -->

<!-- deb-2-7-ui
A status message of Commissioning script created will appear.  You'll then be able to select your script after selecting [Test hardware](/t/hardware-testing/2677) from a machine's 'Take action' menu.
 deb-2-7-ui -->

<!-- deb-2-8-ui
A status message of Commissioning script created will appear.  You'll then be able to select your script after selecting [Test hardware](/t/hardware-testing/2679) from a machine's 'Take action' menu.
 deb-2-8-ui -->

<!-- deb-2-9-ui
A status message of Commissioning script created will appear.  You'll then be able to select your script after selecting [Test hardware](/t/hardware-testing/2681) from a machine's 'Take action' menu.
 deb-2-9-ui -->

<!-- deb-3-0-ui
A status message of Commissioning script created will appear.  You'll then be able to select your script after selecting [Test hardware](/t/hardware-testing/3944) from a machine's 'Take action' menu.
 deb-3-0-ui -->

<!-- snap-2-7-ui
A status message of Commissioning script created will appear.  You'll then be able to select your script after selecting [Test hardware](/t/hardware-testing/2671) from a machine's 'Take action' menu.
 snap-2-7-ui -->

<!-- snap-2-8-ui
A status message of Commissioning script created will appear.  You'll then be able to select your script after selecting [Test hardware](/t/hardware-testing/2673) from a machine's 'Take action' menu.
 snap-2-8-ui -->

<!-- snap-2-9-ui
A status message of Commissioning script created will appear.  You'll then be able to select your script after selecting [Test hardware](/t/hardware-testing/2675) from a machine's 'Take action' menu.
 snap-2-9-ui -->

<!-- snap-3-0-ui
A status message of Commissioning script created will appear.  You'll then be able to select your script after selecting [Test hardware](/t/hardware-testing/3942) from a machine's 'Take action' menu.
 snap-3-0-ui -->

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
<a href="https://assets.ubuntu.com/v1/50e08fdf-nodes-hw-scripts__2.4_select.png" target = "_blank"><img src="https://assets.ubuntu.com/v1/50e08fdf-nodes-hw-scripts__2.4_select.png"></a>

[note]
MAAS executes scripts in lexicographical order. This order allows you to control when your scripts execute, and whether they run before or after the standard MAAS scripts.
[/note]

<a href="#heading--debugging"><h2 id="heading--debugging">Debugging</h2></a>

Clicking on the title of a completed or failed script will reveal the output from that specific script.

<a href="https://assets.ubuntu.com/v1/855015e5-nodes-hw-scripts__2.2_fail.png" target = "_blank"><img src="https://assets.ubuntu.com/v1/855015e5-nodes-hw-scripts__2.2_fail.png"></a>

If you need further details, especially when writing and running your own scripts, you can connect to a machine and examine its logs and environment.

To do this, enable Allow SSH access and prevent the machine from powering off when selecting 'Test hardware' from the machine 'Take action' menu.

<a href="https://assets.ubuntu.com/v1/da793c67-nodes-hw-scripts__2.4_ssh.png" target = "_blank"><img src="https://assets.ubuntu.com/v1/da793c67-nodes-hw-scripts__2.4_ssh.png"></a>

Because scripts operate within an ephemeral version of Ubuntu, enabling this option stops the machine from shutting down, allowing you to connect and probe a script's status.
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui  snap-3-0-ui deb-3-0-ui -->

<!-- deb-2-7-cli
As long as you've added your [SSH key](/t/user-accounts/3204#heading--ssh-keys) to MAAS, you can connect with SSH to the machine's IP with a username of `ubuntu`. Type `sudo -i` to get root access.
 deb-2-7-cli -->

<!-- deb-2-7-ui
As long as you've added your [SSH key](/t/user-accounts/3205#heading--ssh-keys) to MAAS, you can connect with SSH to the machine's IP with a username of `ubuntu`. Type `sudo -i` to get root access.
 deb-2-7-ui -->

<!-- deb-2-8-cli
As long as you've added your [SSH key](/t/user-accounts/3206#heading--ssh-keys) to MAAS, you can connect with SSH to the machine's IP with a username of `ubuntu`. Type `sudo -i` to get root access.
 deb-2-8-cli -->

<!-- deb-2-8-ui
As long as you've added your [SSH key](/t/user-accounts/3207#heading--ssh-keys) to MAAS, you can connect with SSH to the machine's IP with a username of `ubuntu`. Type `sudo -i` to get root access.
 deb-2-8-ui -->

<!-- deb-2-9-cli
As long as you've added your [SSH key](/t/user-accounts/3208#heading--ssh-keys) to MAAS, you can connect with SSH to the machine's IP with a username of `ubuntu`. Type `sudo -i` to get root access.
 deb-2-9-cli -->

<!-- deb-2-9-ui
As long as you've added your [SSH key](/t/user-accounts/3209#heading--ssh-keys) to MAAS, you can connect with SSH to the machine's IP with a username of `ubuntu`. Type `sudo -i` to get root access.
 deb-2-9-ui -->

<!-- deb-3-0-cli
As long as you've added your [SSH key](/t/user-accounts/4147#heading--ssh-keys) to MAAS, you can connect with SSH to the machine's IP with a username of `ubuntu`. Type `sudo -i` to get root access.
 deb-3-0-cli -->

<!-- deb-3-0-ui
As long as you've added your [SSH key](/t/user-accounts/4148#heading--ssh-keys) to MAAS, you can connect with SSH to the machine's IP with a username of `ubuntu`. Type `sudo -i` to get root access.
 deb-3-0-ui -->

<!-- snap-2-7-cli
As long as you've added your [SSH key](/t/user-accounts/3198#heading--ssh-keys) to MAAS, you can connect with SSH to the machine's IP with a username of `ubuntu`. Type `sudo -i` to get root access.
 snap-2-7-cli -->

<!-- snap-2-7-ui
As long as you've added your [SSH key](/t/user-accounts/3199#heading--ssh-keys) to MAAS, you can connect with SSH to the machine's IP with a username of `ubuntu`. Type `sudo -i` to get root access.
 snap-2-7-ui -->

<!-- snap-2-8-cli
As long as you've added your [SSH key](/t/user-accounts/3200#heading--ssh-keys) to MAAS, you can connect with SSH to the machine's IP with a username of `ubuntu`. Type `sudo -i` to get root access.
 snap-2-8-cli -->

<!-- snap-2-8-ui
As long as you've added your [SSH key](/t/user-accounts/3201#heading--ssh-keys) to MAAS, you can connect with SSH to the machine's IP with a username of `ubuntu`. Type `sudo -i` to get root access.
 snap-2-8-ui -->

<!-- snap-2-9-cli
As long as you've added your [SSH key](/t/user-accounts/3202#heading--ssh-keys) to MAAS, you can connect with SSH to the machine's IP with a username of `ubuntu`. Type `sudo -i` to get root access.
 snap-2-9-cli -->

<!-- snap-2-9-ui
As long as you've added your [SSH key](/t/user-accounts/3203#heading--ssh-keys) to MAAS, you can connect with SSH to the machine's IP with a username of `ubuntu`. Type `sudo -i` to get root access.
 snap-2-9-ui -->

<!-- snap-3-0-cli
As long as you've added your [SSH key](/t/user-accounts/4145#heading--ssh-keys) to MAAS, you can connect with SSH to the machine's IP with a username of `ubuntu`. Type `sudo -i` to get root access.
 snap-3-0-cli -->

<!-- snap-3-0-ui
As long as you've added your [SSH key](/t/user-accounts/4146#heading--ssh-keys) to MAAS, you can connect with SSH to the machine's IP with a username of `ubuntu`. Type `sudo -i` to get root access.
 snap-3-0-ui -->

<a href="#heading--access-individual-scripts-and-log-files"><h3 id="heading--access-individual-scripts-and-log-files">Access individual scripts and log files</h3></a>

<a href="#heading--commissioning-and-testing-script-files"><h4 id="heading--commissioning-and-testing-script-files">Commissioning and testing script files</h4></a>

1.   `/tmp/user_data.sh.*/scripts/commissioning/`: Commissioning scripts
2.   `/tmp/user_data.sh.*/scripts/testing/`: Hardware testing scripts

<a href="#heading--log-files"><h4 id="heading--log-files">Log files</h4></a>

1.   `/tmp/user_data.sh*/out/`
2.   `/var/log/cloud-init-output.log`
3.   `/var/log/cloud-init.log`

<a href="#heading--run-all-scripts-manually"><h3 id="heading--run-all-scripts-manually">Run all scripts manually</h3></a>

You can also run all commissioning and hardware-testing scripts on a machine for debugging.

``` bash
/tmp/user_data.sh.*/bin/maas-run-remote-scripts \
    [--no-download] \
    [--no-send] \
    /tmp/user_data.sh.*
```

Where:

1.   `--no-download`: Optional. Do not download the scripts from MAAS again.
2.   `--no-send`: Optional. Do not send the results to MAAS.

For example, to run all the scripts again without downloading again from MAAS:

``` bash
/tmp/user_data.sh.*/bin/maas-run-remote-scripts --no-download /tmp/user_data.sh.*
```

Here, all the scripts are run again after downloading from MAAS, but no output data is sent to MAAS:

``` bash
/tmp/user_data.sh.*/bin/maas-run-remote-scripts --no-send /tmp/user_data.sh.*
```
