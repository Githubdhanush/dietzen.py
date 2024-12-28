# Diet Zen

**Diet Zen** is a Python-based GUI application designed to help users manage their dietary goals and calculate their nutritional needs. Built using the `tkinter` library, it integrates with a MySQL database for user authentication and data storage.

## Features

- **User Authentication**
  - **Sign Up:** New users can register by providing personal details, weight, height, and dietary preferences.
  - **Login:** Existing users can securely log in.

- **BMI Calculation**
  - Computes the user's Body Mass Index (BMI) based on their height and weight.
  - Displays BMI results to help users track their health.

- **Dietary Goal Management**
  - Users can choose from three dietary goals:
    - Lose fat.
    - Maintain weight.
    - Build muscle.
  - Provides customized daily calorie, protein, and fat targets.

## Technologies Used

- **Python**: Core programming language for application development.
- **Tkinter**: For building the graphical user interface (GUI).
- **MySQL**: For persistent data storage, including user details and login information.

## Installation

### Prerequisites

1. **Python 3.7+**: Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. **MySQL**: Install MySQL server and set it up.
3. **Python Libraries**: Install the required libraries using the following command:

   ```bash
   pip install mysql-connector-python
   ```

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/diet-zen.git
   cd diet-zen
   ```

2. **Configure Database**
   - Update the MySQL credentials in the script:

     ```python
     db = mysql.connector.connect(
         host="localhost",
         user="your_mysql_username",
         password="your_mysql_password"
     )
     ```

   - The application will automatically create the required databases and tables on first run if they do not exist.

3. **Run the Application**

   ```bash
   python diet_zen.py
   ```

## Usage

1. **Sign Up**: Create a new account by filling out the sign-up form.
2. **Login**: Enter your username and password to log in.
3. **Calculate BMI**: Use the BMI calculator to check your health status.
4. **Set Goals**: Select a dietary goal to get personalized recommendations for calories, protein, and fats.

## Database Structure

1. **`CUSTOMER_LOGIN_DETAILS` Table**
   - Stores login credentials (username and password).

   | Column    | Type         |
   |-----------|--------------|
   | Username  | VARCHAR(255) |
   | Password  | VARCHAR(255) |

2. **`CUSTOMER_DETAILS` Table**
   - Stores user personal data (name, gender, age, weight, height, etc.).

   | Column    | Type         |
   |-----------|--------------|
   | Name      | VARCHAR(255) |
   | Gender    | VARCHAR(10)  |
   | Age       | INT          |
   | Weight    | FLOAT        |
   | Height    | FLOAT        |
   | Email     | VARCHAR(255) |
   | Mobile    | VARCHAR(15)  |

## Future Improvements

- **Password Security**
  - Use hashing (e.g., bcrypt) to store passwords securely.
- **Responsive UI**
  - Make the application interface adaptable to various screen sizes.
- **Error Handling**
  - Add better input validation and error messages.
- **Additional Goals**
  - Introduce more personalized dietary plans based on activity level and medical conditions.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature.
3. Commit your changes and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For questions or support, reach out to:
- **Name:** DHANUSH AMSANATHAN
- **Email:** dhanushamsanathan@gamil.com
- **GitHub:** https://github.com/Githubdhanush

