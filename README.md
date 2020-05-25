# 메모장 프로젝트

그리드 형태의 메모장. 간단히 메모할 수 있는 기능과 수정, 삭제의 기능을 담은 소규모 프로젝트.



## 작업 환경

OS : Windows 10, macOS 10.15 Catalina

Language : Python3.7.7, HTML5, Jinja2

Framework : django 3.0.6, Bootstrap 4.4.1

DB : SQLite3

Editor : VSCODE 1.45.1



## DB설계

id : PRIMARY KEY, integer

title : VARCHAR(200)

content : TEXT

create_date : datetime

update_date : datetime

![image-20200525105832486](https://user-images.githubusercontent.com/62881936/82773203-6f614380-9e7c-11ea-8fa8-9aac4a001b80.png)

![image-20200525105857008](https://user-images.githubusercontent.com/62881936/82773205-70927080-9e7c-11ea-83f4-98558d4542ba.png)

> 더미 데이터



## 참고 사이트

아이콘 : https://remixicon.com/

Bootstrap : https://startbootstrap.com/ , https://getbootstrap.com/



## 작업기간

2020/05/22 : DB 설계 및 스토리보드 설계

2020/05/23 : 코딩 작업 및 스토리보드 작업

2020/05/24 : 화면단 및 디자인 작업

2020/05/25 : 작업 마무리 및 보고서 작성



## 화면 구성

![image-20200525111021183](https://user-images.githubusercontent.com/62881936/82773206-70927080-9e7c-11ea-9fd0-9723d8f02fa7.png)

> 메인 화면. 메모 테스트4 를 보면 메모 내용이 길어지면 생략을 하고 더보기 버튼이 보이게 된다.



![image-20200525111101812](https://user-images.githubusercontent.com/62881936/82773207-712b0700-9e7c-11ea-9905-22e934b717f5.png)

> 메인 메뉴에서 좌측 "추가" 버튼을 눌러 새로운 메모 추가 화면 진입



![image-20200525111204927](https://user-images.githubusercontent.com/62881936/82773208-71c39d80-9e7c-11ea-9e47-78e5c6641897.png)

> 작성 된 메모의 상세 보기 화면



![image-20200525111236006](https://user-images.githubusercontent.com/62881936/82773209-71c39d80-9e7c-11ea-9f5e-bc70e6e35c13.png)

> 삭제 버튼 클릭시 팝업



![image-20200525111312426](https://user-images.githubusercontent.com/62881936/82773211-725c3400-9e7c-11ea-8bed-61b7e18cd06b.png)

> 상세 보기 화면에서 가운데 "수정" 버튼 클릭시 나오는 수정 화면



## 코드 페이지

![image-20200525111744214](https://user-images.githubusercontent.com/62881936/82773213-72f4ca80-9e7c-11ea-98c4-3eb8d304226a.png)

자세한 코드는 깃허브(github)에 올렸습니다. (https://github.com/yksoon/project_django_memo)



## 프로젝트를 진행 하며 힘들었던 점이나 문제점 및 해결방안

프론트 엔드 쪽의 화면단 구성이나 디자인이 어려웠습니다.

대중들이 보는 이쁨이란 기준을 충족시키는 것이 어려웠고, `<div>` 태그나 `<p>`태그 등 화면 단을 나누는 것이 익숙하지 않아 어려웠던 점이 있었습니다. 물론 부트스트랩 사용도 저에게는 까다로웠습니다.

많이 만져보고 하나하나 디자인 해 가면서 알게 되었던 점도 있고, 다음 프로젝트 진행에는 조금 더 원활하게 화면 구성을 할 수 있을 것 같습니다.



그리고 템플릿 페이지 내에 메모 삭제 코드가 스크립트 안에서 마지막 index값만 불러오는 버그가 있었습니다. 인터넷도 찾아보며 해당 버그에 대해 많은 시간을 소비 하게 되었습니다.

하지만 문제점은 스크립트 안 Jinja2 코드의 문제 였고, 해당 메모의 index 값을 스크립트 안 삭제 url에 매개변수로 보내어 주소로 바로 보내 이를 해결 하였습니다.



## 발전하기 위한 방향

본 프로젝트는 매우 심플한 기본 구조로 되어 있습니다. 아직 여러가지 기능이 들어가 있지 않고, 기본 CRUD 구조로만 되어 있는 기능입니다.

공유 및 사진 첨부 등 여러가지 기능을 추가 하면 더 나은 프로젝트로 진행이 될 것 같습니다.



## 프로젝트를 하며 느낀점

혼자 1인 프로젝트를 진행하려다보니 초기 설계부터 마무리까지 너무 바빴던 것 같습니다. 화면 디자인 및 여러가지 기능을 구현 할 수 없어 아쉬웠고 다음 프로젝트 진행시 본 프로젝트를 참고하며 더 나은 프로젝트를 진행 하는 방향이 좋을 것 같습니다.



