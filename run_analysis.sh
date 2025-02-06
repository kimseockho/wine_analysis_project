#!/bin/bash

# 실행 시작 시간 기록
echo "===== Wine 데이터셋 분석 실행 시작: $(date) =====" > log.txt

# Python 스크립트 실행 (표준 출력 및 오류 로그 저장)
python3 analyze.py >> log.txt 2>&1

# 실행 완료 메시지 기록
echo "===== 분석 완료: $(date) =====" >> log.txt

# 결과 확인 메시지 출력
echo "분석이 완료되었습니다. 로그는 'log.txt' 파일에서 확인하세요."
