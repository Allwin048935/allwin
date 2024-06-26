
# config.py

BINANCE_API_KEY = 'veiqd07BuRmMlxy3eeRLLKNyDnFrIphTcqgSM7XTRUCzQWTyqxK4sPtfVZioaVHi'
BINANCE_API_SECRET = 'N4myBDNkkD203gxxpo8NLQgdZxdvzm7N7PpBjBU0DiTtctTLaFQEVev51N4P5R5g'

# Telegram API keys
#TELEGRAM_BOT_TOKEN = ''
#TELEGRAM_CHAT_ID = ''


# List of futures trading pairs (symbols)
symbols = [
    '1INCHUSDT', '1000SATSUSDT', '1000BONKUSDT', '1000FLOKIUSDT', '1000XECUSDT', '1000LUNCUSDT', '1000PEPEUSDT', '1000SHIBUSDT', 'AAVEUSDT', 'ACEUSDT', 'ACHUSDT', 'ADAUSDT', 'AEVOUSDT', 'AGIXUSDT', 'AGLDUSDT', 'AIUSDT', 'ALGOUSDT', 'ALICEUSDT', 'ALPHAUSDT', 'ALTUSDT', 'AMBUSDT', 'ANKRUSDT', 'APEUSDT', 'API3USDT', 'APTUSDT', 'ARBUSDT', 'ARKUSDT', 'ARKMUSDT', 'ARPAUSDT', 'ARUSDT', 'ASTRUSDT', 'ATAUSDT', 'ATOMUSDT', 'AUDIOUSDT', 'AUCTIONUSDT', 'AXLUSDT',
    'AVAXUSDT', 'AXSUSDT', 'BADGERUSDT', 'BALUSDT', 'BANDUSDT', 'BAKEUSDT', 'BATUSDT', 'BEAMXUSDT', 'BELUSDT', 'BCHUSDT', 'BICOUSDT', 'BIGTIMEUSDT',
    'BLURUSDT', 'BLZUSDT', 'BNBUSDT', 'BNTUSDT', 'BOMEUSDT', 'BONDUSDT', 'BSVUSDT', 'BTCUSDT', 'C98USDT', 'CAKEUSDT', 'CELOUSDT', 'CELRUSDT', 'CFXUSDT', 'CHRUSDT', 'CKBUSDT', 'CHZUSDT',
    'COMBOUSDT','COMPUSDT', 'COTIUSDT', 'CRVUSDT', 'CTSIUSDT', 'CVXUSDT', 'CYBERUSDT', 'DARUSDT', 'DASHUSDT', 'DEFIUSDT', 'DENTUSDT', 'DODOXUSDT',
    'DOGEUSDT', 'DOTUSDT', 'DUSKUSDT', 'DYDXUSDT', 'DYMUSDT', 'EDUUSDT', 'EGLDUSDT', 'ENJUSDT', 'ENSUSDT', 'EOSUSDT', 'ETCUSDT', 'ETHUSDT', 'ETHFIUSDT', 'ETHWUSDT', 'FETUSDT',
    'FILUSDT', 'FLMUSDT', 'FLOWUSDT', 'FRONTUSDT', 'FTMUSDT', 'FXSUSDT', 'GALAUSDT', 'GALUSDT', 'GASUSDT', 'GLMRUSDT', 'GLMUSDT', 'GMTUSDT', 'GMXUSDT', 'GTCUSDT', 'GRTUSDT', 'HBARUSDT', 'HIGHUSDT',
    'HFTUSDT', 'HIFIUSDT', 'HOOKUSDT', 'HOTUSDT', 'ICPUSDT', 'ICXUSDT', 'IDEXUSDT', 'IDUSDT', 'ILVUSDT', 'IMXUSDT', 'INJUSDT', 'IOTXUSDT', 'IOSTUSDT', 'IOTAUSDT', 'JASMYUSDT', 'JOEUSDT', 'JTOUSDT', 'JUPUSDT', 'KASUSDT', 'KAVAUSDT', 'KEYUSDT', 'KNCUSDT',
    'KLAYUSDT', 'KNCUSDT', 'KSMUSDT', 'LDOUSDT', 'LEVERUSDT', 'LINKUSDT', 'LINAUSDT', 'LITUSDT', 'LOOMUSDT', 'LPTUSDT', 'LQTYUSDT', 'LRCUSDT', 'LSKUSDT', 'LTCUSDT', 'LUNA2USDT', 'MAGICUSDT', 'MANTAUSDT',
    'MANAUSDT', 'MASKUSDT', 'MATICUSDT', 'MAVIAUSDT', 'MAVUSDT', 'MBLUSDT', 'MDTUSDT', 'MEMEUSDT', 'METISUSDT', 'MINAUSDT', 'MKRUSDT', 'MOVRUSDT', 'MTLUSDT', 'MYROUSDT', 'NEARUSDT', 'NEOUSDT', 'NFPUSDT',
    'NKNUSDT', 'NMRUSDT', 'NTRNUSDT', 'OCEANUSDT', 'OGNUSDT', 'OMGUSDT', 'OMUSDT', 'ONDOUSDT', 'ONEUSDT', 'ONTUSDT', 'OPUSDT', 'ORBSUSDT',
    'ORDIUSDT', 'OXTUSDT', 'PENDLEUSDT', 'PEOPLEUSDT', 'PERPUSDT', 'PHBUSDT', 'PIXELUSDT', 'POLYXUSDT', 'PORTALUSDT', 'POWRUSDT', 'PYTHUSDT', 'QNTUSDT', 'QTUMUSDT', 'RADUSDT', 'RDNTUSDT', 'REEFUSDT', 'RENUSDT',
    'RIFUSDT', 'RLCUSDT', 'RNDRUSDT', 'RONINUSDT', 'ROSEUSDT', 'RSRUSDT', 'RVNUSDT', 'RUNEUSDT', 'SANDUSDT', 'SEIUSDT', 'SFPUSDT', 'SKLUSDT',
    'SLPUSDT', 'SNTUSDT', 'SNXUSDT', 'SOLUSDT', 'SPELLUSDT', 'SSVUSDT', 'STEEMUSDT', 'STGUSDT', 'STMXUSDT', 'STORJUSDT', 'STPTUSDT', 'STRKUSDT', 'STXUSDT',
    'SUIUSDT', 'SUPERUSDT', 'SUSHIUSDT', 'SXPUSDT', 'THETAUSDT', 'TIAUSDT', 'TLMUSDT', 'TOKENUSDT', 'TONUSDT', 'TRBUSDT', 'TRUUSDT', 'TRXUSDT', 'TUSDT', 'TWTUSDT', 'UMAUSDT', 'UNFIUSDT', 'UNIUSDT',
    'VANRYUSDT', 'VETUSDT', 'WAVESUSDT', 'WAXPUSDT', 'WIFUSDT', 'WLDUSDT', 'WOOUSDT',
    'XAIUSDT', 'XEMUSDT', 'XLMUSDT', 'XMRUSDT', 'XRPUSDT', 'XTZUSDT', 'XVGUSDT', 'XVSUSDT', 'YFIUSDT', 'YGGUSDT', 'ZECUSDT',
    'ZENUSDT', 'ZETAUSDT', 'ZILUSDT', 'ZRXUSDT'
]

# Time interval for fetching historical data
time_interval = '4h'  # You can change this to '4h', '1d', etc.
