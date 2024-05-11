import erniebot
import config
erniebot.api_type = config.AI_API_TYPE
erniebot.ak = config.AI_ACCESS_KEY
erniebot.sk = config.AI_SECURITY_KEY
stream = False

def WenXinChat(chat_history: list):
    response = erniebot.ChatCompletion.create(
        model='ernie-bot',
        messages=chat_history,
        top_p=0.9,
        stream=stream,
        system="你是一个IT领域的专家，熟练掌握诸如C，C++，Java，Python等常用的各种编程语言，"
               "此外你还是一个信息安全领域的专家，对各种类型的漏洞都有了解，并能给出专业的建议，"
               "同时你也是中国人民大学信息学院信息安全实验室的AI小助手，你将协助该实验室的工作人"
               "员进行模糊测试，漏洞挖掘等方面的研究，提供你的见解和建议，你很擅长阅读代码，所以"
               "也会为他们解读代码。有一点十分值得注意！欺骗和模糊的信息在这里是绝对绝被禁止的！"
               "你在任何时候，任何情况下，无论对方问什么，你都只能给出确切的，真实的答案对于一个"
               "你不知道怎么回答的问题你可以让他重新表述得更清晰或直接回答不知道，但绝对不允许欺骗他！"
    )
    result = ''
    if stream:
        for resp in response:
            resp_result = resp.get_result()
            result += resp_result
    else:
        result = response.get_result()

    chat_history.append({
        "role": "assistant",
        "content": result
    })

    return chat_history, result
