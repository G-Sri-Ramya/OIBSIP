# OIBSIP
# OASIS INFOBYTE PYTHON PROGRAMMING INTERNSHIP

## Internship Domain

Python Programming

## Overview

This repository contains the Python projects completed as part of the Oasis Infobyte Python Programming Internship. The projects demonstrate fundamental Python concepts such as user input handling, conditional statements, loops, exception handling, functions, modules and command-line applications.

---

# Project 1: BMI Calculator

## Objective

To calculate the Body Mass Index (BMI) of a person based on height and weight and determine the corresponding health category.

## Tools Used

* Python 3
* Visual Studio Code

## Concepts Used

* User Input
* Arithmetic Operations
* Conditional Statements
* Exception Handling

## Steps Performed

1. Accepted height in meters from the user.

2. Accepted weight in kilograms from the user.

3. Calculated BMI using the formula:

   BMI = Weight / (Height × Height)

4. Displayed the BMI value.

5. Categorized the result as:

   * Underweight
   * Normal Weight
   * Overweight
   * Obesity

## Sample Output

=== BMI Calculator ===

Enter your height in meters : 1.65

Enter your weight in kilograms : 55

BMI = 20.20

Normal Weight

## Outcome

Successfully calculated BMI and classified the user's health status based on standard BMI ranges.

---

# Project 2: Password Generator

## Objective

To generate strong and secure passwords according to user preferences.

## Tools Used

* Python 3
* string module
* secrets module
* Visual Studio Code

## Concepts Used

* Functions
* Random Password Generation
* String Manipulation
* User Input Validation

## Steps Performed

1. Accepted desired password length.
2. Allowed users to choose:

   * Letters
   * Numbers
   * Symbols
3. Generated a random password using secure random selection.
4. Displayed the generated password.

## Features

* Custom password length
* Optional letters
* Optional numbers
* Optional symbols
* Secure password generation

## Sample Output

=== Command-Line Password Generator ===

Enter desired password length : 12

Include letters? (y/n): y

Include numbers? (y/n): y

Include symbols? (y/n): y

Generated Password:

aD#7xP!4kL@9

## Outcome

Successfully generated strong passwords based on user-selected criteria while ensuring randomness and security.

---

# Project 3: Weather Application

## Objective

To develop a command-line weather application that fetches current weather information for a user-specified city.

## Tools Used

* Python 3
* Requests Library
* Visual Studio Code

 Concepts Used
- HTTP Requests
- Web Service Integration
- Loops
- Exception Handling
- User Input Handling

## Steps Performed

1. Accepted a city name from the user.
2. Constructed a weather service URL using the entered city name.
3. Sent an HTTP GET request using the Requests library.
4. Retrieved current weather information from the wttr.in web service.
5. Displayed the weather information in the terminal.
6. Allowed users to perform multiple searches.
7. Terminated the application when the user entered "exit".

## Features

* Live weather updates
* Multiple city searches
* No API key required
* Simple command-line interface

## Sample Output

Enter city name (or 'exit'): Hyderabad

Hyderabad: 🌦 +30°C

Enter city name (or 'exit'): London

London: ⛅ +18°C

## Outcome

Successfully retrieved and displayed real-time weather information for user-specified cities using an online weather service.

---

# Technologies Used

* Python 3
* Requests Library
* String Module
* Secrets Module
* Visual Studio Code

---

# Learning Outcomes

Through these projects, the following concepts were learned:

* Python Programming Fundamentals
* Conditional Statements
* Loops
* Functions
* Exception Handling
* String Manipulation
* Secure Random Data Generation
* HTTP Requests and Responses
* Command-Line Application Development

---

# Conclusion

The internship projects provided practical exposure to Python programming and real-world application development. The BMI Calculator demonstrated mathematical computations and decision-making, the Password Generator showcased secure random password generation, and the Weather Application introduced web service integration and real-time data retrieval. Together, these projects strengthened problem-solving skills and improved understanding of Python development.
