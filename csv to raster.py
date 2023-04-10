import numpy as np
import rasterio
from matplotlib import pyplot as plt

# CSV 파일 읽어오기
data = np.loadtxt('파일명.csv', delimiter=',', skiprows=1, encoding='utf-8')

# 래스터 이미지 생성
with rasterio.open(
    '파일명.tif', 'w',
    driver='GTiff',
    height=data.shape[0],
    width=data.shape[1] - 1,  # 첫 번째 열을 제외한 폭(width)
    count=1,
    dtype='float64',
    crs='+proj=latlong',
    transform=rasterio.transform.from_bounds(0, 0, data.shape[1]-1, data.shape[0], data.shape[1]-1, data.shape[0])
) as dst:
    dst.write_band(1, data[:, 1:])  # 첫 번째 열을 제외한 데이터를 쓰기
    
    
# 래스터 정보 출력
with rasterio.open('파일명.tif') as src:
    # 속성 정보 출력
    print('Width:', src.width)
    print('Height:', src.height)
    print('Number of Bands:', src.count)
    print('CRS:', src.crs)
    print('Transform:', src.transform)
    
    # 래스터 데이터 읽기
    data = src.read()
    
  
# tif 파일 열기
with rasterio.open('humidity.tif') as src:
    # 래스터 데이터 읽기
    data = src.read(1)

# 이미지 시각화
plt.imshow(data, cmap='gray')
plt.show()
