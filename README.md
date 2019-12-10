# opsdroid skill news

A skill for [opsdroid](https://github.com/opsdroid/opsdroid) to tell you the latest news / headlines.

## Requirements

You need an api-key from [News API](https://newsapi.org/).

## Configuration

```yaml
skills:
  news:
    # Required
    result-count: 3
    api-key: da9856884bb68c53
```

## Usage

#### news/headlines

Opsdroid will tell you the URLs of the live top and breaking news on the internet.

> user: what is the headlines
>
> opsdroid: The top headlines are: 
>           "https://www.cnn.com/2019/12/10/americas/chile-air-force-plane-missing-intl-hnk/index.html"
>           "https://www.youtube.com/watch?v=3u2M9mbVVMc"
>           "https://www.engadget.com/2019/12/09/mlb-the-show-non-playstation-platforms-2021"

> user: what is the news on football
>
> opsdroid: The top news are: 
>           "http://www.fourfourtwo.com/news/football-rumours-media-90"
>           "https://www.ccn.com/new-xfl-uniforms-prove-vince-mcmahon-learned-from-2001-disaster/"

_Note: You can also use the command `what's the news` or `what's the headlines`._
