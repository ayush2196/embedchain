import os
from embedchain import App

os.environ["OPENAI_API_KEY"] = "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"

bot = App()
bot.add("web_page", "https://jobs.zalando.com/en/jobs/2710432?gh_src=2104be071")
bot.add("pdf_file", "Ayush's Resume-Data_Engineer.pdf")

answer = bot.query("what changes should I make in my resume to get shortlisted for the job in the web page provided")
print(answer)