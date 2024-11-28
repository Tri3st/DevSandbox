FROM node:22-alpine AS build-stage
WORKDIR /app
COPY frontend/package*.json ./
RUN npm install
COPY . .
 
RUN npm run build

# production stage
FROM nginx:1.13.12-alpine AS production-stage
COPY --from=build-stage /app/frontend/dist /usr/share/nginx/html
# COPY frontend/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
