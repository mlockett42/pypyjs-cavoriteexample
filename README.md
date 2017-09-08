# pypyjs-cavoriteexample
This provides an example for how to use cavorite with pypyjs

### How cavorite works

The DOM is represented as a tree of VNode and TextNode objects. Each VNode object represents
a DOM Element and a TextNode represents a fragement of text inside a HTML element. Usually we
use a shorthand name, c is the VNode class, t is the TextNode class.

There are three ways of outputing the tree to the real DOM so the user can see our webpage - render,
mount and route.

Render is the simplest. In the example we just use VNode objects to build a static webpage with a small
javascript function which prints to the console. We can just pass the tag name, attributes and list of
child nodes to the constructor of the VNode class.

Mount is next most complex. The example takes advantage of the fact that we can subclass the VNode class
and dynamically generate new vnodes. Whenever we change the underlying data we call the
mount_redraw() method, which generates a new virtual DOM and renders those parts that have changed.
Because these are all implemented as python classes our data can be represented in any form we like
in this case a global list of strings.

Router - The router looks at the url and matches via a regex against which VNode to display. When the
URL changes it clears out the old document body and attaches a new old. Since this doesn't actually
reload the browser start can be stored in the browser memory.

Cavorite uses a virtual dom mainly to guard against garbage collection issues in pypyjs but to also
improve performance (parts of the DOM know to have not changed aren't redrawn)


## How to install and run locally

These instructions have only been tested on linux.

Both the cavorite library and the pypyjs demo repo need to be in the same directory. This can be your 
home directory or any directory.

`git clone https://github.com/mlockett42/cavorite.git`

`git clone https://github.com/mlockett42/pypyjs-cavoriteexample.git`

`git submodule update --init --recursive`

This will checkout pypyjs

`cd pypyjs-release`

`python ./tools/module_bundler.py add ./lib/modules ../../cavorite/cavorite`

This will make cavorite available as a pypyjs package.

`cd ..`

`python simple_http_server.py`

Open a web browser and go to http://127.0.0.1:8000.

## How to install and run on the internet

Since this demo doesn't have a backend you can just upload the files and serve them statically. That's
what cavorite.io does. (As long as you have completed the module_bundler step above you will have completed
the relevant steps). Just upload the entire pypyjs-cavoriteexample directory and serve it up.

## Licence
Copyright Mark Lockett 2017 Apache 2.0 Licence

