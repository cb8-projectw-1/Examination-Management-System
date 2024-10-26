# Use the official Nginx image
FROM nginx:alpine

# Copy the HTML and CSS files to the Nginx folder
COPY static /usr/share/nginx/html

# Expose port 80 for HTTP
EXPOSE 80
