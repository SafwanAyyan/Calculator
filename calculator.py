import math
import sympy as sp
import requests
from bs4 import BeautifulSoup
import pint
from statistics import mean, median, mode, stdev
from datetime import datetime
import pyttsx3
import pyperclip
from colorama import init, Fore, Style, Back
import openai
import time
import itertools

# Initialize pint unit registry
ureg = pint.UnitRegistry()

# Initialize text-to-speech engine
tts_engine = pyttsx3.init()

# Initialize colorama
init(autoreset=True)

# Load your API keys
EXCHANGE_RATE_API_KEY = "PUT_YOUR_API_KEY_HERE"
WEATHER_API_KEY = "PUT_YOUR_API_KEY_HERE"
OPENAI_API_KEY = 'PUT_YOUR_API_KEY_HERE'

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
  - {Fore.BLUE}help{Style.RESET_ALL}: Display this help message
  - {Fore.BLUE}exit{Style.RESET_ALL}: Exit the calculator
"""
    return help_text

def print_centered_message(message):
    lines = message.split('\n')
    for line in lines:
        centered_line = line.center(80)  # assuming a width of 80 characters
        print(centered_line)

# Function to display current time
def display_current_time():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

# Simple startup animations
def startup_animation():
    print_centered_message("Starting Calculator")
    for _ in range(3):
        for frame in itertools.cycle(['|', '/', '-', '\\']):
            print(f"\r{Fore.CYAN}{frame}{Style.RESET_ALL}", end='', flush=True)
            time.sleep(0.2)
            if _ == 2: break
        time.sleep(0.2)  # Ensure the loop exits properly
    print(f"\r{Fore.CYAN}Calculator Ready! {Style.RESET_ALL}")

def print_box_with_text(text):
    lines = text.split('\n')
    width = max(len(line) for line in lines) + 4
    print(Fore.CYAN + '+' + '-' * width + '+')
    for line in lines:
        print(Fore.CYAN + '| ' + line.center(width - 2) + ' |')
    print(Fore.CYAN + '+' + '-' * width + '+')

def startup_message():
    startup_animation()
    welcome_message = f"Welcome to the Enhanced Terminal Calculator!\nMade by Safwan Ayyan"
    print_box_with_text(welcome_message)
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
            print_box_with_text(display_help())
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
        else:
            result = evaluate_expression(user_input)

        print(f"{Fore.CYAN + Style.BRIGHT}Result: {Style.RESET_ALL}{result}")
        log_history(f"{user_input} = {result}")

if __name__ == "__main__":
    main()
