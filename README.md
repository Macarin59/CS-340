# CS-340
**How do you write programs that are maintainable, readable, and adaptable? Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future?**

Writing well documented, modular programs is the best way to ensure that your programs remain maintainable, readable, and adapatable. Creating a CRUD python file allows for the AnimalShelter class to be reused throughout multiple programs and applications. If a need ever arises to parse the AnimalShelter data again, the CRUD module could easily be reused.
With some slight modifications the crud.py file could also be refactored into a more modular program that allows the parsing of any MongoDB database with the right parameters given. 

**How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?**

The best way to approach a problem as a computer scientist is to break down the requirements into actionable segments and then determine the best way to tackle each segment. This project differed from previous assignments because of the usage of a query language (MongoDB) which requires a slightly different skillset than the standard program. 
The most important thing to keep in mind when working with databases is security. The last thing you want is to wipe data from the database due to human error. I think keeping the code modular and segmented is the best strategy for future database work. 

**What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?**

Computer scientists write code to allow for a faster and more interconnected world. Programs can help all professions increase their productivity and impact. In the case of Grazioso Salvare, this web application allows them to cutdown on the time it takes to find suitable search-and-rescue candidates, which in turn allows them to train and deploy candidates
faster for the greater good. 
