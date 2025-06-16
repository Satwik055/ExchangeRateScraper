from supabase import *
from loguru import logger


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
                logger.info(f"Successfully updated {row_id} with new price {new_price}")
            else:
                logger.error(f"No rows were updated for row {row_id}. Check if the row exists.")

        except Exception as e:
            logger.error(f"Error updating row {row_id}: {str(e)}")
