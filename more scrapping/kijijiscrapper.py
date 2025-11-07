import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import re

# Function to fetch Kijiji car listings for a given search query
def fetch_car_listings(search_query):
    url = f"https://www.kijiji.ca/b-cars-vehicles/canada/{search_query}/k0c27l0"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print("Failed to fetch data.")
        return []
    
    pattern=re.compile(r"^listing-card.*")
    soup = BeautifulSoup(response.text, 'html.parser')
    listings = soup.find_all("li", attrs={"data-testid" :pattern})
    
    cars = []
    for listing in listings:
        linkinfo = listing.find("a", attrs={"data-testid" :"listing-link"})
        title = linkinfo.text.strip()
        link= linkinfo.get('href')
        price_tag = listing.find("p", attrs={"data-testid" :"autos-listing-price"})
        if price_tag:
            price = price_tag.text.strip().replace("$", "").replace(",", "")
            try:
                price = int(price)
                cars.append({"title": title, "price": price , "link":link})
            except ValueError:
                pass  # Skip non-numeric prices
    
    return cars

# Function to plot the price distribution
def plot_price_distribution(cars):
    prices = [car['price'] for car in cars]
    
    if not prices:
        print("No prices to plot.")
        return
    plt.figure()
    plt.hist(prices, bins=20, edgecolor='black')
    plt.title("Price Distribution of Cars")
    plt.xlabel("Price ($)")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()

# Main script
if __name__ == "__main__":
    search_query = input("Enter car model (e.g., toyota-corolla): ").replace(" ", "-")
    cars = fetch_car_listings(search_query)
    
    if cars:
        print(f"Found {len(cars)} listings:")
        for car in cars:
            print(f"Title: {car['title']}, Price: ${car['price']}")
        plot_price_distribution(cars)
    else:
        print("No listings found.")
