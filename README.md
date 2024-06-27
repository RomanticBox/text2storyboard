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
- [실행예시 ](#실행-예시)
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

 구도 구상 및 스케치 작업에 필요한 시간을 단축하면서도, 콘티 단계에서는 변형 및 활용이 자유롭기 때문에 창작의 자율성 역시 보장할 수 있다.

---

## 파이프라인

StoryWeaver은 다음과 같은 파이프라인을 거쳐 작동한다.

![Pipeline](/imgs/pipeline.PNG)

### 사용 모델

- LLM : Gpt-3.5-turbo-instruct
- Image Generation model : SDXL with Dreambooth training (Kohya)
- consistency block from Story Diffusion

### 작동 과정

1. 사용자로부터 Story telling text를 받아, LLM으로 변환한다. 이때, 이미지 생성을 위한 여러 개의 문장으로 구성된 Image Captions가 생성된다.

2. Image Captions를 LLM에 넣어 스토리의 메인 캐릭터와 캐릭터가 등장할 이미지 변호 (Scene)을 추출한다.

3. 사용자로부터 메인 캐릭터의 특징을 인풋으로 받아, LLM을 통해 이미지 생성에 활용하기 위한 character prompt로 변환한다.

4. (Style Selection) 사용자가 여러 개의 그림체 중 원하는 그림체를 선택한다. 사용자의 선택이 백엔드로 전달되어, 미리 각기 다른 그림체 이미지로 학습된 다섯 개의 모델 중 하나가 선택된다.

5. 선택된 모델로 Character Prompt를 인풋으로 하여 여러 장의 Character Images가 생성된다. 

6. (Character Selection) 사용자는 여러 캐릭터 후보 중 가장 마음에 드는 것을 선택하여 최종 콘티 생성에 반영할 수 있다.

7. 사용자가 선택한 캐릭터 이미지는 맨 처음 생성한 Image Caption과 함께, 학습된 SDXL (Style Selection 단계에서 선택된 것) + Consistency Block을 통과하며 여러 장의 콘티 이미지를 생성한다.

8. 사용자는 웹페이지에서 생성된 이미지를 다운로드 받을 수 있다.


---

## 접근 방법

1. **데이터셋**
    - 웹 크롤링을 통해 영어-콘티 이미지 쌍을 수집하였으며, 이미지 분리 및 태깅을 진행하였다.
    - 필요에 따라 각 그림체 별 이미지를 추가로 수집하였다.

2. **LLM**
    - GPT3.5-instruct-turbo 모델을 활용해 사용자에게서 받은 Storytelling text를 image caption으로 변환하였다. 이때, 문장의 개수는 랜덤이며, 문장 개수가 곧 최종 생성될 콘티 이미지의 개수를 의미한다.
    - 추가로, LLM을 통해 스토리에 기반한 메인 캐릭터 및 캐릭터가 등장하는 씬 번호를 추출했고, 메인 캐릭터 프롬프트를 작성하였다.

3. **SDXL**

    1. **Dreambooth Training**
        - 적은 양의 이미지로도 text2image 모델을 개인화할 수 있는 학습 방법이다.
        - Kohya Dreambooth를 활용하여 각 그림체별 총 5개의 SDXL 모델을 학습시켰다.
        - full-training보다 효율적인 학습이 가능하며, Identifier token을 프롬프트에 넣어 간단히 학습된 스타일을 반영한 이미지를 생성할 수 있다.


    2. **Consistency**
        - 여러장에 걸쳐서 동일한 등장인물이 생성되게 하려면 Consistency 문제를 해결해야 한다.
        - StoryDiffusion에서 공개한 consistent genration 모듈 코드를 활용하였다.
        - 이미지 캡션, 메인 캐릭터 프롬프트와 캐릭터가 등장하는 씬 (이미지) 번호를 기반으로 일관성 있는 콘티 이미지를 생성하고자 했다.


4. **프론트엔드/백엔드/DB**
    
    - LLM, 5개의 학습된 SDXL 모델을 연결하여 파이프라인 단계 별 사용자와 모델 간 상호작용이 가능하도록 구현했다.

        - 프론트엔드: React, 사용자 input 입력
        - 백엔드: FastAPI, 모델 inference 진행
        - DB: MongoDB, 사용자 input 및 생성된 promt, image 저장

---

## 실행 예시

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
|**김예린**|DA|팀장/LLM pipeline/Frontend/PresentationMaterial|
|**김채현**|DS|LLM|
|**남세현**|DS| ... |
|**서건하**|DE|백엔드/프론트/ ... |
|**양인혜**|DS| dataset preparation/data processing/DreamBooth finetuning|
|**이성현**|DS| dataset preparation/data processing/DreamBooth finetuning|
|**정수현**|DS| ... |
