from django.test import TestCase

# Create your tests here.


result = 72

if result >= 90:
    print('优秀')
elif result >= 70:
    print('良好')
elif result >= 60:
    print('及格')
else:
    print('不及格')