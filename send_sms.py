import vonage

client = vonage.Client(key="2ef2f8fb", secret="cEVxNqoqw7bhn0hp")
sms = vonage.Sms(client)
responseData = sms.send_message(
    {
        "from": "Vonage APIs",
        "to": "919840102307",
        "text": "Warning, you have violated a traffic rule(jumping a red signal)",
    }
)

if responseData["messages"][0]["status"] == "0":
    print("Message sent successfully.")
else:
    print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
