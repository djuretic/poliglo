#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint
from time import sleep

from poliglo import default_main, get_inputs

def process(specific_info, data, *args):
    inputs = get_inputs(data, specific_info)

    numbers_range = inputs.get('numbers_range')
    how_many_to_create = inputs.get('how_many_to_create')

    for _ in range(1, how_many_to_create):
        sleep(0.05) #Sleep for visualization purpose
        yield {'number': randint(numbers_range[0], numbers_range[1])}

if __name__ == '__main__':
    from os import environ as env, path
    default_main(env.get('POLIGLO_SERVER_URL'), path.splitext(path.basename(__file__))[0], process)