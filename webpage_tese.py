from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pdfkit
import time

def main():
    url = 'https://www.bluebash.co/'  # The URL of the web page to convert
    output_pdf = 'output.pdf'  # The name of the output PDF file

    # Set up headless Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Create a new instance of the Chrome driver
    service = Service('/usr/local/bin/chromedriver')  # Ensure this path is correct
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        url = "https://example.com"
        output_file = "output.pdf"

        # Open webpage and print to PDF
        driver.get(url)
        driver.execute_cdp_cmd("Page.printToPDF", {"path": output_file})
        driver.quit()

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()