from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serialize import TodoSerializer

'''
View all Todo List of an author
'''
@api_view(['GET'])
def view_todo(request):
    queryset = Todo.objects.filter(author=request.user.id)
    serializer = TodoSerializer(queryset, many=True)
    return Response({'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)

'''
Create a Todo List 
'''
@api_view(['POST'])
#@permission_classes([IsAuthenticated])**Don't need to use IsAuthenticated as i added rest_framework_simplejwt.authenticateion.JWTAuthentication as a DEFAULT_AUTHENTICATION_CLASSES
def create_todo(request):
    serializer = TodoSerializer( data=request.data)
    if serializer.is_valid():
        serializer.save(author=request.user)
        return Response({'success': True, 'todo': serializer.data}, status=status.HTTP_201_CREATED)
    return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

'''
Update a Todo 
'''
@api_view(['PUT'])
#@permission_classes([IsAuthenticated])
def update_todo(request, id):
    todo = get_object_or_404(Todo, id=id, author=request.user)
    serializer = TodoSerializer(todo, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save(updated_at=timezone.now())
        return Response({'success': True, 'todo': serializer.data}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


'''
Delete a Todo
'''
@api_view(['DELETE'])
def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id, author=request.user) 
    todo.delete()
    return Response({'success': True}, status=status.HTTP_200_OK)




'''
Filter Todo List by status or due_date
'''
@api_view(['GET'])
def filter_todo(request):
    status_param = request.query_params.get('status', None)
    due_date_param = request.query_params.get('due_date', None)
    queryset = Todo.objects.filter(author=request.user)

    if status_param:
        queryset = queryset.filter(status=status_param)

    if due_date_param:
        queryset = queryset.filter(due_date=due_date_param)

    serializer = TodoSerializer(queryset, many=True)

    return Response({
        'success': True,
        'data': serializer.data
    }, status=status.HTTP_200_OK)


'''
Mark Todo as Completed
'''
@api_view(['PATCH'])
def mark_todo_completed(request, id):
    try:
        todo = Todo.objects.get(id=id, author=request.user.id)
        if todo.status != 'completed':
            todo.status = 'completed'
            todo.save()
            serializer = TodoSerializer(todo)
            return Response({'success': True, 'data':serializer.data}, status=status.HTTP_200_OK)
        return Response({'success': False}, status=status.HTTP_304_NOT_MODIFIED)
    except Todo.DoesNotExist:
        return Response({'success': False, 'message': 'Todo not found'}, status=status.HTTP_404_NOT_FOUND)

'''
Update Due Date
'''
@api_view(['PATCH'])
def update_due_date(request, id):
    try:
        todo = Todo.objects.get(author=request.user.id, id=id)
        due_date = request.data.get('due_date')

        if not due_date:
            return Response({'error': 'Due date is required.'}, status=status.HTTP_400_BAD_REQUEST)

        todo.due_date = due_date
        todo.save()
        serializer = TodoSerializer(todo)
        return Response({'success': True, 'date': serializer.data}, status=status.HTTP_200_OK)
    except Todo.DoesNotExist:
        return Response({'error': 'Todo not found.'}, status=status.HTTP_404_NOT_FOUND)

'''
Create Bulk Todos at once
'''
@api_view(['POST'])
def create_bulk_todos(request):
    todos_data = request.data.get('todos', [])
    todos = []

    for todo in todos_data:
        serializer = TodoSerializer(data=todo)
        if serializer.is_valid():
            todo = serializer.save(author=request.user)
            todos.append(todo)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    todo_serializer = TodoSerializer(todos, many=True) 
    return Response({'success': True, 'data':todo_serializer.data}, status=status.HTTP_200_OK)


'''
Search Todo by Title 
'''
@api_view(['GET'])
def search_todos(request):
    query = request.query_params.get('q', '')
    if query:
        queryset = Todo.objects.filter(title__icontains=query, author=request.user)
    else:
        queryset = Todo.objects.filter(author=request.user)

    serializer = TodoSerializer(queryset, many=True)
    return Response({'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)



'''
Change Priority of Todo
'''
@api_view(['POST'])
def change_priority(request, id):
    try:
        todo = get_object_or_404(Todo, id=id, author=request.user)
        priority_to_change = request.data.get('priority')
        if priority_to_change:
            todo.priority = priority_to_change
            todo.save()
            serializer = TodoSerializer(todo)
            return Response({'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'success': False, 'message': 'Priority value is required'}, status=status.HTTP_400_BAD_REQUEST)
    except Todo.DoesNotExist:
        return Response({'error': 'Todo not found.'}, status=status.HTTP_404_NOT_FOUND)
    















