### Connection Pooling Setup

#### Azure

First, I went on the Azure website to create a VM instance. I made sure to choose all the necessary selections that were brought up in class, such as choosing East coast region, Standard_B1ms, SSH public key, and HTTP + HTTPS + SSH inbound ports in order to set up a cost-effect Azure Database MySQL Server (flexible server selection). Also, set to Start IP Address 0.0.0.0 to End IP Address 255.255.255.255 *Note*- To configure connection pooling for the Azure databases, you can set the parameters in the python script:

**import mysql.connector 
from my sql.connector import pooling**

Then, proceed to set to set the parameters 'max_connections' and 'connect_timeout'

#### GCP

First, I navigated to console.cloud.google.com. Here, I set up a new VM instance, focusing on the east coast, sandbox, storage, and enterprise selections. Here we start at 0.0.0.0/0 for the IP address. After obtaining the most cost effective solution for this VM instance, we can move on to the next step. 

### Database Schema and Data

I utilized the "bonnie" database because I created this for both Azure and GCP. I based the table on what was used in the class demo. My fields were patient and treatment related and it was simple to establish a foreign key relationship. For example, the patients table had patient ids,first and last names, date of births, gender and contact number fields which had an established relationship to the medical_records table consisting of patient ids, ids, diagnosis, treatment, and admission and discharge dates. Id remained as the primary key for both. **The data schema specifies these tables, the columns, relationships and constraints amongst other elements while enforcing data integrity through these components. By having a data schema, the database can be easily modified and easily scalable.** 

*Error: I faced an "access denied for user---" error when I tried to run the inspector lines of my code.(Pic is uploaded to Errors folder as "db_schema Error") I then realized that it was because I was only running part of the code without running the sequence **below** and I also modified it to include "from sqlalchemy.engine.reflection import Inspector"* 

from sqlalchemy import create_engine, inspect, Column, Integer, String, Date, ForeignKey
from sqlalchemy.engine.reflection import Inspector
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

### MySQL Workbench and ERD Generation

After inputting information for the azure.py and gcp.py with mysql connection info, and successfully running the code, I made the connection to MySQL Workbench for both and generated an ERD which looks the same for both. This is due to the same tables utilized for both. ERD is uploaded in the ERD folder. The ERD depicts the relationships between the tables. 

### SQLAlchemy and Flask Integration

I based the app.py template off the python connection template uploaded in the class files, modifiying to adjust my tables, commands, and endpoints. The endpoints and base.html/data.html files were based off the template from the Week 1 homework. These code was also modifed to my tables, title and webpage names. The base.html and data.html are located under the templates folder. Also, I put my env. in my gitignore for security purposes. 

*Error: Here, I only successfuly connected my Flask app to my GCP MySQL database. I could not connect to Azure. I kept on running into the error of 'Connections using insecure transport are prohibited'. I did double check to include my connection string with "connect_args={'ssl': {'ssl-mode': 'preferred'". I also double check on my Azure server's firewall rules and everything looked okay. I'm not sure what the issue was as my env. file was also hosting correct information.*

### Database Migrations with Alembic

I followed the instructions at the bottom of the template code used in the class demo:

Performed in terminal:

1. alembic init migrations
` alembic init migrations `

2. edit alembic.ini to point to your database
` sqlalchemy.url = mysql+mysqlconnector://username:password@host/database_name `

3. edit env.py to point to your models
`from db_schema import Base`
`target_metadata = Base.metadata `

4. create a migration
` alembic revision --autogenerate -m "create tables" `

5. run the migration
` alembic upgrade head `

in addition, you can run ` alembic history ` to see the history of migrations
or you can run with the --sql flag to see the raw SQL that will be executed

so it could be like:
` alembic upgrade head --sql `

or if you then want to save it:
` alembic upgrade head --sql > migration.sql `

6. check the database

Many files popped up when I proceeded with these steps. I also faced an error when creating tables. But, I resolved it by adding the "#" in the env.py file to be "#target_metadata = None". This worked! Then, I modified my table to include a column of "is_deceased", "is_deceased = Column(String(30), nullable=False)". This is shown in my gcp.py file.
