class ConversationManager:

    def __init__(self, model_name:str, max_messages:int):
        self.model_name=model_name
        self.max_messages=max_messages
        self.messages=[{"role":"system", "content":"You are Financial Fraud investigation expert"}]

    def add_message(self, role, content):
        # Add to history
        new_content = {"role":role,
                       "content":content}
        if self.truncate_if_needed():
            self.messages.pop(1)
        self.messages.append(new_content)

    def get_history(self):
        # Return messages for API
        return self.messages

    def chat(self, user_message):
        # Handle full conversation turn
        self.add_message(role="user", content=user_message)

    def truncate_if_needed(self)->bool:
        # Apply sliding window
        curr_msg_count = len(self.messages)
        return curr_msg_count>=self.max_messages

