#!/usr/bin/env python
import sys, os, time
import tweepy
keys = dict(
consumer_key='iJgCUSrDk4nWqPYpWnbQ4cP8i ',
consumer_secret='NWtdb8AHLV389LyjFBnfES2XtPk551V1TQeU8Gx8r5oEvmpRHE',
access_token='885544101835309056-gYY2Ob8YOOWslR8vQoB3AluhjernUSz', 
access_token_secret='nKLPMXAdjTxCWiucuWGsHpOeAyzwaexk0QwZGcOn0Plux'
)

user = "@Ramsy176"

auth = tweepy.OAuthHandler(keys['iJgCUSrDk4nWqPYpWnbQ4cP8i'], keys['NWtdb8AHLV389LyjFBnfES2XtPk551V1TQeU8Gx8r5oEvmpRHE'])
auth.set_access_token(keys['885544101835309056-gYY2Ob8YOOWslR8vQoB3AluhjernUSz'], keys['nKLPMXAdjTxCWiucuWGsHpOeAyzwaexk0QwZGcOn0Plux'])
api = tweepy.API(auth)

def tweet():
	message=input("lost my phone looks like i gotta tweet off of this🤷: ")
	api.update_status(message)
	time.sleep(1000)
if __name__ == "__main__":
	while 1:
		tweet()
