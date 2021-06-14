||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/maas-requirements-snap-2-7-cli/2874) ~ [UI](/t/maas-requirements-snap-2-7-ui/2875)|[CLI](/t/maas-requirements-snap-2-8-cli/2876) ~ [UI](/t/maas-requirements-snap-2-8-ui/2877)|[CLI](/t/maas-requirements-snap-2-9-cli/2878) ~ [UI](/t/maas-requirements-snap-2-9-ui/2879)|[CLI](/t/maas-requirements-snap-3-0-cli/4013) ~ [UI](/t/maas-requirements-snap-3-0-ui/4014)|
Packages|[CLI](/t/maas-requirements-deb-2-7-cli/2880) ~ [UI](/t/maas-requirements-deb-2-7-ui/2881)|[CLI](/t/maas-requirements-deb-2-8-cli/2882) ~ [UI](/t/maas-requirements-deb-2-8-ui/2883)|[CLI](/t/maas-requirements-deb-2-9-cli/2884) ~ [UI](/t/maas-requirements-deb-2-9-ui/2885)|[CLI](/t/maas-requirements-deb-3-0-cli/4015) ~ [UI](/t/maas-requirements-deb-3-0-ui/4016)|

The minimum requirements for the machines that run MAAS vary widely depending on local implementation and usage.  Below, you will find resource estimates based on MAAS components and operating system (Ubuntu Server). We consider both a test configuration (for proof of concept) and a production environment.

#### Two questions you might have:

1. [What are the requirements for a test environment?](#heading--test-environment)
2. [What are the requirements for a production environment?](#heading--production-environment)

<a href="#heading--test-environment"><h2 id="heading--test-environment">Requirements for a test environment</h2></a>

Here is a proof-of-concept scenario, with all MAAS components installed on a single host. This scenario assumes two complete sets of images (latest two Ubuntu LTS releases) for a single architecture (amd64).

| | Memory (MB) | CPU (GHz) | Disk (GB) |
|:-----|-----:|-----:|-----:|
| [Region controller](/t/concepts-and-terms/785#heading--controllers) (minus PostgreSQL) | 512 | 0.5 | 5 |
| PostgreSQL | 512 | 0.5 | 5 |
| [Rack controller](/t/concepts-and-terms/785#heading--controllers") | 512 | 0.5 | 5 |
| Ubuntu Server (including logs)| 512 | 0.5 | 5 |

Based on this table, the approximate requirements for this scenario are 2 GB memory, 2 GHz CPU, and 20 GB of disk space.

<a href="#heading--production-environment"><h2 id="heading--production-environment">Requirements for a production environment</h2></a>

Here is a production scenario designed to handle a high number of sustained client connections. This scenario implements both high availability (region and rack) and load balancing (region). MAAS reserves extra space for images (database and rack controller), while some images, such as those for Microsoft Windows, may require a lot more -- so plan accordingly.

| | Memory (MB) | CPU (GHz) | Disk (GB) |
|:-----|-----:|-----:|-----:|
| [Region controller](/t/concepts-and-terms/785#heading--controllers) (minus PostgreSQL) | 2048 | 2.0 | 5 |
| PostgreSQL | 2048 | 2.0 | 20 |
| [Rack controller](/t/concepts-and-terms/785#heading--controllers") | 2048 | 2.0 | 20 |
| Ubuntu Server (including logs)| 512 | 0.5 | 5 |

So, based on the above, the approximate requirements for this scenario are:

1. A region controller (including PostgreSQL) installed on one host, with 4.5 GB memory, 4.5 GHz CPU, and 45 GB of disk space.
2. A duplicate region controller (including PostgreSQL) on a second host, also with 4.5 GB memory, 4.5 GHz CPU, and 45 GB of disk space.
3. A rack controller installed on a third host, with 2.5 GB memory, 2.5 GHz CPU, and 40 GB of disk space.
4. A duplicate rack controller on a fourth host, also with 2.5 GB memory, 2.5 GHz CPU, and 40 GB of disk space.

<!-- deb-2-7-cli
[note]
The tables above refer to MAAS infrastructure only. They do not cover the resources needed by subsequently-added nodes. Note that machines should have IPMI-based BMC controllers for power cycling, see [Power management](/t/power-management/3012) for more details.
[/note]

Some examples of factors that influence hardware specifications include:

1. the number of connecting clients (client activity)
2. how you decide to distribute services
3. whether or not you use [high availability/load balancing](/t/high-availability/2588).
4. the number of images that you choose to store (disk space affecting PostgreSQL and the rack controller)
 deb-2-7-cli -->

<!-- deb-2-7-ui
[note]
The tables above refer to MAAS infrastructure only. They do not cover the resources needed by subsequently-added nodes. Note that machines should have IPMI-based BMC controllers for power cycling, see [Power management](/t/power-management/3013) for more details.
[/note]

Some examples of factors that influence hardware specifications include:

1. the number of connecting clients (client activity)
2. how you decide to distribute services
3. whether or not you use [high availability/load balancing](/t/high-availability/2689).
4. the number of images that you choose to store (disk space affecting PostgreSQL and the rack controller)
 deb-2-7-ui -->

<!-- deb-2-8-cli
[note]
The tables above refer to MAAS infrastructure only. They do not cover the resources needed by subsequently-added nodes. Note that machines should have IPMI-based BMC controllers for power cycling, see [Power management](/t/power-management/3014) for more details.
[/note]

Some examples of factors that influence hardware specifications include:

1. the number of connecting clients (client activity)
2. how you decide to distribute services
3. whether or not you use [high availability/load balancing](/t/high-availability/2690).
4. the number of images that you choose to store (disk space affecting PostgreSQL and the rack controller)
 deb-2-8-cli -->

<!-- deb-2-8-ui
[note]
The tables above refer to MAAS infrastructure only. They do not cover the resources needed by subsequently-added nodes. Note that machines should have IPMI-based BMC controllers for power cycling, see [Power management](/t/power-management/3015) for more details.
[/note]

Some examples of factors that influence hardware specifications include:

1. the number of connecting clients (client activity)
2. how you decide to distribute services
3. whether or not you use [high availability/load balancing](/t/high-availability/2691).
4. the number of images that you choose to store (disk space affecting PostgreSQL and the rack controller)
 deb-2-8-ui -->

<!-- deb-2-9-cli
[note]
The tables above refer to MAAS infrastructure only. They do not cover the resources needed by subsequently-added nodes. Note that machines should have IPMI-based BMC controllers for power cycling, see [Power management](/t/power-management/3016) for more details.
[/note]

Some examples of factors that influence hardware specifications include:

1. the number of connecting clients (client activity)
2. how you decide to distribute services
3. whether or not you use [high availability/load balancing](/t/high-availability/2692).
4. the number of images that you choose to store (disk space affecting PostgreSQL and the rack controller)
 deb-2-9-cli -->

<!-- deb-2-9-ui
[note]
The tables above refer to MAAS infrastructure only. They do not cover the resources needed by subsequently-added nodes. Note that machines should have IPMI-based BMC controllers for power cycling, see [Power management](/t/power-management/3017) for more details.
[/note]

Some examples of factors that influence hardware specifications include:

1. the number of connecting clients (client activity)
2. how you decide to distribute services
3. whether or not you use [high availability/load balancing](/t/high-availability/2693).
4. the number of images that you choose to store (disk space affecting PostgreSQL and the rack controller)
 deb-2-9-ui -->

<!-- deb-3-0-cli
[note]
The tables above refer to MAAS infrastructure only. They do not cover the resources needed by subsequently-added nodes. Note that machines should have IPMI-based BMC controllers for power cycling, see [Power management](/t/power-management/4071) for more details.
[/note]

Some examples of factors that influence hardware specifications include:

1. the number of connecting clients (client activity)
2. how you decide to distribute services
3. whether or not you use [high availability/load balancing](/t/high-availability/3947).
4. the number of images that you choose to store (disk space affecting PostgreSQL and the rack controller)
 deb-3-0-cli -->

<!-- deb-3-0-ui
[note]
The tables above refer to MAAS infrastructure only. They do not cover the resources needed by subsequently-added nodes. Note that machines should have IPMI-based BMC controllers for power cycling, see [Power management](/t/power-management/4070) for more details.
[/note]

Some examples of factors that influence hardware specifications include:

1. the number of connecting clients (client activity)
2. how you decide to distribute services
3. whether or not you use [high availability/load balancing](/t/high-availability/3948).
4. the number of images that you choose to store (disk space affecting PostgreSQL and the rack controller)
 deb-3-0-ui -->

<!-- snap-2-7-cli
[note]
The tables above refer to MAAS infrastructure only. They do not cover the resources needed by subsequently-added nodes. Note that machines should have IPMI-based BMC controllers for power cycling, see [Power management](/t/power-management/3006) for more details.
[/note]

Some examples of factors that influence hardware specifications include:

1. the number of connecting clients (client activity)
2. how you decide to distribute services
3. whether or not you use [high availability/load balancing](/t/high-availability/2682).
4. the number of images that you choose to store (disk space affecting PostgreSQL and the rack controller)
 snap-2-7-cli -->

<!-- snap-2-7-ui
[note]
The tables above refer to MAAS infrastructure only. They do not cover the resources needed by subsequently-added nodes. Note that machines should have IPMI-based BMC controllers for power cycling, see [Power management](/t/power-management/3007) for more details.
[/note]

Some examples of factors that influence hardware specifications include:

1. the number of connecting clients (client activity)
2. how you decide to distribute services
3. whether or not you use [high availability/load balancing](/t/high-availability/2683).
4. the number of images that you choose to store (disk space affecting PostgreSQL and the rack controller)
 snap-2-7-ui -->

<!-- snap-2-8-cli
[note]
The tables above refer to MAAS infrastructure only. They do not cover the resources needed by subsequently-added nodes. Note that machines should have IPMI-based BMC controllers for power cycling, see [Power management](/t/power-management/3008) for more details.
[/note]

Some examples of factors that influence hardware specifications include:

1. the number of connecting clients (client activity)
2. how you decide to distribute services
3. whether or not you use [high availability/load balancing](/t/high-availability/2684).
4. the number of images that you choose to store (disk space affecting PostgreSQL and the rack controller)
 snap-2-8-cli -->

<!-- snap-2-8-ui
[note]
The tables above refer to MAAS infrastructure only. They do not cover the resources needed by subsequently-added nodes. Note that machines should have IPMI-based BMC controllers for power cycling, see [Power management](/t/power-management/3009) for more details.
[/note]

Some examples of factors that influence hardware specifications include:

1. the number of connecting clients (client activity)
2. how you decide to distribute services
3. whether or not you use [high availability/load balancing](/t/high-availability/2685).
4. the number of images that you choose to store (disk space affecting PostgreSQL and the rack controller)
 snap-2-8-ui -->

<!-- snap-2-9-cli
[note]
The tables above refer to MAAS infrastructure only. They do not cover the resources needed by subsequently-added nodes. Note that machines should have IPMI-based BMC controllers for power cycling, see [Power management](/t/power-management/3010) for more details.
[/note]

Some examples of factors that influence hardware specifications include:

1. the number of connecting clients (client activity)
2. how you decide to distribute services
3. whether or not you use [high availability/load balancing](/t/high-availability/2686).
4. the number of images that you choose to store (disk space affecting PostgreSQL and the rack controller)
 snap-2-9-cli -->

<!-- snap-2-9-ui
[note]
The tables above refer to MAAS infrastructure only. They do not cover the resources needed by subsequently-added nodes. Note that machines should have IPMI-based BMC controllers for power cycling, see [Power management](/t/power-management/3011) for more details.
[/note]

Some examples of factors that influence hardware specifications include:

1. the number of connecting clients (client activity)
2. how you decide to distribute services
3. whether or not you use [high availability/load balancing](/t/high-availability/2687).
4. the number of images that you choose to store (disk space affecting PostgreSQL and the rack controller)
 snap-2-9-ui -->

<!-- snap-3-0-cli
[note]
The tables above refer to MAAS infrastructure only. They do not cover the resources needed by subsequently-added nodes. Note that machines should have IPMI-based BMC controllers for power cycling, see [Power management](/t/power-management/4069) for more details.
[/note]

Some examples of factors that influence hardware specifications include:

1. the number of connecting clients (client activity)
2. how you decide to distribute services
3. whether or not you use [high availability/load balancing](/t/high-availability/3945).
4. the number of images that you choose to store (disk space affecting PostgreSQL and the rack controller)
 snap-3-0-cli -->

<!-- snap-3-0-ui
[note]
The tables above refer to MAAS infrastructure only. They do not cover the resources needed by subsequently-added nodes. Note that machines should have IPMI-based BMC controllers for power cycling, see [Power management](/t/power-management/4070) for more details.
[/note]

Some examples of factors that influence hardware specifications include:

1. the number of connecting clients (client activity)
2. how you decide to distribute services
3. whether or not you use [high availability/load balancing](/t/high-availability/3946).
4. the number of images that you choose to store (disk space affecting PostgreSQL and the rack controller)
 snap-3-0-ui -->

Also, this discussion does not take into account a possible local image mirror, which would be a large consumer of disk space.

One rack controller should only service 1000 machines or less, regardless of how you distribute them across subnets. There is no load balancing at the rack level, so you will need additional, independent rack controllers. Each controller must service its own subnet(s).
