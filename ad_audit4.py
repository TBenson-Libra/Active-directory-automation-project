import csv
from datetime import datetime, timedelta

print("Initializing local Active Directory simulator...")

# 1. MOCK DATA: Simulating a live Active Directory query response
# This replicates the user attributes you would normally pull using 'ldap3'
mock_ad_directory = [
    {"cn": "John Doe", "mail": "jdoe@example.com", "days_since_login": 12},
    {"cn": "Alice Smith", "mail": "asmith@example.com", "days_since_login": 104},
    {"cn": "Bob Johnson", "mail": "bjohnson@example.com", "days_since_login": 5},
    {"cn": "Charlie Brown", "mail": "cbrown@example.com", "days_since_login": 210},
    {"cn": "Eva Martinez", "mail": "emartinez@example.com", "days_since_login": 92}
]

print("Successfully established mock local database state.")

# 2. Logic Threshold (90 Days)
cutoff_days = 90

# 3. Process and export data to a clean CSV audit report
try:
    with open('stale_users_report.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        # Writing the spreadsheet headers
        writer.writerow(['User Name', 'Email Address', 'Last Activity (Days)', 'Security Action Required']) 
        
        print("\n--- Starting Active Directory Audit Filter ---")
        
        # Loop through our local simulated AD directory
        for user in mock_ad_directory:
            # Check the security logic: is the user inactive for more than 90 days?
            if user["days_since_login"] > cutoff_days:
                print(f"⚠️ FLAG ENCOUNTERED: {user['cn']} has been inactive for {user['days_since_login']} days!")
                
                # Write the flagged stale user data into our spreadsheet rows
                writer.writerow([user['cn'], user['mail'], user['days_since_login'], 'Disable Account & Revoke Token'])
            else:
                print(f"✅ Safe Account: {user['cn']} logged in recently.")

    print("\n🎉 Success! 'stale_users_report.csv' has been generated in your folder.")

except Exception as e:
    print(f"System Error while generating spreadsheet: {e}")
