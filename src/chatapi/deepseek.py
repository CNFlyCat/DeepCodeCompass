from openai import OpenAI

client = OpenAI(api_key="sk-53c597552b4049fbafcfeee6ed09ae4f", base_url="https://api.deepseek.com")

# client = OpenAI(api_key="Cat.2597758#", base_url="https://xrocketcat-rocket-gemini.hf.space/hf/v1")

models_response = client.models.list()  # 获取模型列表
for model in models_response.data:
    print(model.id)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "你好"},
    ],
    stream=False
)

print(response.choices[0].message.content)
