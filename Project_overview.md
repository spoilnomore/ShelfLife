# Project Overview: ShelfLife

## 1. Introduction
ShelfLife is a user-friendly application designed to help users track the expiration dates of their items, such as food, medicine, and other perishable goods. The project leverages modern web technologies to provide a seamless user experience.

---

## 2. Requirements
### Functional Requirements
1. Users can create an account and log in securely.
2. Items can be added, edited, or deleted from the inventory.
3. Expiration dates are tracked, with reminders sent via notifications.

### Non-functional Requirements
1. The app should respond within 2 seconds under normal load.
2. It should support at least 10,000 active users simultaneously.

---

## 3. Architecture
ShelfLife employs the following architecture:
- **Frontend**: Vue.js framework for dynamic and responsive UI.
- **Backend**: Flask for handling API requests and database interactions.
- **Database**: PostgreSQL for storing user data and item information.
- **Testing**: A QA framework with automated unit and integration tests.
- **CI/CD**: Continuous Integration with GitHub Actions.

---

## 4. Features
1. **Inventory Management**:
   - Add items with details like name, category, and expiration date.
   - Edit or delete items as needed.

2. **Notifications**:
   - Reminders for items nearing expiration.
   - Customizable notification settings.

3. **Analytics**:
   - View trends in expired vs. consumed items.
   - Categorized insights into inventory usage.

---

## 5. Development Breakdown
### Contributions
- **Frontend**:
  - Developed by Tomas Chavarria using Vue.js and Bootstrap.
  - Integrated icons using Font Awesome.

- **Backend**:
  - Mikhail Vorotnikov implemented the Flask-based API logic.
  - Includes features like secure authentication and optimized database queries.

- **Testing**:
  - Led by Alejandro, focusing on creating a robust QA framework.
  - Debugged database integration and API routes.

- **Documentation**:
  - README updates and comprehensive project documentation by Alejandro.

---

## 6. Deployment
The project is containerized using Docker for easy deployment. GitHub Actions ensure continuous integration and deployment with minimal manual intervention.

---

## 7. Future Improvements
1. Add multilingual support for a global user base.
2. Include a mobile version for better accessibility.
3. Implement AI-based predictions for item expiration trends.
