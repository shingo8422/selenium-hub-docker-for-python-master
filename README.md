# Docker+Python+Selenium+Chromeの環境を構築

### 環境構築手順

~~~
# docker-compose build
# docker-compose up -d
~~~

### VNC Viewerのインストール

画面上での確認が必要な場合は、[VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/)をインストールしておいてください  
VNC Viewerを起動したら、`localhost:5900`で接続することで、テスト画面を表示できます 。  
パスワードは`secret`です。

### テスト実行

~~~
headlessモード(画面上で確認が必要でない場合)
# docker-compose exec app python headless-test-sample.py

selenium-hubモード(画面上での確認が必要な場合)
// VNC Viewerでテスト画面を表示しておいてください。
# docker-compose exec app python selenium-hub-sample.py
~~~

### 注意事項

DockerfileでGoogleChromeとchromedriverをインストールしていますが  
GoogleChromeの方はバージョンを指定してインストールすることができないため、 
安定版をインストールしています。  

そのためchromedriverのバージョンと相違する可能性があります。  
その場合は、[Dockerfile](https://github.com/shingo8422/selenium-hub-docker-for-python/blob/122a7124c88a750c17e47dacba19815c51421b32/docker/python/Dockerfile#L17)
の１７行目をstableのバージョンに合わせてください。  
