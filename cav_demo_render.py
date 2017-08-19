from __future__ import absolute_import, print_function
import js
from cavorite import c

jquery = js.globals["$"]

preview_div = jquery(".previewdiv")[0]

class Printer(object):
    def __init__(self, message):
        self.message = message
    def print_it(self, e):
        print(self.message)

p = Printer("Hello me!!!")

content = c("div", [c("h1", "Cavorite Test"),
                    c("p", "It works"),
                    c("a", {"href": "https://www.google.com"}, "Google"),
                    c("button", {"onclick": p.print_it}, "Press me")])

content.render(preview_div)



        
            
