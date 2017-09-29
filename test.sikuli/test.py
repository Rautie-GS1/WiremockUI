def addServer(serverName, url, showAdvanced=False):
    rightClick("menuServer.png")
    click("menuAddServer.png")
    type("txtServerName.png", serverName)
    paste(Pattern("txtTargetUrl.png").exact().targetOffset(-6,11), url)

    if (showAdvanced):
        click("tabAdvanced.png")
        click("rowBindAddress.png")
        type(Key.PAGE_DOWN)
        type(Key.PAGE_DOWN)
        type(Key.PAGE_DOWN)
        wait(1)
        click("tabBasic.png")
        
    click("btnAdd.png")

def addMap(mapName, url, showJsonView, fileResponse, content):
    rightClick("itemServer1.png")
    click("menuAddMap.png")
    rightClick("menuMap.png")
    click("menuRename.png")
    type(mapName)
    type(Key.ENTER)
    doubleClick("itemGetAllUser.png")
    click(Pattern("jsonRequestUrl.png").targetOffset(8,1))
    paste(url)
    if (showJsonView):
        click("tabJsonView.png")
        click("tabRaw.png")
    click("btnSave.png")
    click("btnClose.png")
    doubleClick(fileResponse)
    click("txtResponseContent.png")
    type("a", KeyModifier.CTRL)
    paste(content)
    rightClick(Location(581, 207))
    click("menuJson.png")
    click("jsonFormat.png")
    click("btnSave.png")
    click("btnClose.png")

def duplicateMap(mapFrom, mapTo, fileResponse, mapName, content):
    rightClick(mapFrom)
    click("DuplicateCtr.png")
    rightClick(mapTo)
    click("menuRename.png")
    type(mapName)
    type(Key.ENTER)
    doubleClick(mapTo)
    doubleClick(fileResponse)
    click(Location(563, 226))
    type("a", KeyModifier.CTRL)
    paste(content)
    rightClick(Location(581, 207))
    click("menuJson.png")
    click("jsonFormat.png")
    click("btnSave.png")
    click("btnClose.png")

def startInChrome(url, server, view, chromeUrl):
    rightClick(server)
    click("start.png")
    click(view)
    click(chromeUrl)
    paste(url)
    type(Key.ENTER)
    wait(2)
    click("close.png")

def logViewContent():
    rightClick("NETIN.png")
    click("ViewContent.png")
    click(Pattern("closeViewContent.png").targetOffset(24,0))

def logWebRequest():
    rightClick("listener.png")
    click("OpeninWebReq.png")
    wait(1)
    click("execute.png")
    wait(1) 
    click(Pattern("webRequestClose.png").targetOffset(29,-3))


def callInWebRequest(map):
    if (map):
        rightClick(map)
        click("ViewinWebReq.png")
    click("execute.png")
    wait(2)

def toggleMap(map):
    rightClick(map)
    click("Enable.png")

def createPost(mapName, url, fileResponse, content):
    rightClick("itemServer1.png")
    click("menuAddMap.png")
    rightClick("menuMap.png")
    click("menuRename.png")
    type(mapName)
    type(Key.ENTER)
    doubleClick("itemGetAllUser.png")
    click(Pattern("jsonRequestUrl.png").targetOffset(8,1))
    paste(url)
    click(Pattern("methodGET.png").targetOffset(13,3))
    type(Key.DELETE)
    type(Key.DELETE)
    type(Key.DELETE)
    type(Key.DELETE)
    type("POST\",")
    click(Pattern("methodPOST.png").targetOffset(47,0))
    type(Key.ENTER)
    type("    \"bodyPatterns\" : [{\n         \"equalToJson\" : \"{\"Name\":\"User3\",\"Age\":60}\"\n     }]")
    click(Pattern("User3Ace60Na.png").targetOffset(-70,1))
    type(Key.END, KeyModifier.SHIFT)
    type(Key.LEFT, KeyModifier.SHIFT)
    type(Key.LEFT, KeyModifier.SHIFT)
    rightClick("NameUser3ae6.png")
    click("Json.png")
    click("Escape.png")    
    click(Pattern("NameUser3Age.png").targetOffset(-82,1))
    type(Key.END, KeyModifier.SHIFT)
    type(Key.LEFT, KeyModifier.SHIFT)
    type(Key.LEFT, KeyModifier.SHIFT)
    rightClick("NameUser3Aae.png")
    click("Json.png")
    click("Editvalue.png")
    click(Pattern("Qe60H.png").targetOffset(3,-1))
    type(Key.DELETE)
    type(Key.DELETE)
    type("100")
    click("btnReplace.png")
    click("btnSave.png")
    click("btnClose.png")
    doubleClick(fileResponse)
    click("txtResponseContent.png")
    type("a", KeyModifier.CTRL)
    paste(content)
    rightClick(Location(581, 207))
    click("menuJson.png")
    click("jsonFormat.png")
    click("btnSave.png")
    click("btnClose.png")
    
#addServer("server1", "http://www.g1.com.br")
#addMap("GetAllUser", "user/all", True, "responseGetAllUser.png", '[{"Name":"User1","Age":20},{"Name":"User2","Age":21}]')
#addMap("GetUser1", "user/1", False, "itemGetUser1.png", '{"Name":"User1","Age":20}')
#addMap("GetUser2", "user/2", False, "itemGetUser2.png", '{"Name":"User2","Age":50}')
##addMap("GetUser2-alternative", "user/2", False, "itemGetUserAlternative.png", '{"Name":"User2","Age":50, "otherAttribute": 10}')
#duplicateMap("user2GetUser-1.png", "user2GetUser-2.png", "GetUser2aite.png", "GetUser2-alternative", '{"Name":"User2","Age":50, "otherAttribute": 10}')
#createPost("InsertUser", "user/insert", "InsertUser.png", '{"status":"OK"}')
#startInChrome("http://localhost:5500/user/all", "server1.png", Pattern("view.png").targetOffset(268,4), Pattern("chromeUrl.png").targetOffset(47,-2))
#logViewContent()
#logWebRequest()
#callInWebRequest("user2GetUser.png")
#toggleMap("user2GetUser.png")
#callInWebRequest(None)
click("Tool.png")
click("ebRequest.png")
click("verbCombo.png")
click("POST.png")
click(Location(423, 96))
paste("http://localhost:5500/user/insert")
click(Pattern("BodyHeaderFi.png").targetOffset(-49,2))
click(Location(345, 169))
paste('{"Name":"User3","Age":60}')
rightClick(Location(390, 183))
click("menuJson.png")
click("jsonFormat.png")
click("execute.png")
wait(2)
click("Scenario1Sta.png")
rightClick("POSTuserinse.png")
click("Compare.png")
click(Location(1338, 86))
click("Selectinthet.png")
doubleClick(Pattern("userInsertns.png").targetOffset(-45,-5))
click("compare-1.png")
wait(4)