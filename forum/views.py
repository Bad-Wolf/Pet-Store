from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer


class QuestionList(APIView):
    """
    List all questions and answers or create new question.
    """
    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class QuestionDetail(APIView):
    """
    CRUD specific question.
    """
    def get_object(self, pk):
        try:
            return Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        question = self.get_object(pk=pk)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    def put(self, request, pk):
        question = self.get_object(pk=pk)
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        question = self.get_object(pk=pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AnswerDetail(APIView):
    """
    List specific answer or add like/dislike.
    """
    def get_object(self, pk):
        try:
            return Answer.objects.get(pk=pk)
        except Answer.DoesNotExist:
            raise Http404

    def get(self, request, pk, answer_pk):
        full_request_url = request.build_absolute_uri()
        if 'dislike' in full_request_url:
            answer = self.get_object(pk=answer_pk)
            answer.dislikes += 1
            answer.save()
            serializer = AnswerSerializer(answer)
            return Response(serializer.data)
        elif 'like' in full_request_url:
            answer = self.get_object(pk=answer_pk)
            answer.likes += 1
            answer.save()
            serializer = AnswerSerializer(answer)
            return Response(serializer.data)
        else:
            answer = self.get_object(pk=answer_pk)
            serializer = AnswerSerializer(answer)
            return Response(serializer.data)