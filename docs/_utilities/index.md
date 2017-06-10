---
layout: expt
title: "index"
description: "introduction to general purpose utilities goes on this page"
active: utilities
---


## General Purpose utilities



### Code example to acquire a trace from CH1, and plot it
```python
#code snippet example
from PSLab import sciencelab
p=sciencelab.connect()
x,y = p.capture1('CH1',1000,1)

from pylab import *
plot(x,y)
show()
```
