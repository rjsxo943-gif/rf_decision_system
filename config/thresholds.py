# [역할] RSSI / Packet Loss / Latency / Jitter 판단 기준값 (threshold) 전역 상수 정의

RSSI_GOOD   = -65   # dBm: 양호 기준
RSSI_BAD    = -75   # dBm: 불량 기준
RSSI_DEAD   = -85   # dBm: 음영 구역 기준
LOSS_BAD    = 5.0   # %: 패킷 손실률 불량 기준
LATENCY_BAD = 20    # ms: 지연 시간 불량 기준
JITTER_BAD  = 10    # ms: Jitter 불량 기준 (ITU-T G.114)
STD_HIGH    = 5.0   # dB: RSSI 표준편차 높음 기준
