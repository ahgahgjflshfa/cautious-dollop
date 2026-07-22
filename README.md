# 小火箭配置檔

自動取得小火箭廣告阻擋規則，加入自訂路由規則後，產生可供小火箭訂閱的設定檔。

## 功能

- 每日8點自動取得上游規則
- 將 `custom-rules.txt` 內的規則插入 `[Rule]` 區段
- 自動加入 `FINAL,DIRECT`
- 透過 GitHub Actions 更新設定檔
- 自動提交更新結果至 `main` 分支

## 上游來源

```text
https://johnshall.github.io/Shadowrocket-ADBlock-Rules-Forever/sr_ad_only.conf
```

## 產生的設定檔

執行後會更新目錄中的

```text
sr_ad_only_custom.conf
```

## 訂閱

在小火箭中導入

```text
https://raw.githubusercontent.com/ahgahgjflshfa/cautious-dollop/main/sr_ad_only_custom.conf
```
