yoruba_dictionary = {
    "place": "ibi","wife": "aya","dog": "aja","pepper": "ata","body": "ara","hand": "owo",
    "day": "ọjọ́","money": "owo","coward": "ojo","yam": "iṣu","hair": "irun","heart": "ọkan",
    "drum": "ilù","town, city": "Ìlú",
}
igbo_words = {
    "hello": "ndewo","how": "kedu","yes": "ee","no": "mba","thank you": "daalụ","please": "biko",
    "money": "ego","water": "mmiri","fire": "ọkụ","house": "ụlọ","car": "ụgbọ ala","food": "nri",
    "mother": "nne","father": "nna","child": "nwa","friend": "enyi","tomorrow": "echi","today": "taa",
    "god": "Chineke","love": "ịhụnanya"
}
english_hausa_dict = {
    "i": "Ina","you": "Kai/Ke (m/f)","he": "Ya","she": "Ita","we": "Muna","they": "Suna",
    "hello": "Sannu","thank you": "Na gode","yes": "Eh","no": "A'a","water": "Ruwa","food": "Abinci",
    "time": "Lokaci","home": "Gida","word": "Kalma","big": "Babban","small": "Karami","hot": "Zafi",
    "light": "Haske","ask": "Tambaye"
}

tiv_dictionary = {
    "man": "nomso","fish": "eSu","bird": "5om","drink": "ngolime","eat": "ya yoxo","see": "nange",
    "hear": "ngua","sleep": "yawE","die": "gbo","kill": "Nwa ikoxe","come": "mvo/mva","give": "nawo/mnao",
    "sun": "yange","moon": "Ele","water": "ngolum","fire": "su","white": "popo","black": "o yili/yele",
    "night": "tuwu/ime","good": "ido"
}
ibibio_dictionary = {
    "water": "mmọọñ","house": "ufọk","food": "udia","love": "ima","sun": "uweme eyo","moon": "ofiong",
    "work": "utom", "sleep": "ede", "run": "fɛɣɛ́","walk": "njɔ̀k","talk": "nème","sing": "maí",
    "learn": "kpep", "book": "ehuhuo","pen": "pen", "car": "car", "mother": "eka","father": "ete",
    "friend": "udọ","light": "unwana"
}

translators = {
    "yoruba":yoruba_dictionary,
    "igbo":igbo_words,
    "hausa":english_hausa_dict,
    "tiv":tiv_dictionary,
    "ibibio":ibibio_dictionary,
}

english_words = {
    "yoruba": ["place","wife","dog","pepper","body","hand","day","money","coward","yam","hair","heart",
    "wisdom","child","know","eat, feed","water","house","drum","town, city"],

    "igbo": [ "hello","how","yes","no","thank you","please", "money","water","fire","house","car","food",
    "mother","father","child","friend", "tomorrow","today","god","love"],

    "hausa":["i", "you", "he","she","we","they","hello","thank you","yes","no","water","food","time",
    "home","word","big","small","hot","light","ask"],

    "tiv": ["man","fish","bird","drink","eat","see","hear","sleep","die","kill","come","give",
    "sun","moon","water","fire","white","black","night","good"],

    "ibibio":["water","house","food","love","sun","moon","work", "sleep", "run","walk","talk","sing",
              "learn", "book", "pen","car","mother","father""friend","light"],
}



def translate_word():
    print("Hello, Welcome to English Translator program.")
    print("Here are the languages available to translate to: Yoruba,Igbo,Hausa,Tiv and Ibibio")

    continue_translating = True

    while continue_translating:
        choose_language = (input("Type in the language would you like to make use of or 'exit' to quit: ")
                           .lower())
        if choose_language in translators:
            current_dict = translators[choose_language]
            english_translate = True
            while english_translate:
                print(f"These are the words available to translate to {choose_language.capitalize()}:"
                      f"{english_words[choose_language]}")
                english_word = input(
                    f"Enter an English word to translate to {choose_language.capitalize()} "
                    f"(or 'back' to choose another language): ").lower()
                if english_word == "back":
                    print("Here are the languages available to translate to: Yoruba,Igbo,Hausa,Tiv and Ibibio")
                    english_translate = False
                elif english_word in english_words[choose_language]:
                    translation = current_dict.get(english_word)
                    print(f"The {choose_language.capitalize()} translation for '{english_word}' is: "
                          f"'{translation}'")
                else:
                    print(f"Sorry, the word '{english_word}' is not in the {choose_language.capitalize()}"
                          f" dictionary.")
                print("-" * 20)

        elif choose_language == "exit":
            print("Goodbye")
            continue_translating = False
        else:
            print("Invalid language choice. Please select from the list above.")
            print("-" * 20)


translate_word()
