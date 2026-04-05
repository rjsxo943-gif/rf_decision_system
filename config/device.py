# [역할] ESP32 시리얼 포트 등 하드웨어 연결 설정을 .env에서 읽어 제공
import os
from dotenv import load_dotenv
load_dotenv()

SERIAL_PORT = os.getenv('SERIAL_PORT', 'COM3')  # .env에서 읽음
BAUD_RATE   = 115200
TIMEOUT     = 2
