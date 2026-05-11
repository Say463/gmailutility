# 概要

この機能（**Gmail-utility**）は、ユーザーのGmailアカウントから未読メールを取得し、重要度を自動的に判定してDiscordに通知する**個人利用向けツール**です。

### Setting (`Credential.json`の取得)

[Cloudプロジェクトの作成](https://developers.google.com/workspace/guides/create-project?hl=ja)及び[pythonクイックスタート](https://developers.google.com/workspace/gmail/api/quickstart/python?hl=ja#step_1_turn_on_the)を参照してください。  
その後ファイル内にダウンロードした`credential.json`を加えてください。


### Setting（Gmail）

 
1. このプロジェクトファイルをダウンロードし、cmdで`quickstart.py`を実行してください。  

2. お手持ちのGmailにログインすると、画面が遷移するので**詳細**をクリックしてください。その後、**Gmail-Utility(安全ではないページ)に移動**をクリックしてください。  
（この機能は、Googleによる認証を受けていませんが、認可に向けて鋭意改良中です。プライバシーポリシーに関しては、ファイル内のPLIVACY_POLICY.mdを参照してください。）
3. その後の遷移画面で、**続行**をクリックすると、ファイル内に`token.json`が生成されます。以上でgmail側の初期設定は完了です。

 ## Setting (Discord & yaml file)

  **ディスコードで新しいサーバーを立てることを推奨します。**
1. 通知を送ってほしいチャンネルを右クリックして、チャンネルの編集をクリックしてください。
2. 連携サービスから新しいウェブフックを作成してください。ウェブフック情報にある**ウェブフックURLをコピー**をクリックして、```config_example.yaml```にペーストしてください。
3. ```config_example.yaml```を構成してください。構成例は以下の通りです。この構成をそのままコピペしても構いません。keywordsに設定する`"○○": (数字)`は、thresholdを考慮して設定してください。  
例えば、IT企業という言葉に10点の重みをつけたい場合は、`"IT企業: 10"`と入力してください。その際はインデントに注意してください。

```yaml
discord:
  webhook_url: 'ここに自身で発行したwebhook-urlをペーストしてください。'
notifier:
  threshold: 90
  max_check: 10

scoring:

  keywords:
    "インターン": 45
    "スカウト": 45
    "就職": 45
    "採用": 45
    "人事": 45
    "コンテスト": 15
```

 ### 使用法
 以下の設定が終了したら、cmdで`main.py`を実行してください。  
 ```bash
 python main.py
 ```

 
