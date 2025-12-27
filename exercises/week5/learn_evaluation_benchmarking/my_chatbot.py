from openai import responses

from conversation_manager import ConversationManager
import ollama

model="llama3.1:latest"
user_response = input("You: ")
manager = ConversationManager(model_name=model, max_messages=6)
while "stop" != user_response:
    manager.add_message('user', user_response)
    print(manager.get_history())
    response = ollama.chat(model=model, stream=False, messages=manager.get_history())
    assistant_msg=response.message.content
    manager.add_message("assistant",assistant_msg)
    print(f"Assistant: {assistant_msg}")
    print(manager.get_history())
    user_response=input("You: ")

# print(len(manager.get_history()))
# manager.add_message('user', 'Hi2')
# print(len(manager.get_history()))
# manager.add_message('user', 'Hi3')
# print(len(manager.get_history()))
# manager.add_message('user', 'Hi4')
# print(len(manager.get_history()))
# manager.add_message('user', 'Hi5')
# print(len(manager.get_history()))
# manager.add_message('user', 'Hi6')
# print(len(manager.get_history()))
# manager.add_message('user', 'Hi7')
# print(len(manager.get_history()))
# manager.add_message('user', 'Hi8')
# print(len(manager.get_history()))
# manager.add_message('user', 'Hi9')
# print(len(manager.get_history()))
# manager.add_message('user', 'Hi10')
# print(len(manager.get_history()))
# print(manager.get_history())


