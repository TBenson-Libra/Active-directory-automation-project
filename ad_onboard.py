import csv
import string
import secrets

print("Initializing automated onboarding engine...")

# 1. New Hire List (Simulating an incoming ticket or HR spreadsheet)
new_hires = ["David Miller", "Sophia Patel", "Marcus Taylor", "Elena Rostova"]

# 2. Function to generate a secure, compliant temporary password
def generate_temp_password():
    # Define corporate password policy character pools
    letters_lower = string.ascii_lowercase
    letters_upper = string.ascii_uppercase
    digits = string.digits
    special_chars = "!@#$%^*"
    
    # Combine all allowed characters
    all_characters = letters_lower + letters_upper + digits + special_chars
    
    # Set standard corporate length
    password_length = 12
    
    # Randomly pick 12 characters from the pool securely
    temp_password = "".join(secrets.choice(all_characters) for i in range(password_length))
    return temp_password

# 3. Process the new hires and export the data
try:
    with open('new_hire_credentials.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write headers for your audit trail
        writer.writerow(['Full Name', 'Generated SamAccountName', 'Temporary Password', 'Status'])
        
        print("\n--- Processing New Employee Creation ---")
        
        for name in new_hires:
            # Create a standard Active Directory username (e.g., "David Miller" -> "dmiller")
            name_parts = name.lower().split()
            sam_account_name = name_parts[0][0] + name_parts[1]
            
            # Generate the secure temporary password
            password = generate_temp_password()
            
            print(f"👤 Created Account: {sam_account_name} | Password Staged")
            
            # Write data row to the spreadsheet
            writer.writerow([name, sam_account_name, password, 'Staged: Require Reset on First Login'])
            
    print("\n🎉 Success! 'new_hire_credentials.csv' has been generated in your folder.")

except Exception as e:
    print(f"System Error: {e}")
