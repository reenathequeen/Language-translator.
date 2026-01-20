import streamlit as st
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



st.title("Language Translator App")
st.markdown("Hello, Welcome to English Translator program.")
choose_language = st.sidebar.selectbox("Which Language would you like to translate to:", translators.keys())

if choose_language:
    current_dict = translators[choose_language]

    word_to_translate = st.selectbox( f"Select a word to translate to {choose_language.capitalize()}:",
                 options=[""] + list(current_dict.keys()))
    if st.button("Translate"):
        if word_to_translate:
            translation = current_dict.get(word_to_translate, "Translation not found.")
            st.divider()
            st.subheader(f"The translation of '{word_to_translate}' in {choose_language.capitalize()} is: {translation}")
            st.success(f"**{translation}**")
            st.write("Thank you for using the Language Translator App!")


