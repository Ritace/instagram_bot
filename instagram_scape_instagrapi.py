from instagrapi import Client
import json
import pickle
import os
import openpyxl
from datetime import datetime
import argparse
import subprocess
import time

def connect_to_vpn(config_path):
    try:
        # Start the OpenVPN process
        process = subprocess.Popen(['openvpn', config_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Connecting to VPN...")

        # Allow some time for the connection to establish
        time.sleep(10)  # Adjust as needed

        if process.poll() is None:
            print("Connected to VPN.")

            # Now you have a new IP address through the VPN
            # You can perform your tasks that require this IP here

        else:
            print("VPN connection failed. Check logs for details.")

        # Close the OpenVPN process
        process.terminate()

    except Exception as e:
        print("An error occurred:", e)

from services import get_channel_reels, get_df_for_files, given_reel_code_get_info
#cl = Client()
cl2 = Client()
cl3 = Client()
#cl.delay_range = [1, 7]
#cl2.delay_range = [1, 10]
cl3.delay_range = [1, 12]
ACCOUNT_USERNAME = "thapa.tarat2019"
ACCOUNT_PASSWORD = ""  
ACCOUNT_USERNAME2 = "ritacethapa13"
ACCOUNT_PASSWORD2 = ""  

ACCOUNT_USERNAME3 = "spare16access"
ACCOUNT_PASSWORD3 = "Seeker16@"  
#try:
#  cl.load_settings("session.json")
#except:
#  cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)
#  cl.dump_settings("session.json")
#
try: 
  cl2.load_settings("second_session.json")

except:
  cl2.login(ACCOUNT_USERNAME2, ACCOUNT_PASSWORD2)
  cl2.dump_settings("second_session.json")

try:
  cl3.load_settings("third_session.json")
except:
  cl3.login(ACCOUNT_USERNAME3, ACCOUNT_PASSWORD3)
  cl3.dump_settings("third_session.json")
def print_json(obj):
  print(json.dumps(obj, indent=4, sort_keys=True, default=str))
#id = cl.media_pk_from_url("https://www.instagram.com/reel/Cv_mx24PnpW/")
#info = cl.media_info(id).dict()
#print(json.dumps(info, indent=2, sort_keys=True, default=str))
def get_sadhguru_reels(cl):
  
  #check if there is sadhguru_clips.pkl file 
  #if there is one load it else
  #dump above user clips json to file using pickle
  if os.path.isfile("user_clips3500.pkl"):
    print("file already present returning it")
    user_clips = pickle.load(open("user_clips3500.pkl", "rb"))
  else:
    print("file not present sending request")
    user_clips = cl.user_clips(10320868,3500)
    print("request send successful now dumping files")
    pickle.dump(user_clips, open("user_clips3500.pkl", "wb"))
  return user_clips
#user_clips = get_sadhguru_reels(cl)
#i = 0
#data=[]
#for clip in user_clips:
#  clip_dict = clip.dict()
#  #print_json(clip_dict)
#  clip_pk = clip_dict["pk"]
#  clip_play_count = clip_dict["play_count"]
#  clip_caption_text = clip_dict["caption_text"]
#  date = clip_dict["taken_at"]
#  code = clip_dict["code"]
#  data.append([clip_pk,clip_play_count,clip_caption_text,str(date),"https://www.instagram.com/reels/"+code+"/"])

#workbook = openpyxl.Workbook()
#sheet = workbook.active
## Write data to the CSV file
#for row in data:
#    sheet.append(row)
#excel_file_path = "sadhguru_reel.xlsx"
#workbook.save(excel_file_path)
#code="Cv98iPet8gB"
#id = cl.media_pk_from_url("https://www.instagram.com/reel/Cv4z6oPNRs6/")
#info = cl.media_info_v1(id)
#print_json(info.dict())
#media = cl.media_info("3170423214639577686")
#media = cl.media_info_a1("3170423214639577686")
#media = cl.media_info_v1("3170423214639577686")
#print_json(media.dict())
isha_links = {
    "sadhguru.arabic": "48934345499",
    "sadhguru.bangla": "49502075726",
    "sadhguru.deutsch": "8609014551",
    "sadhguru.francais": "8555551383",
    "sadhguru.gujarati": "20937833534",
    "sadhguru.hindiofficial": "23905604089",
    "sadhguru.italiano.ufficiale": "49110136964",
    "sadhguru.korea": "8598671484",
    "sadhguru.malayalam": "20269343193",
    "sadhguru.persian": "6870500834",
    "sadhguru.romana": "48581641246",
    "sadhguru.russian": "6771263617",
    "sadhguru.traditionalchinese": "49490145256",
    "sadhguru_kannada_official": "49807339771",
    "sadhguru_marathi_official": "50693629474",
    "sadhguru_portugues": "49205812190",
    "sadhgurubahasaindonesia": "48548783074",
    "sadhguruespanol": "8084378641",
    "sadhgurutamil": "13296531121",
    "sadhgurutelugu": "44235602269"
}
using_cl = cl2
## this function is used to get the official reels of isha for the given month
def get_isha_official_reels(date,using_cl):
  for isha in isha_links:
    #fetch isha links data for august 
    #info = using_cl.user_info_by_username(isha)
    #pk = info.dict()["pk"]
    i = 0
    pk= isha_links[isha]
    #print(pk)
    file_name = str(date)+"_"+str(pk)
    #print(file_name)
    #print("user id", given_reel_code_get_info(cl,"Cwc_ZrSPrlz")["user"]["pk"])
    if not os.path.isfile("competitor/"+file_name+".pkl"):

      get_channel_reels(using_cl,today_date,pk)
      print("file created for "+ file_name)
      i = i + 1
    else: 
      print("File already present skipping for "+ file_name)
    #if i % 2==0: 
    #  using_cl = cl
    #  print("Now using Cl1")
    #elif i%2 == 1: 
    #  using_cl = cl2
    #  print("Now using Cl2")
    #else: 
    #  using_cl = cl3
    #  print("Now using Cl3")
import pandas as pd

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
import gspread
def process_official_reels(today_date,compare_with):
  df = get_df_for_files(today_date,isha_links)

  df2 = get_df_for_files(compare_with,isha_links)
  #df = df.merge(df2, how="left")
  #missing_rows = df[~df.isin(df2.to_dict('list')).all(1)]
  #df2 = pd.concat([df2, missing_rows])
  df2.rename(columns = {
      'play_count':compare_with+'_play_count',
      'like_count':compare_with+'_like_count',
      'comment_count':compare_with+'_comment_count'
                        }, inplace = True)
  df = df.merge(df2,how="outer",on=['url'])
  df = df.fillna("0")

  df.loc[df['play_count'] == '0', 'play_count'] = df.loc[df['play_count'] == '0', compare_with+'_play_count']
  df.loc[df['like_count'] == '0', 'like_count'] = df.loc[df['like_count'] == '0', compare_with+'_like_count']
  df.loc[df['comment_count'] == '0', 'comment_count'] = df.loc[df['comment_count'] == '0', compare_with+'_comment_count']

  df["play_difference"] =  df["play_count"].astype(int) -df[compare_with+'_play_count'].astype(int)
  df["comment_difference"] =  df["comment_count"].astype(int) -df[compare_with+'_comment_count'].astype(int)
  df["like_difference"] =  df["like_count"].astype(int) -df[compare_with+'_like_count'].astype(int)

  gc = gspread.service_account_from_dict(credens)
  sheets = gc.open_by_key('1UR-Lpp9KYnSD7ah3qhLL4NjMnHzmqDiwpMp71ggyBAg')
  sheet = sheets.worksheet("Instagram_Inhouse_Videos")
  sheet.update([df.columns.values.tolist()] + df.values.tolist())
  print(df)

    
#create a python __main function with args and get compare_with keyword from args
if __name__ == '__main__':
  #vpn_config_path = "path_to_your_vpn_config.ovpn"
  #connect_to_vpn(vpn_config_path)
  #today_date = datetime.today().strftime('%Y-%m-%d')
  #print("uinsg cl3")
  #get_isha_official_reels(today_date,cl3)
  #parser = argparse.ArgumentParser(description="Add in following syntax python instagram_scape_instagrapi.py --compare_with=mm-dd-yyyy")
  #parser.add_argument("--compare_with", type=str, help="Date to compare with")
  #args = parser.parse_args()
  #if args.compare_with:
  #  compare_with = args.compare_with
  #  process_official_reels(today_date,compare_with)
  user_info = cl3.user_info_by_username("isha.foundation")
  print(user_info)
  #get_channel_reels(cl2,today_date,2932990635)

