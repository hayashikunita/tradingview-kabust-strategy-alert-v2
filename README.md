# tradingview-kabust-strategy-alert-v2
  
**kabuステーションAPIとTradingviewのWebhookを繋げ売買の自動化を行います。**
 
# DEMO
 
Tradingviewから送信したWebhookを当サイトで受け取り、売買情報をAPIでPOSTします。
 
# Features
 
今までは、トレーディングアプリを用いて、価格情報などをGETし、データベースに格納し、ストラテジーを当てはめていましたが、多様なプラットフォームの登場により、売買のPOSTのみになりました。
 
# Requirement
 
Flask==2.1.2<br>
 
# Installation

pip install flask<br>
 
# Usage
  
```bash
git clone https://github.com/~~~~~
cd 当ディレクトリ
python app.py
```
ローカル環境では、コメントアウトを外してください。
 
# Note
 
 
まず参考にしたYoutubechennelがあります。まず、こちらをご覧ください。
https://www.youtube.com/watch?app=desktop&v=gMRee2srpe8

もし間違っている点や、省略可能なところがございましたら、ご教授のほど宜しくお願いします。

また、売買に生じるコストや損益は、責任を負いません。<br>
また、セキュリティなどに関しては、責任を負いません。<br>
また、最終的な投資決定は、お客さまご自身の判断でなさるようにお願いいたします。<br>
また、現在は、buy or sellとposition_sizeのみdataを与えていますが、PinescriptやPythonでは様々なやり方があるはずですので、ご自身で変更をお願いします。<br>
また、Tradingviewのwebhookでは、30秒ほど遅延が起こります。これはTradingview側のプランによってスピードが変わる設定になっています。ご自身で変更をお願いします。Premiumでは3秒ほどの遅延が生じます。<br>
また、PythonでRealtimeTickerを取得し、売買する方法もございます。そちらの方が、売買の高速化は可能です。<br>
また、kabuステーションAPIでは、Windowsでしか利用できません。また、kabuステーションという専用のアプリが必要であり、kabuステーション®API利用設定をONにする必要があります。
また、kabuステーションAPIの利用については、こちらの公式ドキュメントをご覧ください。https://kabucom.github.io/kabusapi/ptal/index.html
また、auカブコム証券のAPIは、ローカルに立ち上げた上記のアプリケーションを中継することで動作し、毎日自動的にログアウトされ、自動売買には適さないとされており、以下のサイトをご参考ください<br>
https://www.kojinteki.net/2020/09/19/kabucom-auto-login/
また、ngrokを使用する場合、登録が必要。https://ngrok.com/

# License
 
This is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
