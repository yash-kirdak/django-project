from django.shortcuts import render, redirect, get_object_or_404
from .models import Document
# from .forms import BookletForm

def show(request):
    all_data = Document.objects.all()

    context = {
        'data':all_data
    }
    return render(request,'view.html')

# def page2(request):
#     booklets = Booklet.objects.all()
#     return render(request, 'page2.html', {'booklets': booklets})

# def page3(request):
#     if request.method == 'POST':
#         form = BookletForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('page2')
#     else:
#         form = BookletForm()
#     return render(request, 'page3.html', {'form': form})

# def delete_booklet(request, booklet_id):
#     booklet = get_object_or_404(Booklet, id=booklet_id)
#     booklet.delete()
#     return redirect('page2')
