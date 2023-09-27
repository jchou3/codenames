import justpy as jp

word_text_classes = "bg-neutral-100"

class word_card(jp.Div):

    def __init__(self, **kwargs):
        self.bg_color = "beige"
        self.word = jp.Input(classes = word_text_classes placeholder = "Word")
        self.height = "17%"
        self.width = "18%"


    def react(self, data):
        pass

class board(jp.Div):

    def __init__(self, **kwargs):
        self.display = "flex"
        for i in range(25):
            self.add(word_card())