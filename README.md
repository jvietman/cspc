# CS:PC (Counter-Strike: Prefire Creator)
A tool for CS:GO to create custom prefires on any map.

## !!! OUTDATED !!!
I dont know if this will even work in cs2. This program was build for cs:go. Maybe some file structures changed or script dont work in cs2 like they worked in cs:go. I will check if this works on cs2 soon and maybe automate more stuff to be more user friendly.

## Some info
Maybe I will code an installer, because it is complicated to download and setup everything.

## Guide
### How to load prefires?
Prefires are saved in .cfg (config) files. They contain commands like teleporting every bot, setting up things like ffa (free for all), give weapons, unlimited ammo etc.
You can either create your own prefires or download prefires made by other people (check the "prefire" folder to download prefires I already made).

#### Where do I put the config file?
1. Go into your CS:GO directory
2. Go into the folder csgo > cfg
3. Drag and drop your config file (you can also create folders to organize your prefires)

#### **How do I install the setup config?**
1. Download the "setup.cfg" file from the "prefire" folder in this repository
2. Drag and drop it into your csgo config folder

#### **How do I load the prefire?**
1. Start an offline round on the map of the prefire
2. Open the console (usually with the "~" key)
3. Type in "exec setup" to setup everything
4. Type in "exec \<prefire>" (replace "\<prefire>" with the name of the config file. If you have it in a folder then list out the whole path)

### How to create prefires?
<img src="https://github.com/jvietman/cspc/assets/77661493/5cac0a1c-c842-41e5-8e24-55cec1f4dbd9" width="60%">

1. Start an offline round on the map of the prefire
2. Open the console (usually with the "~" key)
3. Go to the desired position and type in "getpos" (if the bot is bugging, use the command "getpos_exact")
4. After you done that everywhere you want to, copy the whole console log containing the positions
5. Paste the log into the big text entry (first "setpos" must be your spawn position!)
6. Fill out all other information
7. Press "Build" to build the config file

Here is an example of how it could look:

<img src="https://github.com/jvietman/cspc/assets/77661493/4c215882-abd8-4050-ad2e-91501d0fe79c" width="50%">
