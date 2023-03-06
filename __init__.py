from mycroft import MycroftSkill, intent_file_handler


class Happy(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('happy.intent')
    def handle_happy(self, message):
        self.speak_dialog('happy')


def create_skill():
    return Happy()

