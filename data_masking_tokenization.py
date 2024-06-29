import pandas as pd
import os
import logging
from cryptography.fernet import Fernet
import argparse
import re
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Generate a key for encryption and decryption
def generate_key(key_path):
    key = Fernet.generate_key()
    with open(key_path, 'wb') as key_file:
        key_file.write(key)
    return key

# Load the encryption key
def load_key(key_path):
    return open(key_path, 'rb').read()

# Encrypt data
def tokenize_data(data, cipher_suite):
    try:
        token = cipher_suite.encrypt(data.encode())
        return token
    except Exception as e:
        logging.error(f"Error tokenizing data: {e}")
        return None

# Decrypt data
def detokenize_data(token, cipher_suite):
    try:
        data = cipher_suite.decrypt(token).decode()
        return data
    except Exception as e:
        logging.error(f"Error detokenizing data: {e}")
        return None

# Mask data
def mask_data(data):
    return '*' * len(data)

# Validate and mask/tokenize data based on patterns
def validate_and_process_data(df, sensitive_columns, process_function):
    for column in sensitive_columns:
        if column not in df.columns:
            logging.warning(f"Column {column} not found in the dataset")
            continue
        df[column] = df[column].apply(lambda x: process_function(str(x)) if re.match(r'\S+@\S+\.\S+|\d{3}-\d{2}-\d{4}|\d{3}-\d{3}-\d{4}', str(x)) else x)
    return df

# Main function
def main(input_file, output_file, sensitive_columns, key_path):
    try:
        # Read dataset
        df = pd.read_csv(input_file)
        logging.info(f"Loaded data from {input_file}")

        # Data Masking
        masked_df = df.copy()
        masked_df = validate_and_process_data(masked_df, sensitive_columns, mask_data)
        logging.info("Data masking completed")

        # Generate or load the key
        if not os.path.exists(key_path):
            key = generate_key(key_path)
            logging.info(f"Encryption key generated and saved to {key_path}")
        else:
            key = load_key(key_path)
            logging.info(f"Encryption key loaded from {key_path}")

        cipher_suite = Fernet(key)

        # Tokenization
        tokenized_df = df.copy()
        tokenized_df = validate_and_process_data(tokenized_df, sensitive_columns, lambda x: tokenize_data(x, cipher_suite))
        logging.info("Data tokenization completed")

        # Save tokenized dataframe to a file
        tokenized_df.to_csv(output_file, index=False)
        logging.info(f"Tokenized data saved to {output_file}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

# CLI setup
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Data Masking and Tokenization Script")
    parser.add_argument('input_file', help="Path to the input CSV file")
    parser.add_argument('output_file', help="Path to the output CSV file")
    parser.add_argument('sensitive_columns', nargs='+', help="List of sensitive columns to mask/tokenize")
    parser.add_argument('--key_path', default=os.getenv('KEY_PATH', 'secret.key'), help="Path to the encryption key file")
    args = parser.parse_args()

    main(args.input_file, args.output_file, args.sensitive_columns, args.key_path)
