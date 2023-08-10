from langchain import SQLDatabase
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.schema import SystemMessage

DATABASE = "postgres"
USER = "postgres"
PASSWORD = "pgpassword"
HOST = "localhost"
PORT = "5432"

DATABASE_URL = (
    f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
)

db = SQLDatabase.from_uri(DATABASE_URL)
toolkit = SQLDatabaseToolkit(llm=ChatOpenAI(temperature=0), db=db)

agent_kwargs = {
    "system_message": SystemMessage(content="You are an expert SQL data analyst.")
}

llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
agent = initialize_agent(
    toolkit.get_tools(),
    llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=False,
    agent_kwargs=agent_kwargs,
    return_intermediate_steps=True,
)

while True:
    query = input("Query: ")
    answer = agent({"input": query})
    sql_query = answer["intermediate_steps"][-1][0].log
    print(f"\nAgent log: {sql_query}")
    print(f"\nAnswer: {answer['output']}")
    print("\n\n")