||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/region-controllers-snap-2-7-cli/3066) ~ [UI](/t/region-controllers-snap-2-7-ui/3067)|[CLI](/t/region-controllers-snap-2-8-cli/3068) ~ [UI](/t/region-controllers-snap-2-8-ui/3069)|[CLI](/t/region-controllers-snap-2-9-cli/3070) ~ [UI](/t/region-controllers-snap-2-9-ui/3071)|[CLI](/t/region-controllers-snap-3-0-cli/4093) ~ [UI](/t/region-controllers-snap-3-0-ui/4094)|
Packages|[CLI](/t/region-controllers-deb-2-7-cli/3072) ~ [UI](/t/region-controllers-deb-2-7-ui/3073)|[CLI](/t/region-controllers-deb-2-8-cli/3074) ~ [UI](/t/region-controllers-deb-2-8-ui/3075)|[CLI](/t/region-controllers-deb-2-9-cli/3076) ~ [UI](/t/region-controllers-deb-2-9-ui/3077)|[CLI](/t/region-controllers-deb-3-0-cli/4095) ~ [UI](/t/region-controllers-deb-3-0-ui/4096)|

A region controller manages communication with the user, via the Web UI/API, as well as managing the rack controller(s) in your system.  The MAAS postgres database is also managed by the region controller.  Typical region-level responsibilities include requesting that a rack controller boot a machine, and providing the ephemeral Ubuntu image needed to commission or enlist a machine.  

#### Three questions you might have:

1. [How do I set up PostgreSQL for the region?](#heading--postgresql-setup)
2. [How do I add a new region host?](#heading--adding-a-new-region-host)
3. [How can I improve region controller performance?](#heading--increasing-regiond-daemon-workers)

<a href="#heading--postgresql-setup"><h2 id="heading--postgresql-setup">Set up PostgreSQL for the region</h2></a>

Any number of API servers (region controllers) can be present as long as each connects to the same PostgreSQL database and allows the required number of connections.

On the primary database host, edit file <code>/etc/postgresql/9.5/main/pg_hba.conf</code> to allow the eventual secondary API server to contact the primary PostgreSQL database. Include the below line, replacing
<code>$SECONDARY_API_SERVER_IP</code> with the IP address of the host that will contain the secondary API server:

    host maasdb maas $SECONDARY_API_SERVER_IP/32 md5

[note]
The primary database and API servers often reside on the same host.
[/note]

Apply this change by restarting the database:

    sudo systemctl restart postgresql

<a href="#heading--adding-a-new-region-host"><h2 id="heading--adding-a-new-region-host">Add a new region host</h2></a>

On a secondary host, add the new region controller by installing <code>maas-region-api</code>:

    sudo apt install maas-region-api

You will need the <code>/etc/maas/regiond.conf</code> file from the primary API server. Below, we assume it can be copied (scp) from the ‘ubuntu’ account home directory using password authentication (adjust otherwise). The <code>local_config_set</code> command will edit that file by pointing to the host that contains the primary PostgreSQL database. Do not worry: MAAS will rationalise the DNS (<code>bind9</code>) configuration options so that they match those used within MAAS:

    sudo systemctl stop maas-regiond
    sudo scp ubuntu@$PRIMARY_API_SERVER:regiond.conf /etc/maas/regiond.conf
    sudo chown root:maas /etc/maas/regiond.conf
    sudo chmod 640 /etc/maas/regiond.conf
    sudo maas-region local_config_set --database-host $PRIMARY_PG_SERVER
    sudo systemctl restart bind9
    sudo systemctl start maas-regiond

Check three log files for any errors:

1. <code>/var/log/maas/regiond.log</code></li>
2. <code>/var/log/maas/maas.log</code></li>
3. <code>/var/log/syslog</code></li>

<a href="#heading--increasing-regiond-daemon-workers"><h2 id="heading--increasing-regiond-daemon-workers">Improving region controller performance</h2></a>

[note]
This functionality is available starting from MAAS 2.4.
[/note]

The MAAS Region Controller is a daemon collection of 4 workers that are in charge of handling all the internals of MAAS. The regiond workers handle the UI, API and the internal communication between Region and Rack controllers.

In larger environments, which multiple rack controllers, you can easily improve performance within a region.  You can increase the number of workers, which allows faster (parallel) handling of internal communication between region and rack controllers.

<!-- snap-2-7-cli
Increasing the number of workers will also increase the number of required database connections by 11 per extra worker. This may required PostgreSQL to have an increased number of allowed connections; please see <a href="/t/high-availability/2682#heading--region-controller-ha">PostgreSQL High Availability section</a> for more information to increase the connections.
snap-2-7-cli -->

<!-- snap-2-7-ui
Increasing the number of workers will also increase the number of required database connections by 11 per extra worker. This may required PostgreSQL to have an increased number of allowed connections; please see <a href="/t/high-availability/2683#heading--region-controller-ha">PostgreSQL High Availability section</a> for more information to increase the connections.
snap-2-7-ui -->

<!-- snap-2-8-cli
Increasing the number of workers will also increase the number of required database connections by 11 per extra worker. This may required PostgreSQL to have an increased number of allowed connections; please see <a href="/t/high-availability/2684#heading--region-controller-ha">PostgreSQL High Availability section</a> for more information to increase the connections.
snap-2-8-cli -->

<!-- snap-2-8-ui
Increasing the number of workers will also increase the number of required database connections by 11 per extra worker. This may required PostgreSQL to have an increased number of allowed connections; please see <a href="/t/high-availability/2685#heading--region-controller-ha">PostgreSQL High Availability section</a> for more information to increase the connections.
snap-2-8-ui -->

<!-- snap-2-9-cli
Increasing the number of workers will also increase the number of required database connections by 11 per extra worker. This may required PostgreSQL to have an increased number of allowed connections; please see <a href="/t/high-availability/2686#heading--region-controller-ha">PostgreSQL High Availability section</a> for more information to increase the connections.
snap-2-9-cli -->

<!-- snap-2-9-ui
Increasing the number of workers will also increase the number of required database connections by 11 per extra worker. This may required PostgreSQL to have an increased number of allowed connections; please see <a href="/t/high-availability/2687#heading--region-controller-ha">PostgreSQL High Availability section</a> for more information to increase the connections.
snap-2-9-ui -->

<!-- snap-3-0-cli
Increasing the number of workers will also increase the number of required database connections by 11 per extra worker. This may required PostgreSQL to have an increased number of allowed connections; please see <a href="/t/high-availability/3945#heading--region-controller-ha">PostgreSQL High Availability section</a> for more information to increase the connections.
snap-3-0-cli -->

<!-- snap-3-0-ui
Increasing the number of workers will also increase the number of required database connections by 11 per extra worker. This may required PostgreSQL to have an increased number of allowed connections; please see <a href="/t/high-availability/3946#heading--region-controller-ha">PostgreSQL High Availability section</a> for more information to increase the connections.
snap-3-0-ui -->

<!-- deb-2-7-cli
Increasing the number of workers will also increase the number of required database connections by 11 per extra worker. This may required PostgreSQL to have an increased number of allowed connections; please see <a href="/t/high-availability/2688#heading--region-controller-ha">PostgreSQL High Availability section</a> for more information to increase the connections.
deb-2-7-cli -->

<!-- deb-2-7-ui
Increasing the number of workers will also increase the number of required database connections by 11 per extra worker. This may required PostgreSQL to have an increased number of allowed connections; please see <a href="/t/high-availability/2689#heading--region-controller-ha">PostgreSQL High Availability section</a> for more information to increase the connections.
deb-2-7-ui -->

<!-- deb-2-8-cli
Increasing the number of workers will also increase the number of required database connections by 11 per extra worker. This may required PostgreSQL to have an increased number of allowed connections; please see <a href="/t/high-availability/2690#heading--region-controller-ha">PostgreSQL High Availability section</a> for more information to increase the connections.
deb-2-8-cli -->

<!-- deb-2-8-ui
Increasing the number of workers will also increase the number of required database connections by 11 per extra worker. This may required PostgreSQL to have an increased number of allowed connections; please see <a href="/t/high-availability/2691#heading--region-controller-ha">PostgreSQL High Availability section</a> for more information to increase the connections.
deb-2-8-ui -->

<!-- deb-2-9-cli
Increasing the number of workers will also increase the number of required database connections by 11 per extra worker. This may required PostgreSQL to have an increased number of allowed connections; please see <a href="/t/high-availability/2692#heading--region-controller-ha">PostgreSQL High Availability section</a> for more information to increase the connections.
deb-2-9-cli -->

<!-- deb-2-9-ui
Increasing the number of workers will also increase the number of required database connections by 11 per extra worker. This may required PostgreSQL to have an increased number of allowed connections; please see <a href="/t/high-availability/2693#heading--region-controller-ha">PostgreSQL High Availability section</a> for more information to increase the connections.
deb-2-9-ui -->

<!-- deb-3-0-cli
Increasing the number of workers will also increase the number of required database connections by 11 per extra worker. This may required PostgreSQL to have an increased number of allowed connections; please see <a href="/t/high-availability/3947#heading--region-controller-ha">PostgreSQL High Availability section</a> for more information to increase the connections.
deb-3-0-cli -->

<!-- deb-3-0-ui
Increasing the number of workers will also increase the number of required database connections by 11 per extra worker. This may required PostgreSQL to have an increased number of allowed connections; please see <a href="/t/high-availability/3948#heading--region-controller-ha">PostgreSQL High Availability section</a> for more information to increase the connections.
deb-3-0-ui -->

To increase the number of workers, simply edit <code>regiond.conf (/etc/maas/regiond.conf)</code> and set <code>num_workers</code>. For example:

    [...]
    num_workers: 8

Keep in mind that adding too many workers may <em>reduce</em> performance. We recommended one worker per CPU, up to eight workers in total. Increasing beyond that is possible but use at your own risk.
