<details>
<summary> 초기 계획 및 진행과정 2023.02.01~2023.03.12 </summary>
<div markdown="1">       

# Forecasting-the-risk-of-forest-fires
## 산불 위험도 예측을 통한 정보제공 서비스
[2023-1] Capstone Project @SJU

project term 2023.02.01~

## 기상인자와 **인간인자**를 반영한 산불 위험도 예측

- 전국 데이터를 바탕으로 학습을 진행한 뒤 행정구역별(읍면동)로 나누어 위험도 표시

- 며칠전간의 기상적 데이터를 바탕으로 ~~한시간 뒤~~ 전국의 산불 위험도가 어떻게 될 것이다.
  - 일단은 현시점의 위험도 예측
  - 성능 나올시에 기상청에서 제공하는 데이터를 통한 n시간 뒤 위험도 예측

- 각 지역적 특성을 반영하기 위해 자연적 데이터 및 기상데이터 정규화 진행
  - 행정구역별인 이유 : 소방서와 같은 요인은 행정구역별이 더 의미있음.
  
- 웹 사이트 구현

## 데이터

- 산불피해대장 ( 2001 ~ 2022 )
- 기상 데이터 → ASOS + AWS
- 인적 데이터 → 소방서, 등산로, 대도시 인접도
- 자연적 데이터 → TPI, 임업도

## 정규화
정규화의 이유 -> 지역 별로 다른 기상적 특성을 가지고 있기 때문
- 산불발생지역별 정규화(Aws 기준 정규화)
- 전체기상데이터 정규화

## 결측치 처리 - (상대습도, 실효습도, 강수량, 풍속, 기온)
1. 가장 인접한 관측소에서 데이터 끌어오기
2. 거리가 30km 이상이면 그 지역의 연간 월평균으로 채우기 
3. 데이터 특성상 월 평균이 의미가 적을 수 있음 - 추가 결측치 처리방안 필요
  - 이동평균으로 결측값 채우기
  - 보간법으로 NAN 처리 후 사전관찰 방지를 위해 이전의 데이터 사용하기

## 모델링
- 분류기반모델 -> Randomforest/Catboost

## Process
1. AWS, ASOS Raw 데이터 수집 → 시계열
2. 데이터 윈도우 추가 (4일)
3. 실효습도 피처 추가
4. 섬은 drop
5. AWS(기상인자), ASOS(상대습도) 지점별 이동평균으로 결측값 채우기
6. 정규화 진행 여부
    1. 정규화 미진행
        1. 임상도 포함 데이터(4922개)
        2. 임상도 미포함 데이터
    2. 지점별 정규화 진행
        1. 임상도 포함 데이터(4922개)
        2. 임상도 미포함 데이터
<br><br>
<aside>
💡 1st goal : 기상인자만으로 진행
<br>
</aside>

<aside>
💡 2nd goal : 기상인자에 지형적특성(임상도) 반영
<br>
</aside>

<aside>
💡 final goal : 기상인자 + 지형적특성 + 인적특성
<br>
</aside>
</div>
</details>

### 새로운 IDEA

기존 Dataframe 형태로 분석을 진행할시의 문제점으로

1. 정확한 산불 발생위치의 기상 정보를 고려할 수 없다.
2. 산불이 난 지점의 임상이나 경사같은 지형요인을 반영하기 어렵다.
3. 피해면적을 라벨로 학습하여 피해 예상면적을 구하기에는 발생이후의 기상인자를 고려하지 않는다.
4. 인적 특성을 반영하기 어렵다.

와 같은 문제가 있었다.

- 따라서 이런 문제를 해결하고자 기상인자들 및 식생지수, 지형(TPI)등의 이미지 데이터를 수집하여 산불발생지역 
<br>인근을 Crop하고 발생 데이터에 1을 라벨링하여 **산불 발생 예측**으로 전환하기로 결정하였다. 

- 이미지 데이터의 수집 및 실시간 서비스에 활용하기위한 자동화 문제가 현재 관건이며 이를 해결시에 <br>
한국에서 기존에 시도하지 않은 방식의 분석기법이 될 것으로 기대된다.
<br>

**2023.03.22**
<br>

현재 진행도 :
  1. QGIS를 통해 AWS 지점별 보간이 가능한 것을 확인 후 파이썬에서 이를 자동화하는 방안 발견
  2. 선행연구들을 통해 반영할 피쳐들을 찾고 스케일이 어떤지 

추후 계획 : 데이터 수집 자동화로 이미지로 된 기상 및 지형적 요인, 추가로 인적요인까지 반영하여 딥러닝을 통해 <br>
산불 발생예측을하여 이를 확률로 구분하여 지점별 발생가능성을 시각화할 것임

<br><br>
**2023.04.10 진행상황**
- 파이썬으로 AWS 관측 지점 데이터를 불러와서 IDW 방식으로 보간하여 전국의 데이터를 생성
- 그중 강원도 부분만 잘라서 raster 형태로 수집

- <b>How to Crop?</b>
  1. Raster 파일을 csv 형태로 변환하여 Index를 뽑고 Dataframe에 접근하는 형태로 Crop 
  2. Crop한 파일은 csv 형태이므로 다시 이미지로 변환하기 위해서 csv to raster 과정을 진행 
  3. raster는 회색조로 여러 피쳐를 전부 회색조로 학습시키면 정확한 특징 추출이 어려울 것으로<br> 예상되어 함수를 정의하여 컬라형태로 plot을 띄운 후, 이미지로 저장 
  4. 컬러형태의 png 이미지를 모델의 input으로 사용 <br>

<br><br>

**2023.04.11 진행상황**
- 산불난 지점에 대한 이미지 크롭 완료. 
  - 기상 (기온, 습도, 강수량, 풍속, 실효습도)
- RGB 이미지 5개를 하나의 input으로 학습시키기 위한 데이터 로더 생성 및 모델링 진행중

해야할일
- 맵 보간시에 결측값이 많아서 이를 처리해야함
- 기상 데이터와 지형 및 인적요소의 스케일을 맞추어야함
