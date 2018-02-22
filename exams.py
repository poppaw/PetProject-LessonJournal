import sys
import os
import data_operations
import gui


def make_exams_list(file='exams.txt'):
    """
    returns list of past and coming exams with grades
    """
    exams_list = data_operations.generate_list_from_txt('exams.txt')
    return exams_list

labels_list = ['I semestr: techniczny', 'I semestr: utwory',
               'II semestr: techniczny', 'II semestr: utwory']
