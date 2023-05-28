from datetime import datetime
from typing import Optional, List

from fastapi import requests
from pydantic import BaseModel


# from BMU.bmupro import bmu, shd, ghl, egb, btg

class trans(BaseModel):
    id: Optional[int] = None
    email: Optional[List[int]] = None
    password: Optional[str] = None
    password_again: Optional[str] = None
    login: Optional[List[str]] = None
    signup: Optional[List[str]] = None
    amount: Optional[float] = None
    annual: Optional[float] = None
    daily: Optional[float] = None
    depositor: Optional[List[str or id]] = None
    name: Optional[str] = None
    acc_no: Optional[List[str and int]] = None
    phone_no: Optional[str] = None
    salary_amount: Optional[float]


class acc(BaseModel):
    id: Optional[List[str]] = None
    Acc_name: Optional[str] = None
    current_balance: Optional[float or str] = None
    Acc_no: Optional[List[str]] = None
    Session: Optional[List[str]] = None


class giver(BaseModel):
    giver: Optional[str] = None


# mas monthly alert salaries
class Text:
    def __init__(self):
        from starlette.responses import HTMLResponse
        self.usr_log = trans(login=['\n Enter email: ', '\n Password: '])
        self.usr_sgn = trans(signup=['\n Enter email: ', '\n Password: ', '\n Password again: '])
        self.user = [self.usr_log and self.usr_sgn]
        self.bmu = {('\n bmu', '0.1.0'): HTMLResponse("""<html>
                                        <head>
                                        <title></title></head>
                                        <body>
                                        <pre>
                                        <em>
                                        <ul>
                                        <li>
                                        <a href="server"><img src="https://bwroline.com/images/bwrolineImageSapi.com/bwroline.com/api/staticimage?size=70*30&makers=b.jpg" alt="server image"></img></a>
                                        <font face="pyramid" color="blue">
                                        <p align="center">Abuja Gbagyi Media <br>F. C. T - Abuja<br>Since July 2018</font><br>Be and remain 
                                        in touch with the things you've been missing out! Get all the interesting Dramas and Movies 
                                        or videos you've desired to watch, that you can get in touch with the Gbagyi entertainment's 
                                        trends like the    <em><a href="shamudoents.com">shamudoents entertainments</a></em>    
                                        across the globe likewise other trends... We make sure you are connected and remain 
                                        connected with God and to be entertained by our religious traditions    <em><a 
                                        href="ecwagoodnewsbwr.com.com">ecwagoodnewsbwr.com</a></em>    Download also your best and 
                                        latest Musics available here <em><a href="btgees.com">btgees</a></em>    You can get 
                                        reach a legal practitioner for services    <em><a href="ghlp.com">great 
                                        hussein legal practitioners</a></em><br></a></p></pre></body></html>""",
                                                      status_code=200)}
        self.shd = {('\n shd', '0.1.1'): HTMLResponse("""<!DOCTYPE html>
                <html lang="en" dir="ltr">
                <head>
                <meta charset="utf-8">
                    <title><a href="server">BWAYA MEDIA UNIT</a></title>
                </head>
                    <body>
                <br>
                <img src="https://images.apis.com/bwroline.com/shamudoents/images/api/staticimage?size=70*30&makers=sh.jpg" alt="shamudoent shd image"/>
                    <br><font size="2 pt"><i>click img to go home</i></font><br>
                <h1 align="center"><b> SHAMUDOENTS BWARI ENTERTAINMENTS</b></h1>
                <p align= "center"><font color="red" size="4.5pt">
                    Plot 2. Tudun Wada,<br>
                    Behind Sky Bank.<br>
                    Bwari - Abuja<br></font>
                    <hr>
                    <p align= "center">
                    <font size="5pt">
                    SHAMUDOENTS BWARI ENTERTAINMENTS
                    PRESENTS<br>
                    <img src=""https://images.apis.com/bwroline.com/shamudoents/images/api/staticimage?size=70*30&makers=sh3.jpg" ></img><img src=""https://images.apis.com/bwroline.com/shamudoents/images/api/staticimage?size=70*30&makers=sh1.jpg"></img><img src=""https://images.apis.com/bwroline.com/shamudoents/images/api/staticimage?size=70*30&makers=bpics\sh2.jpg"></img><br>
                    Its a part of a great unique intent over and beyond social creativity in to this industry and the webpage coming into existence for the purpose of it services...<br>
                    This is a social entertainment industry with the objective as to;<br>
                    Motivating to explore the youth of young generation on attaining and impart greater heights in the future<br>
                    Making leaders of tomorrow by equipping the children as we annually organise Spelling Bee also other relevant competition.<br>
                    We do also;<br>
                    < -MC/Wedding coverage-><br>
                    < -----Film production----><br>
                    < ------Photo book------><br>
                    < -----Movie editing-----><br>
                    Mind you! Do well to drop a comment by... Regularly visit us to know more on what you've desired to know or make inquiry about.
                    Reach us on contact@:<br>
                    +2348171430080,
                    +2347036818769
                    shamudoent@hotmail.com
                    shamudoents@gmail.com<br>
                </font>
                    </p>
                </body>
                </html>""", status_code=200)},
        self.ghlp = {('\n ghlp', '0.1.2'): HTMLResponse("""<!DOCTYPE html>
                <html lang="en" dir="ltr">
                    <head>
                <meta charset="utf-8">
                    <title><a href="server">BWAYA MEDIA UNIT</a></title>
                </head>
                    <body>
                <br><img src="https://images.apis.com/bwroline.com/ghlp/images/api/staticimage?size=70*30&makers=9ja.jpg" 
                alt="ghlp 9ja images"></img><font size="5pt"><h1 align="center">GREAT HUSSEIN LEGAL 
                PRACTITIONERS</h1></font><img src="https://images.apis.com/bwroline.com/ghlp/images/api/staticimage
                ?size=70*30&makers=bgl1.jpg" alt="ghlp bgl1 image"></img><p align="center"><font size="5pt" 
                color="brown">No. 4, Jibowu Close Off Ozulua Road<br>University Of Lagos Akoka<br>Yaba, 
                Lagos</br></font><hr><p align="center"><img 
                src="https://images.apis.com/bwroline.com/ghlp/images/api/staticimage?size=70*30&makers=bgl.jpg" 
                width="200" height="70"></img><img 
                src="https://images.apis.com/bwroline.com/ghlp/images/api/staticimage?size=70*30&makers=bgl1.jpg" 
                width="200" height="70"></img><br><font size="6pt" color="saphire"><p align="center">Greats Wild 
                Legal Practitioners<font color="blue" size= "6pt">Yusuf Hussein, Esq <br>Principal Counsel 
                <br>Great-Hussein Legal Practitioners <br></br></font><hr><font color="golden-gold" size= "6pt"><p 
                align="center">You are Welcome!<br>Here you shall find all the services for legal living in any part 
                all over the world<br></font><hr><p align="center"><font color="orange" size= "6pt">List of Our 
                Services are:<br></b></font><font face="Sofadione">Legal Case Handle<br>Legal Law Enforcing<br>Legal 
                Housing Agent<br>And other Federation Legal obligations</font><p align="center"><br><font size= "6pt" color="saphire">We practice Justice and Loyalty!</font><br><font size= "6pt" color="green">Legal Greats Legal Practitioners The Desired Place For Hope</font><hr></br><p align="center"><font size="6pt">Tel:08033514288, 08023941762, 01-9521070</br>E-mail:greathusseinlegal@yahoo.com</font><br></br><br></body></html>""",
                                                        status_code=200)},
        self.egb = {('\n egb', '0.1.3'): HTMLResponse("""<!DOCTYPE HTML>
                        <html lang="en" dir="ltr">
                            <head>
                        <meta charset="utf-8">
                            <title><a href="server">BWAYA MEDIA UNIT</a></title>
                        </head>
                            <body>
                        <br>
                        <img src="https://images.apis.com/bwroline.com/ecwagoodnews.com/images/api/staticimage?size=70*30&makers=e.jpg", alt="ECWA LOGO"></img>
                        </h1>
                        <br>
                        <h1 align="center">
                        <font color="blue">
                        ECWA GOOD NEWS CHURCH
                        </font><br>
                        <font size="6pt" color="red">
                        P. O. Box 95, Bwari Abuja
                        </font>
                        </h1>
                        <p align="left">
                        <font color="red" size="5pt">
                        2021 ECWA THEME:
                        </font>
                        </p>
                        <p align="--Ceremonial">
                            <font color="orange" size="6pt">  "Look, He is coming with the clouds..."</font>
                        </p>
                        <P align="right">
                            <font size= "5pt" color="red">Revelation 1:7</font>
                        </p>
                        <br>
                        <img src="https://images.apis.com/bwroline.com/ghlp/images/api/staticimage?size=70*30&makers=e1.jpg", alt="entrance view"></img>
                        <img src="https://images.apis.com/bwroline.com/ghlp/images/api/staticimage?size=70*30&makers=e5.jpg", alt="puppet"></img>
                        <img src="https://images.apis.com/bwroline.com/ghlp/images/api/staticimage?size=70*30&makers=e3.jpg", alt="pictorial side view"></img><br>
                        For daily Sunday sermons, click <a href="sundaysSermons">Sunday sermons</a> to keep updated if in case you are/feel outdated.<br>
                        <hr>
                        Click on <a href="pfftw">Prayer focus for the week</a> to keep connected to the Spirit leadership
                        <hr>
                        <font size="6pt">
                        <p align="center">
                        OUR VISION
                        <br>
                        To be a dynamic Global Church, thoroughly using the scriptures for equipping God's people for every good work (2 Timothy 3:17)<br>
                        <hr>
                        <p align="center">
                        OUR MISSION<br>
                        To Glorify God passionately meeting man's total needs through the Gospel of Jesus Christ
                        <hr><br>
                        <font face="parl" color="green" size="6pt">Watch Word</font>
                        <br>
                        "...And this is the secret: Christ lives in you. This gives you assurance of sharing his glory."
                        <br>Col 1:27 NLT.
                        <br>
                        Church Secretary<br>ELD. BAKO DAVID <br></br>
                        Service Secretary<br>ELD. VICTOR BULUS<br></br>
                        Senior Pastor---REV. TANGWA<br></br>
                        Associate Pastor---PST. MISHAK JUDE
                        <hr><br>
                        <p align="center">
                        Register and update your membership details on<br>
                        CHURCH MEMBERSHIP
                        <hr><br>
                        <p align="center">Membership in ECWA Church is by the following ways:<br>
                        1. Believing and accepting  Jesus as your Lord and personal Saviour.
                        <br>
                        2. Believer's Baptism (Immersion).
                        <br>
                        3.Letter of transfer of membership from your former church.
                        <br>
                        .........................................<br>
                        God Bless You as <br>You Worship with us</p>
                        <hr>
                        <p align="center">
                        Here we have the <br>
                        <a href="boe">ECWA Bwari board of elders</a>
                        <hr>
                        <p align="center">
                        Church Weekly and Fellowship Activities
                        <br>
                        And more other activities available here at: <br>
                        <a href="woma">ECWA Good News Bwari Weekly/Monthly Activities</a><br>
                        <a href="cpfq">CHURCH PROGRAMS FOR THE QUARTER</a>
                        <hr><br>
                        <p align="center">
                        KINGDOM INVESTMENT OPPORTUNITIES (MATT 6:19 - 21) ARE AVAILABLE OVER THIS PAGE @:<br>
                        <i><a href="kio">
                        ECWA KINGDOM INVESTMENT OPPORTUNITIES</a><br>
                        <font size ="4pt" color="maroon">
                        Contact us @: <br>
                        ECWA GOOD NEWS BWARI,<br>
                        P . O . Box 95,<br>
                        Bwari<br>
                        Abuja.<br>
                        </font>
                        </i>
                        </p>
                        <br>
                        </body>
                        </html>""", status_code=200)},
        self.btg = {('btgs', '0.1.4'): HTMLResponse("""<!DOCTYPE HTML>
                        <html lang="en" dir="ltr">
                            <head>
                        <meta charset="utf-8">
                            <title>BWAYA MEDIA UNIT</title>
                        </head>
                            <body>
                        <br>
                        <img src="C:\b\Bwroline\static\bpics\b.jpg" width="300", height="90" alt="bmu logo"></img></a>
                        <br>
                        <h1 align="center">
                        <font color="blue">
                        <b>BEE~TEE GEES ROCKS THE GLOBE MUSIC</font>
                        <br>
                        <font size="4.5pt">
                        <br>
                        <h1 id="btgees.com", "btgs">
                        Our music goes home and away<br>
                        We represent the home away
                        </p>
                        <br>
                        <hr>
                        <p align="center">
                        <img src="C:\b\bpics\b1.jpg" width="300", height="200"></img>
                        <img src="C:\b\bpics\b3.jpg" width="300", height="200"></img>
                        <img src="C:\b\bpics\b2.jpg" width="300", height="200"></img>
                        <hr>
                        <h2 id="btgees" align="center">
                        Welcome to the home site where you'll have to find more of about
                        what you've found nowhere than where you can only find it...
                        <br>
                        On this page you'll find the tracks and the hit music that rocks
                        <hr>
                        <p align="center">
                        <img src="C:\b\bpics\sj31.jpg" width="300" height="200">  </img>
                        <img src="C:\b\bpics\sj21.jpg" width="300" height="200">  </img>
                        <img src="C:\b\bpics\sj4.jpg" width="300" height="200">  </img>

                        <!--popsj.com-->
                        <a href="popsj.com" target="_blank"><br>
                        <p id="bt" align="center">
                        Best Carter</a><br>
                        For your world of favorites and settle for the best from the best
                        <hr>

                        <p id="bt">
                        Check out<br>
                        <a href="btgsfd.com" target="_blank">
                        for the best and latest design so far on btgees fashion </a>
                        <br>

                        What a hectic day? You want to be good any where, at work place, Market square place or even other sides part of the world like you are home! Make good order of your choice live...<br>
                        --Good cooked foods--<br>
                        --> No preservatives nor other harming cause body substances<br>
                        --Nourishing snacks--<br>
                        --> Freshly made and reserved naturally for your good taste<br>
                        --Ceremonial event services--<br>
                        All at Affordable Prices<br>

                        <br>
                        Music is as part of life<br>
                        </br>Fashion and Design is our Culture<br>
                        </br>Eatery is part of our tradition and We Hook Up to make up So Wake up!<br>
                        Download our musics and jokes live right here on... <br>
                        </br>
                        They are musics you'll love that you might 've been searching for...<hr>
                        <p id="btgees.com" r="a">
                        <a href="nja.com" target="_blank">Naija Music</a><br>
                        <a href="frgn.com" target="_blank">Foreign Music</a><br>
                        <a href="njarege.com" target="_blank">Reggae Music</a><br>
                        <a href="oldskl.com" target="_blank">Old Skool</a><br>
                        <a href="mp3.com" target="_blank">Mp3</a><br>
                        <a href="bbl.com" target="_blank">Blues</a><br>
                        <a href="bvids.com" target="_blank">Videos</a>
                        <hr>
                        <p align="center">
                        <font size= "4.5pt" color="brown-orange">
                        No only hear about us but, also meet us live online on this site<br>
                        <br><br>
                        Is it a laughter mood you wish to be! Or better of...</br>
                        <hr>
                        <p id="ct">
                        <a href="index11.html">Bee~Tee Gees Contact </a>
                        email : bwroline@gmail.com <br>
                        website : <a href="server" id="b">server</a>
                        <br>
                        Web application project manager<br>
                        Web  maintainer 
                        <br></br>
                        </body>
                        </html>""", status_code=200)}
        self.txt = {'Amount': 60, 'Sender': [self.usr_log or self.usr_sgn], (): ''}
        self.user += 1, self.user


text = Text()
text1 = [text.bmu, text.ghlp, text.shd, text.egb, text.btg]
text2 = text.ghlp
text3 = text.shd
text4 = text.egb
text5 = text.btg
per_year = float(375 * 60 * 12) / 100
per_day = float((375 * 60 * 365) / 100) * (text)
per_day += per_day


async def usrs_get_bmu(self):
    try:
        [login, signup] = [text.usr_log, text.usr_sgn]
        for bm_u in bmu[text1, text2, text3, text4, text5]:
            if login == text.usr_log:
                bm_u[0]
                login_request = text['']
        day = datetime.day()
    interest_per_year = Text.per_year
    daily = Text.per_day * self.user
    session = {
        60 * day
    }

    while interest_per_year <= 2700.1:
        deposit += interest_per_year
        for bm_u in bmu[self.user, self.bmu, self.shd, self.ghlp, self.egb, self.btg]:
            # requests = ['', self.bmu, self.shd, self.ghlp, self.egb, self.btg]
            self.usr_log += (self.bmu['\n bmu', '0.1.0'])
            self.usr_sgn += (self.bmu['\n bmu', '0.1.0'])
            if [self.user]:
                bwroline = self.user
                shamudoents = self.user
                great_hussein_legal_practitioners = self.user
                ecwa_good_news_bwari = self.user

    b_giv = giver(giver={
        '\n server': ['Transfer for interest to opening:', self.bmu or self.shd or self.ghlp
                            or self.egb or self.btg],
        'Date': [datetime.month, 'Salary Payment'],
        'to': [Optional[str], acc.Acc_no]})

    dic = acc(id=self.bmu, Acc_name='DCI', current_balance=500.6 + deposit, Session=datetime.now(),
              Acc_no={
                  'from_': b_giv,
                  'to': ['https://unitybankplc.com/id/', '0025531657', +2348120744800]})
    dsf = acc(id=self.shd, Acc_name='DCI', current_balance='' + deposit, Session=datetime.now(), Acc_no={
        'from_': b_giv,
        'to': ['0025531657', +234]})
    yid = acc(id=self.egb, Acc_name='DCI', current_balance='' + deposit, Session=datetime.now(), Acc_no={
        'from_': b_giv,
        'to': ['0025531657', +2348120744800]})
    nja = acc(id=self.ghlp, Acc_name='DCI', current_balance='' + deposit, Session=datetime.now(), Acc_no={
        'from_': b_giv,
        'to': ['0025531657', +2348120744800]})
    fc = acc(id=self.btg, Acc_name='DCI', current_balance='' + deposit, Session=datetime.now(), Acc_no={
        'from_': b_giv,
        'to': ['0025531657', +2348120744800]})

    trans1 = trans(id=self.user, amount=60, daily=lo, depositor=self.user, name='DFS', acc_no='', phone_no='',
                   salary_amount=100.50)
    trans2 = trans(id=self.user, amount=60, daily=lo, depositor=self.user, name='NJA', acc_no='', phone_no='',
                   salary_amount=100.50)
    trans3 = trans(id=self.user, amount=60, daily=lo, depositor=self.user, name='YIJ', acc_no='', phone_no='',
                   salary_amount=100.50)
    trans4 = trans(id=self.user, amount=60, daily=lo, depositor=self.user, name='FC', acc_no='', phone_no='',
                   salary_amount=100.50)

    bdb = datetime.now(), ':', ([dic, dsf, yid, nja, fc] == [dic.__getstate__(trans1), dsf.__getstate__(trans2),
                                                             yid.__getstate__(trans3), fc.__getstate__(trans4)])
    return [self.bdb, self.bmu]


async def usrs_get_shd(self):
    return self.shd['\n shd']


text = Text()
bmu = text.usr_request['\n bmu']
shd = text.usr_request['\n shd']
ghl = text.usr_request['\n ghlp']
egb = text.usr_request['\n egb']
btg = text.usr_request['\n btgs']


@app.get("/https://bwroline.com/db/{bdb}")
async def user(self):
    for requests in self.usr_request:
        if self.usr_request == requests:
            for b_m_u in self.usr_request:
                bmu = self.usr_request['bmu']
                if bmu == self.usr_request['bmu']:
                    print(bmu)
            for s_h_d in self.usr_request:
                shd = self.usr_request['shd']
                if shd == self.usr_request['shd']:
                    print(shd)
            for g_h_l_p in self.usr_request:
                ghlp = self.usr_request['ghlp']
                if ghlp == self.usr_request['ghlp']:
                    print(ghlp)
            for e_g_b in self.usr_request:
                egb = self.usr_request['egb']
                if egb == self.usr_request['egb']:
                    print(egb)
            for b_t_g in self.usr_request:
                btg = self.usr_request['btgs']
                if btg == self.usr_request['btgs']:
                    print(btg)
    if self.usr_sgn:
        self.txt['Amount']
        self.txt['Sender'] = self.usr_sgn
    elif self.usr_log:
        self.txt['Amount']
        self.txt['Sender'] = self.usr_log

        n = 0
        if n <= 987654321:
            n += 1
            deposit = 6
            deposit += 6.5
            curr_date = datetime.now()
            b_m_u = [
                {
                    '\n bdb': {
                        '\n deposit': deposit,
                        '\n server': 'bmu',
                        '\n annual': [datetime.year, deposit],
                        '\n daily': [curr_date, deposit]},
                    '\n shamudoents.com': {
                        '\n deposit': deposit,
                        '\n shamudoents.com': 'shd',
                        '\n annual': [datetime.year, deposit],
                        '\n daily': [curr_date, deposit]},
                    '\n greathusseinlegalpractitioners.com': {
                        '\n deposit': deposit,
                        '\n greathusseinlegalpractitioners.com': 'ghl',
                        '\n annual': [datetime.year, deposit],
                        '\n daily': [curr_date, deposit]},
                    '\n ecwagoodnewsbwr.com.com': {
                        '\n deposit': deposit,
                        '\n ecwagoodnewsbwr.com.com': 'egb',
                        '\n annual': [
                            datetime.year, deposit],
                        '\n daily': [curr_date, deposit]},
                    '\n btgees.com': {
                        '\n deposit': deposit,
                        '\n btgees.com': 'btg',
                        '\n annual': [datetime.year, deposit],
                        '\n daily': [curr_date, deposit]}
                }
            ]

            s_h_d = [
                {
                    '\n bdb': {
                        '\n deposit': deposit,
                        '\n server': 'bmu',
                        '\n annual': [datetime.year, deposit],
                        '\n daily': [curr_date, deposit]},
                    '\n shamudoents.com': {
                        '\n deposit': deposit,
                        '\n shamudoents.com': 'shd',
                        '\n annual': [datetime.year, deposit],
                        '\n daily': [curr_date, deposit]}
                }
            ]

            g_h_l = [
                {
                    '\n bdb': {
                        '\n deposit': deposit,
                        '\n server': 'bmu',
                        '\n annual': [datetime.year, deposit],
                        '\n daily': [curr_date, deposit]},
                    '\n ghlp.com': {
                        '\n deposit': deposit,
                        '\n greathusseinlegalpractitioners.com': 'ghl',
                        '\n annual':
                            [datetime.year, deposit],
                        '\n daily': [curr_date, deposit]}
                }
            ]

            e_g_b = [
                {
                    '\n bdb': {
                        '\n deposit': deposit,
                        '\n server': 'bmu',
                        '\n annual': [datetime.year, deposit],
                        '\n daily': [curr_date, deposit]},
                    '\n egb.com': {
                        '\n deposit': deposit,
                        '\n ecwagoodnewsbwr.com.com': 'egb',
                        '\n annual': [datetime.year, deposit],
                        '\n daily': [curr_date, deposit]}
                }
            ]

            b_t_g = [
                {
                    '\n bdb': {
                        '\n deposit': deposit,
                        '\n server': 'bmu',
                        '\n annual': [datetime.year, deposit],
                        '\n daily': [curr_date, deposit]},
                    '\n btg.com': {
                        '\n deposit': deposit,
                        '\n btgees.com': 'btg',
                        '\n annual': [datetime.year, deposit],
                        '\n daily': [curr_date, deposit]}
                }
            ]

            dic = acc(id=n, Acc_no=['0025531657', +2348120744800], Acc_name='DCI', balance=500.6 + deposit, )
            # interest = p*r*n. p = beginning balance, r = interest rate, p = period
            annual_int = float(375 * 6.5 * 12) / 100
            return interest + deposit

    dic = trans(id=o, deposit=6.5, annual=per_year, daily=lo, depositor=["\n dbd", id], name='DIC',
                acc_no=["", int], salary_amount=198.84)
    dfs = trans(id=o, deposit=6.5, annual=per_year, daily=lo, depositor=['\n shd', ''], name='DFS',
                acc_no=['45752', +2347666897], salary_amount=100.50)
    nja = trans(id=o, deposit=6.5, annual=per_year, daily=lo, depositor=['', ''], name='NJA',
                acc_no=['54', +234], salary_amount=100.50)
    yij = trans(id=o, deposit=6.5, annual=per_year, daily=lo, depositor=['', ''], name='YIJ',
                acc_no=['42', +234], salary_amount=100.50)
    fc = trans(id=o, deposit=6.5, annual=per_year, daily=lo, depositor=['', ''], name='FC',
               acc_no=['54', +234], salary_amount=100.50)

    txt0 = {'acct': '', 'phone': ''}, {'+234': ('Alert', dic), 'to': DIC, 'content': ''}
