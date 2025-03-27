FROM node:22-alpine AS build-stage

WORKDIR /app

COPY package.json package-lock.json ./  # Ensure both package.json and package-lock.json are copied 

RUN npm install

COPY . .  # Copy everything after dependencies are installed

RUN npm run build  # Ensure this creates 'dist' inside /app

# production stage
FROM nginx:1.13.12-alpine AS production-stage

RUN mkdir -p /var/www/mysite

# Copy Vue build output to the correct directory
COPY --from=build-stage /app/dist /usr/nginx/html  # Fixed destination path

EXPOSE 80  # Nginx default port (was 5173, which is default for vite dev server)

CMD ["nginx", "-g", "daemon off;"]
