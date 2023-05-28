from starlette.responses import HTMLResponse
from fastapi import FastAPI
from bwroline.bwroline.bom import BMU_Details, BMU_Detail

BWAYA_metadata = [
    {
        "name": "BMU",
        "description": "Website Application **CREATED** to help self interest"
    },
    {
        "name": "bwroline",
        "description": "A Website Application **CREATED** to help self interest",
        "externalDocs": {
            "description": "Website Application to help self interest",
            "url": "https://j26067.deta.dev/",
        },
    },
]

description = """A website application **created** to help self interest"""

app = FastAPI(title="server.com", description=description, version="0.0.1", terms_of_service="use", contact={
    "name": "btghoa",
    "url": "http://bwroline.com/about/btghoa/",
    "email": "bwroline@gmail.com",
}, license_info={
    "name": "Apache 2.0",
    "url": "https://www.apache.org/licenses/LICENSE-2.0.html"
}, openapi_tags=BWAYA_metadata)


P = HTMLResponse(content="""<html><head><title>PROS-0-line.com</title></head><body><p>***PROS-0-line Home***</p></body></html>""", status_code=200)
bmu_ = HTMLResponse(content="""<html>
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
                                                hussein legal practitioners</a></em><br></a></p></pre></body></html>""", status_code=200)
bwr_ = HTMLResponse(content="""
<html><head><title></title></head><body><pre><em><ul><li><a href="server"><img src="https://bwroline.com/images/bwrolineImageSapi.com/bwroline.com/api/staticimage?size=70*30&makers=b.jpg" alt="server image"></img></a><font face="pyramid" color="blue"><p align="center">Abuja Gbagyi Media <br>F. C. T - Abuja<br>Since July 2018</font><br>Be and remain in touch with the things you've been missing out! Get all the interesting Dramas and Movies or videos you've desired to watch, that you can get in touch with the Gbagyi entertainment's trends like the <em><a href="shamudoents.com">shamudoents entertainments</a></em> across the globe likewise other trends... We make sure you are connected and remain connected with God and to be entertained by our religious traditions<em><a href="ecwagoodnewsbwr.com.com">ecwagoodnewsbwr.com</a></em>Download also your best and latest Musics available here <em><a href="btgees.com">btgees</a></em>You can get reach a legal practitioner for services<em><a href="ghlp.com">great hussein legal practitioners</a></em><br></a></p></pre></body>
</html>""", status_code=200)
shd_ = HTMLResponse(content="""<!DOCTYPE html>
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
ghl_ = HTMLResponse(content="""<!DOCTYPE html>
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
                    Housing Agent<br>And other Federation Legal obligations</font><p align="center"><br><font size= "6pt" color="saphire">We practice Justice and Loyalty!</font><br><font size= "6pt" color="green">Legal Greats Legal Practitioners The Desired Place For Hope</font><hr></br><p align="center"><font size="6pt">Tel:08033514288, 08023941762, 01-9521070</br>E-mail:greathusseinlegal@yahoo.com</font><br></br><br></body></html>""", status_code=200)
egb_ = HTMLResponse(content="""<!DOCTYPE HTML>
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
btg_ = HTMLResponse(content="""<!DOCTYPE HTML>
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
                            </html>""", status_code=200)


b0 = {
    "user_id": 1,
    "key": "server",
    "website": str(bmu_),
    "phone": "+2348120744800",
    "to": "",
    "acct_number": "0025531657",
    "size": None,
    "click": 0,
    "tags": {"server/server", "server/shamudoents.com", "server/ghlp.com",
             "server/greathusseinlegalpractitioners.com", "server/egb.com",
             "server/ecwagoodnewsbwr.com.com", "server/btgees.com"},
    "is_active": True,
    "target_url": [
        {
            "url": "https://bwroline.com/bpics/b.jpg",
            "name": "bwroline"
        },
    ],
    "name": BMU_Details.bwr
}
b1 = {
    "user_id": 2,
    "key": "shamudoents.com",
    "website": str(shd_),
    "phone": "",
    "bk": "",
    "size": None,
    "click": 0,
    "tags": {"server", "shamudoents.com"},
    "is_active": True,
    "target_url": {
        "url": "https://{name}.com/server/bpics/b.jpg",
        "name": "shamudoents.com"
    },
    "name": BMU_Details.shd
}
b2 = {
    "user_id": 3,
    "key": "great_hussein_legal_practitioners",
    "website": str(ghl_),
    "phone": "",
    "bk": "",
    "size": None,
    "click": 0,
    "tags": {"server", "ghlp.com"},
    "is_active": True,
    "name": BMU_Details.ghlp,
    "url_target": {
        "url": "https://{name}.com/server/bpics/b.jpg",
        "name": ["ghlp.com", "greathusseinlegalpractitioners.com"]
    },
}
b3 = {
    "user_id": 4,
    "key": "ecwa_goodnews_bwari",
    "website": str(egb_),
    "phone": "",
    "bk": "",
    "size": None,
    "click": 0,
    "tags": {"server", "egb.com"},
    "is_active": True,
    "url_target": {
        "url": "https://{name}.com/server/bpics/b.jpg",
        "name": "ecwagoodnewsbwr.com.com"
    },
    "name": BMU_Details.egb
}
b4 = {
    "user_id": 5,
    "key": "btgees",
    "website": str(btg_),
    "phone": "",
    "bk": "",
    "size": None,
    "click": 0,
    "tags": {"server", "btgees.com"},
    "is_active": True,
    "url_target": {
        "url": "https://{name}.com/server/{bpics}/{b.jpg}",
        "name": "btgees.com"
    },
    "name": BMU_Details.btgs
}

# bwroline data
bmu = BMU_Detail(**b0)
shd = BMU_Detail(**b1)
ghl = BMU_Detail(**b2)
egb = BMU_Detail(**b3)
btg = BMU_Detail(**b4)