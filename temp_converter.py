#Python program to calculate the Fahrenheit equivalent of a Celsius temperature and issue a weather statement based on the Fahrenheit temperature.
# Author: Adam Frederick
#  22 Feb 2026
#






def converter (tempC):
    tempF = round(tempC * (9/5) + 32)
    return tempF

def weather_statement(tempF):
    # print(f'temp is {tempF}')
    if tempF >= 95:
        return " A heat avdisory has been issued"
    elif tempF <=94 and tempF >=85:
        return "Plessant but warm"
    elif tempF <=84 and tempF >=70:
        return " Very pleasant but weather today"
    elif tempF <= 69 and tempF >= 50:
        return "Pleasant but cool"
    elif tempF <= 49 and tempF >= 33:
        return " Cold weather"
    elif tempF <= 32:
        return "A freeze warning has been issued"
    else:
        return "An invalid tempature has been processed, check your data!"
    
# converted_temp = converter(-1)
# issued_statement = weather_statement(converted_temp)
temp_list =[35.5, 30.5, 22.2, 16.1, 7.3, -1]
        
# print(f'{converted_temp}.{issued_statement} ')
# def list_test(temps):
#     for temp in temps:
#         print(f'{temp}C.')n

# list_test(temp_list)
# print("help")

def weather_statement_issue(temps):
    for temp in temps:
        conv_temp = converter(temp)
        iws= weather_statement(conv_temp)
        print(f'The temperature is {temp}\u00b0C or {conv_temp}\u00b0F. {iws}')

# weather_statement_issue(temp_list)




def launch ():
    descission = input("Would you like to test with the default list? [y/n]:")
    if descission.lower() == 'y':
           weather_statement_issue(temp_list)
    else:
        user_number = input("What temperature (in Celcius) would you like to issue a statement on? [enter number]: ")
        user_temp = [int(user_number)]
        weather_statement_issue(user_temp)

launch()  