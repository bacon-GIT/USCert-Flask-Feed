import feedparser


# parseAlerts grabs the (entry), extracts all necessary info, dumps the
# rest into "more_details" and returns a list.
def parseAlerts(entry):

    # Parse all vulnerabilities into $feed
    feed = feedparser.parse("https://www.us-cert.gov/ncas/alerts.xml")
    # Sets $feed_entries to the current vulnerability
    feed_entries = feed.entries[entry]

    # Parse elements
    title = feed_entries['title']
    link = feed_entries['link']
    summary = feed_entries['published']

    more_details = feed_entries

    # Return items from list
    vuln_entry = []
    vuln_entry.extend([title, link, summary])
    return vuln_entry
