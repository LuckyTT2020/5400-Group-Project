# Amazon Query Search System

###   This project develop query search system for users to find desired product with correct rating score through typing in the keyword for search. Furthermore, we will store the search history and analyze it (provide the most poupular search). The goal of this project is to provide product recommendations on user end and collect users' selection for organization analysis. The data collection is fetch from existing Kaggle dataset called Amazon Review.

##### The project use flask as the html creating tool to display the user interface and connect to MongoDB database for query search. Then store search history in SQL database for the future analysis.
> 1.The localhost website is formulated using html file.\
> \
> 2. Users type in keyword and rating and search on the localhost website.\
> \
> 3. The request is sent with flask to local MongoDB on docker.\
> \
> 4. Keyword and rating input will be put in query function to create new query item.\
> \
> 5. The file processes the query search and get query results.\
> \
> 6. Query results are sent back to the localhost website and being displayed for customers.\

##### Prerequisites:
1. set up virtualn enviroment\
`$ pip3 install virtualenv` \
`$ virtualenv env`  \
`$ source env/bin/activate`
2. download flask and run \

3. Docker pull for mongoDB image
`$ docker pull mongo` \

4. install related packages



User Interface\
Type in desirable search keyword and the product overall rating you want to, scale 1 to 5, then hit search.\
The page will display a list of products from Amazon Review Records to provide suggesting products for customers.\
If go to search_analysis page, it will return the most popular search historys.







