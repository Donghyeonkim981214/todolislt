# ToDoList_Renewal

## 0. 목차
1. 프로젝트 소개
  * ToDoList_Renewal
  * 개발환경
2. 기능소개
  * 기본 기능
  * 로그인 후 가능한 기능

## 1. 프로젝트 소개
* ToDoList_Renewal
  본 프로젝트는 전에 만든 todolist를 보완한 프로젝트로 특히 UI 부분을 좀 더 다듬고 AWS EB를 통해 배포한 todolist웹입니다.  
  Web url: http://todolist-env.eba-smsu6wyz.ap-northeast-2.elasticbeanstalk.com/
* 개발환경
  * os: windows10
  * editor: visual studio code
  * language: python 3.6
  * backend: Django 3.1.7
  * database: mysql
  * frontend: html, css
  * deploy: AWS EB

## 2. 기능 소개
  * 기본기능(Guest mode)
  로그인하지 않고 사용할 수 있는 기능은 다음과 같습니다.
   1. ToDo 작성 및 삭제
   2. ToDo 수정

  * 로그인 후 추가로 가능한 기능(USer mode)
   1. ToDo 완료
   2. 마감기한 내 실패한 ToDo 따로 분리
