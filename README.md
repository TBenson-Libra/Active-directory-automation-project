# Active-directory-automation-project
A project to help me learn python and crafting automation tools for active directory

A collection of operational Python scripts designed to automate routine system administration, user provisioning, and compliance auditing workflows within enterprise network environments.

## Scripts Included
1. **`ad_audit3.py` (Security & Offboarding Audit through IP address pinpointing)**
   - Scans directory data structures to identify inactive user accounts past a 90-day threshold.
   - Automatically flags accounts for deactivation and exports a structured compliance audit trail to CSV format.

2.**`ad_audit4.py` (Security & Offboarding Audit through local input)**
    - Scans directory data structures to identify inactive user accounts past a 90-day threshold.
   - Automatically flags accounts for deactivation and exports a structured compliance audit trail to CSV format.
   - uses local input within the code instead of scanning for an outside source connection


2. **`ad_onboard.py` (Automated Provisioning & IAM)**
   - Automates bulk user onboarding by parsing name directories into standard corporate `samAccountName` formatting.
   - Utilizes the cryptographically secure `secrets` library to auto-generate highly compliant, randomized temporary passwords.
   - Generates staging credentials ready for identity database injection.

## Technical Skills Demonstrated
- Automation & Scripting (Python 3)
- Identity & Access Management (IAM) Workflow Logic
- Data Parsing and Compliance Reporting (CSV engine)
- Software Security Best Practices (`secrets` library module)
