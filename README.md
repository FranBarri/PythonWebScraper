# PythonWebScraper
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
  </head>
  <body>
    <h1>LinkedIn Job Scraper</h1>
    <p>This script enables users to automate the process of scraping job listings from LinkedIn by running a bot. The bot opens a new Chrome tab, logs in to LinkedIn using the user's credentials (which are stored in a .txt file), and navigates to the "Jobs" section using filters specified by the user in the code.</p>
    <p>The bot then reads through each job application on the page, extracting relevant information such as the job title, company name, location, posting date, and work time. This information is saved in a CSV file that can be easily accessed by the user.</p>
    <h2>Requirements</h2>
    <p>Before using this script, please make sure you have the following:</p>
    <ul>
      <li>Python 3.x installed</li>
      <li>The following Python packages installed:
        <ul>
          <li>selenium</li>
          <li>pandas</li>
        </ul>
      </li>
      <li>Google Chrome browser installed</li>
    </ul>
    <h2>Usage</h2>
    <p>To use this script, follow these steps:</p>
    <ol>
      <li>Clone this repository to your local machine.</li>
      <li>Modify the link the line 49 with your LinkedIn login credentials.</li>
      <li>Modify the <code>job_filter</code> variable in the <code>JobScraper.py</code> file with your desired job filters.</li>
      <li>Run the script using the command <code>python JobScraper.py</code>.</li>
    </ol>
    <p>After running the script, the job listings data will be saved in a file called <code>job_listings.csv</code>.</p>
    <h2>Contributions</h2>
    <p>Feel free to contribute to this project by submitting pull requests or creating issues in the repository. We welcome any feedback or suggestions for improving the script.</p>
  </body>
</html>
