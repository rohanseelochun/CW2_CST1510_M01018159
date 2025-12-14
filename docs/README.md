# Project for module CST1510 


# Week 7: Secure Authentication System
Student Name: Rohan Seelochun
Student ID: M01018159
Course: CST1510 -CW2 - Multi-Domain Intelligence Platform
## Project Description
A command-line authentication system implementing secure password hashing
This system allows users to register accounts and log in with proper pass
## Features
- Secure password hashing using bcrypt with automatic salt generation
- User registration with duplicate username prevention
- User login with password verification
- Input validation for usernames and passwords
- File-based user data persistence
## Technical Implementation
- Hashing Algorithm: bcrypt with automatic salting
- Data Storage: Plain text file (`users.txt`) with comma-separated values
- Password Security: One-way hashing, no plaintext storage
- Validation: Username (3-20 alphanumeric characters), Password (6-50 characters)


## Week 8: Data Pipeline & CRUD (SQL)

### Project Description
In Week 8, the project was extended by introducing a relational database.  
Database tables were created for all three domains, and full CRUD (Create, Read, Update, Delete) operations were implemented.

Data from CSV files and previously stored user credentials were migrated into the database to ensure consistency and persistence.

### Features
- Creation of the main SQLite `.db` database file  
- Database tables for cybersecurity incidents, IT tickets, datasets metadata, and users  
- Migration of CSV data and user records into database tables  
- Full CRUD functionality across all domains  
- Validation of database structure and data integrity  

### Technical Implementation
- **Database Engine:** SQLite  
- **Schema Definition:** SQL `CREATE TABLE` statements  
- **CRUD Operations:** Implemented using parameterized SQL queries  
- **Data Migration:** CSV files and `users.txt` imported into database tables  
- **Testing:** Verification of correct data insertion and retrieval


## Week 9: Web Interface, MVC & Visualisation

### Project Description
In Week 9, the system was transformed into an interactive web application using Streamlit.  
This allowed users to interact with the platform through dashboards, forms, and analytics pages instead of the command line.

### Features
- Structured web application with multiple pages  
- Secure login and registration system  
- Dashboard displaying data across all domains  
- Analytics page with visual representations of data  
- Ability to create, update, and delete records through the UI  
- Settings page for viewing account information and logging out  

### Technical Implementation
- **Framework:** Streamlit  
- **Session Management:** `st.session_state` for authentication and navigation  
- **Data Visualisation:** Streamlit built-in chart components  
- **Input Validation:** Ensures correct and valid user input  
- **Access Control:** Restricted page access for authenticated users only  


## Week 10: AI Integration

### Project Description
In Week 10, AI functionality was added as an extension to the Multi-Domain Intelligence Platform.  
The purpose of this stage was to demonstrate how an AI model can be integrated into an existing system to provide domain-specific assistance.

The AI assistants allow users to ask questions related to cybersecurity, IT operations, and data science, with responses generated based on the selected domain.

### Features
- Dedicated AI assistant page within the web application  
- Three separate tabs corresponding to the three domains  
- Domain-specific question handling  
- AI responses aligned with the selected domain’s expertise  
- Integration with existing system data  

### Technical Implementation
- **AI Model:** Gemini API  
- **Integration Method:** API-based request and response handling  
- **Data Handling:** Domain data loaded from the SQLite database  
- **Context Preparation:** Database records converted into string format  
- **Session Management:** Interaction history stored using `st.session_state`  
- **User Interface:** Tab-based navigation to select the AI assistant  