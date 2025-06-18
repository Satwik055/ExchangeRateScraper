import sys
import time
import schedule
from scraper_module import *
from currency import *
from supabase_module import *
from utils import *
from logtail import LogtailHandler
import requests

handler = LogtailHandler(source_token="6SVzxgfxk53h1bNkj1gHkgps", host="s1349851.eu-nbg-2.betterstackdata.com")
logger.remove(0)
logger.add(sys.stderr, format="{time} | {level} | {message}")
logger.add(handler, format="{message}", level="INFO", backtrace=False, diagnose=False)

SUPABASE_URL = 'https://fqsnwalptczelvhiwohd.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZxc253YWxwdGN6ZWx2aGl3b2hkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mzg2NzI4MTYsImV4cCI6MjA1NDI0ODgxNn0.TzD0KcPnEJz0DvLYxUmK68PeDuNy47sU0jRlyhAls-I'
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def fetch_and_update_rates():
    try:
        usd_rate = add_commission(1, scrape_exchange_rate(Currency.USD))
        aud_rate = add_commission(0.5, scrape_exchange_rate(Currency.AUD))
        cad_rate = add_commission(0.5, scrape_exchange_rate(Currency.CAD))
        gbp_rate = add_commission(1, scrape_exchange_rate(Currency.GBP))
        eur_rate = add_commission(1, scrape_exchange_rate(Currency.EUR))

        update_tti_rates(supabase, str(usd_rate), str(eur_rate), str(cad_rate), str(aud_rate), str(gbp_rate))
    except Exception as e:
        logger.error(f"Failed to update rates: {str(e)}")


schedule.every(30).minutes.do(fetch_and_update_rates)



def sendHeartbeat():
    heartbeat_url = "https://uptime.betterstack.com/api/v1/heartbeat/NQigbZ58SrhVcn5x4RZQ5t6u"
    requests.get(heartbeat_url)


if __name__ == "__main__":
    while True:
        sendHeartbeat()
        print("Heartbeat")
        schedule.run_pending()
        time.sleep(30)
