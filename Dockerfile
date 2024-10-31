# Use an official Node runtime as the base image
FROM node:20-alpine

# Set the working directory in the container to /app
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install the application dependencies
RUN npm install

# Install the Vue CLI globally (if needed for dev)
RUN npm install -g @vue/cli

# Expose ports
EXPOSE 8080 3000

# Command to start the Vue.js server
CMD ["npm", "run", "serve"]
