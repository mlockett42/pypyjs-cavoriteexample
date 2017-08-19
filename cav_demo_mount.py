from __future__ import absolute_import, print_function
import js
from cavorite import c

jquery = js.globals["$"]

preview_div = jquery(".previewdiv")[0]

data = ["1", "2"]

class ListItem(c):
    def __init__(self, parent, value):
        super(ListItem, self).__init__("p", [c("button", {"onclick": self.handle_click}, str(value))])
        self.value = value
        self.parent = parent

    def handle_click(self, e):
        global data
        data.remove(self.value)
        r = self.get_root()
        r.mount_redraw()

class ListDisplayer(c):
    def __init__(self):
        super(ListDisplayer, self).__init__("div")

    def get_children(self):
        global data
        ret = [ListItem(self, v) for v in data]
        return ret

def add_new(e):
    global data
    data.append(str(len(data) + 1))
    global content
    content.mount_redraw()

content = c("div", [c("h1", "Cavorite Mount Test"),
                    c("button", {"onclick": add_new}, "Press me"),
                    ListDisplayer()])

content.mount(preview_div)



        
            
