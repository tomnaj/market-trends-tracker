import logging
from apscheduler.schedulers.blocking import BlockingScheduler
from market_trends_tracker.database import save_to_db
from scraper import scrape_product_data

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def start_scheduler():
    logging.info("Starting the scheduler...")
    scheduler = BlockingScheduler()

    # Schedule the job to run every 6 hours
    @scheduler.scheduled_job('interval', seconds=10)  # Adjusted for testing
    def scheduled_scraping():
        logging.info("Scheduled job triggered.")
        try:
            products = scrape_product_data()  # Scrape product data
            logging.info(f"Scraped products: {products}")  # Log the scraped products
            if products:
                save_to_db(products)  # Save scraped products to the database
                logging.info(f"Data scraped and saved successfully: {len(products)} products.")
            else:
                logging.warning("No products were scraped.")
        except Exception as e:
            logging.error(f"An error occurred during scraping: {e}")

    scheduler.start()

if __name__ == "__main__":
    start_scheduler()  # Start the scheduler when the script is run directly
