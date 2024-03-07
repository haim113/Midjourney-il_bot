import requests
from bs4 import BeautifulSoup
import telegram
from telegram import Bot, InputMediaPhoto

BOT_TOKEN = "YOUR_BOT_TOKEN"
CHANNEL_ID = "YOUR_CHANNEL_ID"

bot = Bot(token=BOT_TOKEN)

def scrape_and_send():
    url = "https://midjourney.com/showcase"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    image_elements = soup.find_all("img", class_="rounded-lg")
    prompt_elements = soup.find_all("p", class_="mb-4")

    for image, prompt in zip(image_elements, prompt_elements):
        image_url = image["src"]
        prompt_text = prompt.text.strip()

        try:
            image_data = requests.get(image_url).content
            bot.send_photo(chat_id=CHANNEL_ID, photo=image_data, caption=prompt_text)
            print(f"Sent image with prompt: {prompt_text}")
        except Exception as e:
            print(f"Error sending image: {e}")

scrape_and_send()
