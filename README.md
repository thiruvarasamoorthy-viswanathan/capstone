# capstone
Capstone - Cloud DevOps Engineer Nanodegree Program Project 5

[![CircleCI](https://circleci.com/gh/thiruvarasamoorthy-viswanathan/capstone/tree/main.svg?style=svg)](https://circleci.com/gh/thiruvarasamoorthy-viswanathan/capstone/tree/main)

In this project, below are the learning objectives achieved:

- Building a python application
- Lint the application code
- Build docker image and push to Docker hub
- Create EKS Cluster and Nodes and deploy the image to EKS
- Test the application (Smoke Test)
- Rolling deployment

### Project Submission

- Below are the various links:

1. GIT: https://github.com/thiruvarasamoorthy-viswanathan/capstone
2. CircleCI : https://app.circleci.com/pipelines/github/thiruvarasamoorthy-viswanathan/capstone?filter=all
3. Doker Hub: https://hub.docker.com/repository/docker/vtm1983/udacity-devops-capstone/tags?page=1&ordering=last_updated
4. Application Load Balancer link: http://a7f070a87060d449e9a26368929d3526-1292348691.us-west-2.elb.amazonaws.com/ (Please note the link will be available for few hours as its deplyed in Udacity account and ec2 instance shutdown in couple of hours. Screenshots attached of the link)

-  screenshots in PNG format, named using the screenshot number listed as below. These screenshots are included in code repository in the root folder.
<br/><br/>
## WORK FLOW

### **1. Linting**

***Lint Failure***

![alt text](https://github.com/thiruvarasamoorthy-viswanathan/capstone/blob/main/screenshots/01_Execute_Linting_Failure_CircleCI.png)

***Lint Success***

![alt text](https://github.com/thiruvarasamoorthy-viswanathan/capstone/blob/main/screenshots/02_Execute_Linting_Success_CircleCI.png)


### **2. Docker Build and Push to Docker Hub**

***Docker Build Failure***

![alt text](https://github.com/thiruvarasamoorthy-viswanathan/capstone/blob/main/screenshots/03_Build_Docker_Container_Build_Failure_CircleCI.png)

***Docker Build Success***

![alt text](https://github.com/thiruvarasamoorthy-viswanathan/capstone/blob/main/screenshots/04_Build_Docker_Container_Build_Success_CircleCI.png)

***Docker Hub Push Success***

![alt text](https://github.com/thiruvarasamoorthy-viswanathan/capstone/blob/main/screenshots/05_Build_Docker_Hub_Push_Success_CircleCI.png)

![alt text](https://github.com/thiruvarasamoorthy-viswanathan/capstone/blob/main/screenshots/06_Docker_Hub_Push_Success.png)

### **3. EKS Kluster/Node creation and Application deployment**

***EKS Cluster and Node Creation***

![alt text](https://github.com/thiruvarasamoorthy-viswanathan/capstone/blob/main/screenshots/08_EKS_Cluster_Creation_AWS_Console.png)

![alt text](https://github.com/thiruvarasamoorthy-viswanathan/capstone/blob/main/screenshots/09_EKS_WorkerNode_Creation_AWS_Console.png)

![alt text](https://github.com/thiruvarasamoorthy-viswanathan/capstone/blob/main/screenshots/10_EKS_Cluster_AWS_Console.png)

![alt text](https://github.com/thiruvarasamoorthy-viswanathan/capstone/blob/main/screenshots/11_EKS_WorkerNode_EC2_AWS_Console.png)

***EKS Deployment***

![alt text](https://github.com/thiruvarasamoorthy-viswanathan/capstone/blob/main/screenshots/07_EKS_Cluster_Container_Deployment_CircleCI.png)

![alt text](https://github.com/thiruvarasamoorthy-viswanathan/capstone/blob/main/screenshots/12_EKS_WorkerNode_LoadBalancer_AWS_Console.png)

![alt text](https://github.com/thiruvarasamoorthy-viswanathan/capstone/blob/main/screenshots/13_Application_Loadbalancer_Link.png)


***Smoke Test***

![alt text](https://github.com/thiruvarasamoorthy-viswanathan/capstone/blob/main/screenshots/14_Smoke_Test_Loadbalancer_CircleCI.png)

***Rolling Deployment***

![alt text](https://github.com/thiruvarasamoorthy-viswanathan/capstone/blob/main/screenshots/15_Rollingdeployment_CircleCI.png)

![alt text](https://github.com/thiruvarasamoorthy-viswanathan/capstone/blob/main/screenshots/16_DockerHub_Neimage.png)

![alt text](https://github.com/thiruvarasamoorthy-viswanathan/capstone/blob/main/screenshots/17_Workflow_Rollingdeployment_CircleCI.png)

