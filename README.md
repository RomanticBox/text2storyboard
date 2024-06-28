# Story Weaver

<div align="center">
<h3>24-1 YBIGTA 컨퍼런스</h3>

**StoryWeaver: 웹툰 작가를 위한 콘티 생성기**

<img src="https://img.shields.io/badge/React Native-61DAFB?style=for-the-badge&logo=React&logoColor=white"> <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=FastAPI&logoColor=white"> <img src="https://img.shields.io/badge/OpenAI API-412991?style=for-the-badge&logo=OpenAI&logoColor=white"> <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=MySQL&logoColor=white">

</div>

## 목차
- [문제 정의](#문제-정의)
- [파이프라인](#파이프라인)
- [접근 방법](#접근-방법)
- [실행예시 ](#실행-결과과)
- [팀 구성](#팀-구성)

---

## 문제 정의

### 배경

StoryWeaver 프로젝트를 진행하게 된 이유는 다음과 같다.

1. **웹툰 업계의 열악한 작업 환경**
- 웹툰 창작에는 많은 시간이 소요되며,이로 인해 작가들의 건강 문제 등이 주목받아 왔다.

2. **기존 작업 시간을 단축하기 위한 시도와 한계**
- 자동 채색 AI, 웹툰 작가의 그림체를 학습한 이미지 생성 모델 등 다양한 AI 활용 시도들이 있었다.
- 하지만, 작가의 허락 없는 이미지 학습 및 독자들의 반발로 호의적인 반응을 얻지 못했다.

이에, StoryWeaver는 웹툰 작가의 대본/시나리오를 바탕으로 **콘티를 생성**함으로써 웹툰 작가의 작업 시간을 축소하고, 웹툰 작가의 노동 환경을 개선하는 것을 목적으로 한다.

- ***스토리보드(콘티)란?***
   - ***본격적인 작화 작업에 앞서 만드는 그림의 밑바탕. 일종의 청사진에 해당한다.***

### 목표

 StoryWeaver는 사용자가 자연어 스토리를 입력하면 LLM과 SDXL 모델을 통해 입력된 상황에 맞는 여러 장의 콘티 이미지를 생성한다. 이를 통해 다음과 같은 효과를 기대해 볼 수 있다.

1. **작업시간 단축**
2. **저작권 문제 해소**
3. **작가의 고유한 작업 스타일 유지**

 구도 구상 및 과

![Main](/imgs/1.PNG)

![Storytelling Input](/imgs/2.PNG)

![Character Input](/imgs/3.PNG)

![Style Selection](/imgs/4.PNG)

![Character Image Selection](/imgs/5.PNG)

![Output](/imgs/6.PNG)

---

## 팀 구성

|이름|팀|역할|
|-|-|-|
|**김예린**|DA|TeamLeader/LLM pipeline/Frontend/PresentationMaterial|
|**김채현**|DS|LLM pipeline/LLM+SDXL pipeline/Frontend|
|**남세현**|DS|DreamBooth finetuning/data processing/Consistency Module|
|**서건하**|DE|Backend/Back+Frontend Connect|
|**양인혜**|DS| dataset preparation/data processing/DreamBooth finetuning|
|**이성현**|DS| dataset preparation/data processing/DreamBooth finetuning|
|**정수현**|DS| data processing/DreamBooth finetuning/LLM+SDXL pipeline|
