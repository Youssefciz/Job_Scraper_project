
Job Scraper Project
===================

Description
-----------
The **Job Scraper** is a Python-based web application designed to scrape job listings from LinkedIn to provide users with relevant job opportunities. It uses BeautifulSoup and Requests to parse HTML and extract job data efficiently. The project features a responsive web interface built with Bootstrap, providing a clean and user-friendly way to display job listings.

Features
--------
- **Web Scraping:** Implemented web scraping techniques using BeautifulSoup and Requests to collect job data from LinkedIn.
- **Responsive Web Design:** Created a responsive web interface using Bootstrap for optimal user experience across devices.
- **JSON API Endpoint:** Developed a JSON API endpoint to serve job listing data in a structured format.
- **Error Handling:** Managed HTTP response status codes and log errors effectively to ensure smooth operation.
- **RESTful API Development:** Gained experience in RESTful API development and client-side JavaScript for AJAX requests.

Installation
------------
1. **Clone the Repository**
   ```bash
   git clone https://github.com/Youssefciz/Job_Scraper_project.git
   ```

2. **Navigate to the Directory**
   ```bash
   cd Job_Scraper_project
   ```

3. **Set Up a Virtual Environment (Optional but Recommended)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. **Install Dependencies**
   Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

Usage
-----
1. **Run the Application**
   To start the web application:
   ```bash
   python app.py
   ```

2. **Access the Web Interface**
   Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```
   Here you can input a job search query, and the application will display relevant job listings scraped from LinkedIn.

3. **Customizing the Scraper**
   - Modify `app.py` to change the scraping logic, such as targeting different websites or filtering specific job types.
   - Update `index.html` to customize the web interface layout or design.

Example
-------
- Start the server:
   ```bash
   python app.py
   ```

- Navigate to the web interface, enter your job search criteria, and view the results.