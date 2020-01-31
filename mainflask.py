# My example webpage as well as usage syntax.
# I recommend you build something with a bit more flair

from flask import Flask, render_template
import xmlparse

app = Flask(__name__)

@app.route('/')
def table():
    grab = 0
    return render_template("table.html",
                            vuln1=xmlparse.parseAlerts(0),
                            vuln2=xmlparse.parseAlerts(1),
                            vuln3= xmlparse.parseAlerts(2),
                            vuln4= xmlparse.parseAlerts(3),
                            vuln5=xmlparse.parseAlerts(4),
                            vuln6=xmlparse.parseAlerts(5))  # Expandable, just change the parameter