import json

def lambda_handler(event, context):
    # slackからの投稿を slack_input_text へ格納
    print("関数呼び出されsection")
    # print(type(event))
    # print(event.keys())
    print(event)

    # EventがPullRequestの時
    if ('pull_request' in event):
        print('PullRequestEventから呼ばれたよ！')

    # EventがPushsの時
    elif ('ref' in event):
        print('pushsEventから呼ばれたよ！')



    # PRがmergeされた時
    # if ()
    return {
        'statusCode': 200
    }
