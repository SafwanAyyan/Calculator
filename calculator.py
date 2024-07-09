import math
import sympy as sp
import requests
from bs4 import BeautifulSoup
import pint
from statistics import mean, median, mode, stdev
from datetime import datetime
from datetime import date, timedelta
from tabulate import tabulate
import pyttsx3
import pyperclip
from colorama import init, Fore, Style, Back
import openai
import json

# Initialize pint unit registry
ureg = pint.UnitRegistry()

# Initialize text-to-speech engine
tts_engine = pyttsx3.init()

# Initialize colorama
init(autoreset=True)

# Load your API keys
EXCHANGE_RATE_API_KEY = "your_exchange_rate_api_key."
WEATHER_API_KEY = "your_weather_api_key"
STOCK_API_KEY = "your_stock_api_key"
TRANSLATION_API_KEY = "your_translation_api_key"
OPENAI_API_KEY = 'your_openai_api_key'

openai.api_key = OPENAI_API_KEY

# Function definitions

def evaluate_expression(expression):
    try:
        result = sp.sympify(expression)
        return result
    except Exception as e:
        return f"Error: {e}"

def convert_units(quantity, from_unit, to_unit):
    try:
        quantity = float(quantity)
        from_quantity = quantity * ureg(from_unit)
        to_quantity = from_quantity.to(to_unit)
        return f"{to_quantity:.4f}"
    except Exception as e:
        return f"Error: {e}"

def convert_currency(amount, from_currency, to_currency):
    try:
        url = f"https://v6.exchangerate-api.com/v6/{EXCHANGE_RATE_API_KEY}/pair/{from_currency}/{to_currency}/{amount}"
        response = requests.get(url)
        data = response.json()
        if data["result"] == "error":
            return f"Error: {data['error-type']}"
        converted_amount = data["conversion_result"]
        return f"{converted_amount:.2f} {to_currency.upper()}"
    except Exception as e:
        return f"Error: {e}"

def convert_temperature(value, from_unit, to_unit):
    try:
        value = float(value)
        if from_unit == 'C':
            if to_unit == 'F':
                return f"{(value * 9 / 5) + 32:.2f} F"
            elif to_unit == 'K':
                return f"{value + 273.15:.2f} K"
        elif from_unit == 'F':
            if to_unit == 'C':
                return f"{(value - 32) * 5 / 9:.2f} C"
            elif to_unit == 'K':
                return f"{(value - 32) * 5 / 9 + 273.15:.2f} K"
        elif from_unit == 'K':
            if to_unit == 'C':
                return f"{value - 273.15:.2f} C"
            elif to_unit == 'F':
                return f"{(value - 273.15) * 9 / 5 + 32:.2f} F"
        return "Error: Invalid temperature conversion"
    except Exception as e:
        return f"Error: {e}"

def fetch_weather(location):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={WEATHER_API_KEY}&units=metric"
        response = requests.get(url)
        weather_data = response.json()
        if weather_data.get("cod") != 200:
            return f"Error: {weather_data.get('message')}"
        temp = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]
        return f"{temp}°C, {description.capitalize()}"
    except Exception as e:
        return f"Error: {e}"

def fetch_latest_news():
    try:
        response = requests.get("https://news.google.com/rss")
        soup = BeautifulSoup(response.content, features="xml")
        items = soup.findAll("item")[:5]
        news = [(item.title.text, item.link.text) for item in items]
        return news
    except Exception as e:
        return f"Error: {e}"

def prime_factorization(number):
    try:
        number = int(number)
        factors = sp.factorint(number)
        return factors
    except Exception as e:
        return f"Error: {e}"

def convert_base(number, base_from, base_to):
    try:
        number = int(number, base_from)
        if base_to == 10:
            return str(number)
        elif base_to == 2:
            return bin(number)[2:]
        elif base_to == 8:
            return oct(number)[2:]
        elif base_to == 16:
            return hex(number)[2:].upper()
        return "Error: Invalid base conversion"
    except Exception as e:
        return f"Error: {e}"

def calculate_statistics(data):
    try:
        data = list(map(float, data))
        stats = {
            'Mean': mean(data),
            'Median': median(data),
            'Mode': mode(data),
            'Standard Deviation': stdev(data)
        }
        return stats
    except Exception as e:
        return f"Error: {e}"

def log_history(entry):
    with open("calc_history.txt", "a") as file:
        file.write(f"{datetime.now()}: {entry}\n")

def view_history():
    try:
        with open("calc_history.txt", "r") as file:
            history = file.readlines()
        return ''.join(history)
    except Exception as e:
        return "No history available."

def speak_result(result):
    tts_engine.say(result)
    tts_engine.runAndWait()

def copy_to_clipboard(text):
    try:
        pyperclip.copy(text)
        return "Result copied to clipboard."
    except Exception as e:
        return f"Error: {e}"

def ask_chatgpt(question):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": question
                }
            ]
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"Error: {e}"

def fetch_definition(word):
    try:
        response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
        definition_data = response.json()
        return definition_data[0]['meanings'][0]['definitions'][0]['definition']
    except Exception as e:
        return f"Error: {e}"

def nth_root(value, n):
    try:
        value, n = float(value), float(n)
        result = value ** (1/n)
        return f"{result:.4f}"
    except Exception as e:
        return f"Error: {e}"

def factorial(value):
    try:
        value = int(value)
        result = math.factorial(value)
        return f"{result}"
    except Exception as e:
        return f"Error: {e}"

def display_help():
    help_text = f"""
{Fore.GREEN + Style.BRIGHT}Welcome to the Enhanced Terminal Calculator!{Style.RESET_ALL}
Supported Operations:
  +, -, *, /, sin(), cos(), tan(), log(), log10(), sqrt(), pow(), pi, e, gamma(), factorial(), round(), nth_root()
  Example: nth_root(27, 3) for cube root of 27.
Additional Options:
  - {Fore.BLUE}convert <quantity> <from_unit> <to_unit>{Style.RESET_ALL}: Unit conversion
  - {Fore.BLUE}exchange <amount> <from_currency> <to_currency>{Style.RESET_ALL}: Currency conversion
  - {Fore.BLUE}tempconvert <value> <from_unit> <to_unit>{Style.RESET_ALL}: Temperature conversion
  - {Fore.BLUE}baseconvert <number> <base_from> <base_to>{Style.RESET_ALL}: Base conversion
  - {Fore.BLUE}factorize <number>{Style.RESET_ALL}: Prime factorization
  - {Fore.BLUE}stats <number1> <number2> ... <numberN>{Style.RESET_ALL}: Basic statistics (mean, median, mode, standard deviation)
  - {Fore.BLUE}weather <location>{Style.RESET_ALL}: Fetch detailed weather information for location
  - {Fore.BLUE}news{Style.RESET_ALL}: Fetch the latest news
  - {Fore.BLUE}history{Style.RESET_ALL}: View calculation history
  - {Fore.BLUE}speak <result>{Style.RESET_ALL}: Speak the result
  - {Fore.BLUE}copy <result>{Style.RESET_ALL}: Copy the result to clipboard
  - {Fore.BLUE}chatgpt <question>{Style.RESET_ALL}: Ask ChatGPT a question
  - {Fore.BLUE}time{Style.RESET_ALL}: Display the current device time
  - {Fore.BLUE}define <word>{Style.RESET_ALL}: Fetch the definition of a word
  - {Fore.BLUE}calendar{Style.RESET_ALL}: Display the calendar
  - {Fore.BLUE}schedule <date> <task>{Style.RESET_ALL}: Schedule a task
  - {Fore.BLUE}remind <task>{Style.RESET_ALL}: Set a reminder
  - {Fore.BLUE}stock <symbol>{Style.RESET_ALL}: Fetch real-time stock price for the specified symbol
  - {Fore.BLUE}translate <target_language> <text>{Style.RESET_ALL}: Translate text into the specified target language
  - {Fore.BLUE}help{Style.RESET_ALL}: Display this help message
  - {Fore.BLUE}exit{Style.RESET_ALL}: Exit the calculator
"""
    return help_text

def print_boxed_message(message):
    lines = message.split('\n')
    max_length = max(len(line) for line in lines)
    print(Fore.CYAN + '+' + '-' * (max_length + 2) + '+')
    for line in lines:
        print(Fore.CYAN + '| ' + line.center(max_length) + ' |')
    print(Fore.CYAN + '+' + '-' * (max_length + 2) + '+')

# Function to display current time
def display_current_time():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

def display_calendar():
    today = date.today()
    calendar = []
    for i in range(-today.weekday(), 14 - today.weekday()):
        day = today + timedelta(days=i)
        calendar.append(day.strftime("%Y-%m-%d"))
    return "\n".join(calendar)

def schedule_task(date_str, task):
    try:
        with open("tasks.txt", "a") as file:
            file.write(f"{date_str}: {task}\n")
        return f"Task '{task}' scheduled for {date_str}."
    except Exception as e:
        return f"Error: {e}"

def set_reminder(task):
    try:
        with open("reminders.txt", "a") as file:
            file.write(f"{task}\n")
        return f"Reminder set for task: {task}"
    except Exception as e:
        return f"Error: {e}"

def fetch_stock_price(symbol):
    try:
        url = f"https://financialmodelingprep.com/api/v3/quote/{symbol}?apikey={STOCK_API_KEY}"
        response = requests.get(url)
        data = response.json()
        if not data:
            return "Error: Invalid stock symbol or no data available."
        stock_info = data[0]
        return f"{stock_info['symbol']}: ${stock_info['price']} (Last updated: {stock_info['timestamp']})"
    except Exception as e:
        return f"Error: {e}"

def translate_text(text, target_language):
    try:
        url = f"https://translation.googleapis.com/language/translate/v2"
        params = {
            'q': text,
            'target': target_language,
            'key': TRANSLATION_API_KEY
        }
        response = requests.post(url, params=params)
        translation_data = response.json()
        translated_text = translation_data['data']['translations'][0]['translatedText']
        return translated_text
    except Exception as e:
        return f"Error: {e}"

def startup_message():
    message = f"""
{Back.MAGENTA + Fore.WHITE + Style.BRIGHT}========================================================={Style.RESET_ALL}
{Back.MAGENTA + Fore.WHITE + Style.BRIGHT}         Welcome to the Enhanced Terminal Calculator!         {Style.RESET_ALL}
{Back.MAGENTA + Fore.WHITE + Style.BRIGHT}                   Made by Safwan Ayyan                       {Style.RESET_ALL}
{Back.MAGENTA + Fore.WHITE + Style.BRIGHT}========================================================={Style.RESET_ALL}
    """
    print(message)
    print(f"{Fore.YELLOW + Style.BRIGHT}Current Time: {Style.RESET_ALL}{display_current_time()}")
    print(f"{Fore.YELLOW + Style.BRIGHT}Type '{Fore.BLUE + 'help' + Fore.YELLOW}' for a list of commands.")
    print(f"{Fore.YELLOW + Style.BRIGHT}Type '{Fore.BLUE + 'exit' + Fore.YELLOW}' to quit.\n")

def main():
    result = ""  # Initialize result with an empty string
    startup_message()

    while True:
        user_input = input(f"{Fore.YELLOW + Style.BRIGHT}>>> {Style.RESET_ALL}")

        if user_input.lower() == 'exit':
            break
        elif user_input.lower() == 'help':
            print_boxed_message(display_help())
        elif user_input.lower().startswith('convert'):
            try:
                _, quantity, from_unit, to_unit = user_input.split()
                result = convert_units(quantity, from_unit, to_unit)
            except ValueError:
                result = "Error: Invalid input for convert command."
        elif user_input.lower().startswith('exchange'):
            try:
                _, amount, from_currency, to_currency = user_input.split()
                result = convert_currency(amount, from_currency, to_currency)
            except ValueError:
                result = "Error: Invalid input for exchange command."
        elif user_input.lower().startswith('tempconvert'):
            try:
                _, value, from_unit, to_unit = user_input.split()
                result = convert_temperature(value, from_unit.upper(), to_unit.upper())
            except ValueError:
                result = "Error: Invalid input for tempconvert command."
        elif user_input.lower().startswith('baseconvert'):
            try:
                _, number, base_from, base_to = user_input.split()
                result = convert_base(number, int(base_from), int(base_to))
            except ValueError:
                result = "Error: Invalid input for baseconvert command."
        elif user_input.lower().startswith('factorize'):
            try:
                _, number = user_input.split()
                result = prime_factorization(number)
            except ValueError:
                result = "Error: Invalid input for factorize command."
        elif user_input.lower().startswith('stats'):
            try:
                _, *data = user_input.split()
                result = calculate_statistics(data)
            except ValueError:
                result = "Error: Invalid input for stats command."
        elif user_input.lower().startswith('weather'):
            try:
                _, location = user_input.split()
                result = fetch_weather(location)
            except ValueError:
                result = "Error: Invalid input for weather command."
        elif user_input.lower().startswith('news'):
            news = fetch_latest_news()
            if isinstance(news, str):
                result = news  # If there's an error, news will be a string with the error message
            else:
                result = tabulate(news, headers=['Title', 'Link'])
        elif user_input.lower() == 'time':
            result = display_current_time()
        elif user_input.lower().startswith('history'):
            result = view_history()
        elif user_input.lower().startswith('speak'):
            _, *text = user_input.split()
            result = ' '.join(text)
            speak_result(result)
        elif user_input.lower().startswith('copy'):
            _, *text = user_input.split()
            result = ' '.join(text)
            result = copy_to_clipboard(result)
        elif user_input.lower().startswith('chatgpt'):
            _, *question = user_input.split()
            question = ' '.join(question)
            result = ask_chatgpt(question)
        elif user_input.lower().startswith('define'):
            try:
                _, word = user_input.split()
                result = fetch_definition(word)
            except ValueError:
                result = "Error: Invalid input for define command."
        elif user_input.lower().startswith('nth_root'):
            try:
                _, value, n = user_input.split()
                result = nth_root(value, n)
            except ValueError:
                result = "Error: Invalid input for nth_root command."
        elif user_input.lower().startswith('factorial'):
            try:
                _, value = user_input.split()
                result = factorial(value)
            except ValueError:
                result = "Error: Invalid input for factorial command."
        elif user_input.lower().startswith('calendar'):
            result = display_calendar()
        elif user_input.lower().startswith('schedule'):
            try:
                _, date_str, *task = user_input.split()
                task = ' '.join(task)
                result = schedule_task(date_str, task)
            except ValueError:
                result = "Error: Invalid input for schedule command."
        elif user_input.lower().startswith('remind'):
            try:
                _, *task = user_input.split()
                task = ' '.join(task)
                result = set_reminder(task)
            except ValueError:
                result = "Error: Invalid input for remind command."
        elif user_input.lower().startswith('stock'):
            try:
                _, symbol = user_input.split()
                result = fetch_stock_price(symbol)
            except ValueError:
                result = "Error: Invalid input for stock command."
        elif user_input.lower().startswith('translate'):
            try:
                _, target_language, *text = user_input.split()
                text = ' '.join(text)
                result = translate_text(text, target_language)
            except ValueError:
                result = "Error: Invalid input for translate command."
        else:
            result = evaluate_expression(user_input)

        print(f"{Fore.CYAN + Style.BRIGHT}Result: {Style.RESET_ALL}{result}")
        log_history(f"{user_input} = {result}")

if __name__ == "__main__":
    main()
