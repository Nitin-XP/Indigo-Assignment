# Flight Status and Notifications System

This project aims to provide real-time flight status updates and notifications to passengers, enhancing their travel experience by keeping them informed about delays, cancellations, and gate changes.

## Features

- **Real-Time Updates:** Displays current flight status including delays, cancellations, and gate changes using provided mock data.
- **Push Notifications:** Sends notifications via SMS and email for any changes in flight status.
- **User-Friendly Interface:** An intuitive and responsive front-end built with React.js.
- **Data Handling:** Fetches and processes flight data from MongoDB.

## Technologies Used

- **Frontend:** React.js and other libraries.
- **Backend:** Python and Flask.
- **Database:** MongoDB for storing flight and notification data.
- **Notifications:** 
  - Email using smtplib.
  - SMS using Twilio.

## Installation
## Step 1: Clone the Repository
Open Windows Terminal and run the following command to clone the repository:
bash
git clone https://github.com/Nitin-XP/Indigo-Assignment.git

## Step 2: Navigate to the Project Directory
Change to the project directory:

bash
cd Indigo-Assignment

## Step 3: Set Up a Virtual Environment
Create and activate a virtual environment:

bash
python -m venv venv
.\venv\Scripts\activate

## Step 4: Install Backend Dependencies
Install the required Python packages:

bash
pip install -r requirements.txt

## Step 5: Install Frontend Dependencies
Navigate to the frontend directory and install the required npm packages:

bash
cd client
npm install

## Step 6: Start the Backend Server
Navigate back to the project root directory and start the Flask server:

bash
cd ..
cd server
.venv\Scripts\activate
python server.py

## Step 7: Start the Frontend Development Server
Navigate back to the frontend directory and start the React development server:

bash
cd client
npm run dev

Access the Application
Open your browser and go to http://localhost:3000 to access the frontend interface.
The backend server runs on http://localhost:5000.
Note
Ensure MongoDB is installed and running on your machine. Configure your database connection settings in the backend code as needed.


## Usage

- Open your browser and go to `http://localhost:3000` to access the frontend interface.
- The backend server runs on `http://localhost:5000`.

## Data Handling

- **Flight Data:** Managed using MongoDB, providing a flexible schema to store various flight details.
- **Notifications:** Implemented using smtplib for emails and Twilio for SMS.

## Contributing

Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## Contact

For any questions or suggestions, please contact nitinkumar150103@gmail.com.

---

This README provides a concise overview of the project, highlighting its features, technologies, and setup instructions.
