# Walmart Deals Scraper

## Project Overview

This project is designed to scrape the deals section of Walmart's website. It aims to efficiently gather data on products, including images, prices, titles, and customer reviews. The script utilizes Selenium for web browsing and BeautifulSoup for parsing the HTML content.

## Features

- **Headless Browsing**: Leveraging Chrome's headless mode for efficient scraping without GUI.
- **Dynamic Content Loading**: Waits for the dynamic content of the webpage to load.
- **Image URL Extraction**: Retrieves URLs of product images.
- **Price Extraction**: Captures the pricing information of each product.
- **Product Title and Review Extraction**: Gathers product titles and customer review data.
- **Proxy Support**: Provision for using a proxy for web scraping.

## Prerequisites

- Python 3.x
- Selenium
- BeautifulSoup4
- ChromeDriver
- Google Chrome Browser

## Installation

1. **Python Packages**: Install the required Python packages.
   ```
   pip install selenium beautifulsoup4
   ```
2. **ChromeDriver**: Download and set up ChromeDriver corresponding to your Chrome version from [ChromeDriver - WebDriver for Chrome](https://sites.google.com/chromium.org/driver/). Ensure it's in your PATH or specify the path in the script.

## Usage

1. **Run the Script**: Execute the script in a Python environment.
2. **Headless Mode**: Uncomment the `--headless` option in the script for headless execution.
3. **Proxy Configuration**: If needed, configure the proxy settings by uncommenting and setting the `proxy` variable.

## Script Workflow

1. **Initializing WebDriver**: Sets up Chrome with optional headless mode and proxy settings.
2. **Page Navigation**: Opens the Walmart deals URL.
3. **Content Loading**: Waits for the product list to load on the webpage.
4. **Data Extraction**: Parses the loaded page, extracting images, prices, titles, and reviews.
5. **Data Output**: Prints the extracted information on the console.
6. **Cleanup**: Closes the browser after scraping.

## Limitations & Considerations

- **Website Structure Changes**: The script might require updates if Walmart's website structure changes.
- **Legal and Ethical Considerations**: Ensure compliance with Walmart's terms of service regarding web scraping.
- **Rate Limiting**: Implement delays or checks to avoid being rate-limited or banned by the website.

## Conclusion

This Walmart Deals Scraper is a practical tool for extracting valuable product information. It showcases the integration of Selenium and BeautifulSoup in a Python environment for effective web scraping tasks.