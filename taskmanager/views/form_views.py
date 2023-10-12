from django import forms
from ..models.task import Task
from django.core.exceptions import ValidationError

# Create your views here.

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task # 指定关联的模型
        fields = ['name','description','task_type','difficulty', 'cycle'] # 指定需要处理的字段
    
    # 验证name字段
    def clean_name(self):
        name = self.cleaned_data.get('name') # 获取清理过的name字段数据
        # 检查是否存在相同名称的Task
        if Task.objects.filter(name=name).exists():
            raise ValidationError('任务名称已存在') #如果存在，抛出错误
        return name

    # 对于多个字段进行验证
    def clean(self):
        cleaned_data = super().clean() # 获取清理过的字段数据
        task_type = cleaned_data.get('task_type') 
        difficulty = cleaned_data.get('difficulty')

        # 如果task_type 是 'Type1' ，则difficulty只能是 'Easy' 或 'Medium'
        if task_type == 'Type1' and difficulty not in ['Easy','Medium']:
            self.add_error('difficulty','对于Type1任务，难度必须是Easy或Medium')
        
        # 如果验证通过，返回所有清理过的数据
        return cleaned_data