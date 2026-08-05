Graytech Active Directory Deployment Summary

Domain

graytech.local

Company

Graytech

Summary

The Graytech lab is a fictional Active Directory environment created for SOC analyst training and cybersecurity portfolio development.

Objects Created

| Object Type     | Count |
|-----------------|-------|
| Fictional Users | 100   |
| Departments     | 15    |
| Department OUs  | 15    |
| Role Groups     | 17    |
| Resource Groups | 15    |
| SMB Shares      | 15    |

Department List

- Human Resources
- Finance
- Information Technology
- Security Operations
- Engineering
- Sales
- Marketing
- Legal
- Customer Support
- Operations
- Research
- Product Management
- Procurement
- Facilities
- Executive

Access Control Model

The lab uses an AGDLP-style permission model:

User Account
  -> Global Department Group
  -> Domain Local Resource Group
  -> SMB Share / NTFS Permission


Example:

gt0001
  -> GG_GT_HR_Users
  -> DL_GT_HR_Modify
  -> GT-HR Share


Security Notes

- No real employee data is used.
- All users are fictional.
- Passwords and secrets are not stored in this repository.
- Initial password exports are kept off GitHub.
