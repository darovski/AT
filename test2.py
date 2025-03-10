import pytest
from main import count_vowels

def test_is_count_vowels():
   assert count_vowels("") == 0

def test_is_count_vowels_en1():
   assert count_vowels("miralogic") == 4
   assert count_vowels("hello world") == 3

def test_is_count_vowels_en2():
   assert count_vowels("aeuoa") == 5
   assert count_vowels("aeueoae ouaeuo") == 13

def test_is_count_vowels_en3():
   assert count_vowels("wsdcvbntghklp") == 0
   assert count_vowels("qszxc") == 0

def test_is_count_vowels_en4():
   assert count_vowels("wsDCyYEAntaghoklpe") == 5

def test_is_count_vowels_ru1():
   assert count_vowels("Доброе утро страна") == 7
   assert count_vowels("Проверка работы функции") == 9

def test_is_count_vowels_ru2():
   assert count_vowels("ауёеия") == 6
   assert count_vowels("юиуеёеияыэ") == 10

def test_is_count_vowels_ru3():
   assert count_vowels("цфвсмтр") == 0
   assert count_vowels("трпнмсвцфчсмтрпнк") == 0

def test_is_count_vowels_ru3():
   assert count_vowels("атрПпуенмФИЯсвВЫфчсЮЭмтМИрпнкы") == 10

def test_is_count_vowels_en_ru():
   assert count_vowels("AsdwEynbu.ouFgvатрПпуенмФИЯсвВЫфчсЮЭмтМИрпнкы") == 16