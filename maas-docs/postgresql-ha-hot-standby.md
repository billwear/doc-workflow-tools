||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/postgresql-ha-hot-standby-snap-2-7-cli/2994) ~ [UI](/t/postgresql-ha-hot-standby-snap-2-7-ui/2995)|[CLI](/t/postgresql-ha-hot-standby-snap-2-8-cli/2996) ~ [UI](/t/postgresql-ha-hot-standby-snap-2-8-ui/2997)|[CLI](/t/postgresql-ha-hot-standby-snap-2-9-cli/2998) ~ [UI](/t/postgresql-ha-hot-standby-snap-2-9-ui/2999)|[CLI](/t/postgresql-ha-hot-standby-snap-3-0-cli/4065) ~ [UI](/t/postgresql-ha-hot-standby-snap-3-0-ui/4066)|
Packages|[CLI](/t/postgresql-ha-hot-standby-deb-2-7-cli/3000) ~ [UI](/t/postgresql-ha-hot-standby-deb-2-7-ui/3001)|[CLI](/t/postgresql-ha-hot-standby-deb-2-8-cli/3002) ~ [UI](/t/postgresql-ha-hot-standby-deb-2-8-ui/3003)|[CLI](/t/postgresql-ha-hot-standby-deb-2-9-cli/3004) ~ [UI](/t/postgresql-ha-hot-standby-deb-2-9-ui/3005)|[CLI](/t/postgresql-ha-hot-standby-deb-3-0-cli/4067) ~ [UI](/t/postgresql-ha-hot-standby-deb-3-0-ui/4068)|

**Disclaimer: These *notes* give an idea of what is involved in setting up 'hot standby' HA mode in PostgreSQL. The below procedures are not regularly tested. Please use the [PostgreSQL documentation](https://www.postgresql.org/docs/9.5/static/high-availability.html) when setting up HA on PostgreSQL.**

Five variables are used on this page:

1.   PRIMARY_PG_IP: The IP address of the host that contains the primary database.
2.   SECONDARY_PG_IP: The IP address of the host that contains the secondary database.
3.   REP_USER: The internal database user that manages replication on the primary.
4.   REP_USER_PW: The password of the replication user.
5.   REP_ARCHIVE: The directory where the database will place files to be replicated.

Their values are represented when they are preceded with the '$' character (e.g. $REP_USER_PW). These are to be replaced with actual values in the commands and files below.

<a href="#heading--primary"><h2 id="heading--primary">Primary</h2></a>

Perform these actions on the primary host.

<a href="#heading--create-internal-database-user"><h3 id="heading--create-internal-database-user">Create internal database user</h3></a>

Create an internal database user to manage replication. You will be prompted to supply a password ($REP_USER_PW) for this new user:

``` bash
sudo -u postgres createuser -U postgres $REP_USER -P -c 5 --replication
```

<a href="#heading--set-up-replication-file-storage"><h3 id="heading--set-up-replication-file-storage">Set up replication file storage</h3></a>

Set up a place to store replication files:

``` bash
REP_ARCHIVE=/var/backups/pgsql/archive
sudo mkdir -p $REP_ARCHIVE
sudo chown postgres $REP_ARCHIVE
```

<a href="#heading--allow-secondary-host-to-connect"><h3 id="heading--allow-secondary-host-to-connect">Allow secondary host to connect</h3></a>

Edit `/etc/postgresql/9.5/main/pg_hba.conf` to allow the secondary host to contact this primary host.

``` no-highlight
host    replication     $REP_USER   $SECONDARY_PG_IP/32         md5
```

<a href="#heading--configure-for-replication"><h3 id="heading--configure-for-replication">Configure for replication</h3></a>

Edit `/etc/postgresql/9.5/main/postgresql.conf` to listen on more than just its localhost interface, turn on replication, and point to the archive directory:

``` no-highlight
listen_addresses = '*'
wal_level = hot_standby
archive_mode = on
archive_command = 'test ! -f $REP_ARCHIVE/%f && cp %p $REP_ARCHIVE/%f'
max_wal_senders = 3
```

<a href="#heading--restart-the-database"><h3 id="heading--restart-the-database">Restart the database</h3></a>

Restart the database to apply the above changes:

``` bash
sudo systemctl restart postgresql
```

Check log file `/var/log/postgresql/postgresql-9.5-main.log` on this primary host for any errors.

The primary database is now ready to accept replication requests from the secondary database (that will be set up below).

<a href="#heading--secondary"><h2 id="heading--secondary">Secondary</h2></a>

Perform these actions on the secondary host.

This host should ideally match the primary host in terms of:

1.   CPU architecture
2.   OS type and version
3.   PostgreSQL version

Replication has been known to fail due to an architecture mismatch.

<a href="#heading--install-postgresql-and-stop-the-service"><h3 id="heading--install-postgresql-and-stop-the-service">Install PostgreSQL and stop the service</h3></a>

Install PostgreSQL and stop the service:

``` bash
sudo apt install postgresql
sudo systemctl stop postgresql
```

<a href="#heading--copy-over-primary-database-files"><h3 id="heading--copy-over-primary-database-files">Copy over primary database files</h3></a>

Move the default database files out of the way and replace them with a copy of the primary database files. You will be prompted for the password of the remote replication user.

``` bash
sudo mv /var/lib/postgresql/9.5/main /var/lib/postgresql/9.5/main.old
sudo -u postgres pg_basebackup -h $PRIMARY_PG_IP -D /var/lib/postgresql/9.5/main -U $REP_USER -v -P --xlog-method=stream
Password: 
```

Once a copy of the primary database is transferred, proceed to configure actual replication.

<a href="#heading--place-database-in-hot-standby-mode"><h3 id="heading--place-database-in-hot-standby-mode">Place database in hot standby mode</h3></a>

Edit `/etc/postgresql/9.5/main/postgresql.conf` and put this secondary host in hot standby mode:

``` no-highlight
hot_standby = on
```

<a href="#heading--set-up-recovery-configuration-file"><h3 id="heading--set-up-recovery-configuration-file">Set up recovery configuration file</h3></a>

Copy a sample recovery configuration file into place:

``` bash
sudo cp /usr/share/postgresql/9.5/recovery.conf.sample /var/lib/postgresql/9.5/main/recovery.conf
```

<a href="#heading--configure-for-recovery"><h3 id="heading--configure-for-recovery">Configure for recovery</h3></a>

Edit `/var/lib/postgresql/9.5/main/recovery.conf`. Specify hot standby mode and enter the information necessary for contacting the primary:

``` no-highlight
standby_mode = on
primary_conninfo = 'host=$PRIMARY_PG_IP port=5432 user=$REP_USER password=$REP_USER_PW'
```

<a href="#heading--start-the-database"><h3 id="heading--start-the-database">Start the database</h3></a>

Start the database:

``` bash
sudo systemctl start postgresql
```

Check log file `/var/log/postgresql/postgresql-9.5-main.log` on this secondary host for any errors.

The secondary database is now replicating the primary database.

<a href="#heading--verification-of-replication"><h2 id="heading--verification-of-replication">Verification of replication</h2></a>

This section includes a raw test that will show whether replication is functioning.

On the **secondary** database host, perform a query on the 'maasserver_node' table in the 'maasdb' database:

``` bash
sudo -u postgres psql maasdb -c 'SELECT hostname,status,power_state FROM maasserver_node'
```

The output will look something like:

``` no-highlight
     hostname      | status | power_state 
-------------------+--------+-------------
 pmatulis-imp-maas |      0 | unknown
 node3             |      4 | off
 node1             |      6 | on
 node2             |      4 | off
 node4             |      6 | on
(5 rows)
```

This includes any hosts that are being used for API servers or rack controllers ('pmatulis-imp-maas' in this example). There are 4 regular MAAS nodes.

To quickly check that replication is working simply (temporarily) rename a node's hostname in the web UI and re-invoke the above command to see if the change is reflected.

Another test could be to change the status of a node, for example, by Commissioning or Deploying (a status of '4' is 'Ready' and a status of '6' is 'Deployed').
