#!/usr/bin/env python
# -*- coding: utf-8 -*-

def clinic():
    print "Вы только что зашли в клинику!"
    print "Какую дверь вы выберете, правую или левую?"
    answer = raw_input("Наберите left или right и нажмите 'Enter'.\n").lower()
    if answer == "left" or answer == "l":
        print "Это комната оскорблений! Вы просто птичий помет какой-то!"
    elif answer == "right" or answer == "r":
        print "Конечно же, это комната споров! Я же уже говорил Вам это!"
    else:
        print "Вы не выбрали дверь! Правую или левую? Пробуйте еще!"
        clinic()
    
    print "Еще раз?"
    answer = raw_input("y/n; yes/no; 1/0\n").lower()
    if answer == "y" or answer == "yes" or answer == "1":
        clinic()
    else:
        print "Bye"
        quit()

clinic()


	
