import os

def extractpositions(log):
    lines = log.strip().split('\n')

    positions = []

    for line in lines:
        if line.startswith("setpos"):
            positions.append(line[len("setpos "):])

    return positions

def buildconfig(path, positions, name="prefire", filepath=os.getcwd(), infiniteammo=False, weapon="weapon_ak47"):
    template = """mp_teammates_are_enemies 1;
mp_respawn_on_death_ct 1;
mp_respawn_on_death_t 1;
"""

    cfg_contents = "say \""+path+"\";\n\n"+template

    if infiniteammo:
        cfg_contents += "sv_infinite_ammo 1;\n"
    else:
        cfg_contents += "sv_infinite_ammo 0;\n"
    
    cfg_contents += "give "+weapon+";\n"

    cfg_contents += "setpos "+positions[0]+";\n\n"
    del positions[0]

    num = 2
    for pos in positions:
        cfg_contents += "setpos_player "+str(num)+" "+pos+";\n"
        num += 1

    with open(filepath+"/"+name+".cfg", "w") as file:
        file.write(cfg_contents)