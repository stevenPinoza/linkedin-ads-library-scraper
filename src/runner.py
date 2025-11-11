thonimport json
import requests
from extractors.linkedin_parser import parse_linkedin_ads
from outputs.exporters import export_to_json, export_to_csv

def run_scraper(urls, max_results=100, output_format='json'):
    """
    Run the scraper to extract LinkedIn ads data from provided URLs.

    :param urls: List of LinkedIn Ad Library search URLs to scrape
    :param max_results: Maximum number of results to scrape per URL
    :param output_format: The output format (json or csv)
    """
    all_ads = []
    for url in urls:
        ads = parse_linkedin_ads(url, max_results)
        all_ads.extend(ads)

    if output_format == 'json':
        export_to_json(all_ads, 'output.json')
    elif output_format == 'csv':
        export_to_csv(all_ads, 'output.csv')

if __name__ == '__main__':
    urls = ["https://www.linkedin.com/ad-library/search?accountOwner=apple&countries=US"]
    run_scraper(urls)