# TravelBot
Travel Spot search system through Dialogue in Japanese.

## Overview

## Description

## Example Dialogue

```
S：何名様でご旅行予定ですか？
U：だいたい、3～4名くらいですね
S：時期はいつごろとかありますか？
U：そうですね、だいたいシルバーウィークくらいで。
S：どのあたりに行ってみたいとかありますか？
U：そうですね、特段どうこうというのはないんですけど、関東近郊くらいで。一泊2日で考えているんですけども
S：たとえば海の方に行きたいとか山の方に行きたいとかありますか？
U：海と山では山の方に行ってみたいかな
S：ではこのあたりはいったことがありますか？
U：そこにはいったことがあります
S：ではここはどうでしょうか
U：いったことはありません
S：でしたらお勧めですよ。○○も周りにありますよ。
```

## Requirement

* Python3.5
* virtualenv


Set Docomo and SLACK API Key to environment variables.

```
$ export DOCOMO_DIALOGUE_API_KEY=xxxxxxxx
$ export SLACK_API_KEY=xxxxxxxx
```

Set PYTHONPATH to environment variables.

```
$ cd TravelBot
$ export PYTHONPATH=`pwd`
```

## Usage
First, move to application directory. 

```
$ cd application
```

If you want to start slack bot, Then execute following command.

```
$ python slack_bot.py
```

If you want to start websocket server, Then execute following command.

```
$ python server.py
```

## Install

```
$ pip install -r requirements.txt
```

## Licence

[MIT](https://github.com/Hironsan/TravelBot/blob/master/LICENSE)

## Author

[Hironsan](https://github.com/Hironsan)