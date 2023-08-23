from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import random
from .serializers import *


class PasswordGenerate(APIView):
    def post(self, request):
        serializers = PasswordGenerateSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)

        data = serializers.validated_data


        def pswd(lenght, num=False, rus_s=False, rus_cups_s=False, eng_s=False, eng_cups_s=False, sp_s=False):
            rus = ('а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я')
            rus_cups = ('А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ы', 'Ь', 'Э', 'Ю', 'Я')
            eng = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
            eng_cups = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
            spec_simbols = ('!', '"', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~')
            password = ''

            test = [num, rus_s, rus_cups_s, eng_s, eng_cups_s, sp_s]

            if lenght > 0 and any(test):
                while len(password) <= lenght:
                    if num:
                        password = password + str(random.randint(0, 9))
                    if rus_s:
                        password += str(random.choice(rus))
                    if rus_cups_s:
                        password += str(random.choice(rus_cups))
                    if eng_s:
                        password += str(random.choice(eng))
                    if eng_cups_s:
                        password += str(random.choice(eng_cups))
                    if sp_s:    
                        password += str(random.choice(spec_simbols))

                if len(password) > lenght:
                    password = password[:len(password)-(len(password)-lenght)]
                a = list(password)
                random.shuffle(a)
                password = ''.join(a)
                return password
            
            else:
                return password
        return Response({'password': pswd(data['lenght'], data['use_digit'],
                                          data['use_rus'], data['use_upper_rus'], 
                                          data['use_eng'], data['use_upper_eng'], data['use_spec_simbols'])}, status=200)

   