# api

## ファイル構造

- `/api`: API Server
- `/greet`: 呼び出すライブラリ

## 実行方法

### 初期化
```bash
$ rye sync
```


### API Server の起動
```bash
$ rye run python -m api    
```

テストするとき
```
$ curl http://127.0.0.1:8000 
```

ドキュメント(swagger)を見るとき (HTMLを出力)
```
$ curl http://127.0.0.1:8000/docs
```

### ライブラリ単体の実行

```bash
$ rye run python -m greet
```

### ライブラリのテスト

```bash
$ rye run pytest
```

テストは失敗すると思う
