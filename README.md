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

## Standalone

Parse the latest Cert vulnerabilities into a table. I run this as my MOTD.
Syntax:
Run with no arguments for a default of 5, or use '--entry' argument to specify:

	python3 parse.py --entry 10

Format:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
| TITLE         LINK                                                    DATE PUBLISHED
|
| AA20-266A     | https://us-cert.cisa.gov/ncas/alerts/aa20-266a        | Tue, 22 Sep 2020 15:00:00 +0000
|
| LokiBot Malware
