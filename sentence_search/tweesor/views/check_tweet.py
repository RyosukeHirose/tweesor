from django.views.generic import ListView

import sys
import fasttext as ft



def learning():
    argvs = sys.argv
    print(argvs[1])
    input_file = argvs[1]   
    output_file = argvs[2]

    classifier = ft.train_supervised(input_file)
    classifier.save_model(output_file)
