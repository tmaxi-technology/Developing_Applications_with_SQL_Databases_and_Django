from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.template import loader

def exam_result(request):
  template = loader.get_template('onlinecourse\exam_result_bootstrap.html')
  return render(request, 'onlinecourse\exam_result_bootstrap.html')
def course_detail(request):
  template = loader.get_template('onlinecourse\course_detail_bootstrap.html')
  return HttpResponse(template.render())
  return HttpResponse('course_detail_bootstrap.html')
