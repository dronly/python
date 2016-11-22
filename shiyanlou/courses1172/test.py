#!/usr/bin/env python3
# -*- coding: utf-8 -*-

actions = ['Up', 'Left', 'Down', 'Right', 'Resart', 'Exit']
letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']
actions_dict = dict(zip(letter_codes, actions * 2))

print(letter_codes)
print(actions_dict)