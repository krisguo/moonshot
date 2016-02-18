
# Serializer


from django.conf import settings

settings.configure()


# make new data

from questions.models import Question





question = Question(title='moon shot test is hard?')
question.save()

question = Question(title='Do you afraid from snakes?')
question.save()


#update data
from questions.serializers import QuestionSerializer
serializer = QuestionSerializer(question)
serializer.data
# {'pk': 3, 'description': u'', 'title': u'Do you afraid from snakes?'}





#get json from data

from rest_framework.renderers import JSONRenderer
content = JSONRenderer().render(serializer.data)
content
# '{"pk":3,"title":"Do you afraid from snakes?","description":""}'





# Deserialization is similar. First we parse a stream into Python native datatypes...
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser
stream = BytesIO(content)
data = JSONParser().parse(stream)
# ...then we restore those native datatypes into a fully populated object instance.
serializer = QuestionSerializer(data=data)
serializer.is_valid()
# True
serializer.validated_data
# OrderedDict([('title', ''), ('code', 'print "hello, world"\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])
serializer.save()
# <Snippet: Snippet object>



# get all data
serializer = QuestionSerializer(Question.objects.all(), many=True)



# One nice property that serializers have is that you can inspect all the fields in a serializer instance, by printing its representation.
from questions.serializers import QuestionSerializer
serializer = QuestionSerializer()
print(repr(serializer))



# install list for heroku
# pip install httpie
# http http://127.0.0.1:8000/questions/
# http http://127.0.0.1:8000/questions/2/
