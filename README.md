### Connection Pooling Setup

#### Azure

First, I went on the Azure website to create a VM instance. I made sure to choose all the necessary selections that were brought up in class, such as choosing East coast region, Standard_B1ms, SSH public key, and HTTP + HTTPS + SSH inbound ports in order to set up a cost-effect Azure Database MySQL Server (flexible server selection). *Note*- To configure connection pooling for the Azure databases, you can set the parameters in the python script:

**import mysql.connector 
from my sql.connector import pooling**

Then, proceed to set to 20 max_connections and connect_timeout.

. I also documented my username and password for this instance. Also, I went back in to modify/add the sql 3306 port. I later used the IP address to connect to MySQL Workbench and it was successful. To do so, on shell, we had to use several commands to create a user along with the password, adjust the bind-address, and installing mysqul-server + mysql-client. Logging in, we used the sudo mysql command. Setting up the VM instance was not difficult but configuring on shell took some time.

### The rationale behind my database schema

I utilized the bonnie database because it was what I had previously created/used. My fields were patient and demographic related and it was simple to establish a foreign key relationship. For example, my demographics table had demographic ids, patient ids, first names, and address which had an established relationship to the patients table consisting of patient_id and MRN.

### Steps/Challenges/Errors + Troubleshooting

I faced many errors in the assignment, some of which were resolved and some were not. First, I could not login with my password to my VM. Then I realized the admin name was case-sensitive and then I was able to log in after multiple permission denials. Then, I encountered an unsuccessful MySQL connection after sucessfully connecting a few minutes prior. To resolve this, I deleted the connection on MySQL workbench and reconnected. This helped me successfully connect again. Lastly, I kept on encountering a "Can't connect to MySQL server on 'None' (Errno-2) when I tried to run my flask app. I thought this was an env. file error-maybe I didn't enter the correct credentials or maybe there was a 'None' text throughout my code that I hadn't replace with the substantial info. But, I tried to resolve it these ways and I couldn't fix it. I have attached all screenshot images in the 'errors' folder
