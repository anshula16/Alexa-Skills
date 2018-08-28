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
    if intentName == "whatischocolate":
        return chocoland_fact(intent, session)
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
    speechOutput =  "Hello , Welcome to Choco FACT-ory! " \
                    "You can know interesting facts about Chocolates by saying Tell me facts about chocolates"
    repromptText =  "You can know interesting facts about Chocolates by saying Tell me facts about chocolates"
    shouldEndSession = False
    
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def chocoland_fact(intent, session):
    import random
    index = random.randint(0,len(chocolate)-1)
    cardTitle = intent['name']
    sessionAttributes = {}
    speechOutput = chocolate[index]
    repromptText = "You can know interesting facts about Chocolates by saying Tell me facts about chocolates"
    shouldEndSession = True                   
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def handleSessionEndRequest():
    cardTitle = "Session Ended"
    speechOutput = "Thank you for using Choco FACT-ory Alexa Skills Kit. " \
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



chocolate = ["There is a correlation between the amount of chocolate a country consumes on average and the number of Nobel Laureates that country has produced." ,
          "At one point the Nazis plotted to assassinate Winston Churchill with an exploding bar of chocolate." ,
          "The scientific name for the tree that chocolate comes from, Theobroma cacao, means food of the gods.",
          "Chocolate has over 600 flavor compounds, while red wine has just 200." ,
          "In fact, chocolate was consumed as a liquid, not a solid, for 90% of its history." ,
          "During the Revolutionary War, soldiers were sometimes paid in chocolate." ,
          "Hershey's Kisses got their name from the kissing sound the machine that deposits the chocolate on the conveyor belt makes.",
          "The inventor of the chocolate chip cookie, Ruth Wakefield, sold her cookie recipe to Nestle in exchange for a lifetime supply of chocolate." ,
          "German chocolate cake has nothing to do with Germany. It's named after its inventor, Sam German." ,
          "M&Ms were created in 1941 as a means for soldiers to enjoy chocolate without it melting." ,
          "Chocolate can sicken and even kill dogs.",
          "Kit Kat is produced worldwide by Nestle, except in the U.S. where their competitor, Hershey makes them." ,
          "White Chocolate is not technically Chocolate, as it contains no cocoa solids or cocoa liquor. White chocolate contains cocoa butter instead." ,
          "Dark chocolate may improve blood flow and lower blood pressure.",
          "It takes about a year for a cocoa tree to produce enough pods to make about 10 small-sized chocolate bars.",
          "Chocolate Was a Form of Currency in the Mayan Times",
          "The Chocolate Chip Cookie Was Invented by Accident",
          "There are Actually Four Different Types of Chocolate: Dark, Milk, White, and Blond",
          "The First Chocolate Bar was Invented in 1847 by Joseph Fry",
          "The French Celebrate April Fools Day with Fish-Shaped Chocolate" ,
          "Snickers is Actually Named After a Horse" ,
          "Eating dark chocolate everyday reduces the risk of heart disease by one third."
        ]
