#### Commands Django

* Migrate  : python manage.py makemigrations course <app name>
* Check the migrations on models : python manage.py sqlmigrate <app name> 0004
* apply migrations: python manage.py migrate
* create super user for admin django : python manage.py createsuperuser
  * user: admin
  * mot de passe: admin123456
* Go to the shell : python manage.py shell
  * Check model info:
    * from <app name>.models import <models/tables>
    * select * from  - <models/table>.objects.all()
 * At this time the useful link to setup the [logins is here](https://wsvincent.com/django-user-authentication-tutorial-login-and-logout/)
 
---

##### Examples:

* Creating and saving info:

```python
subject1 = subject.objects.create(subj_name='Grammar')
subject1.save()
sub1_cate1 = subject_category.objects.create(subject= subject1 , category_name='W Questions')
sub1_cate1.save()
sub1_cate1_quest = questions.objects.create(category=sub1_cate1,question_desc='pick out the right pronoun')
sub1_cate1_quest.save()

answer1 = answer.objects.create( subject=subject1, category=sub1_cate1, questions=sub1_cate1_quest,answer_desc ='Do',correct=0)
answer2 = answer.objects.create( subject=subject1, category=sub1_cate1, questions=sub1_cate1_quest,answer_desc ='Is',correct=1)
answer1.save()
answer2.save()
```
