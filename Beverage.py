import speech_recognition as sr
import pyttsx3 as p
import array as arr

engine = p.init()


class select_Beverages():
    def get_category(self):

        def get_Coffee():
            coffee_list = {1: 'Oreo Coffe', 2: 'Cold Cofee', 3: 'Cold Coffee (sugar free)', 4: 'Hazlenut Cafe',
                           5: 'Iced Vanilla'}
            engine.say('choose your drink')
            engine.say('Select from')
            engine.runAndWait()
            print(coffee_list.items())

            r2 = sr.Recognizer()
            with sr.Microphone() as source:
                r2.adjust_for_ambient_noise(source)
                audio = r2.listen(source)

                '''to select the beverage use the keyword like Coffee , Iced tea etc'''
                try:
                    Chosen_Coffee = r2.recognize_google(audio)
                    print(Chosen_Coffee)
                except sr.UnknownValueError:
                    print("")
                except sr.RequestError:
                    print("")
            return Chosen_Coffee

        def get_IcedTea():
            icedTea_list = {1: 'Sugar free', 2: 'Lemon', 3: 'Peach'}
            engine.say('choose your drink')
            engine.say('Select from')
            engine.runAndWait()
            print(icedTea_list.items())

            r3 = sr.Recognizer()
            with sr.Microphone() as source:
                r3.adjust_for_ambient_noise(source)
                audio = r3.listen(source)

                # to select the beverage use the keyword like Coffee , Iced tea et
                try:
                    Chosen_Tea = r3.recognize_google(audio)
                    print(Chosen_Tea)
                except sr.UnknownValueError:
                    print("")
                except sr.RequestError:
                    print("")
            return Chosen_Tea

        def get_Shakes():
            Shakes_list = {1: 'Chocolate', 2: 'Chocolate Brownie', 3: 'Vanilla', 4: 'Oreo',
                           5: 'Salted Caramel and Peanut butter'}
            engine.say('choose your drink')
            engine.say('Select from')
            engine.runAndWait()
            print(Shakes_list.items())

            r5 = sr.Recognizer()
            with sr.Microphone() as source:
                r5.adjust_for_ambient_noise(source)
                audio = r5.listen(source)

                '''to select the beverage use the keyword like Coffee , Iced tea etc'''
                try:
                    Chosen_Shake = r5.recognize_google(audio)
                    print(Chosen_Shake)
                except sr.UnknownValueError:
                    print("")
                except sr.RequestError:
                    print("")
            return Chosen_Shake

        def get_Soda():
            Sodas_list = {1: 'Fresh Lime', 2: 'Fresh Lime (sugar free)', 3: 'Orange', 4: 'Pineapple', 5: 'Pomogranate',
                          6: 'Kiwi'}
            engine.say('choose your drink')
            engine.say('Select from')
            engine.runAndWait()
            print(Sodas_list.items())

            r4 = sr.Recognizer()
            with sr.Microphone() as source:
                r4.adjust_for_ambient_noise(source)
                audio = r4.listen(source)

                '''to select the beverage use the keyword like Coffee , Iced tea etc'''
                try:
                    Chosen_Soda = r4.recognize_google(audio)
                    print(Chosen_Soda)
                except sr.UnknownValueError:
                    print("")
                except sr.RequestError:
                    print("")
            return Chosen_Soda

        def get_Smoothies():
            Smoothies_list = {1: 'Bluleberry', 2: 'Passion Fruit', 3: 'Mixed Berries', 4: 'Fresh kiwi',
                              5: 'Strwberry'}
            engine.say('choose your drink')
            engine.say('Select from')
            engine.runAndWait()
            print(Smoothies_list.items())

            r6 = sr.Recognizer()
            with sr.Microphone() as source:
                r6.adjust_for_ambient_noise(source)
                audio = r6.listen(source)

                '''to select the beverage use the keyword like Coffee , Iced tea etc'''
                try:
                    Chosen_Smoothie = r6.recognize_google(audio)
                    print(Chosen_Smoothie)
                except sr.UnknownValueError:
                    print("")
                except sr.RequestError:
                    print("")
            return Chosen_Smoothie

        def get_Mojito():
            Mojito_list = {1: 'Lemon and Mint', 2: 'Orange', 3: 'Pomogrante', 4: 'Virgin Mojito'}
            engine.say('choose your drink')
            engine.say('Select from')
            engine.runAndWait()
            print(Mojito_list.items())

            r7 = sr.Recognizer()
            with sr.Microphone() as source:
                r7.adjust_for_ambient_noise(source)
                audio = r7.listen(source)

                '''to select the beverage use the keyword like Coffee , Iced tea etc'''
                try:
                    Chosen_Mojito = r7.recognize_google(audio)
                    print(Chosen_Mojito)
                except sr.UnknownValueError:
                    print("")
                except sr.RequestError:
                    print("")
            return Chosen_Mojito

        Beverages = ['Coffee', 'Iced Tea', 'Shakes', 'Fresh fruit soda', 'Smoothies', 'Mojito']
        engine.say('Please select the Category of beverage you want')
        engine.say('Select From')
        engine.runAndWait()
        for beverage in Beverages:
            print(beverage)

        r1 = sr.Recognizer()
        with sr.Microphone() as source:
            r1.adjust_for_ambient_noise(source)
            audio = r1.listen(source)

            '''to select the beverage use the keyword like Coffee , Iced tea etc'''
            try:
                Chosen_Beverage_Category = r1.recognize_google(audio)
                print(Chosen_Beverage_Category)
            except sr.UnknownValueError:
                print("")
            except sr.RequestError:
                print("")

        if 'shakes' in Chosen_Beverage_Category:
            chosen_beverage = get_Shakes()
            #print(chosen_beverage)

        elif 'coffee' in Chosen_Beverage_Category:
            chosen_beverage = get_Coffee()
            #print(chosen_beverage)

        elif 'iced tea' in Chosen_Beverage_Category:
            chosen_beverage = get_IcedTea()
            #print(chosen_beverage)

        elif 'soda' in Chosen_Beverage_Category:
            chosen_beverage = get_Soda()
            #print(chosen_beverage)

        elif 'smoothie' in Chosen_Beverage_Category:
            chosen_beverage = get_Smoothies()

        elif 'mojito' in Chosen_Beverage_Category:
            chosen_beverage = get_Mojito()

        return chosen_beverage