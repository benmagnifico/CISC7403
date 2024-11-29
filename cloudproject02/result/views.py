from django.db import connection
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
# def result(request):
#     with connection.cursor() as cursor:
#         cursor.execute("SELECT COUNT(*) FROM app01_vote WHERE choice = %s", ['cat'])
#         result = cursor.fetchone()
#         print(result)
#
#     return render(request, 'result.html')

def result(request):
    print(request.method)

    try:
        # 查询数据库中所有的投票选项
        # votes = Vote.objects.all()
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM vote WHERE choice = %s", ['cat'])
            resultc = cursor.fetchone()
            print(resultc[0])#猫
            cursor.execute("SELECT COUNT(*) FROM vote WHERE choice = %s", ['doge'])
            resultd = cursor.fetchone()#狗
            print(resultd[0])
    except:
        print("")

        # 假设这里是从数据库获取的投票数据，这里手动构造示例数据
    json_data = {
        'catVote': 1000,
        'dogVote': 10000,
        'catperc': 1,  # 格式化为 1 位小数
        'dogperc': 1,  # 格式化为 1 位小数
        'totalVote': 1
    }

    # 返回 JSON 数据
    return  render(request, 'results.html', {'json_data': json_data})
    # data = [
    #     {
    #         "catVote": 10, # 猫的投票数
    #         "dogVote": 20, # 狗的投票数
    #         "catperc": "33.3%", # 猫的投票占比
    #         "dogperc": "66.7%", # 狗的投票占比
    #         "totalVote": 30 # 总投票数
    # }
    # ]
    #
    # # 返回 JSON 格式的响应
    # return  render(request, 'results.html', {'data': data})



    #
    # json_data = {
    #     'catVote': cat_vote.vote_count if cat_vote else 0,
    #     'dogVote': dog_vote.vote_count if dog_vote else 0,
    #     'catperc': f"{cat_perc:.1f}%",  # 格式化为 1 位小数
    #     'dogperc': f"{dog_perc:.1f}%",  # 格式化为 1 位小数
    #     'totalVote': total_vote
    # }
    #
    # # 返回 JSON 数据
    # return JsonResponse(json_data)
















    #     # 构建一个包含所有投票结果的列表
    #     results = []
    #     for vote in votes:
    #         result.append({
    #             'option': vote.option,  # 投票选项
    #             'vote_count': vote.vote_count  # 投票数
    #         })
    #
    #     # 返回 JSON 格式的数据
    #     return JsonResponse(result, safe=False)  # safe=False 允许返回非字典的数据结构
    # except Exception as e:
    #     # 如果发生任何错误，返回错误信息
    #     return JsonResponse({'error': str(e)}, status=500)


def sample(request):

    try:
        # 查询数据库中所有的投票选项
        # votes = Vote.objects.all()
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM vote WHERE choice = %s", ['cat'])
            resultc = cursor.fetchone()

            # cursor.execute("SELECT choice, MAX(timestamp) AS latest_vote_time FROM app01_vote GROUP BY choice")
            # ORDER BY CASE WHEN choice = 'cat' THEN 1 WHEN choice = 'dog' THEN 2 ELSE 3 END;
            cursor.execute("SELECT choice, MAX(timestamp) AS latest_vote_time FROM vote GROUP BY choice ORDER BY CASE WHEN choice = 'cat' THEN 1 WHEN choice = 'dog' THEN 2 ELSE 3 END")


            alltime =cursor.fetchall()
            # if resultc is None:
            #     resultc=0;
            #     alltime[0][1]=''
            # print("all")
            # print(alltime[0][1])
            # print(alltime[1][1])
            #
            # print(resultc[0])  # 猫
            cursor.execute("SELECT COUNT(*) FROM vote WHERE choice = %s", ['dog'])
            resultd = cursor.fetchone()  # 狗
            print("ddog")
            # print(resultd.shape)
            # if resultd is None:
            #     resultd[0]=0;
            #     alltime[1][1]=''
            print(resultd[0])
            if resultc[0]==0 and resultd[0]==0:
                result = {
                    "catvote": 0,
                    "dogvote": 0,
                    "catpercent": "0%",
                    "dogpercent": "0%",
                    "total": 0,
                    "timeCat": "No data",
                    "timeDog": "No data"
                }
                return render(request, 'sample.html', {'results': result, })
            if resultc[0]==0 and resultd[0]!=0:
                result = {
                    "catvote": 0,
                    "dogvote": resultd[0],
                    "catpercent": "0%",
                    "dogpercent": "100%",
                    "total": resultd[0],
                    "timeCat": "No data",
                    "timeDog": alltime[1][1]
                }
                return render(request, 'sample.html', {'results': result, })
            if resultc[0]!=0 and resultd[0]==0:
                result = {
                    "catvote": resultc[0],
                    "dogvote": 0,
                    "catpercent": "100%",
                    "dogpercent": "0%",
                    "total": resultc[0],
                    "timeCat": alltime[0][1],
                    "timeDog": "No data"
                }
                return render(request, 'sample.html', {'results': result, })

    except Exception as e:
        print("")
        # print(f"Error occurred: {e}")

    result={
        "catvote":resultc[0],
        "dogvote":resultd[0],
        "catpercent":str(round((resultc[0]/(resultc[0]+resultd[0])*100), 2))+"%",
        "dogpercent": str(round((1-(resultc[0]/(resultc[0]+resultd[0])))*100,2))+"%",
        "total": resultc[0]+resultd[0],
        "timeCat":alltime[0][1],
        "timeDog":alltime[1][1]
#"SELECT choice, MAX(timestamp) AS latest_vote_time FROM app01_vote GROUP BY choice"
    }

    return render(request, 'sample.html', {'results': result,})
