init python:
    # add this line before beepy_voice function
    renpy.music.register_channel(name='beeps', mixer='voice')

init python:
    def caretaker_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("audio/caretaker.mp3", channel='beeps')
        elif event == "slow_done":
            renpy.sound.stop(channel='beeps')

    def judy_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("audio/judy.mp3", channel='beeps')
        elif event == "slow_done":
            renpy.sound.stop(channel='beeps')

    def buff_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("audio/buff.mp3", channel='beeps')
        elif event == "slow_done":
            renpy.sound.stop(channel='beeps')

    def gruff_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("audio/gruff.mp3", channel='beeps')
        elif event == "slow_done":
            renpy.sound.stop(channel='beeps')

    def bossy_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("audio/baby.mp3", channel='beeps')
        elif event == "slow_done":
            renpy.sound.stop(channel='beeps')


# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Caretaker", callback=caretaker_voice)
define b = Character("Buff", callback=buff_voice)
define g = Character("Gruff", callback=gruff_voice)
define bm = Character("Bossy B. Bossman", callback=bossy_voice)
define j = Character("Judge Judy", callback=judy_voice)
define gu = Character("Guard", callback=buff_voice)


# The game starts here.

label start:

    scene black
    "This demo that I was already in the process of making... {i}may{/i} have aged horribly in light of current tragic events."
    "Please note that all violence included within this game is intentionally cartoonish and is not meant to make light of any recent occurances."

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    play music apartment fadein 2 fadeout 2
    scene apartment
    with Dissolve(2)
    pause 4

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    play sound ringtone fadein 2
    show caretaker
    with Dissolve(2)
    pause 2
    stop sound
    play sound beep
    pause 1

    # These display lines of dialogue.

    c "Good morning Daniel! Rise and shine!"
    c "Sorry I couldn't be at the nursing home in person today. I've been feeling a little under the weather, so I hope this convieniently one-way video call will suffice!"
    c "..."
    c "Still not speaking, huh?"
    c "Well that's perfectly okay Daniel!"
    c "I understand that the war was very traumatic for you; the least I could do is show a little patience."
    c "I mean, what you went through would surely fracture anyone's mentality!"
    c "Speaking of which, you {i}have{/i} been taking your meds, right?"
    pause 2
    c "RIGHT!?"
    menu:
        "Nod":
            c "Oh thank god..."
            c "You know what you're like without the-"
    play sound cocking
    pause 3
    c "..."
    c "Daniel?"
    c "Did I just hear-"
    show gun
    c "IS THAT A GUN, DANIEL!?"
    menu:
        "Nod":
            c "WHY DO YOU HAVE A GUN!?"
    menu:
        "Nod":
            c "THAT DOESN'T ANSWER MY QUESTION!"
    menu:
        "Nod agressively":
            c "Daniel, let's be reasonable here!"
            c "I know you've been very vocal online about your 'second ammendment rights', but..."
            c "...you {i}kind of{/i} lost that privelage when you threatened that bus full of children."
    menu:
        '"Totally worth it."':
            c "Daniel! Did you just... SPEAK?"
    menu:
        "Nod":
            c "Aaaaand you're back to being mute again, aren't you?"
    menu:
        "Firm nod":
            c "Listen, the point is... you {i}can not{/i} set foot out that door! You're a danger to the general public!"
    menu:
        "Step foot":
            jump street
        "Oblige":
            c "Good, good..."
            c "(Indistinct praying)"
            c "Now please... go back to bed. I'll be there to help soon, but until then I think you need more rest."
    menu:
        "Sleep":
            stop music
            scene crisisaverted
            with Dissolve(2)
            pause 4
            scene black
            with Dissolve(2)
            return

        "Nah, nevermind, gun spree time!":
            c "Wait, WAIT! Daniel, WHERE ARE YOU GOING!?"
            jump street

label street:
    play music street fadein 2 fadeout 2
    scene street
    show caretaker
    with Dissolve(2)
    pause 2
    c "Daniel, please go home! I'm begging you!"
    menu:
        "Shake head":
            c "Daniel, wait, don't hang u-"
            play sound beep
            hide caretaker
            with Dissolve(1)
            pause 2
    menu:
            "To the park!":
                "Huh, looks like the park is conviniently having construction right now."
                "It's almost as if it was too much content for the demo!"
                "Oh well, guess we'll just go to the alleyway instead!"
                jump alleyway
            "To that alleyway!":
                jump alleyway

label park:

label alleyway:
    play music apartment fadein 2 fadeout 2
    scene alleyway
    with Dissolve(2)
    show gruff
    with Dissolve(2)
    g "Hehehe... what have we got here, Buff?"
    show buff
    with Dissolve(2)
    b "Looks like we've got ourselves an old man to pick on, Gruff!"
    g "Ooh, goody goody! But what should we {i}do?{/i}"
    b "Gee, I don't know Gruff. The boss has never sent us out on our own before..."
    g "Well then we'll just have to kidnap him! A flawless idea!"
    b "Yes! The boss is sure to be pleased."
    play sound ringtone fadein 2
    show caretaker
    with Dissolve(2)
    pause 2
    stop sound
    play sound beep
    pause 1
    c "Daniel! Please don't hang up again!"
    c "Wait... where are you?"
    b "Oh, hello phone person!"
    g "Yes, hello!"
    g "..."
    g "Wait, we shouldn't be letting him do this."
    b "Oh yeah, cause of the kidnappin and all that..."
    c "Wait, wait, wait... {i}KIDNAPPING!?{/i}"
    c "Daniel, what have you gotten yourself into ALREADY?"
    c "No, I can't get mad. We need to focus."
    g "C'mon, hurry up and let us kidnap ya! Waddaya say?"
    c "Daniel, I know how your PTSD affects you in situations like this."
    c "You get stuck in a state of fight-or-flight. Or, I guess in this case it would be 'agree-or-shoot'."
    c "But I just want you to know that there are plenty of other options you could-"
    menu:
        "Agree":
            c "Daniel, wait, no-"
            play sound beep
            hide caretaker
            with Dissolve(1)
            pause 2
            g "Hehe, good choice."
            b "Yeah, we're gonna take {i}real{/i} good care of you, ehehe..."
            g "And by that we mean we literally have no idea what we're gonna do with you, mwahahhahaahawhahhahfjafhsfshahfjah!"
            b "..."
            b "Was that supposed to be a laugh?"
            g "I was just trying to switch it up a bit, okay? Cmon, let's just get out of here before the cops show."
            jump hideout

        "Shoot":
            c "Daniel, wait, no-"
            play sound beep
            hide caretaker
            with Dissolve(1)
            pause 2
            b "Good, looks like he's gonna come with u-"
            play sound cocking
            show gun
            pause 0.5
            g "Woah, woah, woah! Slow down there buddy! We don't want any trouble!"
            b "Dude, he's just some old guy, what are you so scared about?"
            g "This guy could be Helen Keller for all I care! It doesn't matter anymore!"
            g "He has..."
            g "T H E  G R E A T  M E D I A T O R"
            b "Heh, like he would ever actuall-"
            play sound gunshot
            hide buff
            hide gruff
            with Dissolve(1)
            play music crowd fadeout 2
            scene court
            with Dissolve(2)
            pause 2
            j "Order in the court!"
            play music room fadeout 2
            j "It is time to commence the case of Bossy B. Bossman VS Daniel."
            j "The defendant, Daniel, has been brought here on the charge of murder. Please state your plea."
            menu:
                "(Awkward silence with the occasional coughing and sniffling)":
                    j "Thank you. We now call Bossy 'Boss Baby' Bossman to the stand."
                    show bossman
                    with Dissolve(2)
                    pause 2
                    bm "Thank you. Ahem..."
                    bm "{b}WAAAAAAAAAAAAAAAAAAAAAA!{/i}"
                    bm "Sorry, I just... I just needed to get that out of my system."
                    bm "I'm understandably a bit cranky, because {i}someone{/i} killed the henchmen who were supposed to burp me!"
                    j "Excuse me... {i}henchmen?{/i}"
                    bm "Uh... I meant {i}good friends...{/i}"
                    bm "(Who ocassionally carry out hits for me....)"
                    j "Right..."
                    bm "Anyway, this jerkwad right here shot my {i}friends{/i} in cold blood, and he should be held to the fullest extent of the law!"
                    j "Sir, a bystander said that they heard some commotion going on in the alley about a 'kidnapping'. Does this ring a bell?"
                    bm "Uhhhh... No! No, not at all..."
                    j "As a judge, I am legally required to ignore your suspicious tone of voice."
                    j "(Also the fact that you are LITERALLY a baby)"
                    j "Well, without another witness, I am afraid that we are at a standstill."
                    j "That is, unless {i}you{/i} know of another witness, Daniel?"
                    menu:
                        "Nod":
                            play sound ringtone fadein 2
                            show caretaker
                            with Dissolve(2)
                            pause 2
                            stop sound
                            play sound beep
                            pause 1
                            c "Daniel? Daniel, where are you?"
                            j "Hello. This is Judge Judy. Daniel is in court."
                            c "Daniel, {i}WHAT DID YOU DO?{/i}"
                            j "According to reports, he shot two men dead within an alleyway this afternoon."
                            c "Oh Daniel... I know you did what you had to do, but this is serious!"
                            j "'Did what he had to do'? So do you bear witness, then, that this act was in self defense?"
                            c "Yes! I was in a call with Daniel when it happened!"
                            c "Those two men were gang members who attempted to kidnap him!"
                            j "It is settled, then! This man..."
                            j "Is innocent!"
                            bm "{b}WAAAAAAAAAAAAAAAAAA!{/b}"
                            j "And as for you, 'Bossman', I believe you're going to be sent somewhere {i}quite a bit {/i} more strict than the daycare."
                            stop music
                            scene civiljustice
                            with Dissolve(2)
                            pause 4
                            scene black
                            with Dissolve(2)
                            return


                        "Shoot":
                            play sound cocking
                            show gun
                            pause 0.5
                            j "SOMEBODY {i}PLEASE{/i} EXPLAIN TO ME HOW HE GOT INTO HERE WITH THE VERY SAME GUN HE LITERALLY JUST USED FOR MURDER!?"
                            gu "Huh... guess he had two of em?"
                            play sound gunshot
                            stop music
                            scene coldblooded
                            with Dissolve(2)
                            pause 4
                            scene black
                            with Dissolve(2)
                            return




label hideout:
    play music room fadein 2 fadeout 2
    scene darkoffice
    with Dissolve(2)
    pause 2
    g "He- hey boss..."
    g "Ya here?"
    b "Strange... Bossy's not responding."
    b "Here, let me get the lights..."
    g "Wait, Buff, no!"
    scene office
    with Dissolve(1)
    pause 2
    bm "{b}WAAAAAAAAAAAAAAAAAAAAAAAA!{/b}"
    g "Ugh, now you've done it!"
    bm "I was in the middle of my afternoon nappy! What's wrong with you two goons?"
    b "I'm very sorry, Bossman! It won't happen again!"
    b "I'll just turn the lights back off and-"
    bm "No, no, it's too late. I'm all worked up now."
    bm "Just... tell me whatever it is you incompetent idiots wanted to say."
    g "Well then lookey here, Bossman! We brought ya somethin!"
    bm "Oh yes, yes, I see him now that the eye mucus is clearing..."
    bm "Is that... an old man?"
    b "Oh, not just {i}any{/i} old man!"
    g "Yeah, boss! He's an old man..."
    b "That we {i}kidnapped!{/i}"
    bm "..."
    bm "But why?"
    g "IDK, crime stuff I guess."
    bm "..."
    bm "..."
    bm "..."
    bm "(Deep inhale)"
    bm "(Even deeper exhale)"
    bm "So you mean to tell me..."
    bm "That you kidnapped this frail, senile old man..."
    bm 'Because "crime stuff".'
    g "..."
    b "..."
    g "Well when you put it that way..."
    bm "I'm literally a {b}BABY{/b}, and even I am baffled at your lack of competence!"
    b "Hey, don't say that! You're not just a baby! You're our boss!"
    g "Yeah, nobody messes with our Boss Baby!"
    "You finally get the joke, and suddenly have an overwhelming urge to punch your screen and/or hunt down whoever created this game."
    bm "You guys are right... I need to have a little more confidence. Hold my pudgy head high!"
    bm "And besides, I just had an idea. Perhaps you boys didn't do too bad after all!"
    bm "We can get ourselves..."
    bm "A RANSOME!"
    b "Yeah, boss! I like that idea!"
    g "That was {i}totally{/i} our plan all along!"
    bm "So what'll it be, old man? You got any family we can call?"
    menu:
        "Shake head":
            bm "Wait, wait, wait..."
            bm "You mean to tell me that you've got no family?"
            bm "There isn't, like, anyone who cares about you that you could call?"
            play sound ringtone fadein 2
            show caretaker
            with Dissolve(2)
            pause 2
            stop sound
            play sound beep
            pause 1
            bm "Oh good! Right on time!"
            bm "Listen, phone person, we demand a ransome or els-"
            c "{b}I QUIT!{/b}"
            play sound beep
            hide caretaker
            with Dissolve(1)
            pause 2
            g "Wow..."
            b "You really {i}are{/i} alone..."
            bm "Well, there goes our plans I guess."
            g "I gotta say, I kinda feel bad for the guy."
            b "Yeah. At least us three have got each other. This old man..."
            b "He's got no one."
            bm "Well... maybe he doesn't need to be alone."
            g "Wait, Bossman, are you suggesting what I think you're suggesting?"
            b "Come on now, are we really gonna let this old man into the family?"
            bm "Well why not? I'm just a baby, aren't I? And look what I'm capable of!"
            bm "Besides, he don't got nobody else to go home to anyhow."
            bm "So waddaya say, old man? You want {i}us{/i} to be your new family?"
            menu:
                "Agree":
                    stop music
                    scene bighappyfamily
                    with Dissolve(2)
                    pause 4
                    scene black
                    with Dissolve(2)
                    return

                "Shoot":
                    jump shootboss

        "Shoot":
            jump shootboss

label shootboss:
    play sound cocking
    show gun
    pause 0.5
    b "HOLY CRAP HOLY CRAP HOLY CRAP"
    b "BOSS, HE HAS A GUN!"
    bm "I SEE THAT, BUFF!"
    bm "Gee, I wonder who it was who forgot to check the hostage for LETHAL WEAPONS!?"
    g "He's just an old man, boss! How were we supposed to know?"
    bm "I'm running a mob family at the age of 8 months, and you assumed this man was harmless because he was {b}OLD?{/b}"
    b "Oh come on, like he'd ever shoot a bab-"
    play sound gunshot
    scene emptyoffice
    show gun
    with Dissolve(1)
    hide gun with Dissolve(2)
    show buff
    show gruff
    with Dissolve(2)
    pause 2
    g "..."
    b "..."
    g "Buff..."
    b "Gruff..."
    g "Is he..."
    b "Gone?"
    g "No, he can't be! I'm sure he's just... taking another one of his naps?"
    b "I don't think so, Gruff."
    g "..."
    b "..."
    g "He always warned us this would happen, what with us wagin war with the Crips down at the Daycare and all that."
    b "But... if Bossman is gone... what do we do now?"
    g "I suppose we... we need a new Bossman, Buff."
    b "But who could possibly fill his role?"
    g "I suppose we need someone ruthless. Someone who's not afraid to get stuff done. And most importantly..."
    g "Someone who's willing to put all morals aside and pop a cap in any of those Daycare fellows who dares cross our path..."
    pause 2
    g "You thinking what I'm thinking, Buff?"
    b "I- I think I catch your drift, Gruff."
    g "Old dude, I know you just, like, totally bodied our Bossman and all that, but..."
    g "Do you wanna be our shiny {i}new{/i} Bossman?"
    menu:
        "Agree":
            stop music
            scene shinynewbossman
            with Dissolve(2)
            pause 4
            scene black
            with Dissolve(2)
            return

        "Shoot":
            play sound gunshot
            hide buff
            hide gruff
            with Dissolve(1)
            stop music
            scene coldheartedvigilante
            with Dissolve(2)
            pause 4
            scene black
            with Dissolve(2)
            return
