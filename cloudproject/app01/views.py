from django.shortcuts import render
from django.http import JsonResponse
from .models import Vote
import datetime
import logging



from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Vote
import json

# 设置日志



# def vote(request):
#     if request.method == "POST":
#         # 获取投票选项
#         choice = request.POST.get("option")
#         print(choice)
#         # 获取对应的投票选项
#         # vote = Vote.objects.get(choice=choice)
#         new_vote = Vote.objects.create(choice='doge')
#         # 增加投票数
#         # vote.choice += 1
#         # vote.save()
#         new_vote.save()
#
#         # 获取当前投票数，返回给前端
#         # return render(request, 'cloudProjects/vote.html', {'vote': vote})
#
#     # GET请求时返回初始页面
#     return render(request, 'cloudProjects/vote.html')
# @csrf_exempt
# def vote(request):
#     print("2")
#     print(request.method)
#     # new_vote = Vote.objects.create(choice='doge')
#     # new_vote.save()
#
#     # if request.method == "POST":
#     if request.method == "POST":
#         print("1")
#         # 获取投票选项
#         # 获取请求体中的 JSON 数据
#         try:
#             data = json.loads(request.body)  # 将请求体解析为 JSON
#             option = data.get('option')  # 提取 "option" 字段的值
#             print(option)
#             if option=="dog":
#                 new_vote = Vote.objects.create(choice='doge')
#                 new_vote.save()
#             else:
#                 new_vote = Vote.objects.create(choice='cat')
#                 new_vote.save()
#
#         except json.JSONDecodeError:
#             return JsonResponse({'error': 'Invalid JSON'}, status=400)
#     new_vote = Vote.objects.create(choice='cat')#测试
#     new_vote.save()
#         # choice = request.POST.get("option")
#         # print(choice)
#         # # 获取对应的投票选项
#         # # vote = Vote.objects.get(choice=choice)
#         # new_vote = Vote.objects.create(choice='doge')
#         # # 增加投票数
#         # # vote.choice += 1
#         # # vote.save()
#         # new_vote.save()
#
#         # 获取当前投票数，返回给前端
#         # return render(request, 'cloudProjects/vote.html', {'vote': vote})
#
#     # GET请求时返回初始页面
#     return render(request, 'vote.html')






# Create your views here.
# def vote(request):
#
#     # return  render(request, 'cloudProjects/vote.html')
#     return render(request, 'cloudProjects/vote.html')

# def vote(request, choice):
#     # 验证用户点击的选项是否有效
#     if choice not in ['cats', 'dogs']:
#         return JsonResponse({'error': 'Invalid choice'}, status=400)
#
#     # 记录投票数据到 Vote 表
#     Vote.objects.create(choice=choice, timestamp=datetime.datetime.now())
#
#     # 记录按钮点击日志到 VoteLog 表
#     # VoteLog.objects.create(choice=choice, timestamp=datetime.datetime.now())
#
#     # 返回成功响应，通知前端
#     return JsonResponse({'message': 'Your vote has been recorded for ' + choice})
# def result(request):
#     return render(request, 'cloudProjects/result.html')

# @csrf_exempt  # 用于跳过 CSRF 验证（开发环境中可使用，生产环境中要小心）
# def handle_vote(request):
#     if request.method == 'POST':
#         try:
#             # 获取前端传递的 JSON 数据
#             data = json.loads(request.body)
#             option = data.get('option')
#
#             # 检查 option 是否有效
#             if not option:
#                 return JsonResponse({'error': 'No option provided'}, status=400)
#
#             # 尝试获取该选项对应的 Vote 对象，如果没有则创建新的选项
#             vote, created = Vote.objects.get_or_create(option=option)
#
#             # 更新投票数
#             vote.count += 1
#             vote.save()
#
#             # 返回更新后的投票数
#             return JsonResponse({'option': vote.option, 'count': vote.count})
#
#         except json.JSONDecodeError:
#             return JsonResponse({'error': 'Invalid JSON'}, status=400)
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)
#     else:
#         return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

#
# def vote_page(request):
#     # 获取当前投票数
#     vote = Vote.objects.first()
# #     return render(request, 'vote_page.html', {'vote': vote})
# def result(request):
#     return render(request, 'cloudProjects/result.html')


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import logging

# 用于存储投票结果的字典
# vote_count = {
#     'cat': 0,
#     'dog': 0,
#
# }

logger = logging.getLogger('myapp')
@csrf_exempt  # 禁用 CSRF 验证（仅用于示例，生产环境需要使用 CSRF 验证）
def sv(request):
    # print(logger.info('Vote option'))
    if request.method == 'POST':
        # 解析请求体中的 JSON 数据
        try:
            data = json.loads(request.body)
            option = data.get('option')
            # print("参数1")
            # print(option)
            if option == "dog":
                new_vote = Vote.objects.create(choice='dog')
                new_vote.save()
                print(option)
                logger.info(f'Vote option: {option}')
                # print(logger.info(f'Vote option: {option}'))
                print("ss")
                return JsonResponse({
                    'option': option,

                })
            else:
                new_vote = Vote.objects.create(choice='cat')
                new_vote.save()
                logger.info(f'Vote option: {option}')
                # print(logger.info("Vote option: cat"))
                print("oo")

        #     if option in vote_count:
        #         vote_count[option] += 1
        #         print(vote_count[option])
        #         print("sadadssa")
        #         # 返回投票结果
                return JsonResponse({
                    'option': option,

                })
        #
        #     else:
        #         return JsonResponse({'error': 'Invalid option'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    return render(request, 'vote.html')
    # else:
    #     return JsonResponse({'error': 'Invalid method'}, status=405)

from django.http import JsonResponse
import logging
from datetime import datetime
# logger = logging.getLogger('vote')
from django.utils import timezone
from datetime import datetime
# def log(request):
#     if request.method == 'POST':
#         # 获取前端传递的投票选项（cats 或 dogs）
#         try:
#             data = json.loads(request.body)
#             vote_option = data.get('option')
#
#             # 如果选项不是 cats 或 dogs，则返回错误信息
#             if vote_option not in ['cat', 'dog']:
#                 return JsonResponse({'message': 'Invalid vote option'}, status=400)
#
#             # 记录投票日志，包括点击时间和选择的选项
#             # naive_datetime = datetime.now()  # 这是 naive datetime
#             # aware_datetime = timezone.make_aware(naive_datetime)  # 转换为 aware datetime
#             log_message = f"Voted for {vote_option} at { datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
#             logger.info(log_message)  # 记录日志到 Docker 控制台
#             print("log_message")
#
#             # 返回成功的响应
#             return JsonResponse({'message': f'Vote for {vote_option} recorded successfully!', 'option': vote_option})
#
#         except ValueError:
#             return JsonResponse({'message': 'Invalid request data'}, status=400)
#
#     # 如果请求不是POST方法，返回错误
#     return JsonResponse({'message': 'Invalid request method'}, status=405)