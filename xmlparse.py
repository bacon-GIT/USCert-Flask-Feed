import feedparser
import time

# parseAlerts grabs the (entry), extracts all necessary info, dumps the
# rest into "more_details" and returns a list.
def parseAlerts(entry):

    # Parse all vulnerabilities into $feed
    feed = feedparser.parse("https://www.us-cert.gov/ncas/alerts.xml")
    # Sets $feed_entries to the current vulnerability
    feed_entries = feed.entries[entry]
    # Extremely useful degugging line:
    #print("Feed Entries: ", feed_entries)

    # Parse elements
    title = feed_entries['title']
    link = feed_entries['link']
    summary_parsed = feed_entries['summary']
    summary = summary_parsed[:72].strip("&")

    # If entry has not been revised
    if ("Summary") in summary:
        summary = summary_parsed[:38]

    # TODO
    more_details = "click me"

    # Return items from list
    vuln_entry = []
    vuln_entry.extend([title, link, summary, more_details])
    return vuln_entry

#parseAlerts(1)
#    title = entry[0]['title']
#    description = entry[0]['title']
