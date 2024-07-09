**🚀 Advanced Terminal Calculator 🧮**
======================================

![Calculator Image](https://img.freepik.com/free-vector/calculator-floating-cartoon-vector-icon-illustration-finance-business-icon-concept-isolated-flat_138676-9297.jpg?w=826&t=st=1720361971~exp=1720362571~hmac=6d06ff83027303a5356db5167b25b3deee7c3a26821a6cff68cf461aa23ab56e)

**Welcome to the Advanced Terminal Calculator!**

This tool combines the functionalities of a calculator, unit converter, weather forecaster, and more into a single terminal-based interface. With integrated APIs and advanced mathematical functions, it's designed to cater to both casual and professional users. 🤓🔢

* * * * *

**📚 Table of Contents**
------------------------

-   [Features](#features)
-   [Getting Started](#getting-started)
    -   [Prerequisites](#prerequisites)
    -   [Installation](#installation)
    -   [Running the Tool](#running-the-tool)
-   [Help Section](#help-section)
    -   [Mathematical Operations](#mathematical-operations)
    -   [Unit Conversions](#unit-conversions)
    -   [Currency Conversion](#currency-conversion)
    -   [Temperature Conversion](#temperature-conversion)
    -   [Base Conversion](#base-conversion)
    -   [Prime Factorization](#prime-factorization)
    -   [Statistics Calculation](#statistics-calculation)
    -   [Weather Information](#weather-information)
    -   [Latest News](#latest-news)
    -   [Time](#time)
    -   [History Operations](#history-operations)
    -   [Voice Assistance](#voice-assistance)
    -   [Copy to Clipboard](#copy-to-clipboard)
    -   [GPT-3.5 Turbo Integration](#gpt-35-turbo-integration)
    -   [Define Words](#define-words)
    -   [Display Help](#display-help)
    -   [Exit](#exit)
-   [Contributing](#contributing)
-   [License](#license)

* * * * *

**🌟 Features**
---------------

-   💱 **Currency Conversion**: Convert amounts between different currencies.
-   🌦️ **Weather Forecasting**: Fetch weather information for any location.
-   📰 **News Retrieval**: Get the latest news headlines.
-   🧮 **Mathematical Functions**: Perform a wide range of mathematical operations.
-   🤖 **Integration with GPT-3.5 Turbo**: Chat with OpenAI's ChatGPT.
-   🎙️ **Voice Assistance**: Use TTS to read out the results.
-   📜 **History Logging**: Log and retrieve previous calculations.
-   🔢 **Unit Conversion**: Convert between different units of measurement.
-   🌡️ **Temperature Conversion**: Convert temperatures between Celsius, Fahrenheit, and Kelvin.
-   🧩 **N-th Root and Factorial Calculations**: Perform advanced mathematical operations.
-   🔄 **Base Conversion**: Convert numbers between different bases, such as binary, decimal, octal, and hexadecimal.
-   🧮 **Prime Factorization**: Find the prime factors of a number.
-   📊 **Statistics Calculation**: Calculate basic statistics such as mean, median, mode, and standard deviation.
-   🕰️ **Current Time**: Display the current device time.

* * * * *

**🚀 Getting Started**
----------------------

### **🔧 Prerequisites**

-   **Python 3.x**
-   Required Python packages (install using `pip install -r requirements.txt`)

### **💻 Installation**

1.  **Clone the repository:**

    `git clone https://github.com/SafwanAyyan/Calculator`

2.  **Install dependencies:**

    `pip install -r requirements.txt`

### **▶️ Running the Tool**

To start the calculator, run:

`python calculator.py`

* * * * *

**🆘 Help Section**
-------------------

### **🧮 Mathematical Operations**

Supports a wide range of mathematical operations, from basic arithmetic to advanced functions.

-   Basic operations: Addition (+), Subtraction (-), Multiplication (*), Division (/)
    -   Example: `2 + 2`
-   Trigonometric functions: `sin`, `cos`, `tan`
    -   Example: `sin(30)`
-   Logarithmic functions: `log` (natural logarithm), `log10` (base 10 logarithm)
    -   Example: `log(10)`
-   Square root: `sqrt`
    -   Example: `sqrt(16)`
-   Exponential functions: `pow(base, exp)` or `base**exp`
    -   Example: `pow(2, 3)` or `2**3`
-   Constants: `pi`, `e`
-   N-th Root: `nth_root(value, n)`
    -   Example: `nth_root(27, 3)`
-   Factorial: `factorial`
    -   Example: `factorial(5)`

### **🔢 Unit Conversions**

Convert units from one measurement to another.

-   Usage:
    -   `convert <quantity> <from_unit> <to_unit>`
    -   Example: `convert 10 km mi` (Convert 10 kilometers to miles)

### **💱 Currency Conversion**

Convert amounts from one currency to another using real-time exchange rates.

-   Usage:
    -   `exchange <amount> <from_currency> <to_currency>`
    -   Example: `exchange 100 USD EUR` (Convert 100 US Dollars to Euros)

### **🌡️ Temperature Conversion**

Convert temperatures between Celsius, Fahrenheit, and Kelvin.

-   Usage:
    -   `tempconvert <value> <from_unit> <to_unit>`
    -   Example: `tempconvert 30 C F` (Convert 30 Celsius to Fahrenheit)

### **🔄 Base Conversion**

Convert numbers between different bases, such as binary, decimal, octal, and hexadecimal.

-   Usage:
    -   `baseconvert <number> <base_from> <base_to>`
    -   Example: `baseconvert 1010 2 10` (Convert binary 1010 to decimal)

### **🧮 Prime Factorization**

Find the prime factors of a number.

-   Usage:
    -   `factorize <number>`
    -   Example: `factorize 36`

### **📊 Statistics Calculation**

Calculate basic statistics such as mean, median, mode, and standard deviation.

-   Usage:
    -   `stats <number1> <number2> ... <numberN>`
    -   Example: `stats 1 2 3 4 5` (Calculates mean, median, mode, and standard deviation)

### **🌦️ Weather Information**

Fetch detailed weather information for a specified location.

-   Usage:
    -   `weather <location>`
    -   Example: `weather London`

### **📰 Latest News**

Fetch the latest news headlines.

-   Usage:
    -   `news`

### **🕰️ Time**

Display the current device time.

-   Usage:
    -   `time`

### **📜 History Operations**

Log and retrieve previous calculations.

-   Log Calculation: Automatically logs each calculation.
-   Retrieve History:
    -   `history`

### **🎙️ Voice Assistance**

Speak out the result of calculations.

-   Usage:
    -   `speak <result>`
    -   Example: `speak The result is 42`

### **📋 Copy to Clipboard**

Copy the result to your clipboard.

-   Usage:
    -   `copy <result>`
    -   Example: `copy The result is 42`

### **🤖 GPT-3.5 Turbo Integration**

Ask questions and get responses from OpenAI's ChatGPT.

-   Usage:
    -   `chatgpt <question>`
    -   Example: `chatgpt How are you?`

### **📚 Define Words**

Fetch word definitions using an online dictionary API.

-   Usage:
    -   `define <word>`
    -   Example: `define algorithm`

### **❓ Display Help**

Display the help message.

-   Usage:
    -   `help`

### **🚪 Exit**

Exit the calculator.

-   Usage:
    -   `exit`

* * * * *

**🤝 Contributing**
-------------------

Contributions are welcome! Fork the repository and submit a pull request with your improvements. Make sure your changes are well-documented and tested. 🌟

* * * * *

**📜 License**
--------------

This project is licensed under the MIT License.

* * * * *

**📋 Requirements**
-------------------

### **requirements.txt**

`sympy==1.9
requests==2.26.0
beautifulsoup4==4.10.0
pint==0.18
tabulate==0.8.9
pyttsx3==2.90
pyperclip==1.8.2
colorama==0.4.4
openai==0.12.0`
