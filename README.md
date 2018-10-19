# prom2teams

## Docker

Test the container:

``` Bash
curl -vX POST http://localhost:8699 -d @tests/test_processor/alert.json --header "Content-Type: application/json"
```