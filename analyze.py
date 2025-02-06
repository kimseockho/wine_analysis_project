import numpy as np
import pandas as pd
from sklearn.datasets import load_wine

# 와인 데이터셋 로드
wine = load_wine()
df = pd.DataFrame(wine.data, columns=wine.feature_names)

# 분석 수행
num_rows, num_cols = df.shape
mean_values = df.mean()
std_values = df.std()
alcohol_max = df["alcohol"].max()
alcohol_min = df["alcohol"].min()

# 결과 저장
output_text = f"""
### Wine 데이터셋 분석 결과 ###

1. 데이터셋 크기:
   - 행(row) 개수: {num_rows}
   - 열(column) 개수: {num_cols}

2. 각 특성(컬럼)의 평균(mean)과 표준편차(std):
{pd.DataFrame({'Mean': mean_values, 'Std': std_values})}

3. 특정 특성 (`alcohol`) 값 범위:
   - 최대값: {alcohol_max}
   - 최소값: {alcohol_min}
"""

# 결과를 파일에 저장
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(output_text)

print("분석이 완료되었습니다. 결과는 'output.txt' 파일에서 확인하세요.")
