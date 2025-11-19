# Project for module CST1510 

# Week 7: Secure Authentication System

**Student Name:** Rohan Seelochun  
**Student ID:** M01018159  
**Course:** CST1510 - CW2 - Multi-Domain Intelligence Platform  

## Project Description
A command-line authentication system implementing secure password hashing using bcrypt.  
This system allows users to register accounts and log in securely.

## Features
- Secure password hashing using bcrypt with automatic salt generation
- User registration with duplicate username prevention
- User login with password verification
- File-based user data persistence (`users.txt`)
- Simple interactive menu for Register/Login/Exit

## Technical Implementation
- **Hashing Algorithm:** bcrypt (with automatic salting)
- **Data Storage:** Plain text file (`users.txt`) with comma-separated values
- **Password Security:** One-way hashing, no plaintext storage
- **Validation:** Basic checks for username and password

## How to Run
1. Install dependencies:
   ```bash
   pip install bcrypt