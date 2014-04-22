#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools

#all the group are playing
data=["ברזיל","יפן","אוסטרליה","איראן","דרום קוריאה","הולנד","איטליה","ארגנטינה","ארצות הברית","קוסטה ריקה","בלגיה","שווייץ","גרמניה","קולומביה","רוסיה","בוסניה והרצגובינה","אנגליה","ספרד","צ'ילה","אקוודור","הונדורס","ניגריה","חוף השנהב","קמרון","גאנה","אלג'יריה","יוון","קרואטיה","פורטוגל","צרפת","מקסיקו","אורוגוואי"]
heb_carters=["א","ב","ג","ד","ה","ו","ז","ח","ט","י","כ","ל","מ","נ","ס","ע","פ","צ","ק","ר","ש","ת"]

#all permptation avilable this year 
p=itertools.permutations(data,2)
c=itertools.permutations(heb_carters,2)


#size of the list
print sum(1 for _ in p)

