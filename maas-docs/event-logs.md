||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/event-logs-snap-2-7-cli/3382) ~ [UI](/t/event-logs-snap-2-7-ui/3383)|[CLI](/t/event-logs-snap-2-8-cli/3384) ~ [UI](/t/event-logs-snap-2-8-ui/3385)|[CLI](/t/event-logs-snap-2-9-cli/3386) ~ [UI](/t/event-logs-snap-2-9-ui/3387)|[CLI](/t/event-logs-snap-3-0-cli/3925) ~ [UI](/t/event-logs-snap-3-0-ui/3926)|
Packages|[CLI](/t/event-logs-deb-2-7-cli/3388) ~ [UI](/t/event-logs-deb-2-7-ui/3389)|[CLI](/t/event-logs-deb-2-8-cli/3390) ~ [UI](/t/event-logs-deb-2-8-ui/3391)|[CLI](/t/event-logs-deb-2-9-cli/3393) ~ [UI](/t/event-logs-deb-2-9-ui/3392)|[CLI](/t/event-logs-deb-3-0-cli/3927) ~ [UI](/t/event-logs-deb-3-0-ui/3928)|

The events log tracks state changes and the execution of basic configuration steps, serving as a timeline for your MAAS machines.  A simple view of the events log might look something like this:

```
  Time 	                        Event
  Sun, 04 Oct. 2020 23:12:35 	Ready
  Sun, 04 Oct. 2020 23:12:31 	Running test - smartctl-validate on sda
  Sun, 04 Oct. 2020 23:10:37 	Gathering information
  Sun, 04 Oct. 2020 23:10:30 	Loading ephemeral
  Sun, 04 Oct. 2020 23:10:15 	Performing PXE boot
  Sun, 04 Oct. 2020 23:09:54 	Powering on
  Sun, 04 Oct. 2020 23:09:53 	Commissioning
```

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
To view the Events log (for a particular machine), select a machine from the machine list and choose the "Events" tab at the top of the screen:

<a href="https://discourse.maas.io/uploads/default/original/1X/45ad4b968f85ef38e875e6df03d9f832fc7d4743.png" target = "_blank"><img  src="https://discourse.maas.io/uploads/default/original/1X/45ad4b968f85ef38e875e6df03d9f832fc7d4743.png"></a>

You can also see a more detailed view by selecting "View full history" in near the upper right of the log output.
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui -->

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 
To view the raw Events log, enter the following command:

```
maas $PROFILE events query
```

You can tabulate the results, sorted by machine, with the following command:

```
maas admin events query | jq -r '(["HOSTNAME","TIMESTAMP","TYPE","DESCRIPTION"] | (., map(length*"-"))),
(.events[] | [.hostname, .created, .type, .description // "-"]) | @tsv' | column -t -s $'\t'
snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli  -->
