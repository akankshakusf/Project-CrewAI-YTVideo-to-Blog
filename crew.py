import os
from crewai import Crew  # No need to import `Process`
from agents import blog_researcher, blog_writer
from task import research_task, write_task
import certifi  # Correct import

# Set SSL certificate file path using certifi
os.environ["SSL_CERT_FILE"] = certifi.where()

# Set OpenAI API Key (Assuming it's already set in your environment)
os.environ["CREWAI_DISABLE_TELEMETRY"] = "1"  # Prevent SSL errors

#  Form the tech-focused Crew
crew = Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[research_task, write_task],
    verbose=True,
    process="sequential",  # Use a string instead of `Process.sequential`
    memory=True,
    cache=True,
    share_crew=True
)

# Start execution & print result
result = crew.kickoff()
print(result)
