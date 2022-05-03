# mongodb-import-world-factbook
This is a basic script used to import the CIA's World Factbook JSON set into a MongoDB database stored in an Atlas Cluster

This code was created as a supplement to a Database course within the Harvard Extension CSCIE59 Class and is available for free use.

Do not expect error checks, nice abstraction, or...well, you already know. Its literally one python file :). This file takes in only a MongoDB connection string as a parameter. 

Ex: “mongodb+srv://<<username>>:<<password>>@<<yourcluster>>/myFirstDatabase?retryWrites=true&w=major"

You don't need to change the myFirstDatabase as the code is hardcoded to the database and collections names that I created in my MongoDB Cloud database. The DB and Collections are named world_information and countries. If you created a cluster before stumbling upon this code, you can update the script to use your db and collections name. 
  
Once you clone this repo, you will also need to clone the World Factbook json repo into the working directory of this repo

This one -> https://github.com/factbook/factbook.json.git
  
Then just run:
  
python3 import_worldfiles.py <your connection string>

Then it should just work. Hopefully. :)
  
  
