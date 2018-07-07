import twitter
import json
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import   Table, Column, Integer,  String, MetaData
from sqlalchemy import insert


def create_connection ():
  with open('twitterapi', 'r') as file:
    data = json.load(file)

  for connection, value in data.items():
    if ("DB" in connection):
      for info in value:
        user = info['user']
        passwd = info['passwd']
        port = info['port']
        endpoint = info['endpoint']
        db = info['db']

  string_conn = "mysql+pymysql://{}:{}@{}/{}?host={}?port={}".format(
    user,passwd,endpoint,db,endpoint,port)

  engine = sqlalchemy.create_engine(string_conn)
  conn = engine.connect()
  #conn.set_character_set('utf8')
  conn.execute('SET NAMES utf8;')
  conn.execute('SET CHARACTER SET utf8;')
  conn.execute('SET character_set_connection=utf8;')
  return conn

conn = create_connection ()

meta = MetaData(conn)
tbl_tweet = Table('tweethistorical',meta,
                  Column('tdesc', String(4000)),
                  Column('ttime' ,String(50)),
                  Column( 'tuserid', Integer),
                  Column('tuserlocation', String(50)),
                  Column('tusername', String(50)),
                  Column('tusersname', String(250)),
                  Column('tuserfollowers' , Integer),
                  autoload=True)


with open ('twitterapi','r') as file:
  data = json.load(file)

for connection,value in data.items():
  if("API" in connection):
    for info in value:
      consumer_key = info['consumer_key']
      consumer_secret = info['consumer_secret']
      access_token_key = info['access_token_key']
      access_token_secret = info['access_token_secret']


api = twitter.Api(consumer_key=consumer_key,
  consumer_secret=consumer_secret,
  access_token_key=access_token_key,
  access_token_secret=access_token_secret)



search = api.GetSearch("worldcup") # Replace happy with your search
for tweet in search:
  record = tbl_tweet.insert().values(
  tdesc = tweet.text.encode('utf-8'),
  ttime = tweet.created_at[4:20],
  tuserid = tweet.user.id,
  tuserlocation = tweet.user.location,
  tusername = tweet.user.name,
  tusersname = tweet.user.screen_name,
  tuserfollowers = tweet.user.followers_count)
  conn.execute(record)




