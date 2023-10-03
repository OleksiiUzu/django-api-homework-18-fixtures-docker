from django.shortcuts import render, redirect
import blog.models
import animals.models
import blog.forms


def index(request):
    post = blog.models.Blog.objects.all()
    return render(request, 'blog/index.html', {'result': post})


def blog_post(request, post_id):
    post = blog.models.Blog.objects.get(id=post_id)
    return render(request, 'blog/post.html', {'res': post})


def feedback(request):
    if request.method == 'POST':

        # print(data)
        '''new_feedback = blog.models.Feedback( title=data['title'],
                                                text=data['Text'],
                                                media=data['media'],
                                                user=request.user,
                                                animal_id=int(data['animal_type']))
        new_feedback.save()'''
        form = blog.forms.FeedbackForm(request.POST)
        feedback_data = form.save(commit=False)
        data = request.POST
        if data:
            animal = animals.models.Animal.objects.get(id=int(data['animal_type']))
            feedback_data.user = request.user
            feedback_data.animal = animal
            feedback_data.save()
            return redirect('/blog/feedback')
    all_feedback = blog.models.Feedback.objects.all()
    all_animals_data = animals.models.Animal.objects.all()
    animals_type = [i.animal_type for i in all_animals_data]
    animal_type_query = request.GET.get('animal_type')
    filtered_animals = animals.models.Animal.objects.all().filter(animal_type=animal_type_query)

    if animal_type_query:
        all_feedback = all_feedback.all().filter(animal_id__in=[i.id for i in filtered_animals])

    results = all_feedback.all()
    return render(request, 'blog/feedback.html', {'feedback': results,
                                                  'animals': set(animals_type),
                                                  'all_animals': all_animals_data,
                                                  'feedback_form': blog.forms.FeedbackForm()})
