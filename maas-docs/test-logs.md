||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/test-logs-snap-2-7-cli/3126) ~ [UI](/t/test-logs-snap-2-7-ui/3127)|[CLI](/t/test-logs-snap-2-8-cli/3128) ~ [UI](/t/test-logs-snap-2-8-ui/3129)|[CLI](/t/test-logs-snap-2-9-cli/3130) ~ [UI](/t/test-logs-snap-2-9-ui/3131)|[CLI](/t/test-logs-snap-3-0-cli/4117) ~ [UI](/t/test-logs-snap-3-0-ui/4118)|
Packages|[CLI](/t/test-logs-deb-2-7-cli/3132) ~ [UI](/t/test-logs-deb-2-7-ui/3133)|[CLI](/t/test-logs-deb-2-8-cli/3134) ~ [UI](/t/test-logs-deb-2-8-ui/3135)|[CLI](/t/test-logs-deb-2-9-cli/3136) ~ [UI](/t/test-logs-deb-2-9-ui/3137)|[CLI](/t/test-logs-deb-3-0-cli/4119) ~ [UI](/t/test-logs-deb-3-0-ui/4120)|

For any machine which has undergone testing, the Tests log screen -- under the "Tests" tab -- shows a list of tests that have been run for that machine, along with a timestamp and result.  You can view the detailed logs for each test script from this tab.

By default, every MAAS machine is tested with the `smartctl-validate` script, which is a script prepared by Canonical using the [smartmontools](https://www.smartmontools.org) kit.  This is a disk integrity test.  Typical output includes the following:

```
INFO: Verifying SMART support for the following drive: /dev/sda
INFO: Running command: sudo -n smartctl --all /dev/sda
INFO: SMART support is available; continuing...
INFO: Verifying SMART data on /dev/sda
INFO: Running command: sudo -n smartctl --xall /dev/sda
SUCCESS: SMART validation has PASSED for: /dev/sda
--------------------------------------------------------------------------------
smartctl 6.6 2016-05-31 r4324 [x86_64-linux-4.15.0-115-generic] (local build)
Copyright (C) 2002-16, Bruce Allen, Christian Franke, www.smartmontools.org

=== START OF INFORMATION SECTION ===
Device Model:     QEMU HARDDISK
Serial Number:    QM00001
Firmware Version: 2.5+
User Capacity:    5,368,709,120 bytes [5.36 GB]
Sector Size:      512 bytes logical/physical
Device is:        Not in smartctl database [for details use: -P showall]
ATA Version is:   ATA/ATAPI-7, ATA/ATAPI-5 published, ANSI NCITS 340-2000
Local Time is:    Wed Sep  2 22:29:12 2020 UTC
SMART support is: Available - device has SMART capability.
SMART support is: Enabled
AAM feature is:   Unavailable
APM feature is:   Unavailable
Rd look-ahead is: Unavailable
Write cache is:   Enabled
ATA Security is:  Unavailable
Wt Cache Reorder: Unavailable

=== START OF READ SMART DATA SECTION ===
SMART overall-health self-assessment test result: PASSED

General SMART Values:
Offline data collection status:  (0x82)	Offline data collection activity
					was completed without error.
					Auto Offline Data Collection: Enabled.
Self-test execution status:      (   0)	The previous self-test routine completed
					without error or no self-test has ever 
					been run.
Total time to complete Offline 
data collection: 		(  288) seconds.
Offline data collection
capabilities: 			 (0x19) SMART execute Offline immediate.
					No Auto Offline data collection support.
					Suspend Offline collection upon new
					command.
					Offline surface scan supported.
					Self-test supported.
					No Conveyance Self-test supported.
					No Selective Self-test supported.
SMART capabilities:            (0x0003)	Saves SMART data before entering
					power-saving mode.
					Supports SMART auto save timer.
Error logging capability:        (0x01)	Error logging supported.
					No General Purpose Logging support.
Short self-test routine 
recommended polling time: 	 (   2) minutes.
Extended self-test routine
recommended polling time: 	 (  54) minutes.

SMART Attributes Data Structure revision number: 1
Vendor Specific SMART Attributes with Thresholds:
ID# ATTRIBUTE_NAME          FLAGS    VALUE WORST THRESH FAIL RAW_VALUE
  1 Raw_Read_Error_Rate     PO----   100   100   006    -    0
  3 Spin_Up_Time            PO----   100   100   000    -    16
  4 Start_Stop_Count        -O----   100   100   020    -    100
  5 Reallocated_Sector_Ct   PO----   100   100   036    -    0
  9 Power_On_Hours          PO----   100   100   000    -    1
 12 Power_Cycle_Count       PO----   100   100   000    -    0
190 Airflow_Temperature_Cel PO----   069   069   050    -    31 (Min/Max 31/31)
                            ||||||_ K auto-keep
                            |||||__ C event count
                            ||||___ R error rate
                            |||____ S speed/performance
                            ||_____ O updated online
                            |______ P prefailure warning

Read SMART Log Directory failed: scsi error badly formed scsi parameters

General Purpose Log Directory not supported

SMART Extended Comprehensive Error Log (GP Log 0x03) not supported

SMART Error Log Version: 1
No Errors Logged

SMART Extended Self-test Log (GP Log 0x07) not supported

SMART Self-test log structure revision number 1
No self-tests have been logged.  [To run self-tests, use: smartctl -t]

Selective Self-tests/Logging not supported

SCT Commands not supported

Device Statistics (GP/SMART Log 0x04) not supported

SATA Phy Event Counters (GP Log 0x11) not supported
```
