from BMU.main import users
from fastapi import FastAPI
from starlette.responses import HTMLResponse
from starlette.requests import Request

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

# b = Deta("9c0cbf01-e710-43a9-9e94-ad74f93b082a")
# bdb = deta.Base("BWAYA")
# put_many(
# items: list,
# *,
# expire_in: int = None,
# expire_at: typing.Union[int, float, datetime.datetime] = None,
# )

app = FastAPI(
    title="server.com",
    description=description,
    version="0.0.1",
    # terms_of_service="",
    contact={
        "name": "btghoa",
        "url": "http://bwroline.com/btghoa/",
        "email": "bwroline@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html"
    },
    openapi_tags=BWAYA_metadata
)


@app.get("/")
@app.get("//")
@app.post("/server/{bwroline}/", tags=["bwroline"])  # do this edit to other routers
async def bwroline(request: Request):
    b = users.dict()
    return HTMLResponse("""<html>
    <head>
    <title></title></head>
    <body>
    <pre>
    <em>
    <ul>
    <li>
    <a href="server"><img src="https://bwroline.com/images/bwrolineImageSapi.com/bwroline.com/api/staticimage?size=70*30&makers=b.jpg" alt="server image"></img></a>
    <font face="pyramid" color="blue">
    <p align="center">
    Abuja Gbagyi Media <br>
    F. C. T - Abuja<br>
    Since July 2018</font><br>
    Be and remain in touch with the things you've been missing out! Get all the interesting Dramas and Movies or videos you've desired to watch, that you can get in touch with the Gbagyi entertainment's trends like the    <em><a href="shamudoents.com">shamudoents entertainments</a></em>    across the globe likewise other trends... We make sure you are connected and remain connected with God and to be entertained by our religious traditions    <em><a href="ecwagoodnewsbwr.com.com">ecwagoodnewsbwr.com</a></em>    Download also your best and latest Musics available here <em><a href="btgees.com">btgees</a></em>    You can get reach a legal practitioner for services    <em><a href="ghlp.com">great hussein legal practitioners</a></em>
    <br></a>
    </p>
    </pre>
    </body>
    </html>""", status_code=200)


@app.get("/shamudoents.com/{shamudoents}/")
@app.post("/shamudoents.com/{shamudoents}/")
async def shamudoents():
    return HTMLResponse("""<!DOCTYPE html>
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


@app.get("/ghlp.com/{great_hussein_legal_practitioners}/")
@app.post("/ghlp.com/{great_hussein_legal_practitioners}/")
async def great_hussein_legal_practitioners():
    return HTMLResponse("""<!DOCTYPE html>
    <html lang="en" dir="ltr">
        <head>
    <meta charset="utf-8">
        <title><a href="server">BWAYA MEDIA UNIT</a></title>
    </head>
        <body>
    <br>
    <img src="https://images.apis.com/bwroline.com/ghlp/images/api/staticimage?size=70*30&makers=9ja.jpg" alt="ghlp 9ja images"></img><font size="5pt"><h1 align="center">GREAT HUSSEIN LEGAL PRACTITIONERS</h1></font><img src="https://images.apis.com/bwroline.com/ghlp/images/api/staticimage?size=70*30&makers=bgl1.jpg" alt="ghlp bgl1 image"></img>
    <p align="center">
    <font size="5pt" color="brown">No. 4, Jibowu Close Off Ozulua Road<br>
    University Of Lagos Akoka<br>
    Yaba, Lagos
    </br></font>
    <hr>
    <p align="center">
    <img src="https://images.apis.com/bwroline.com/ghlp/images/api/staticimage?size=70*30&makers=bgl.jpg" width="200" height="70"></img>
    <img src="https://images.apis.com/bwroline.com/ghlp/images/api/staticimage?size=70*30&makers=bgl1.jpg" width="200" height="70"></img>
    <br>
    <font size="6pt" color="saphire">
    <p align="center">
    Greats Wild Legal Practitioners
    <font color="blue" size= "6pt">
    Yusuf Hussein, Esq 
    <br>
    Principal Counsel <br>
    Great-Hussein Legal Practitioners 
    <br></br>
    </font>
    <hr>
    <font color="golden-gold" size= "6pt">
    <p align="center">
    You are Welcome!
    <br>
    Here you shall find all the services for legal living in any part all over the world
    <br>
    </font>
    <hr>
    <p align="center">
    <font color="orange" size= "6pt">
    List of Our Services are:<br></b>
    </font>
    <font face="Sofadione">
    Legal Case Handle<br>
    Legal Law Enforcing<br>
    Legal Housing Agent<br>
    And other Federation Legal obligations
    </font>
    <p align="center">
    <br>
    <font size= "6pt" color="saphire">
    We practice Justice and Loyalty!
    </font>
    <br>
    <font size= "6pt" color="green">
    Legal Greats Legal Practitioners The Desired Place For Hope
    </font>
    <hr></br>
    <p align="center">
    <font size="6pt">
    Tel:08033514288, 08023941762, 01-9521070
    </br>E-mail:greathusseinlegal@yahoo.com
    </font><br></br>
    <br>
    </body>
    </html>
    """, status_code=200)


@app.get("/sundaysSermons/")
@app.post("/sundaysSermons/")
async def gbss():
    return [HTMLResponse("""<a href=ecwagoodnewsbwr.com.com"><img src="" alt="ecwa home"></img></a>""", status_code=200)]


@app.get("/boe/")
@app.post("/boe")
async def boe():
    return [HTMLResponse("""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head><title>BOARD OF ELDERS</title>
    <base href="C:\b\"/>
</head>
<body bgcolor="silver">
<br>
<i>Click
<br><a href="ecwagoodnewsbwr.com.com"><img src="https://images.apis.com/bwroline.com/ecwagoodnews.com/images/api/staticimage?size=70*30&makers=e.jpg", alt="ECWA LOGO"></img> 
<br><font size=4.5pt color="purple"></font>
</a><br>
logo to go back home</i><br>
<h1 align="center">
<font color="blue">
ECWA GOODNEWS CHURCH</font>
<br>
<font color="red" size="4.5pt">P. O. Box 95, Bwari Abuja</font></hr>
<br>
<p align="center">
    <font color="blue" size="4.5pt">BOARD OF ELDERS<hr>
</br>
<p align="center"><font size="5pt">CHAIRMAN<br>
REV. AUDU M. AUTA</br>
08157572405, 08028732540<br></br>
<br>
VICE CHAIRMAN<br>
PST MISHAK JUDE<br>
07036684272, 07085208723
</br>
<br>
EVANGELISM<br>
<br>
ELDER ISRAEL MUSA</br>
08065203227
</br>
<br>
SERVICE SECRETARY<br>
<br>
ELDER  EMMANUEL KEFAS
</br>
08066008921, 08071338010
</br>
<br>
SECRETARY<br>
ELDER SHEYIN NUHU<br>
08024502307, 08067550084
</br>
<br>
WELFARE<br>
ELDER VICTOR YEPWI<br>
07036156860
</br>
<br>
MAINTENANCE
<br>
ELDER MAHDI S. SETH
<br>
08050421672
</br>
<br>
FINANCIAL SECRETARY<br>
<br>
ELDER SAMUEL EMMANUEL
<br>
08170792709
</br>
<br>
TREASURER
<br>
ELDER AMOS MUSA
</br>
<br>
08035909289
</br>
<br>
ZONAL FELLOWSHIP
<br>
ELDER ALFRED POLOK
<br>
08065359358
</br>
<br>
</font>
</br>
</th>
</font></hr>
</body>
</html>

""", status_code=200)]


@app.get("/pfftw/")
@app.post("/pfftw/")
def pfftw():
    return [HTMLResponse("""<!DOCTYPE html public>
<html>
<head><title>ECWA GOODNEWS BWARI PRAYER FOCUS FOR THE WEEK</title>
</head>
<body>
    <i>Click
        <a href="ecwagoodnewsbwr.com.com">
            <img src="https://images.apis.com/bwroline.com/ecwagoodnews.com/images/api/staticimage?size=70*30&makers=e.jpg", alt="ECWA LOGO"></img> 
            <br><font size=4.5pt color="purple"></font></a>
            Logo to go back home</i>
<p align="center">
    <b>
        <font color="blue" size="6pts" type="gothic">PRAYER FOCUS FOR THE WEEK</font>
    <font size="5.5pts">
        <br><br>
        MONDAY<br>
        Praise God for His ability and strength expressed in and through you everyday of your life.<br><br>
        TUESDAY<br>
        Give glory to God for saving you and providing your daily needs.<br><br>
        WEDNESDAY<br>
        Thank God for choosing you to be a worshipper and sarvant of His.<br><br>
        THURSDAY<br>
        Pray for the salvation of souls in within the country and abroad.<br><br>
        FRIDAY
        Ask God to help you to always become conscious of His holiness.<br><br>
        SATURDAY<br>
        Prayer for our country, Nigeria and our many brethren in diaspora.<br>
    </font>
    </b>
</p>
<br>
</body>
</html>
""", status_code=200)]


@app.get("/woma/")
@app.post("/woma/")
def woma():
    return [HTMLResponse("""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
        "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
    <title></title>
    <base href="C:\b\"/>
</head>
<body bgcolor="gray">
<br>
<i>Click
    <br><a href="ecwagoodnewsbwr.com.com">
    <img src="https://images.apis.com/bwroline.com/ecwagoodnews.com/images/api/staticimage?size=70*30&makers=e.jpg", alt="ECWA LOGO"></font>
    </a>Logo to go back home</i><br></br> 
<H1 align="center" ><b>
<font color="blue">
ECWA GOOD NEWS</font>
<br>
<font size="5pt" color="red">P. O. Box 95, Bwari Abuja</font>
<p align="center">
    <b>
    <font color="gold" size="5pts">
    Church Weekly and Fellowship Activities
    </font>
    <hr>
    <p align="center">
        <font size="5pts">
    <br>
    SUNDAY
    <br>
    Sunday School ----- 8:00 - 9:00am
    </br>
    <br>
    MONDAY
    <br>
    Family home day
    </br>
    <br>
    Drama Rehearsal ----- 5:00 - 7:00pm
    </br>
    <br>
    TUESDAY
    <br>
    Men Fellowship ----- 5:00 - 6:30pm
    </br>
    <br>
    Women Fellowship ----- 4:00 - 6:00pm
    </br>
    <br>
    Youth Fellowship ----- 5:00 - 6:30pm
    </br>
    <br>
    WEDNESDAY
    <br>
    Prayer meeting ----- 5:00 - 6:30pm
    </br>
    <br>
    Band ----- 6:30 - 8:00pm
    </br>
    <br>
    THURSDAY
    <br>
    Bible studies ----- 6:30 - 8:00pm
    </br>
    <br>
    FRIDAY
    <br>
    Women Choir ----- 4:00 - 6:00pm
    </br>
    <br>
    Boys/Girls Brigade ----- 4:00 - 5:30pm
    </br>
    <br>
    Youth Fellowship ----- 5:00 - 6:30pm
    </br>
    <br>
    Prayer Band ----- 5:00 - 6:30pm
    </br>
    <br>
    Evangelism ----- 4:00 - 6:00pm
    </br>
    <br>
    Children Fellowship ----- 5:00 - 6:30pm
    </br>
    <br>
    Choir practice ----- 5:30 - 700pm
    </br>
    <br>
    Preparatory Class ----- 6:00 - 7:00pm
    </br>
    <br>
    SATURDAY
    <br>
    Good news Band --- 6:30 - 8:00pm
    </br>
    <br>
    Teenagers Ministry ----- 4:30 - 6:30pm
    </br>
    <br>
    Discipleship (Interdenominational) ----- 2:00 - 4:00pm
    </br>
    <br>
    Choir practice ----- 4:30 - 6:00pm
    </br>
    <br>
    Drama Rehearsal ----- 5:00 - 7:00pm
    <br>
    </font>    
<p align="center">
<font size="5pt" color="gold">
CHURCH MONTHLY PROGRAMS
</font>
<hr>
<br>
<font size="5pt">
<li align="center">First Sunday of every month is couple's forum/Child dedication</li>
<br>
<li align="center">Second Sunday of every month is selected for Zonal Bible studies in our various zones</li>
<br>
In order to locate your zone through by your zonal leader, click <a href="egbzl.html">ZONAL LEADERS</a>
<br>
<li align="center">Third Sunday of every month is single's forum and men's fellowship monthly evangelism</li>
<br>
<li align="center">Last Sunday of every month is Holy Communion and prayers for the monthly babies</li>
<br>
<li align="center">Every Sunday 2pm is Baptismal class</li>
<br>
<li align="center">Discipleship is every last Tuesday of the month</li>
<br>
<li align="center">Every first day of the month prayer from 6:00am - 7:00am</li>
<br>
<li align="center">Any intending couple should see the marriage committee six months ahead of time before the proposed month for the wedding@<a href="intendCoup.html">Intending Couple</a></li>
<hr><br>
</br>
</body>
</html>
""", status_code=200)]


@app.get("/cpfq/")
@app.post("/cpfq/")
def cpfq():
    return [HTMLResponse("""""", status_code=200)]


@app.get("/ecwagoodnewsbwr.com/{EGB}")
@app.post("/ecwagoodnewsbwr.com/{EGB}/")
async def ecwagoodnewsbwr():
    return HTMLResponse("""<!DOCTYPE HTML>
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


@app.get("/foodOrder/")
@app.post("/foodOrder/")
async def foodOrder():
    return [HTMLResponse("""<!DOCTYPE html>
<html>
<head><title> ORDER LIST ITEMS </title>
</head>
<body bgcolor="silver">
<br>
<a href="btgees.com" target="_parent">
<img src="C:\b\bpics\b.jpg" height=75 width=100></img><br>
<font color="gold">  Home btgees  </font>
</a><b><hr>
<p id="c">
Make order of lists for items of your choice<br>
<img src="C:\b\bpics\sj1.jpg" height="200" width="280"></img><br>
Make your good wise choice order for foods and or also fashion
<br>
LIST OF OUR FOODS ITEM<br>
</br>
<form>
    <p id="c">
Order Food Items:<br>
Meat Pie  
<input type="checkbox" name="Meat Pie" action=""><br>
Fish Roll  
<input type="checkbox" name="Fish Roll" action=""><br>
Sausage Roll
<input type="checkbox" name="Sausage Roll" action=""><br>
Doughnut
<input type="checkbox" name="Doughnut" action=""><br>
Cake  
<input type="checkbox" name="Cake" action=""><br>
Cookies  
<input type="checkbox" name="Cookies" action=""><br>
Egg Roll  
<input type="checkbox" name="EggRoll" action=""><br>
Chin - Chin
<input type="checkbox" name="Chin Chin" action=""><br>
Ham - Burger  
<input type="checkbox" name="Ham Burger" action=""><br>
Shawarma  
<input type="checkbox" name="Shawarma" action=""><br>
Bread Roll  
<input type="checkbox" name="Bread Roll" action=""><br>
Chicken and Chips  
<input type="checkbox" name="Chicken Chips" action=""><br>
Barbecue Fish Chicken  
<input type="checkbox" name="Barbecue Fish Chicken" action=""><br>
<input type="button" value="submit" name="Food Item" action="">
</input><br></br>
Cloth Items:<br>
Agbada (Big cloth):<br>
For men<input type="checkbox" name="Agbada for men" action=""><br>
For women<input type="checkbox" name="Agbada for women" action=""><br>
<input type="button" value="submit" name="Cloth Items" action=""><br>
God is our inspiration</font>
<br>
<a href="popsj.com">  <font color="rainbow">  Home ceefdee  </font></a></b></p>
</form>
<br>
</body>
</html>""", status_code=200)]


@app.get("/popsj.com/")
@app.post("/popsj.com/")
async def carter():
    return [HTMLResponse("""<!DOCTYPE html>
<html>
<head>
    <title>btgees-ceefdee snacks</title>
</head>
<body bgcolor="fade-gray">
<b>
<br>

<font size="4pt" color="gold">
<h1 align="center"><a href="server">
<img src="https://images.apis.com/bwroline.com/bwroline.com/images/api/staticimage?size=70*30&makers=b.jpg" height=60 width=100 alt="BMU Logo"></img><br>
Home btgees</a></font></h1><br>
<p align="center">
PRINCE OF PEACE<br>
<font size="10pts">SNACKS JOINT</font>
<br>
<font size="8pts" color="blue">Daniel Olayinka</font>
<br>
<font color="brown" size="6.5pts">The manager Head Office:<br>
Nigerian Law School,  Opp. Hostel D.<br>
Bwari - Abuja.
</font><br>
<font size="7pt">
The world of favorites
<br>
<hr>
<p align="center">
<font color="brown"> Eateries</font>
<br>
<img src="https://images.apis.com/bwroline.com/popsj.com/images/api/staticimage?size=70*30&makers=sj1.jpg" width="300" height="200">  </img>
<img src="https://images.apis.com/bwroline.com/popsj.com/images/api/staticimage?size=70*30&makers=sj3.jpg" width="300" height="200">  </img>
<img src="https://images.apis.com/bwroline.com/popsj.com/images/api/staticimage?size=70*30&makers=sj2.jpg" width="300" height="200">  </img>
<br></br>
<p align="center">
<font color="green">Order good foods and also aid able nourishing snacks that will quench your taste for another kinds<br>
<font color="red">We make mass made for occasional use, snacks such as</font>
<font color="emerald" size=7pt>
<ol>
<li>Meat pie</li>
<li>Egg Rolls</li>
<li>Fish roll</li>
<li>Donut/Doughnut</li>
<li>Cakes</li>
</ol>
</font>
<br>
<p align="center">
<a href="foodOrder" target="_blank">Order food item</a>
<hr>
<br></br>
<p align="center">
Our eateries are edible and well satisfactory to everyone nation wild and internationally reliable.<br>
</br>
Good cooked foods, nourishing snacks and also, other ceremonial event services.<br>
Love fashions!!<br>
Go  <a href="btgsfd.com" target="_blank">  bee tees fashions and designs  </a>
<br></br>
<p align="center">
ALL ON AFFORDABLE PRICES!<br>
<font color="red">We pay services Home and Abroad </font>
<br>
As you are highly welcome</br>
God is our inspiration</p><br>
<br></br>
</body>
</html>
""", status_code=200)]


@app.get("/btgsfd.com/")
@app.post("/btgsfd.com/")
async def btgfd():
    return [HTMLResponse("""<!DOCTYPE html>
<html>
<head>
    <title>btgees-fashion and design</title>
    <link rel="stylesheet" type="text/css" href="b.css"/>
</head>
<body bgcolor="pale-brown">
<a href="btgees.com"> <font color="gold">
    <p align="left">
        <img src="C:\b\bpics\b.jpg" width="98" height="45" alt="btgs home"></img><br>  Home btgees  </font></a>
<br>
<font size="5.5pt">
    <p id="">
Watch out the latest of some best quality fashioned designed stocks of your choice And we make sure we do our best to give offer and deliver the bests to your door watch...<br>
Make your order direct and very simple here as you 

<a href="foodOrder" target="_blank"> make Order </a>    of your choice     

<br></br>
<img src="C:\b\bpics\fsh.jpg"  height=180 width=300></img>
<img src="C:\b\bpics\fsh1.jpg" height=180 width=300></img>
<img src="C:\b\bpics\fsh2.jpg" height=180 width=300></img><br>
</br>
<li align="center">--Good and quality designed materials--</li>
<li align="center">--Latest fashion design--</li>
<li align="center">--Already made wears--</li><br>
<p id="index10" align="center">
Make it easy as you've found it easy to make your lists order direct  from here too!<br></br>

<a href="popsj.com" target="_blank">Best Carter</a>
<br></br>
Order good quality fashion designs likewise, your good meals<br></br>
What are they? Make good order of your choice live...<br>
<img src="C:\b\bpics\sj2.jpg" height="150", width="300"></img>
<img src="C:\b\bpics\sj4.jpg" height="150", width="300"></img>
<img src="C:\b\bpics\sj1.jpg" height="150", width="300"></img>
<br></br>
<li align="center">--Good cooked foods--</li>
<li align="center">--Nourishing snacks--</li>
<li align="center">--Ceremonial event services--</li><br>
<p align="center">
All at Affordable Prices<br>
</font>
<br>
</br>
</body>
</html>""", status_code=200)]


@app.get("/nja.com/")
@app.post("/nja.com/")
async def nja():
    return [HTMLResponse("""<!DOCTYPE html>
<html>
<head>
    <title></title>
    <base href="C:\b\"/>
</head>
<body>
<br></br><b>
<h1 align="center">
<a href="btgees.com"> 
BEE~TEE GEES ROCKS THE GLOBE MUSIC
</a>
<hr>
<font size="4.5pt">
<p align="center">
<br>
Our music goes home and away We represent the home away
<br>
<img src="C:\b\bpics\b2.jpg" height="150" width="240"></img>
<img src="C:\b\bpics\9ja.jpg" height="150" width="230"></img>
<img src="C:\b\bpics\njabtgs.jpg" height="150" width="240"></img><br>
<hr>
<p align="center">
Find here the old skool and the latest naija jams on net for free download
</font>
<br>
<font size="4pt" color="gray">
<p align="left">
<a href="">   </a>
<br>
</font>
</body>
</html>
""", status_code=200)]


@app.get("/frgn.com/")
@app.post("/frgn.com/")
async def frgn():
    return [HTMLResponse("""<!DOCTYPE html>
<html>
<head>
    <title>foreign-btgees</title>
    <base href="C:\b\"/>
</head>
<body bgcolor="brilliant-emerald">
<b>
<h1 align="center">
<a href="btgees.com"> 
BEE~TEE GEES ROCKS THE GLOBE MUSIC
</a> 
<br>
<hr>
<font size="4.5pt">
<p align="center" id="frgn">
Our music goes home and away<br>
We represent the home away<br>
Welcome to the home site where you'll have to find more of the foreign jams from no where than here...<br>
</br>
<img src="C:\b\bpics\frgn1.jpg" height="150" width="300"></img>
<img src="C:\b\bpics\frgn3.jpg" height="150" width="300"></img>
<img src="C:\b\bpics\frgn2.jpg" height="150" width="300"></img>
<br></br>
...On this page you'll find the tracks and the hit music that rocks<br>
</br>
A place for other music round the World
<hr>
<p align="left">
<font color="gray" size="5pt"><i>
<a href="frgn.com">
Raps</a><br>
<a href="bll.com">Blues</a>
<br>
<a href="mp3.com">Mp3s</a>
<br>
<a href="frgn.com" target="_self">All Foreign jams</a>
</i>
</font><br>
<font size="7pt">
<p align="center">
Have A Happy download</p>
</br>
<br>
</br>
</body>
</html>
""", status_code=200)]


@app.get("/njarege.com/")
@app.post("/njarege.com/")
def njarege():
    return [HTMLResponse("""<!DOCTYPE html>
<html>
<head>
    <title>raggae btgees</title>
</head>
<body>
<br>
<h1 align="center">
<font -family="stream">
<a href="btgees.com"> BEE~TEE GEES ROCKS THE GLOBE MUSIC
</a></font>
<br></br>
<p align="center">
<font size="4.5pt">
Our musics goes home and away<br>
<img src="C:\b\bpics\rg2.jpg" width="200" height="200"></img>
<img src="C:\b\bpics\rg1.jpg" width=200 height=200></img>
<img src="C:\b\bpics\rg3.jpg" width=200 height=200></img>
</br>We represent the home away
<br>
<font color="melon">
mp3 free download at  
<a href="btgees.com">  btgees mp3</a><br>
On this page you find the Raggae musics of the world that rocks</font>
<br>
<a href="njarege.com" target="_self">Raggae beats</a>
</br>
</body>
</html>
""", status_code=200)]


@app.get("/oldskl.com/")
@app.post("/oldskl.com/")
def oldskl():
    return [HTMLResponse("""<html>
    <head><title>oldsklbtgs</title>
    <base href="C:\b\"/>
</head>
<body>
    <h1 align="center">
        <a href="btgees.com">BTGEES ROCKS OLD SCHOOLS</a>
    </h1>
    <hr>
    <p align="left">
        <font size="4.5pt">
    <a href="oldskl.com" target="_self">The ever blues jams</a><br>
    <a href="njarege" target="_self">The reggae of before and the present still on...</a><br>
</body>
</html>""", status_code=200)]


@app.get("/mp3.com/")
@app.post("/mp3.com/")
async def mp3():
    return [HTMLResponse("""<!DOCTYPE html>
<html>
<head>
    <title>mp3btgees</title>
</head>
<body bgcolor="gray">
<br>
<h1 align="center">
<font -family="stream">
<a href="btgees.com">
BEE~TEE GEES ROCKS THE GLOBE MUSIC
</a></font>
<hr></hr>
<p align="center">
<font size="4.5pt">Our music goes home and away<br>
</br>We represent the home away
<br>
<img src="C:\b\bpics\mp1.jpg" width=300 height=200></img>
<img src="C:\b\bpics\mp3.jpg" width=300 height=200></img>
<img src="C:\b\bpics\mp2.jpg" width=300 height=200></img>
<br>
Get your lovely mp3 collections and keep loving them on...<br>
<font family="bold-italic"  color="blue">mp3gees Old Skool   </font><br>
<a href="btgees.com" >
btgees</a><br>
<br>
Enjoy happy downloads
<br>
</body>
</html>
""", status_code=200)]


@app.get("/bbl.com/")
@app.post("/bbl.com/")
async def bbl():
    return [HTMLResponse("""<!DOCTYPE html>
<html lang="utf-8">
<head>
    <title>http://bluesbtgs.com</title>
    <base href="C:\b\"/>
</head>
<body bgcolor="brilliant-saphire">
<br><b>
<h1 align="center"><font face="stream">
<a href="btgees.com">BEE~TEE GEES ROCKS THE GLOBE MUSIC</a></font>
</br>
<hr>
<p align="center">
<font size="4.5pt">
Our musics goes home and away We represent the home away
<br>
<img src="C:\b\bpics\blbtg.jpg" width="200" height="240" alt="blues btgees"></img><br>
Get your kool R&B mp3 collections and keep loving them on<br>
<i color="blue">mp3gees kool blues</i><br>
<p align="left">
<a href="mp3.com" target="_self">    Mp3    </a><br>
<a href="oldskl.com" target="_self">    Old 60s mp3    </a><br>
<a href="njarege.com" target="_self">    SmooANDCoo Reggae mp3    </a><br>
<hr>
<p align="center">
</hr>
</font>
<br>
<font size="4pt">
<p align="center">
Happy enjoy downloading the cool musics of your choice...
<br>
</body>
</html>""", status_code=200)]


@app.get("/bvids.com/")
@app.post("/bvids.com/")
async def bvids():
    return [HTMLResponse("""<!DOCTYPE html>
<html>
<head><title>Videos</title>
</head>
<body>
<font size="7pt">
<p align="center">
</body>
</html>""", status_code=200)]


@app.get("/btgees.com/")
@app.post("/btgees.com/")
async def btgees():
    return [HTMLResponse("""<!DOCTYPE HTML>
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
    </html>""", status_code=200)]


@app.get("/btghoa/")
@app.post("/btghoa/")
async def btghoa():
    return [HTMLResponse("""<!DOCTYPE html>
<html>
<head>
    <title>btgees head-office address</title>
	<base href="C:\b\"/>
</head>
<body><b>
<p align="center">
    <font size="5.5pt" color="gray">
    bee~ tees Bwari</br>
clone of the <a href="index.html">server</a><br><hr>
<p align="center">
Head 01.<br>
<br>
PROSOline Multi-Links Global Communications<br>
<br>
For enquiry Contact The <font size="4.5pt", color="crystal">DIC @</font>dic.bwroline@gmail.com</a><br>
Flat No. 01, Dakoyis Compound No. 01.<br>
Off Dara Street,<br>
Behind Science Primary School, Bwari<br>
Abuja- F. C. T<br>
Nigeria.
</hr>
<br></br>
ECWA Good News Church Abuja Bwari<br>
P. O. Box 95,<br>
<br>
Bwari.<br>
<br>
Abuja-F. C. T<br>
<br>
Nigeria</a><br>
<br>
Email: ecwagoodnewsbwr.com.egb@gmail.com<br>
For visit to Church! Go: <a href="index3.html">ecwabwr.com</a><br>
<br>
District 211,<br>
Off Dara Street<br>
Behind Central Primary<br>
Bwari<br>
Abuja<br>
Phone: (+234)-(0)8076726468 or<br>
+2348120744800<br>
<br>
<br>
</body>
</html>
""", status_code=200)]
