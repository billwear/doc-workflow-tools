||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/high-availability-snap-2-7-cli/2682) ~ [UI](/t/high-availability-snap-2-7-ui/2683)|[CLI](/t/high-availability-snap-2-8-cli/2684) ~ [UI](/t/high-availability-snap-2-8-ui/2685)|[CLI](/t/high-availability-snap-2-9-cli/2686) ~ [UI](/t/high-availability-snap-2-9-ui/2687)|[CLI](/t/high-availability-snap-3-0-cli/3945) ~ [UI](/t/high-availability-snap-3-0-ui/3946)|
Packages|[CLI](/t/high-availability-deb-2-7-cli/2688) ~ [UI](/t/high-availability-deb-2-7-ui/2689)|[CLI](/t/high-availability-deb-2-8-cli/2690) ~ [UI](/t/high-availability-deb-2-8-ui/2691)|[CLI](/t/high-availability-deb-2-9-cli/2692) ~ [UI](/t/high-availability-deb-2-9-ui/2693)|[CLI](/t/high-availability-deb-3-0-cli/3947) ~ [UI](/t/high-availability-deb-3-0-ui/3948)|

This page describes how to provide high availability (HA) for MAAS at both region and rack levels.  In the context of MAAS, there are four types of HA:

1. BMC (node power cycling)
2. DHCP
3. PostgreSQL
4. API services

#### Nine questions you might have:

1. [How do I make rack controllers highly available?](#heading--rack-controller-ha)
2. [How do I enable highly-available BMC?](#heading--bmc-ha)
3. [How do I enable highly-available DHCP services?](#heading--dhcp-ha)
4. [How do I make region controllers highly available?](#heading--region-controller-ha)
5. [How do I enable highly-available PostgreSQL?](#heading--postgresql-ha)
6. [How do I enable highly-available API services?](#heading--secondary-api-servers)
7. [How do I enable load balancing for API services?](#heading--load-balancing-with-haproxy-optional)
8. [How do I move a rack controller from one MAAS instance to another?](#heading--move-rack-controller)
9. [What are the potential dangers of moving a rack controller?](#heading--dangers-moving-rack-controller)

<a href="#heading--rack-controller-ha"><h2 id="heading--rack-controller-ha">Make rack controllers highly available</h2></a>

<!-- deb-2-7-cli
You need to [install multiple rack controllers](/t/rack-controllers/3060#heading--install-a-rack-controller) to achieve real high availability.  Once that's done, you automatically gain highly-available BMC control, and you can also enable highly-available DHCP.
 deb-2-7-cli -->

<!-- deb-2-7-ui
You need to [install multiple rack controllers](/t/rack-controllers/3061#heading--install-a-rack-controller) to achieve real high availability.  Once that's done, you automatically gain highly-available BMC control, and you can also enable highly-available DHCP.
 deb-2-7-ui -->

<!-- deb-2-8-cli
You need to [install multiple rack controllers](/t/rack-controllers/3062#heading--install-a-rack-controller) to achieve real high availability.  Once that's done, you automatically gain highly-available BMC control, and you can also enable highly-available DHCP.
 deb-2-8-cli -->

<!-- deb-2-8-ui
You need to [install multiple rack controllers](/t/rack-controllers/3063#heading--install-a-rack-controller) to achieve real high availability.  Once that's done, you automatically gain highly-available BMC control, and you can also enable highly-available DHCP.
 deb-2-8-ui -->

<!-- deb-2-9-cli
You need to [install multiple rack controllers](/t/rack-controllers/3064#heading--install-a-rack-controller) to achieve real high availability.  Once that's done, you automatically gain highly-available BMC control, and you can also enable highly-available DHCP.
 deb-2-9-cli -->

<!-- deb-2-9-ui
You need to [install multiple rack controllers](/t/rack-controllers/3065#heading--install-a-rack-controller) to achieve real high availability.  Once that's done, you automatically gain highly-available BMC control, and you can also enable highly-available DHCP.
 deb-2-9-ui -->

<!-- deb-3-0-cli
You need to [install multiple rack controllers](/t/rack-controllers/4091#heading--install-a-rack-controller) to achieve real high availability.  Once that's done, you automatically gain highly-available BMC control, and you can also enable highly-available DHCP.
 deb-3-0-cli -->

<!-- deb-3-0-ui
You need to [install multiple rack controllers](/t/rack-controllers/4092#heading--install-a-rack-controller) to achieve real high availability.  Once that's done, you automatically gain highly-available BMC control, and you can also enable highly-available DHCP.
 deb-3-0-ui -->

<!-- snap-2-7-cli
You need to [install multiple rack controllers](/t/rack-controllers/3054#heading--install-a-rack-controller) to achieve real high availability.  Once that's done, you automatically gain highly-available BMC control, and you can also enable highly-available DHCP.
 snap-2-7-cli -->

<!-- snap-2-7-ui
You need to [install multiple rack controllers](/t/rack-controllers/3055#heading--install-a-rack-controller) to achieve real high availability.  Once that's done, you automatically gain highly-available BMC control, and you can also enable highly-available DHCP.
 snap-2-7-ui -->

<!-- snap-2-8-cli
You need to [install multiple rack controllers](/t/rack-controllers/3056#heading--install-a-rack-controller) to achieve real high availability.  Once that's done, you automatically gain highly-available BMC control, and you can also enable highly-available DHCP.
 snap-2-8-cli -->

<!-- snap-2-8-ui
You need to [install multiple rack controllers](/t/rack-controllers/3057#heading--install-a-rack-controller) to achieve real high availability.  Once that's done, you automatically gain highly-available BMC control, and you can also enable highly-available DHCP.
 snap-2-8-ui -->

<!-- snap-2-9-cli
You need to [install multiple rack controllers](/t/rack-controllers/3058#heading--install-a-rack-controller) to achieve real high availability.  Once that's done, you automatically gain highly-available BMC control, and you can also enable highly-available DHCP.
 snap-2-9-cli -->

<!-- snap-2-9-ui
You need to [install multiple rack controllers](/t/rack-controllers/3059#heading--install-a-rack-controller) to achieve real high availability.  Once that's done, you automatically gain highly-available BMC control, and you can also enable highly-available DHCP.
 snap-2-9-ui -->

<!-- snap-3-0-cli
You need to [install multiple rack controllers](/t/rack-controllers/4089#heading--install-a-rack-controller) to achieve real high availability.  Once that's done, you automatically gain highly-available BMC control, and you can also enable highly-available DHCP.
 snap-3-0-cli -->

<!-- snap-3-0-ui
You need to [install multiple rack controllers](/t/rack-controllers/4090#heading--install-a-rack-controller) to achieve real high availability.  Once that's done, you automatically gain highly-available BMC control, and you can also enable highly-available DHCP.
 snap-3-0-ui -->

<a href="#heading--bmc-ha"><h3 id="heading--bmc-ha">Enable highly-available BMC</h3></a>

HA for BMC control (node power cycling) is provided out-of-the-box, once a second rack controller is present. MAAS will automatically identify which rack controller is responsible for a BMC and set up communication accordingly.

<a href="#heading--dhcp-ha"><h3 id="heading--dhcp-ha">Enable highly-available DHCP services</h3></a>

DHCP HA affects the way MAAS manages node, including enlistment, commissioning and deployment. It enables primary and secondary DHCP instances to serve the same VLAN. This VLAN replicates all lease information is between rack controllers. MAAS-managed DHCP is a requirement for DHCP HA.

<!-- deb-2-7-cli
If you are enabling DHCP for the first time after adding a second rack controller, please read [Enabling DHCP](/t/managing-dhcp/2904#heading--enabling-dhcp).  On the other hand, if you have already enabled DHCP on your initial rack controller, you'll need to reconfigure DHCP.
 deb-2-7-cli -->

<!-- deb-2-7-ui
If you are enabling DHCP for the first time after adding a second rack controller, please read [Enabling DHCP](/t/managing-dhcp/2905#heading--enabling-dhcp).  On the other hand, if you have already enabled DHCP on your initial rack controller, you'll need to reconfigure DHCP.
 deb-2-7-ui -->

<!-- deb-2-8-cli
If you are enabling DHCP for the first time after adding a second rack controller, please read [Enabling DHCP](/t/managing-dhcp/2906#heading--enabling-dhcp).  On the other hand, if you have already enabled DHCP on your initial rack controller, you'll need to reconfigure DHCP.
 deb-2-8-cli -->

<!-- deb-2-8-ui
If you are enabling DHCP for the first time after adding a second rack controller, please read [Enabling DHCP](/t/managing-dhcp/2907#heading--enabling-dhcp).  On the other hand, if you have already enabled DHCP on your initial rack controller, you'll need to reconfigure DHCP.
 deb-2-8-ui -->

<!-- deb-2-9-cli
If you are enabling DHCP for the first time after adding a second rack controller, please read [Enabling DHCP](/t/managing-dhcp/2908#heading--enabling-dhcp).  On the other hand, if you have already enabled DHCP on your initial rack controller, you'll need to reconfigure DHCP.
 deb-2-9-cli -->

<!-- deb-2-9-ui
If you are enabling DHCP for the first time after adding a second rack controller, please read [Enabling DHCP](/t/managing-dhcp/2909#heading--enabling-dhcp).  On the other hand, if you have already enabled DHCP on your initial rack controller, you'll need to reconfigure DHCP.
 deb-2-9-ui -->

<!-- deb-3-0-cli
If you are enabling DHCP for the first time after adding a second rack controller, please read [Enabling DHCP](/t/managing-dhcp/4035#heading--enabling-dhcp).  On the other hand, if you have already enabled DHCP on your initial rack controller, you'll need to reconfigure DHCP.
 deb-3-0-cli -->

<!-- deb-3-0-ui
If you are enabling DHCP for the first time after adding a second rack controller, please read [Enabling DHCP](/t/managing-dhcp/4036#heading--enabling-dhcp).  On the other hand, if you have already enabled DHCP on your initial rack controller, you'll need to reconfigure DHCP.
 deb-3-0-ui -->

<!-- snap-2-7-cli
If you are enabling DHCP for the first time after adding a second rack controller, please read [Enabling DHCP](/t/managing-dhcp/2898#heading--enabling-dhcp).  On the other hand, if you have already enabled DHCP on your initial rack controller, you'll need to reconfigure DHCP.
 snap-2-7-cli -->

<!-- snap-2-7-ui
If you are enabling DHCP for the first time after adding a second rack controller, please read [Enabling DHCP](/t/managing-dhcp/2899#heading--enabling-dhcp).  On the other hand, if you have already enabled DHCP on your initial rack controller, you'll need to reconfigure DHCP.
 snap-2-7-ui -->

<!-- snap-2-8-cli
If you are enabling DHCP for the first time after adding a second rack controller, please read [Enabling DHCP](/t/managing-dhcp/2900#heading--enabling-dhcp).  On the other hand, if you have already enabled DHCP on your initial rack controller, you'll need to reconfigure DHCP.
 snap-2-8-cli -->

<!-- snap-2-8-ui
If you are enabling DHCP for the first time after adding a second rack controller, please read [Enabling DHCP](/t/managing-dhcp/2901#heading--enabling-dhcp).  On the other hand, if you have already enabled DHCP on your initial rack controller, you'll need to reconfigure DHCP.
 snap-2-8-ui -->

<!-- snap-2-9-cli
If you are enabling DHCP for the first time after adding a second rack controller, please read [Enabling DHCP](/t/managing-dhcp/2902#heading--enabling-dhcp).  On the other hand, if you have already enabled DHCP on your initial rack controller, you'll need to reconfigure DHCP.
 snap-2-9-cli -->

<!-- snap-2-9-ui
If you are enabling DHCP for the first time after adding a second rack controller, please read [Enabling DHCP](/t/managing-dhcp/2903#heading--enabling-dhcp).  On the other hand, if you have already enabled DHCP on your initial rack controller, you'll need to reconfigure DHCP.
 snap-2-9-ui -->

<!-- snap-3-0-cli
If you are enabling DHCP for the first time after adding a second rack controller, please read [Enabling DHCP](/t/managing-dhcp/4033#heading--enabling-dhcp).  On the other hand, if you have already enabled DHCP on your initial rack controller, you'll need to reconfigure DHCP.
 snap-3-0-cli -->

<!-- snap-3-0-ui
If you are enabling DHCP for the first time after adding a second rack controller, please read [Enabling DHCP](/t/managing-dhcp/4034#heading--enabling-dhcp).  On the other hand, if you have already enabled DHCP on your initial rack controller, you'll need to reconfigure DHCP.
 snap-3-0-ui -->

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
Access the appropriate VLAN (via the 'Subnets' page) and choose action 'Reconfigure DHCP'. There, you will see the second rack controller in the 'Secondary controller' field. All you should have to do is press the 'Reconfigure DHCP' button:

<a href="https://discourse.maas.io/uploads/default/original/1X/c2fe0e3d5a663ac7dda0ed33b7591c4a6dfaff20.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/c2fe0e3d5a663ac7dda0ed33b7591c4a6dfaff20.jpeg"></a>
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui  -->

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 
To reconfigure DHCP after adding a new rack controller, use the following sequence of commands:

```
vid=$(maas maas subnets read | jq -r '.[] | select(.cidr == "10.0.0.0/24") | .vlan.vid')
fabric_name=$(maas maas subnets read | jq -r '.[] | select(.cidr == "10.0.0.0/24") | .vlan.fabric')
query=".[] | select(.name == \"$fabric_name\") | .id"
fabric_id=$(maas maas fabrics read | jq "$query")
maas maas ipranges create type=reserved start_ip=10.0.0.3 end_ip=10.0.0.49
maas maas ipranges create type=dynamic start_ip=10.0.0.50 end_ip=10.0.0.99
maas maas vlan update ${fabric_id} ${vid} primary_rack=$(hostname) dhcp_on=true
```

Be sure to substitute the sample values for those of your own environment.
snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli  -->

<a href="#heading--multiple-region-endpoints"><h3 id="heading--multiple-region-endpoints">Configure multiple region endpoints</h3></a>

<!-- deb-2-7-ui deb-2-7-cli deb-2-8-ui deb-2-8-cli deb-2-9-ui deb-2-9-cli deb-3-0-cli deb-3-0-ui
MAAS will automatically discover and track all reachable region controllers in a single cluster of rack controllers  It will also attempt to automatically connect to them if the one in use becomes inaccessible.  Administrators can alternatively specify multiple region-controller endpoints for a single rack controller by adding entries to `/etc/maas/rackd.conf`.  For example:
deb-2-7-ui deb-2-7-cli deb-2-8-ui deb-2-8-cli deb-2-9-ui deb-2-9-cli deb-3-0-ui deb-3-0-cli  -->

<!-- snap-2-7-ui snap-2-7-cli snap-2-8-ui snap-2-8-cli snap-2-9-ui snap-2-9-cli snap-3-0-cli snap-3-0-ui
MAAS will automatically discover and track all reachable region controllers in a single cluster of rack controllers  It will also attempt to automatically connect to them if the one in use becomes inaccessible.  Administrators can alternatively specify multiple region-controller endpoints for a single rack controller by adding entries to `/var/snap/maas/current/rackd.conf`.  For example:
snap-2-7-ui snap-2-7-cli snap-2-8-ui snap-2-8-cli snap-2-9-ui snap-2-9-cli snap-3-0-ui snap-3-0-cli -->
    .
    .
    .
    maas_url:
      - http://<ip 1>:<port>/MAAS/
      - http://<ip 2>:<port>/MAAS/
    .
    .
    .

The setup of highly-available DHCP is now complete.  Note that, for HA purposes, DHCP provisioning will take into account multiple DNS services when there is more than one region controller on a single region.

<a href="#heading--region-controller-ha"><h2 id="heading--region-controller-ha">Make region controllers highly available</h2></a>

Implementing highly-available region control involves setting up two highly-available services:

1.   PostgreSQL HA
2.   Secondary API server(s)

Load balancing is optional, but is highly recommended.

<a href="#heading--postgresql-ha"><h3 id="heading--postgresql-ha">Enable highly-available PostgreSQL</h3></a>

MAAS stores all state information in the PostgreSQL database. It is therefore recommended to run it in HA mode. Configuring HA for PostgreSQL is external to MAAS. You will, therefore, need to study the [PostgreSQL documentation](https://www.postgresql.org/docs/9.5/static/high-availability.html) and implement the variant of HA that makes you feel most comfortable.

<!-- deb-2-7-cli
A quick treatment of [PostgreSQL HA: hot standby](/t/postgresql-ha-hot-standby/3000) is provided here for convenience only. This summary will give you an idea of the command line implementation of HA with PostgreSQL.
 deb-2-7-cli -->

<!-- deb-2-7-ui
A quick treatment of [PostgreSQL HA: hot standby](/t/postgresql-ha-hot-standby/3001) is provided here for convenience only. This summary will give you an idea of the command line implementation of HA with PostgreSQL.
 deb-2-7-ui -->

<!-- deb-2-8-cli
A quick treatment of [PostgreSQL HA: hot standby](/t/postgresql-ha-hot-standby/3002) is provided here for convenience only. This summary will give you an idea of the command line implementation of HA with PostgreSQL.
 deb-2-8-cli -->

<!-- deb-2-8-ui
A quick treatment of [PostgreSQL HA: hot standby](/t/postgresql-ha-hot-standby/3003) is provided here for convenience only. This summary will give you an idea of the command line implementation of HA with PostgreSQL.
 deb-2-8-ui -->

<!-- deb-2-9-cli
A quick treatment of [PostgreSQL HA: hot standby](/t/postgresql-ha-hot-standby/3004) is provided here for convenience only. This summary will give you an idea of the command line implementation of HA with PostgreSQL.
 deb-2-9-cli -->

<!-- deb-2-9-ui
A quick treatment of [PostgreSQL HA: hot standby](/t/postgresql-ha-hot-standby/3005) is provided here for convenience only. This summary will give you an idea of the command line implementation of HA with PostgreSQL.
 deb-2-9-ui -->

<!-- deb-3-0-cli
A quick treatment of [PostgreSQL HA: hot standby](/t/postgresql-ha-hot-standby/4067) is provided here for convenience only. This summary will give you an idea of the command line implementation of HA with PostgreSQL.
 deb-3-0-cli -->

<!-- deb-3-0-ui
A quick treatment of [PostgreSQL HA: hot standby](/t/postgresql-ha-hot-standby/4068) is provided here for convenience only. This summary will give you an idea of the command line implementation of HA with PostgreSQL.
 deb-3-0-ui -->

<!-- snap-2-7-cli
A quick treatment of [PostgreSQL HA: hot standby](/t/postgresql-ha-hot-standby/2994) is provided here for convenience only. This summary will give you an idea of the command line implementation of HA with PostgreSQL.
 snap-2-7-cli -->

<!-- snap-2-7-ui
A quick treatment of [PostgreSQL HA: hot standby](/t/postgresql-ha-hot-standby/2995) is provided here for convenience only. This summary will give you an idea of the command line implementation of HA with PostgreSQL.
 snap-2-7-ui -->

<!-- snap-2-8-cli
A quick treatment of [PostgreSQL HA: hot standby](/t/postgresql-ha-hot-standby/2996) is provided here for convenience only. This summary will give you an idea of the command line implementation of HA with PostgreSQL.
 snap-2-8-cli -->

<!-- snap-2-8-ui
A quick treatment of [PostgreSQL HA: hot standby](/t/postgresql-ha-hot-standby/2997) is provided here for convenience only. This summary will give you an idea of the command line implementation of HA with PostgreSQL.
 snap-2-8-ui -->

<!-- snap-2-9-cli
A quick treatment of [PostgreSQL HA: hot standby](/t/postgresql-ha-hot-standby/2998) is provided here for convenience only. This summary will give you an idea of the command line implementation of HA with PostgreSQL.
 snap-2-9-cli -->

<!-- snap-2-9-ui
A quick treatment of [PostgreSQL HA: hot standby](/t/postgresql-ha-hot-standby/2999) is provided here for convenience only. This summary will give you an idea of the command line implementation of HA with PostgreSQL.
 snap-2-9-ui -->

<!-- snap-3-0-cli
A quick treatment of [PostgreSQL HA: hot standby](/t/postgresql-ha-hot-standby/4065) is provided here for convenience only. This summary will give you an idea of the command line implementation of HA with PostgreSQL.
 snap-3-0-cli -->

<!-- snap-3-0-ui
A quick treatment of [PostgreSQL HA: hot standby](/t/postgresql-ha-hot-standby/4066) is provided here for convenience only. This summary will give you an idea of the command line implementation of HA with PostgreSQL.
 snap-3-0-ui -->

Each region controller uses up to 40 connections to PostgreSQL in high load situations. Running two region controllers requires no modifications to the `max_connections` in `postgresql.conf`. More than two region controllers require that `max_connections` be adjusted to add 40 more connections per added region controller.

<a href="#heading--secondary-api-servers"><h3 id="heading--secondary-api-servers">Enable highly-available API services</h3></a>

<!-- snap-2-7-cli
Setting up high-availability using snaps is relatively easy: 

1.  Set up PostgreSQL for high-availability as [explained above](/t/high-availability/2682#heading--postgresql-ha). PostgreSQL should run outside of the snap.
2.  [Install](/t/maas-installation/3318#heading--install-from-snap) the MAAS snap on each machine you intend to use as a rack or region controller. You'll need the MAAS shared secret, located here, `/var/snap/maas/common/maas/secret`, on the first region controller you set up.
3.  [Initialise the snap](/t/maas-installation/3318#heading--initialisation) as a `rack` or `region` controller. Note that if you intend to use a machine as a region controller, you'll need to tell MAAS how to access your PostgreSQL database host with the following arguments:
    -   `--database-host DATABASE_HOST`
    -   `--database-name DATABASE_NAME`
    -   `--database-user DATABASE_USER`
    -   `--database-pass DATABASE_PASS`
 snap-2-7-cli -->

<!-- snap-2-7-ui
Setting up high-availability using snaps is relatively easy: 

1.  Set up PostgreSQL for high-availability as [explained above](/t/high-availability/2683#heading--postgresql-ha). PostgreSQL should run outside of the snap.
2.  [Install](/t/maas-installation/3319#heading--install-from-snap) the MAAS snap on each machine you intend to use as a rack or region controller. You'll need the MAAS shared secret, located here, `/var/snap/maas/common/maas/secret`, on the first region controller you set up.
3.  [Initialise the snap](/t/maas-installation/3319#heading--initialisation) as a `rack` or `region` controller. Note that if you intend to use a machine as a region controller, you'll need to tell MAAS how to access your PostgreSQL database host with the following arguments:
    -   `--database-host DATABASE_HOST`
    -   `--database-name DATABASE_NAME`
    -   `--database-user DATABASE_USER`
    -   `--database-pass DATABASE_PASS`
 snap-2-7-ui -->

<!-- snap-2-8-cli
Setting up high-availability using snaps is relatively easy: 

1.  Set up PostgreSQL for high-availability as [explained above](/t/high-availability/2684#heading--postgresql-ha). PostgreSQL should run outside of the snap.
2.  [Install](/t/maas-installation/3320#heading--install-from-snap) the MAAS snap on each machine you intend to use as a rack or region controller. You'll need the MAAS shared secret, located here, `/var/snap/maas/common/maas/secret`, on the first region controller you set up.
3.  [Initialise the snap](/t/maas-installation/3320#heading--initialisation) as a `rack` or `region` controller. Note that if you intend to use a machine as a region controller, you'll need to tell MAAS how to access your PostgreSQL database host with the following four arguments:

1.   `--database-host DATABASE_HOST`
2.   `--database-name DATABASE_NAME`
3.   `--database-user DATABASE_USER`
4.   `--database-pass DATABASE_PASS`
 snap-2-8-cli -->

<!-- snap-2-8-ui
Setting up high-availability using snaps is relatively easy: 

1.  Set up PostgreSQL for high-availability as [explained above](/t/high-availability/2685#heading--postgresql-ha). PostgreSQL should run outside of the snap.
2.  [Install](/t/maas-installation/3321#heading--install-from-snap) the MAAS snap on each machine you intend to use as a rack or region controller. You'll need the MAAS shared secret, located here, `/var/snap/maas/common/maas/secret`, on the first region controller you set up.
3.  [Initialise the snap](/t/maas-installation/3321#heading--initialisation) as a `rack` or `region` controller. Note that if you intend to use a machine as a region controller, you'll need to tell MAAS how to access your PostgreSQL database host with the following four arguments:

1.   `--database-host DATABASE_HOST`
2.   `--database-name DATABASE_NAME`
3.   `--database-user DATABASE_USER`
4.   `--database-pass DATABASE_PASS`
 snap-2-8-ui -->

<!-- snap-2-9-cli
Setting up high-availability using snaps is relatively easy:

1.  Set up PostgreSQL for high-availability as [explained above](/t/high-availability/2686#heading--postgresql-ha). PostgreSQL should run outside of the snap.
2.  [Install](/t/maas-installation/3322#heading--install-from-snap) the MAAS snap on each machine you intend to use as a rack or region controller. You'll need the MAAS shared secret, located here, `/var/snap/maas/common/maas/secret`, on the first region controller you set up.
3.  [Initialise the snap](/t/maas-installation/3322#heading--initialisation) as a `rack` or `region` controller. Note that if you intend to use a machine as a region controller, you'll need to tell MAAS how to access your PostgreSQL database host with the following four arguments:

1.   `--database-host DATABASE_HOST`
2.   `--database-name DATABASE_NAME`
3.   `--database-user DATABASE_USER`
4.   `--database-pass DATABASE_PASS`
 snap-2-9-cli -->

<!-- snap-2-9-ui
Setting up high-availability using snaps is relatively easy: 

1.  Set up PostgreSQL for high-availability as [explained above](/t/high-availability/2687#heading--postgresql-ha). PostgreSQL should run outside of the snap.
2.  [Install](/t/maas-installation/3323#heading--install-from-snap) the MAAS snap on each machine you intend to use as a rack or region controller. You'll need the MAAS shared secret, located here, `/var/snap/maas/common/maas/secret`, on the first region controller you set up.
3.  [Initialise the snap](/t/maas-installation/3323#heading--initialisation) as a `rack` or `region` controller. Note that if you intend to use a machine as a region controller, you'll need to tell MAAS how to access your PostgreSQL database host with the following four arguments:

1.   `--database-host DATABASE_HOST`
2.   `--database-name DATABASE_NAME`
3.   `--database-user DATABASE_USER`
4.   `--database-pass DATABASE_PASS`
 snap-2-9-ui -->

<!-- snap-3-0-cli
Setting up high-availability using snaps is relatively easy:

1.  Set up PostgreSQL for high-availability as [explained above](/t/high-availability/3945#heading--postgresql-ha). PostgreSQL should run outside of the snap.
2.  [Install](/t/maas-installation/4001#heading--install-from-snap) the MAAS snap on each machine you intend to use as a rack or region controller. You'll need the MAAS shared secret, located here, `/var/snap/maas/common/maas/secret`, on the first region controller you set up.
3.  [Initialise the snap](/t/maas-installation/4001#heading--initialisation) as a `rack` or `region` controller. Note that if you intend to use a machine as a region controller, you'll need to tell MAAS how to access your PostgreSQL database host with the following four arguments:

1.   `--database-host DATABASE_HOST`
2.   `--database-name DATABASE_NAME`
3.   `--database-user DATABASE_USER`
4.   `--database-pass DATABASE_PASS`
 snap-3-0-cli -->

<!-- snap-3-0-ui
Setting up high-availability using snaps is relatively easy: 

1.  Set up PostgreSQL for high-availability as [explained above](/t/high-availability/3946#heading--postgresql-ha). PostgreSQL should run outside of the snap.
2.  [Install](/t/maas-installation/4002#heading--install-from-snap) the MAAS snap on each machine you intend to use as a rack or region controller. You'll need the MAAS shared secret, located here, `/var/snap/maas/common/maas/secret`, on the first region controller you set up.
3.  [Initialise the snap](/t/maas-installation/4002#heading--initialisation) as a `rack` or `region` controller. Note that if you intend to use a machine as a region controller, you'll need to tell MAAS how to access your PostgreSQL database host with the following four arguments:

1.   `--database-host DATABASE_HOST`
2.   `--database-name DATABASE_NAME`
3.   `--database-user DATABASE_USER`
4.   `--database-pass DATABASE_PASS`
 snap-3-0-ui -->

<!-- deb-2-7-cli
Please see [Region controllers](/t/region-controllers/3072) and [Multiple region endpoints](#heading--multiple-region-endpoints) for more information about how to install and configure rack controllers for multiple region controllers.
 deb-2-7-cli -->

<!-- deb-2-7-ui
Please see [Region controllers](/t/region-controllers/3073) and [Multiple region endpoints](#heading--multiple-region-endpoints) for more information about how to install and configure rack controllers for multiple region controllers.
 deb-2-7-ui -->

<!-- deb-2-8-cli
Please see [Region controllers](/t/region-controllers/3074) and [Multiple region endpoints](#heading--multiple-region-endpoints) for more information about how to install and configure rack controllers for multiple region controllers.
 deb-2-8-cli -->

<!-- deb-2-8-ui
Please see [Region controllers](/t/region-controllers/3075) and [Multiple region endpoints](#heading--multiple-region-endpoints) for more information about how to install and configure rack controllers for multiple region controllers.
 deb-2-8-ui -->

<!-- deb-2-9-cli
Please see [Region controllers](/t/region-controllers/3076) and [Multiple region endpoints](#heading--multiple-region-endpoints) for more information about how to install and configure rack controllers for multiple region controllers.
 deb-2-9-cli -->

<!-- deb-2-9-ui
Please see [Region controllers](/t/region-controllers/3077) and [Multiple region endpoints](#heading--multiple-region-endpoints) for more information about how to install and configure rack controllers for multiple region controllers.
 deb-2-9-ui -->

<!-- deb-3-0-cli
Please see [Region controllers](/t/region-controllers/4095) and [Multiple region endpoints](#heading--multiple-region-endpoints) for more information about how to install and configure rack controllers for multiple region controllers.
 deb-3-0-cli -->

<!-- deb-3-0-ui
Please see [Region controllers](/t/region-controllers/4096) and [Multiple region endpoints](#heading--multiple-region-endpoints) for more information about how to install and configure rack controllers for multiple region controllers.
 deb-3-0-ui -->

<a href="#heading--load-balancing-with-haproxy-optional"><h3 id="heading--load-balancing-with-haproxy-optional">Load balancing with HAProxy (optional)</h3></a>

You can add load balancing with [HAProxy](http://www.haproxy.org/) load-balancing software to support multiple API servers. In this setup, HAProxy provides access to the MAAS web UI and API.

[note]
If you happen to have Apache running on the same server where you intend to install HAProxy, you will need to stop and disable `apache2`, because HAProxy binds to port 80.
[/note]

<a href="#heading--install"><h4 id="heading--install">Install</h4></a>

``` bash
sudo apt install haproxy
```

<a href="#heading--configure"><h4 id="heading--configure">Configure</h4></a>

Configure each API server's load balancer by copying the following into `/etc/haproxy/haproxy.cfg` (see the [upstream configuration manual (external link)](http://cbonte.github.io/haproxy-dconv/1.6/configuration.html) as a reference). Replace $PRIMARY_API_SERVER_IP and $SECONDARY_API_SERVER_IP with their respective IP addresses:

``` yaml
frontend maas
    bind    *:80
    retries 3
    option  redispatch
    option  http-server-close
    default_backend maas

backend maas
    timeout server 90s
    balance source
    hash-type consistent
    server localhost localhost:5240 check
    server maas-api-1 $PRIMARY_API_SERVER_IP:5240 check
    server maas-api-2 $SECONDARY_API_SERVER_IP:5240 check
```

where `maas-api-1` and `maas-api-2` are arbitrary server labels.

Now restart the load balancer to have these changes take effect:

``` bash
sudo systemctl restart haproxy
```

The configuration of region controller HA is now complete.

**The API server(s) must be now be referenced (e.g. web UI, MAAS CLI) using port 80 (as opposed to port 5240).**

<a href="#heading--move-rack-controller"><h2 id="heading--move-rack-controller">Move a rack controller from one MAAS instance to another</h2></a>

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
In effect, there is no such action as moving a rack controller, although you can delete a rack controller from one MAAS and reinstantiate the same controller (binary-wise) on another MAAS instance.  First, delete the rack controller.  In the "Controllers" tab in the UI, select the rack controller you with to delete, choose "Take action" and select "Delete."  You will be asked to confirm with a red button, entitled "Delete 1 controller."
 snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui  -->

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 
In effect, there is no such action as moving a rack controller, although you can delete a rack controller from one MAAS and reinstantiate the same controller (binary-wise) on another MAAS instance.  First, delete the rack controller, with the command:

```
maas $PROFILE rack-controller delete $SYSTEM_ID
```

where `$PROFILE` is your admin profile name, and `$SYSTEM_ID` can be found by examining the output of the command:

```
maas $PROFILE rack-controllers read
```

There is no confirmation step, so make sure you have the right rack controller before proceeding.
 snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli  -->

Next, you must register a new rack controller, which is always done from the command line.

<!-- deb-2-7-ui deb-2-7-cli deb-2-8-ui deb-2-8-cli deb-2-9-ui deb-2-9-cli deb-3-0-ui deb-3-0-cli 
For this exercise, we're assuming you are using the already installed rack controller code that was previously running on the "from" MAAS instance.  All that's necessary is that you register a new rack controller with the "to" MAAS instance, like this:

```
sudo maas-rack register --url $MAAS_URL_OF_NEW_MAAS --secret $SECRET_FOR_NEW_MAAS
```

where the secret is found in `/var/lib/maas/secret`.
 deb-2-7-ui deb-2-7-cli deb-2-8-ui deb-2-8-cli deb-2-9-ui deb-2-9-cli deb-3-0-ui deb-3-0-cli  -->

<!-- snap-2-7-ui snap-2-7-cli snap-2-8-ui snap-2-8-cli snap-2-9-ui snap-2-9-cli snap-3-0-ui snap-3-0-cli
For this exercise, we're assuming you are using the already installed rack controller code that was previously running on the "from" MAAS instance.  All that's necessary is that you register a new rack controller with the "to" MAAS instance, like this:

```
sudo maas init rack --maas-url $MAAS_URL_OF_NEW_MAAS --secret $SECRET_FOR_NEW_MAAS
```

where the secret is found in `/var/snap/maas/common/maas/secret`.
 snap-2-7-ui snap-2-7-cli snap-2-8-ui snap-2-8-cli snap-2-9-ui snap-2-9-cli snap-3-0-ui snap-3-0-cli-->

<!-- deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-2-7-ui snap-2-8-ui snap-2-9-ui snap-3-0-ui deb-3-0-ui 
Note that in the UI, if you go to the "Controllers" tab and press the button entitled, "Add rack controller," at the top of the Controllers screen, MAAS will give you a complete command string, including the correct URL and secret values.  Simply cut and paste that string to move the rack controller, paying attention to whether you are using snap or package build modes.
 deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-2-7-ui snap-2-8-ui snap-2-9-ui snap-3-0-ui deb-3-0-ui  -->

<a href="#heading--move-rack-controller"><h3 id="heading--dangers-moving-rack-controller">Dangers of moving a rack controller</h3></a>

There are dangers associate with moving a rack controller -- dangers that may generate errors, get you into a non-working state, or cause you significant data loss.  These dangers are precipitated by one caveat and two potential mistakes:

* **Using the same system as a rack controller and a VM host:** While not forbidden or inherently dangerous, using the same machine as both a rack controller and a VM host may cause resource contention and poor performance.  If the resources on the system are not more than adequate to cover both tasks, you may see slowdowns (or even apparent "freeze" events) on the system.

* **Moving a rack controller from one version of MAAS to another:** MAAS rack controller software is an integral part of each version of MAAS.  If you delete a rack controller from, say, a 2.6 version of MAAS, and attempt to register that 2.6 version of the rack controller code to, say, a 2.9 version of MAAS, you may experience errors and potential data loss.  Using the above example, if you are running both a VM host and a rack controller for MAAS 2.6 on one system, and you suddenly decide to delete that rack controller from 2.6 and attempt to register the same code to a 2.9 MAAS, the VM host may fail or disappear.  This will possibly delete all the VMs you have created or connected to that VM host -- which may result in data loss.  This action is not supported.

* **Connecting one instance of a rack controller to two instances of MAAS, regardless of version:** Trying to connect a single rack controller to two different instances of MAAS can result in all sorts of unpredictable (and potentially catastrophic) behavior.  It is not a supported configuration.

Take these warnings to heart.  It may seem like a faster approach to "bridge" your existing rack controllers from one MAAS to another -- or from one version of MAAS to another -- while they're running.  Ultimately, though, it will probably result in more work than just following the recommended approach.
