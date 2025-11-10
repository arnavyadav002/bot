import requests

# base_url = "https://api.telegram.org/bot7856234649:AAHBv9W4q_NEkRtZ0que606X6eti_TbQPkE"   FOR PUSH TO GITHUB



def read_msg():

  parameters = {
      "offset" : "470695239"
  }

  resp = requests.get(base_url + "/getUpdates", data = parameters)
  data = resp.json()

  for result in data["result"]:
    if "hi" in result["message"]["text"]:
      send_msg()


def send_msg():
  parameters = {
      "chat_id" : "-4802805386",
      "text" : "Hello !!!"
  }

  resp = requests.get(base_url + "/sendMessage", data = parameters)
  print(resp.text)



read_msg()
