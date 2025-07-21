# Lead Collector with AWS

This project is an **adaptation of a real-world solution** delivered to a client who needed a lightweight and scalable way to collect leads in the field. It has been restructured to protect the client's privacy while demonstrating the usefulness of a practical, serverless, and cost-free solution. It has been restructured to highlight its value in **data engineering** and **real business applications**.

Link to the app [here](https://main.dafmmtpmb6gia.amplifyapp.com/).

---

## Business Context

Field sales agents working at events, street campaigns, or door-to-door initiatives often need a simple solution to quickly capture **names and phone numbers** of potential leads using their mobile devices, without needing to install an app.

The client required:

- A **lightweight and functional landing page**
- That could be **accessed via a shared link**
- **Mobile-friendly** interface
- Real-time **data storage for later analysis**

---

## Architecture Overview

This project uses AWS services to build a scalable, serverless application:


```mermaid
graph TD

  %% Fluxo principal

  Amplify[Landing Page - AWS Amplify]
  Lambda[AWS Lambda]
  APIGW[API Gateway]
  Dynamo[DynamoDB]


  Amplify --> Lambda
  Lambda --> APIGW
  APIGW --> Dynamo
  ```

- **AWS Amplify**: For frontend deployment  
- **AWS Lambda**: For processing lead submissions  
- **API Gateway**: To connect the frontend to the backend  
- **AWS DynamoDB**: NoSQL database to store the submitted data  


The application allows users to register their names and phone numbers through a mobile-friendly form. These entries are processed by a Lambda function and securely stored in DynamoDB via a serverless pipeline.
