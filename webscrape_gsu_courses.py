from lxml import html
import requests
from twilio.rest import Client

if __name__ == '__main__':
    page = requests.get('https://www.gosolar.gsu.edu/bprod/bwckschd.p_disp_listcrse?term_in=201708&subj_in=CSC&crse_in=8320&crn_in=91281')
    tree = html.fromstring(page.content)

    d = tree.xpath('//td/text()')

    # the following line needs your Twilio Account SID and Auth Token
    client = Client("", "")

    if d[23] == '0' :
        print("no seats yet !")
    else:
        client.messages.create(from_="+16783832849",
                               to="+14457849900", #myphonenumber
                               body="seats just became available; sign up for ad-os now!")
