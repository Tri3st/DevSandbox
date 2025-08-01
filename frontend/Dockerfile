FROM node:18-alpine AS build-stage

WORKDIR /app

COPY ./package.json .

RUN npm install

COPY . .

RUN npm run build

# production stage
FROM nginx:1.27.2-alpine AS production-stage

COPY --from=build-stage app/dist /usr/share/nginx/html 
# COPY frontend/dist /usr/share/nginx/html

RUN mkdir -p /etc/nginx/certs

# COPY conf/certs/ /etc/nginx/certs/
COPY conf/nginx-default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

# CMD [ "top" ]
CMD ["nginx", "-g", "daemon off;"]
