import openai

# 初始化 OpenAI API 客户端
openai.api_key = ""
# 定义一个函数生成 ChatGPT 的回复
def generate_response(prompt):
    # 调用 OpenAI API 生成回复
    completions = openai.Completion.create(
        engine="text-davinci-003",  # 指定使用的引擎名称
        prompt=prompt,  # API 请求的提示信息
        max_tokens=1024,  # API 响应的最大令牌数
        n=1,  # API 请求的完成数
        stop=None,  # API 响应的终止标志
        temperature=0.5,  # API 请求的温度参数
    )

    # 从 API 响应中取得回复
    message = completions.choices[0].text
    return message
def ChatGPT_AI_DrawBot(prompt):
        response = openai.Image.create(
          prompt=prompt,
          n=1,
          size="512x512"
        )
        image_url = response['data'][0]['url']
        return image_url

