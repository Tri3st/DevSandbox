FROM node:22-alpine AS build-stage

WORKDIR /app

COPY ./package.json .

RUN npm install

COPY . .

RUN npm run build

# production stage
FROM nginx:1.13.12-alpine AS production-stage

COPY --from=build-stage /app/frontend/dist /var/www/mysite
# COPY frontend/dist /usr/share/nginx/html

EXPOSE 5173

CMD ["nginx", "-g", "daemon off;"]
