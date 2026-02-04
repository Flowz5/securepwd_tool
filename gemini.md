# SecurePwd Pro Project Analysis

This document provides a summary of the SecurePwd Pro project, a Python-based tool for password security.

## Project Overview

*   **Project Name:** SecurePwd Pro
*   **Description:** A command-line utility for generating strong random passwords, analyzing their strength (entropy), and checking for previous exposure in data breaches.
*   **Programming Language:** Python
*   **Key Features:**
    *   Secure password generation.
    *   Password entropy calculation.
    *   Verification against the HaveIBeenPwned database to check for leaks.
    *   User-friendly and colorful terminal interface.

## Core Components

### `main.py`

This is the main script of the project. It contains the following key functions:

*   `generate_password(length)`: Creates a password of a specified length using the `secrets` module for cryptographic-strength randomness.
*   `calculate_entropy(password)`: Computes the entropy of the password in bits, which is a measure of its unpredictability.
*   `check_pwned_api(password)`: Securely checks if the password has appeared in any known data breaches by querying the HaveIBeenPwned API using the "k-Anonymity" model.
*   `run()`: The entry point of the application. It prompts the user for a desired password length, calls the other functions to generate and analyze the password, and then displays the results in a well-formatted table in the console.

### `requirements.txt`

This file lists the external libraries required by the project:

*   `requests`: Used to make HTTP requests to the HaveIBeenPwned API.
*   `rich`: A library for creating rich and beautiful command-line interfaces, used here to display the analysis results.

## How to Run the Project

1.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
2.  **Run the script:**
    ```bash
    python main.py
    ```

The tool will then prompt for a password length and output the generated password along with its security analysis.
