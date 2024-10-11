from django.shortcuts import render,HttpResponse
from rest_framework import status
from rest_framework.response import Response
import sys
sys.path.insert(1, '../../visualization/')
import drawLexisDiagram
from adjustData import adjust_data
from GraphController import GraphController
from APCAnalysis import apc_analysis
from visualizeDefaultRate import default_age,default_cohort
from drawLexisDiagram import draw_Lexis_Diagram_Real


from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny,IsAuthenticated
from .serializers import MyTokenObtainPairSerializer
from .serializers import *
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics




#__________________________________login views2___________________________________
@api_view(['POST'])
@permission_classes([AllowAny])
#@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def log_in2(request):
    data = request.data
    print(data)
    try:
        data = request.data
        email=data["email"]
        password = data["password"]
        print(email,password)
        isUser = my_authenticate(email,password)
        if isUser is not None:
            user2 = User.objects.filter(username=isUser)
            user = User.objects.get(username=isUser)
            serializer = userSerializers(user2, many=True)
            token = Token.objects.get_or_create(user=user)
            data = serializer.data
            return Response({token[0].key},status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid Credentials'},
                        status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response({'error': 'Please provide both username and password'},
                        status=status.HTTP_404_NOT_FOUND)


#__________________________________login views1___________________________________
@api_view(['POST'])
@permission_classes([AllowAny])
#@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def logIn(request):
    data = request.data
    print(data)
    try:
        data = request.data
        email=data["email"]
        password = data["password"]
        print(email,password)
        isUser = my_authenticate(email,password)
        if isUser is not None:
            user2 = User.objects.filter(username=isUser)
            user = User.objects.get(username=isUser)
            serializer = userSerializers(user2, many=True)
            token = Token.objects.get_or_create(user=user)
            data = serializer.data
            return Response({'user':data[0],"token":token[0].key},status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid Credentials'},
                        status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response({'error': 'Please provide both username and password'},
                        status=status.HTTP_404_NOT_FOUND)



#improve: password more secure, return 404 if wrong.
def my_authenticate(emailOrUsername,password):
    #checking if the user entered email or username to log in
    if emailOrUsername.__contains__('@'):
        user = User.objects.filter(email=emailOrUsername).first()
        print(user)
    else:
        user = User.objects.filter(username=emailOrUsername).first()
    # checking if the password is correct
    if user:
        is_correct = user.check_password(password)
        if is_correct:
            print("pass!")
            return user
        else:
            print('Wrong password')
            return None
    else:
        print('Cannot find the user')
        return None


    

#___________________________register views______________________________ No authentication required
class Register(generics.CreateAPIView):
    try:
        queryset = User.objects.all()
        permission_classes = (AllowAny,)
        serializer_class = RegisterSerializer
        print("Register successfully")
    #    return Response(status=status.HTTP_200_OK)
    except:
        print("Register not successfully")
    #    return Response(serializer.data,status=status.HTTP_200_OK)



@api_view(['POST'])
@permission_classes([IsAuthenticated,])
#____________________________downloadGraph views v4__________________________________  authentication required
def download_graph4(request):
    try:
        data = request.data
        print(data)
        filename = data['filename']
        colorBlind = False

        if(data['isDark'] == 'false'):
            colorBlind = False
        elif(data['isDark'] == 'true'):
            colorBlind = True
        colorVision = data["colorVision"]

        # TODO
        feature = data["feature"]
        condition = data["condition"]
        value = data["value"]
        error = data["error"]
        separator = data["separator"]
        decimal = data["decimal"]
        ageTitle = data["ageTitle"]
        cohortTitle = data["cohortTitle"]
        defaultFlagTitle = data["defaultFlagTitle"]
        predictedDefaultTitle = data["predictedDefaultTitle"]
        ageUnit = data["ageUnit"]
        cohortUnit = data["cohortUnit"]
        language = data["language"]
        adjust_data(filename, ageTitle, cohortTitle, defaultFlagTitle, predictedDefaultTitle)
        graphController = GraphController(filename = filename,isDark = colorBlind,colorVision = colorVision,
                                          error = error, age_unit = ageUnit, cohort_unit = cohortUnit,
                                          separator=separator,decimal=decimal,language=language)
        data = graphController.data_filter(feature,condition,value)
        #graphController = GraphController(filename = "sim",isDark = False,feature = None, condition = None, 
        #        value = None, error = "0", ageUnit = "Month", cohortUnit = "Month")
        default_age(data,graphController.isDark,colorVision,language)
        default_cohort(data,graphController.isDark,colorVision,language)
        draw_Lexis_Diagram_Real(data,language,graphController.isDark)
        apc_analysis(data,graphController.isDark,graphController.colorVision,graphController.error,language)
        #apc_analysis(graphController.data,graphController.isDark,graphController.error)
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Exception as e: 
        print(e)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

#__________________________________adjust views___________________________________
@api_view(['POST'])
@permission_classes([IsAuthenticated,])
#@permission_classes([AllowAny,]) 
#@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def adjust_apc(request):
    try:
        data = request.data
        filename = data['filename']
        colorBlind = False
        if(data['isDark'] == 'false'):
            colorBlind = False
        elif(data['isDark'] == 'true'):
            colorBlind = True

        feature = data["feature"]
        condition = data["condition"]
        value = data["value"]
        error = data["error"]
        separator = data["separator"]
        decimal = data["decimal"]
        ageUnit = data["ageUnit"]
        cohortUnit = data["cohortUnit"]
        graphController = GraphController(filename = filename,isDark = colorBlind,
                                          error = error, age_unit = ageUnit, cohort_unit = cohortUnit,
                                          separator=separator,decimal=decimal)
        apc_analysis(graphController.data_filter(feature,condition,value),
                     graphController.isDark,graphController.colorVision, graphController.error)
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
'''
@api_view(['POST'])
@permission_classes([IsAuthenticated,])
#____________________________downloadGraph views v3__________________________________  authentication required
def downloadGraph3(request):
    try:
        data = request.data
        print(data)
        filename = data['filename']
        colorBlind = False

        if(data['isDark'] == 'false'):
            colorBlind = False
        elif(data['isDark'] == 'true'):
            colorBlind = True

        # TODO
        #feature = data["feature"]
        #condition = data["condition"]
        #value = data["value"]
        feature = None
        condition = None
        value = None

        error = data["error"]

        separator = data["separator"]
        decimal = data['decimal']
        ageTitle = data["ageTitle"]
        cohortTitle = data["cohortTitle"]
        defaultFlagTitle = data["defaultFlagTitle"]
        predictedDefaultTitle = data["predictedDefaultTitle"]
        ageUnit = data["ageUnit"]
        cohortUnit = data["cohortUnit"]
        adjust_data.adjust_data(filename, ageTitle, cohortTitle, defaultFlagTitle, predictedDefaultTitle)
        print("miao")
        defaultRateAge.defaultRateAge(filename = filename,isDark = colorBlind,feature = feature, 
                                      condition = condition, value = value, ageUnit = ageUnit, 
                                      cohortUnit = cohortUnit,separator = separator, decimal=decimal)
        print("wang")
        defaultRateCohort.defaultRateCohort(filename = filename,isDark = colorBlind,feature = feature, 
                                            condition = condition, value = value,ageUnit = ageUnit, cohortUnit = cohortUnit,
                                            separator = separator, decimal=decimal)
        print("1")
        drawLexisDiagram.drawLexisDiagram(filename = filename,feature = feature, condition = condition, value = value,
                                          separator = separator, decimal=decimal)
        print("f")
        APC.APCAnalysis(filename = filename,isDark = colorBlind,feature = feature, condition = condition, 
                         value = value, error = error,ageUnit = ageUnit, cohortUnit = cohortUnit,
                         separator = separator, decimal=decimal)
        print("4")
        return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    


    


    

#__________________________________adjust views___________________________________
@api_view(['POST'])
@permission_classes([IsAuthenticated,])
#@permission_classes([AllowAny,]) 
#@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def adjust(request):
    try:
        data = request.data
        print(data)
        filename = data['filename']
        colorBlind = False
        if(data['isDark'] == 'false'):
            colorBlind = False
        elif(data['isDark'] == 'true'):
            colorBlind = True
        error = data["error"]
        defaultRateAge.defaultRateAge(filename = filename,isDark = colorBlind,error = error)
        defaultRateCohort.defaultRateCohort(filename = filename,isDark = colorBlind,error = error)
        drawLexisDiagram.drawLexisDiagram(filename = filename)
        APC.APCAnalysis(filename = filename,isDark = colorBlind,error = error)
        return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

#__________________________________filter views___________________________________
@api_view(['POST'])
@permission_classes([IsAuthenticated,])
#@permission_classes([AllowAny,]) 
#@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def addCondition(request):
    try:
        data = request.data
        print(data)
        filename = data['filename']
        colorBlind = False
        if(data['isDark'] == 'false'):
            colorBlind = False
        elif(data['isDark'] == 'true'):
            colorBlind = True
        feature = data["feature"]
        condition = data["condition"]
        value = data["value"]
        defaultRateAge.defaultRateAge(filename = filename,isDark = colorBlind,
                                      feature = feature, condition = condition, value = value)
        defaultRateCohort.defaultRateCohort(filename = filename,isDark = colorBlind,
                                            feature = feature, condition = condition, value = value)
        drawLexisDiagram.drawLexisDiagram(filename = filename,feature = feature, 
                                          condition = condition, value = value)
        APC.APCAnalysis(filename = filename,isDark = colorBlind,feature = feature, 
                         condition = condition, value = value)
        return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated,])
#____________________________downloadGraph views v2__________________________________  authentication required
def downloadGraph2(request):
    try:
        data = request.data
        print(data)
        filename = data['filename']
        colorBlind = False
        if(data['isDark'] == 'false'):
            colorBlind = False
        elif(data['isDark'] == 'true'):
            colorBlind = True
        defaultRateAge.defaultRateAge(filename = filename,isDark = colorBlind)
        defaultRateCohort.defaultRateCohort(filename = filename,isDark = colorBlind)
        drawLexisDiagram.drawLexisDiagram(filename = filename)
        APC.APCAnalysis(filename = filename,isDark = colorBlind)
        return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET'])
@permission_classes([IsAuthenticated,])
#____________________________downloadGraph views v1__________________________________  authentication required
def downloadGraph(request):
    try:
        defaultRateAge.defaultRateAge('sim')
        defaultRateCohort.defaultRateCohort('sim')
        drawLexisDiagram.drawLexisDiagram('sim')
        APC.APCAnalysis('sim')
        return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([IsAuthenticated,])
#____________________________downloadGraphisBlind views__________________________________  authentication required
def downloadGraphisBlind(request):
    try:
        defaultRateAge.defaultRateAge(True)
        defaultRateCohort.defaultRateCohort(True)
        drawLexisDiagram.drawLexisDiagram()
        APC.APCAnalysis(True)
        return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated,])
#____________________________dr_age views__________________________________  authentication required
def download_dr_age(request):
    try:
        defaultRateAge.defaultRateAge()
        # dr_age.dr_age()
        #file = open('../../../res/dr_age.html', 'rb')
        #response = HttpResponse(file)
        #response['Content-Type'] = 'application/octet-stream' #设置头信息，告诉浏览器这是个文件
        #response['Content-Disposition'] = 'attachment;filename="dr_age.html"'
        return Response(status=status.HTTP_200_OK)
    
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def download_dr_age_predicted(request):
    try:
        defaultRateAge.defaultRateAge()
        # dr_age.dr_age()
        file = open('../../../res/dr_age_predicted.html', 'rb')
        response = HttpResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="dr_age.html"'
        return response

    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


#____________________________dr_cal views__________________________________  authentication required
@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def download_dr_cal(request):
    try:
        defaultRateCohort.defaultRateCohort()
        return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)



#____________________________lexis views__________________________________  authentication required
@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def download_lexis(request):
    try:
        drawLexisDiagram.drawLexisDiagram()
        return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


#____________________________APCAnalysis views__________________________________  authentication required
@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def download_apc(request):
    try:
        APC.APCAnalysis()
        return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)



#==================================Used for color blind mode
@api_view(['GET'])
@permission_classes([IsAuthenticated,])
#____________________________dr_age_blind views__________________________________  authentication required
def download_dr_age_blind(request):
    try:
        defaultRateAge.defaultRateAge(True)
        # dr_age.dr_age()
        #file = open('../../../res/dr_age.html', 'rb')
        #response = HttpResponse(file)
        #response['Content-Type'] = 'application/octet-stream' #设置头信息，告诉浏览器这是个文件
        #response['Content-Disposition'] = 'attachment;filename="dr_age.html"'
        return Response(status=status.HTTP_200_OK)
    
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


#____________________________dr_cal_blind views__________________________________  authentication required
@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def download_dr_cal_blind(request):
    try:
        defaultRateCohort.defaultRateCohort(True)
        return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)




#____________________________APCAnalysis_blind views__________________________________  authentication required
@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def download_apc_blind(request):
    try:
        APC.APCAnalysis(True)
        return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
'''