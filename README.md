# telegram-downloader
Download all content from a Telegram channel.

## Motivation 
When you know a channel which continously shares content of interest, you may want to store them on your computer. 
It is also useful as the channel, or the app itself, may shut down at some point. 

## Usage
The program is targeted for channels which provide media such as documents, audio files, videos or pictures.
In this design, it is rather not suitable for plain text messages.

## Procedure
To use this program, it is beforehand required to have an API ID and an API hash which you can get from https://core.telegram.org/api/obtaining_api_id#obtaining-api-id. After that:

1. Set the folder where you want the files to be downloaded.
2. Paste your API ID and API hash in the designated fields.
3. Type in the channel name under the variable `channel`. Pasting the full link such as https://t.me/channelname works too.
4. Set the value for `limit` which indicates how many files you want to download. It downloads in order from the most recent one. Set `None` if you want to get all.
5. After starting the program, you may be prompted to enter your telephone number. Enter it with international format such as +49123456789 . Telegram sends you then a code which you then must enter too.
    
The program downloads all but checks if media is already present in the folder (it may have been downloaded before). If it is present, it is skipped.

## Development setup

Required external libraries are
- Telethon: https://github.com/LonamiWebs/Telethon

```sh
pip install telethon
```

## Meta

Author: Jonas Dossmann

Distributed under the AGPL-3.0 license.

[https://github.com/dossma/](https://github.com/dossma/)

<!-- Markdown link & img dfn's -->
[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dossma/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dossma/node-datadog-metrics
[wiki]: https://github.com/dossma/ebook-file-renaming/wiki
