```markdown
# Data Masking and Tokenization

# Overview

This project provides a robust solution for masking and tokenizing sensitive data in datasets using Python. The script utilizes the `pandas` library for data manipulation and the `cryptography` library for secure tokenization. The main goal is to protect sensitive information in datasets before storing them in cloud databases or sharing them across different platforms.

# Features

- Dynamic Column Selection: Users can specify which columns contain sensitive data.
- Data Masking: Replace sensitive data with masked values.
- Tokenization: Encrypt and replace sensitive data with tokens.
- Secure Key Storage: Encryption keys are securely stored and managed.
- Pattern Matching: Identify and validate sensitive data patterns before processing.
- Environment Variable Support: Manage key paths using environment variables.
- Logging: Detailed logging to track script execution and issues.

# Prerequisites

- Python 3.6 or higher
- `pandas` library
- `cryptography` library
- `python-dotenv` library

# Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Damilola-Yinusa/data-masking-tokenization.git
    cd data-masking-tokenization
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install pandas cryptography python-dotenv
    ```

4. Set up the environment variables:

    Create a `.env` file in the root directory of the project and add the following line (optional):

    ```env
    KEY_PATH=path/to/secret.key
    ```

# Usage

1. Prepare your input CSV file: Ensure you have a CSV file with the data you want to mask and tokenize.

2. Run the script:

    ```bash
    python enhanced_data_masking_tokenization.py input_data.csv output_data.csv email phone ssn --key_path=my_secret.key
    ```

    Replace `input_data.csv` with the path to your input file, `output_data.csv` with the desired output file path, and `email phone ssn` with the columns you want to mask and tokenize. The `--key_path` argument is optional and can be omitted if you use the `.env` file.

# Example

Given a CSV file `sample_data.csv` with the following content:

```csv
name,email,phone,ssn
Alice,alice@example.com,123-456-7890,111-22-3333
Bob,bob@example.com,987-654-3210,444-55-6666
Charlie,charlie@example.com,555-555-5555,777-88-9999
```

Running the script:

```bash
python enhanced_data_masking_tokenization.py sample_data.csv output_data.csv email phone ssn
```

Will generate `output_data.csv` with masked and tokenized values for the specified columns.

# Security

- Ensure the encryption key (`secret.key`) is stored securely and not exposed in your source code or public repositories.
- Use environment variables to manage sensitive paths and configurations.

# Contributing

I welcome contributions to enhance the functionality and security of this project. Please open an issue or submit a pull request.


