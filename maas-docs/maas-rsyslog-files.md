||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/maas-rsyslog-files-snap-2-7-cli/3430) ~ [UI](/t/maas-rsyslog-files-snap-2-7-ui/3431)|[CLI](/t/maas-rsyslog-files-snap-2-8-cli/3432) ~ [UI](/t/maas-rsyslog-files-snap-2-8-ui/3433)|[CLI](/t/maas-rsyslog-files-snap-2-9-cli/3434) ~ [UI](/t/maas-rsyslog-files-snap-2-9-ui/3435)|[CLI](/t/maas-rsyslog-files-snap-3-0-cli/4017) ~ [UI](/t/maas-rsyslog-files-snap-3-0-ui/4018)|
Packages|[CLI](/t/maas-rsyslog-files-deb-2-7-cli/3436) ~ [UI](/t/maas-rsyslog-files-deb-2-7-ui/3437)|[CLI](/t/maas-rsyslog-files-deb-2-8-cli/3438) ~ [UI](/t/maas-rsyslog-files-deb-2-8-ui/3439)|[CLI](/t/maas-rsyslog-files-deb-2-9-cli/3441) ~ [UI](/t/maas-rsyslog-files-deb-2-9-ui/3440)|[CLI](/t/maas-rsyslog-files-deb-3-0-cli/4019) ~ [UI](/t/maas-rsyslog-files-deb-3-0-ui/4020)|

This is how a markdown file
handles a newline in the middle of a paragraph.

The MAAS rsyslog files allow you to monitor what's going on within individual MAAS machines. They are located at
<!-- snap-2-7-ui snap-2-7-cli snap-2-8-ui snap-2-8-cli snap-2-9-ui snap-2-9-cli snap-3-0-ui snap-3-0-cli
`/var/snap/maas/common/log/rsyslog/`. 
snap-2-7-ui snap-2-7-cli snap-2-8-ui snap-2-8-cli snap-2-9-ui snap-2-9-cli snap-3-0-ui snap-3-0-cli -->
<!-- deb-2-7-ui deb-2-7-cli deb-2-8-ui deb-2-8-cli deb-2-9-ui deb-2-9-cli deb-3-0-ui deb-3-0-cli
`/var/log/maas/rsyslog`. 
deb-2-7-ui deb-2-7-cli deb-2-8-ui deb-2-8-cli deb-2-9-ui deb-2-9-cli deb-3-0-ui deb-3-0-cli -->
Within this directory, there is one subdirectory for each machine, and within machine subirectories, there is one directory for each date upon which logging data was collected. These files will give you a great deal of the information you need to debug issues with your machines.

<a href="#heading--add-or-update-a-remote-syslog-server"><h2 id="heading--add-or-update-a-remote-syslog-server">Add or update a remote syslog server</h2></a>

To add or update a remote syslog server in your MAAS environment:

``` bash
maas $PROFILE maas set-config name="remote_syslog" value="$SYSLOG_FQDN"
```

For example, to set your syslog server to `192.168.100.11`:

``` bash
maas $PROFILE maas set-config name="remote_syslog" value=192.168.100.11
```

If you clear the `remote_syslog` value, MAAS will revert to the default behaviour, which is to send all syslog information to all MAAS region controllers.

For example:

``` bash
maas $PROFILE maas set-config name="remote_syslog" value=""
```


