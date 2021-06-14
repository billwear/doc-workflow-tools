||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/maas-logging-snap-2-7-cli/2862) ~ [UI](/t/maas-logging-snap-2-7-ui/2863)|[CLI](/t/maas-logging-snap-2-8-cli/2864) ~ [UI](/t/maas-logging-snap-2-8-ui/2865)|[CLI](/t/maas-logging-snap-2-9-cli/2866) ~ [UI](/t/maas-logging-snap-2-9-ui/2867)|[CLI](/t/maas-logging-snap-3-0-cli/4009) ~ [UI](/t/maas-logging-snap-3-0-ui/4010)|
Packages|[CLI](/t/maas-logging-deb-2-7-cli/2868) ~ [UI](/t/maas-logging-deb-2-7-ui/2869)|[CLI](/t/maas-logging-deb-2-8-cli/2870) ~ [UI](/t/maas-logging-deb-2-8-ui/2871)|[CLI](/t/maas-logging-deb-2-9-cli/2872) ~ [UI](/t/maas-logging-deb-2-9-ui/2873)|[CLI](/t/maas-logging-deb-3-0-cli/4011) ~ [UI](/t/maas-logging-deb-3-0-ui/4012)|

MAAS has a robust logging capability, which presents several different views, including a number of node-specific log files and several syslogd-style text logs.  Each of these logs provides different information, or at the very least, different views of the same information.  MAAS gathers logging information about the various MAAS states and records both automated and user-driven actions.

#### Five questions you may have:

<!-- deb-2-7-cli
1. [What is the syslog logging path?](#heading--path)
2. [How do I use a remote syslog server?](#heading--using-a-remote-syslog-server)
3. [What are commissioning logs?](/t/commissioning-logs/2496)
4. [What are test logs?](/t/test-logs/3132)
5. [What are event logs?](/t/event-logs/3388)
6. [What are audit event logs?](t/audit-event-logs/2316)
deb-2-7-cli -->

<!-- deb-2-7-ui
1. [What is the syslog logging path?](#heading--path)
2. [How do I use a remote syslog server?](#heading--using-a-remote-syslog-server)
3. [What are commissioning logs?](/t/commissioning-logs/2497)
4. [What are test logs?](/t/test-logs/3133)
5. [What are event logs?](/t/event-logs/3389)
6. [What are audit event logs?](t/audit-event-logs/2317)
 deb-2-7-ui -->

<!-- deb-2-8-cli
1. [What is the syslog logging path?](#heading--path)
2. [How do I use a remote syslog server?](#heading--using-a-remote-syslog-server)
3. [What are commissioning logs?](/t/commissioning-logs/2498)
4. [What are test logs?](/t/test-logs/3134)
5. [What are event logs?](/t/event-logs/3390)
6. [What are audit event logs?](t/audit-event-logs/2318)
 deb-2-8-cli -->

<!-- deb-2-8-ui
1. [What is the syslog logging path?](#heading--path)
2. [How do I use a remote syslog server?](#heading--using-a-remote-syslog-server)
3. [What are commissioning logs?](/t/commissioning-logs/2499)
4. [What are test logs?](/t/test-logs/3135)
5. [What are event logs?](/t/event-logs/3391)
6. [What are audit event logs?](t/audit-event-logs/2319)
 deb-2-8-ui -->

<!-- deb-2-9-cli
1. [What is the syslog logging path?](#heading--path)
2. [How do I use a remote syslog server?](#heading--using-a-remote-syslog-server)
3. [What are commissioning logs?](/t/commissioning-logs/2500)
4. [What are test logs?](/t/test-logs/3136)
5. [What are event logs?](/t/event-logs/3393)
6. [What are audit event logs?](t/audit-event-logs/2320)
 deb-2-9-cli -->

<!-- deb-2-9-ui
1. [What is the syslog logging path?](#heading--path)
2. [How do I use a remote syslog server?](#heading--using-a-remote-syslog-server)
3. [What are commissioning logs?](/t/commissioning-logs/2501)
4. [What are test logs?](/t/test-logs/3137)
5. [What are event logs?](/t/event-logs/3392)
6. [What are audit event logs?](t/audit-event-logs/2321)
 deb-2-9-ui -->

<!-- deb-3-0-cli
1. [What is the syslog logging path?](#heading--path)
2. [How do I use a remote syslog server?](#heading--using-a-remote-syslog-server)
3. [What are commissioning logs?](/t/commissioning-logs/3871)
4. [What are test logs?](/t/test-logs/4119)
5. [What are event logs?](/t/event-logs/3927)
6. [What are audit event logs?](t/audit-event-logs/3831)
 deb-3-0-cli -->

<!-- deb-3-0-ui
1. [What is the syslog logging path?](#heading--path)
2. [How do I use a remote syslog server?](#heading--using-a-remote-syslog-server)
3. [What are commissioning logs?](/t/commissioning-logs/3872)
4. [What are test logs?](/t/test-logs/4120)
5. [What are event logs?](/t/event-logs/3928)
6. [What are audit event logs?](t/audit-event-logs/3832)
 deb-3-0-ui -->

<!-- snap-2-7-cli
1. [What is the syslog logging path?](#heading--path)
2. [How do I use a remote syslog server?](#heading--using-a-remote-syslog-server)
3. [What are commissioning logs?](/t/commissioning-logs/2490)
4. [What are test logs?](/t/test-logs/3126)
5. [What are event logs?](/t/event-logs/3382)
6. [What are audit event logs?](t/audit-event-logs/2310)
 snap-2-7-cli -->

<!-- snap-2-7-ui
1. [What is the syslog logging path?](#heading--path)
2. [How do I use a remote syslog server?](#heading--using-a-remote-syslog-server)
3. [What are commissioning logs?](/t/commissioning-logs/2491)
4. [What are test logs?](/t/test-logs/3127)
5. [What are event logs?](/t/event-logs/3383)
6. [What are audit event logs?](t/audit-event-logs/2311)
 snap-2-7-ui -->

<!-- snap-2-8-cli
1. [What is the syslog logging path?](#heading--path)
2. [How do I use a remote syslog server?](#heading--using-a-remote-syslog-server)
3. [What are commissioning logs?](/t/commissioning-logs/2492)
4. [What are test logs?](/t/test-logs/3128)
5. [What are event logs?](/t/event-logs/3384)
6. [What are audit event logs?](t/audit-event-logs/2312)
 snap-2-8-cli -->

<!-- snap-2-8-ui
1. [What is the syslog logging path?](#heading--path)
2. [How do I use a remote syslog server?](#heading--using-a-remote-syslog-server)
3. [What are commissioning logs?](/t/commissioning-logs/2493)
4. [What are test logs?](/t/test-logs/3129)
5. [What are event logs?](/t/event-logs/3385)
6. [What are audit event logs?](t/audit-event-logs/2313)
 snap-2-8-ui -->

<!-- snap-2-9-cli
1. [What is the syslog logging path?](#heading--path)
2. [How do I use a remote syslog server?](#heading--using-a-remote-syslog-server)
3. [What are commissioning logs?](/t/commissioning-logs/2494)
4. [What are test logs?](/t/test-logs/3130)
5. [What are event logs?](/t/event-logs/3386)
6. [What are audit event logs?](t/audit-event-logs/2314)
 snap-2-9-cli -->

<!-- snap-2-9-ui
1. [What is the syslog logging path?](#heading--path)
2. [How do I use a remote syslog server?](#heading--using-a-remote-syslog-server)
3. [What are commissioning logs?](/t/commissioning-logs/2495)
4. [What are test logs?](/t/test-logs/3131)
5. [What are event logs?](/t/event-logs/3387)
6. [What are audit event logs?](t/audit-event-logs/2315)
 snap-2-9-ui -->

<!-- snap-3-0-cli
1. [What is the syslog logging path?](#heading--path)
2. [How do I use a remote syslog server?](#heading--using-a-remote-syslog-server)
3. [What are commissioning logs?](/t/commissioning-logs/3869)
4. [What are test logs?](/t/test-logs/4117)
5. [What are event logs?](/t/event-logs/3925)
6. [What are audit event logs?](t/audit-event-logs/3829)
 snap-3-0-cli -->

<!-- snap-3-0-ui
1. [What is the syslog logging path?](#heading--path)
2. [How do I use a remote syslog server?](#heading--using-a-remote-syslog-server)
3. [What are commissioning logs?](/t/commissioning-logs/2495)
4. [What are test logs?](/t/test-logs/4118)
5. [What are event logs?](/t/event-logs/3926)
6. [What are audit event logs?](t/audit-event-logs/3830)
 snap-3-0-ui -->

The discussion of these logs and their contents can be very extensive, so each type of logging has its own documentation section, reachable from the left-hand menu -- or from the list of questions above.

<a href="#heading--path"><h2 id="heading--path">The syslog logging path</h2></a>

<!-- deb-2-7-ui deb-2-7-cli deb-2-8-ui deb-2-8-cli deb-2-9-ui deb-2-9-cli
Syslog data is kept in `/var/log/maas/rsyslog/<machine-name><yyyy-mm-dd>/messages`.  Every machine known to MAAS will have corresponding syslogs.
deb-2-7-ui deb-2-7-cli deb-2-8-ui deb-2-8-cli deb-2-9-ui deb-2-9-cli -->

<!-- snap-2-7-ui snap-2-7-cli snap-2-8-ui snap-2-8-cli snap-2-9-ui snap-2-9-cli
Syslog data is kept in `/var/snap/maas/common/log/rsyslog/<machine-name><yyyy-mm-dd>/messages`. Every machine known to MAAS will have corresponding syslogs.
snap-2-7-ui snap-2-7-cli snap-2-8-ui snap-2-8-cli snap-2-9-ui snap-2-9-cli -->

<a href="#heading--using-a-remote-syslog-server"><h2 id="heading--using-a-remote-syslog-server">Using a remote syslog server</h2></a>

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui
To add a remote syslog server, click the Settings tab and then click the Network services tab. Scroll down to the Syslog section, where you can add a syslog URL or IP:

<a href="https://assets.ubuntu.com/v1/e139d4e9-installconfig-syslog__2.6-remote-syslog.png" target = "_blank"><img src="https://assets.ubuntu.com/v1/e139d4e9-installconfig-syslog__2.6-remote-syslog.png"></a>

Click the Save button to save your changes.
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui -->

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli
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

[note]
Note that MAAS controllers' syslogs are not forwarded to the external syslog server -- only machine syslog information is forwarded.
[/note]
snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli -->
