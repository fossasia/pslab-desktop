## Configuration details for Jekyll based help files

+ Generated HTML files are stored in MD_HTML
+ helpfiles for general purpose utilities such as data loggers, scope, voltmeters etc are located in _utilities
+ application specific files are located in _apps/

When the user selects an experiment from the desktop app, the relevant helpfile is automatically displayed in a built-in browser

### testing the build locally

Jekyll can be used to host a temporary web server via the command `jekyll serve`.

Navigate to `localhost:4000` in the web browser to access the generated html 


### TODO

Use YayDoc to generate static HTML instead of Jekyll

