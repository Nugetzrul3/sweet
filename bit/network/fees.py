COST_PER_KBYTE = 0.01
minimum_fee = 0.0001


def set_fee_cache_time(seconds):
    pass

def get_fee(tx_size_bytes: int):

    fee = (tx_size_bytes / 1000) * COST_PER_KBYTE

    if fee <= minimum_fee:
        return minimum_fee
    else:
        return round(fee, 5)


def get_fee_cached(tx_size):
    return get_fee(tx_size)
