Project Overview: ShelfLife
1. Introduction
ShelfLife is a user-friendly, innovative application designed to assist users in efficiently tracking the expiration dates of their personal items, including food, medicine, and other perishable goods. With ShelfLife, users can ensure timely consumption, reduce waste, and maintain a well-organized inventory. The project leverages cutting-edge web technologies to provide a seamless and intuitive user experience.

The goal of ShelfLife is to bridge the gap between manual inventory management and automated solutions. By incorporating reminders, analytics, and a robust architecture, ShelfLife not only simplifies day-to-day tracking but also introduces features that encourage sustainable consumption habits. The project emphasizes accessibility, scalability, and performance to cater to a diverse user base, ranging from individuals to small businesses.

2. Requirements
Functional Requirements
Users must be able to register, log in, and log out securely using encrypted authentication mechanisms.
The application must allow users to add items to their inventory with fields such as:
Name
Category (e.g., food, medicine)
Expiration date
Quantity
Notes
Users must be able to edit or delete existing items in the inventory.
The application must send timely reminders for items approaching their expiration date.
Users should be able to customize notification preferences (e.g., email, SMS, or in-app).
The application must include a search and filter feature to help users sort and find items easily.
Non-functional Requirements
The app should maintain a response time of fewer than 2 seconds under normal load.
The application must support at least 10,000 active users concurrently without performance degradation.
The system should ensure data integrity and security by employing:
Encrypted database storage
Role-based access control
The UI must be responsive and adaptive for use on both desktop and mobile devices.
The application should be deployable across various environments using Docker containers.
3. Architecture
ShelfLife’s architecture is designed to be modular, scalable, and maintainable. The application employs a three-tier architecture:

Frontend:

Developed using Vue.js to create dynamic and responsive user interfaces.
Integration with Bootstrap for a clean, consistent design.
Font Awesome icons enhance visual clarity and improve the user experience.
Backend:

Flask serves as the core framework for API development, providing endpoints for user actions, inventory management, and notifications.
Implements secure authentication using libraries like Flask-Security.
Database:

PostgreSQL serves as the database, optimized for structured and efficient storage of user data and inventory items.
Includes features like indexing for faster search queries.
Testing:

A comprehensive QA framework built using Pytest ensures the reliability of individual components and the overall system.
Automated tests for API endpoints, database transactions, and UI interactions.
Continuous Integration/Continuous Deployment (CI/CD):

GitHub Actions is used to automate the build and deployment pipeline.
Docker containers streamline environment consistency across development, testing, and production.
4. Features
Inventory Management
Users can add, edit, and delete items in their inventory.
Categorization of items by type (e.g., food, medicine).
Real-time updates to the inventory display as changes are made.
Notifications
Customizable reminders for items approaching expiration.
Notifications sent via email, SMS, or in-app alerts based on user preference.
Dashboard widgets summarizing critical items requiring attention.
Analytics
Visual trends showing expired vs. consumed items over time.
Categorized insights into inventory usage for different item types.
Detailed statistics on waste reduction achieved through timely reminders.
5. Development Breakdown
Frontend
Contributions:
Developed by Tomas Chavarria using Vue.js.
Implemented the inventory dashboard and user settings interface.
Ensured responsiveness across devices using Bootstrap.
Backend
Contributions:
Mikhail Vorotnikov implemented Flask API endpoints for CRUD operations.
Integrated PostgreSQL for secure and efficient data storage.
Added support for role-based access control and secure authentication.
Testing
Contributions:
Led by Alejandro, who developed automated test suites for key modules.
Performed manual debugging of database integration and front-end-backend communication issues.
Identified and resolved over 30 critical bugs during QA.
Documentation
Contributions:
Authored by Alejandro, including detailed README updates.
Created diagrams illustrating system architecture and workflows.
Prepared user guides for onboarding and system usage.
6. Deployment
ShelfLife is containerized using Docker, allowing consistent deployment across development, staging, and production environments. The CI/CD pipeline ensures:

Automatic builds and tests upon each code push to the repository.
Seamless deployment to staging and production servers.
GitHub Actions facilitates integration with Docker Hub for image management, ensuring scalability and reliability.

7. Future Improvements
Planned Enhancements
Localization: Add multilingual support for non-English-speaking users.
Mobile Application: Develop a native mobile app for iOS and Android to improve accessibility.
AI Integration:
Implement predictive analytics to suggest optimal consumption patterns.
Use machine learning to identify trends in user inventory data.
Potential Features
Integration with grocery delivery APIs for automated restocking suggestions.
Advanced analytics dashboards for small businesses managing inventory.
Support for team-based inventory management (e.g., for families or roommates).