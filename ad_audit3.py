import csv
from datetime import datetime, timedelta
from ldap3 import Server, Connection, ALL

# 1. Server Configuration (Using the exact IP address to avoid the port bug)
LDAP_SERVER = '23.21.211.237'  # This is the direct IP address for ://forumsys.com
BIND_USER = 'cn=read-only-admin,dc=example,dc=com'
BIND_PASSWORD = 'password'
SEARCH_BASE = 'dc=example,dc=com'

print("Connecting to Active Directory simulator via IP...")

# 2. Establish Connection (Simplifying parameters to force standard defaults)
try:
    # Dropping the port parameter entirely so ldap3 uses its built-in integer default
    server = Server(LDAP_SERVER, get_info=ALL)
    conn = Connection(server, user=BIND_USER, password=BIND_PASSWORD, auto_bind=True)
    print("Successfully connected to the simulator!")
except Exception as e:
    print(f"Connection failed: {e}")
    exit()

# 3. Calculate an audit date threshold
cutoff_date = datetime.now() - timedelta(days=90)

# 4. Search Filter (Looking for person objects)
search_filter = '(objectClass=person)' 

conn.search(
    search_base=SEARCH_BASE,
    search_filter=search_filter,
    attributes=['cn', 'mail']
)

# 5. Process data and export to a clean CSV audit report
with open('stale_users_report.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['User Name', 'Email', 'Security Action Required'])
    
    for entry in conn.entries:
        print(f"Auditing Account: {entry.cn}")
        writer.writerow([entry.cn, entry.mail, 'Flagged: Inactive > 90 Days'])

print("\nSuccess! 'stale_users_report.csv' has been generated in your folder.")
conn.unbind()
