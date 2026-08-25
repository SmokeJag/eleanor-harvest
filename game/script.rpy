# -------------------------------------------------------------------------------------------
# ELEANOR: CHILDREN OF THE HARVEST
# A standalone mystery in the SmokeJaguar universe
# SmokeJaguar Studios
# -------------------------------------------------------------------------------------------
#
# CHARACTER DEFINITIONS
# -------------------------------------------------------------------------------------------
define e = Character("Eleanor", color="#c8a2c8")
define n = Character("Neith", color="#e8d8e8")
define m = Character("Maren Holt", color="#d4a373")
define v = Character("The Vicar", color="#8fb3a8")
define ch = Character("The Child", color="#e8d8e8")
define mil = Character("The Miller", color="#8a6a4a")
define sch = Character("The Schoolteacher", color="#6a8a8a")
define old = Character("Old Nan", color="#a8a8a8")
define inn = Character("The Innkeeper", color="#c8a2c8")
define om = Character("The Old Man", color="#a8a8a8")
define pat = Character("A Nervous Patron", color="#8a8a6a")

# -------------------------------------------------------------------------------------------
# IMAGE ALIASES
# -------------------------------------------------------------------------------------------
image bg mansion_ext = "images/backgrounds/bg_mansion_restored.webp"
image bg hallway = "images/backgrounds/bg_hallway.webp"
image bg library = "images/backgrounds/bg_library.webp"
image bg village = Solid("#3a3a3a")
image bg village id = Solid("#2a2a2a")
image bg chapel = Solid("#1a1a2a")
image bg inn = Solid("#4a3a2a")
image eleanor_neutral = Solid("#c8a2c8")
image eleanor_determined = Solid("#c8a2c8")
image neith_neutral = Solid("#e8d8e8")
image maren = Solid("#8a6a4a")
image vicar = Solid("#4a6a4a")
image miller = Solid("#7a5a3a")
image schoolteacher = Solid("#5a7a7a")
image oldnan = Solid("#9a9a9a")
image innkeeper = Solid("#c8a2c8")

# -------------------------------------------------------------------------------------------
# CUSTOM TRANSITIONS
# -------------------------------------------------------------------------------------------
define slow_dissolve = Dissolve(1.5)
define slow_fade = Fade(1.0, 0.5, 1.0)
define flash = Fade(0.1, 0.0, 0.5, color="#ffffff")

# The quick-menu has an inventory button; define the list so the screen doesn't crash.
default inventory = []

# -------------------------------------------------------------------------------------------
# GAME START
# -------------------------------------------------------------------------------------------
label start:
    jump episode_five

label episode_five:
    # Game State
    $ clue_vicar = False
    $ clue_well = False
    $ harrow_truth = False
    $ truth_miller = False
    $ truth_school = False
    $ truth_nan = False
    $ saw_chapel = False
    $ saw_ledgers = False
    $ saw_moors = False
    $ beast_seen = False
    $ beast_clue = False
    $ neith_trust = 0

    scene bg hallway
    with slow_fade

    "There are some letters you open knowing you will regret it. This one had been waiting on the table all morning, the ink smeared, the paper creased from a hand that had held it too tightly."

    "It was not addressed to us by name. It was addressed to 'the ladies who solve things.'"

    show eleanor_neutral at left
    show neith_neutral at right
    with dissolve

    n "You've read it twice."

    e "Because I'm hoping I misread it the first time."

    n "What does it say?"

    e "It says a village in the north has a problem. And that it has had this problem, on and off, for two hundred years. And that it is coming round again."

    n "What kind of problem?"

    e "The kind the village does not call by its name."

    "The letter was postmarked from a village in Somerset called Grimshade. I had never heard of it, and that, more than anything, unsettled me. Somerset was full of old names and older stories, and a village that had kept itself out of the maps for two hundred years was a village that had something to hide."

    n "It is more than a day's journey, Eleanor. We will not reach it before nightfall."

    e "Then we will find a bed on the road, and reach it in the morning."

    scene black
    with slow_fade

    centered "{size=+6}{color=#d4a373}EPISODE FIVE — CHILDREN OF THE HARVEST{/color}{/size}"

    pause 1.5

    scene bg inn
    with slow_fade

    "The inn was called the Hanged Man, which told you most of what you needed to know about the road it stood on. It was a low, timbered building at a crossroads, its sign creaking in the wind, its windows glowing amber against the gathering dark."

    "We had been on the road since mid-morning, and the miles had worn the day down to a grey thread. The inn was the first light we had seen in hours."

    show eleanor_neutral at left
    show neith_neutral at right
    with dissolve

    n "A cheerful name."

    e "The best inns always have the worst names. It keeps the timid away."

    "Inside, the Hanged Man was warm and close, full of the smell of woodsmoke and ale and the low murmur of voices. A fire burned in a great hearth, and around it, a handful of locals sat with their pipes and their pints, the way men do when the night is long and the stories are old."

    show innkeeper at center
    with dissolve

    "The innkeeper was a broad, ruddy woman with arms like a blacksmith's and the watchful eyes of someone who had heard every tale the road could bring. She set two tankards before us without being asked."

    inn "You are a long way from anywhere, ladies. What brings you to the Hanged Man?"

    e "We are bound for Grimshade, in the morning."

    "The room went quiet. Not suddenly—the way a room goes quiet when everyone in it decides, at the same moment, not to speak."

    inn "Grimshade. Aye. That is a name we do not say lightly on this road."

    n "Why not?"

    "The innkeeper looked at us for a long moment. Then she leaned in, and her voice dropped."

    inn "Because the road to Grimshade is a road that does not like to be travelled, ladies. And the village at the end of it is a village that does not like to be found. There are stories."

    e "What stories?"

    "She glanced at the fire, and the men around it had gone very still, their eyes on their pints."

    inn "They say the village made a bargain, long ago, with something that lives under the hill. And that every so often, it comes due. They say the wells run dry and the fields go grey, and then—"

    "She stopped, and shook her head."

    inn "No. I will not tell it. Some stories are not for telling to strangers who mean to walk into them."

    "A man by the fire—old, with a face like a walnut—spoke up, his voice cracked with age."

    om "But there is another story, if you want one. A different one. About a house on the far side of the county, and a thing that was buried and should have stayed buried."

    "I felt Neith go still beside me."

    e "What house?"

    "The old man smiled, showing a gap in his teeth."

    om "They call it the Hollow House. It stands empty now, on the edge of the moors, and they say a family lived there once who made a bargain of their own. They say the bargain is still there, waiting, and that it has been waiting a very long time."

    "The fire popped. The innkeeper straightened, and the moment broke."

    inn "Enough of that. You will want beds, and you will want them before the road turns cold. I will have the girl make up the rooms."

    "She had turned to go when a man by the fire—younger than the first, with the quick, nervous look of a man who did not like the dark—spoke up."

    pat "Begging your pardon, but if you are bound for the moors, there is another thing you should know. They have seen the Beast again."

    "A low murmur ran around the room. Not fear, exactly. Something older, and more careful."

    e "The Beast?"

    "The innkeeper paused, and her face was hard to read."

    inn "The Beast of the moors, they call it. A great black cat, bigger than any dog, seen on and off since my grandmother's time. There was a while in the last century when folk said the big cats were all let loose, when it became against the law to keep them. That is the sensible story."

    "She looked at me, and her voice dropped."

    inn "But there is another story. They say it is not a cat at all, not the kind you can catch. They say it has been on the moors longer than the village, and that it only shows itself when something in the county is about to turn."

    e "Turn?"

    inn "Turn sour. Turn strange. They say it watched, before the last Harvest, and that it has been seen of late, on the road between here and Grimshade."

    "I dismissed it as I would any moorland tale — the sort of story that grows in the telling, and that every county has. But Neith was looking at the fire, and her hand was still."

    "I said nothing. But I remembered it. The Beast of the moors, watching the road to Grimshade."

    "She led us up the narrow stairs, and at the top she paused, a little apologetic."

    inn "I am sorry, ladies. It is a busy night, and I have only the one room left. It is a good room, mind—a double bed, and a fire. But it is only the one."

    "I felt Neith glance at me, and I did not look back. There was a beat of silence, the kind that says more than words, and then I spoke, keeping my voice even."

    e "That will be fine. Thank you."

    "The innkeeper looked between us, and something in her face softened—not with surprise, but with a quiet, knowing warmth, the way people look when they recognise a thing they have seen before."

    inn "Aye. I thought it might be."

    "She left us at the door, and we stood in the narrow corridor, the firelight spilling from the room, and neither of us moved for a moment."

    n "She knows."

    e "She has been running this inn a long time. She has seen everything."

    n "And she was not surprised."

    "I looked at her then, in the low light, and I did not need to say anything. Three years, and the sight of her still steadied me. The room was small, and the bed was one, and it was not a thing we had to explain to anyone."

    e "Come on. The road is long tomorrow."

    "She smiled, and followed me in, and the door closed on the quiet of the inn."

    scene black
    with slow_fade

    "That night, in a strange inn, I lay awake and thought of two villages and two bargains. And I wondered, in the dark, whether the road to Grimshade was the only road we were walking."

    "Beside me, Neith slept, and the warmth of her was a steady thing in the cold of the night. Whatever the road held, I would not walk it alone."

    scene bg village
    with slow_fade

    "The village was called Grimshade, and it earned the name. It sat in a fold of grey hills like something that had been there too long and meant to stay, its houses crouched around a single square and a well that had not been used in living memory."

    "The rain did not so much fall as hang. The streets were empty, though it was mid-morning, and the windows we passed were shuttered."

    show eleanor_neutral at left
    show neith_neutral at right
    with dissolve

    n "This is not a village that wants visitors."

    e "It is not a village that wants to be looked at."

    "We had come at the request of a woman's letter, and a mother's hope. A child had gone missing six weeks ago. The child had not been found, and the village had stopped searching. That was the part that had brought us."

    "The door we knocked on belonged to the last person who had written to anyone in authority. Her name was Maren Holt."

    show maren at center
    with dissolve

    m "You came. I did not think you would come."

    e "You asked us to. The letter was very plain."

    m "The village does not talk about it, ladies. But it is due. It is due tonight. They took her six weeks ago and they have been keeping her since—the way they always have, when the harvest nears."

    n "Taken who?"

    m "They will not say. They stopped saying years ago. But my sister's girl, she is the seventh. There have always been seven, every nine years, since the village was a village."

    "She said it the way people say a thing they have learned to survive by saying flat."

    m "They call it the Harvest. They do not call it by its true name, and they have agreed, all of them, to look at it out of the corners of their eyes."

    n "Maren. What is under the well?"

    "She flinched. It was a small flinch, but in the stillness of that room, it was loud."

    m "No one speaks of the well."

    e "And yet here we are."

    "Maren looked at us for a long moment, and I saw the war in her—the fear of the thing, and the fear of what the village would do to her for speaking. She had already chosen, by writing that letter. But the choosing had cost her."

    n "Maren. We will not let them take her. But we need to understand what we are facing. What is under the well?"

    "She shook her head slowly, the way you shake your head at a thing you have spent a lifetime refusing to name."

    m "I do not know. No one knows. It has been there longer than the village. But there are those who remember the old stories—the miller, the schoolteacher, old Nan. They will not speak to the village. But they might speak to you."

    e "Why would they?"

    m "Because you are not from here. You have not agreed to look away. That is the only thing that has ever made anyone in Grimshade speak."

    scene black
    with slow_fade

    centered "{size=+6}{color=#d4a373}THE VILLAGE{/color}{/size}"

    pause 1.5

    scene bg village
    with slow_fade

    "We walked the streets of Grimshade, and the village walked away from us."

    "It was not a cruelty, not exactly. It was a reflex, worn smooth by generations. A woman gathering washing from a line saw us and turned her back, slowly, as if we were not there. A man mending a fence stopped, looked at the ground, and went inside. The doors did not slam. They simply closed."

    "That was the thing I would come to understand about Grimshade. It did not hate. It did not even fear, not in the way you could name. It had simply learned, a long time ago, that the safest thing to do with a stranger was to become, all at once, a village of empty windows."

    show eleanor_neutral at left
    show neith_neutral at right
    with dissolve

    n "They are not hiding from us, Eleanor. They are hiding from the thing they have agreed to feed."

    e "And from the part of themselves that knows it is wrong."

    n "Yes. That is the part that is hardest to live with. So they have buried it, and they call the burial peace."

    "I looked at her, and I felt the weight of what she was saying. She had spent a century in the Duat, watching souls weigh their own hearts. She knew what it cost a person to look away from the thing they had done."

    e "How do you live with it, Neith? The knowing?"

    "She was quiet for a moment. The rain hung in the air, and the village held its breath around us."

    n "I do not live with it by looking away. I live with it by looking, and choosing, every day, not to be the thing I saw."

    "She met my eyes, and in the grey light, hers were steady."

    n "That is the only way, Eleanor. You cannot unsee a thing. You can only decide, each time, what you will do with what you have seen."

    "I reached out and took her hand. It was warm, and it steadied me in a way I could not have named."

    e "Then let us look. And let us decide."

    "We turned toward the village, and the old voices."

    # --- Investigation loop: the truth-givers and optional routes ---
    label ep5_investigate:
        menu:
            "Talk to the miller about the bargain" if not truth_miller:
                jump ep5_miller
            "Talk to the schoolteacher about the records" if not truth_school:
                jump ep5_school
            "Talk to Old Nan about the truth" if not truth_nan:
                jump ep5_nan
            "Investigate the locked chapel" if not saw_chapel:
                jump ep5_chapel
            "Search the schoolteacher's ledgers" if not saw_ledgers:
                jump ep5_ledgers
            "Walk the edge of the moors" if not saw_moors:
                jump ep5_moors
            "You have learned all the truths — go to the well" if truth_miller and truth_school and truth_nan:
                jump ep5_all_truths

        jump ep5_investigate

    label ep5_miller:
        scene bg inn
        with slow_fade

        "The miller was a broad, grey man who had outlived his mill and most of his patience. He did not invite us in. He stood in the doorway, blocking the light, and he looked at us the way you look at a debt you had hoped was forgotten."

        show eleanor_neutral at left
        show neith_neutral at right
        show miller at center
        with dissolve

        mil "You are the ones. The ones who came to open the well."

        e "We came to find a child."

        "He was silent for a long moment. Then he stepped aside, and let us in."

        mil "The child is not the first. And she will not be the last, unless you are very lucky, or very foolish. Sit. I will tell you what the village does not say."

        "He poured three cups of something dark and bitter, and he did not drink his."

        mil "The thing in the well is not a thing. It is a *debt*. A bargain, made before the village was a village, by a man who wanted the land to be fertile and the rain to come."

        e "A bargain with what?"

        mil "With the thing that was already here. It was here before the first stone was laid. It is not a god, and it is not a devil. It is older than both, and it is hungry, and it has learned, over the centuries, to be patient."

        n "And the price?"

        "The miller looked at the floor."

        mil "The price was always the same. What the land could not give, the village gave instead. Every nine years, one of the young. It was the only way the land stayed green."

        e "And you have kept this. For two hundred years."

        mil "We have kept it because we were afraid not to. And because it was easier, each time, to tell ourselves it was the only way. That is the lie at the heart of it, ladies. It was never the only way. It was just the easiest."

        "He was quiet for a moment, staring at the fire. When he spoke again, his voice was lower."

        mil "On the night, they walk the well widdershins—against the sun, the way the bargain was first made. That is the ritual of it. Three turns the wrong way round, and the debt is paid. I have seen it done since I was a boy, and I have never once seen them turn the right way."

        "He reached into his coat and drew out an old, creased ledger."

        mil "The seal on the well—it is not held by weight. It is held by the *debt*. The first bargain set a price, and the stone was set to keep it. That is the first truth of the well: you cannot lift it by force. Only by the truth."

        e "Which truth?"

        mil "That it is a debt, not a god. And debts can be refused."

        $ truth_miller = True

        "The miller's truth settled in me, cold and clear."

        jump ep5_investigate

    label ep5_school:
        scene bg village
        with slow_fade

        "The schoolteacher was a thin, precise woman who kept the village's records and its conscience, in that order. She met us in the churchyard, among the graves, and she did not pretend we were welcome."

        show eleanor_neutral at left
        show neith_neutral at right
        show schoolteacher at center
        with dissolve

        sch "You have been to the miller. He told you the bargain."

        e "He told us the price. He did not tell us what the thing is."

        "She looked at the graves, and her voice was quiet."

        sch "The records go back two hundred years, ladies. Every nine years, a name. Always a young one. Always the same season. I have kept the records, and I have never once written a cause of death, because there is no cause that the village will admit."

        n "And the thing itself?"

        sch "The oldest record calls it the *first hunger*. It was here before the village, before the church, before the land was cleared. The first settlers did not find a valley. They found a thing that was already waiting, and they made a bargain with it because they were afraid."

        e "And the bargain has never been broken?"

        "She was silent for a long moment. Then she looked at me, and there was something in her eyes I had not expected—a thin, tired hope."

        sch "It has never been broken because no one has ever been brave enough to try. But the records hold a second truth, ladies. The seal has weakened before—whenever the truth is spoken aloud. It moves. It does not hold because of iron. It holds because of silence."

        "She tapped the oldest page of the ledger."

        sch "The second truth: the stone lifts when the truth is named. Keep it silent, and it is heavier than a mountain. Name it, and it becomes nothing more than a stone."

        e "You have read it. In the records."

        sch "I have read it a hundred times, and I have never said it aloud, because to say it is to begin. But you—you can say what I could not."

        $ truth_school = True

        "The schoolteacher's truth settled in me, the second key."

        jump ep5_investigate

    label ep5_nan:
        scene bg village id
        with slow_fade

        "Old Nan's cottage was the oldest in the village, a crooked, smoke-blackened thing that seemed to have grown out of the ground rather than been built on it. She was waiting for us at the door, and she did not look surprised to see us."

        show eleanor_neutral at left
        show neith_neutral at right
        show oldnan at center
        with dissolve

        old "You have come about the well. I have been waiting for you for sixty years."

        e "You knew we would come?"

        old "I knew someone would, one day. The village has been waiting too, though it does not know it. It has been waiting for someone to say the thing it has been afraid to say."

        n "What is the thing, Nan?"

        "She looked at us, and her eyes were old and clear, and terrible."

        old "The thing in the well is not a thing at all. It is a *name*. A name that was spoken once, in fear, and that has been fed ever since. It has no body of its own. It is made of the fear the village gives it, and the silence, and the children."

        e "Then how do you end it?"

        "Old Nan smiled, and it was not a kind smile."

        old "You do not feed it. That is the only way. You stop giving it the thing it needs, and it starves. But the village will not stop, because the village is afraid. And fear is the thing that keeps it alive."

        "She reached out and took my hand, and her grip was surprisingly strong."

        old "The third truth, child. To lift the seal, you must name the fear without flinching. The stone is not heavy. It is held down by the weight of what the village will not say. Speak it, and the stone becomes as light as a word."

        e "And if I name it wrong?"

        old "Then it will know you are afraid, and it will not move. You must mean it. Not for a woman you have not met. For the truth of what is down there. When you mean it, it will break."

        $ truth_nan = True

        "Old Nan's truth, the last of the three, settled into me."

        jump ep5_investigate

    label ep5_chapel:
        scene bg chapel
        with slow_fade

        "The chapel stood at the edge of the village, a small, squat building of grey stone that the moss had been reclaiming for generations. The door was heavy and new, and it was locked from the outside—a latch and a padlock, the kind you put on a place you mean to keep people out of, not in."

        show eleanor_neutral at left
        show neith_neutral at right
        with dissolve

        n "A church that locks its door from the outside."

        e "A church that has something to keep."

        "I tested the padlock. It held. But at the base of the door, worn into the stone by years of feet, I saw a small gap, and through it, the darkness of the nave."

        "I knelt and looked in."

        "It was not a chapel for worship. The pews had been cleared to the walls, and the floor was bare stone. And at the far end, where the altar should have been, there was only a single iron ring set into the floor, and a trapdoor."

        n "What do you see, Eleanor?"

        e "A trapdoor, Neith. Under where the altar used to be."

        "She was silent for a long moment."

        n "They keep the harvest somewhere it can be hidden. Not in the village. Beneath the altar, where the village could not look at it."

        "I stood, and looked at the locked door."

        e "The miller was right. This is where they hold her."

        $ saw_chapel = True

        "I marked the place in my mind, and we left the chapel to its silence."

        jump ep5_investigate

    label ep5_ledgers:
        scene bg village
        with slow_fade

        "The schoolteacher's ledger was not in the church. It was in the vestry, in a large walnut press—a tall, heavy cabinet for keeping records—but the lock was not a hard one, and the key hung on a hook beside it, as if it had been left there for someone who meant to look."

        show eleanor_neutral at left
        show neith_neutral at right
        with dissolve

        "The pages were old and yellowed, and the handwriting changed across the decades—different hands, different generations, but always the same record. A name, a date, a single word: *taken.*"

        n "Two hundred years of names, Eleanor. All of them young. All of them the same season."

        e "And no cause of death. No coroner. No record at all, beyond the name and the word."

        n "That is the whole crime, in a ledger. The village did not even keep the truth of what it did. It kept only enough to count."

        "I turned the pages slowly, reading the names. And then I stopped, on an entry far older than the others, its ink brown with age."

        "It was not a name. It was a note, in a margin, in a hand that was different again."

        e "Neith. Read this."

        "She bent to look, and the lamplight caught her face as she read the fading letters. When she straightened, her voice was very quiet."

        n "The beast remembers the bargain; when the child does not feed, the dark opens."

        "The words fell into the room like the first crack in ice. It was not a record. It was a warning—written by someone who had known the truth, and had hidden it where the village would not look, in a column of names and dates."

        e "Neith. That is not about the harvest. That is about what the harvest is *for*."

        n "No. It is about what the village does not understand it is keeping. The silence holds the stone, Eleanor. And the stone holds the dark."

        "I looked at the margin note again, at the hand that had written it—a hand that had known it would never be read, and had written it anyway."

        "The Beast was not a story. It was in the records. It had been there all along."

        $ saw_ledgers = True
        $ beast_clue = True

        "We put the ledger back, and the names of twenty-nine children seemed to follow us out into the grey light."

        jump ep5_investigate

    label ep5_moors:
        scene bg village id
        with slow_fade

        "The moors beyond Grimshade were a great grey emptiness, the sky and the heather meeting in a low, heavy line. A haar lay over the high ground—a cold, clinging mist that swallowed the horizon—and the wind moved through it, and nothing else did. It was a place that had never been tamed, and did not intend to be."

        show eleanor_neutral at left
        show neith_neutral at right
        with dissolve

        n "There is no path here."

        e "There is. Look."

        "A track, worn into the heather, faint but unmistakable, running from the edge of the village toward the heart of the moor."

        "We followed it for a while, and the village fell away behind us, and the moor closed in, and the silence grew until it was a thing you could almost touch."

        "And then, ahead, at the edge of a rise, something moved."

        "It was there for a moment—a shape, black against the grey, larger than any dog, moving with a slowness that was not a dog's, not a fox's. It stood at the crest of the rise, and it looked back at us."

        "And then it was gone, and the moor was empty, and the only sign it had been there at all was the ringing silence it left behind."

        "Neith was still."

        n "You saw it."

        e "I saw a big cat, Neith. The kind of thing that gets loose and is never caught."

        n "And is never seen, either, in the daylight, watching a road."

        "I said nothing. But I had seen it, black against the grey, and I had felt, across that wide empty space, that it was not the thing the villagers feared. It was something that had been watching the village for a long, long time."

        $ saw_moors = True
        $ beast_seen = True

        "We walked back to the village, and the moor seemed to watch us go."

        jump ep5_investigate

    label ep5_all_truths:
        "Three truths now lay in me, clear as the rain. The deed, the word, and the fear. The miller's debt. The schoolteacher's silence. Old Nan's name."

        scene black
        with slow_fade

        centered "{size=+6}{color=#d4a373}THE WELL{/color}{/size}"

        pause 1.5

        scene bg village id
        with slow_fade

        "The well sat in the centre of the square, capped with a stone lid so heavy it must have taken six men to lift. It was not the sort of thing you put over a well you meant to use again."

        "But I had not come to lift it with strength. I had come to lift it with the truth."

    "The vicar was waiting for us. He had been, I suspect, since he saw the carriage arrive. He was a thin, greying man, and he wore his authority the way a man wears a coat that is too warm for the season."

    show eleanor_neutral at left
    show neith_neutral at right
    show vicar at center
    with dissolve

    v "You will not open that well, ladies."

    e "And who are you to tell us?"

    v "I am the man who keeps the peace of this village. And that well is not a well. It is a promise."

    n "A promise to what?"

    v "To something older than the church. Older than the village. Something that was here when the first stones were laid, and that we have agreed, all of us, to keep fed."

    e "Fed."

    v "The harvest. It was every nine years, once. Now the interval is shorter. We do not know why."

    e "You 'we.' You know what happened to the child."

    "The vicar's mouth was a thin line."

    v "We do not speak of what happens to the harvest, ladies. We speak only of what it buys us. The rain. The harvest of the fields. The village that survives another nine years."

    "And I understood, with a coldness that had nothing to do with the rain, that he was not a monster. He was a man who had been taught, from birth, to look away."

    n "And if we refuse to let it happen?"

    v "Then we have two choices. And I promise you, ladies, you will not like either of them."

    "The vicar's words hung in the cold air. Beside me, I felt Neith watching him, reading the man the way she read everything—through the years she had spent in the Duat, weighing what people truly were."

    n "He is afraid, Eleanor. Not of the thing in the well. Of the moment it is refused. He has been waiting his whole life for someone to refuse it, and he does not know how to go on after that."

    "She had seen it. I could trust that, or I could go on my own reading."

    menu:
        "Trust Neith's read — let her guide this":
            $ neith_trust += 1
            "I trusted her. I always trusted her, even when my own mind wanted to race ahead."
            e "Then we refuse it. And whatever follows, we refuse it together."
        "Go with my own reading — I know this place now":
            "I did not argue with her. But I trusted my own eyes over her instinct."
            e "Let us see what is really in the well first. Then we decide."

    if neith_trust >= 1:
        n "Together, then."

    menu:
        "Open the well — face what the village feeds":
            jump well_opened

        "Follow the child instead — find her before the harvest":
            jump follow_the_child

    return

label well_opened:
    "I looked at the vicar, and I did not blink."

    e "Show me the well."

    "We stood before the stone, and I felt the three truths in me—the debt, the word, the fear."

    "The vicar watched, and his voice was low."

    v "You cannot lift it, lady. It has taken six strong men before, and it did not move."

    e "It was never a matter of strength. It was a matter of what you will not say."

    "I spoke it then, plainly and without flinching."

    e "This is not a harvest. It is a debt, and you have been feeding it your children for two hundred years because you were afraid to refuse it. I am not afraid. I name it, and I refuse it."

    "The stone shivered. It had never heard its own name before."

    with flash

    "The seal rose from the well as if it were no heavier than a word, and a miasma came up out of it—a thick, foul mist that hung in the air. It was not the smell of water. It was the smell of something that had been fed for a very long time and had never been cleaned."

    "The walls of the well went down and down, and at the bottom, glinting faintly, was a thing that was not a stone."

    with flash

    "It looked up at us. And it opened its mouth."

    "It was not screaming. It was the more terrible thing. It was singing—an old, cracked sound—and it sang with the voices of a hundred children."

    $ well_opened = True

    e "Neith. Do not look at it."

    n "I am looking at it. It has been down here. The people have been feeding it."

    "The vicar was behind us, and his voice was grey."

    v "You have opened it. Now it knows it is seen. You have brought the harvest forward."

    scene black
    with slow_fade

    centered "{size=+6}{color=#d4a373}THE WELL{/color}{/size}"

    pause 1.5

    jump harvest_open

label follow_the_child:
    "I did not look at the well. I looked at the vicar, and I made a choice."

    e "You will not deliver her to the well tonight. You have been keeping her where?"

    v "The harvest is carried to the well the night before the first frost. That is the way it has always been."

    n "Tonight is the first frost. And she has been kept, all these six weeks, waiting for it."

    "The vicar said nothing. But his eyes went to a path that ran out of the square, over a low stone wall, and into the dark of the valley."

    "We followed it. The path led to a small, locked chapel at the edge of the village, and in a cellar beneath it, with a lantern, we found her."

    "The child was huddled in the corner. She did not scream when she saw us. She had stopped hoping for rescue a long time ago."

    "The sight of her, small and grey in the lamplight, had a way of taking the words out of me. I pressed my hand flat against the cold wall until the stone bit, to keep my own from trembling. She had been kept here, counted, and she knew it."

    show eleanor_neutral at left
    show neith_neutral at right
    with dissolve

    n "You do not have to be the strong one in every room, Eleanor. I can sit with her. You watch the door."

    "She offered me the steadiness of a century. I could take it, or I could hold myself together the way I always had."

    menu:
        "Let Neith sit with the child — trust her steadiness":
            $ neith_trust += 1
            "I let her. It was not a surrender. It was a trusting."
            "Neith knelt, and the child looked at her, and something in the small, grey face eased, just a little."
        "Keep my hand on it myself — I do it alone":
            "I knelt myself, and I took the child's hand in mine, and I did not look away. It was what I did, and what I was."

    e "We are going to get you out of here. Do you understand?"

    "She shook her head. And her voice, when it came, was small and flat."

    ch "They will not let you. The thing in the well will not let me go. It is why they keep me."

    n "Who is 'they'?"

    ch "Everyone. It is everyone, but no one. They are the village. And they will not let you take me, because if I go, it will be hungry."

    "I looked at her, small and grey and certain she would die here. And I said the only thing that mattered."

    e "What is the first thing you will see, when you are out of here?"

    "She blinked. It was the first surprise in her face since we had come in."

    ch "The sky. I have not seen the sky, since they brought me here. They keep us in the dark, so the well knows us by it."

    e "Then that is the first thing you will see. I promise you that."

    "For the first time, something in her face, small and grey, flickered like a candle catching."

    scene black
    with slow_fade

    centered "{size=+6}{color=#d4a373}THE CHILD{/color}{/size}"

    pause 1.5

    jump harvest_child

label harvest_open:
    scene bg village id
    with slow_fade

    "The square had filled. Not with a crowd. With a silence. Every house had sent a face, and every face was turned toward the open well, and none of them was looking at us."

    "The child was still captive, somewhere in the dark of the chapel, and the whole village knew it. They had gathered to see the bargain kept—the thing fed, the girl taken, the nine years won."

    "But the well was open now, and the thing in it was awake, and it had felt its name spoken."

    show eleanor_neutral at left
    show neith_neutral at right
    with dissolve

    n "Eleanor. They will bring her. They will not wait for the frost."

    v "You have opened it. It must be fed. There is no way back from this but the one that has always been."

    "I looked at the open well, and at the village that had kept it fed for two hundred years, and I understood what I had to do. Not to argue with them. To end the thing that made them fear."

    "The choice was mine. The child was not here to bargain with. It was only the hunger, and me, and what I would do to it."

    menu:
        "Speak the words that unmake the hunger":
            jump unmake_the_hunger

        "Call the Beast of the moors" if beast_seen and beast_clue and neith_trust >= 2:
            jump the_beast_path

        "Unmake the hunger (only way, if the Beast path is closed)" if not (beast_seen and beast_clue and neith_trust >= 2):
            jump unmake_the_hunger

    jump unmake_the_hunger

label harvest_child:
    scene bg village id
    with slow_fade

    "The child in my arms, and the village in the square, and every face turned toward the thing I carried."

    "They had gathered to take her. And she was in my arms, small and grey and no longer waiting to be taken."

    show eleanor_neutral at left
    show neith_neutral at right
    with dissolve

    n "They will not let you leave with her, Eleanor. Not while they still fear the well."

    e "Then I give them something else to fear."

    "I stood in the middle of them, and I did not bargain with the thing in the well. I bargained with the village."

    menu:
        "Stand against the village — make them see the child":
            jump face_the_village

        "Take the child and run — get her out of the valley":
            jump run_with_the_child

    return

label face_the_village:
    "I walked into the middle of them, the child in my arms, and I made them look at her."

    e "This is her. She has a name, and a life, and a future you have decided she does not have. And I will not let you do it."

    "The vicar's voice was quiet."

    v "You do not understand. If we do not feed it, it will take everything. The village will starve. The wells will run dry. We have kept this."

    e "You have kept something that has made you afraid, for two hundred years. And you are so afraid that you have made a child the price of your fear."

    "No one spoke. And then, at the back, a woman spoke. It was Maren Holt."

    m "She is right. We are so afraid of the thing we made we will not see a child. And I will not be afraid anymore."

    "One voice. And then another. And the ring of faces began to break, not all at once, but in pieces, like a wall that has been holding too much."

    "And then I saw the vicar. He had not moved, had not spoken. He stood at the centre of it all, the man who had kept the peace of the bargain, and he was watching his village refuse it."

    "His mouth worked, as if to call them back, to hold the line he had held all his life. But no words came. He had spent so long being the keeper of the silence that, in the moment it broke, he had nothing left to say."

    "He lowered his eyes. And I understood that the village's monster was not the man—it was the keeping. And now that it was refused, he was only an old man who had believed, all his life, that there was no other way."

    if neith_trust >= 2:
        "And through the breaking of them, Neith moved to stand with me, not behind me. She had been watching, as she always watched, and now she lent me the weight of her certainty."
        n "You have fed it because you were afraid. But fear is a choice you can put down, as you are putting it down now, one of you at a time."
        "Her voice carried, and I saw more faces turn—because it was not a stranger telling them to be brave. It was a woman who had spent a century being brave, and had the scars to prove it."

    "And with the village broken, there was nothing left to protect the well. I walked to its edge, the child still in my arms, and I spoke the words that the jaguar had taught me, the ones that unmake."

    with flash

    "The thing in the well did not know how to refuse a will that was not afraid of it. It came apart slowly, and in pieces, and when it was gone, the well was only a well, and the child was free."

    jump ending_unmaking

label run_with_the_child:
    "I did not argue. I took the child's hand, and I ran. Not toward the houses, but away, across the wall, into the dark of the valley, Neith at my side, and the village behind us did not follow."

    "They let us go. They let us go, and that was almost the worst of it, because it meant the child was not the one they truly wanted. They wanted the thing to stay, and they would feed it anything else."

    "We carried her out of the valley, and by morning, we were on the road, and she was free."

    "We did not look back at Grimshade. The hunger was still down there, in the well, and the village would feed it again, or starve it, or find their courage in their own time. That was not a fight we could carry out of the valley with a child in our arms."

    "We had done the one thing we came to do. And we had to trust that was enough."

    jump ending_epilogue

label unmake_the_hunger:
    "It came up out of the ground the way rot comes up out of a wound. It did not have a fixed shape—it had the shape of a hunger that had been a name for too long."

    "And I walked to the edge of the well, and I spoke the words that the jaguar had taught me, the ones that unmake."

    "And the thing in the well, that had fed for two hundred years, did not know how to refuse a will that was not afraid of it."

    with flash

    "It did not scream. It was far worse, it came apart the way a thing that has been held together only by fear comes apart. Slowly, and in pieces, and with a sound like the worst note of a song."

    "And when it was gone, the village was silent, and the well was only a well."

    jump ending_unmaking

label the_beast_path:
    "I did not speak the words that unmake. I stepped to the edge of the well, and I did not name the hunger."

    "The words were there, in my memory, the jaguar's gift from the temple—the words that had unmade the older hunger. But I had used them once, and I had felt what they cost. They did not heal. They unmade. They would end the thing in the well, but they would end it the way you end a wound, by cutting it away—and I did not know what else they might cut."

    "So I did not reach for the words. I called, instead, the thing that the village had been afraid to name, and that I had seen on the moor, black against the grey."

    "I called the Beast."

    "For a moment, nothing. The village stared, and the hunger coiled in the dark, and I felt the gamble of it like a stone in my throat."

    "And then the moor answered."

    "It came down from the high ground like a shadow given shape—great and black and older than the village, older than the bargain. It did not move like a cat that had escaped a pet keeper. It moved like something that had always been there, watching, waiting."

    "It was not the hunger. It was the thing the hunger had pushed aside to rule the well."

    "The Beast passed through the ring of villagers as if they were mist, and it stood over the open well, and it looked down at the hunger with eyes that had seen the beginning."

    "And it did what the village had never had the courage to do. It refused."

    with flash

    "The hunger screamed—not in fear, but in outrage—and the Beast's refusal tore through it the way the truth tore through a lie. The well cracked, and the dark blazed, and then it was gone."

    "The Beast stood a moment longer, black against the grey dawn, and it looked at me. And I understood, without a word, what the old margin had meant. *The beast remembers the bargain.* It had been waiting, all these years, for a Thorne to come and break it."

    "Then it turned, and went back to the moor, and was gone."

    jump ending_beast

label ending_unmaking:
    scene bg hallway
    with slow_fade

    "We left Grimshade at dawn. The rain had stopped, and the road was clear, and we did not look back."

    "I do not think the village will ever be quite the same. But I do not know if that is a comfort, or a wound. Some things, once seen, cannot be unseen—and the village has seen itself now, in the light of what it was willing to do."

    "The child was safe, and the well was only a well again, and the hunger was gone. But it had cost the village its innocence, and I did not know if that was a price worth the bargain they had kept for two hundred years."

    "We drove in silence for a long time. The hills greyed and fell away behind us, and the world opened out into the ordinary morning of the rest of the country, where children went to school and wells were only wells."

    show eleanor_neutral at left
    show neith_neutral at right
    with dissolve

    n "You are thinking of her."

    e "I am. Maren's niece. She will carry it. That is the part they do not tell you about the village, that even when you save them, the saving has a price."

    n "What price?"

    "I looked out at the passing fields, and I felt the weight of the morning."

    e "The child will grow up knowing the village was willing to give her to the well. That is not a thing you forget. And the village will grow up knowing it was willing to do it. That is not a thing *they* forget, either."

    "Neith was quiet for a long moment. The carriage rocked, and the road unwound."

    n "You cannot save them from the knowing, Eleanor. You can only save them from the doing. And you did that."

    e "Did I? Or did I just make them afraid of a different thing?"

    "She turned to look at me, and in the grey light, her eyes were steady and kind."

    n "You made them afraid of the truth of what they were. That is a fear worth having. It is the only fear that has ever made anyone change."

    "I looked at her, and I felt the weight of it lift, just a little. Not because the morning was easy. But because I was not carrying it alone."

    e "How do you do it, Neith? Carry the knowing, and not let it break you?"

    "She was quiet. Then she reached across and took my hand."

    n "I do not carry it alone. That is the whole secret, Eleanor. I have you. And you have me. And between us, we can carry almost anything."

    "I held her hand, and I felt the truth of it settle in me. The village would carry its shame, and the child would carry her fear, and the world would go on being the world. But we would carry it together."

    e "Then let us carry it together. All of it."

    "She smiled—a small, tired, real smile."

    n "We already do."

    "We drove on into the morning, the two of us, and the road ahead was long, and the world was heavy, and it did not matter, because we were not alone in it."

    if neith_trust >= 2:
        "I did not say it, but I thought it, in the steady warmth of her beside me: this was the truest thing I had ever built. Not the mansion, not the name. The trust that let me put down my armour when it mattered, and let her carry the load with me."
        "She did not look at me. But I felt her hand tighten on mine, and I knew she had heard it anyway."

    jump ending_epilogue

label ending_beast:
    scene bg hallway
    with slow_fade

    "We left Grimshade at dawn, and I did not look back at the well."

    "The hunger was gone, and the village was silent, and on the high ground, watching the road, I saw the Beast once more—a black shape against the grey, keeping its own watch."

    "The villagers would tell the story of the Beast for another generation, and they would not tell the truth of it. They would say the big cat had come and gone, a wild thing. And that was the kinder story, and I let them have it."

    "But I knew. The Beast had not been an escaped pet. It had been the guardian of the old bargain, waiting all these years, and it had done what the village could not. It had refused."

    show eleanor_neutral at left
    show neith_neutral at right
    with dissolve

    n "You are thinking of it."

    e "The Beast. Yes. They will tell themselves it was a wild cat, and that is the story they need. But I saw it refuse. And I saw what it was."

    n "And what was it?"

    "I looked at her, and in the grey light, I tried to put words to it."

    e "The thing the hunger had pushed aside. The guardian that kept the bargain—or perhaps only ever the thing that refused. I do not know that it wanted anything at all. I only know it refused what the village could not."

    "I did not look at the moor again. It is better, I think, to leave some things on the high ground, watching, and not to try to name them into tame things."

    n "And you ended it. Not with the words that unmake, but with the trust to call what you did not understand."

    e "I trusted you, Neith. You were the one who believed the Beast was real, when I wanted to call it a story."

    "She looked at me, and in the light, her eyes were soft."

    n "And that is why I am here, Eleanor. Because you trust me enough to see what is hidden."

    "We drove on into the morning, and behind us, the moors held their secret, and the Beast kept its watch."

    jump ending_epilogue

label ending_epilogue:
    scene black
    with slow_fade

    centered "{size=+8}{color=#c8a2c8}The Mansion Mysteries will continue...{/color}{/size}"

    pause 2.0

    centered "{size=+6}{color=#d4a373}END OF EPISODE FIVE{/color}{/size}"

    pause 2.0

    return
