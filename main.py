import json

def lambda_handler(event, context):
    # slackからの投稿を slack_input_text へ格納
    print("関数呼び出されsection")
    print(event)

    return {
        'statusCode': 200
    }
