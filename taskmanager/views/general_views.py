from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from ..models.task import Task

# Create your views here.

# 主页视图
def home(request):
    return render(request, 'home.html') # 渲染home.html模板

# 一个简单的hell world视图
def hello_world(request):
    return HttpResponse('hello world')

# 任务列表视图
def task_list(request):
    tasks = Task.objects.all() # 获取所有任务对象
    return render(request, 'task_list.html',{'tasks': tasks}) # 渲染任务列表模板

# 创建任务视图
# def create_task(request):
#     if request.method == 'POST': #如果是POST请求，表示用户提交了表单
#         form =  TaskForm(request.POST) # 使用POST数据创建表单实例
#         if form.is_valid(): # 验证表单
#             form.save() # 保存任务到数据库
#             return redirect('task_list') # 保存成功重定向到任务列表页面
#     else:
#         form = TaskForm() #如果是GET请求。创建一个空表单
#     return render(request, 'create_task.html',{'form': form}) # 渲染创建任务的表单页面