from __future__ import absolute_import, print_function
import js

jquery = js.globals["$"]

preview_div = jquery(".previewdiv")[0]

preview_div.innerHTML = "<h2>heading 2</h2>"


print ("Hello cav demo")

