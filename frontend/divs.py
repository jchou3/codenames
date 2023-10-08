import justpy as jp

word_text_classes = "bg-neutral-100"
word_card_classes = "m-2 bg-neutral-100 border-gray-200 rounded border-2 padding-4 w-1/6"

class word_card(jp.Div):

    def __init__(self, **kwargs):
        self.bg_color = "beige"
        self.height = "17%"
        self.width = "18%"
        super().__init__(**kwargs)
        root = self
        button_box = jp.Div(a = root, text = "should be above")
        inp = jp.Input(a=root, classes = word_text_classes, placeholder = "Word")
        

class board(jp.Div):

    def __init__(self, **kwargs):
        self.display = "flex"
        for i in range(25):
            self.add(word_card())


def tester():
    wp = jp.WebPage()
    main_div = jp.Div(a=wp, text="testing a div", classes = "text-red-500 flex")
    inp = jp.Input(a=main_div, placeholder = "testing", )
    inp.div = jp.Div(text="where does this div go", a = main_div)
    return wp


def tester2():
    wp = jp.WebPage()
    word_card(a=wp, classes = word_card_classes)
    return wp

jp.justpy(tester2)
