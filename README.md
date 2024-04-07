# go_cli

A command line interface to lookup train information.

```
<disclaimer>
This is a personal project, not affiliated with any organization, only use Open APIs
</disclaimer>
```

# THIS IS NOT READY TO BE USED BY ANYONE!

Uses [Open Data - GO API](http://api.openmetrolinx.com/OpenDataAPI/Help/Index/en) which links to [API Specification](http://api.openmetrolinx.com/OpenDataAPI/Content/API_Data_Catalogue.pdf).

## Before you start

You'll need the Open API key from Metrolinx which you request from http://api.openmetrolinx.com/OpenDataAPI/ and it only took a couple of days to receive via email.

### Dependencies

This code imports from the following pacakges so make sure you install those first.

- `requests` - for the REST calls
- `argparse` - for command line arguments

## Options

Option | Description
---|---
`-k` | Your GO API key. See the "Before you start" section.
`-s` | The Bus Stop or Train Station being queried e.g. "AP" for Appleby. See [go_api.py](./go_api.py) for the list of station codes.