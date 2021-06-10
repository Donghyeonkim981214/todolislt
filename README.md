# ToDoList

ToDoList is a project with Django.

## Tech

ToDoList used the following techniques:

Backend
- python_version = "3.6"
- django

FrontEnd
- django-crispy-forms
- django-widget-tweaks
- bootstrap5

Editor
- visual studio code

Deploy
- AWS EB, S3, RDS
- Web url: <del>http://todolist-env.eba-smsu6wyz.ap-northeast-2.elasticbeanstalk.com/</del>(AWS요금부과 때문에 내려둔 상태)

## Features
### USER

#### home
You can choice two modes. One is Guest mode. Another is User mode.  
- Guest mode is does not require login. But After out page, Memo you created is all deleted.  
- User mode requires login. Memo you created is all saved. And Your memos are divided into three states.(Doing, Success, Failed)
<img width="80%" src="https://user-images.githubusercontent.com/43703346/121566713-beaeed80-ca58-11eb-91f4-4273ff10abf5.PNG"/>

#### log in
fisrt page is login page. If you don't have an account, you have to sign up.
<img width="80%" src="https://user-images.githubusercontent.com/43703346/121565749-bd30f580-ca57-11eb-8aea-0be343750617.PNG"/>

#### sign up
<img width="80%" src="https://user-images.githubusercontent.com/43703346/121565804-cc17a800-ca57-11eb-973c-f83caf643d52.PNG"/>

### GuestMode
#### create task
<img width="80%" src="https://user-images.githubusercontent.com/43703346/121566783-d0909080-ca58-11eb-940f-74be46d02000.gif"/>

#### delete task
<img width="80%" src="https://user-images.githubusercontent.com/43703346/121566828-dbe3bc00-ca58-11eb-94d0-da78894fa6e3.gif"/>

### User

#### create task
<img width="80%" src="https://user-images.githubusercontent.com/43703346/121567197-439a0700-ca59-11eb-862a-9c8f447c31b0.gif"/>

#### update task
<img width="80%" src="https://user-images.githubusercontent.com/43703346/121567226-4e549c00-ca59-11eb-8175-203d5f377879.gif"/>

#### delete task
<img width="80%" src="https://user-images.githubusercontent.com/43703346/121567282-5b718b00-ca59-11eb-8f18-e3bb1397c1e7.gif"/>

#### Doing
If memo is not due or set, Memo included in Doing.

#### Success
If memo is checked success, Memo included in Success.

#### Failed
If the memo is past due, Memo included in Failed.

### User
#### profile
You can update your profile.
<img width="80%" src="https://user-images.githubusercontent.com/43703346/121567935-1863e780-ca5a-11eb-8eb4-6526ea1c6376.PNG"/>
