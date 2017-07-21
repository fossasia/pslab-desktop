#!/usr/bin/python
from virtualapp import app

# Launch on all available interfaces
app.run(debug=True,host='0.0.0.0')
