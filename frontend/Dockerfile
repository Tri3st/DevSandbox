FROM node:18-alpine AS build-stage

WORKDIR /app

COPY ./package.json .

RUN npm install

COPY . .

RUN npm run build

# production stage
FROM nginx:1.27.2-alpine AS production-stage

COPY --from=build-stage /var/www/mysite 
# COPY frontend/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
