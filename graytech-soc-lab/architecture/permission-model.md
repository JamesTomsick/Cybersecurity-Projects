The Graytech lab uses a group-based access control model inspired by AGDLP.

Model

mermaid
flowchart TD
    User[User Account] --> GG[Global Department Group]
    GG --> DL[Domain Local Resource Group]
    DL --> NTFS[NTFS Modify Permission]
    NTFS --> Share[Department SMB Share]


Example

mermaid
flowchart TD
    GTUser[gt0001] --> HRUsers[GG_GT_HR_Users]
    HRUsers --> HRModify[DL_GT_HR_Modify]
    HRModify --> HRShare[GT-HR Share]


Why This Matters

This model separates user identity from resource permissions. Instead of assigning permissions directly to individual users, access is managed through groups.

This makes it easier to:

- Audit access
- Add or remove users from departments
- Review permissions
- Investigate unauthorized access
- Practice enterprise IAM concepts
