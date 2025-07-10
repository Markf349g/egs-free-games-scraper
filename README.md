# 🎮 Epic Games Free Games Scraper

Your ✨ **automated browser tool** to check out **free game giveaways** from the [Epic Games Store](https://store.epicgames.com), and return the results in clean, structured **JSON format**.

Perfect for integration into existing software, dashboards, bots, or notification systems!

---

## 🚀 Features

- 🕸️ **Browser automation** using Selenium
- 📦 Dependency management with `uv`
- 🔍 Scrapes current and upcoming **free game offers**
- 📄 Exports results in structured `JSON`
- ✅ **Unit tested** with `pytest`
- 🧩 Easy integration into any Python-based workflow

---

## 🕸️ Web Scraping of the Epic Games Store

This tool automatically scans the [Epic Games Store](https://store.epicgames.com) and parses the latest **free game giveaways**, including their names, dates, status, and images.
<p>
   <img src="egs-free-games-image.jpg" alt="Epic Games Store Free Games Image" width="400" />
</p>

## 🧪 Sample Output (JSON)

```json
{
  "Backpack Hero": {
    "Name": "Backpack Hero",
    "Image": "https://cdn1.epicgames.com/spt-assets/da842a6b6e324c39b54b16910856bdb3/backpack-hero-k5abu.png?resize=1&w=360&h=480&quality=medium",
    "Status": "FREE NOW",
    "Free Date": "Now - Jul 10 at 10:00 PM"
  },
  "Figment": {
    "Name": "Figment",
    "Image": "https://cdn1.epicgames.com/epic/offer/EGS_Figment_BedtimeDigitalGames_S2-860x1148-6470fca68f6a5b0a56a9033f83ab9afd.jpg?resize=1&w=360&h=480&quality=medium",
    "Status": "FREE NOW",
    "Free Date": "Now - Jul 10 at 10:00 PM"
  },
  "Figment 2: Creed Valley": {
    "Name": "Figment 2: Creed Valley",
    "Image": "https://cdn1.epicgames.com/salesEvent/salesEvent/EGS_Figment2CreedValley_BedtimeDigitalGames_S2_1200x1600-aee3edb65954908fbacadc5dbbfbed4e?resize=1&w=360&h=480&quality=medium",
    "Status": "COMING SOON",
    "Free Date": "Jul 10 - Jul 17"
  },
  "Sky Racket": {
    "Name": "Sky Racket",
    "Image": "https://cdn1.epicgames.com/spt/209cb869-46b1-4cee-a906-80c2970f5e5e/download-sky-racket-offer-fa9be0e.jpg?resize=1&w=360&h=480&quality=medium",
    "Status": "COMING SOON",
    "Free Date": "Jul 10 - Jul 17"
  }
}
```

---

## ⚙️ Technologies Used

| Tool         | Purpose                             |
|--------------|--------------------------------------|
| 🐍 `Python`   | Core language for scripting          |
| 🌐 `Selenium` | Browser automation & web scraping    |
| 📦 `uv`       | Fast, modern dependency management   |
| 🧪 `pytest`   | Unit testing and validation          |

---

## 📦 Installation

Make sure you have a working Python environment, a compatible browser driver (e.g., ChromeDriver), and that [`uv`](https://docs.astral.sh/uv) is installed for dependency management.

---

## ▶️ How to Run

```bash
uv run egs_free_games_scraper.py
```

Or use the module directly in your Python code:

```python
from egs_free_games_parser import EpicGamesStoreScraper

# A few lines example
web_driver: WebDriver = webdriver.Chrome()

egss_class: EpicGamesStoreScraper = EpicGamesStoreScraper(
	web_driver=web_driver,
	destructor=False
)
json_value: str = egss_class.get_free_games_json()
print(json_value)

web_driver.quit()

# A one line example
print(EpicGamesStoreScraper().get_free_games_json())
```

---

## 🧰 Integration

Want to integrate into a Discord bot, Telegram notifier, or dashboard?  
Simply consume the JSON output and render game titles, images, or timers based on availability.

---

## ✅ Testing

Run validation tests with:

```bash
pytest
```

Tests include checks for JSON format, content structure, and error handling.

---

## 📚 License

MIT — Free to use and modify.
