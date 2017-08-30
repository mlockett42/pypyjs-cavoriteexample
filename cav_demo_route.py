from __future__ import absolute_import, print_function
import js
from cavorite import c, t, Router

body = js.globals.document.body

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

class Level(c):
    def __init__(self):
        super(Level, self).__init__("p")

    def get_children(self):
        return [t("Level = " + str(self.get_root().url_kwargs['level']))]
        

level = c("div", [Level()])

welcome_page = c("div", [c("p", "Welcome to cavorite"),
                         c("p", [c("a", {"href": "/#!levels/110"}, "Level 110")]),
                         c("p", [c("a", {"href": "/#!levels/119"}, "Level 119")]),
                         c("p", [c("a", {"href": "/cav_demo_mount.html"}, "Mount Demo")]),
                         c("p", [c("a", {"href": "/cav_demo_render.html"}, "Render Demo")]),
                         c("p", [c("a", {"href": "https://github.com/mlockett42/cavorite"}, "Cavorite - Github")]),
                         c("p", [c("a", {"href": "https://github.com/mlockett42/pypyjs-cavoriteexample"}, "pypyjs-cavoriteexample - Github")])
                         ])

error_404_page = c("div", [c("p", "No match 404 error"),
                           c("p", [c("a", {"href": "/#!"}, "Back to main page")])])

r = Router({r'^levels/(?P<level>[0-9]+)$': level,
            r'^$': welcome_page},
            error_404_page, body)
r.route()



        
            
