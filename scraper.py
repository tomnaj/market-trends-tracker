import requests
from bs4 import BeautifulSoup
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def scrape_product_data():
    url = "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/"
    try:
        page = requests.get(url)
        page.raise_for_status()  # Raise an error for bad responses
        soup = BeautifulSoup(page.content, "html.parser")
        products = []

        for product in soup.select("div.thumbnail"):
            name = product.select("h4 > a")[0].get_text(strip=True) if product.select("h4 > a") else "No name"
            price = product.select("h4.price")[0].get_text(strip=True).replace("$", "") if product.select("h4.price") else "0"
            availability = product.select("span.availability")[0].get_text(strip=True) if product.select("span.availability") else "Not available"
            rating = float(product.select("span.rating")[0].get_text(strip=True)) if product.select("span.rating") else 0.0
            product_url = product.select("a")[0].get("href") if product.select("a") else "No URL"

            products.append({
                "name": name,
                "price": float(price) if price else 0.0,
                "availability": availability,
                "rating": rating,
                "url": product_url
            })

        logging.info(f"Scraped {len(products)} products.")
        return products

    except requests.RequestException as e:
        logging.error(f"Error fetching the page: {e}")
        return []
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return []

if __name__ == "__main__":
    scraped_products = scrape_product_data()  # Run the scraper directly for testing
    print(scraped_products)  # Print the scraped products for verification
