# text-2-sql
Converting text to SQL using Langchain + GPT 3.5

## Description
The demo demonstrates the process of interacting with an SQL table using text.   
It begins by receiving a user's question. Then, a SQL Agent provided by Langchain utilizes an LLM (GPT-3.5) to convert the text into a SQL query.  
This SQL query is then executed to retrieve the necessary information from the database.  
The retrieved information serves as context for delivering an appropriate answer to the user.

## Considerations 
### Database
The db is a Postgres SQL db running over a docker container.  
To enable the db run the below command.  

    $docker-compose up

### Install packages
Install the packages with the below command.  

    $pip install -r requirements.txt

### Dataset
The dataset is a public dataset provided by hugging-face.  
Run the jupyter notebook *dataset.ipynb* in order to load and process the dataset. At the end of the notebook the dataset will be saved into the db.  

### SQL Agent
Langchain provides a SQL Agent that deal with the understanding of the user's query and with the conversion of the to user's query to SQL query.  
Run the jupyter notebook *text-2-sql.ipynb* in order to enable the SQL Agent and testing it.   
Set up the OPENAI Token before running the jupyter notebook.  

    %env OPENAI_API_KEY=<OPENAI TOKEN>

## Testing
If you want to play around a script. Set up the OPENAI Token as environment variable.

    $export OPENAI_API_KEY=<OPENAI TOKEN>

Run the command  

    $python3 cli.py


https://github.com/jamesev15/text-2-sql/assets/84110446/2302281c-4e96-4b4f-b519-b50de266a9f0



