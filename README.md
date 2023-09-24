# PyxelUniversalFont

PyxelUniversalFontは、公開されている"pyxel"ライブラリにフォントを追加するための拡張ツールです。

## 目次

- [機能](#機能)
- [インストール方法](#インストール方法)
- [使用方法](#使用方法)
- [サポートしているフォント](#サポートしているフォント)
- [コマンド一覧](#コマンド一覧)

## 機能

- pyxelで使える追加のフォントを簡単にインストール
- カスタムフォントの追加サポート
- pyxelのゲームやアプリケーションでの文字表示を綺麗に、多様に

## インストール方法

```bash
pip install PyxelUniversalFont
```

その後、pyxelのプロジェクト内で以下のようにインポートしてください。

```python
import PyxelUniversalFont
```

## 使用方法

```python
import pyxel
import PyxelUniversalFont as puf

class App:
    def __init__(self) -> None:
        pyxel.init(500, 100)
        
        # フォントを指定
        self.writer = puf.Writer("IPA_Gothic")
        
        pyxel.run(self.update, self.draw)
        
    def update(self):
        pass
    
    def draw(self):
        pyxel.cls(7)

        # draw(x座標, y座標, テキスト, フォントサイズ, 色, 背景色)
        self.writer.draw(0, 0, "こんにちは、世界！", 48, 0, 7)

if __name__ == "__main__": 
    App()
```

## サポートしているフォント

以下は、デフォルトでサポートされているフォントです。

- IPA ゴシック
- IPA Pゴシック
- IPA 明朝
- IPA P明朝

次のコマンドで開かれるディレクトリに、任意のフォントを追加できます。
```bash
puf edit
```

## コマンド一覧

1. サンプルアプリケーションの起動:
    ```bash
    puf sample
    ```
2. フォント保存用ディレクトリを開く:
    ```bash
    puf edit
    ```

