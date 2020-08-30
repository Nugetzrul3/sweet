# Transactions:
VERSION_1 = 0x01.to_bytes(4, byteorder='little')
VERSION_2 = 0x02.to_bytes(4, byteorder='little')
TIMESTAMP = 0x01.to_bytes(4, byteorder='little')
MARKER = b'\x00'
FLAG = b'\x01'
SEQUENCE = 0xFFFFFFFF .to_bytes(4, byteorder='little')
LOCK_TIME = 0x00 .to_bytes(4, byteorder='little')
HASH_TYPE = 0x01 .to_bytes(4, byteorder='little')

# Scripts:
OP_0 = b'\x00'
OP_CHECKLOCKTIMEVERIFY = b'\xb1'
OP_CHECKSIG = b'\xac'
OP_CHECKMULTISIG = b'\xae'
OP_DUP = b'v'
OP_EQUALVERIFY = b'\x88'
OP_HASH160 = b'\xa9'
OP_PUSH_20 = b'\x14'
OP_PUSH_32 = b'\x20'
OP_RETURN = b'\x6a'
OP_EQUAL = b'\x87'

MESSAGE_LIMIT = 80

# Address formats:
BECH32_VERSION_SET = ('sugar', 'tugar', 'rugar')
BECH32_MAIN_VERSION_SET = BECH32_VERSION_SET[:1]
BECH32_TEST_VERSION_SET = BECH32_VERSION_SET[1:]
MAIN_PUBKEY_HASH = b'\x3f'
MAIN_SCRIPT_HASH = b'\x7d'
TEST_PUBKEY_HASH = b'\x42'
TEST_SCRIPT_HASH = b'\x80'

# Keys:
MAIN_PRIVATE_KEY = b'\x80'
MAIN_BIP32_PUBKEY = b'\x04\x88\xb2\x1e'
MAIN_BIP32_PRIVKEY = '\x04\x88\xad\xe4'
TEST_PRIVATE_KEY = b'\xEF'
TEST_BIP32_PUBKEY = b'\x04\x88\xb2\x1e'
TEST_BIP32_PRIVKEY = b'\x04\x88\xad\xe4'
PUBLIC_KEY_UNCOMPRESSED = b'\x04'
PUBLIC_KEY_COMPRESSED_EVEN_Y = b'\x02'
PUBLIC_KEY_COMPRESSED_ODD_Y = b'\x03'
PRIVATE_KEY_COMPRESSED_PUBKEY = b'\x01'

# Units:
# https://en.bitcoin.it/wiki/Units
SATOSHI = 1
uSUGAR = 10 ** 2
mSUGAR = 10 ** 5
SUGAR = 10 ** 8
