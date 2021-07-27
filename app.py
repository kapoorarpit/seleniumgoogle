from bs4 import BeautifulSoup
import csv
import requests
import string
import random

def completesearch():
    URL = "https://www.google.com/search?q=restaurants+in+bareilly&rlz=1C5CHFA_enIN915IN917&biw=1366&bih=657&sz=0&tbm=lcl&sxsrf=ALeKk00fQd1Rn4rasvz13BmfqjlCrWtDww%3A1626968288572&ei=4JD5YIG3IpvA3LUPiKSG8AI&oq=restaurants+in+bareilly&gs_l=psy-ab.3...30763.35199.0.35410.21.13.0.0.0.0.0.0..0.0....0...1c.1.64.psy-ab..21.0.0....0.qoXwj1O3fQg#rlfi=hd:;si:17725647855011379645,l,ChdyZXN0YXVyYW50cyBpbiBiYXJlaWxseUjI6f3yx66AgAhaJRAAGAAYAiIXcmVzdGF1cmFudHMgaW4gYmFyZWlsbHkqBAgDEACSARFpbmRpYW5fcmVzdGF1cmFudKoBDBABKggiBGZvb2QoAA,y,RITW0WcMr98;mv:[[28.3934151,79.4460326],[28.3523818,79.41366099999999]]"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"}
    r = requests.get(URL,headers=header )

    soup = BeautifulSoup(r.text, features='html.parser')

    '''name = soup.select('div.dbg0pd', {'class': 'cXedhc.uQ4NLD'})
    for i in name:
        print(i.get_text())'''
    #to get names of hotel<span style="margin-right:5px" class="Aq14fc" aria-hidden="true">4.5</span><div class="Ob2kfd"><div><span style="margin-right:5px" class="Aq14fc" aria-hidden="true">4.5</span><g-review-stars><span class="Fam1ne EBe2gf" aria-label="Rated 4.5 out of 5," role="img"><span style="width:63px"></span></span></g-review-stars><span class="hqzQac" style="white-space:nowrap;font-size:14px;margin-left:5px" data-ved="2ahUKEwjCzoSDjvzxAhVqFLcAHQ6FDQUQiCswAXoECAoQBQ"><span jscontroller="h6wiFf" jsaction="rcuQ6b:npT2md"><a href="#" data-fid="0x39a007568a8178f7:0x8a721884851ba309" data-is_owner="false" data-nohref="1" data-sort_by="qualityScore" data-async-trigger="reviewDialog" role="button" jsaction="FNFY6c" data-ved="2ahUKEwjCzoSDjvzxAhVqFLcAHQ6FDQUQ8mswAXoECAoQBg"><span>70 Google reviews</span></a><span jsaction="lQqO9c:TvD9Pc;vp3PF:MHYjYb"><g-lightbox jsname="KG3hVc" style="display:inline-block" jscontroller="ggQ0Zb" data-df="false" jsshadow="" jsaction="rcuQ6b:npT2md"><div jsname="jt9vfc" aria-hidden="true" role="button" tabindex="0" jsaction="focus:sT2f3e" style="display:none"></div><div jsname="AHe6Kc" class="ynlwjd VDgVie oLLmo u98ib" style="display:none;outline:none;z-index:1000" aria-label="Reviews" role="dialog" tabindex="-1" jsaction="klllfd:hfClUb;QFR3de:vhMcte;pD9K6e:FL9aIe;KbF57e:DlGmce;mLt3mc"><div class="dtCYCd VDgVie" style="z-index:1000" jsaction="yZGKvf" data-ved="2ahUKEwjCzoSDjvzxAhVqFLcAHQ6FDQUQ-UMwAXoECAoQCA"><g-loading-icon jsname="aZ2wEe" class="Xfh32 v5nPIf GuPFE VDgVie" style="display:none;height:30px;min-width:30px"><div class="pSFfp fY2Z0" style="height:30px;width:30px" aria-valuetext="Loading..." role="progressbar"><div class="yiqufc jg5aPd"><div class="r1glSd"><div class="wgim3c jWrfPe unqUac ZvZqlb"></div></div><div class="YvBkFd"><div class="wgim3c jWrfPe m0HFif"></div></div><div class="r1glSd"><div class="wgim3c jWrfPe unqUac tJdqHd"></div></div></div><div class="e3Nvve jg5aPd"><div class="r1glSd"><div class="wgim3c jWrfPe unqUac ZvZqlb"></div></div><div class="YvBkFd"><div class="wgim3c jWrfPe m0HFif"></div></div><div class="r1glSd"><div class="wgim3c jWrfPe unqUac tJdqHd"></div></div></div><div class="kpjGNb jg5aPd"><div class="r1glSd"><div class="wgim3c jWrfPe unqUac ZvZqlb"></div></div><div class="YvBkFd"><div class="wgim3c jWrfPe m0HFif"></div></div><div class="r1glSd"><div class="wgim3c jWrfPe unqUac tJdqHd"></div></div></div><div class="Ft8sDf jg5aPd"><div class="r1glSd"><div class="wgim3c jWrfPe unqUac ZvZqlb"></div></div><div class="YvBkFd"><div class="wgim3c jWrfPe m0HFif"></div></div><div class="r1glSd"><div class="wgim3c jWrfPe unqUac tJdqHd"></div></div></div></div></g-loading-icon></div><div class="Xvesr" style="z-index:1002" aria-label="Close" role="button" tabindex="0" jsaction="yZGKvf" data-ved="2ahUKEwjCzoSDjvzxAhVqFLcAHQ6FDQUQ-EMwAXoECAoQCg"></div><div jsname="Sx9Kwc" class="AU64fe zsYMMe TUOsUe" style="display:none;z-index:1001"><span jsslot=""><div class="VFlF2c review-dialog"></div></span></div></div><div jsname="qngMid" aria-hidden="true" role="button" tabindex="0" jsaction="focus:tuePCd" style="display:none"></div></g-lightbox></span></span></span></div></div>
    ratings = soup.select('span', {'class': 'TLYLSe'})   
    for i in ratings:
        print(i.get_text())


if __name__ == "__main__":
    completesearch()