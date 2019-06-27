from django.shortcuts import render

# Create your views here.

def home(request):
    full_text = request.GET.get('fulltext')

    if full_text is not None:
        word_list = full_text.split()

        return render(request, 'wordcount/home.html', {'fulltext': full_text, 'total': len(word_list)})


def about(request):
    return render(request, 'wordcount/about.html')

def count(request):
    full_text = request.GET.get('fulltext')

    if full_text is not None:
        word_list = full_text.split()

        word_dictionary = {}

        for word in word_list:
            if word in word_dictionary:
                # Increase
                word_dictionary[word] += 1
            else:
                # add to the dictionary
                word_dictionary[word] = 1

        return render(request, 'wordcount/count.html', {'fulltext': full_text, 'total': len(word_list), 'dictionary': word_dictionary.items()})