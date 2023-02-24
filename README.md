# GovDeals_Auction_Checker
 Scrapes govdeals.com monitoring for specific keywords and new listings

# Dependencies 
* Requests
* BeautifulSoup4
* discord_webhook 

# Motivation 
Created this due to looking for a specific vehicle from a government agency and decided it would be simpler to automate it rather than manually checking it frequently

# How it works
Sends a request to the webpage looking for an html response, uses BeautifulSoup4 to locate divs that indicate new listings, and string matching to determine if it matches the keyword of what I am looking for.
