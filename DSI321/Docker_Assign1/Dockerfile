FROM node:alpine

COPY . /user/app
WORKDIR /user/app

RUN npm install
EXPOSE 5000

CMD ["npm", "start"]