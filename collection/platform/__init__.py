# [역할] 실행 OS를 자동 감지하여 RSSI 읽기 함수를 플랫폼별로 분기
import platform
if platform.system() == 'Windows':
    from .windows import get_rssi
else:
    from .linux import get_rssi
