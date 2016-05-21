#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import argparse
import json
import math

parser = argparse.ArgumentParser()
parser.add_argument("--text", required=True, help="Input text")
parser.add_argument("--short", action='store_true')
args = parser.parse_args()

input_text = args.text.decode('utf8')

VALID_CHARS = u'qwertzuiopasdfghjklyxcvbnm1234567890QWERTZUIOPASDFGHJKLYXCVBNM ?:.,;-=/+ěščřžýáíéĚŠČŘŽÝÁÍÉůúŇ'

def chars_score(text):
    known_cnt = 0
    for char in text:
        if char in VALID_CHARS:
            known_cnt += 1
    return float(known_cnt)/min(len(text), 1)

def length_score(text):
    cnt = 0
    for char in text:
        if char in VALID_CHARS:
            cnt += 1
    return min(math.log(cnt, 1000), 1.0)

# TODO: add another functions here
# def xyz_score(text):
#    text magic here
#    return 0.5

def compute(scores):
    total = 0
    cnt = 0
    for score in scores:
        cnt += 1
        total = (total * (cnt-1) + score['value']) / cnt;
    return {'score': total, 'parts': scores}

scores = []
scores.append({'name': 'chars_score', 'value': chars_score(input_text)})
scores.append({'name': 'length_score', 'value': length_score(input_text)})
# TODO: add another functions here
# scores.append({'name': 'xyz_score', 'value': xyz_score(args.text)})

total_score = compute(scores)

if args.short:
    print(total_score['score'])
else:
    print(json.dumps(total_score, sort_keys=True, indent=4))
