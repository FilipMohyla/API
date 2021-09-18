import requests

date_input = input("Zadej datum ve formátu DD.MM.YYYY: ")

while True:
    def get_request():
        ### This function gets and make a list of exchange rates text in given day ###
        
        api_url = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt;jsessionid=D425EFE65F34D093A695131816F3D2B8?date=" + date_input
        request = requests.get(api_url)
        request = request.text
        request = request.split("\n")
        del request[0:2], request[-1]

        return request


    def split_record():
        ### This function splits records in rows into individual records ###
        list_of_exchange_rates = []

        for row in get_request():
            
            row = row.split("|")
            list_of_exchange_rates.append(row)
        
        return list_of_exchange_rates


    def ex_rates_keys_values():
        ### This function returns a dictionary consents symbol of currency as its key 
        # and values(price, country, currency and ammount of currency) ###   
        values = {}

        for i in split_record():
            
            if "," in i[-1]:

                i[-1] = i[-1].replace(",", ".")

            values[i[-2]] = [float(i[-1]), i[0], i[1], i[2]]
        
        return values


    def exchange_rates_counting():
        ###This function takes currency symbol & amout to exchange as user input and display how much he can exchange###
        
        for record in split_record():

            print(f"{record[0]} - {record[3]}")

        print()
        symbol_choice = input("Zvol si symbol ze seznamu výše: ").upper()
        money_to_exchange = int(input("Zadej, kolik Kč chceš směnit: "))
        user_choice = ex_rates_keys_values()[symbol_choice]

        if user_choice[-1] == "1":

            print(f"""
            Zvolil/a sis symbol pro {user_choice[1]}
            Kurz ze dne {date_input} je {user_choice[0]} Kč za 1 {user_choice[2]} 
            Za {money_to_exchange} Kč dostaneš {round(money_to_exchange / user_choice[0], 2)} {user_choice[2]}""")

        if user_choice[-1] == "100":

            print(f"""
            Zvolil/a sis symbol pro {user_choice[1]}
            Kurz ze dne {date_input} je {user_choice[0]} Kč za 100 {user_choice[2]} 
            Za {money_to_exchange} Kč dostaneš {round((money_to_exchange / user_choice[0]) * 100, 2)} {user_choice[2]}""")

        if user_choice[-1] == "1000":

            print(f"""
            Zvolil/a sis symbol pro {user_choice[1]}
            Kurz ze dne {date_input} je {user_choice[0]} Kč za 1000 {user_choice[2]} 
            Za {money_to_exchange} Kč dostaneš {round((money_to_exchange / user_choice[0]) * 1000, 2)} {user_choice[2]}""")

    exchange_rates_counting()
    print()
    ask_continue = input("Chceš se podívat i na jiný den (y/n)?")

    if ask_continue == "y":
        date_input = input("Zadej datum ve formátu DD.MM.YYYY: ")
        api_url = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt;jsessionid=D425EFE65F34D093A695131816F3D2B8?date=" + date_input
        
    else:

        break
