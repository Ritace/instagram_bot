
#id = cl.media_pk_from_url("https://www.instagram.com/reel/Cv4z6oPNRs6/")
from instagrapi import Client
import json
import pickle
import os
import openpyxl
cl = Client()
cl.delay_range = [1, 7]
credens = {
    "type": "service_account",
    "project_id": "redditbot-363109",
    "private_key_id": "a07629ebcbcecc27e45de1d21e72e065d2f4205a",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDZ+QeKSHucxFTJ\nAhnGyvAaKq0JGejU5D1W8ESt5slAUBVP0JL6p0yMJlcPepveD86DtcQdrO48BfMv\nzJrE0DWpeIi1/qFaG62L+o30p2dtCLqBewzd2pZ2bEPZfyTa+NJU2QzGE9yjiB6B\nEzkLIvYKtNmdHVH/seaSzkXNOgbSXfwKbWbGBmLfuKFLAxWy2jGBUqX1sZaSYRIx\nnlnhvz/cCF8EogIqGYhYs8TK30oUq9Z4Q4LmHauBUbQba+Ga2X29su/KITph/Hg5\nXSs4kiNv/xGX1DUED9/nlevpSXMhNnu0Y8lJAwwp9husRHoL7CJ91QirUf+kms9R\nNHUA5xqNAgMBAAECggEABfSCSrphOi64/Ebk6mP3/FcHJDUDgfF8ZYgp8DBadjnZ\n4zTZFyUD995CSad5Y6893qZUJdVoKtakxr0Jy2++z5L99S7wPJR+ANGHGFSMhFOV\nON1iRBtpOfIKRoJtQNhEctH9QdogEI2y+6bJS68YVsGLIno/F8PF/2PIT2uS7SNc\nSvEVGA8GT/BqQP5UPiSjEtLw6mtF0hPcmpVsMjGwH+v8PMHKGohHxCUb8QrnxrMj\nZncGzNkb5KLcNwKBrLQBiCvWJTkB69NeUuBaaJfRiyS1BMobe3xonxQNR6C0C8IH\nW1x8R1iO0GUVTQoSsmbnsgAoXTKr1Mf107t32RT0wQKBgQDw/jOHz2QsrIUghAyQ\nQQIF5M+wdGZfRZHOfWXIGv2DCc7dtrUIQhp+HPtPdTbhXFdGwBpypOq7Mt1SOeqH\nrnzUd7IhGNknFHdkB4A5s1OPvTmS91O+Rde0vI+1xz+qnopaRSTMXqc3Ng+3yLbn\nx/FcOXOX+BjVruUjsd0+vJ73bQKBgQDni9nJEVp0r6FIGZd6ubUcLOqC7duWnZDB\n9dfy10mFHbNevaiCnhgEqvltzn7B2d7gjtm+tE7te733GIUK075+yLPpfgCjTehI\nj48fkRQ8fOeklnm0fuVw8U7vegr5RWVpgrajuNcyrkjx2OtUkxpJdjqkMUCYM6X/\nvJvUUgkboQKBgQDQ9urB2W/4WMO61SV7tBLH/4ajb9sQw2dR0GQAJn8qL8gDchj5\nhzAnqIO1e2LR+Nroy0xjmmK7XbiRQwz9B6zQItX/Yudwvotj3ikuXzOW0LJqoDEq\nLK+E1XgbXCD1ljFLYucsmuqNsj/g0Zbf1fyQRnTYElWee9/OmrzIWI/S5QKBgFxX\nEYt2ODTAtfki+54d4XRTFVMRuLjgLZKskGpwIQnNRnNJ/6HXmoyCAucfqr10PcYg\nMgYzsiZTavbX+HbQ6u906wr7DRYTQ8dsOQ/Fs+RLi7W/rNmmoanhEjG+4hF283KY\nhm3UkT3M85o/f9pCsAEL/WbtnW0Va+YJObv621cBAoGAcObi0XZxuqVhsCwGTU7V\nu/uORsf1E0LuXeLzNiMBoO84UMhxc+mFO1nurV0RqZ6wAyOELsHJIpWoueSJTWRl\nqw0wQ6y6UTvagGgzC+88SD7jRhJaBrnjsa9IDO98qzfgw/Oxb17611HUiaW/aNUl\nrXOuHaX8vHWS6dCNuvm+7qc=\n-----END PRIVATE KEY-----\n",
    "client_email": "joyfulbot@redditbot-363109.iam.gserviceaccount.com",
    "client_id": "105153036553319946005",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/joyfulbot%40redditbot-363109.iam.gserviceaccount.com"
}
ACCOUNT_USERNAME = "ritacethapa13"
ACCOUNT_PASSWORD = "Killforweeds@13"  
try:
  cl.load_settings("session.json")
  print("already logged in session file loaded")
except:
  print("not logged in session file not loaded")
  cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)

  print("loggin in successful")
  cl.dump_settings("session.json")

from services import  given_reel_code_get_info, print_json, add_competetor
#info = given_reel_code_get_info(cl,"Cv7rGwvqFk4")
#add_competetor(info["user"]["pk"],info["user"]["full_name"])
from services import get_channel_reels

if os.path.isfile("competitor/competitor_list.pkl"):
  competitor_list = pickle.load(open("competitor/competitor_list.pkl", "rb"))
import gspread
import pandas as pd
temp_user_clips = []
for id in competitor_list.keys():
  user_clips = get_channel_reels(cl,"2023-08-26",id)
  for clip in user_clips:
    dict_clip = clip.dict()
    temp_user_clips.append({"video_duration":dict_clip["video_duration"],
                            "name":dict_clip["user"]["full_name"],
                            "play_count":dict_clip["play_count"],
                            "caption_text":dict_clip["caption_text"],
                            "taken_at":str(dict_clip["taken_at"]),
                            "url":"https://www.instagram.com/p/"+dict_clip["code"]+"/",
                            "like_count":dict_clip["like_count"],
                            "comment_count":dict_clip["comment_count"]
                            })
df = pd.json_normalize(temp_user_clips)

gc = gspread.service_account_from_dict(credens)
sheets = gc.open_by_key('1UR-Lpp9KYnSD7ah3qhLL4NjMnHzmqDiwpMp71ggyBAg')
sheet = sheets.worksheet("Instagram_Competetor_Videos")
sheet.update([df.columns.values.tolist()] + df.values.tolist())


