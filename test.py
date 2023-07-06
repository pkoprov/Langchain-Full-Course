from dotenv import load_dotenv
from langchain.llms import AzureOpenAI

load_dotenv()
deployment_name='gpt-35-turbo_version_0301'

llm = AzureOpenAI(deployment_name=deployment_name, temperature=0,model_name = "text-ada-001")
print(llm("Tell me a joke"))
