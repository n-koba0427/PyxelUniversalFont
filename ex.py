import pyxel
import PyxelUniversalFont as puf

pyxel.init(500, 50)

# フォントを指定
writer = puf.Writer("misaki_gothic.ttf")

pyxel.cls(7)

# draw(x座標, y座標, テキスト, フォントサイズ, 文字の色)
# 背景色はデフォルト値(-1:透明)
writer.draw(25, 4, "PyselUniversalFont", 50, 16)

pyxel.show()