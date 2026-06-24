from crewai import Agent, Task, Crew, Process

# ==========================================
# 1. הגדרת הסוכנים (Agents)
# ==========================================

researcher = Agent(
    role="Market Researcher",
    goal="Find accurate, up-to-date technical specifications and consumer trends for the given home equipment product.",
    backstory="You are a meticulous research analyst. You extract key facts, features, and benefits of home products.",
    verbose=True
)

writer = Agent(
    role="Content Writer",
    goal="Transform research notes into a clear, engaging, and professional product article.",
    backstory="You are a technical writer who turns raw research into well-structured, reader-friendly articles for an e-commerce website. You write in plain language with a logical flow.",
    verbose=True
)

seo_specialist = Agent(
    role="SEO Specialist",
    goal="Create highly optimized Title Tags and Meta Descriptions based on the product article.",
    backstory="You are an expert in digital marketing and search engine optimization. You know exactly how to craft metadata that drives clicks and ranks high on Google.",
    verbose=True
)

reviewer = Agent(
    role="Quality Reviewer",
    goal="Review the final article and SEO metadata for accuracy, clarity, and brand consistency.",
    backstory="You are a senior editor who checks facts, improves readability, and returns a polished final version. You never change the core meaning, only improve quality.",
    verbose=True
)

# ==========================================
# 2. הגדרת המשימות (Tasks)
# ==========================================

research_task = Task(
    description="Search and collect key features, technical specs, and target audience needs for the product: {product_name}. Produce a structured summary.",
    expected_output="A structured research summary with facts and specs about the product.",
    agent=researcher
)

writing_task = Task(
    description="Using the research provided, write a 300-word engaging product description article. Keep the tone professional but accessible.",
    expected_output="A complete 300-word product article in Markdown format.",
    agent=writer
)

seo_task = Task(
    description="Based on the written article, generate one compelling SEO Title Tag (up to 60 characters) and one Meta Description (up to 155 characters).",
    expected_output="SEO Title Tag and Meta Description ready for website publication.",
    agent=seo_specialist
)

review_task = Task(
    description="Review the article and the SEO metadata. Ensure there are no factual errors, grammar mistakes, and that the structure flows logically.",
    expected_output="A polished, publication-ready article along with its SEO metadata.",
    agent=reviewer
)

# ==========================================
# 3. הרכבת הצוות והפעלה (Crew & Kickoff)
# ==========================================

crew = Crew(
    agents=[researcher, writer, seo_specialist, reviewer],
    tasks=[research_task, writing_task, seo_task, review_task],
    process=Process.sequential, 
    verbose=True
)

# הפעלת השרשרת עם מוצר לדוגמה של MG4HOME
result = crew.kickoff(inputs={"product_name": "Smart Home Robot Vacuum Cleaner with Mop"})

print("######################")
print("FINAL RESULT:")
print("######################")
print(result)
