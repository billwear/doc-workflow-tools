||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/user-accounts-snap-2-7-cli/3198) ~ [UI](/t/user-accounts-snap-2-7-ui/3199)|[CLI](/t/user-accounts-snap-2-8-cli/3200) ~ [UI](/t/user-accounts-snap-2-8-ui/3201)|[CLI](/t/user-accounts-snap-2-9-cli/3202) ~ [UI](/t/user-accounts-snap-2-9-ui/3203)|[CLI](/t/user-accounts-snap-3-0-cli/4145) ~ [UI](/t/user-accounts-snap-3-0-ui/4146)|
Packages|[CLI](/t/user-accounts-deb-2-7-cli/3204) ~ [UI](/t/user-accounts-deb-2-7-ui/3205)|[CLI](/t/user-accounts-deb-2-8-cli/3206) ~ [UI](/t/user-accounts-deb-2-8-ui/3207)|[CLI](/t/user-accounts-deb-2-9-cli/3208) ~ [UI](/t/user-accounts-deb-2-9-ui/3209)|[CLI](/t/user-accounts-deb-3-0-cli/4147) ~ [UI](/t/user-accounts-deb-3-0-ui/4148)|

Presumably, you have already created an administrative user, but MAAS can also have regular users (who log in to the interface or use the CLI). What users you create depends on how you intend to use MAAS.  An administrator can manage all aspects of MAAS, whereas a non-administrator user can perform a subset of tasks on machines they acquire and deploy.  MAAS limits the details a non-admin user can view, such as nodes allocated to other users. Also, non-admin users cannot access the global settings page in the web UI, nor any of the equivalent API calls from the command line.

Additionally, in order for a user to log into a MAAS-deployed machine that user must have their public SSH key installed on it.  This article explains how to create users and add their public SSH keys to MAAS, so that every deployed machine will automatically have that key installed.

#### Five questions you may have:

1. [How do I add a user?](#heading--add-a-user)
2. [How do I change a user's preferences?](#heading--user-preferences)
3. [How do I add an SSH key for a user?](#heading--ssh-keys)
4. [How do I add an API key for a user?](#heading--api-key)
5. [How do users change their password?](#heading--change-password)

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
You can manage user accounts from the 'Users' tab of the 'Settings' page.

<a href="https://assets.ubuntu.com/v1/76402e4b-manage-user-accounts__2.4_current-users.png" target = "_blank"><img src="https://assets.ubuntu.com/v1/76402e4b-manage-user-accounts__2.4_current-users.png"></a>

[note]
A currently logged in user cannot delete themselves from the web UI.
[/note]
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui  -->

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 
```
USERNAME        EMAIL                     ADMIN?
--------        -----                     ------
admin           admin@admin.com           true
billwear        bwear@stormrider.io       true
MAAS            maas@localhost            false
maas-init-node  node-init-user@localhost  false
```

You can generate a list like this with the command:

```
maas admin users read \
| jq -r '(["USERNAME", "EMAIL", "ADMIN?"]
| (., map(length*"-"))), (.[]
| [.username, .email, .is_superuser]) | @tsv' \
| column -t
```

Note that you do not need line continuations within the `jq` command because it's quoted for the shell.
snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli  -->

<a href="#heading--add-a-user"><h2 id="heading--add-a-user">Add a user</h2></a>

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 
To add a regular user, enter the following command:

```
maas $PROFILE users create username=$USERNAME \
    email=$EMAIL_ADDRESS password=$PASSWORD is_superuser=0
```

All the options are necessary. Note that stipulating a password on the CLI may be a security hazard, depending on your environment.
snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli  -->

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
Clicking the 'Add user' button will result in a form to be displayed:

<a href="https://assets.ubuntu.com/v1/1c59c2c5-manage-user-accounts__2.4_add-user.png" target = "_blank"><img src="https://assets.ubuntu.com/v1/1c59c2c5-manage-user-accounts__2.4_add-user.png"></a>

Fill in the fields and hit 'Add user' when done.

<a href="#heading--user-preferences"><h2 id="heading--user-preferences">User preferences</h2></a>

Clicking the MAAS username in the top right corner will show that user's preferences.
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui  -->

<a href="#heading--ssh-keys"><h3 id="heading--ssh-keys">SSH keys</h3></a>

Before a user can deploy a machine, they must import at least one public SSH key into MAAS. This key allows the user to access the deployed machine with the corresponding private key, which the user must possess. See [Public key authentication](https://www.ssh.com/ssh/public-key-authentication) (ssh.com) if you're not familiar with SSH keys.

<!-- deb-2-7-cli
[note]
The user normally imports their initial SSH key on the first login to the web UI (see [Configuration journey](/t/configuration-journey/2532)).
[/note]
deb-2-7-cli -->

<!-- deb-2-7-ui
[note]
The user normally imports their initial SSH key on the first login to the web UI (see [Configuration journey](/t/configuration-journey/2533)).
[/note]
 deb-2-7-ui -->

<!-- deb-2-8-cli
[note]
The user normally imports their initial SSH key on the first login to the web UI (see [Configuration journey](/t/configuration-journey/2534)).
[/note]
 deb-2-8-cli -->

<!-- deb-2-8-ui
[note]
The user normally imports their initial SSH key on the first login to the web UI (see [Configuration journey](/t/configuration-journey/2535)).
[/note]
 deb-2-8-ui -->

<!-- deb-2-9-cli
[note]
The user normally imports their initial SSH key on the first login to the web UI (see [Configuration journey](/t/configuration-journey/2536)).
[/note]
 deb-2-9-cli -->

<!-- deb-2-9-ui
[note]
The user normally imports their initial SSH key on the first login to the web UI (see [Configuration journey](/t/configuration-journey/2537)).
[/note]
 deb-2-9-ui -->

<!-- deb-3-0-cli
[note]
The user normally imports their initial SSH key on the first login to the web UI (see [Configuration journey](/t/configuration-journey/3887)).
[/note]
 deb-3-0-cli -->

<!-- deb-3-0-ui
[note]
The user normally imports their initial SSH key on the first login to the web UI (see [Configuration journey](/t/configuration-journey/3888)).
[/note]
 deb-3-0-ui -->

<!-- snap-2-7-cli
[note]
The user normally imports their initial SSH key on the first login to the web UI (see [Configuration journey](/t/configuration-journey/2526)).
[/note]
 snap-2-7-cli -->

<!-- snap-2-7-ui
[note]
The user normally imports their initial SSH key on the first login to the web UI (see [Configuration journey](/t/configuration-journey/2527)).
[/note]
 snap-2-7-ui -->

<!-- snap-2-8-cli
[note]
The user normally imports their initial SSH key on the first login to the web UI (see [Configuration journey](/t/configuration-journey/2528)).
[/note]
 snap-2-8-cli -->

<!-- snap-2-8-ui
[note]
The user normally imports their initial SSH key on the first login to the web UI (see [Configuration journey](/t/configuration-journey/2529)).
[/note]
 snap-2-8-ui -->

<!-- snap-2-9-cli
[note]
The user normally imports their initial SSH key on the first login to the web UI (see [Configuration journey](/t/configuration-journey/2530)).
[/note]
 snap-2-9-cli -->

<!-- snap-2-9-ui
[note]
The user normally imports their initial SSH key on the first login to the web UI (see [Configuration journey](/t/configuration-journey/2531)).
[/note]
 snap-2-9-ui -->

<!-- snap-3-0-cli
[note]
The user normally imports their initial SSH key on the first login to the web UI (see [Configuration journey](/t/configuration-journey/3885)).
[/note]
 snap-3-0-cli -->

<!-- snap-3-0-ui
[note]
The user normally imports their initial SSH key on the first login to the web UI (see [Configuration journey](/t/configuration-journey/3886)).
[/note]
 snap-3-0-ui -->

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 
To add a public SSH key to a MAAS user account:

```
maas $PROFILE sshkeys create "key=$SSH_KEY"
```
snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli  -->

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
To add a locally-generated public key, select 'Upload' from the 'Source' menu and paste the complete contents of your key file, usually called `id_rsa.pub`, into the 'Public key' field. Click 'Import' to add the key to MAAS.

Public keys residing on either [Launchpad](https://help.launchpad.net/YourAccount) or [GitHub](https://help.github.com/articles/connecting-to-github-with-ssh/) can also be added. Select either from the 'Source' menu and specify the user ID associated with the key(s). Press the 'Import' button to add any keys MAAS discovers to the current user's MAAS account.

<a href="https://assets.ubuntu.com/v1/fc95765e-manage-user-accounts__2.4_add-user-ssh-key.png" target = "_blank"><img src="https://assets.ubuntu.com/v1/fc95765e-manage-user-accounts__2.4_add-user-ssh-key.png"></a>
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui  -->

<a href="#heading--api-key"><h3 id="heading--api-key">API key</h3></a>

<!-- deb-2-7-ui
The user preferences page includes an API key for the currently active user. This key can be copied and regenerated as needed. The API key is used to login to the API from the [MAAS CLI](/t/maas-cli/2821).  Other services connecting to MAAS such as Juju will also need this key.
 deb-2-7-ui -->

<!-- deb-2-8-ui
The user preferences page includes an API key for the currently active user. This key can be copied and regenerated as needed. The API key is used to login to the API from the [MAAS CLI](/t/maas-cli/2823).  Other services connecting to MAAS such as Juju will also need this key.
 deb-2-8-ui -->

<!-- deb-2-9-ui
The user preferences page includes an API key for the currently active user. This key can be copied and regenerated as needed. The API key is used to login to the API from the [MAAS CLI](/t/maas-cli/2825).  Other services connecting to MAAS such as Juju will also need this key.
 deb-2-9-ui -->

<!-- deb-3-0-ui
The user preferences page includes an API key for the currently active user. This key can be copied and regenerated as needed. The API key is used to login to the API from the [MAAS CLI](/t/maas-cli/3987).  Other services connecting to MAAS such as Juju will also need this key.
 deb-3-0-ui -->
 
<!-- snap-2-7-ui
The user preferences page includes an API key for the currently active user. This key can be copied and regenerated as needed. The API key is used to login to the API from the [MAAS CLI](/t/maas-cli/2815).  Other services connecting to MAAS such as Juju will also need this key.
 snap-2-7-ui -->

<!-- snap-2-8-ui
The user preferences page includes an API key for the currently active user. This key can be copied and regenerated as needed. The API key is used to login to the API from the [MAAS CLI](/t/maas-cli/2817).  Other services connecting to MAAS such as Juju will also need this key.
 snap-2-8-ui -->

<!-- snap-2-9-ui
The user preferences page includes an API key for the currently active user. This key can be copied and regenerated as needed. The API key is used to login to the API from the [MAAS CLI](/t/maas-cli/2819).  Other services connecting to MAAS such as Juju will also need this key.
 snap-2-9-ui -->

<!-- snap-3-0-ui
The user preferences page includes an API key for the currently active user. This key can be copied and regenerated as needed. The API key is used to login to the API from the [MAAS CLI](/t/maas-cli/3986).  Other services connecting to MAAS such as Juju will also need this key.
 snap-3-0-ui -->

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 
We recommend that you use the web UI to set or change a user's API key.  To see how, select the "UI" choice for your version and delivery method at the top of this page.
snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli  -->

<a href="#heading--change-password"><h3 id="heading--change-password">Change password</h3></a>

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 
We recommend that you use the web UI to change user passwords.  To see how, select the "UI" choice for your version and delivery method at the top of this page.
snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli  -->

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
The current user can change their password at the bottom of the page by entering the old password and entering the new password twice. Click 'Save password' to finish.

<a href="https://assets.ubuntu.com/v1/289ef578-manage-user-accounts__2.4_change-user-password.png" target = "_blank"><img src="https://assets.ubuntu.com/v1/289ef578-manage-user-accounts__2.4_change-user-password.png"></a>

[note]
An administrator can change any user's password from within the 'Users' tab of the 'Settings' page.
[/note]
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui  -->
