import json
import threading

from post_message_to_slack import post_message_to_slack, post_personal_message_to_slack

#  並列処理させてエラーを出にくくする
def lambda_function(event, content):
    thread_1 = threading.Thread(target=return_200)
    thread_2 = threading.Thread(target=main_func(event, content))
    return 0

# slackにとりあえず200を返す
def return_200():
    print("prodess kill")
    return 0


def lambda_handler(event, context):
    # slackからの投稿を slack_input_text へ格納
    print("関数呼び出されsection")
    # print(type(event))
    print(event.keys())
    print(event)

    # EventがPullRequestの時
    if ('pull_request' in event):
        print('PullRequestEventから呼ばれたよ！')
        action = event['action']
        PR = event['pull_request']

        # PRがmergeされた時
        if (action == 'edited' and PR['merged']):
            print('関数がマージされたよ。')

    # EventがPushsの時
    elif ('ref' in event):
        print('pushsEventから呼ばれたよ！')



    # PRがmergeされた時
    # if ()
    return {
        'statusCode': 200
    }
