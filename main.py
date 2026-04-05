# [역할] --mode 인자로 collect / preprocess / train / evaluate / gui / replay 파이프라인을 단계별로 실행하는 진입점

import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', choices=['collect','preprocess','train','evaluate','gui','replay'], required=True)
    args = parser.parse_args()

if __name__ == '__main__':
    main()
