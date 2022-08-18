from chatterbot.logic import LogicAdapter


class MyLogicAdapter(LogicAdapter):

 def __init__(self, chatbot, **kwargs):
    super().__init__(chatbot, **kwargs)

    def can_process(self, statement):

        words = ['what', 'is', 'temperature']
        if all(x in statement.text.split() for x in words):
            return True
        else:
            return False

    def process(self, input_statement, additional_response_selection_parameters):
        from chatterbot.conversation import Statement
        import requests

        # Make a request to the temperature API
        response = requests.get('https://api.temperature.com/current?units=celsius')
        data = response.json()

        # Let's base the confidence value on if the request was successful
        if response.status_code == 200:
            confidence = 1
        else:
            confidence = 0

        temperature = data.get('temperature', 'unavailable')

        response_statement = Statement(text='The current temperature is {}'.format(temperature))

        return confidence, response_statement