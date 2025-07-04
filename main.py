from fastapi import FastAPI
from ft_scraper import scrape_ft_pea
from datetime import datetime
import pytz

app = FastAPI()


@app.get("/ft/latest")
def get_latest_ft():
    ft_value = scrape_ft_pea()
    if not ft_value:
        return {"error": "FT value not found"}
    return {
        "ft_value": ft_value,
        "scraped_at": datetime.now(pytz.timezone("Asia/Bangkok")).strftime("%Y-%m-%d %H:%M:%S"),
    }
