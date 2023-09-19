## this is a file that contains functions that are used as services 
import pickle
import os 
import json
import pandas as pd


def get_channel_reels(cl, date, id):
  file_name = str(date)+"_"+str(id)
  if os.path.isfile("competitor/"+file_name+".pkl"):
    print("file already present returning it")
    user_clips = pickle.load(open("competitor/"+file_name+".pkl", "rb"))
  else:
    print("file not present sending request")
    user_clips = cl.user_clips(id,700)
    print("request sending successful now dumping files")
    pickle.dump(user_clips, open("competitor/"+file_name+".pkl", "wb"))
  return user_clips

def print_json(obj):
  print(json.dumps(obj, indent=4, sort_keys=True, default=str))
def add_competetor(id,name):
  competitor_list = {}
  if os.path.isfile("competitor/competitor_list.pkl"):
    competitor_list = pickle.load(open("competitor/competitor_list.pkl", "rb"))
  ##check if competitor_list[0] is in competitor_list keys 
  if id not in competitor_list.keys():
    competitor_list[id] ={"name":name} 
    pickle.dump(competitor_list, open("competitor/competitor_list.pkl", "wb"))
  else: 
    return
  
def given_reel_code_get_info(cl,reel_code):
  id = cl.media_pk_from_url("https://www.instagram.com/reel/"+reel_code+"/")
  info = cl.media_info_v1(id)
  #print_json(info.dict())
  return info.dict()
def get_df_for_files(date,isha_links):
  temp_user_clips = []
  for isha in isha_links:
    #fetch isha links data for august 
    pk = isha_links[isha]
    file_name = str(date)+"_"+str(pk)
    if os.path.isfile("competitor/"+file_name+".pkl"):
      print("file present for "+ file_name)
      ind_channel_data = pickle.load(open("competitor/"+file_name+".pkl", "rb"))
      for ind_reel in ind_channel_data:
        dict_clip = ind_reel.dict()
        temp_user_clips.append({"channel_name":isha,
                                "video_duration":dict_clip["video_duration"],
                                "name":dict_clip["user"]["full_name"],
                                "play_count":dict_clip["play_count"],
                                "caption_text":dict_clip["caption_text"],
                                "taken_at":str(dict_clip["taken_at"]),
                                "url":"https://www.instagram.com/p/"+dict_clip["code"]+"/",
                                "like_count":dict_clip["like_count"],
                                "comment_count":dict_clip["comment_count"]
                                })
    else: 
      print("File not present skipping for "+ file_name)
  df = pd.json_normalize(temp_user_clips)
  return df
