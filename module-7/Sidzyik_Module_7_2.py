# Made by: Samuel Sidzyik
# Module 7.2 Assignment.py
# Start Date February 12, 2026
# Finished 2/22/26

# Learning unit testing with simple print of country information
# Structure taken from provided chapter in Python Crash Course (2019) - Chapter 11

def main():
    while True:
        print ("Enter 'q' at any time to quit.")
        city = input("\nPlease give me a city: ")
        if city == 'q':
            break
        country = input("Please give me a country: ")
        if country == 'q':
            break
        
        formatted = get_formatted_locale(city,country)
        print(f"\tFormatted locale: {formatted}")



def get_formatted_locale(city,country,population='',language=''):
    """Generate a neatly formatted full name."""
    locale = f"{city}, {country}".title()
    if population != '':
        locale = locale + f' - population {population}'
    if language != '':
        locale = locale + f', {language}'
    return locale

if __name__ == "__main__":
    main()