from django.http import HttpResponseBadRequest
from django.shortcuts import render
import json


def highlight_sentencess(paragraph, response):
    for elem in response:
        paragraph = paragraph.replace(elem['sentence'], f"<MARK>{elem['sentence']}</MARK>")
    # print(paragraph)
    return paragraph

"""
The api data must be wrong
"""
# def highlight_sentencess(paragraph, response):
#     highlighted_paragraph = ""
#     prev_end = 0
#     for elem in response:
#         # Use the span values to extract the sentence from the paragraph
#         start, end = elem['span']['start'], elem['span']['end']
#         sentence = paragraph[start:end]
#         highlighted_paragraph += paragraph[prev_end:start] + f"<MARK>{sentence}</MARK>"
#         prev_end = end
#     highlighted_paragraph += paragraph[prev_end:]
#     return highlighted_paragraph



def highlight_sentence(request):
    if request.method == 'POST':
        try:
            paragraph = request.POST.get('paragraph')
            response = json.loads(request.POST.get('response'))

            if not paragraph or not response:
                raise ValueError("Invalid input data")

            highlighted_paragraph = highlight_sentencess(paragraph, response)

            return render(request, 'highlight_sentence.html',
                          {'paragraph': highlighted_paragraph,
                           'userpara':paragraph,
                           'resp': response
                           })
        except (ValueError, json.JSONDecodeError) as e:
            return render(request, 'highlight_sentence.html')
    else:
        return render(request, 'highlight_sentence.html')
