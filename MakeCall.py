from twilio.rest import Client as Call

class MakeCalls:
    def CallUser():
        client = Call("<>","<>")
        From_number = "<>"
        To_number = "<>"
        # Src_path = "http://localhost:63342/hopeless_2/response.xml"
        Src_path = "http://demo.twilio.com/docs/voice.xml"
        # Src_path = "http://www.vothla.com/Twilio_Demo.xml"
        print("Call Intiated")
        client.calls.create(to=To_number,from_=From_number,url= Src_path,method = 'GET')
        print("Call Completed")


    def SendMessage(msg):
        client = Call("ACe6debefea0793a37c388b807abd01a9f","981649a2155c5d4243ae562a01ba3316")
        From_number = "+18316121429"
        To_number = "+919049084492"
        client.messages.create(
            to=To_number,
            from_=From_number,
            body=str(msg)
        )





# mc = MakeCalls
# mc.SendMessage("Hello")
