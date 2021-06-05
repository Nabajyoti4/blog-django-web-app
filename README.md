# blog-django-web-app
A blog made using Django backend to serve post to user and also display the contents related to the blogger. The whole application is fully hosted on AWS EBS service with S3 storage to store static files

The tech stack used are:
1. Django framework 
2. Postgres database from AWS RDS services
3. S3 storage to store static files like css , js , images and also uploaded files 
4. Hosting is done in ElasticBeanStalk in AWS

Website Functionalities:
1. Super admin can add Post, Author, Tags
2. A Post can have author and tags realted to it
3. User can view all post , single post
4. In single post user can give comments with comment form made with help of django Forms with validation 
5. From single post page user can mark or remove favorite post , which are stored in session


Index page
![alt text](https://github.com/Nabajyoti4/blog-django-web-app/blob/main/index.png)


Full post Page
![alt text](https://github.com/Nabajyoti4/blog-django-web-app/blob/main/post.png)
