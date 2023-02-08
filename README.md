# Forecasting-the-risk-of-forest-fires
## 산불 위험도 예측 프로젝트
[2023-1] Capstone Project @SJU

project term 2023.02.01~

## 기상인자와 **인간인자**를 반영한 산불 위험도 예측

- 전국 데이터를 바탕으로 학습을 진행한 뒤 행정구역별(읍면동)로 나누어 위험도 표시

- 며칠전간의 기상적 데이터를 바탕으로 ~~한시간 뒤~~ 전국의 산불 위험도가 어떻게 될 것이다.
  - 일단은 현시점의 위험도 예측
  - 성능 나올시에 기상청에서 제공하는 데이터를 통한 n시간 뒤 위험도 예측

- 각 지역적 특성을 반영하기 위해 자연적 데이터 및 기상데이터 정규화 진행
  - 행정구역별인 이유 : 소방서와 같은 요인은 행정구역별이 더 의미있음.
  
<aside>
💡 1차 목표 : 기상인자만으로 진행
<br>
</aside>

<aside>
💡 2차 목표 : 기상인자에 지형적특성(임업도) 반영
<br>
</aside>

<aside>
💡 3차 목표 : 기상인자 + 지형적특성 + 인적특성
<br>
</aside>

## 데이터

- 산불피해대장 ( 2001 ~ 2022 )
- 기상 데이터 → ASOS + AWS
- 인적 데이터 → 소방서, 등산로, 대도시 인접도
- 자연적 데이터 → TPI, 임업도
