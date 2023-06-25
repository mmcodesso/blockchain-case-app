# Blockchain Application for Audit Practice

This project is a simple web-based blockchain application created for teaching the principles of blockchain technology to accounting and auditing students.

## Overview

The application uses Python and Flask for the backend, and HTML/CSS/Javascript for the frontend. It demonstrates the core principles of blockchain, such as immutability and decentralized consensus, in the context of recording transactions of students enrolling in courses.

Students can interact with the application, add transactions to the blockchain, and simulate the audit process by verifying the integrity of the blockchain.

## Installation and Setup

Follow these steps to set up the project:

1. **Clone the Repository:**

   ```
   git clone https://github.com/mmcodesso/blockchain-case-app.git
   cd blockchain-case-app
   ```

2. **Setup Python Environment:**

   It's recommended to use a virtual environment to isolate the project dependencies. You can set it up using:

   ```
   python3 -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install Dependencies:**

   The project dependencies are listed in the `requirements.txt` file. You can install these using pip:

   ```
   pip install -r requirements.txt
   ```

4. **Start the Application:**

   You can start the application using the Flask command:

   ```
   export FLASK_APP=blockchain.py  # On Windows use `set FLASK_APP=blockchain.py`
   flask run
   ```

The application will start on `http://localhost:5000/`.

## Usage

To use the application, start by navigating to the `/assignment` route to view the assignment instructions. Then, follow the instructions to interact with the blockchain, add transactions, and audit the blockchain.

## Contributing

Contributions are welcome. Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
```
