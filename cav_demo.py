from __future__ import absolute_import, print_function
import js
from cavorite import c

jquery = js.globals["$"]

preview_div = jquery(".previewdiv")[0]

content = c("div", [c("h1", "Cavorite Test"), c("p", "It works"), c("a", {"href": "https://www.google.com"}, "Google")])

content.render(preview_div)



        
            
