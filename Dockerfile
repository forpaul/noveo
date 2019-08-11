FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /noveo_back
WORKDIR /noveo_back
COPY requirements.txt /noveo_back/
RUN pip3 install -r requirements.txt
COPY . /noveo_back/


FROM node:lts-alpine
RUN npm install -g http-server
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
EXPOSE 8080
CMD [ "http-server", "dist" ]