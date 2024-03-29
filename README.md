# ALPHA PONG

<img src="https://user-images.githubusercontent.com/58676453/179725992-941d0319-8e8e-40cd-8798-ea6558f59df3.png" width="500"/>


## Download Link

https://jin-gyu.itch.io/alpha-pong

압축 풀기 -> ALPHAPONG 폴더 -> main.exe 파일 실행


## Contributor

카이스트 산업및시스템공학과 [정진규](https://github.com/jeongjingyu)

부산대학교 IT응용공학과 [김세훈](https://github.com/ki-met-hoon)

포스텍 컴퓨터공학과 [박정은](http://github.com/jjungnii)



## Concept

<img src="https://user-images.githubusercontent.com/58676453/179738909-03c75f0d-fab3-470e-96b8-c90937ef77aa.png" width="300"/>


'ALL RESPECT FOR ATARI AND DEEPMIND...'

[퐁](https://namu.wiki/w/%ED%90%81)(Pong)은 1972년 Atari에서 출시한 아케이드 게임으로, 상업적으로 성공한 첫 비디오 게임이자 모든 비디오 게임의 어머니로 알려져 있으며, 단순한 2인용 탁구 게임이지만 여전히 재미있고 중독성이 있다.

[알파고](https://namu.wiki/w/%EC%95%8C%ED%8C%8C%EA%B3%A0)(ALPHAGO)는 2015년 구글의 Deepmind에서 출시한 인공지능 바둑 프로그램으로, 인공지능을 세상에 가장 크게 알린 프로그램이며, 강화학습을 통해 승리 가능성을 높이는 다음 수를 예측한다.

ALPHAGO의 방식을 Pong에 적용한 ALPHAPONG은 출시 50년이 지난 기존 Pong 게임에 강화학습 기술을 적용, agent의 학습량에 따라 서로 다른 레벨의 AI를 설정하여 1인 플레이어가 AI를 상대하게 한다.

거기에 흩뿌려져있는 이스터에그는 덤!


## Brief Overview

- 강화학습을 통해 Pong에서의 state에 따라 agent가 action을 학습
- 학습량에 따라 모델의 parameter를 가져와 EASY, NORMAL, HARD 모드로 설정
- GHOST MODE!


## Dependency

- python: 3.10.5
- pygame: 2.1.2
- tensorflow: 2.9.1
- matplotlib: 3.5.2
