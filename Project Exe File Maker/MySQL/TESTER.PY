import random
from datetime import datetime, timedelta

state_patterns = {
    'AN': r'AN\s\d{1,2}\s[A-Z]{1,2}\s\d{4}$',  # Andaman and Nicobar Islands
    'AP': r'AP\s\d{1,2}\s[A-Z]{1,2}\s\d{4}$',  # Andhra Pradesh
    'AR': r'AR\s\d{1,2}\s[A-Z]{1,2}\s\d{4}$',  # Arunachal Pradesh
    'AS': r'AS\s\d{1,2}\s[A-Z]{1,2}\s\d{4}$',  # Assam
    'BR': r'BR\s\d{1,2}\s[A-Z]{1,2}\s\d{4}$',  # Bihar
    'CH': r'CH\s\d{1,2}\s[A-Z]{1,2}\s\d{4}$',  # Chandigarh
    'CT': r'CT\s\d{1,2}\s[A-Z]{1,2}\s\d{4}$',  # Chhattisgarh
    'DD': r'DD\s\d{1,2}\s[A-Z]{1,2}\s\d{4}$',  # Dadra and Nagar Haveli and Daman and Diu
    'DL': r'DL\s\d{1,2}\s[A-Z]{1,2}\s\d{4}$',  # Delhi
    'DN': r'DN\s\d{1,2}\s[A-Z]{1,2}\s\d{4}$',  # Dadra and Nagar Haveli and Daman and Diu
    'GA': r'GA\s\d{1,2}\s[A-Z]{1,2}\s\d{4}$',  # Goa
    'GJ': r'GJ\s\d{1,2}\s[A-Z]{1,2}\s\d{4}$',  # Gujarat
    'HP': r'HP\s\d{1,2}\s[A-Z]{1,2}\s\d{4}$',  # Himachal Pradesh
    'HR': r'HR\s\d{1,2}\s[A-Z]{1,2}\s\d{4}$',  # Haryana
    'JH': r'JH\s\d{1,2}\s[A-Z]{1,2}\s\d{4}$',  # Jharkhand
    'JK': r'JK\s\d{1,2}\s[A-Z]{1,2}\s\d{4}$',  # Jammu and Kashmir
    'KA': r'KA\s\d{1,2}\s[A-Z]{1,2}\s\d{4}$',  # Karnataka
    'KL': r'KL\s\d{1,2}\s[A-Z]{1,2}\s\d{4}$',  # Kerala
    'LA': r'LA\s\d{1,2}\s[A-Z]{1,2}\s\d{4}$',  # Ladakh
    'LD': r'LD\s\d{1,2}\s[A-Z]{1,2}\s\d{4}$',  # Lakshadweep
    'MH': r'MH\s\d{1,2}\s[A-Z]{1,2}\s\d{4}$',  # Maharashtra
    'ML': r'ML\s\d{1,2}\s[A-Z]{1,2}\s\d{4}$',  # Meghalaya
    'MN': r'MN\s\d{1,2}\s[A-Z]{1,2}\s\d{4}$',  # Manipur
    'MP': r'MP\s\d{1,2}\s[A-Z]{1,2}\s\d{4}$',  # Madhya Pradesh
    'MZ': r'MZ\s\d{1,2}\s[A-Z]{1,2}\s\d{4}$',  # Mizoram
    'NL': r'NL\s\d{1,2}\s[A-Z]{1,2}\s\d{4}$',  # Nagaland
    'OD': r'OD\s\d{1,2}\s[A-Z]{1,2}\s\d{4}$',  # Odisha
    'PB': r'PB\s\d{1,2}\s[A-Z]{1,2}\s\d{4}$',  # Punjab
    'PY': r'PY\s\d{1,2}\s[A-Z]{1,2}\s\d{4}$',  # Puducherry
    'RJ': r'RJ\s\d{1,2}\s[A-Z]{1,2}\s\d{4}$',  # Rajasthan
    'SK': r'SK\s\d{1,2}\s[A-Z]{1,2}\s\d{4}$',  # Sikkim
    'TN': r'TN\s\d{1,2}\s[A-Z]{1,2}\s\d{4}$',  # Tamil Nadu
    'TR': r'TR\s\d{1,2}\s[A-Z]{1,2}\s\d{4}$',  # Tripura
    'TS': r'TS\s\d{1,2}\s[A-Z]{1,2}\s\d{4}$',  # Telangana
    'UK': r'UK\s\d{1,2}\s[A-Z]{1,2}\s\d{4}$',  # Uttarakhand
    'UP': r'UP\s\d{1,2}\s[A-Z]{1,2}\s\d{4}$',  # Uttar Pradesh
    'WB': r'WB\s\d{1,2}\s[A-Z]{1,2}\s\d{4}$',  # West Bengal
    'AN': r'AN\d{1,2}[A-Z]{1,2}\d{4}$',  # Andaman and Nicobar Islands
    'AP': r'AP\d{1,2}[A-Z]{1,2}\d{4}$',  # Andhra Pradesh
    'AR': r'AR\d{1,2}[A-Z]{1,2}\d{4}$',  # Arunachal Pradesh
    'AS': r'AS\d{1,2}[A-Z]{1,2}\d{4}$',  # Assam
    'BR': r'BR\d{1,2}[A-Z]{1,2}\d{4}$',  # Bihar
    'CH': r'CH\d{1,2}[A-Z]{1,2}\d{4}$',  # Chandigarh
    'CT': r'CT\d{1,2}[A-Z]{1,2}\d{4}$',  # Chhattisgarh
    'DD': r'DD\d{1,2}[A-Z]{1,2}\d{4}$',  # Dadra and Nagar Haveli and Daman and Diu
    'DL': r'DL\d{1,2}[A-Z]{1,2}\d{4}$',  # Delhi
    'DN': r'DN\d{1,2}[A-Z]{1,2}\d{4}$',  # Dadra and Nagar Haveli and Daman and Diu
    'GA': r'GA\d{1,2}[A-Z]{1,2}\d{4}$',  # Goa
    'GJ': r'GJ\d{1,2}[A-Z]{1,2}\d{4}$',  # Gujarat
    'HP': r'HP\d{1,2}[A-Z]{1,2}\d{4}$',  # Himachal Pradesh
    'HR': r'HR\d{1,2}[A-Z]{1,2}\d{4}$',  # Haryana
    'JH': r'JH\d{1,2}[A-Z]{1,2}\d{4}$',  # Jharkhand
    'JK': r'JK\d{1,2}[A-Z]{1,2}\d{4}$',  # Jammu and Kashmir
    'KA': r'KA\d{1,2}[A-Z]{1,2}\d{4}$',  # Karnataka
    'KL': r'KL\d{1,2}[A-Z]{1,2}\d{4}$',  # Kerala
    'LA': r'LA\d{1,2}[A-Z]{1,2}\d{4}$',  # Ladakh
    'LD': r'LD\d{1,2}[A-Z]{1,2}\d{4}$',  # Lakshadweep
    'MH': r'MH\d{1,2}[A-Z]{1,2}\d{4}$',  # Maharashtra
    'ML': r'ML\d{1,2}[A-Z]{1,2}\d{4}$',  # Meghalaya
    'MN': r'MN\d{1,2}[A-Z]{1,2}\d{4}$',  # Manipur
    'MP': r'MP\d{1,2}[A-Z]{1,2}\d{4}$',  # Madhya Pradesh
    'MZ': r'MZ\d{1,2}[A-Z]{1,2}\d{4}$',  # Mizoram
    'NL': r'NL\d{1,2}[A-Z]{1,2}\d{4}$',  # Nagaland
    'OD': r'OD\d{1,2}[A-Z]{1,2}\d{4}$',  # Odisha
    'PB': r'PB\d{1,2}[A-Z]{1,2}\d{4}$',  # Punjab
    'PY': r'PY\d{1,2}[A-Z]{1,2}\d{4}$',  # Puducherry
    'RJ': r'RJ\d{1,2}[A-Z]{1,2}\d{4}$',  # Rajasthan
    'SK': r'SK\d{1,2}[A-Z]{1,2}\d{4}$',  # Sikkim
    'TN': r'TN\d{1,2}[A-Z]{1,2}\d{4}$',  # Tamil Nadu
    'TR': r'TR\d{1,2}[A-Z]{1,2}\d{4}$',  # Tripura
    'TS': r'TS\d{1,2}[A-Z]{1,2}\d{4}$',  # Telangana
    'UK': r'UK\d{1,2}[A-Z]{1,2}\d{4}$',  # Uttarakhand
    'UP': r'UP\d{1,2}[A-Z]{1,2}\d{4}$',  # Uttar Pradesh
    'WB': r'WB\d{1,2}[A-Z]{1,2}\d{1,4}$',  # West Bengal
    'BH': r'\d{2}BH\d{4}[A-Z]{1,2}$'      ,  #BH Registration
    'BH11': r'\d{2}\sBH\s\d{4}\s[A-Z]{1,2}$',
    'BH1': r'\d{2}BH\d{4}\s[A-Z]{1,2}$',
    'DL1':r'DL\d{1}[A-Z]{1}\s[A-Z]{2}\s\d{4}$',#Delhi1
    'DL2':r'DL\d{1}[A-Z]{2}\s\d{4}$' 
    }

def generate_random_registration_number():
    state_code = random.choice(list(state_patterns.keys()))
    pattern = state_patterns[state_code]
    registration_number = ""

    while True:
        for char in pattern:
            if char == ' ':
                registration_number += ' '
            elif char == 'A':
                registration_number += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
            elif char == '0':
                registration_number += random.choice('0123456789')
            else:
                registration_number += char

            if len(registration_number) == len(pattern):
                return registration_number

def generate_random_date():
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31)
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    return random_date.strftime('%Y-%m-%d')

def generate_random_number():
    return random.randint(2, 50) * 10

if __name__ == "__main__":
    for _ in range(10):
        random_registration_number = generate_random_registration_number()
        random_date = generate_random_date()
        random_number = generate_random_number()
        
        formatted_number = str(random_number)
        
        print(f"Registration Number: {random_registration_number}")
        print(f"Date: {random_date}")
        print(f"Formatted Number: {formatted_number}\n")
