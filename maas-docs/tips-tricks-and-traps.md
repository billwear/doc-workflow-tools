||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/tips-tricks-and-traps-snap-2-7-cli/3150) ~ [UI](/t/tips-tricks-and-traps-snap-2-7-ui/3151)|[CLI](/t/tips-tricks-and-traps-snap-2-8-cli/3152) ~ [UI](/t/tips-tricks-and-traps-snap-2-8-ui/3153)|[CLI](/t/tips-tricks-and-traps-snap-2-9-cli/3154) ~ [UI](/t/tips-tricks-and-traps-snap-2-9-ui/3155)|[CLI](/t/tips-tricks-and-traps-snap-3-0-cli/4129) ~ [UI](/t/tips-tricks-and-traps-snap-3-0-ui/4130)|
Packages|[CLI](/t/tips-tricks-and-traps-deb-2-7-cli/3156) ~ [UI](/t/tips-tricks-and-traps-deb-2-7-ui/3157)|[CLI](/t/tips-tricks-and-traps-deb-2-8-cli/3158) ~ [UI](/t/tips-tricks-and-traps-deb-2-8-ui/3159)|[CLI](/t/tips-tricks-and-traps-deb-2-9-cli/3160) ~ [UI](/t/tips-tricks-and-traps-deb-2-9-ui/3161)|[CLI](/t/tips-tricks-and-traps-deb-3-0-cli/4131) ~ [UI](/t/tips-tricks-and-traps-deb-3-0-ui/4132)|
This section contains a collection of tips, tricks, and traps which may help solve unusual or infrequent issues that come up.

#### What would you like to do?

1. [Migrate an existing snap installation to use a local PostgreSQL server](#heading--migrating-maas)
2. [Manually export the MAAS database](#heading--manual-export)
3. [Network boot an IBM Power server](#heading--ibm-power-server-pxe-boot)
4. [Try jq recipes using the CLI](#heading--jq-machine-list)
<!-- snap-2-8-cli snap-2-8-ui snap-2-9-cli snap-2-9-cli snap-3-0-ui snap-3-0-cli deb-2-8-cli deb-2-8-ui deb-2-9-cli deb-2-9-cli deb-3-0-ui deb-3-0-cli
5. [Resolve MAAS/LXD DNS & DHCP conflicts/network issues](#heading--maas-lxd-network-conflicts)
 snap-2-8-cli snap-2-8-ui snap-2-9-cli snap-2-9-cli snap-3-0-ui snap-3-0-cli deb-2-8-cli deb-2-8-ui deb-2-9-cli deb-2-9-cli deb-3-0-ui deb-3-0-cli -->

<h2 id="heading--migrating-maas">Migrating an existing snap installation</h2>

If you're currently running MAAS from a snap in `all` mode, you can easily migrate your database to a local PostgreSQL server with the following command:

    sudo /snap/maas/current/helpers/migrate-snap-database

This will install PostgreSQL from the archive and migrate the MAAS database to it. 

**Note** that if PostgreSQL is already installed on the machine, the script will move the current datadir out of the way and replace it with the one from the snap, after  confirmation with the user. If you want to keep the current database set and just import the MAAS database, you'll need to perform a manual dump/restore of the MAAS database, explained below.

The migration script will automatically adjust the snap configuration to use the new database.  Note, though, that the target database must be at least the same version level as the one currently used in the snap (PostgreSQL 10).  Consequently, the migration script only supports Ubuntu 18.04 (bionic) or later.

<h2 id="heading--manual-export">Manually exporting the MAAS database</h2>

If you want to export the database from the snap to an already setup PostgreSQL server, possibly on a different machine, you can manually export it from MAAS as follows. With MAAS running (as this ensures access to the database), run:

    export PGPASS=$(sudo awk -F':\\s+' '$1 == "database_pass" {print $2}' \
        /var/snap/maas/current/regiond.conf)
    sudo pg_dump -U maas -h /var/snap/maas/common/postgres/sockets \
        -d maasdb -F t -f maasdb-dump.tar

This will produce a binary dump in `maasdb-dump.tar`.  You can then stop the MAAS snap via

    sudo snap stop maas

Before importing it to the new database server, you need to create a user and database for MAAS:

``` nohighlight
sudo -u postgres \
    psql -c "CREATE USER maas WITH ENCRYPTED PASSWORD '<password>'"
sudo -u postgres createdb maasdb -O maas
```

Also, make sure that remote access is set up for the newly created `maas` user in `/etc/postgresql/10/main/pg_hba.conf`.  The file should contain a line similar to:

    host    maasdb  maas    0/0     md5

Be sure to replace `0/0`, above, with the proper CIDR to restrict access to a specific subnet.  Finally, you can import the database dump with:

    sudo -u postgres pg_restore -d maasdb maasdb-dump.tar

To finish the process, you'll need to update the MAAS snap config to:

1. update the database config in `/var/snap/maas/current/regiond.conf` with the proper `database_host` and `database_pass`
2. change the content of `/var/snap/maas/common/snap_mode` from `all` to `region+rack`

Using a local PostgreSQL server is a little bit of work, but it provides great benefits in terms of MAAS scalability and performance.

<h2 id="heading--ibm-power-server-pxe-boot">Network booting IBM Power servers</h2>

Some IBM Power server servers have OPAL firmware which uses an embedded Linux distribution as the boot environment. All the PXE interactions are handled by **Petitboot**, which runs in the userspace of this embedded Linux rather than a PXE ROM on the NIC itself.

When no specific interface is assigned as the network boot device, petitboot has a known issue which is detailed in [LP#1852678](https://bugs.launchpad.net/ubuntu-power-systems/+bug/1852678), specifically comment #24, that can cause issues when deploying systems using MAAS, since in this case all active NICs are used for PXE boot with the same address.

So, when using IBM Power servers with multiple NICs that can network boot, it's strongly recommended to configure just a single <specific> NIC as the network boot device via **Petitboot**.

<!-- snap-2-8-cli snap-2-8-ui snap-2-9-cli snap-2-9-cli snap-3-0-ui snap-3-0-cli deb-2-8-cli deb-2-8-ui deb-2-9-cli deb-2-9-cli deb-3-0-ui deb-3-0-cli
<h2 id="heading--maas-lxd-network-conflicts">Resolve DNS conflicts between LXD and MAAS</h2>

If you get into a situation where MAAS and LXD are both managing DNS on your MAAS network, there's a simple fix. You can turn off LXD's DNS management with the following command:

````bash
lxc network set $LXD_BRIDGE_NAME dns.mode=none
````

You should also disable DHCP on IPv4 and IPv6 withing LXD:

````bash
lxc network set $LXD_BRIDGE_NAME ipv4.dncp=false
lxc network set $LXD_BRIDGE_NAME ipv6.dhcp=false
````

Once you've done this, you can check your work with the following command:

````bash
lxc network show $LXD_BRIDGE_NAME
````

 snap-2-8-cli snap-2-8-ui snap-2-9-cli snap-2-9-cli snap-3-0-ui snap-3-0-cli deb-2-8-cli deb-2-8-ui deb-2-9-cli deb-2-9-cli deb-3-0-ui deb-3-0-cli -->


<h2 id="heading--jq-machine-list">jq recipes using the CLI</h2>

Here are some `jq` recipes to get some human-readable output from the MAAS CLI.

<h3 id="heading--jqml-sh">Basic machine list</h3>

This recipe, which we keep in a file called `jqml.sh`, prints a basic machine list

    #!/bin/bash
    maas admin machines read | jq -r '(["HOSTNAME","SYSID","POWER","STATUS",
    "OWNER", "POOL", "VLAN","FABRIC","SUBNET"] | (., map(length*"-"))),
    (.[] | [.hostname, .system_id, .power_state, .status_name, .owner, .pool.name,
    .boot_interface.vlan.name, .boot_interface.vlan.fabric,
    .boot_interface.links[0].subnet.name]) | @tsv' | column -t

For this to work, you need to **only** break lines in the jq string ('...') or add backslashes if you break outside that boundary.

<h3 id="heading--jqmltag-sh">Machine list with first tag added</h3>

It's a good idea to keep your most important machine tag first, as it's the first one you'll see.  It makes scanning your list (UI or CLI/jq) much more efficient.  Here's a recipe that adds the first tag to the console-printed machine list.  We keep it in `jqmltag.sh`, but of course, you can call it whatever you want.

     #!/bin/bash
     maas admin machines read | jq -r '(["HOSTNAME","SYSID","POWER","STATUS",
     "OWNER", "TAGS", "POOL", "VLAN","FABRIC","SUBNET"] | (., map(length*"-"))),
     (.[] | [.hostname, .system_id, .power_state, .status_name, .owner // "-", 
     .tag_names[0] // "-", .pool.name,
     .boot_interface.vlan.name, .boot_interface.vlan.fabric,
     .boot_interface.links[0].subnet.name]) | @tsv' | column -t
