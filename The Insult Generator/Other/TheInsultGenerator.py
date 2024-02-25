import random

#SNOWFLAKES BEWARE, IF YOU'RE READING THIS THIS IS YOUR LAST CHANCE AT COMING OUT UNSCATHED. 

#Introduction

print("Welcome To The INSULT GENERATOR")
print("The Grill Is Sizzling Hot")
print("Press 'enter' to regenerate an insult.")
print("Type 'exit' to exit.")

# Put the names of people you want to insult here!
names_input = input("Enter the names you want to insult (comma-separated): ")

# Check if the user entered names
while not names_input:
    print("You must enter at least one name.")
    names_input = input("Enter the names you want to insult (comma-separated): ")

person_names_list = [name.strip() for name in names_input.split(',')]

# Connecting words from Name to Insult.
con_word_list = ["is", "is", "is", "is", "is", "is definitely","could definitely be", "would definitely be", "may be", "might be", "shall be", "can't be", "would be", "must be", "ought to be", "could be", "is definitely", "is absolutely", "is ,without hesitation,", "is, no further questions,", "is perceived to be", "is conjectured to be", "is presupposed to be", "is surmised to be", "is postulated to be", "is inferred to be", "is deduced to be", "is derived to be", "is assumed to be", "is guessed to be", "is speculated to be", "is hypothesized to be", "is theorized to be", "is posited to be", "is anticipated to be", "is forecasted to be", "is predicted to be", "is prophesied to be", "is foreseen to be", "is foretold to be", "is foreknown to be", "is foreordained to be", "is predestined to be", "is predetermined to be", "is fated to be", "is destined to be", "is meant to be", "is designed to be", "is intended to be", "is planned to be", "is scheduled to be", "is arranged to be", "is organized to be", "is orchestrated to be", "is prepared to be", "is ready to be", "is set to be", "is fixed to be", "is appointed to be", "is assigned to be", "is delegated to be", "is allocated to be", "is earmarked to be", "is destined to be","seems to be", "appears to be", "is likely to be", "is prone to be", "is inclined to be", "tends to be", "is predisposed to be", "has the potential to be", "has the capability to be", "has the tendency to be", "has the propensity to be", "is bound to be", "is expected to be", "is presumed to be", "is thought to be", "is believed to be", "is considered to be", "is regarded as", "is viewed as", "is judged to be", "is evaluated as", "is estimated to be", "is assessed to be", "is appraised to be", "is rated to be", "is graded to be", "is ranked to be", "is classified as", "is categorized as", "is labeled as", "is defined as", "is characterized as", "is described as", "is depicted as", "is portrayed as", "is illustrated as", "is represented as", "is presented as", "is marked as", "is identified as", "is recognized as", "is acknowledged as", "is accepted as", "is confirmed as", "is validated as", "is verified as", "is substantiated as", "is supported as", "is backed as", "is justified as", "is warranted as", "is proven to be", "is established as", "is confirmed to be", "is authenticated as", "is attested to be", "is ratified as", "is sanctioned as", "is approved as", "is endorsed as", "is accredited as", "is certified as", "is authorized as", "is permitted as", "is allowed as", "is granted as", "is conceded as", "is bestowed as", "is gifted as", "is awarded as", "is presented with"]

# NAUGHTY WORDS. 
naughty_words_list = ["gay","a bastard","a brotherfucker","a child-fucker","a cocksucker","a turd","a dickwad","a wanksta", "a fuckface", "a cunt goblin", "a cockhead", "a Karen", "a weirdo", "a dork", "a nerd", "a chad Korean guy","a cumguzzlingfuckmonkey","a fuckhead", "a fucktard", "a little bitch cunt", "a shithead", "a bitch", "a cunt", "an arsehead", "an arse", "an ass", "a motherfucker", "a pissbaby", "a prick", "a pussy", "a dick", "a cock", "a little dicksucking whore", "a slay", "a whore", "an idiot", "a jerk", "a slut", "a slutty little whore", "a loser", "a failure", "a waste of space", "a stupid bitch", "a motherfucking whore", "a jerkface", "a maggot", "an ass-kisser", "a redditor", "an airhead", "an idiot", "an asshole", "a bimbo", "a bozo", "a dipshit", "a dingleberry", "a shithead", "a son of a bitch", "a twat", "a wanker"]

# Sometimes a '?!' makes it 10x funnier.
punctuation_list = ["!", "...", ".", "?", "?!", "!!!", "!!", "..!"]


while True:
    user_input = input("")
    
    if user_input.lower() == 'exit':
        break

    # Check if person_names_list is not empty
    if not person_names_list:
        print("You must enter at least one name.")
        names_input = input("Enter the names you want to insult (comma-separated): ")
        person_names_list = [name.strip() for name in names_input.split(',')]

    random_name = random.choice(person_names_list)

    # Check if there are at least two unique names in person_names_list
    if len(person_names_list) > 1:
        # Ensure names are not the same
        random_name_2 = random.choice([name for name in person_names_list if name != random_name])
    else:
        # If theres 1 name, they are the same.
        random_name_2 = random_name

    random_con_word = random.choice(con_word_list)
    random_con_word_2 = random.choice(con_word_list)
    random_naughty_word = random.choice(naughty_words_list)
    random_naughty_word_2 = random.choice([name for name in naughty_words_list if name != random_naughty_word])
    random_naughty_word_3 = random.choice([name for name in naughty_words_list if name != random_naughty_word_2])
    random_punctuation = random.choice(punctuation_list)

    # Conjunctions
    comma = (",")
    and_1 = ("and")
    also = ("also")
    is_1 = ("is")
    too = ("too")


 # Sentences

        #Multiple Names
    if len(person_names_list) > 1:
        phrases = [
            "{} {} {}{}".format(random_name, random_con_word, random_naughty_word, random_punctuation),
            "{} {} {} {} {} {} {}{}".format(random_name, random_con_word, random_naughty_word, and_1, also, random_con_word_2, random_naughty_word_2, random_punctuation),
            "{} {} {} {} {}{}".format(random_name, random_con_word, random_naughty_word, and_1, random_naughty_word_2, random_punctuation),
            "{} {} {}{} {} {} {} {}{}".format(random_name, random_con_word, random_naughty_word, comma, and_1, random_name_2, is_1, too, random_punctuation),
            "{} {} {}{} {} {} {} {}{}".format(random_name, random_con_word, random_naughty_word, comma, and_1, random_name_2, is_1, also, random_punctuation),
            "{} {} {}{} {}{} {} {}{}".format(random_name, random_con_word, random_naughty_word, comma, random_naughty_word_2, comma, and_1, random_naughty_word_3, random_punctuation )
        ]
    else:
        # Single User
        phrases = [
            "{} {} {}{}".format(random_name, random_con_word, random_naughty_word, random_punctuation),
            "{} {} {} {} {} {} {}{}".format(random_name, random_con_word, random_naughty_word, and_1, also, random_con_word_2, random_naughty_word_2, random_punctuation),
            "{} {} {} {} {}{}".format(random_name, random_con_word, random_naughty_word, and_1, random_naughty_word_2, random_punctuation),
            "{} {} {} {} {}{} {} {}{}".format(random_name, random_con_word, random_naughty_word, comma, random_naughty_word_2, comma, and_1, random_naughty_word_3, random_punctuation )
        ]


    #Print The Insult

    random_phrase = random.choice(phrases)

    print(random_phrase)


    #DONE!
