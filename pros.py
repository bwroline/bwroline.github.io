import time
from datetime import datetime
from typing import Union
# import requests
from starlette.responses import HTMLResponse
from fastapi import FastAPI, Request
from bom import PROSOline as PROS
from bwroline.bom import BMU_Detail as BTM, BMU_Mess as BRM
from bwroline.user import pwd_context, Token, User

Bwroline = FastAPI()


@Bwroline.get("/")
@Bwroline.post("/.bdb/.b.bwr.bdb.bmu.**/.bdb.bwroline.com/")
# @Bwroline.middleware("https")
def time_process(self, request: Request, call_next):
    s_t = time.time()
    response = call_next(request)
    process_time = time.time() - s_t
    response.headers['X-time taken to process each bwroline file'] = str(process_time)
    return response


class PROSOline:
    name = 'PROSOline Global Multi-links Communication Limited'
    bwr = HTMLResponse("""<!DOCTYPE HTML>
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
                                    """, status_code=200)
    sh = HTMLResponse("""<!DOCTYPE html>
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
                                                                                       </html>""", status_code=200)
    gh = HTMLResponse("""<!DOCTYPE html>
                                                                <html lang="en" dir="ltr">
                                                                    <head>
                                                                <meta charset="utf-8">
                                                                    <title><a href="server">BWAYA MEDIA UNIT</a></title>
                                                                </head>
                                                                    <body>
                                                                <br><img src="https://images.apis.com/bwroline.com/ghlp/images/api/staticimage?size=70*30&makers=9ja.jpg" 
                                                                alt="ghlp 9ja images"></img><font size="5pt"><h1 align="center">GREAT HUSSEIN LEGAL PRACTITIONERS</h1></font><img src="https://images.apis.com/bwroline.com/ghlp/images/api/staticimage?size=70*30&makers=bgl1.jpg" alt="ghlp bgl1 image"></img><p align="center"><font size="5pt" color="brown">No. 4, Jibowu Close Off Ozulua Road<br>University Of Lagos Akoka<br>Yaba, Lagos</br></font><hr><p align="center"><img src="https://images.apis.com/bwroline.com/ghlp/images/api/staticimage?size=70*30&makers=bgl.jpg" width="200" height="70"></img><img src="https://images.apis.com/bwroline.com/ghlp/images/api/staticimage?size=70*30&makers=bgl1.jpg" width="200" height="70"></img><br><font size="6pt" color="saphire"><p align="center">Greats Wild Legal Practitioners<font color="blue" size= "6pt">Yusuf Hussein, Esq <br>Principal Counsel <br>Great-Hussein Legal Practitioners <br></br></font><hr><font color="golden-gold" size= "6pt"><p align="center">You are Welcome!<br>Here you shall find all the services for legal living in any part all over the world<br></font><hr><p align="center"><font color="orange" size= "6pt">List of Our Services are:<br></b></font><font face="Sofadione">Legal Case Handle<br>Legal Law Enforcing<br>Legal Housing Agent<br>And other Federation Legal obligations</font><p align="center"><br><font size= "6pt" color="saphire">We practice Justice and Loyalty!</font><br><font size= "6pt" color="green">Legal Greats Legal Practitioners The Desired Place For Hope</font><hr></br><p align="center"><font size="6pt">Tel:08033514288, 08023941762, 01-9521070</br>E-mail:greathusseinlegal@yahoo.com</font><br></br><br></body></html>""", status_code=200)
    eg = HTMLResponse("""<!DOCTYPE HTML>
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
                                                                                </html>""", status_code=200)
    bt = HTMLResponse("""<!DOCTYPE HTML><html lang="en" dir="ltr"><head><meta charset="utf-8"><title>BWAYA MEDIA UNIT</title>
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
                                                                                </html>""", status_code=200)

    def __init__(self, b_=bwr, s=sh, g=gh, e=eg, t=bt, bwaya=[bwr, sh, gh, eg, bt]):
        self.b: b_ = PROS.website
        self.s: s = PROS.website
        self.g: g = PROS.website
        self.e: e = PROS.website
        self.t: t = PROS.website
        self.bw: bwaya = list[PROS.website]

    def bmu(self):
        bmu = [PROSOline.bwr, PROSOline.sh, PROSOline.gh, PROSOline.eg, PROSOline.bt]
        return bmu

    def bwroline(self):
        bwr = PROSOline.bwr
        return {"website": bwr}

    def shamudoents(self):
        sh = PROSOline.sh
        return {"website": sh}

    def great_hussein(self):
        gh = PROSOline.gh
        return {"website": gh}

    def ecwa_goodnews_church(self):
        eg = PROSOline.eg
        return {"website": eg}

    def btgees(self):
        bt = PROSOline.bt
        return {"website": bt}


b = PROSOline()
bw = b.bwroline()
sh = b.shamudoents()
gh = b.great_hussein()
eg = b.ecwa_goodnews_church()
bt = b.btgees()


f = 0
count: Union[list, str, int, float, bool, None]
while f <= 998877665544.556655e6:
    f += 4.556655e6
    pass

print(bw, sh, gh, eg, bt)

DIC = {
    "user_id": "",
        "DESC": "",
        "key": "",
        "price": 4.556655e6,
        "phone": "08120744800",
        "b_k_n_d_s_c": ("0025****", "0025536157", "****1657", 1, 4.556655e6),
        "tags": "b_t_r_a_n_s",
        "is_active": True,
        "name": "bwroline.com",
        "website": str(bw),
}
FSD = {
"user_id": "",
          "DESC": "",
          "key": "",
        "price": 4.556655e6,
        "phone": "",
        "bk_n_d_s_c": ["0025****", "****1657", 1, 4.556655e6],
        "tags": "b_t_r_a_n_s",
        "is_active": True,
        "name": "shamudoents.com",
        "website": str(sh)
}
NJA = {
"user_id": "",
        "DESC": "",
        "key": "",
        "price": 4.556655e6,
        "phone": "",
        "bk_n_d_s": ["0025****", "****1657", 1, 4.556655e6],
        "tags": "b_t_r_a_n_s",
        "is_active": True,
        "name": "greatHusseinLegalPractitioners.com",
        "website": str(gh)
}
JIY = {
"user_id": "",
        "DESC": "",
        "key": "",
        "price": 4.556655e6,
        "phone": "",
        "bk_n_d_s": ["0025****", "****1657", 1, 4.556655e6],
        "tags": "b_t_r_a_n_s",
        "is_active": True,
        "name": "ecwagoodnewsbwr.com.com",
        "website": str(eg)
}
FC = {
"user_id": "",
        "DESC": "",
        "key": "",
        "price": 4.556655e6,
        "phone": "",
        "bk_n_d_s": ["0025****", "****1657", 1, 4.556655e6],
        "tags": "b_t_r_a_n_s",
        "is_active": True,
        "name": "btgees.com",
        "website": str(bt)
}

# r = requests.get(f"https://bwroline.com/{bwroline}")
# br = requests.post(f"https://bwroline.com/{bwroline}", data={"name": "bwroline"})


def count():
    o = 0
    while o <= 999999.999999e9:
        o += 4.556655e6
        return o
    print()


@Bwroline.get("/.bdb/.bdb.bmu/{bwroline.com}/users/{bwroline.com}{bmu}", response_model=BRM)  # path parameters, BRM ---> BMU ResPMess
@Bwroline.post("/.bdb/.bdb.bmu/users/{bwroline.com}{bmu}", response_model=BRM)
@Bwroline.post("/.bdb/.bdb.bmu/{Transaction_details}/{bwroline.com}", response_model=BTM)
def bwroline(bwr: Union[int, str, None] = None):  # BMT ---> BMU TransModel
    dic_dict = PROS.dict()
    if bwr:
        dic_dict.update({"DESC": "PROSOline Multi", "bmu": "bwroline", "acc_numb": ["****531657", "0025531657", "002553****"], "active": True, "curr_balance": PROS.bal + PROS.curr_balance + count()})  # BRM ---> BMU ResPMess
    return {"BMT": dic_dict}


@Bwroline.get("/.bdb/.bdb.bmu/{bwroline.com}/{shamudoents.com}/users/{bwroline.com}{shamudoents.com}{shd}", response_model=BRM)  # path parameters, BRM ---> BMU ResPMess
@Bwroline.post("/.bdb/.bdb.bmu/users/{shamudoents.com}{shd}", response_model=BRM)
@Bwroline.post("/.bdb/.bdb.bmu/{Transaction_details}/{shamudoents.com}{bwroline.com}", response_model=BTM)
def shamudoents(shd: Union[int, str, None] = None):  # query not found in operation path. # BMT ---> BMU TransModel
    fsd_dict = PROS.dict()
    if shd:
        fsd_dict.update({"DESC": "PROSOline Multi", "bmu": "bwroline", "acc_numb": [""], "active": True, "curr_balance": PROS.curr_balance + count()})  # BRM ---> BMU ResPMess
    return {"transaction_details": fsd_dict}


@Bwroline.get("/.bdb/.bdb.bmu/{bwroline.com}{greatHusseinLegalPractitioners}/users/{bwroline.com}{ghlp}", response_model=BRM)  # path parameters, BRM ---> BMU ResPMess
@Bwroline.post("/.bdb/.bdb.bmu/users/{bwroline.com}{ghlp}", response_model=BRM)
@Bwroline.post("/.bdb/.bdb.bmu/{Transaction_details}/{ghlp.com}{bwroline.com}", response_model=BTM)
def great_hussein_leg_pract_(ghl: Union[int, str, None] = None):
    ajn_dict = PROS.dict()  # BMT ---> BMU TransModel
    if ghl:
        ajn_dict.update({"DESC": "PROSOline Multi", "bmu": "bwroline", "acc_numb": [""], "active": True, "curr_balance": PROS.bal + PROS.curr_balance + count()})  # BRM ---> BMU ResPMess
    return {"transaction_details": ajn_dict}


@Bwroline.get("/.bdb/.bdb.bmu/{bwroline.com}{ecwagoodnewsbwr.com.com}/users/{bwroline.com}{ecwagoodnewsbwr.com.com}{egbwr}", response_model=BRM)  # path parameters, BRM ---> BMU ResPMess
@Bwroline.post("/.bdb/.bdb.bmu/users/{bwroline.com}{ecwagoodnewsbwr.com.com}{egbwr}", response_model=BRM)
@Bwroline.post("/.bdb/.bdb.bmu/{Transaction_details}/{ecwagoodnewsbwr.com.com}{bwroline.com}", response_model=BTM)
def ecwa_good_news_bwr(egb: Union[int, str, None] = None):
    jiy_dict = PROS.dict()  # BMT ---> BMU TransModel
    if egb:
        jiy_dict.update({"DESC": "PROSOline Multi", "bmu": "bwroline", "acc_numb": [""], "active": True, "curr_balance": PROS.curr_balance + count()})  # BRM ---> BMU ResPMess
    return {"transaction_details": jiy_dict}


@Bwroline.get("/.bdb/.bdb.bmu/{bwroline.com}{btgees.com}/users/{bwroline.com}{btgees.com}{btgs}", response_model=BRM)  # path parameters, BRM ---> BMU ResPMess
@Bwroline.post("/.bdb/.bdb.bmu/users/{bwroline.com}{btgs}", response_model=BRM)
@Bwroline.post("/.bdb/.bdb.bmu/{Transaction_details}/{btgees.com}{bwroline.com}", response_model=BTM)
def btgees(btg: Union[int, str, None] = None):
    fc_dict = PROS.dict()  # BMT ---> BMU TransModel
    if btg:
        fc_dict.update({"DESC": "PROSOline Multi", "bmu": "bwroline", "acc_numb": [""], "active": True, "curr_balance": PROS.curr_balance + count()})  # BRM ---> BMU ResPMess
    return {"transaction_details": fc_dict}



# shamudoents_ == open(webbrowser.open_new_tab('index1.html')),
# greatHussein_ == open(webbrowser.open_new_tab('index2.html')),
# ecwaGoodnews_ == open(webbrowser.open_new_tab('index3.html')),
# btgees_ == open(webbrowser.open_new_tab('index4.html'))

