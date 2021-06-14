||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/using-rbac-with-maas-snap-2-7-cli/3592) ~ [UI](/t/using-rbac-with-maas-snap-2-7-ui/3593)|[CLI](/t/using-rbac-with-maas-snap-2-8-cli/3594) ~ [UI](/t/using-rbac-with-maas-snap-2-8-ui/3595)|[CLI](/t/using-rbac-with-maas-snap-2-9-cli/3596) ~ [UI](/t/using-rbac-with-maas-snap-2-9-ui/3597)|[CLI](/t/using-rbac-with-maas-snap-3-0-cli/4157) ~ [UI](/t/using-rbac-with-maas-snap-3-0-ui/4158)|
Packages|[CLI](/t/using-rbac-with-maas-deb-2-7-cli/3598) ~ [UI](/t/using-rbac-with-maas-deb-2-7-ui/3599)|[CLI](/t/using-rbac-with-maas-deb-2-8-cli/3600) ~ [UI](/t/using-rbac-with-maas-deb-2-8-ui/3601)|[CLI](/t/using-rbac-with-maas-deb-2-9-cli/3602) ~ [UI](/t/using-rbac-with-maas-deb-2-9-ui/3603)|[CLI](/t/using-rbac-with-maas-deb-3-0-cli/4159) ~ [UI](/t/using-rbac-with-maas-deb-3-0-ui/4160)|

This page is a draft reference for using RBAC with MAAS.  It is currently in an incomplete state, but feel free to benefit from whatever is here as this page develops.  A discourse announcement will be made when this page has reached a minimally usable state.

Not sure what part of the UbuntuSSO, etc., internal-looking-type stuff can actually be published to the general user population.

<a href="#heading--candid"><big>Candid</big></a>

Candid is an identity service which extends macaroon-based authentication. The candid service is important in configuring RBAC for MAAS, so you may want to review this [brief tutorial].


<a href="#heading--rbac"><h2 id="heading--rbac">RBAC</h2></a>

<a href="#heading--ldap"><h2 id="heading--ldap">LDAP</h2></a>

LDAP (Lightweight Directory Access Protocol) is a hierarchical storage and retrieval system based on a directory structure, much like the old telephone books.  LDAP can really store information about anything that can be described with attributes -- that is, `key=value` pairs -- but it's most commonly used to store information about an organization, its assets, and its users.

You can install and configure LDAP on one or more systems, in the sense that OpenLDAP consists of two parts, the LDAP server and the LDAP client.  They can both run on the same system, or the server can run on one system and the client on multiple systems.  The Ubuntu OpenLDAP protocol is one potential authorisation tool that can be integrated with MAAS, so we'll cover how to set it up here, and explain how to integrate it with MAAS in the next section.

<a href="#heading--installing-ldap-server"><h3 id="heading--installing-ldap-server">Installing and configuring the OpenLDAP server</h3></a>

In this example, we're going to install the LDAP server on `stormrider.io` and the client on a localhost named `wintermute` -- but you can install them wherever it suits you, even on the same physical machine, without losing any of the tutorial value.

To install the OpenLDAP server, execute the following commands:

```
sudo apt update
```

This command, which should always be executed before installing packages, makes sure to update the list of repositories to the most current state.  Doing so will usually prevent you from being unable to find the package you're looking for -- unless it resides in a private PPA (not the case here).

<details><summary>Typical output</summary>
Hit:1 http://archive.ubuntu.com/ubuntu bionic InRelease
Get:2 http://security.ubuntu.com/ubuntu bionic-security InRelease [88.7 kB]
Get:3 http://archive.ubuntu.com/ubuntu bionic-updates InRelease [88.7 kB]           
Get:4 http://security.ubuntu.com/ubuntu bionic-security/main amd64 Packages [1572 kB]
Get:5 http://archive.ubuntu.com/ubuntu bionic-backports InRelease [74.6 kB]       
Get:6 http://archive.ubuntu.com/ubuntu bionic/universe amd64 Packages [8570 kB]             
Get:7 http://security.ubuntu.com/ubuntu bionic-security/restricted amd64 Packages [245 kB]
Get:8 http://security.ubuntu.com/ubuntu bionic-security/restricted Translation-en [31.7 kB]
Get:9 http://security.ubuntu.com/ubuntu bionic-security/universe amd64 Packages [1113 kB]       
Get:10 http://security.ubuntu.com/ubuntu bionic-security/universe Translation-en [249 kB]      
Get:11 http://security.ubuntu.com/ubuntu bionic-security/multiverse amd64 Packages [19.1 kB]     
Get:12 http://security.ubuntu.com/ubuntu bionic-security/multiverse Translation-en [4412 B]        
Get:13 http://archive.ubuntu.com/ubuntu bionic/universe Translation-en [4941 kB]                        
Get:14 http://archive.ubuntu.com/ubuntu bionic/multiverse amd64 Packages [151 kB]                       
Get:15 http://archive.ubuntu.com/ubuntu bionic/multiverse Translation-en [108 kB]                       
Get:16 http://archive.ubuntu.com/ubuntu bionic-updates/main amd64 Packages [1913 kB]                    
Get:17 http://archive.ubuntu.com/ubuntu bionic-updates/restricted amd64 Packages [266 kB]               
Get:18 http://archive.ubuntu.com/ubuntu bionic-updates/restricted Translation-en [35.3 kB]              
Get:19 http://archive.ubuntu.com/ubuntu bionic-updates/universe amd64 Packages [1719 kB]                
Get:20 http://archive.ubuntu.com/ubuntu bionic-updates/universe Translation-en [363 kB]                 
Get:21 http://archive.ubuntu.com/ubuntu bionic-updates/multiverse amd64 Packages [24.9 kB]              
Get:22 http://archive.ubuntu.com/ubuntu bionic-updates/multiverse Translation-en [6464 B]               
Get:23 http://archive.ubuntu.com/ubuntu bionic-backports/main amd64 Packages [10.0 kB]                  
Get:24 http://archive.ubuntu.com/ubuntu bionic-backports/main Translation-en [4764 B]                   
Get:25 http://archive.ubuntu.com/ubuntu bionic-backports/universe amd64 Packages [10.3 kB]              
Get:26 http://archive.ubuntu.com/ubuntu bionic-backports/universe Translation-en [4588 B]               
Fetched 21.6 MB in 16s (1334 kB/s)                                                                      
Reading package lists... Done
Building dependency tree       
Reading state information... Done
6 packages can be upgraded. Run 'apt list --upgradable' to see them.
</details>

Once you know that you've got the most current repositories in view, you can install the LDAP server like this:


```
sudo apt install slapd ldap-utils
```

Soon after the install begins, you'll be presented with a dialog box to enter and confirm the LDAP administrator password; choose it wisely and remember it.  Aside from the dialog box, the typical output is shown in the detail section below.

<details><summary>Typical output</summary>
ading package lists... Done
Building dependency tree       
Reading state information... Done
The following package was automatically installed and is no longer required:
  libfreetype6
Use 'sudo apt autoremove' to remove it.
The following additional packages will be installed:
  libltdl7 libodbc1
Suggested packages:
  libsasl2-modules-gssapi-mit | libsasl2-modules-gssapi-heimdal libmyodbc odbc-postgresql tdsodbc
  unixodbc-bin
The following NEW packages will be installed:
  ldap-utils libltdl7 libodbc1 slapd
0 upgraded, 4 newly installed, 0 to remove and 6 not upgraded.
Need to get 1731 kB of archives.
After this operation, 17.6 MB of additional disk space will be used.
Do you want to continue? [Y/n] Y
Get:1 http://archive.ubuntu.com/ubuntu bionic/main amd64 libltdl7 amd64 2.4.6-2 [38.8 kB]
Get:2 http://archive.ubuntu.com/ubuntu bionic/main amd64 libodbc1 amd64 2.3.4-1.1ubuntu3 [183 kB]
Get:3 http://archive.ubuntu.com/ubuntu bionic-updates/main amd64 slapd amd64 2.4.45+dfsg-1ubuntu1.10 [1385 kB]
Get:4 http://archive.ubuntu.com/ubuntu bionic-updates/main amd64 ldap-utils amd64 2.4.45+dfsg-1ubuntu1.10 [124 kB]
Fetched 1731 kB in 3s (640 kB/s)   
Preconfiguring packages ...
Selecting previously unselected package libltdl7:amd64.
(Reading database ... 28762 files and directories currently installed.)
Preparing to unpack .../libltdl7_2.4.6-2_amd64.deb ...
Unpacking libltdl7:amd64 (2.4.6-2) ...
Selecting previously unselected package libodbc1:amd64.
Preparing to unpack .../libodbc1_2.3.4-1.1ubuntu3_amd64.deb ...
Unpacking libodbc1:amd64 (2.3.4-1.1ubuntu3) ...
Selecting previously unselected package slapd.
Preparing to unpack .../slapd_2.4.45+dfsg-1ubuntu1.10_amd64.deb ...
Unpacking slapd (2.4.45+dfsg-1ubuntu1.10) ...
Selecting previously unselected package ldap-utils.
Preparing to unpack .../ldap-utils_2.4.45+dfsg-1ubuntu1.10_amd64.deb ...
Unpacking ldap-utils (2.4.45+dfsg-1ubuntu1.10) ...
Setting up ldap-utils (2.4.45+dfsg-1ubuntu1.10) ...
Setting up libltdl7:amd64 (2.4.6-2) ...
Setting up libodbc1:amd64 (2.3.4-1.1ubuntu3) ...
Setting up slapd (2.4.45+dfsg-1ubuntu1.10) ...
  Creating new user openldap... done.
  Creating initial configuration... done.
  Creating LDAP directory... done.
Processing triggers for ufw (0.36-0ubuntu0.18.04.1) ...
Processing triggers for ureadahead (0.100.0-21) ...
Processing triggers for libc-bin (2.27-3ubuntu1.4) ...
Processing triggers for systemd (237-3ubuntu10.44) ...
Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
</details>

By the way, `slapd` stands for "Standalone LDAP Daemon," also known as the LDAP server.

Even though `slapd` is running with some default values, it's a good idea to at least review (and possibly reset) some of those values to match your own particular environment.  You can do this by running `dpkg-reconfigure`:

```
sudo dpkg-reconfigure slapd
```

Doing so leads to a series of ASCII dialog panels whose recommended answers are given below:

* Omit OpenLDAP server configuration? - No
* DNS domain name - Provide your DNS domain name, which will be used to construct the base DN. In this example, we’ll `stormrider.io`
* Organization name - Something to identify your organization, for example “maasteam”
* Administrator password: This is the same password you already provided before, enter it again (or choose a new one), and confirm it.
* Database format - select the default MDB
* Do you want the database to be removed when slapd is purged? - For test environments, then “Yes” is fine. For production, answer “No”
* Move the old database? - Same recommendation as previous question

```
BASE	dc=stormrider,dc=io
URI	ldap://ldap.wintermute.com
```

<a href="#heading--populate-ldap"><h3 id="heading--populate-ldap">Populating LDAP with sample data</h3></a>

The next step is adding some content to the LDAP database.  It's typical to use a group ID much higher than the values normally used in /etc/group, unless you know a particular gid is available.  This avoids any conflicts.

We're going to create:

* a node called `People` to store users,
* a node called 'Groups` to store groups,
* and a group called `developers`.

You can create this by editing a file called, for example, `addcontents.ldif` and loading it with something similar to this:

```
dn: ou=People,dc=stormrider,dc=io
objectClass: organizationalUnit
ou: People

dn: ou=Groups,dc=stormrider,dc=io
objectClass: organizationalUnit
ou: Groups

dn: cn=developers,ou=Groups,dc=stormrider,dc=io
objectClass: posixGroup
cn: developers
gidNumber: 5000
```

Add the contents of this file to LDAP with the following command:

```
ldapadd -x -D cn=admin,dc=stormrider,dc=io -W -f addcontent.ldif
```

After entering the LDAP password, `ldapadd` should report back adding three entries:

```
adding new entry "ou=People,dc=stormrider,dc=io"
adding new entry "ou=Groups,dc=stormrider,dc=io"
adding new entry "cn=developers,ou=Groups,dc=stormrider,dc=io"
```

Next, well add a user login, which we'll use to login from the client we'll build in the next section.  In this case, the user already has a `gidNumber`, so we're not assigning a different one.  Normally, we'd choose a very large number, such as 10000, to avoid any conflicts with existing user assignments.

Add the following to myuser.ldif:

```
dn: uid=stormrider,ou=People,dc=stormrider,dc=io
objectClass: inetOrgPerson
objectClass: posixAccount
objectClass: shadowAccount
uid: stormrider
sn: nobody
givenName: stormrider
cn: stormrider
displayName: stormrider
uidNumber: 1000
gidNumber: 5000
gecos: John Doe
loginShell: /bin/bash
homeDirectory: /home/stormrider
```

Then add the contents of the file to LDAP with:

```
sudo ldapadd -x -D cn=admin,dc=stormrider,dc=io -W -f myuser.ldif 
```

Again, after entering the LDAP admin password, `slapd` confirms your entry:

```
adding new entry "uid=stormrider,ou=People,dc=stormrider,dc=io"
```

<a href="#heading--install-ldap-client"><h3 id="heading--install-ldap-client">Installing the LDAP client</h3></a>

For the purposes of this demo, we'll set up an unencrypted LDAP connection.  You can find instructions for using TLS encryption with LDAP at [ubuntu.com](https://ubuntu.com/server/docs/service-ldap-with-tls).

On your client system (in this case, the laptop `wintermute`), install the following packages:

```
sudo apt install libnss-ldap libpam-ldap ldap-utils nscd
```

After a bit of installation messaging, you'll start receiving a few ASCII dialog panels, into which you should provide answers similar to the following:

* The URI should be: ldap://ldap.stormrider.io (or whatever domain you chose for your example);  make sure this name is resolvable by the client.
* The DN should be dc=stormrider,dc=io (or your domain)
* LDAP version to use: 3
* Make local root Database admin: Yes
* Does the LDAP database require login? No
* LDAP account for root: cn=admin,dc=stormrider,dc=io
* LDAP root account password: the admin password you entered in the server

Next, edit `/etc/nsswitch.conf` to use LDAP for authentication:

```
passwd:         files systemd ldap
group:          files systemd ldap
shadow:         compat ldap
gshadow		files ldap
```

Add the home directory template to `/etc/pam.d/common-session`:

```
session required pam_mkhomedir.so skel=/etc/skel umask=077
```

Finally, restart the name service daemon:

```
sudo systemctl restart nscd
```

<a href="#heading--testing-ldap"><h3 id="heading--testing-ldap">Testing LDAP</h3></a>

You can check your work by by running `ldapsearch -x`:

```
# extended LDIF
#
# LDAPv3
# base <dc=stormrider,dc=io> (default) with scope subtree
# filter: (objectclass=*)
# requesting: ALL
#

# stormrider.io
dn: dc=stormrider,dc=io
objectClass: top
objectClass: dcObject
objectClass: organization
o: admin_crew
dc: stormrider

# People, stormrider.io
dn: ou=People,dc=stormrider,dc=io
objectClass: organizationalUnit
ou: People

# Groups, stormrider.io
dn: ou=Groups,dc=stormrider,dc=io
objectClass: organizationalUnit
ou: Groups

# developers, Groups, stormrider.io
dn: cn=developers,ou=Groups,dc=stormrider,dc=io
objectClass: posixGroup
cn: developers
gidNumber: 5000

# stormrider, People, stormrider.io
dn: uid=stormrider,ou=People,dc=stormrider,dc=io
objectClass: inetOrgPerson
objectClass: posixAccount
objectClass: shadowAccount
uid: stormrider
sn: nobody
givenName: stormrider
cn: stormrider
displayName: stormrider
uidNumber: 1000
gidNumber: 5000
gecos: John Doe
loginShell: /bin/bash
homeDirectory: /home/stormrider

# search result
search: 2
result: 0 Success

# numResponses: 6
# numEntries: 5
```

You can also check whether or not you can get the user's information from the LDAP server:

```
getent passwd stormrider
stormrider:x:1000:1000:stormrider,,,:/home/stormrider:/bin/bash
```

Of course, the ultimate test is whether or not you can login to the client via SSH:

```
ssh stormrider@$LDAPCLIENT
stormrider@$LDAPCLIENT's password:
Creating directory '/home/stormrider'.
Welcome to Ubuntu 20.04.01 LTS
```

<details>
<summary>Tell me more about LDAP</summary>
Note that a directory service is just a collection of entries filled out with key-value pairs.  Considering the typical paper telephone book as an example, you might see an entry like this:

```
Smith, John.....28 Edge Ave, 34567...................555-3438
```

So in the LDAP sense, this entry is indexed by the attribute "first name, last name" and includes attributes for street address, zipcode, and telephone number.  If we were to assume this person lives in Valparaiso, Florida, USA, we might write this LDAP entry like this:

```
dn: sn=Smith,ou=whitepages,dc=valpariso,dc=FL
objectClass: residence
sn: Smith
cn: John Smith
addr: 28 Edge Ave
zip: 34567
areacode: 901
phone: 555-3438
```

The number of ways to encode this in LDAP is not particularly limited.  For example, if the entire entry were something like this:

```
Smith, John.....28 Edge Ave, 34567...................555-3438
    Children's telephone.............................555-6743
```

then the record would be a little longer:

```
dn: sn=Smith,ou=whitepages,dc=valpariso,dc=FL
objectClass: residence
sn: Smith
cn: John Smith
addr: 28 Edge Ave
zip: 34567
areacode: 901
phone: 555-3438
phoneClass: primary
phone2: 555-6743
phoneClass: children
```

We could continue to complicate this example like this, with no trouble representing it in an LDAP entry:

```
Smith, John.....28 Edge Ave, 34567...................555-3438
    Children's telephone.............................555-6743
    Smith & Sons plumbers............................555-3439
```

This would just extend the LDAP record some more:

```
dn: sn=Smith,ou=whitepages,dc=valpariso,dc=FL
objectClass: mlresidence
sn: Smith
cn: John Smith
addr: 28 Edge Ave
zip: 34567
areacode: 901
phone: 555-3438
phoneClass: primary
phone2: 555-6743
phone2Class: children
phone3: 555-3439
phone3Class: business
```

We could keep this up all day long.  In fact, the account holder may have times when they wished for this kind of LDAP entry, which would transform the children's phone into a payphone:

```
dn: sn=Smith,ou=whitepages,dc=valpariso,dc=FL
objectClass: multiclass
sn: Smith
cn: John Smith
addr: 28 Edge Ave
zip: 34567
areacode: 901
phone: 555-3438
phoneClass: primary
phone2: 555-6743
phone2Class: coinop
phone3: 555-3439
phone3Class: business
```

<a href="#heading--DITs"><h3 id="heading--DITs">Directory Information Trees (DITs)</h3></a>

Most of the modern paper phone books have not one section, but four: the whitepages, the yellow pages, the government pages, and the phone company pages.  These are, in fact, four separate directories in one, connected mostly with the binding glue.  Each of these would be separate groups within the overall directory, e.g.,

```
ou=whitepages
ou=yellowpages
ou=government
ou=provider
```

where "provider" is the grouping for telephone company services, like Repair, MAC (move-add-change), Long Distance, and so on.  These groups are added to one LDAP as Data Information Trees (DITs).  Every entry has exactly one parent entry and, as we see in the example above, any number of child entries or attributes per entry.  Likewise, the differing DIT branches don't link, even though in real life, they may be linked.  For example:

```
Smith, John.....28 Edge Ave, 34567...................555-3438
    Children's telephone.............................555-6743
    Smith & Sons plumbers............................555-3439
```

The whitepages entry above has no bearing on the Yellow Pages entry below:

```
A straight flush beats a full house every time!
Don't gamble with your plumbing needs!
Call Smith & Sons plumbing, day or night, we'll come and fix it!
28 Edge Ave, Valparaiso..............................555-3439
Answering service, 24hr line.........................555-0735
```

<a href="#heading--ldap-components"><h3 id="heading--ldap-components">LDAP components</h3></a>

The attributes above are casually defined, but there is normally fairly complex syntax.  It's necessary to name attributes, provide any aliases for the attributes, explain what type of data is expected, and so on.  For example, the "name" attribute might be represented like this:

```
attributetype ( 2.5.27.4 NAME 'name' ALIAS 'accountholder' DESC 'ATT37.57: common supertype of name attributes'
    EQUALITY caseIgnoreMatch
    SUBSTR caseIgnoreSubstringMatch
    SYNTAX WE.1.3.62.42.7866.12(32768))
```

Obviously, attribute definitions are much more complicated than just finding a line in the phone book or LDAP directory.  Fortunately, many of the most common attributes have already been defined so that they can be easily applied.

<a href="#heading--object-class"><h3 id="heading--object-class">ObjectClass definitions</h3></a>

ObjectClasses are just collections or groupings of attributes that are generally useful in describing an item.  Above, we have four ObjectClasses of telephone numbers: whitepages, yellowpages, government, and provider.  When you specify `objectClass` in your LDAP entry, you are basically choosing a pre-defined set of attributes you can assign for that entry -- though it's not necessary to assign them all.

Bringing this into a LDAP example, the objectClass person typically includes the following attributes:

* cn = common name ("John Smith")

* description = human readable description of the entry ("my plumber")

* seeAlso = reference to related entries (e.g., other plumbers, in case John's on vacation)

* sn = surname ("Smith")

* telephoneNumber = 901-555-3439

* userPassword = a password for the user

You can use more than one objectClass if you need different attributes, but you have to have at least one (called the structural class).  Any additional ones are called auxiliary classes.

<a href="#heading--schemas"><h3 id="heading--schemas">Schemas</h3></a>

ObjectClasses can be grouped together into schemas.  There's no hard and fast rule for these, they are simply combinations of other objectClasses and attributes.  For example, the `objectClass=yellowpages` might actually have two schemas: `textonly` and `adgraphics`, depending upon whether the ad has graphics with it, or whether or not, for example, there is an "S" page for the yellow pages where "Smith and Sons Plumbing" is listed as a text entry, along with a reference like this: "See our display ad in the Plumbers section."

There are a couple of interesting examples:

* core.schema is the basic LDAPv3 attribute and object set required for the OpenLDAP implementation.

* inetorgperson.schema is commonly used to store people's contact information.

* LDIF (LDAP Interchange Format) is a plaintext schema for LDAP entries, most commonly used for getting data in and out of LDAP servers.


<a href="#heading--dit-nesting"><h3 id="heading--dit-nesting">DIT nesting</h3></a>

So far, so good, but how to we create the overall Data Information Tree (DIT)?  In other words, how do we assemble and bind the phone book?

Well, the short answer is this: it goes from general to specific.  At the top level of the DIT is the broadest categorization of information.  In the telephone book, this might be the four cardboard tabs marked "Phone Company Numbers", "Whitepages", "Government Numbers", and "Yellow Pages" (if it's a fancy one), or, more likely, sidestripes down the edges of the page to help you see where one category stops and the other begins.  These can be organized around whatever objectClasses seem most useful, though they usually fall logically within the domains (i.e., `dc=valparaiso,dc=fl`).

These entries use the `organizationalUnit` objectClass: like `ou=whitepages`.  Entries are referred to by attributes, so for search and sorting purposes, it's important to use an unambiguous attribute or group of attributes within the DIT.  This unambiuous attribute is called the relative distinguished name (RDN) and it functions a lot like a file name in a directory hierarchy.  To refer to an entry unambiguously, we need the RDN and all of the parent RDNs, a chain called the distinguished name or DN.  When adding things to the DIT, you have to specify the DN so that they system knows how do add it, and that it is unique within the system.

You may realize, at this point, the the phone book example breaks down a bit, since the address is sometimes needed to pinpoint someone with a common name.  For example, "Sarah Connor" may not be particularly happy to be confused with two others in a listing like this one:

```
Connor, Sarah.....28 Elm Street....
Connor, Sarah.....45 Plover Drive....
Connor, Sarah.....13 Zenix Place, Apt 3-J....
```

Typically, of course, the DN is modified to guarantee uniqueness:

```
Connor, Sarah J....45 Plover Drive....
Connor, Sarah M....28 Elm Street....
Connor, Sarah O....13 Zenix Place, Apt 3-J....
```

In modern LDAP usage, the RDN is usually chosen based on usename:

```
dn: uid=sconnor3,ou=People,dc=valparaiso,dc=fl
objectClass: termTarget
cn: Sarah Connor
sn: Connor
uid: sconnor3
```

Note that we use a different objectClass to get access to the `uid` attribute to make Sarah Connor unique for this LDAP entry.

<a href="#heading--ldap-protocols"><h3 id="heading--ldap-protocols">LDAP protocols</h3></a>

All of these definitions make LDAP a protocol, of course.  When you organise facts on paper into regular structures, we call them "forms" or "formats."  When you organize facts electronically, we call them "protocols" or "schemas."  Same concept, different media.

Likewise, the LDAP protocol has some variations:

* `ldap://` is the basic LDAP protocol.

* `ldaps://` is LDAP with TLS encryption.

* `ldapi://` is LDAP via interprocess communication (IPC), that is, communicated via sockets instead of networks, per sei.
</details>

<a href="#heading--rbac-with-maas"><h2 id="heading--rbac-with-maas">Using RBAC with MAAS</h2></a>


