||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/backup-snap-2-7-cli/2334) ~ [UI](/t/backup-snap-2-7-ui/2335)|[CLI](/t/backup-snap-2-8-cli/2336) ~ [UI](/t/backup-snap-2-8-ui/2337)|[CLI](/t/backup-snap-2-9-cli/2338) ~ [UI](/t/backup-snap-2-9-ui/2339)|[CLI](/t/backup-snap-3-0-cli/3837) ~ [UI](/t/backup-snap-3-0-ui/3838)|
Packages|[CLI](/t/backup-deb-2-7-cli/2340) ~ [UI](/t/backup-deb-2-7-ui/2341)|[CLI](/t/backup-deb-2-8-cli/2342) ~ [UI](/t/backup-deb-2-8-ui/2343)|[CLI](/t/backup-deb-2-9-cli/2344) ~ [UI](/t/backup-deb-2-9-ui/2345)|[CLI](/t/backup-deb-3-0-cli/3839) ~ [UI](/t/backup-deb-3-0-ui/3840)|

MAAS currently does not provide specific tools to back up and restore a working MAAS configuration. MAAS servers are part of your data centre, just like other Linux-based servers, so your current backup and disaster recovery solution should be sufficient to back up your MAAS environment.  Even so, you should know which files and actions are critical -- to ensure that you get a clean backup, and further ensure that you can restore it cleanly.

#### Six questions you may have:

1. [What configuration files should I capture in my backup?](#heading--configuration-files)
2. [How should I prepare PostgreSQL data for backup?](#heading--postgresql-export)
3. [What services should I stop before backing up?](#heading--stop-critical-services)
4. [How should I archive files to make the backup more efficient?](#heading--archive-configuration-files)
5. [How do I restore my system, should the need arise?](#heading--restore-files)
6. [What steps should I take to restore the database to normal operation?](#heading--recreatingupdating-the-db)

<a href="#heading--configuration-files"><h2 id="heading--configuration-files">Configuration files</h2></a>

The following three MAAS components need to be backed-up and restored, on each region and rack controller, to recreate a working environment:

<!-- deb-2-7-ui deb-2-7-cli deb-2-8-ui deb-2-8-cli deb-2-9-ui deb-2-9-cli deb-3-0-ui deb-3-0-cli
1.  The PostgreSQL database
2.  The configuration files in `/etc/maas`
3.  The configuration files in `/var/lib/maas`

`/var/lib/maas/boot-resources` can safely be excluded as this contains images easily re-downloaded within MAAS.
deb-2-7-ui deb-2-7-cli deb-2-8-ui deb-2-8-cli deb-2-9-ui deb-2-9-cli deb-3-0-ui deb-3-0-cli-->

<!-- snap-2-7-ui snap-2-7-cli snap-2-8-ui snap-2-8-cli snap-2-9-ui snap-2-9-cli snap-3-0-ui snap-3-0-cli
1.  The PostgreSQL database
2.  The configuration files in `/snap/maas/current/etc/maas`
3.  The configuration files in `/var/snap/maas/common/maas/`

`/var/snap/maas/common/maas/boot-resources` can safely be excluded as this contains images easily re-downloaded within MAAS.
snap-2-7-ui snap-2-7-cli snap-2-8-ui snap-2-8-cli snap-2-9-ui snap-2-9-cli snap-3-0-ui snap-3-0-cli -->

Other configuration files, such as those used by your network configuration (`/etc/network/interfaces`, for example) will need to be backed-up and restored according to your specific deployment requirements.

<a href="#heading--postgresql-export"><h2 id="heading--postgresql-export">PostgreSQL export</h2></a>

Prior to stopping services (as described in the next section), export your PostgreSQL database with a database dump.  This process is described in the following procedure, which involves three assumptions: 

1. you have installed region and rack controllers on the same machine. 
2. you have installed MAAS on Ubuntu 18.04 LTS (Bionic).
3. you are restoring software an identical hardware and network configuration.

To backup your PostgreSQL database to a file called `dump.sql` in your home directories, enter the following:

``` bash
sudo -u postgres pg_dumpall -c > ~/dump.sql
```

If you run the above `pg_dumpall` process in the background, you can ensure this has completed and that there are no other established sessions with the following command:

``` bash
sudo -u postgres psql -c  "SELECT * FROM pg_stat_activity"
```

Running sessions, such as pg_dumpall, will appear in the `application_name` column of the output alongside `psql` running the above `pg_stat_activity` query. Excepting psql, if `application_name` is empty, you can safely stop the database service.

<a href="#heading--stop-critical-services"><h2 id="heading--stop-critical-services">Stop critical services</h2></a>

After you have dumped your PostgreSQL database, and verified that the dump has finished, you should stop the following four services with the `sudo systemctl stop <service>` command:

1.   postgresql.service
2.   maas-dhcpd.service
3.   maas-rackd.service
4.   maas-regiond.service

Stopping these services will avoid conflicting updates during the remaining backup steps.

<a href="#heading--archive-configuration-files"><h2 id="heading--archive-configuration-files">Archive configuration files</h2></a>

Archive the database and the required configuration files with a command similar to the following:

<!-- deb-2-7-ui deb-2-7-cli deb-2-8-ui deb-2-8-cli deb-2-9-ui deb-2-9-cli deb-3-0-ui deb-3-0-cli
``` bash
sudo tar cvpzf ~/backup.tgz --exclude=/var/lib/maas/boot-resources /etc/maas /var/lib/maas ~/dump.sql
```
deb-2-7-ui deb-2-7-cli deb-2-8-ui deb-2-8-cli deb-2-9-ui deb-2-9-cli deb-3-0-ui deb-3-0-cli -->

<!-- snap-2-7-ui snap-2-7-cli snap-2-8-ui snap-2-8-cli snap-2-9-ui snap-2-9-cli snap-3-0-ui snap-3-0-cli 
``` bash
sudo tar cvpzf ~/backup.tgz --exclude=/var/snap/maas/common/maas/boot-resources /snap/maas/current/etc/maas /var/snap/maas/common/maas ~/dump.sql
```
snap-2-7-ui snap-2-7-cli snap-2-8-ui snap-2-8-cli snap-2-9-ui snap-2-9-cli snap-3-0-ui snap-3-0-cli -->

Make sure you move the resulting `backup.tgz` to some external storage you can access when restoring the system.  Also, make sure to restart the services you stopped prior to completing the backup.

We've now backed up all the components necessary to recreate a MAAS deployment. Next, we'll discuss how to restore this configuration.

<a href="#heading--restore-files"><h2 id="heading--restore-files">Restore files</h2></a>

Start with a freshly-updated installation of Ubuntu on identical hardware. Reinstall MAAS via the standard procedure (`sudo apt install maas`), then stop the following three services (PostgreSQL needs to keep running):

1.   maas-dhcpd.service
2.   maas-rackd.service
3.   maas-regiond.service

Copy the backup file to the new machine and untar its contents (`sudo tar xvzpf backup.tgz`).

To restore the state of the database, enter the following from the backup directory:

``` bash
sudo -u postgres psql -f dump.sql postgres
```

Next, copy across the old configuration files to their new locations, taking care to move the originals aside just in case:

<!-- deb-2-7-ui deb-2-7-cli deb-2-8-ui deb-2-8-cli deb-2-9-ui deb-2-9-cli deb-3-0-ui deb-3-0-cli 
``` bash
sudo mv /etc/maas /etc/_maas; mv /var/lib/maas /var/lib/_maas
essudo cp -prf etc/maas /etc/; cp -prf var/lib/maas /var/lib/
```

If your restore process regenerated the `/var/lib/maas/secret` file, make sure update this secret on any additional rack controllers.
deb-2-7-ui deb-2-7-cli deb-2-8-ui deb-2-8-cli deb-2-9-ui deb-2-9-cli deb-3-0-ui deb-3-0-cli -->

<!-- snap-2-7-ui snap-2-7-cli snap-2-8-ui snap-2-8-cli snap-2-9-ui snap-2-9-cli snap-3-0-ui snap-3-0-cli 
``` bash
sudo mv /snap/maas/current/etc/maas /snap/maas/current/etc/_maas
sudo mv /var/snap/maas/common/maas /var/snap/maas/common/_maas
sudo cp -prf /snap/maas/current/etc/maas /snap/maas/current/etc/
sudo cp -prf /var/snap/maas/common/maas /var/snap/maas/common/
```

If your restore process regenerated the `/var/snap/maas/common/maas/secret` file, make sure update this secret on any additional rack controllers.
snap-2-7-ui snap-2-7-cli snap-2-8-ui snap-2-8-cli snap-2-9-ui snap-2-9-cli snap-3-0-ui snap-3-0-cli -->

[note]
Take care to preserve the correct permissions when restoring files and directories.
[/note]

<a href="#heading--recreatingupdating-the-db"><h2 id="heading--recreatingupdating-the-db">Recreating/updating the DB</h2></a>

When you restore a backup, you'll have to "upgrade" the DB schema to re-create DB triggers or ensure that the schema matches the currently-running version.

MAAS relies on various DB triggers for multiple operations. As such, it is always required to re-create those after restoring from a backup. Similarly, newer versions of MAAS may have new or missing migrations, and merely restoring a backup may not be enough to restore normal operation.

As such, it is required to re-create the DB triggers (or upgrade the DB and run new/missing migrations) with the following command:

``` bash
sudo maas-region dbupgrade
```

[note]
Please note to run this command on one of the Region Controllers (if this is a multi-region MAAS cluster).
[/note]

Now either restart your system(s) or the stopped services. You'll find your MAAS deployment fully restored.
