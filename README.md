GitHubで特定のラベルがついたPRの情報をSlackに流す。

## 欲しい機能
- コマンドでマージできるPR一覧を確認できる。
- PRがmergeできるようになったらSlackの特定の部屋に通知がいく。
- releaseしたPRのラベルをそれぞれ取得して、通知したい部屋に流す。
- 特定のラベルがついたリリースを特定の部屋に通知する。
- それぞれのPR情報（作成者、 レビュワー、 ラベル、 PRの名前、 PR詳細）を通知する
- 特定のチームが抱えるリポジトリの情報をすべて取得したい

## 基本設計
コマンドはなし。PRのリリースをトリガーに特定のSlack部屋にPR情報を通知する。


リリースされたPRの情報を取得するGitHub API
https://developer.github.com/v3/repos/releases/#get-the-latest-release

## 導入
### GitHub
トークンは必要ない。
導入したいリポジトリの`webhooks`に指定すればいいだけ。

```
- Payload URL    :  API Gatewayのエンドポイント
- Content type    application/json
- Secret :    空白
- Which events would you like to trigger this webhook?
   - Pull requests
   - Pushs

```

### Slackへの導入
以下のページから該当のワークスペースにbotを作成する。
https://api.slack.com/

`Bot user`から登録するBotを作成する。


作成したら、`OAuth & Permissions` の下にある`Scopes`から権限を追加する。
- Send messages as user
- Add a bot user with the username @github_release_info

できたら、`Install App to Workspace`を実行。

実行したら、そこの画面に表示されている
- OAuth Access Token
- Bot User OAuth Access Token

これらをメモしておく。

### Lambda Functionの作成
このリポジトリをzipにまとめ、Lambda関数にアップロードする。

環境変数に以下の値を入力。
- SLACK_OAUTH_ACCESS_TOKEN : SlackのOAuth Access Token
- SLACK_BOT_USER_ACCESS_TOKEN : SlackのBot User OAuth Access Token

webhookのドキュメント
https://developer.github.com/webhooks/
webhook pull requestsのドキュメント
https://developer.github.com/v3/activity/events/types/#pullrequestevent
web hook pushのドキュメント
https://developer.github.com/v3/activity/events/types/#pushevent

関数設計

payloadの先頭にactionカラムが入っているのが、PullRequestEvent(PRE)。
payloadの先頭にrefカラムが入っているのが、PushsEvent。

まずはmasterへのpushを検出する部分を実装する。
masterへのpushが行われた場合、以下の形になる。
'ref': 'refs/heads/master',

また、PREventでmergeを検出するのもあり。
マージされたタイミングのみを検出するには、以下の形が良さそう。
'action': 'closed' && 'merged': True,

送られてくるデータは辞書型。


運用ルール
- mergeしたPRには`Done`スタンプをつける
- そこの部屋に
- PRになるべくラベルをつけること

まとめると
mergeできるようになったPRのラベルを取得して、Slackの部屋に通知する。


メリット
PRにきちんとラベルをつける習慣が生まれることで、管理がしやすくなる。





## 参考文献
https://qiita.com/unsoluble_sugar/items/072c9740e258ee93ff9a