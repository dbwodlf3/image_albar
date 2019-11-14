# 할것

한글 인식 하기는 어렵고 그런 프로그램을 만드는데에는 시간이 오래걸리니 이미지를 짤라서 텍스트 영역을 얻고 어디에 속하는지 까지만 만들자.

# Image 짜르기

이미지 짜르기.

openCV

# 문제 상황
사진은 다 짤려있음.

문제가 되는건 전시장에 배치를 했는데, 어느면의 어느칸 어느 줄에 위치해 있는지 모른다는 것.

이것을 사진을 찍엇기 때문에, 찍은 사진을 바탕으로 면, 칸, 줄 을 찾아야함.

## 데이터 형식
사진속 아이템이 5개씩, 사진 6장이 하나의 그룹을 이룸. (그런데 모든 사진이 그런건 아님. 자잘한 오류들이 있음. 똑같은 사진을 2장 찍었다거나, 전시되는 장소의 높이가 달라진다거나.)

근데 대부분은 위의 경우가 맞음...

오른쪽 위에서부터 1-1임.

## 해결 방법

사진속의 그림에서 칸과 줄을 찾는다.

해당 그림의 성명, 소속, 나이를 기반으로 등록 사이트에 검색한다.

### 사람 손으로 수기 입력

자료 데이터가 6만5천건이다...

### 프로그램으로 등록

우선 사진의 이미지를 OCR을 할 수 있어야 한다.

이미지를 OCR한 다음에, DB 쿼리를 보내야 한다. (DB API를 제공 해 줘야함.)


## Todo List
- [ ] 자를 이미지의 좌표를 구하기.