define quest = Character("Quest", color="#ff6500")
define qc = Character("Quest Complete", color="ff6500", what_prefix="{s}", what_suffix="{/s}")

default pirate = "Pete"

screen boat_ctc():
    modal True
    imagebutton:
        auto "boat %s"
        focus_mask True
        action Jump("boatfound")

label start:
    show bg water

    show dock:
        zoom .9
        ypos .2
        xpos .2

    show pete happy bald:
        yalign 2

    "This is [pirate]."

    show pete happy hat

    $ pirate = "Captain " + pirate

    "[pirate]."

    "[pirate] is a pirate."

    show pete sad hat

    "[pirate] has no ship."

    hide pete

    show screen boat_ctc()

    quest "Find a ship for [pirate]."

label boatfound:
    hide screen boat_ctc
    qc "Find a ship for [pirate]."
    return
