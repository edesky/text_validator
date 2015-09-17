#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import json


parser = argparse.ArgumentParser()
parser.add_argument("--text", required=True, help="Dirty input text")
parser.add_argument("--short", action='store_true')
args = parser.parse_args()


def chars_score(text):
  known_chars = u'qwertzuiopasdfghjklyxcvbnm1234567890QWERTZUIOPASDFGHJKLYXCVBNM ?:.,;-=/+ěščřžýáíéĚŠČŘŽÝÁÍÉůúŇ'
  known_cnt = 0

  for char in text:
    if char in known_chars:
      known_cnt += 1

  return float(known_cnt)/len(text)

# TODO: add another functions here
# def xyz_score(text):
#    text magic here
#    return 0.5


def compute(scores):
    total = 0
    cnt = len(scores)
    for score in scores:
        total = (total * (cnt-1) + score['value']) / cnt;
    return {'score': total, 'parts': scores}


scores = []
scores.append({'name': 'chars_score', 'value': chars_score(args.text)})
# TODO: add another functions here
# scores.append({'name': 'xyz_score', 'value': xyz_score(args.text)})

total_score = compute(scores)

if args.short:
    print(total_score['score'])
else:
    print(json.dumps(total_score, sort_keys=True, indent=4))
