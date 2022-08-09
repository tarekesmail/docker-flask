**Flask API App**
This repo contains the flask python application with sample endpoints, This application Dockerized, and helm chart included

To Run the application on your local machine
1. Clone the repo
2. Build Container *`docker build . -t flask-api`*
3. Run Container *`docker run -p 5000:5000 flask-api`*


**Home Page**
> curl http://localhost:5000/

**List Users**
> curl http://localhost:5000/users

**List Apps**
> curl http://localhost:5000/apps

**Deploy in Kubernetes**
You can use helm chart to deploy the application in kubernetes by installing the chart and you can specify the namespace

    helm install flask-api ./helm/flask-api -n NAMESAPCE

**Editing the site URL**
You can edit values.yaml file and change `test.tarek.com` to the new domain name.

**Security Settings** 
This container running in kubernetes with UserID: 1000 and without Root Access in addition the readonly root file system.

**TODOs**

 - [ ] Enable multi stage image and add base image to accelerate the build
 - [ ] Run container as user from Dockerfile
 - [ ] Adding database to application and set environment variables
 - [ ] Use prometheus python module to collect metrics from running app
 - [ ] Apply testing in Docker build
 - [ ] Use CI/CD with something like github actions
 - [ ] If the cert-manager installed inside cluster we can add the annotations in the helm chart in values file
 - [ ] Adding secrets to vault and inject it using sidecar container to the application

