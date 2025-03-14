import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.playground import Playground, serve_playground_app
from agno.storage.agent.sqlite import SqliteAgentStorage
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

# Load environment variables from .env
load_dotenv()

# Load storage path from .env or use default
agent_storage = os.getenv("AGENT_STORAGE_PATH", "tmp/agents.db")

web_agent = Agent(
    name="Web Agent",
    model=OpenAIChat(id="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY")),
    tools=[DuckDuckGoTools()] if os.getenv("DUCKDUCKGO_ENABLED") == "True" else [],
    instructions=["Always include sources"],
    storage=SqliteAgentStorage(table_name="web_agent", db_file=agent_storage),
    add_datetime_to_instructions=True,
    add_history_to_messages=True,
    num_history_responses=5,
    markdown=True,
)

agent = Agent(
    name="Agent",
    model=OpenAIChat(id="gpt-4o", api_key=os.getenv("OPENAI_API_KEY")),
    storage=SqliteAgentStorage(table_name="finance_agent", db_file=agent_storage),
    add_datetime_to_instructions=True,
    add_history_to_messages=True,
    num_history_responses=5,
    markdown=True,
)

app = Playground(agents=[web_agent, agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", host="0.0.0.0", port=7777, reload=True)

