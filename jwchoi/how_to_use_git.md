1. Git 관련 유의사항
	a. 공간은 총 4가지 이상: Local PC - Staging - Local repository - Remote repository

2. update 하는 방법
   	1. 폴더를 하나 만들어서 레퍼지토리를 클론할 공간을 만든다.
   	2. 레퍼지토리에 readme.md 같은 파일을 하나 만들어준다. (파일이 전혀 없는 레퍼지토리는 클론할때 문제 생겼음.)
   	3. git clone 주소(ex: git clone https://github.com/icefoxand/Web_Django.git): 깃 레퍼지토리가 똑같이 로컬PC에 생김
	4. git pull : 리모트 레퍼지토리의 뉴버전을 로컬 레퍼지토리로 가져와서, 업글
	5. git add . : 내가 로컬 피시에서 특정 내용을 변경후, staging 공간으로 변경사항을 옮김
	6. git commit -m '하고싶은말' : 변경사항을 로컬 레퍼지토리에 적용함
	7. git push origin 브랜치이름(ex: git push origin main) : 변경사항이 적용된 버전을 리모트 레퍼지토리에 보내서, 업글
    
3.  로컬 레포지토리 있고, 깃허브(remote repository) 있는데 둘이 연결이 안된 경우: git remote add origin https://github.com/icefoxand/Web_Django.git

4.  자리 옮기면 할 일
   	- git global 을 user.name, user.email 로 업데이트 안해주면 그 자리에 저번에 앉았던 사람의 이름, 이메일로 올라가게 됨
        - git config --global user.name "jiwonchoi" --replace-all
        - git config --global user.email "such159357@naver.com" --replace-all
        - 위의 두 명령어를 실행해줄 것
111