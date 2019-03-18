import json

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

        # print(PR.keys())
        # print(PR['merged'])
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
