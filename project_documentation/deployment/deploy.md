# Deployment Guide

This document outlines the deployment requirements and steps for Project Nexus.

## Requirements

- **CI/CD Pipeline:**  
  The project uses a CI/CD pipeline defined in [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml) that builds the Docker image for the ARM64 architecture. Ensure your server also has ARM64 architecture.

- **Project Directory on Server:**  
  Set up a project directory on your server that includes:
  - [docker-compose.yml](docker-compose.yml)
    - the docker-compose.yml file should specify the the image in the web service section instead of building it using Dockerfile
  - [nginx.conf](nginx.conf)
  - [.env](.env)  
  All files must have proper read permissions for the CI/CD pipeline to access and deploy them.

## Deployment Steps

1. **CI/CD Pipeline Trigger:**  
   When the CI/CD pipeline runs, it builds the Docker container with the ARM64 flag and pushes the image to your Docker registry.

2. **Container Deployment:**  
   The deployment job on your server performs:
   - `docker pull sofib1/project-nexus:latest`
   - `docker compose down` followed by `docker compose up -d`

3. **Post-Deployment Setup:**  
   *For the first deployment only, or whenever necessary:*
   - Run database migrations:  
     ```sh
     docker-compose exec web python manage.py migrate
     ```
   - Create a superuser:  
     ```sh
     docker-compose exec web python manage.py createsuperuser
     ```
   - Collect static files:  
     ```sh
     docker-compose exec web python manage.py collectstatic --noinput
     ```

## NGINX Configuration Enhancements

The current [nginx.conf](http://_vscodecontentref_/0) file can be extended for:
- Redirecting HTTP to HTTPS.
- SSL termination.
- Additional caching or load balancing rules.

## Useful Docker & Docker Compose Commands

- **Start or Restart Containers:**
  ```sh
  docker compose up -d
- **Stop Containers:**
  ```sh
  docker compose down
- **View Logs (e.g., for the web container):**
  ```sh
  docker compose logs -f web
- **Execute a Command Inside a Running Container:**
  ```sh
  docker compose exec web <command>
- **Rebuild Containers (if Dockerfile changes):**
  ```sh
  docker compose build

## Final Steps

1.  **Trigger CI/CD Pipeline:**

    Push your code changes to the `master` branch of your GitHub repository to trigger the CI/CD pipeline.

2.  **Monitor Deployment:**

    Monitor the pipeline execution in GitHub Actions to ensure a successful deployment.

3.  **Verify Application:**

    Access your application through your domain name (if configured) or server IP address to verify the deployment.
---

- Ensure that your environment file and all configuration files maintain the proper permissions so that the CI/CD process can read and deploy them successfully.