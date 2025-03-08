import os
from dotenv import load_dotenv
from crewai import Agent, LLM
from tools import yt_tool  # Ensure yt_tool is defined

# Disable telemetry
os.environ["CREWAI_DISABLE_TELEMETRY"] = "1"

# Load environment variables
load_dotenv()

# Ensure OpenAI API key is set
openai_api_key = os.getenv("OPENAI_API_KEY")
#if not openai_api_key:
    #raise ValueError("OpenAI API key is missing. Please set it in the .env file.")

# Define LLM model
llm = LLM(
    model="gpt-3.5-turbo",  # Use a valid model name
    api_key=openai_api_key
)

# Blog Researcher Agent
blog_researcher = Agent(
    role="Blog Researcher from YouTube Videos",
    goal="Get relevant video content for the topic: {topic} from YouTube.",
    verbose=True,
    memory=True,
    backstory="Expert in AI, ML, and GenAI video analysis, extracting insights from YouTube videos.",
    tools=[yt_tool],  # Ensure yt_tool is defined
    allow_delegation=True,
    llm=llm,  # Assign the LLM
)

# Blog Writer Agent
blog_writer = Agent(
    role="Blog Writer",
    goal="Write engaging blog content based on YouTube videos for topic: {topic}.",
    verbose=True,
    memory=True,
    backstory="An expert in simplifying AI/ML concepts into readable blog posts.",
    tools=[yt_tool],
    allow_delegation=False,
    llm=llm,  # Assign the LLM
)