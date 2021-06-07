import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get('TEST_TOKEN')

AWS_ACCESS_KEY_ID = os.environ.get('POLLY_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('POLLY_SECRET_ACCESS_KEY')
AWS_REGION_NAME = 'eu-central-1'

"""Keywords"""
TTS_SAY = '!tts say'
TTS_LEAVE = '!tts leave'
TTS_SAY_VOICE = '!tts say-'
TTS_VOICES = '!tts voices'

DEFAULT_VOICE = 'Hans'
CHARACTER_LIMIT = 2000

VOICES = {
    'en1': 'Ivy',
    'en2': 'Joanna',
    'en3': 'Matthew',
    'en4': 'Joey',

    'ger1': 'Marlene',
    'ger2': 'Vicki',
    'ger3': 'Hans',

    'fr1': 'Celine',
    'fr2': 'Mathieu',

    'it1': 'Bianca',
    'it2': 'Giorgio',

    'du1': 'Lotte',
    'du2': 'Ruben',

    'kr1': 'Seoyeon',
    'jp1': 'Mizuki',
    'jp2': 'Takumi',

    'sp1': 'Lucia',
    'sp2': 'Conchita',
    'sp3': 'Enrique',

    'ru1': 'Tatyana',
    'ru2': 'Maxim',

    'sw1': 'Astrid',
    'tu1': 'Filiz',
    'ar1': 'Zeina',
    'ic1': 'Karl'
}
