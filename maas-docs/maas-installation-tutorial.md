||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/maas-installation-tutorial-snap-2-7-cli/3318) ~ [UI](/t/maas-installation-tutorial-snap-2-7-ui/3319)|[CLI](/t/maas-installation-tutorial-snap-2-8-cli/3320) ~ [UI](/t/maas-installation-tutorial-snap-2-8-ui/3321)|[CLI](/t/maas-installation-tutorial-snap-2-9-cli/3322) ~ [UI](/t/maas-installation-tutorial-snap-2-9-ui/3323)|[CLI](/t/maas-installation-tutorial-snap-3-0-cli/4001) ~ [UI](/t/maas-installation-tutorial-snap-3-0-ui/4002)|
Packages|[CLI](/t/maas-installation-tutorial-deb-2-7-cli/4545) ~ [UI](/t/maas-installation-tutorial-deb-2-7-ui/4541)|[CLI](/t/maas-installation-tutorial-deb-2-8-cli/4546) ~ [UI](/t/maas-installation-tutorial-deb-2-8-ui/4542)|[CLI](/t/maas-installation-tutorial-deb-2-9-cli/4547) ~ [UI](/t/maas-installation-tutorial-deb-2-9-ui/4543)|[CLI](/t/maas-installation-tutorial-deb-3-0-cli/4548) ~ [UI](/t/maas-installation-tutorial-deb-3-0-ui/4544)|

This is the placeholder for the MAAS installation tutorial.

<!-- snap-3-0-cli snap-3-0-ui
<a href="#heading--example"><h3 id="heading--example">Example of MAAS initialisation</h3></a>

The following demonstrates the `region+rack` mode, a popular initialisation choice for MAAS:

    sudo maas init region+rack

`maas` will ask for the MAAS URL:

    MAAS URL [default=http://10.55.60.1:5240/MAAS]: http://192.168.122.1:5240/MAAS

If you also need to create an admin user, you can use:

    sudo maas createadmin

which takes you through the following exchange:

    Create first admin account:       
    Username: admin
    Password: ******
    Again: ******
    Email: admin@example.com
    Import SSH keys [] (lp:user-id or gh:user-id): lp:petermatulis

[note]
You will use the username and password created above to access the web UI.  If you enter a [Launchpad](https://launchpad.net/) or [GitHub](https://github.com) account name with associated SSH key, MAAS will import them automatically.
[/note]
