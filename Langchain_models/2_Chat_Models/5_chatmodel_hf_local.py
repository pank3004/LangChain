from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
#import os

#os.environ['HF_HOME'] = 'D:/huggingface_cache'

llm = HuggingFacePipeline.from_model_id(
    model_id='Qwen/Qwen1.5-1.8B-Chat',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)
model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of France")

print(result.content)