# [역할] Random Forest 학습에 사용하는 하이퍼파라미터 및 검증 설정 상수 정의

RANDOM_SEED      = 42    # 재현 가능성 확보를 위한 고정 시드
N_ESTIMATORS     = 100   # RF 트리 개수 (tuner.py로 최적화 후 갱신)
MAX_DEPTH        = 10    # 트리 최대 깊이
CV_FOLDS         = 5     # K-Fold Cross Validation k값
TEST_SIZE        = 0.2   # 학습/테스트 분할 비율
CLASS_LABELS     = ['정상', '거리문제', '간섭', '음영', '다중경로']
