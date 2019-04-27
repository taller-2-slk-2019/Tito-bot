class ConversationRequest:

    def __init__(self, data):
        self.bot_name = data['bot']
        self.conversation_id = data['conversationId']
        self.user_id = data['userId']
