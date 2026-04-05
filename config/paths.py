# [역할] 프로젝트 전체에서 사용하는 파일/폴더 경로를 한 곳에서 관리
import os

BASE_DIR         = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DATA_PATH    = os.path.join(BASE_DIR, 'data', 'raw')
PROCESSED_PATH   = os.path.join(BASE_DIR, 'data', 'processed')
AP_SCAN_PATH     = os.path.join(BASE_DIR, 'data', 'ap_scan')
MOCK_PATH        = os.path.join(BASE_DIR, 'data', 'mock')
BACKUP_PATH      = os.path.join(BASE_DIR, 'data', 'backup')
MAP_PATH         = os.path.join(BASE_DIR, 'data', 'map')
MODEL_PATH       = os.path.join(BASE_DIR, 'saved_model')
RESULTS_PATH     = os.path.join(BASE_DIR, 'results')
LOGS_PATH        = os.path.join(BASE_DIR, 'logs')
