import requests 
from bs4 import BeautifulSoup as soup
from discord_webhook import DiscordWebhook, DiscordEmbed
from time import sleep
import datetime


webhook = DiscordWebhook(url='')

def find_listings():
    print("Initialized.")
    r = requests.get("https://www.govdeals.com/chpvehiclesales")
    #print(r.text)
    bs = soup(r.text, "html.parser")
    try:
        div = bs.find("p", {"align": "center"})
        if div.text == "No items currently listed for sale.":
            embed = DiscordEmbed(title="No items currently listed for sale.", description=f'retrying at {datetime.datetime.now() + datetime.timedelta(hours=1)}', color='03b2f8')
            # set author
            embed.set_author(name='Ask', url='https://github.com/Askioe', icon_url='https://user-images.githubusercontent.com/58087709/102176189-c4cf6300-3e55-11eb-9331-1c0895b9a736.jpg')

            embed.set_image(url="https://user-images.githubusercontent.com/58087709/102176189-c4cf6300-3e55-11eb-9331-1c0895b9a736.jpg")
            # set footer
            embed.set_footer(text='Fuck you Glenn')
            # set timestamp (default is now)
            embed.set_timestamp()
            webhook.add_embed(embed)
            response = webhook.execute()
            return 0
    except:
        print("Found listings!")
        name_array = bs.find_all("div", {"id": lambda x: x and x.__contains__('boxx_row')})
        for i in name_array:
            title = i.find('a', {"class": "highslide"})['title']
            image = i.find('a', {"class": "highslide"})['href']
            url = i.find('a', {"href": lambda x: x and x.__contains__('index.cfm')})['href']
            if "Dodge Charger" in i.text:
                embed = DiscordEmbed(title=title, color='03b2f8')
                # set author
                embed.set_author(name='Ask', url='https://github.com/Askioe', icon_url='https://user-images.githubusercontent.com/58087709/102176189-c4cf6300-3e55-11eb-9331-1c0895b9a736.jpg')

                embed.set_image(url="https://govdeals.com"+image)

                # set thumbnail
                embed.set_thumbnail(url="https://govdeals.com"+image)

                # set footer
                embed.set_footer(text='Fuck you Glenn')

                # set timestamp (default is now)
                embed.set_timestamp()

                # add fields to embed
                embed.add_embed_field(name='Year: ', value=title[0:4])
                embed.add_embed_field(name='Quick Link: ', value="https://govdeals.com/"+url)
                # add embed object to webhook
                webhook.add_embed(embed)

                response = webhook.execute()
                sleep(.5)
        return 0


def main():
    while True:
        find_listings()
        sleep(60 * 60)


if __name__ == "__main__":
    main()
