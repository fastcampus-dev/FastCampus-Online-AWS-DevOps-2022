# node base image 설치
FROM node:16-slim
# 기본 디렉토리 지정
WORKDIR /usr/src/app
# 소스 복사
COPY . .
# 패키지 설치
RUN npm install
# Listen 포트 정의
EXPOSE 8080
# 서버 기동
CMD ["npm", "start"]