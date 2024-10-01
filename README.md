# Facebook ROI Calculator

This is a web application designed for calculating the Expected Return on Investment (ROI) for Facebook advertising campaigns based on key metrics like monthly ad spend, cost per click (CPC), opt-in rate, lead conversion rate, and average sale price. The application also supports switching between two currencies—USD and INR.

**Check out the web app online at:** [ROI Calculator](https://roi-calculator-ecru.vercel.app/)

## Features

- **Input Metrics**: Adjust sliders and input fields for:
  - Monthly Ad Spend
  - Cost Per Click (CPC)
  - Opt-In Conversion Rate
  - Lead to Customer Conversion Rate
  - Average Sale Price

- **Currency Switching**: The application allows you to switch between USD and INR, with values being updated accordingly.

- **Real-Time Calculation**: ROI, Gross Revenue, and Net Profit/Loss are calculated in real-time as input metrics change.

- **User-Friendly Interface**: The app features an interactive UI for easy visualization of results.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python with Flask
- **Hosting**: Vercel for deployment

## Installation

### Prerequisites

- Python 3.x installed.
- Flask installed. You can install Flask using:

  ```bash
  pip install Flask
  ```
# Steps to Run
**1.Clone the Repository:**

  ```bash

git clone https://github.com/your-repository-url
  ```

**2.Navigate to the Project Directory:**
```bash
cd facebook_roi_calculator
```

**3.Install the Required Packages:**
```bash
pip install -r requirements.txt
```

**4.Run the Flask App:**
```bash
flask run
```

**5.Access the Application:**

Once the server is running, go to your browser and open http://127.0.0.1:5000/ to use the ROI Calculator.


**Project Structure**
```bash
roi-calculator/
│
├── static/
│   ├── styles.css       # CSS file for styling the web app
│   └── logo.svg         # Logo used in the UI
│
├── templates/
│   └── index.html       # HTML file for the ROI Calculator UI
|
├── app.py                # Main Python file to start the Flask server
├── index.py              # Entry point of the web application
├── requirements.txt      # Python dependencies for the project
├── vercel.json           # Configuration file for Vercel deployment
└── wsgi.py               # Entry point for the WSGI server for deployment
```

**Contact**<br>
Email: akashn1412@gmail.com<br>
LinkedIn: https://www.linkedin.com/in/akash-nishad-792579221/<br>
GitHub: https://github.com/akashn-1412<br>
 
