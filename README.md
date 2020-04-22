# ~~~~~~~𝔜𝔢 𝔒𝔩𝔢 𝔙𝔲𝔩𝔫𝔢𝔯𝔞𝔟𝔦𝔩𝔦𝔱𝔶 𝔅𝔬𝔞𝔯𝔡~~~~~~~
## A fairly simple to integrate table
for USCert vulnerabilities, something that might be ***very worth it*** to keep up with.

Xmlparse: Main functions here, this is really the only module you need to download. The templates are nice for getting integration ideas, and mainflask.py has the necessary syntax.

-Syntax:

```
 
import xmlparse    # Really need to rename this module
from flask import Flask, render_template
 
@app.route('/')
def table():
    grab = 0
    return render_template("table.html",
                            vuln1=xmlparse.parseAlerts(0),
                            vuln2=xmlparse.parseAlerts(1),
                            vuln3= xmlparse.parseAlerts(2),
                            vuln4= xmlparse.parseAlerts(3),
                            vuln5=xmlparse.parseAlerts(4),
                            vuln6=xmlparse.parseAlerts(5))
```
And that can continue as far as your heart desires.
