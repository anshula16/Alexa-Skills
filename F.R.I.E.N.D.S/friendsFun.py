import json

def lambda_handler(event, context):
    if event['request']['type'] == "LaunchRequest" :
        return onLaunch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest" :
        return onIntent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest" :
        return onSessionEnd(event['request'], event['session'])

def onLaunch(launchRequest, session):
    return welcomeuser()

def onIntent(intentRequest, session):
             
    intent = intentRequest['intent']
    intentName = intentRequest['intent']['name']
    if intentName == "friendsshow":
        return friends_fact(intent, session)
    elif intentName == "AMAZON.HelpIntent":
        return welcomeuser()
    elif intentName == "AMAZON.CancelIntent" or intentName == "AMAZON.StopIntent":
        return handleSessionEndRequest()
    else:
        raise ValueError("Invalid intent")

def onSessionEnd(sessionEndedRequest, session):
    print("on_session_ended requestId=" + sessionEndedRequest['requestId'] + ", sessionId=" + session['sessionId'])

def welcomeuser():
    sessionAttributes = {}
    cardTitle = " Hello"
    speechOutput =  "Hello , Welcome to FRIENDS! " \
                    "You can know interesting facts about FRIENDS show by saying Tell me facts about friends show"
    repromptText =  "You can know interesting facts about FRIENDS by saying Tell me facts about friends show"
    shouldEndSession = False
    
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def friends_fact(intent, session):
    import random
    index = random.randint(0,len(friend)-1)
    cardTitle = intent['name']
    sessionAttributes = {}
    speechOutput = friend[index]
    repromptText = "You can know interesting facts about FRIENDS by saying Tell me facts about friends show"
    shouldEndSession = True                   
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def handleSessionEndRequest():
    cardTitle = "Session Ended"
    speechOutput = "Thank you for using FRIENDS Alexa Skills Kit. " \
                    "Have a great time! "
    shouldEndSession = True
    return buildResponse({}, buildSpeechletResponse(cardTitle, speechOutput, None, shouldEndSession))

def buildSpeechletResponse(title, output, repromptTxt, endSession):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
            },
            
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
            },
            
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': repromptTxt
                }
            },
        'shouldEndSession': endSession
    }


def buildResponse(sessionAttr , speechlet):
    return {
        'version': '1.0',
        'sessionAttributes': sessionAttr,
        'response': speechlet
    }



friend = ["When Matt LeBlanc auditioned for the role he only had 11 dollars.",
        "Before the show was cast, the main love story was intended to be between Monica and Joey",
        "Gunther didn't have a name until the middle of the second season. Originally, he did not have a speaking part.",
        "The story line of Phoebe having her brother's babies was thought up when Lisa Kudrow announced her real-life pregnancy.",
        "Originally, Chandler and Phoebe were supporting characters.",
        "The orange couch used in Central Perk was found in the basement of the Warner Bros. studio.",
        "Season Two is the only season of Friends where there is no episode on Thanksgiving Day.",
        "Ellen DeGeneres had turned down the role of Phoebe.",
        "The show was originally called 'Insomnia Cafe'. It was then renamed 'Friends Like Us', and then 'Six of One'; before becoming Friends.",
        "Paul Rudd got the role of Mike after a casting director wrote \"dreamy\" in her notes.",
        "All the Friends have kissed each other except Monica and Phoebe.",
        "Courteney Cox is the only Friend to not receive an Emmy nod for her work on the show",
        "Gunther's first line came after 33 episodes, when he said \"yeah.\"",
        "Lisa Kudrow (Phoebe) used to be scared of the duck living in Chandler and Joey's apartment in the third season of the show.",
        "\"The One Where No One's Ready\" takes place entirely in Monica's apartment because the show didn't have a large enough budget for guest stars or additional sets.",
        "Phoebe's wedding is not attended by any of her relatives, including her twin sister Ursula, her father, her birth mother, her brother Frank Jr. or the triplets she gave birth to.",
        "Chandler was written as a character who was awkward around women because Matthew Perry told producers that he himself was.",
        "David Schwimmer was the first of the main six actors to be cast in the show.",
        "Jennifer Aniston was the last of the main six actors to be cast in the show.",
        "Courteney Cox had to film the scene in which Rachel has Emma just after having a miscarriage.",
        "Joey wasn't written as a dim character. Matt LeBlanc suggested it.",
        "When Lisa Kudrow first read the script, she thought Chandler's character was gay.",
        "In the last episode, it is mentioned that all six characters have lived in Monica's apartment. They have all also lived in Joey's apartment.",
        "When the last series ended, Jennifer Aniston and her then-husband Brad Pitt hosted a dinner party at their home. They served bottles of wine that producer Kevin Bright had saved from the first series.",
        "When the last series ended, each cast member was given a piece of the sidewalk from outside Central Perk as a keepsake.",
        "Joey and Chandler's big white dog actually belonged to Jennifer Aniston. A friend gave it to her as a good-luck gift when the show started.",
        "An average Friends episode took five hours to film.",
        "London radio stations revealed where filming was taking place and the cast were mobbed by fans.",
        "Ross's son doesn't appear at his wedding. He was in Carol and Susan's wedding in The One With The Lesbian Wedding.",
        "James Michael Tyler (Gunther) got the role solely because he was already working at a coffee shop and knew how to operate a coffee machine.",
        "The role of Ross was written for David Schwimmer.",
        "Episodes were filmed in front of a live studio audience, except for cliffhangers.",
        "Matthew Perry admitted to not remembering filming three seasons of Friends due to drugs. ",
        "Matthew Perry still calls Kathleen Turner \"Dad\" after she played his father on the show.",
        "The show's actual theme song, \"I'll Be There For You,\" by The Rembrandts, was on the Billboard Hot 100 charts for eight weeks in 1995.",
        "Courteney Cox is three years older than David Schwimmer, despite the fact that Monica is supposed to be three years younger than Ross."
        ]
