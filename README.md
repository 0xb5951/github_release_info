GitHubで特定のラベルがついたPRの情報をSlackに流す。

## 欲しい機能
- コマンドでマージできるPR一覧を確認できる。
- PRがmergeできるようになったらSlackの特定の部屋に通知がいく。
- releaseしたPRのラベルをそれぞれ取得して、通知したい部屋に流す。
- 特定のラベルがついたリリースを特定の部屋に通知する。
- それぞれのPR情報(作成者, レビュワー, ラベル, PRの名前, PR詳細)を通知する
- 特定のチームが抱えるリポジトリの情報をすべて取得したい

## 基本設計
コマンドはなし。PRのリリースをトリガーに特定のSlack部屋にPR情報を通知する。


リリースされたPRの情報を取得するGitHub API
https://developer.github.com/v3/repos/releases/#get-the-latest-release

## 導入
### GitHub
以下にアクセスして、新規でリポジトリトークンを作成する。
https://github.com/settings/tokens/new

とりあえず`repo`の権限だけ付与しておく。Tokenは一度だけしか表示されないので、メモっておく。


運用ルール
- mergeしたPRには`Done`スタンプをつける
- そこの部屋に
- PRになるべくラベルをつけること

まとめると
mergeできるようになったPRのラベルを取得して、Slackの部屋に通知する.


メリット
PRにきちんとラベルをつける習慣が生まれることで、管理がしやすくなる.





## 参考文献
https://qiita.com/unsoluble_sugar/items/072c9740e258ee93ff9a