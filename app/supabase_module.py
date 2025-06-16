from supabase import *


# formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
#
# handler = logging.StreamHandler()
# handler.setLevel(logging.INFO)
# handler.setFormatter(formatter)
#
# logger = logging.getLogger("my_logger")
# logger.setLevel(logging.INFO)
# logger.addHandler(handler)
#

def update_tti_rates(
        supabase: Client,
        usd_rate: str,
        eur_rate: str,
        cad_rate: str,
        aud_rate: str,
        gbp_rate: str
):
    rates = {
        'EUR': eur_rate,
        'GBP': gbp_rate,
        'AUD': aud_rate,
        'CAD': cad_rate,
        'USD': usd_rate,
        'BANK': usd_rate
    }

    for row_id, new_price in rates.items():
        try:
            response = supabase.table('exchange_rate').update({'tti': new_price}).eq('currency_name', row_id).execute()
            if response.data:
                print(f"Successfully updated {row_id} with new price {new_price}")
                # logger.info(f"Successfully updated {row_id} with new price {new_price}")
            else:
                print(f"No rows were updated for row {row_id}. Check if the row exists.")
                # logger.error(f"No rows were updated for row {row_id}. Check if the row exists.")

        except Exception as e:
            print(f"Successfully updated {row_id} with new price {new_price}")
            # logger.error(f"Error updating row {row_id}: {str(e)}")
