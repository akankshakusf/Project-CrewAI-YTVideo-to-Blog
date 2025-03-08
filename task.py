from crewai import Task
from tools import yt_tool
from agents import blog_researcher, blog_writer

# Define the topic for a single YouTube video
topic = "AI VS ML VS DL VS Data Science"

# Task 1: Research Task
research_task = Task(
    description=(
        f"Identify the video: {topic}.\n"
        f"Get detailed information about the video from the channel."
    ),
    expected_output=f"A comprehensive 3-paragraph report based on the video content for {topic}.",
    tool_kwargs={"search_query": topic},  # Ensure yt_tool is correctly imported
    agent=blog_researcher,
)

# Task 2: Writing Task
write_task = Task(
    description=f"Extract and summarize information from the YouTube video on the topic: {topic}.",
    expected_output=f"Summarize the YouTube video for {topic} and generate a blog post.",
    tool_kwargs={"search_query": topic},
    agent=blog_writer,
    async_execution=True,  # Runs in parallel with research_task
    output_file="new-blog-post.md"  # Saves output to a file
)
