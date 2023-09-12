## Installation
   - Clone this repository to your local machine.
   - Open a terminal and navigate to the project directory.
   - Install the required dependencies with the following command:
        ```
        pip install -r requirements.txt
        ```


## Usage
- Change the .env.example file to .env
- In the new .env file, make sure you have entered:
    - Valid login credentials for Hudl
    - Choice of browser for running tests
    - Whether to use a headless browser option
- Add valid login credentials to .env
- Select browser (chrome, firefox, edge or safari)
- To run all the tests, execute the following command:#
    ```
    pytest -m regression
    ```

## The Ask

Setup an automation environment on your local machine using Selenium
Automate any cases that you would think are good to test the functionality of validating logging into hudl.com ( http://hudl.com/ ).
Ignore social logins (Facebook, Google, Apple, etc.) and account creation. Automate only functionality around using credentials.
Push your tests to a GitHub repository (a public repo is fine) and share the link (please do not include any passwords in a public repo).We are expecting you to automate scenarios that you deem critical to validate the functionality of credentialed login to hudl.com ( http://hudl.com/ ).
This project is an opportunity to showcase your organization structure, approach to automation, and ability to effectively write new automated test cases.We will be looking for well-established best practices and patterns. Lastly, we will run your automation suite against the site, so please write it in a way that allows us to do so.
 
This isn't a timed test, however, we estimate this exercise to take you around 2-3 hours to complete. To allow us to continue to move through this process quickly, we ask that you return this project to us in 4 days. If you need more time for whatever reason, we ask that you please let us know, so we can properly set expectations with our project reviewers.
 
## Tips
 
If you're unfamiliar with Selenium the best place to start is with the below readings:
https://www.seleniumhq.org/projects/webdriver/
https://gist.github.com/huangzhichong/3284966
Once you have completed your project and pushed it to GitHub, please use the link at the bottom of this email to share the URL to the public repo.

# Notes

It has been a while since I used Selenium as I have been writing tests in Cypress for the past few years. Happy to discuss any design decisions that I made.
If I were to take some additional time, I would focus on improving my code comments and implement a better reporting solution.