# Amazon Query Search System

###   This project develop query search system for users to find desired product with correct rating score through typing in the keyword for search. The goal of this project is to provide product recommendations on user end and collect users' selection for organization analysis. The data collection is fetch from existing Kaggle dataset called Amazon Review.

## The project use flask as the html creating tool to display the user interface and connect to MongoDB database for query search.

1. set up virtualn enviroment\
`$ pip3 install virtualenv` \
`$ virtualenv env`  \
`$ source env/bin/activate`
2. download flask and run \












User Interface\
Type in desirable search keyword and the product overall rating you want to, scale 1 to 5, then hit search.\
The page will display a list of products from Amazon Review Records to provide suggesting products for customers.\


Docker Part\
  Docker is required for MongoDB database, Please visit Mongodb website to find suitable ways to pull the image\
  For most of the cases, `$ docker pull mongo` \





