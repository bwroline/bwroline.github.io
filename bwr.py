import time

from fastapi import Request, FastAPI
import webbrowser
from main import read_user, read_items

from starlette.responses import HTMLResponse

from bwroline.bom import BMU_Detail
from bwroline.schemas import User
from bwroline.user import get_current_active_user
B = FastAPI()


# @B.middleware("https")
def time_process(self, request: Request, call_next):
    s_t = time.time()
    response = call_next(request)
    process_time = time.time() - s_t
    response.headers['X-time taken to process each bwroline file'] = str(process_time)
    return response


def clicks(self, ck: list[int, float, str]):
    prce = 4.556655e6
    click = 1
    while prce or click <= 9999:
        click += 1
        intrst = f'{click} * ({time_process * 4.556655e6})'
        d_ = click + int(float(intrst))
        print(f'No.: {click + click}, Amount: NGN{intrst}')  # mark my interest


class PROSOline:
    name = ''
    bwr = str(HTMLResponse("""<!DOCTYPE HTML>
                            <html lang="en" dir="ltr">
                            <head>
                                <meta charset="utf-8">
                                <title></title>
                                <base href="C:\/Users\/HP\/.com\/bwroline">
                            </head>
                            <body>
                            <p>
                                <em>
                                    <a href="index.html">
                                        <img src="C:\/Users\/HP\/.com\/bwroline\/bpics\/b.jpg" alt="bwroline.com image"></img>
                                    </a>
                                </em>
                            </p>
                            <font face="pyramid" color="blue">
                                <p align="center">Abuja Gbagyi Media <br>
                                    F. C. T - Abuja<br>
                                    Since July 2018
                                </p>
                            </font><br>
                            Be and remain in touch with the things you've been missing out! Get all the interesting Dramas and Movies or videos
                            you've desired to watch, that you can get in touch with the Gbagyi entertainment's trends like the
                            <a href="index1.html" target="_blank">shamudoents entertainments</a>across the globe likewise other trends... We make
                            sure you are connected and remain connected with
                            God and to be entertained by our religious traditions<a href="index3.html" target="_blank">ecwagoodnewsbwr.com</a>
                            Download also your best and latest Musics available here <a href="index4.html" target="_blank">btgees</a>
                            You can get reach a legal practitioner for services <a href="index2.html" target="_blank">great hussein legal
                                practitioners</a><br>
                            </body>
                            </html>
                            """, status_code=200))
    sh = str(HTMLResponse("""<!DOCTYPE html>
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
                                                                           </html>""", status_code=200))
    gh = str(HTMLResponse("""<!DOCTYPE html>
                                                        <html lang="en" dir="ltr">
                                                            <head>
                                                        <meta charset="utf-8">
                                                            <title><a href="server">BWAYA MEDIA UNIT</a></title>
                                                        </head>
                                                            <body>
                                                        <br><img src="https://images.apis.com/bwroline.com/ghlp/images/api/staticimage?size=70*30&makers=9ja.jpg" 
                                                        alt="ghlp 9ja images"></img><font size="5pt"><h1 align="center">GREAT HUSSEIN LEGAL PRACTITIONERS</h1></font><img src="https://images.apis.com/bwroline.com/ghlp/images/api/staticimage?size=70*30&makers=bgl1.jpg" alt="ghlp bgl1 image"></img><p align="center"><font size="5pt" color="brown">No. 4, Jibowu Close Off Ozulua Road<br>University Of Lagos Akoka<br>Yaba, Lagos</br></font><hr><p align="center"><img src="https://images.apis.com/bwroline.com/ghlp/images/api/staticimage?size=70*30&makers=bgl.jpg" width="200" height="70"></img><img src="https://images.apis.com/bwroline.com/ghlp/images/api/staticimage?size=70*30&makers=bgl1.jpg" width="200" height="70"></img><br><font size="6pt" color="saphire"><p align="center">Greats Wild Legal Practitioners<font color="blue" size= "6pt">Yusuf Hussein, Esq <br>Principal Counsel <br>Great-Hussein Legal Practitioners <br></br></font><hr><font color="golden-gold" size= "6pt"><p align="center">You are Welcome!<br>Here you shall find all the services for legal living in any part all over the world<br></font><hr><p align="center"><font color="orange" size= "6pt">List of Our Services are:<br></b></font><font face="Sofadione">Legal Case Handle<br>Legal Law Enforcing<br>Legal Housing Agent<br>And other Federation Legal obligations</font><p align="center"><br><font size= "6pt" color="saphire">We practice Justice and Loyalty!</font><br><font size= "6pt" color="green">Legal Greats Legal Practitioners The Desired Place For Hope</font><hr></br><p align="center"><font size="6pt">Tel:08033514288, 08023941762, 01-9521070</br>E-mail:greathusseinlegal@yahoo.com</font><br></br><br></body></html>""", status_code=200))
    eg = str(HTMLResponse("""<!DOCTYPE HTML>
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
                                                                    </html>""", status_code=200))
    bt = str(HTMLResponse("""<!DOCTYPE HTML><html lang="en" dir="ltr"><head><meta charset="utf-8"><title>BWAYA MEDIA UNIT</title>
                                                                    </head><body><br><img src="C:\b\Bwroline\static\bpics\b.jpg" width="300", height="90" alt="bmu logo"></img></a><br>
                                                                    <h1 align="center"><font color="blue"><b>BEE~TEE GEES ROCKS THE GLOBE MUSIC</font><br>
                                                                    <font size="4.5pt"><br><h1 id="btgees.com", "btgs">
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
                                                                    </html>""", status_code=200))

    def __init__(self, bwaya: str = None):
        self.b = self.Bo(PROSOline.bwr, PROSOline.sh, PROSOline.gh, PROSOline.eg, PROSOline.bt)
        self.s = self.Se(PROSOline.sh)
        self.g = self.Gl()
        self.e = self.Ec()
        self.t = self.Be()
        self.bw = bwaya

    def bwroline(self, bwr: int| str = None):
        print(f'<p align="center"> PROS-O-line Global Multi-links Media Nigeria LTD </p>')

    class Bo:
        def __init__(self, bwr_: list[str, int, float], shd_: list[str, int, float], ghl_: list[str, int, float], egb_: list[str, int, float], btg_: list[str, int, float]):
            self.t = btg_
            self.e = egb_
            self.g = ghl_
            self.s = shd_
            self.b = bwr_
            self.b_ = PROSOline.bwr
            self.p_ = f'{4.556655e6} * {5} * {clicks}'

        def bwroline(self, bwr: list[int, str] == ['0', '1']):
            print(f'<p align="center"> Bwaya Media Unit (BMU)</p>')
            print(f'0: {bwr}: bwroline.com: [{PROSOline.Bo.bwroline}, \t {PROSOline.Se.shamudoents}, \t {PROSOline.Gl.great_hussein}, \t {PROSOline.Ec.ecwa_goodnews_church}, \t {PROSOline.Be.btgees}]')

        def b_sum(self):
            print(f'{4.556655} * {clicks} * {get_current_active_user}')

    class Se:
        def __init__(self, shd: HTMLResponse):
            self.b_ = """<!DOCTYPE HTML>
                                    <html lang="en" dir="ltr">
                                    <head>
                                        <meta charset="utf-8">
                                        <title></title>
                                        <base href="C:\/Users\/HP\/.com\/bwroline">
                                    </head>
                                    <body>
                                    <p>
                                        <em>
                                            <a href="index.html">
                                                <img src="C:\/Users\/HP\/.com\/bwroline\/bpics\/b.jpg" alt="bwroline.com image"></img>
                                            </a>
                                        </em>
                                    </p>
                                    <font face="pyramid" color="blue">
                                        <p align="center">Abuja Gbagyi Media <br>
                                            F. C. T - Abuja<br>
                                            Since July 2018
                                        </p>
                                    </font><br>
                                    Be and remain in touch with the things you've been missing out! Get all the interesting Dramas and Movies or videos
                                    you've desired to watch, that you can get in touch with the Gbagyi entertainment's trends like the
                                    <a href="index1.html" target="_blank">shamudoents entertainments</a>across the globe likewise other trends... We make
                                    sure you are connected and remain connected with
                                    God and to be entertained by our religious traditions<a href="index3.html" target="_blank">ecwagoodnewsbwr.com</a>
                                    Download also your best and latest Musics available here <a href="index4.html" target="_blank">btgees</a>
                                    You can get reach a legal practitioner for services <a href="index2.html" target="_blank">great hussein legal
                                        practitioners</a><br>
                                    </body>
                                    </html>
                                    """
            self.s_ = """<!DOCTYPE html>
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
                                                                                   </html>"""
            self.sh = shd
            self.p_ = f'{4.556655e6} * {2} * {clicks} * {get_current_active_user}'

        def shamudoents(self):
            print(f'PROS-O-line": 0, \n Shamudoents: {self.s_}')

        def s_sum(self):
            print(f'{4.556655} * {clicks} * {get_current_active_user}')

    class Gl:
        def __init__(self):
            self.g_ = PROSOline.gh
            self.b_ = PROSOline.bwr
            self.p_ = f'{4.556655e6} * {2} * {clicks}'

        def great_hussein(self, ghl: int| str = None):
            print(f'PROS-O-line: 0 \n Great Hussein Legal Practitioners: {self.g_} id: {ghl}')

        def g_sum(self):
            print(f'{4.556655} * {clicks} * * {get_current_active_user}')

    class Ec:
        def __init__(self):
            self.e_ = PROSOline.eg
            self.b_ = PROSOline.bwr
            self.p_ = f'{4.556655e6} * {2} * {clicks}'

        def ecwa_goodnews_church(self, egb: int or str = None):
            print(f'PROS-O-line: 0 \n ECWA Goodnews Church: {self.e_} id: {egb}')

        def e_sum(self):
            print(f'{4.556655} * {clicks} * {get_current_active_user}')

    class Be:
        def __init__(self):
            self.t_ = PROSOline.bt
            self.b_ = PROSOline.bwr
            self.p_ = f'{4.556655e6} * {2} * {clicks}'

        def btgees(self, btg: int| str = None):
            print(f'PROS-O-line": 0, \n Btgees: {self.t_} id: {btg}')

        def t_sum(self):
            print(f'{4.556655} * {clicks} * {get_current_active_user}')


b = PROSOline(PROSOline.bwr)
bw = b.Bo(
    """<!DOCTYPE HTML>
                            <html lang="en" dir="ltr">
                            <head>
                                <meta charset="utf-8">
                                <title></title>
                                <base href="C:\/Users\/HP\/.com\/bwroline">
                            </head>
                            <body>
                            <p>
                                <em>
                                    <a href="index.html">
                                        <img src="C:\/Users\/HP\/.com\/bwroline\/bpics\/b.jpg" alt="bwroline.com image"></img>
                                    </a>
                                </em>
                            </p>
                            <font face="pyramid" color="blue">
                                <p align="center">Abuja Gbagyi Media <br>
                                    F. C. T - Abuja<br>
                                    Since July 2018
                                </p>
                            </font><br>
                            Be and remain in touch with the things you've been missing out! Get all the interesting Dramas and Movies or videos
                            you've desired to watch, that you can get in touch with the Gbagyi entertainment's trends like the
                            <a href="index1.html" target="_blank">shamudoents entertainments</a>across the globe likewise other trends... We make
                            sure you are connected and remain connected with
                            God and to be entertained by our religious traditions<a href="index3.html" target="_blank">ecwagoodnewsbwr.com</a>
                            Download also your best and latest Musics available here <a href="index4.html" target="_blank">btgees</a>
                            You can get reach a legal practitioner for services <a href="index2.html" target="_blank">great hussein legal
                                practitioners</a><br>
                            </body>
                            </html>
                            """,
    """<!DOCTYPE html>
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
                                                                           </html>""",
    """<!DOCTYPE html>
                                                        <html lang="en" dir="ltr">
                                                            <head>
                                                        <meta charset="utf-8">
                                                            <title><a href="server">BWAYA MEDIA UNIT</a></title>
                                                        </head>
                                                            <body>
                                                        <br><img src="https://images.apis.com/bwroline.com/ghlp/images/api/staticimage?size=70*30&makers=9ja.jpg" 
                                                        alt="ghlp 9ja images"></img><font size="5pt"><h1 align="center">GREAT HUSSEIN LEGAL PRACTITIONERS</h1></font><img src="https://images.apis.com/bwroline.com/ghlp/images/api/staticimage?size=70*30&makers=bgl1.jpg" alt="ghlp bgl1 image"></img><p align="center"><font size="5pt" color="brown">No. 4, Jibowu Close Off Ozulua Road<br>University Of Lagos Akoka<br>Yaba, Lagos</br></font><hr><p align="center"><img src="https://images.apis.com/bwroline.com/ghlp/images/api/staticimage?size=70*30&makers=bgl.jpg" width="200" height="70"></img><img src="https://images.apis.com/bwroline.com/ghlp/images/api/staticimage?size=70*30&makers=bgl1.jpg" width="200" height="70"></img><br><font size="6pt" color="saphire"><p align="center">Greats Wild Legal Practitioners<font color="blue" size= "6pt">Yusuf Hussein, Esq <br>Principal Counsel <br>Great-Hussein Legal Practitioners <br></br></font><hr><font color="golden-gold" size= "6pt"><p align="center">You are Welcome!<br>Here you shall find all the services for legal living in any part all over the world<br></font><hr><p align="center"><font color="orange" size= "6pt">List of Our Services are:<br></b></font><font face="Sofadione">Legal Case Handle<br>Legal Law Enforcing<br>Legal Housing Agent<br>And other Federation Legal obligations</font><p align="center"><br><font size= "6pt" color="saphire">We practice Justice and Loyalty!</font><br><font size= "6pt" color="green">Legal Greats Legal Practitioners The Desired Place For Hope</font><hr></br><p align="center"><font size="6pt">Tel:08033514288, 08023941762, 01-9521070</br>E-mail:greathusseinlegal@yahoo.com</font><br></br><br></body></html>""",
    """<!DOCTYPE HTML>
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
                                                                    </html>""",
    """<!DOCTYPE HTML><html lang="en" dir="ltr"><head><meta charset="utf-8"><title>BWAYA MEDIA UNIT</title>
                                                                    </head><body><br><img src="C:\b\Bwroline\static\bpics\b.jpg" width="300", height="90" alt="bmu logo"></img></a><br>
                                                                    <h1 align="center"><font color="blue"><b>BEE~TEE GEES ROCKS THE GLOBE MUSIC</font><br>
                                                                    <font size="4.5pt"><br><h1 id="btgees.com", "btgs">
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
                                                                    </html>"""
)
sh = b.Se(PROSOline.sh)

p = b.Bo(4.556655e6, 4.556655e6, 4.556655e6, 4.556655e6, 4.556655e6)
bwroline = b.Bo.bwroline
shamudoents = b.Se.shamudoents
greatHussein = b.Gl.great_hussein
ecwaGoodnews = b.Ec.ecwa_goodnews_church
btgees = b.Be.btgees
bmu = [bwroline, shamudoents, greatHussein, ecwaGoodnews, btgees]
for q in bmu:
    shamudoents_ == open(webbrowser.open_new_tab('index1.html')),
    greatHussein_ == open(webbrowser.open_new_tab('index2.html')),
    ecwaGoodnews_ == open(webbrowser.open_new_tab('index3.html')),
    btgees_ == open(webbrowser.open_new_tab('index4.html'))

    while get_current_active_user() == [User, time_process] and get_current_active_user() == [int, str, bytes, bool, float]:
        userAccess00 = {'bwr': [bw], 'id': [0, 1], 'active': True},
        userAccess0 = {'shamudoents_bwr': [bw], 'id': [0, 2], 'active': True}
        userAccess1 = {'bwr': [bw], 'id': [0, 3], 'active': True}
        userAccess2 = {'bwr': [ecwaGoodnews_], 'id': [0, 4], 'active': True}
        userAccess3 = {'bwr': [btgees_], 'id': [0, 5], 'active': True}
        userAccess = [userAccess00, userAccess0, userAccess1, userAccess2, userAccess3]

        to_pros = {'d_eposit': f'{clicks} * {time_process}', 'for access': f'{userAccess}'}
        if get_current_active_user == [time_process, User]:
            for bwroline_ in userAccess:
                read_user.read_items()
                PROS = BMU_Detail(**to_pros)

            for shamudoents_ in bmu:
                get_current_active_user = User(**userAccess0)
                PROS = BMU_Detail(**to_pros)

            for greatHussein_ in bmu:
                get_current_active_user= User(**userAccess1)
                PROS = BMU_Detail(**to_pros)

            for ecwaGoodnews_ in bmu:
                get_current_active_user= User(**userAccess2)
                PROS = BMU_Detail(**to_pros)

            for btgees_ in bmu:
                get_current_active_user= User(**userAccess3)
                PROS = BMU_Detail(**to_pros)
